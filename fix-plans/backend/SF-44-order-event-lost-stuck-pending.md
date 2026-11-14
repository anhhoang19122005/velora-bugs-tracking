# SF-44: Mất event thì đơn kẹt PENDING mãi, không giữ hàng và không bị hủy

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major (chưa tái hiện, phát hiện khi đọc code; có thể điều chỉnh) |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend` (`order-service`), số dòng theo `develop` `e090ed4` |
| **Nhánh đề xuất** | `fix/order-stuck-pending-reconcile-sf-44`, tách từ `develop`. Nên làm sau SF-38 vì hoàn lượt mã dùng chung endpoint của SF-38 |
| **Khối lượng** | Khoảng 40 dòng code, 1 truy vấn mới, `@EnableScheduling`, 4 unit test, 1 integration test |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-44). Liên quan [SF-37](../storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) (mục Message broker) và [SF-38](SF-38-promotion-usage-over-redeemed.md) |

## Hiện tượng

Một đơn đã commit nhưng `OrderPlacedEvent` không tới được inventory-service thì đơn ở trạng thái `PENDING`, `stockReserved = false` mãi. Không có hàng được giữ, không có bước nào hủy đơn, và không ai được báo.

**Chưa tái hiện.** Phát hiện khi đọc code ngày 14/11 trong lúc kiểm tra vai trò của RabbitMQ trong SF-37. Tại thời điểm đó `GET /api/v1/orders?status=PENDING` trả 0 đơn, tức là chưa có đơn kẹt nào trong dữ liệu local. Cần một lần tái hiện có chủ đích (ví dụ chặn kết nối RabbitMQ của order-service lúc đặt hàng) trước khi sửa, để xác nhận đúng hành vi.

## Nguyên nhân

1. `EventPublisher.publishAfterCommit` gửi event sau khi commit, và `send` bắt mọi lỗi rồi chỉ ghi log, không ném (`messaging/EventPublisher.java`). Comment trong code ghi đây là chủ ý, để sự cố Rabbit không làm hỏng giao dịch đã commit.
2. Gửi xong là quên: order-service không có bảng outbox, không bật publisher confirm (chỉ payment-service có `publisher-confirm-type: correlated`), và không có tác vụ định kỳ nào (đã tìm `@Scheduled`: chỉ có ở gateway, payment-service, tracking-service; `OrderServiceApplication` không có `@EnableScheduling`).
3. Hai trường hợp làm event không tới nơi:
   - Broker không nhận (mất kết nối, hết hạn mức): `send` ghi log lỗi và bỏ.
   - Tiến trình `order-service` chết ngay sau commit và trước `afterCommit`: event chưa từng được gửi.
4. Mọi lối thoát khỏi `PENDING` đều cần một event đi tới: `handleStockReserved` (thành công hoặc thất bại), `handlePaymentCompleted`, `handlePaymentFailed`. Không có đường nào dựa vào thời gian.

payment-service đã có đúng loại bảo vệ này (`PaymentOutboxScheduler` chạy mỗi 5 phút), nên hai service đang xử lý khác nhau.

## Hệ quả

- Khách thấy đơn "Chờ xác nhận" mãi. Với Idempotency-Key của SF-37, bấm đặt lại chỉ trả về chính đơn kẹt đó.
- Đơn có mã giảm giá giữ luôn lượt mã (SF-38 giữ lượt ngay lúc đặt).
- Đơn VNPay bỏ dở ở cổng thanh toán cũng ở `PENDING` vô thời hạn và giữ hàng đã đặt (cùng cách sửa).
- Hàng đã giữ cho đơn kẹt (khi chỉ mất `StockReservedEvent`) không được trả về kho.

## Thay đổi

Thêm một tác vụ định kỳ trong `order-service`. Làm vậy an toàn vì cả hai đầu đã idempotent (đã đọc lại ngày 14/11):

- inventory bỏ qua `OrderPlacedEvent` nhận lặp nhờ bảng `processed_order_reservations` (`order_id` UNIQUE) và vẫn gửi lại `StockReservedEvent` (`StockReservationServiceImpl.java:34-40`, `OrderPlacedEventListener`), nên phát lại sửa được cả trường hợp mất `StockReservedEvent`.
- `handleStockReservedSuccess` chỉ xử lý khi đơn còn `PENDING` và chưa đánh dấu `stockReserved` (`OrderServiceImpl.java:572-575`).

### 1. Truy vấn

`repository/OrderRepository.java`:

```java
    // Orders still waiting on the saga after a grace period; used to republish lost events or expire them.
    List<Order> findByStatusAndCreatedAtBefore(OrderStatus status, Instant before);
```

### 2. Hàm điều phối trong `OrderServiceImpl`

Thêm vào interface `OrderService`: `void reconcileStuckOrders();`

```java
    private static final Duration REPUBLISH_AFTER = Duration.ofMinutes(2);
    private static final Duration EXPIRE_AFTER = Duration.ofMinutes(30);

    @Override
    @Transactional
    public void reconcileStuckOrders() {
        Instant now = Instant.now();
        for (Order order : orderRepository.findByStatusAndCreatedAtBefore(OrderStatus.PENDING, now.minus(REPUBLISH_AFTER))) {
            if (order.getCreatedAt().isBefore(now.minus(EXPIRE_AFTER))) {
                // Cancels, flips a paid order to REFUNDED, publishes OrderCancelledEvent (stock) and, after SF-38, gives the promotion back.
                handleStockReservedFailure(order, "Order expired while PENDING");
            } else if (!order.isStockReserved()) {
                // Inventory skips an order it already reserved and just answers again, so a repeat only repairs a lost event.
                publishOrderPlaced(order);
            }
        }
    }
```

### 3. Tác vụ định kỳ

`OrderServiceApplication.java`: thêm `@EnableScheduling`.

`scheduler/StuckOrderReconciler.java`:

```java
@Component
@RequiredArgsConstructor
@Slf4j
public class StuckOrderReconciler {
    private final OrderService orderService;

    @Scheduled(fixedDelayString = "${app.orders.reconcile-ms:60000}")
    public void run() {
        try {
            orderService.reconcileStuckOrders();
        } catch (Exception e) {
            log.error("Reconciling stuck orders failed", e); // next run tries again
        }
    }
}
```

**Vì sao:**

- Một lần quét làm hai việc nhỏ và độc lập: phát lại event cho đơn quá 2 phút chưa giữ hàng, và hủy đơn `PENDING` quá 30 phút.
- Hủy đơn dùng lại `handleStockReservedFailure` (dòng 586-595), đã xử lý đủ: đổi trạng thái, đánh dấu hoàn nếu đã thanh toán, gửi `OrderCancelledEvent` để inventory trả hàng. Khi SF-38 xong, hoàn lượt mã cũng nằm trong nhánh hủy hệ thống đó, nên đơn kẹt không còn giữ lượt.
- Dùng `fixedDelay` để hai lần quét không chồng nhau trên một instance.
- Ngưỡng 2 phút và 30 phút để cấu hình được, mặc định như trên.

### Lưu ý khi chọn ngưỡng 30 phút

- payment-service không đặt `vnp_ExpireDate` (đã tìm trong code), nên thời hạn phiên thanh toán do VNPay quyết định (thường 15 phút, chưa kiểm chứng). Nên đặt `vnp_ExpireDate` rõ ràng để ngưỡng hủy luôn lớn hơn nó.
- Nếu khách thanh toán sau khi đơn đã bị hủy, `handlePaymentCompleted` bỏ qua vì đơn không còn `PENDING` (dòng 605-607) và tiền đã bị trừ mà không có đơn. Rủi ro này đã tồn tại khi khách tự hủy đơn VNPay rồi vẫn thanh toán; plan này làm nó có thể xảy ra thêm khi quá hạn, nên cần quyết định có hoàn tiền tự động hay không (ngoài phạm vi).

## Các trường hợp đã cover

| # | Tình huống | Cơ chế xử lý | Kết quả | Kiểm bằng |
|---|---|---|---|---|
| 1 | Mất `OrderPlacedEvent` (broker lỗi hoặc tiến trình chết sau commit) | Quét sau 2 phút, phát lại event | inventory giữ hàng, đơn thành CONFIRMED (COD) | IT mới; kiểm thử lại thủ công |
| 2 | Mất `StockReservedEvent` (inventory gửi lỗi) | Phát lại `OrderPlacedEvent`, inventory nhận ra đã giữ và gửi lại `StockReservedEvent` | Đơn thành CONFIRMED, không giữ hàng hai lần | Unit `reconcile_republishesOrderNotYetReserved` |
| 3 | Event vẫn mất sau nhiều lần quét | Quá 30 phút thì hủy đơn | Đơn CANCELLED, hàng được trả (nếu có giữ), lượt mã được hoàn (sau SF-38) | Unit `reconcile_expiresOrderPendingTooLong` |
| 4 | Đơn VNPay bỏ dở ở cổng thanh toán | Quá 30 phút thì hủy | Đơn CANCELLED, lượt mã được hoàn | Như dòng 3 |
| 5 | Đơn đã CONFIRMED, CANCELLED hoặc trạng thái khác | Truy vấn chỉ lấy `PENDING` | Không bị đụng tới | Unit `reconcile_ignoresOrdersNotPending` |
| 6 | Đơn mới tạo (dưới 2 phút) | Chưa tới ngưỡng | Không phát lại sớm, tránh đua với event đang đi | Unit `reconcile_ignoresOrdersYoungerThanGrace` |
| 7 | Phát lại trong lúc event gốc vẫn đang được xử lý | Cả hai đầu idempotent | Không giữ hàng hai lần, không đổi trạng thái hai lần | Đã đọc code (xem trên); IT kiểm số lô đã giữ không đổi |
| 8 | Quét chạy lỗi (DB hoặc Rabbit) | Bắt lỗi, ghi log, lần sau chạy lại | Không làm sập ứng dụng | Unit |

### Chưa cover (biết trước)

| # | Tình huống | Hệ quả | Hướng xử lý nếu cần |
|---|---|---|---|
| A | Nhiều instance `order-service` cùng quét | Cùng một đơn có thể bị hủy hai lần; khóa lạc quan (`@Version`) làm một bên thất bại (SF-41), không sai dữ liệu | Thêm ShedLock nếu chạy nhiều instance |
| B | Event bị mất ở phía khác: `PaymentCompletedEvent`, `PaymentFailedEvent`, `OrderCancelledEvent` | Đơn VNPay đã thanh toán nhưng event mất vẫn kẹt `PENDING` rồi bị hủy sau 30 phút dù khách đã trả tiền | payment-service có outbox lo phần của nó; cần kiểm tra thêm. Nguy hiểm vì tiền đã trừ |
| C | `OrderCancelledEvent` mất thì hàng không được trả | Tồn kho thấp hơn thực tế | Quét thêm các đơn `CANCELLED` còn ledger giữ hàng, ngoài phạm vi |
| D | Listener của order-service ném lỗi thì bị giao lại liên tục (mặc định Spring AMQP, chưa kiểm chứng); listener của inventory nuốt lỗi | Kẹt hàng đợi hoặc mất lần trả hàng | Cấu hình dead-letter và retry; xử lý riêng |
| E | Bảng outbox thay cho tác vụ quét | Chính xác hơn nhưng tốn công | Chỉ làm nếu tác vụ quét không đủ |

## Test

**`OrderServiceTest`** (stub `orderRepository.findByStatusAndCreatedAtBefore`)
- `reconcile_republishesOrderNotYetReserved`
- `reconcile_expiresOrderPendingTooLong`
- `reconcile_ignoresOrdersNotPending`
- `reconcile_ignoresOrdersYoungerThanGrace`

**`CartAndOrderIT`**
- `reconcile_orderStuckPending_isRepublishedOnce`: tạo đơn rồi đặt `createdAt` lùi 5 phút bằng truy vấn, `stockReserved = false`, gọi `reconcileStuckOrders()`, kiểm tra `EventPublisher` được gọi đúng một lần cho đơn đó.

## Kiểm thử lại

1. **Tái hiện trước khi sửa:** chặn kết nối RabbitMQ của order-service (hoặc dùng cấu hình sai host) rồi đặt một đơn COD: đơn ở `PENDING`, `stockReserved = false` và không bao giờ chuyển trạng thái.
2. **Sau khi sửa, mất `OrderPlacedEvent`:** làm như trên, khôi phục kết nối, đợi quá 2 phút: đơn thành `CONFIRMED`, tồn kho giảm đúng một lần.
3. **Mất `StockReservedEvent`:** hủy hàng đợi của order-service tạm thời, đặt đơn, khôi phục: đơn thành `CONFIRMED`, tồn kho không giảm hai lần.
4. **Đơn bỏ dở:** đặt đơn VNPay, bỏ ở cổng thanh toán, đợi quá 30 phút: đơn `CANCELLED`, hàng được trả, lượt mã (nếu có) được hoàn.
5. Chạy lại kịch bản 1 đến 3 và các kịch bản mã giảm giá ở trang Storefront-Bất biến để chắc chắn tác vụ quét không phá luồng bình thường.
6. `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `order-service`.

## Tuân thủ quy tắc

Java 4 dấu cách, Spotless. Không đổi API công khai, không cần sinh lại contract. Cấu hình mới `app.orders.reconcile-ms` có giá trị mặc định, nên không cần đặt biến môi trường.

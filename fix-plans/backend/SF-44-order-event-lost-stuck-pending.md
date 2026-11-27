# SF-44: Mất event thì đơn kẹt PENDING mãi, không giữ hàng và không bị hủy

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major (chưa tái hiện, phát hiện khi đọc code; có thể điều chỉnh) |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend` (`order-service`, `inventory-service`, `payment-service`), đối chiếu `develop` `d5b6ac2` |
| **Nhánh đề xuất** | `fix/order-stuck-pending-reconcile-sf-44`, tách từ `develop`. Nên làm sau SF-38 vì hoàn lượt mã dùng chung endpoint của SF-38 |
| **Khối lượng** | Tách khôi phục giữ hàng khỏi nhánh hết hạn. Nhánh hết hạn cần đối soát thanh toán. |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-44). Liên quan [SF-37](../storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) (mục Message broker) và [SF-38](SF-38-promotion-usage-over-redeemed.md) |

## Hiện tượng

Một đơn đã commit nhưng `OrderPlacedEvent` không tới được inventory-service thì đơn ở trạng thái `PENDING`, `stockReserved = false` mãi. Hàng chưa được giữ. Nếu sự kiện không được gửi lại hoặc người dùng không hủy, đơn có thể tiếp tục chờ.

**Chưa tái hiện.** Phát hiện khi đọc code ngày 14/11 trong lúc kiểm tra vai trò của RabbitMQ trong SF-37. Tại thời điểm đó `GET /api/v1/orders?status=PENDING` trả 0 đơn, tức là chưa có đơn kẹt nào trong dữ liệu local. Cần một lần tái hiện có chủ đích (ví dụ chặn kết nối RabbitMQ của order-service lúc đặt hàng) trước khi sửa, để xác nhận đúng hành vi.

## Nguyên nhân

`order-service` gửi `OrderPlacedEvent` sau khi commit và chỉ ghi log nếu gửi lỗi. Chưa thấy bản ghi gửi lại hoặc tác vụ xử lý đơn kẹt trong luồng này. Outbox của payment-service xử lý sự kiện thanh toán.

## Thiết kế đề xuất

1. **Lưu sự kiện cùng đơn.** Ghi `OrderPlacedEvent` vào outbox trong cùng `@Transactional` với đơn. Outbox là bảng lưu sự kiện cần gửi để tiến trình khác có thể gửi lại sau khi lỗi. Tham chiếu `PaymentOutboxScheduler` và publisher confirm. Chỉ đánh dấu đã gửi sau khi RabbitMQ xác nhận. Dùng lại contract event nếu payload đủ. Inventory tiếp tục chống giữ hàng lặp theo ID đơn.
2. **Đối soát đơn cũ hoặc thiếu phản hồi.** Quét `PENDING` chưa có kết quả sau ngưỡng chờ. Kiểm lại trạng thái trước khi phát lại theo ID đơn. Kiểm sự kiện đến muộn sau hủy để kho không giữ lại hàng.
3. **Xử lý hết hạn riêng.** Hai phút để bắt đầu đối soát và 30 phút để bắt đầu kiểm tra hết hạn là ngưỡng đề xuất. Với đơn có thanh toán qua cổng hoặc chuyển khoản, đối soát payment-service trước khi hủy. Nếu đã nhận tiền, khôi phục hoặc xử lý theo luồng thanh toán hiện tại. Nếu chưa rõ tình trạng tiền hoặc service không phản hồi, giữ đơn để thử lại. Chỉ tự hủy khi đã xác nhận phiên thanh toán hết hiệu lực và chưa thu tiền. Việc hết hạn và xác nhận thanh toán cần có quy tắc xử lý tranh chấp để khoản thanh toán đến giữa hai bước không bị bỏ sót.
4. **Tiền và kho sau khi hủy.** Với đơn đã trả tiền mà nghiệp vụ quyết định hủy, dùng luồng hiện tại để mở khoản hoàn và chuyển `REFUND_PENDING`. Chỉ ghi `REFUNDED` khi đã ghi nhận hoàn đủ tiền. Trả kho và hoàn lượt mã phải có khả năng thử lại theo ID đơn. Phối hợp [SF-38](SF-38-promotion-usage-over-redeemed.md) cho phần lượt mã.

## Code dự kiến

Trong giao dịch tạo đơn, ghi outbox ngay sau khi có ID đơn. Worker claim từng bản ghi, publish bằng mô hình xác nhận của PaymentOutboxScheduler rồi đánh dấu đã gửi sau confirm. Nếu worker chết sau confirm, consumer nhận lại theo cùng ID đơn.

```java
var savedOrder = orderRepository.save(order);
outboxRepository.save(OrderOutbox.pending(
    savedOrder.getId(), buildOrderPlacedEvent(savedOrder)));
return orderMapper.toResponse(savedOrder);
```

## Kiểm thử cần có

| Tình huống | Kết quả mong đợi |
|---|---|
| Tiến trình dừng giữa commit và gửi, hoặc RabbitMQ chưa xác nhận | Bản ghi outbox còn chờ và được gửi khi khôi phục. |
| Mất `OrderPlacedEvent` hoặc `StockReservedEvent` | Sau phát lại, đơn COD hợp lệ được xác nhận. Kho chỉ giảm một lần. |
| Sự kiện phát lại đến sau khi đơn đã hủy | Kho không bị giữ lại cho đơn đã hủy. |
| Nhiều worker quét cùng đơn hoặc callback đến lúc kiểm tra hết hạn | Mỗi tác dụng phụ đúng một lần. Đọc lại trạng thái trước khi chuyển. |
| Payment-service đã nhận tiền nhưng order-service chưa nhận sự kiện | Đối soát và khôi phục hoặc mở khoản hoàn theo nghiệp vụ. |
| Payment-service lỗi hoặc chưa rõ đã nhận tiền | Chưa tự hủy. Ghi nhận để thử lại. |
| Phiên thanh toán hết hạn, xác nhận chưa thu tiền | Hủy đơn. Hoàn kho và lượt mã nếu đã giữ. |
| Hủy đơn đã trả tiền theo quy tắc nghiệp vụ | `REFUND_PENDING` cho tới khi ghi nhận chi trả đủ. |

Chưa tái hiện sự cố mất sự kiện trong lần rà này. Khi triển khai cần kiểm thử mất sự kiện và đối soát thanh toán trên môi trường test cô lập.

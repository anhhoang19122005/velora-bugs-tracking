# SF-40: Gửi đồng thời tạo nhiều yêu cầu đổi trả cho cùng một cuốn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend` (`order-service`), số dòng theo `develop` `e090ed4` |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38-40`, chung nhánh với SF-37, SF-38 |
| **Khối lượng** | Khoảng 8 dòng code, 1 integration test |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-40) và Storefront-Bất biến (kịch bản 10 đến 14) |

## Hiện tượng

Đơn 57 đã hoàn tất, có 1 cuốn. Gửi 5 request `POST /api/v1/returns` cho cùng dòng hàng cùng lúc thì cả 5 yêu cầu được tạo (RMA-20261114-000006 đến -000010). Cả 5 đều duyệt và nhận hàng được. Dòng hàng ghi `returnedQuantity` 5 trên số lượng 1. **Mỗi yêu cầu có `refundAmount` 193.000 đ, bằng toàn bộ tiền đơn**, tổng ghi nhận hoàn 965.000 đ cho đơn 193.000 đ. Hiện payment-service không nghe `OrderReturnedEvent` (chỉ notification-service nghe), nên chưa có tiền bị chuyển tự động. Nhưng số liệu hoàn tiền đã sai, và việc hoàn tiền thủ công dựa trên số này sẽ sai theo. Gửi lần lượt thì yêu cầu thứ hai bị 409.

## Nguyên nhân

`ReturnRequestServiceImpl.create` (dòng 78-118) kiểm tra rồi mới ghi, không khóa:

- Dòng 93-97: kiểm tra đã có yêu cầu PENDING hoặc APPROVED cho đơn chưa.
- Dòng 155-159: kiểm tra số lượng còn trả được (`sumActiveReturnedQtyByOrderDetailId`).
- Dòng 192-197: tính tiền hoàn trên phần tiền còn lại (`sumRefundAmountByOrderIdActive`).

Các transaction chạy song song không thấy bản ghi chưa commit của nhau, nên cả 5 đều qua cả ba bước kiểm tra và đều tính tiền hoàn là toàn bộ đơn. `approve` (dòng 218-229) và `markReceived` (dòng 244-266) không kiểm tra lại số lượng, nên các bản trùng đi được đến cuối.

## Thay đổi

Khóa dòng đơn hàng trong lúc tạo yêu cầu, để các lần tạo cho cùng một đơn chạy lần lượt.

`services/order-service/src/main/java/vn/edu/iuh/fit/taschen/order/repository/OrderRepository.java`, cạnh `findByIdAndUserId` (dòng 31):

```java
    // Serialises return creation per order: the active-return and returnable-quantity checks in
    // ReturnRequestServiceImpl#create must see each other's inserts.
    @Lock(LockModeType.PESSIMISTIC_WRITE)
    @Query("SELECT o FROM Order o WHERE o.id = :id AND o.userId = :userId")
    Optional<Order> findByIdAndUserIdForUpdate(@Param("id") Long id, @Param("userId") Long userId);
```

`ReturnRequestServiceImpl.java:81-82`:

```diff
         Order order = orderRepository
-                .findByIdAndUserId(request.orderId(), userId)
+                .findByIdAndUserIdForUpdate(request.orderId(), userId)
```

**Vì sao:**

- `SELECT ... FOR UPDATE` trên Postgres làm request thứ hai chờ đến khi request đầu commit. Lúc đó kiểm tra ở dòng 93 thấy yêu cầu PENDING vừa tạo và trả 409, giống hệt khi gửi lần lượt. Cả ba bước kiểm tra (yêu cầu đang mở, số lượng, tiền hoàn) đều được bảo vệ nhờ một khóa duy nhất.
- Chỉ khóa một dòng đơn trong thời gian rất ngắn, không ảnh hưởng đơn khác.
- Không chọn cách khóa lạc quan (tăng `version` của đơn): các request thua sẽ nhận 500 cho đến khi sửa SF-41.

**Không cần sửa `approve` và `markReceived`** khi việc tạo đã an toàn. Có thể làm thêm sau: kiểm tra lại số lượng trong `approve`, để chặn các yêu cầu trùng đã lỡ tạo ra trước bản sửa.

## Các trường hợp đã cover

| # | Tình huống | Cơ chế xử lý | Kết quả | Kiểm bằng |
|---|---|---|---|---|
| 1 | Hai đến năm request tạo đổi trả cho cùng đơn, gửi cùng lúc | Khóa dòng đơn `FOR UPDATE`; request sau chờ rồi thấy yêu cầu PENDING vừa tạo (dòng 93-97) | Đúng 1 yêu cầu, còn lại 409 | IT `createReturn_concurrentRequests_createOne`; kịch bản 10 |
| 2 | Khách bấm gửi lần hai sau khi mất phản hồi | Đã có yêu cầu PENDING cho đơn | 409 "đã có yêu cầu đổi trả", không trùng. Khách không nhận lại được yêu cầu cũ ở lần bấm đó, nhưng thấy nó ở tab Đổi/Trả | Kịch bản 14 |
| 3 | Gửi lần lượt yêu cầu thứ hai cho cùng dòng hàng | Kiểm tra yêu cầu đang mở, rồi kiểm tra số lượng còn trả được (dòng 155-159) | 409 hoặc 400, như hiện nay | Kịch bản 14 |
| 4 | Trả một phần, yêu cầu đầu đã RECEIVED, tạo yêu cầu mới cho phần còn lại | Yêu cầu RECEIVED không còn tính là đang mở; số lượng còn lại tính theo `sumActiveReturnedQtyByOrderDetailId` | Được tạo nếu còn số lượng; vượt thì 400 | Thêm ca vào `ReturnRequestServiceTest` (chưa có sẵn) |
| 5 | Hai đơn khác nhau của cùng một khách cùng gửi đổi trả | Khóa theo từng đơn, không khóa chung | Không chờ nhau | Nằm trong thiết kế |
| 6 | Tiền hoàn của yêu cầu | Tính trong cùng đoạn đã khóa (dòng 192-197) nên đọc đúng tổng tiền đã hoàn | Tổng hoàn không vượt tiền đơn | Thêm vào IT `createReturn_concurrentRequests_createOne`: kiểm tổng `refundAmount` của đơn |
| 7 | Khóa dòng đơn tranh chấp với hủy đơn hoặc đổi trạng thái | Khóa chỉ giữ trong transaction tạo yêu cầu, rất ngắn | Request kia chờ vài chục mili giây rồi chạy tiếp | Không cần ca riêng |

### Chưa cover (biết trước)

| # | Tình huống | Hệ quả | Hướng xử lý nếu cần |
|---|---|---|---|
| A | Duyệt hoặc nhận hàng cùng một yêu cầu đồng thời | Dữ liệu đổi đúng một lần nhưng các request còn lại trả 500 (khóa lạc quan), thuộc SF-41 | Sửa ở SF-41 |
| B | Các yêu cầu trùng đã tạo trước khi sửa (đơn 57 có 5 yêu cầu RECEIVED) | Giữ nguyên | Dọn tay; hoặc kiểm tra lại số lượng trong `approve` để chặn các bản trùng còn PENDING |
| C | Mất phản hồi rồi khách muốn xem lại yêu cầu vừa tạo | Chỉ thấy qua danh sách | Có thể thêm Idempotency-Key như SF-37 nếu cần trải nghiệm này |
| D | Hoàn tiền thật cho đơn VNPay khi nhận hàng trả, và nhập lại hàng vào kho | `markReceived` gửi `OrderReturnedEvent` sau commit (`ReturnRequestServiceImpl.java:263`), nhưng chỉ có notification-service nghe (đã tìm trong các service). payment-service không nghe nên không hoàn tiền, inventory không nghe nên không tự nhập lại kho (tồn sách đo ngày 14/11 không tăng sau khi nhận hàng trả) | Ngoài phạm vi plan này; cần quyết định nghiệp vụ trước |
| E | Mất `OrderReturnedEvent` | Chỉ ảnh hưởng thông báo cho khách; `EventPublisher` chỉ ghi log | Mức thấp, không xử lý trong plan này |

## Dữ liệu đã hỏng

Đơn 57 (`ORD-20261114-000061`, khách `deep1114084504@taschen.test`) có 5 yêu cầu RECEIVED với tổng hoàn 965.000 đ. Đây là dữ liệu test. Nên xóa hoặc sửa tay sau khi có bản sửa, để báo cáo doanh thu không bị trừ sai.

## Test

`ReturnRequestControllerIT`: `createReturn_concurrentRequests_createOne`. Tạo đơn COMPLETED có 1 cuốn, gửi 5 request tạo đổi trả qua `ExecutorService` và `CountDownLatch`. Kiểm tra đúng 1 response 201, 4 response 409, và chỉ có 1 bản ghi `return_requests` cho đơn.

`ReturnRequestServiceTest`: đổi các stub `findByIdAndUserId` thành `findByIdAndUserIdForUpdate`.

## Kiểm thử lại

- Kịch bản 10: 5 request cùng lúc chỉ tạo 1 yêu cầu, 4 request còn lại 409.
- Kịch bản 13 không còn tái hiện được (không còn yêu cầu trùng để duyệt).
- Kịch bản 14 (gửi lần lượt yêu cầu thứ hai) vẫn 409.
- `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `order-service`.

## Tuân thủ quy tắc

Java 4 dấu cách, Spotless. Không đổi API, không cần sinh lại contract, không cần migration.

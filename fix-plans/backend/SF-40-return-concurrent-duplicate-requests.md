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

# OrderServiceImpl.initiatePayment

Hộp trắng. Vẽ workflow của code trước, sau đó thiết kế test case phủ từng nhánh. Actual Result chỉ ghi khi nhánh đó đã chạy thật.

## Workflow code

Bắt đầu → N1 đơn của người dùng? → N2 phương thức VNPAY? → N3 đơn PENDING và chưa trả? → N4 gọi payment-service → trả paymentUrl

| Node | Loại | Điều kiện / Hành động | Vị trí code | Nếu đúng | Nếu sai |
|---|---|---|---|---|---|
| N1 | Quyết định | findByIdAndUserId có kết quả | OrderServiceImpl.java:491-496 | Đi N2 | 404 RESOURCE_NOT_FOUND |
| N2 | Quyết định | paymentMethod = VNPAY | OrderServiceImpl.java:478 | Đi N3 | 409 CONFLICT "COD is collected on delivery" |
| N3 | Quyết định | status = PENDING và paymentStatus khác PAID | OrderServiceImpl.java:481 | Đi N4 | 409 CONFLICT "not awaiting payment" |
| N4 | Quyết định | paymentServiceClient.initiateVnPay(POST /vnpay) | OrderServiceImpl.java:498-502, PaymentServiceClient.java:21 | Trả paymentUrl | 500 INTERNAL_ERROR |

## Bảng thiết kế test case theo đường đi

| ID | Đường đi (Node) | Test case name | Data Input | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|
| 1 | N1(sai) | WB01 - Đơn của người khác | orderId không thuộc người dùng | 404 RESOURCE_NOT_FOUND | 404 RESOURCE_NOT_FOUND với orderId 1 | Pass | <pre>HTTP 404<br>{<br>  "success": false,<br>  "code": "RESOURCE_NOT_FOUND",<br>  "message": "The requested resource could not be found.",<br>  "traceId": "a87c7ffc-3752-4601-bed3-0d50dc1446f5",<br>  "path": "/api/v1/orders/1/payments/initiate"<br>}</pre> |
| 2 | N1 → N2(sai) | WB02 - Đơn COD | orderId 18 (COD) | 409 CONFLICT | 409 CONFLICT với đơn COD id 18 | Pass | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "54369a94-3e54-4963-892b-d8d6e963e801",<br>  "path": "/api/v1/orders/18/payments/initiate"<br>}</pre> |
| 3 | N2 → N3(sai) | WB03 - Đơn đã hủy | orderId 19 (CANCELLED) | 409 CONFLICT | 409 CONFLICT với đơn đã hủy id 19 | Pass | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "dbcdcb6b-2e59-4eae-aede-77b7ebe09344",<br>  "path": "/api/v1/orders/19/payments/initiate"<br>}</pre> |
| 4 | N1 → N2 → N3 → N4 | WB04 - Khởi tạo thanh toán | orderId 19, VNPAY, PENDING, 25000 | 200, trả paymentUrl sandbox | 500 INTERNAL_ERROR ở N4. payment-service không có POST /vnpay, chỉ có POST gốc, nên Feign lỗi | Fail | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "6674dbdf-5950-4e69-8712-1a8ca516cd56",<br>  "path": "/api/v1/orders/19/payments/initiate"<br>}</pre> |

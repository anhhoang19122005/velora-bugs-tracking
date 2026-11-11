# OrderServiceImpl.checkout

Hộp trắng. Vẽ workflow của code trước, sau đó thiết kế test case phủ từng nhánh. Actual Result chỉ ghi khi nhánh đó đã chạy thật.

## Workflow code

Bắt đầu → N1 giỏ trống? → lặp từng sản phẩm: N2 có trong giỏ? → N3 khớp số lượng? → N4 sách còn bán? → N5 gọi tồn kho → N6 đủ tồn? → hết lặp → N7 có promotionId? → N8 kiểm tra mã → N9 lấy địa chỉ → N10 lưu đơn (validate Order) → N11 xóa giỏ, phát sự kiện → 201

| Node | Loại | Điều kiện / Hành động | Vị trí code | Nếu đúng | Nếu sai |
|---|---|---|---|---|---|
| N1 | Quyết định | cart.items().isEmpty() | OrderServiceImpl.java:109 | 409 CONFLICT "Cart is empty" | Đi tiếp N2 |
| N2 | Quyết định | Sản phẩm yêu cầu có trong giỏ | OrderServiceImpl.java:223-230 | Đi tiếp N3 | 400 VALIDATION_ERROR "not in your cart" |
| N3 | Quyết định | Số lượng yêu cầu = số lượng trong giỏ | OrderServiceImpl.java:231 | Đi tiếp N4 | 400 VALIDATION_ERROR "does not match your cart" |
| N4 | Xử lý | catalogLookupService.getActiveVariant | OrderServiceImpl.java:236 | Trả về giá, tên sách | Lỗi từ catalog |
| N5 | Quyết định | Gọi inventory-service thành công và có dữ liệu | OrderServiceImpl.java:263-275 | Trả về tổng tồn kho | 500 INTERNAL_ERROR |
| N6 | Quyết định | available &lt; quantity | OrderServiceImpl.java:256 | 409 INSUFFICIENT_STOCK | Thêm dòng đơn, quay lại N2 hoặc sang N7 |
| N7 | Quyết định | request.promotionId() != null | OrderServiceImpl.java:117 | Đi N8 | Không giảm giá, đi N9 |
| N8 | Quyết định | promotionServiceClient.validate(POST /validate) | OrderServiceImpl.java:286-301, PromotionServiceClient.java:18 | Tính giảm giá, đi N9 | 404 nếu NotFound; 409 nếu Conflict; 400 với lỗi Feign khác |
| N9 | Quyết định | Lấy địa chỉ của người dùng | OrderServiceImpl.java:310-324 | Đi N10 | 404 nếu không có; 500 với lỗi Feign khác |
| N10 | Quyết định | Order hợp lệ khi lưu: recipientPhone khớp ^(03&#124;05&#124;07&#124;08&#124;09&#124;02)[0-9]{8,9}&#36;, tên không ký tự đặc biệt | OrderServiceImpl.java:142, Order.java:54,59 | Đi N11 | ConstraintViolationException → 500 |
| N11 | Kết thúc | clearCart, publishOrderPlaced, trả OrderResponse | OrderServiceImpl.java:145-148 | 201 Order placed |  |

## Bảng thiết kế test case theo đường đi

| ID | Đường đi (Node) | Test case name | Data Input | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|
| 1 | N1(đúng) | WB01 - Giỏ hàng trống | Giỏ trống, gọi POST /orders trực tiếp | 409 CONFLICT "Cart is empty" | 409 CONFLICT | Pass | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "66903592-ead0-4bf7-9125-cf13bbe258ba",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 2 | N1 → N2(sai) | WB02 - Sản phẩm không có trong giỏ | Giỏ có bookId 47; yêu cầu bookId 46 | 400 VALIDATION_ERROR | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "46dbbf6b-3093-4849-8b3c-8d8ce65d2809",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 3 | N1 → N2 → N3(sai) | WB03 - Số lượng khác giỏ | Giỏ bookId 47 x1; yêu cầu quantity 2 | 400 VALIDATION_ERROR | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "a3e7b4b8-6645-4b55-a0c9-ed50f8fd9dcd",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 4 | N2 → N3 → N4 → N5(sai) | WB04 - Dịch vụ tồn kho không phản hồi | Tắt inventory-service; bookId 47 x1 | 500 INTERNAL_ERROR, không tạo đơn | Tắt inventory-service: 500 INTERNAL_ERROR, không tạo đơn. Đã bật lại dịch vụ | Pass | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "84720eb1-9512-45c0-b26e-b3ea5ad64d1c",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 5 | N5 → N6(đúng) | WB05 - Không đủ tồn kho | bookId có tồn N; quantity N+1 trong giỏ | 409 INSUFFICIENT_STOCK | Không tạo được điều kiện: giỏ hàng từ chối số lượng vượt tồn (409) nên không đi đến N6. Cần dữ liệu tồn catalog lớn hơn tồn kho thực | Blocked | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "404bdb3b-967b-4dcf-b766-56aec665ca27",<br>  "path": "/api/v1/carts/me/items"<br>}</pre> |
| 6 | N6 → N7(sai) → N9 → N10 → N11 | WB06 - Đặt hàng không mã, thành công | bookId 47 x1, addressId 24, COD, promotionId null | 201, totalAmount 25000, status PENDING | 201, ORD-20261110-000021, totalAmount 25000.00, PENDING | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 18,<br>    "orderCode": "ORD-20261110-000021",<br>    "promotionId": null,<br>    "discountAmount": null,<br>    "totalAmount": 25000.0,<br>    "status": "PENDING",<br>    "paymentStatus": "UNPAID",<br>    "paymentMethod": "COD"<br>  },<br>  "message": "Order placed"<br>}</pre> |
| 7 | N7(đúng) → N8 → N9 → N10 → N11 | WB07 - Đặt hàng có mã hợp lệ | bookId 47 x1, addressId 24, COD, promotionId 27 (10%) | 201, discountAmount 2500, totalAmount 22500 | 400 VALIDATION_ERROR ở N8. promotion-service không có POST /validate, chỉ có GET /validate/{code}, nên Feign lỗi và rơi vào nhánh 400 | Fail | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "8747696b-1ce3-45a0-ae34-7c71eaba04b5",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 8 | N8(NotFound) | WB08 - promotionId không tồn tại | promotionId 999999 | 404 RESOURCE_NOT_FOUND | 400 VALIDATION_ERROR thay vì 404, cùng nguyên nhân thiếu POST /validate (Bug SF-08) | Fail | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "200625e9-7831-4f12-a7bc-7a377ceb1957",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 9 | N8 → N9(sai) | WB09 - Địa chỉ không thuộc người dùng | addressId của người khác | 404 RESOURCE_NOT_FOUND | 404 RESOURCE_NOT_FOUND với addressId 1 | Pass | <pre>HTTP 404<br>{<br>  "success": false,<br>  "code": "RESOURCE_NOT_FOUND",<br>  "message": "The requested resource could not be found.",<br>  "traceId": "f6a08f1c-fe4f-4eb6-9caf-8fa757e2e552",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 10 | N9 → N10(sai) | WB10 - SĐT không qua validate của Order | addressId có SĐT 0123456789 | 4xx báo rõ số điện thoại sai | 500 INTERNAL_ERROR do ConstraintViolationException tại recipientPhone | Fail | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "fc68cfac-dacf-4bd5-bd52-f7f24e44912a",<br>  "path": "/api/v1/orders"<br>}</pre> |

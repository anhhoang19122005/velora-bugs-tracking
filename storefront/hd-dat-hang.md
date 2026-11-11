# Đặt hàng tại checkout

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Giỏ hàng | Có sản phẩm, đủ tồn kho | Giỏ trống | Số lượng = tồn kho | Số lượng = tồn kho + 1 |
| Giỏ hàng |  | Số lượng vượt tồn kho |  |  |
| Địa chỉ | Đã chọn, SĐT hợp lệ | Chưa có địa chỉ |  |  |
| Địa chỉ |  | SĐT không hợp lệ cho đơn hàng |  |  |
| Thanh toán | COD | Chưa chọn |  |  |
| Thanh toán | VNPay |  |  |  |
| Mã giảm giá | Bỏ trống | Mã không tồn tại |  |  |
| Mã giảm giá | Mã đã duyệt, còn hiệu lực | Mã hết hạn |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Giỏ hàng | Data Input: Địa chỉ | Data Input: Thanh toán | Data Input: Mã giảm giá | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Đặt COD không mã | Conan 101 x1 (25.000 đ) | Mặc định, 0912345678 | COD | "" | 201, trạng thái PENDING, giỏ trống | 201, ORD-20261110-000021, tổng 25.000 đ, giỏ trống | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 18,<br>    "orderCode": "ORD-20261110-000021",<br>    "promotionId": null,<br>    "discountAmount": null,<br>    "totalAmount": 25000.0,<br>    "status": "PENDING",<br>    "paymentStatus": "UNPAID",<br>    "paymentMethod": "COD"<br>  },<br>  "message": "Order placed"<br>}</pre> |
| 2 | Valid Partition | TC02 - Đặt VNPay | Conan 101 x1 | Mặc định, 0912345678 | VNPay | "" | Tạo đơn và chuyển sang cổng VNPay sandbox | Tạo đơn nhưng initiate trả 500, không chuyển cổng (Bug SF-07) | Fail | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "6674dbdf-5950-4e69-8712-1a8ca516cd56",<br>  "path": "/api/v1/orders/19/payments/initiate"<br>}</pre> |
| 3 | Valid Partition | TC03 - Đặt COD có mã hợp lệ | Conan 101 x1 (25.000 đ) | Mặc định, 0912345678 | COD | MANUAL1110 (10%) | 201, tổng 22.500 đ, đơn có promotionId | 400 VALIDATION_ERROR, không tạo đơn (Bug SF-08) | Fail | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "8747696b-1ce3-45a0-ae34-7c71eaba04b5",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 4 | Invalid Partition | TC04 - Giỏ trống | Trống | Mặc định | COD | "" | Không cho tiến hành thanh toán | Giỏ trống, nút thanh toán bị khóa, báo chọn ít nhất một sản phẩm | Pass | Không gọi API |
| 5 | Invalid Partition | TC05 - Chưa có địa chỉ | Conan 100 x1 | Chưa có | COD | "" | Khóa nút Đặt hàng, báo cần chọn địa chỉ | Nút bị khóa, hiện "Chọn địa chỉ nhận hàng." | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - SĐT địa chỉ không hợp lệ cho đơn | Conan 100 x1 | Mặc định, 0123456789 | COD | "" | Báo rõ số điện thoại sai, trả lỗi 4xx | 500 INTERNAL_ERROR, toast báo kiểm tra tồn kho/địa chỉ (Bug SF-02) | Fail | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "fc68cfac-dacf-4bd5-bd52-f7f24e44912a",<br>  "path": "/api/v1/orders"<br>}</pre> |
| 7 | Invalid Partition | TC07 - Chưa chọn thanh toán | Conan 100 x1 | Mặc định | "" | "" | Khóa nút Đặt hàng, báo chọn phương thức | Nút bị khóa, hiện "Chọn phương thức thanh toán để tiếp tục." | Pass | Không gọi API |
| 8 | Invalid Partition | TC08 - Mã không tồn tại | Conan 101 x1 | Mặc định | COD | SAIMA123 | Báo không tìm thấy mã, tổng không đổi | Hiện "Không tìm thấy mã khuyến mãi.", tổng 25.000 đ | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": false,<br>    "promotionId": null,<br>    "code": "SAIMA123",<br>    "discountPercent": null,<br>    "discountAmount": null,<br>    "reason": "Promotion code not found"<br>  },<br>  "message": "OK"<br>}</pre> |
| 9 | Valid Boundary | TC09 - Số lượng bằng tồn kho | Sách còn N, đặt N | Mặc định | COD | "" | 201, tạo đơn thành công | 201, đơn ORD-20261110-000023 với 50 cuốn, tổng 1.250.000 đ. Đã hủy ngay sau khi test | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 20,<br>    "orderCode": "ORD-20261110-000023",<br>    "totalAmount": 1250000.0,<br>    "status": "PENDING",<br>    "paymentMethod": "COD"<br>  },<br>  "message": "Order placed"<br>}</pre> |
| 10 | Invalid Boundary | TC10 - Số lượng vượt tồn kho một đơn vị | Sách còn N, đặt N+1 | Mặc định | COD | "" | Không tạo đơn, 409 INSUFFICIENT_STOCK, báo rõ sản phẩm | Ô số lượng tự giảm 51 về 50, nên không đặt vượt được. Không đi đến 409 vì bị chặn sớm hơn | Pass | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "404bdb3b-967b-4dcf-b766-56aec665ca27",<br>  "path": "/api/v1/carts/me/items"<br>}</pre> |

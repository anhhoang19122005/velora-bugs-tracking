# Khách tạo yêu cầu đổi trả

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Sản phẩm | Đã chọn, thuộc đơn đã hoàn tất | Chưa chọn |  |  |
| Lý do | Đã chọn | Chưa chọn |  |  |
| Mô tả | 30 đến 1000 ký tự | Rỗng | &#124;mô tả&#124; = 30 | &#124;mô tả&#124; = 29 |
| Mô tả |  |  | &#124;mô tả&#124; = 1000 | &#124;mô tả&#124; = 1001 |
| Số lượng | 1 đến số lượng còn đổi trả được |  | Số lượng = số còn lại | Số lượng = số còn lại + 1 |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Sản phẩm | Data Input: Lý do | Data Input: Mô tả | Data Input: Số lượng | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Tạo yêu cầu hợp lệ | Conan 100 | Đổi ý | 59 ký tự | 1 | 201, chuyển về tab Đổi/Trả, trạng thái chờ duyệt | 201, RMA-20261110-000002, hiện Chờ duyệt | Pass | HTTP 201. Chỉ còn status 200/201 trong Network, body không lưu được. |
| 2 | Invalid Partition | TC02 - Chưa chọn sản phẩm | "" | "" | "" | "" | Khóa nút gửi, báo chọn sản phẩm | Nút bị khóa, hiện "Chọn ít nhất một sản phẩm." | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Chưa chọn lý do | Conan 100 | "" | 59 ký tự | 1 | Khóa nút gửi, báo chọn lý do | Nút bị khóa, hiện "Chọn lý do đổi/trả." | Pass | Không gọi API |
| 4 | Invalid Partition | TC04 - Mô tả rỗng | Conan 100 | Đổi ý | "" | 1 | Báo mô tả là bắt buộc, không gửi | Nút gửi bị khóa, hiện "Mô tả cần 30–1000 ký tự." | Pass | Không gọi API |
| 5 | Valid Boundary | TC05 - Mô tả đúng 30 ký tự | Conan 100 | Đổi ý | 'a' x 30 | 1 | 201, tạo thành công | 201, RMA-20261110-000003, chờ duyệt | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 3,<br>    "returnCode": "RMA-20261110-000003",<br>    "orderId": 21,<br>    "reasonCode": "CHANGED_MIND",<br>    "status": "PENDING",<br>    "refundAmount": 25000.0<br>  },<br>  "message": "OK"<br>}</pre> |
| 6 | Valid Boundary | TC06 - Mô tả đúng 1000 ký tự | Conan 100 | Đổi ý | 'a' x 1000 | 1 | 201, tạo thành công | Tạo thành công RMA-20261110-000004, mô tả 1000 ký tự | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "returnCode": "RMA-20261110-000004",<br>    "status": "PENDING",<br>    "descriptionLength": 1000,<br>    "refundAmount": 25000<br>  },<br>  "message": "Đọc lại từ GET /returns/me"<br>}</pre> |
| 7 | Invalid Boundary | TC07 - Mô tả 29 ký tự | Conan 100 | Đổi ý | 'a' x 29 | 1 | Báo mô tả tối thiểu 30 ký tự | Nút gửi bị khóa, hiện "Mô tả cần 30–1000 ký tự." | Pass | Không gọi API |
| 8 | Invalid Boundary | TC08 - Mô tả 1001 ký tự | Conan 100 | Đổi ý | 'a' x 1001 | 1 | Không cho nhập quá hoặc báo tối đa 1000 ký tự | Nút gửi bị khóa, bộ đếm 1001/1000, hiện "Mô tả cần 30–1000 ký tự." | Pass | Không gọi API |
| 9 | Invalid Boundary | TC09 - Số lượng vượt số còn lại | Conan 100 | Đổi ý | 59 ký tự | 2 (mua 1) | Không cho chọn quá số lượng còn đổi trả được | Ô số lượng tự giảm 2 về 1, không chọn vượt được | Pass | Không gọi API |

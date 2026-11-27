# HD-Nhà cung cấp

[← Kết quả Guide me](../README.md)

Guide me: Thêm một nhà cung cấp

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Tên | 1-255 | Rỗng | 255 | 256 |
|  | Email | Trống hoặc đúng định dạng | Sai định dạng |  |  |
|  | Điện thoại | Trống hoặc 0 + 9-10 chữ số | Không bắt đầu bằng 0 | 10 số | 9 số |
|  |  |  | Có chữ, khoảng trắng | 11 số | 12 số |
|  | Trạng thái | Hoạt động: chọn được trên đơn mua | Ngừng hoạt động: không chọn được |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Vai trò | Data Input: Tên | Data Input: Email / Điện thoại | Data Input: Địa chỉ / Trạng thái | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM07-01 - Warehouse thêm nhà cung cấp | Warehouse | Công ty Sách A | a@sach.vn / 0901234567 | 1 Lê Lợi / Hoạt động | 201, dùng được ngay trên đơn mua, không cần duyệt. Seller thấy trong ô nhà cung cấp khi thêm sách. | POST 201, trạng thái hoạt động=True; Seller thấy trong danh sách chọn: True | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Công ty TNHH Sách Bình Minh",<br>  "email": "lienhe@sachbinhminh.vn",<br>  "phone": "0903772145",<br>  "address": "126 Nguyễn Thị Minh Khai, Phường Võ Thị Sáu, Quận 3, TP. Hồ Chí Minh"<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 36,<br>    "name": "Công ty TNHH Sách Bình Minh",<br>… (rút gọn)</pre> |
| 2 |  | GM07-02 - Chỉ nhập tên | Warehouse | NCC tối giản | (trống) / (trống) | (trống) | 201. Nếu form gửi chuỗi rỗng và bị 400 thì ghi lỗi. | Tạo qua form chỉ với tên "Nhà sách Hải Đăng": HTTP 201 | Pass | <pre>POST /api/suppliers (qua form warehouse)<br>Request body:<br>{<br>  "name": "Nhà sách Hải Đăng"<br>}<br>HTTP 201<br>{"id":37,"name":"Nhà sách Hải Đăng","email":null,"phone":null,"address":null,"active":true}</pre> |
| 3 |  | GM07-03 - Ngừng hoạt động rồi thử tạo đơn mua bằng API [Nghi vấn G-12] | Admin | NCC đã ngừng | — | Ngừng hoạt động; POST /api/v1/purchase-orders | Guide: không chọn được. Kiểm cả giao diện và API. Code không thấy kiểm trạng thái khi tạo đơn mua. | Ngừng hoạt động: DELETE 204; còn trong danh sách đang hoạt động: False. Tạo đơn mua với nhà cung cấp đã ngừng qua API: HTTP 201 (mã PO-20261127-000038). Guide nói không chọn được<br>Bug [B06](../loi.md#b06)<br>[Ảnh 1](../images/GM07-03-1.png) | Fail | <pre>DELETE /api/v1/suppliers/38<br>HTTP 204<br>{}<br><br>POST /api/v1/purchase-orders<br>Request body:<br>{<br>  "supplierId": 38,<br>  "note": "Đặt bổ sung tháng 12",<br>  "items": [<br>    {<br>      "bookId": 1,<br>      "variantId": 1,<br>      "quantity": 10,<br>… (rút gọn)</pre><br>[Đầy đủ](../api/GM07-03.txt) |
| 4 | Invalid Partition | GM07-04 - Email sai định dạng | Warehouse | NCC E | abc@ / 0901234567 | — | 400 ở ô email. | HTTP 400 {'email': 'Invalid email format'} | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Nhà sách Thái Hà",<br>  "email": "lienhe@",<br>  "phone": "0903772146"<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "f624425a8a6d4926",<br>  "path": "/api/v1/suppliers",<br>… (rút gọn)</pre> |
| 5 |  | GM07-05 - Điện thoại không bắt đầu bằng 0 | Warehouse | NCC P | p@sach.vn / 9012345678 | — | 400. | HTTP 400 | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Nhà sách Thái Hà",<br>  "phone": "9012345678"<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "231e9f2626ec4ee2",<br>  "path": "/api/v1/suppliers",<br>  "timestamp": "2026-11-27T04:16:41.714510900Z",<br>… (rút gọn)</pre> |
| 6 |  | GM07-06 - Seller thêm nhà cung cấp | Seller | NCC của seller | — | — | 403. | HTTP 403 | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Nhà sách Kim Đồng chi nhánh 2"<br>}<br>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to perform this action"<br>}</pre> |
| 7 | Valid Boundary | GM07-07 - Điện thoại 11 số | Warehouse | NCC 11 | (trống) / 02812345678 | — | 201. | HTTP 201 | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Công ty Sách Đông A",<br>  "phone": "02838221456"<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 39,<br>    "name": "Công ty Sách Đông A",<br>    "email": null,<br>    "phone": "02838221456",<br>… (rút gọn)</pre> |
| 8 | Invalid Boundary | GM07-08 - Điện thoại 9 số | Warehouse | NCC 9 | (trống) / 090123456 | — | 400. | HTTP 400 | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Công ty Sách Đông A",<br>  "phone": "090123456"<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "b5edb6bc8da547c5",<br>  "path": "/api/v1/suppliers",<br>  "timestamp": "2026-11-27T04:16:41.855290400Z",<br>… (rút gọn)</pre> |
| 9 |  | GM07-09 - Địa chỉ 501 ký tự | Warehouse | NCC D | — | 501 ký tự | 400. | HTTP 400 | Pass | <pre>POST /api/v1/suppliers<br>Request body:<br>{<br>  "name": "Công ty Sách Đông A",<br>  "address": "Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận Hoàn Kiếm, Hà Nội Số 9 Đinh Lễ, Quận H"<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "d0f483256b8b436c",<br>  "path": "/api/v1/suppliers",<br>  "timestamp": "2026-11-27T04:16:41.889082800Z",<br>… (rút gọn)</pre> |

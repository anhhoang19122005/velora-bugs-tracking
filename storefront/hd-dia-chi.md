# Thêm và sửa địa chỉ giao hàng

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Người nhận | 1 đến 255 ký tự, không ký tự đặc biệt | Rỗng | &#124;tên&#124; = 255 | &#124;tên&#124; = 256 |
| Người nhận |  | Có ký tự đặc biệt |  |  |
| SĐT | Đầu số 02, 03, 05, 07, 08, 09 (quy tắc của đơn hàng) | Rỗng | &#124;SĐT&#124; = 10 | &#124;SĐT&#124; = 9 |
| SĐT |  | Đầu số 01, 04, 06 |  |  |
| SĐT |  | Chứa chữ |  |  |
| Địa chỉ | 1 đến 500 ký tự | Rỗng | &#124;địa chỉ&#124; = 500 | &#124;địa chỉ&#124; = 501 |
| Phường, Quận, Tỉnh/TP | 1 đến 255 ký tự | Rỗng |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Người nhận | Data Input: SĐT | Data Input: Địa chỉ | Data Input: Phường | Data Input: Quận | Data Input: Tỉnh/TP | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Thêm địa chỉ hợp lệ | Test Test | 0912345678 | 12 Duong Kiem Thu | Phuong Test | Quan Test | TP Test | Lưu thành công, địa chỉ hiện ở checkout | PUT 200, địa chỉ hiện đúng ở checkout | Pass | HTTP 200. Chỉ còn status 200/201 trong Network, body không lưu được. |
| 2 | Invalid Partition | TC02 - Người nhận rỗng | "" | 0912345678 | 12 Duong | P1 | Q1 | HCM | Báo lỗi tại ô người nhận | Hiện "Vui lòng nhập thông tin này.", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Người nhận có ký tự đặc biệt | Test@# | 0912345678 | 12 Duong | P1 | Q1 | HCM | Báo lỗi ngay tại form, không để đến lúc đặt hàng | Form chấp nhận, lưu được địa chỉ tên "Test@#" (Bug SF-10) | Fail | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 25,<br>    "recipientName": "Test@#",<br>    "phoneNumber": "0912345678",<br>    "isDefault": false<br>  },<br>  "message": "OK"<br>}</pre> |
| 4 | Invalid Partition | TC04 - SĐT đầu số không dùng được | Test Test | 0123456789 | 12 Duong | P1 | Q1 | HCM | Báo số điện thoại không hợp lệ, không lưu | 201, lưu thành công. Sau đó đặt hàng bị 500 (Bug SF-02) | Fail | HTTP 201. Chỉ còn status 200/201 trong Network, body không lưu được. |
| 5 | Invalid Partition | TC05 - SĐT chứa chữ | Test Test | 09123abc78 | 12 Duong | P1 | Q1 | HCM | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại phải có 10 chữ số và bắt đầu bằng 0." | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - Địa chỉ rỗng | Test Test | 0912345678 | "" | P1 | Q1 | HCM | Báo lỗi tại ô địa chỉ | Hiện "Vui lòng nhập thông tin này.", không gọi API | Pass | Không gọi API |
| 7 | Invalid Partition | TC07 - Phường rỗng | Test Test | 0912345678 | 12 Duong | "" | Q1 | HCM | Báo lỗi tại ô phường | Hiện "Vui lòng nhập thông tin này.", không gọi API | Pass | Không gọi API |
| 8 | Valid Boundary | TC08 - SĐT đúng 10 số | Test Test | 0987654321 | 12 Duong | P1 | Q1 | HCM | Lưu thành công | 201, lưu thành công | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 26,<br>    "recipientName": "Test Test",<br>    "phoneNumber": "0987654321",<br>    "isDefault": false<br>  },<br>  "message": "OK"<br>}</pre> |
| 9 | Valid Boundary | TC09 - Địa chỉ đúng 500 ký tự | Test Test | 0912345678 | 'a' x 500 | P1 | Q1 | HCM | Lưu thành công | 201, lưu thành công với địa chỉ 500 ký tự | Pass | HTTP 201, địa chỉ id 27 (street 500 ký tự, không in lại) |
| 10 | Invalid Boundary | TC10 - SĐT 9 số | Test Test | 091234567 | 12 Duong | P1 | Q1 | HCM | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại phải có 10 chữ số và bắt đầu bằng 0." | Pass | Không gọi API |
| 11 | Invalid Boundary | TC11 - Địa chỉ 501 ký tự | Test Test | 0912345678 | 'a' x 501 | P1 | Q1 | HCM | Báo địa chỉ quá dài | Hiện "Địa chỉ chi tiết không được vượt quá 500 ký tự." | Pass | Không gọi API |

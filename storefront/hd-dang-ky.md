# Đăng ký storefront

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Họ tên | Có đủ họ và tên, mỗi phần &lt;= 50 ký tự | Rỗng | Một phần = 50 ký tự | Một phần = 51 ký tự |
| email | Đúng định dạng, chưa tồn tại | Rỗng |  |  |
| email |  | Sai định dạng |  |  |
| email |  | Đã tồn tại |  |  |
| SĐT | Khớp ^0[0-9]{9}&#36; | Rỗng | &#124;SĐT&#124; = 10 | &#124;SĐT&#124; = 9 |
| SĐT |  | Không bắt đầu bằng 0 |  | &#124;SĐT&#124; = 11 |
| SĐT |  | Chứa chữ |  |  |
| Giới tính | Đã chọn | Chưa chọn |  |  |
| password | 8 đến 100 ký tự (backend) | Rỗng | &#124;password&#124; = 8 | &#124;password&#124; = 7 |
| password |  |  | &#124;password&#124; = 100 | &#124;password&#124; = 101 |
| confirm | Trùng password | Khác password |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Họ tên | Data Input: email | Data Input: SĐT | Data Input: Giới tính | Data Input: password | Data Input: confirm | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Đăng ký hợp lệ | Khach Test Manual | manual-20261110@taschen.test | 0912026110 | Khác | (mật khẩu test) | (mật khẩu test) | 201, chuyển sang trang xác thực email | 201, chuyển sang /vi/verify-email | Pass | HTTP 201. Chỉ còn status 200/201 trong Network, body không lưu được. |
| 2 | Invalid Partition | TC02 - Họ tên rỗng | "" | tc02@taschen.test | 0912345678 | Nam | (mật khẩu test) | (mật khẩu test) | Báo lỗi tại ô họ tên, không gọi API | Hiện "Nhập họ và tên của bạn.", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Email sai định dạng | Khach Test | abc | 0912345678 | Nam | (mật khẩu test) | (mật khẩu test) | Báo email không hợp lệ | Hiện "Email không hợp lệ.", không gọi API | Pass | Không gọi API |
| 4 | Invalid Partition | TC04 - Email đã tồn tại | Khach Test | testing2@gmail.com | 0912345678 | Nam | (mật khẩu test) | (mật khẩu test) | Báo lỗi email đã dùng tại ô email | Hiện "Email này đã được đăng ký..." tại ô email | Pass | <pre>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "b0223b5df69f47c1",<br>  "path": "/api/v1/auth/register"<br>}</pre> |
| 5 | Invalid Partition | TC05 - SĐT không bắt đầu bằng 0 | Khach Test | tc05@taschen.test | 1912345678 | Nam | (mật khẩu test) | (mật khẩu test) | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại gồm 10 chữ số, bắt đầu bằng 0." | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - SĐT chứa chữ | Khach Test | tc06@taschen.test | 09123abc78 | Nam | (mật khẩu test) | (mật khẩu test) | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại gồm 10 chữ số, bắt đầu bằng 0." | Pass | Không gọi API |
| 7 | Invalid Partition | TC07 - Chưa chọn giới tính | Khach Test | tc07@taschen.test | 0912345678 | "" | (mật khẩu test) | (mật khẩu test) | Báo lỗi tại ô giới tính | Hiện "Chọn giới tính.", không gọi API | Pass | Không gọi API |
| 8 | Invalid Partition | TC08 - Mật khẩu xác nhận khác | Khach Test | tc08@taschen.test | 0912345678 | Nam | Abcd1234 | Abcd9999 | Báo mật khẩu không khớp tại ô confirm | Hiện "Mật khẩu nhập lại không khớp." | Pass | Không gọi API |
| 9 | Valid Boundary | TC09 - Mật khẩu đúng 8 ký tự | Khach Test | tc09@taschen.test | 0912345678 | Nam | Abcd1234 | Abcd1234 | 201, chuyển sang trang xác thực | 201, chuyển sang /vi/verify-email | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 112,<br>    "userCode": "CUS-000109",<br>    "email": "tc09@taschen.test",<br>    "active": false<br>  },<br>  "message": "OK"<br>}</pre> |
| 10 | Valid Boundary | TC10 - SĐT đúng 10 số | Khach Test | tc10@taschen.test | 0912345670 | Nam | (mật khẩu test) | (mật khẩu test) | 201, chuyển sang trang xác thực | 201, chuyển sang /vi/verify-email | Pass | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 113,<br>    "userCode": "CUS-000110",<br>    "email": "tc10@taschen.test",<br>    "active": false<br>  },<br>  "message": "OK"<br>}</pre> |
| 11 | Invalid Boundary | TC11 - Mật khẩu 7 ký tự | Khach Test | tc11@taschen.test | 0912345678 | Nam | Abcd123 | Abcd123 | Báo mật khẩu tối thiểu 8 ký tự ngay tại form | Hiện "Mật khẩu cần ít nhất 8 ký tự.", không gọi API | Pass | Không gọi API |
| 12 | Invalid Boundary | TC12 - SĐT 9 số | Khach Test | tc12@taschen.test | 091234567 | Nam | (mật khẩu test) | (mật khẩu test) | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại gồm 10 chữ số, bắt đầu bằng 0." | Pass | Không gọi API |
| 13 | Invalid Boundary | TC13 - SĐT 11 số | Khach Test | tc13@taschen.test | 09123456789 | Nam | (mật khẩu test) | (mật khẩu test) | Báo số điện thoại không hợp lệ | Hiện "Số điện thoại gồm 10 chữ số, bắt đầu bằng 0." | Pass | Không gọi API |

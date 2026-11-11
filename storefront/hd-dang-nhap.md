# Đăng nhập storefront

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| email | Đúng định dạng, đã đăng ký | Rỗng |  |  |
| email |  | Sai định dạng |  |  |
| email |  | Đúng định dạng, chưa đăng ký |  |  |
| password | Đúng mật khẩu | Rỗng | &#124;password&#124; = 5 và 6 (đăng nhập không giới hạn độ dài) |  |
| password |  | Sai mật khẩu |  |  |
| Trạng thái tài khoản | Đã xác thực email | Chưa xác thực email |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: email | Data Input: password | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Đăng nhập đúng | testing2@gmail.com | (mật khẩu test) | Về trang chủ, toast thành công, POST /auth/login 200 | Về /vi, toast "Đăng nhập thành công", 200 | Pass | HTTP 200 (ẩn token) |
| 2 | Invalid Partition | TC02 - Email rỗng | "" | (mật khẩu test) | Báo lỗi tại ô email, không gọi API | Hiện "Nhập email của bạn.", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Email sai định dạng | 12345678 | testing2@gmail.com | Báo "Email không hợp lệ", không gọi API | Hiện "Email không hợp lệ", không có request login | Pass | Không gọi API |
| 4 | Invalid Partition | TC04 - Email chưa đăng ký | nobody-probe@taschen.test | wrong-probe-1 | 401, báo sai thông tin đăng nhập | Hiện "Email hoặc mật khẩu không đúng..." | Pass | <pre>HTTP 401<br>{<br>  "success": false,<br>  "code": "UNAUTHORIZED",<br>  "message": "Authentication is required to access this resource.",<br>  "traceId": "c2831f77537d40cb",<br>  "path": "/api/v1/auth/login"<br>}</pre> |
| 5 | Invalid Partition | TC05 - Mật khẩu rỗng | testing2@gmail.com | "" | Báo lỗi tại ô mật khẩu, không gọi API | Hiện "Nhập mật khẩu.", không gọi API | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - Sai mật khẩu | testing2@gmail.com | sai-mat-khau-1 | 401, báo sai thông tin đăng nhập | Hiện "Email hoặc mật khẩu không đúng..." | Pass | <pre>HTTP 401<br>{<br>  "success": false,<br>  "code": "UNAUTHORIZED",<br>  "message": "Authentication is required to access this resource.",<br>  "traceId": "e7f533f3d92b4110",<br>  "path": "/api/v1/auth/login"<br>}</pre> |
| 7 | Invalid Partition | TC07 - Tài khoản chưa xác thực | manual-20261110@taschen.test | (mật khẩu test) | Từ chối, báo chưa xác thực email | Hiện "Tài khoản này chưa xác thực email nên chưa đăng nhập được." kèm liên kết xác thực | Pass | <pre>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to access this resource.",<br>  "traceId": "2a9f3d467b054fa6",<br>  "path": "/api/v1/auth/login"<br>}</pre> |
| 8 | Valid Boundary | TC08 - Mật khẩu đúng 6 ký tự | testing2@gmail.com | abc123 | Qua kiểm tra form, gọi API và nhận 401 | Qua kiểm tra form, API trả 401 | Pass | <pre>HTTP 401<br>{<br>  "success": false,<br>  "code": "UNAUTHORIZED",<br>  "message": "Authentication is required to access this resource.",<br>  "traceId": "3e56c09c943d43cf",<br>  "path": "/api/v1/auth/login"<br>}</pre> |
| 9 | Valid Boundary | TC09 - Mật khẩu 5 ký tự | testing2@gmail.com | abc12 | Qua kiểm tra form, gọi API và nhận 401 | Qua kiểm tra form, API trả 401 | Pass | <pre>HTTP 401<br>{<br>  "success": false,<br>  "code": "UNAUTHORIZED",<br>  "message": "Authentication is required to access this resource.",<br>  "traceId": "f4b1efaec5f34ea4",<br>  "path": "/api/v1/auth/login"<br>}</pre> |

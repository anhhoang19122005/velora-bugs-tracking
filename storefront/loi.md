# Danh sách lỗi - Storefront

Nhóm **bug giao diện (UI) SF-18–SF-27** có mục lục riêng tại [ui/](ui/README.md).

Ghi nhận ngày 2026-11-12: SF-02, SF-03, SF-07, SF-08, SF-10 đã có bản sửa merge; chưa kiểm thử lại. Trong các mục này, bước tái hiện, mong đợi, thực tế, response và ảnh bên dưới được giữ nguyên từ **trước khi sửa**, không phải kết quả trên bản develop mới.

| # | Mức độ | Luồng | Endpoint / Màn hình | Nghi ngờ thuộc | Ảnh |
|---|---|---|---|---|---|
| [SF-01](#sf-01) | Major (đã sửa) | 1 - Đăng nhập, đăng ký | POST /auth/login, /auth/register · route.ts | storefront (route.ts) | [Ảnh 1](../images/SF-01-1.jpg), [Ảnh 2](../images/SF-01-2.jpg) |
| [SF-02](#sf-02) | Major (đã sửa; chưa kiểm thử lại) | 3 - Checkout COD | POST /api/v1/orders · form địa chỉ | identity-service (địa chỉ) / order-service | [Ảnh 1](../images/SF-02-1.jpg) |
| [SF-03](#sf-03) | Major (đã sửa; chưa kiểm thử lại) | 3 - Checkout COD | order-service GlobalExceptionHandler | order-service | [Ảnh 1](../images/SF-03-1.png) |
| [SF-04](#sf-04) | Major (đã sửa) | Khởi động môi trường | taschen-backend/dev.ps1 | backend (dev.ps1) | [Ảnh 1](../images/SF-04-1.png) |
| [SF-05](#sf-05) | Major (đã sửa) | 2 - Giỏ hàng | Mọi trang storefront · lib/auth/token.ts | storefront | [Ảnh 1](../images/SF-05-1.jpg), [Ảnh 2](../images/SF-05-2.jpg) |
| [SF-06](#sf-06) | Major | 1 - Đăng ký | Mailpit · notification-service | backend / hạ tầng | [Ảnh 1](../images/SF-06-1.jpg) |
| [SF-07](#sf-07) | Major (đã sửa; chưa kiểm thử lại) | 4 - Checkout VNPAY | POST /orders/{id}/payments/initiate | order-service / payment-service | [Ảnh 1](../images/SF-07-1.jpg) |
| [SF-08](#sf-08) | Major (đã sửa; chưa kiểm thử lại) | 7 - Khuyến mãi | POST /api/v1/orders có mã | order-service / promotion-service | [Ảnh 1](../images/SF-08-1.jpg), [Ảnh 2](../images/SF-08-2.jpg) |
| [SF-09](#sf-09) | Major | 1 - Xác thực email | Email xác thực · notification-service | notification-service (cấu hình link) | [Ảnh 1](../images/SF-09-1.jpg) |
| [SF-10](#sf-10) | Major (đã sửa; chưa kiểm thử lại) | Địa chỉ, đặt hàng | POST /users/me/addresses | identity-service / storefront | [Ảnh 1](../images/SF-10-1.jpg) |
| [SF-11](#sf-11) | Minor (đã sửa) | 1 - Đăng nhập | Trang đăng nhập | storefront | [Ảnh 1](../images/SF-11-1.jpg) |
| [SF-12](#sf-12) | Minor (đã sửa) | Trang chủ, chi tiết sách | /recommendations/*, POST /events | backend (dev.ps1) | [Ảnh 1](../images/SF-12-1.jpg) |
| [SF-13](#sf-13) | Minor (đã sửa) | Hồ sơ | /vi/profile | storefront | [Ảnh 1](../images/SF-13-1.png) |
| [SF-14](#sf-14) | Minor (đã sửa) | Nhiều trang | login, cart, orders · chi tiết đơn | storefront | [Ảnh 1](../images/SF-14-1.jpg) |
| [SF-15](#sf-15) | Minor (đã sửa) | 5 - Hủy đơn | Chi tiết đơn storefront | storefront | [Ảnh 1](../images/SF-15-1.jpg) |
| [SF-16](#sf-16) | Minor (đã đóng) | 1 - Đăng nhập | Form đăng nhập | storefront | [Ảnh 1](../images/SF-16-1.jpg) |
| [SF-17](#sf-17) | Minor (đã sửa) | Backoffice 2 - Hiển thị sách | Chi tiết sách storefront | storefront | [Ảnh 1](../images/SF-17-1.jpg) |
| [SF-18](#sf-18) | Minor (đã sửa) | 3 - Checkout COD | /checkout · chọn địa chỉ | storefront | [Ảnh 1](../images/SF-18-1.png) |
| [SF-19](#sf-19) | Minor (đã sửa) | 3 - Checkout COD | /checkout | storefront | [Ảnh 1](../images/SF-19-1.webp) |
| [SF-20](#sf-20) | Minor (đã sửa) | Giao diện điện thoại | Header · NotificationsMenu / AccountMenu | storefront | [Ảnh 1](../images/SF-20-1.png) |
| [SF-21](#sf-21) | Minor (đã sửa) | 2 - Danh mục, thêm giỏ | /books · BookCard | storefront | [Ảnh 1](../images/SF-21-1.jpg) |
| [SF-22](#sf-22) | Minor (đã sửa) | Đơn hàng và đổi/trả | /orders · bộ lọc đơn hàng, đổi/trả | storefront | [Ảnh 1](../images/SF-22-1.jpg) |
| [SF-23](#sf-23) | Minor (đã sửa) | 2 - Chi tiết sách | /detail/[...slug] · breadcrumb | storefront | [Ảnh 1](../images/SF-23-1.jpg) |
| [SF-24](#sf-24) | Minor (đã sửa) | Đơn hàng và thông báo | /orders · menu thông báo | storefront | [Ảnh 1](../images/SF-24-1.jpg), [Ảnh 2](../images/SF-24-2.jpg) |
| [SF-25](#sf-25) | Minor (đã sửa) | 8 - Giao diện điện thoại | Header · thanh điều hướng phụ | storefront | [Ảnh 1](../images/SF-25-1.jpg) |
| [SF-26](#sf-26) | Minor (đã sửa) | Điều hướng, xử lý trang không tồn tại | Đường dẫn không tồn tại dưới /vi | storefront | [Ảnh 1](../images/SF-26-1.jpg) |
| [SF-27](#sf-27) | Minor (đã sửa) | Điều hướng và tiêu đề trang | /cart, /orders, /search, /login, /register | storefront | [Bằng chứng nguồn](../fix-plans/storefront/SF-27.md#bằng-chứng) |

## SF-01

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `3ed6beb`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-01.md) |
| **Luồng** | 1 - Đăng nhập, đăng ký |
| **Endpoint / Màn hình** | POST /auth/login, /auth/register · route.ts |
| **Nghi ngờ thuộc** | storefront (route.ts) |
| **Bước tái hiện** | 1. Chạy storefront ở cổng khác 3000 (đã test 3003)<br>2. Đăng nhập hoặc đăng ký |
| **Mong đợi** | Proxy server-to-server không phụ thuộc CORS, như ghi chú trong route.ts |
| **Thực tế** | 403 body rỗng. Proxy chuyển tiếp header Origin, gateway từ chối vì chỉ cho phép localhost:3000 |
| **Bằng chứng (status/body)** | Gọi gateway với Origin :3003 -&gt; 403; Origin :3000 hoặc không Origin -&gt; 401 |
| **API Response** | 403, body rỗng |
| **Ảnh bằng chứng** | [SF-01-1.jpg](../images/SF-01-1.jpg)<br>[SF-01-2.jpg](../images/SF-01-2.jpg) |

## SF-02

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại. Đối chiếu Git/source ngày 2026-11-12. Xem [bản ghi sửa](../fix-plans/storefront-backend/SF-02.md). Backend [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`; storefront [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`. |
| **Bản sửa đã merge** | Backend `e3f5aad`, `0324996`; storefront `b59c5c6`. Địa chỉ nhận đúng 10 chữ số đầu 02/03/05/07/08/09; checkout chặn địa chỉ cũ sai, handler validation trả 400. |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | POST /api/v1/orders · form địa chỉ |
| **Nghi ngờ thuộc** | identity-service (địa chỉ) / order-service |
| **Bước tái hiện** | 1. Lưu địa chỉ với SĐT 0123456789 (form chấp nhận, 201)<br>2. Chọn COD, đặt hàng |
| **Mong đợi** | Form từ chối SĐT sai, hoặc đặt hàng trả lỗi 4xx rõ ràng |
| **Thực tế** | 500, toast báo kiểm tra tồn kho/địa chỉ. Đơn bị chặn vì SĐT |
| **Bằng chứng (status/body)** | ConstraintViolationException: recipientPhone must be a valid Vietnamese phone number Số điện thoại: địa chỉ dùng ^0[0-9]{9}&#36;, đơn hàng dùng ^(03&#124;05&#124;07&#124;08&#124;09&#124;02)[0-9]{8,9}&#36;. |
| **API Response** | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "fc68cfac-dacf-4bd5-bd52-f7f24e44912a",<br>  "path": "/api/v1/orders",<br>  "timestamp": "2026-11-10T03:25:26.050267100Z"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-02-1.jpg](../images/SF-02-1.jpg) |

## SF-03

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại. Đối chiếu Git/source ngày 2026-11-12. Xem [bản ghi sửa](../fix-plans/backend/SF-03.md). Backend [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`. |
| **Bản sửa đã merge** | Backend `0c9fe1d`: thêm logger, traceId và stack trace cho lỗi 500; chưa quan sát log runtime sau sửa. |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | order-service GlobalExceptionHandler |
| **Nghi ngờ thuộc** | order-service |
| **Bước tái hiện** | Gây bất kỳ lỗi 500 nào ở order-service rồi xem log |
| **Mong đợi** | Log có exception và traceId |
| **Thực tế** | Không có dòng log nào, traceId không tra được |
| **Bằng chứng (status/body)** | handleUnexpected không gọi log; phải bật SPRING_MVC_LOG_RESOLVED_EXCEPTION mới thấy |
| **API Response** | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "fc68cfac-dacf-4bd5-bd52-f7f24e44912a",<br>  "path": "/api/v1/orders",<br>  "timestamp": "2026-11-10T03:25:26.050267100Z"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-03-1.png](../images/SF-03-1.png) |

## SF-04

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa theo xác nhận của người dùng ngày 2026-11-12; chưa đối chiếu commit/PR, chưa kiểm thử lại trong lần cập nhật này. Xem [kế hoạch](../fix-plans/backend-platform/SF-04.md). Bước tái hiện, response và ảnh dưới đây là bằng chứng trước khi sửa. |
| **Luồng** | Khởi động môi trường |
| **Endpoint / Màn hình** | taschen-backend/dev.ps1 |
| **Nghi ngờ thuộc** | backend (dev.ps1) |
| **Bước tái hiện** | Chạy ./dev.ps1 start |
| **Mong đợi** | notification-service chạy với Mongo trong taschen-platform/.env |
| **Thực tế** | Crash: kết nối localhost:27017. dev.ps1 chỉ đặt MONGO_URI, service đọc NOTIFICATION_MONGO_URI |
| **Bằng chứng (status/body)** | MongoSocketOpenException, Application run failed |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-04-1.png](../images/SF-04-1.png) |

## SF-05

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `3ed6beb`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-05.md) |
| **Luồng** | 2 - Giỏ hàng |
| **Endpoint / Màn hình** | Mọi trang storefront · lib/auth/token.ts |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Đăng nhập<br>2. Tải lại trang (F5)<br>3. Thêm sách vào giỏ<br>4. Mở /cart bằng URL |
| **Mong đợi** | Giữ phiên đăng nhập và giỏ hàng |
| **Thực tế** | Mất phiên, không báo cho người dùng. Vẫn báo đã thêm vào giỏ, nhưng giỏ trống sau khi tải lại |
| **Bằng chứng (status/body)** | token.ts ghi rõ token chỉ giữ trong bộ nhớ; cần xác nhận có phải chủ đích |
| **API Response** | GET /users/me: 401. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [SF-05-1.jpg](../images/SF-05-1.jpg)<br>[SF-05-2.jpg](../images/SF-05-2.jpg) |

## SF-06

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Luồng** | 1 - Đăng ký |
| **Endpoint / Màn hình** | Mailpit · notification-service |
| **Nghi ngờ thuộc** | backend / hạ tầng |
| **Bước tái hiện** | 1. Đăng ký tài khoản mới<br>2. Mở Mailpit |
| **Mong đợi** | Có email xác thực |
| **Thực tế** | Đăng ký 201 nhưng chỉ 1 trong 4 email đến Mailpit, các email còn lại không thấy. Nghi có consumer khác trên CloudAMQP dùng chung nhận mất, chưa xác nhận |
| **Bằng chứng (status/body)** | Mailpit có 1 thư (tc09@taschen.test) sau 4 lần đăng ký |
| **API Response** | POST /auth/register: 201. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [SF-06-1.jpg](../images/SF-06-1.jpg) |

## SF-07

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại. Đối chiếu Git/source ngày 2026-11-12. Xem [bản ghi sửa](../fix-plans/storefront-backend/SF-07.md). Backend [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`; storefront [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`. |
| **Bản sửa đã merge** | Backend `afaec9a`, `e3ee8c2`, `32f5dd4`; storefront `4e923d7`. Sửa endpoint/response payment, chuỗi ký URL-encode, giữ query khi thêm locale và điều hướng trang kết quả. |
| **Luồng** | 4 - Checkout VNPAY |
| **Endpoint / Màn hình** | POST /orders/{id}/payments/initiate |
| **Nghi ngờ thuộc** | order-service / payment-service |
| **Bước tái hiện** | 1. Chọn VNPay<br>2. Đặt hàng |
| **Mong đợi** | Chuyển sang cổng VNPAY sandbox |
| **Thực tế** | 500, không chuyển trang. Đang dùng mã demo mặc định, nguyên nhân chưa xác định |
| **Bằng chứng (status/body)** | AppException INTERNAL_ERROR ở order-service Đọc code: PaymentServiceClient gọi POST /vnpay, PaymentController không có endpoint này. |
| **API Response** | <pre>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>  "message": "Something went wrong. Please try again later.",<br>  "traceId": "6674dbdf-5950-4e69-8712-1a8ca516cd56",<br>  "path": "/api/v1/orders/19/payments/initiate",<br>  "timestamp": "2026-11-10T03:46:41.520610300Z"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-07-1.jpg](../images/SF-07-1.jpg) |

## SF-08

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại. Đối chiếu Git/source ngày 2026-11-12. Xem [bản ghi sửa](../fix-plans/storefront-backend/SF-08.md). Backend [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`; storefront [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`. |
| **Bản sửa đã merge** | Backend `e4b317a`, `afaec9a`; storefront `0bfd28a`. Thêm endpoint khuyến mãi theo ID có token nội bộ, sửa Feign/valid và giải thích lỗi mã trên UI. |
| **Luồng** | 7 - Khuyến mãi |
| **Endpoint / Màn hình** | POST /api/v1/orders có mã |
| **Nghi ngờ thuộc** | order-service / promotion-service |
| **Bước tái hiện** | 1. Áp mã đã duyệt, hiện giảm 2.500 đ<br>2. Chọn COD, đặt hàng |
| **Mong đợi** | Đơn tạo với tổng đã giảm |
| **Thực tế** | 400 VALIDATION_ERROR. Cùng giỏ hàng, bỏ mã thì 201. Trên UI không hiện lý do |
| **Bằng chứng (status/body)** | Validate mã trả valid:true ngay trước đó Đọc code: PromotionServiceClient gọi POST /validate, PromotionController chỉ có GET /validate/{code}. |
| **API Response** | <pre>Validate<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": true,<br>    "promotionId": 27,<br>    "code": "MANUAL1110",<br>    "discountPercent": 10.0,<br>    "discountAmount": 2500.0,<br>    "reason": null<br>  },<br>  "message": "OK"<br>}<br><br>Đặt hàng<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "8747696b-1ce3-45a0-ae34-7c71eaba04b5",<br>  "path": "/api/v1/orders",<br>  "timestamp": "2026-11-10T03:45:01.694559600Z"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-08-1.jpg](../images/SF-08-1.jpg)<br>[SF-08-2.jpg](../images/SF-08-2.jpg) |

## SF-09

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Luồng** | 1 - Xác thực email |
| **Endpoint / Màn hình** | Email xác thực · notification-service |
| **Nghi ngờ thuộc** | notification-service (cấu hình link) |
| **Bước tái hiện** | 1. Đăng ký<br>2. Mở email trong Mailpit, bấm liên kết |
| **Mong đợi** | Liên kết mở được hệ thống đang chạy |
| **Thực tế** | Liên kết trỏ tới https://api.taschen.example/... là địa chỉ giả, không mở được. Phải dùng mã trong email |
| **Bằng chứng (status/body)** | Nội dung email trong Mailpit |
| **API Response** | <pre>GET /auth/verify qua proxy local<br>HTTP 200<br>{<br>  "success": true,<br>  "data": null,<br>  "message": "OK"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-09-1.jpg](../images/SF-09-1.jpg) |

## SF-10

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại. Đối chiếu Git/source ngày 2026-11-12. Xem [bản ghi sửa](../fix-plans/storefront-backend/SF-10.md). Backend [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`; storefront [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`. |
| **Bản sửa đã merge** | Backend `e3f5aad`, `0324996`; storefront `b59c5c6`. Đồng bộ kiểm tra ký tự tên/các phần địa chỉ, chặn địa chỉ cũ sai tại checkout. |
| **Luồng** | Địa chỉ, đặt hàng |
| **Endpoint / Màn hình** | POST /users/me/addresses |
| **Nghi ngờ thuộc** | identity-service / storefront |
| **Bước tái hiện** | Lưu địa chỉ người nhận "Test@#" |
| **Mong đợi** | Từ chối ngay tại form |
| **Thực tế** | 201 lưu thành công, trong khi đơn hàng cấm ký tự đặc biệt ở tên người nhận nên sẽ lỗi khi đặt hàng. Chưa chạy bước đặt hàng với địa chỉ này |
| **Bằng chứng (status/body)** | Order.java:54 và Storefront-HD-Địa chỉ TC03 |
| **API Response** | <pre>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 25,<br>    "recipientName": "Test@#",<br>    "phoneNumber": "0912345678",<br>    "isDefault": false<br>  },<br>  "message": "OK"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-10-1.jpg](../images/SF-10-1.jpg) |

## SF-11

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `534cb69`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-11.md) |
| **Luồng** | 1 - Đăng nhập |
| **Endpoint / Màn hình** | Trang đăng nhập |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Đăng nhập khi gateway trả 403 vì lý do khác (như bug SF-01) |
| **Mong đợi** | Thông báo đúng nguyên nhân |
| **Thực tế** | Báo "Tài khoản này chưa xác thực email" dù tài khoản đã VERIFIED |
| **Bằng chứng (status/body)** | POST login 403; hồ sơ hiện VERIFIED |
| **API Response** | 403, body rỗng |
| **Ảnh bằng chứng** | [SF-11-1.jpg](../images/SF-11-1.jpg) |

## SF-12

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa theo xác nhận của người dùng ngày 2026-11-12; chưa đối chiếu commit/PR, chưa kiểm thử lại trong lần cập nhật này. Xem [kế hoạch](../fix-plans/backend-platform/SF-12.md). Bước tái hiện, response và ảnh dưới đây là bằng chứng trước khi sửa. |
| **Luồng** | Trang chủ, chi tiết sách |
| **Endpoint / Màn hình** | /recommendations/*, POST /events |
| **Nghi ngờ thuộc** | backend (dev.ps1) |
| **Bước tái hiện** | Mở trang chủ hoặc chi tiết sách khi chạy bằng dev.ps1 |
| **Mong đợi** | Không có lỗi 500 |
| **Thực tế** | Các API gợi ý và tracking trả 500, trang vẫn hiển thị |
| **Bằng chứng (status/body)** | Nghi do dev.ps1 không khởi động tracking-service, chưa xác nhận |
| **API Response** | 500. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [SF-12-1.jpg](../images/SF-12-1.jpg) |

## SF-13

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `278146b`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-13.md) |
| **Luồng** | Hồ sơ |
| **Endpoint / Màn hình** | /vi/profile |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Mở Tài khoản của tôi |
| **Mong đợi** | Thương hiệu Velora trên toàn bộ giao diện, tiêu đề đúng |
| **Thực tế** | Header, footer và tiêu đề tab ghi "Taschen", trong khi trang hồ sơ ghi "Velora". Tiêu đề "Hồ sơ của tôi" lỗi hiển thị dấu |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-13-1.png](../images/SF-13-1.png) |

## SF-14

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `278146b`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-14.md) |
| **Luồng** | Nhiều trang |
| **Endpoint / Màn hình** | login, cart, orders · chi tiết đơn |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Xem tiêu đề tab, trạng thái đơn |
| **Mong đợi** | Tiêu đề riêng từng trang, trạng thái tiếng Việt |
| **Thực tế** | Tiêu đề tab là "Book Store". Trạng thái hiện PENDING, UNPAID |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-14-1.jpg](../images/SF-14-1.jpg) |

## SF-15

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `be16d74`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-15.md) |
| **Luồng** | 5 - Hủy đơn |
| **Endpoint / Màn hình** | Chi tiết đơn storefront |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Bấm Huỷ đơn |
| **Mong đợi** | Hỏi xác nhận trước khi hủy |
| **Thực tế** | Hủy ngay sau một lần bấm, không thể hoàn tác. Seller thì có hộp xác nhận |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 18,<br>    "orderCode": "ORD-20261110-000021",<br>    "status": "CANCELLED",<br>    "paymentStatus": "UNPAID",<br>    "paymentMethod": "COD",<br>    "totalAmount": 25000.0<br>  },<br>  "message": "OK"<br>}<br>(đã rút gọn)</pre> |
| **Ảnh bằng chứng** | [SF-15-1.jpg](../images/SF-15-1.jpg) |

## SF-16

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Luồng** | 1 - Đăng nhập |
| **Trạng thái** | Đã đóng ngày 2026-11-10: hoạt động đúng, test case đặt sai mong đợi. Xem [kế hoạch](../fix-plans/storefront/SF-16.md) |
| **Endpoint / Màn hình** | Form đăng nhập |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Nhập mật khẩu 5 ký tự, bấm đăng nhập |
| **Mong đợi** | Form báo tối thiểu 6 ký tự, không gọi API |
| **Thực tế** | Form không chặn, vẫn gửi API và nhận 401 |
| **Bằng chứng (status/body)** | Storefront-HD-Đăng nhập TC09 |
| **API Response** | <pre>HTTP 401<br>{<br>  "success": false,<br>  "code": "UNAUTHORIZED",<br>  "message": "Authentication is required to access this resource.",<br>  "traceId": "f4b1efaec5f34ea4",<br>  "path": "/api/v1/auth/login"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-16-1.jpg](../images/SF-16-1.jpg) |

## SF-17

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `a8ab9a5`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](../fix-plans/storefront/SF-17.md) |
| **Luồng** | Backoffice 2 - Hiển thị sách |
| **Endpoint / Màn hình** | Chi tiết sách storefront |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Mở sách chưa nhập năm và số trang |
| **Mong đợi** | Hiện "Chưa cập nhật" hoặc ẩn đi |
| **Thực tế** | Số trang và năm xuất bản hiện 0, khối lượng 0 g |
| **Bằng chứng (status/body)** | Ảnh chi tiết sách id 50 |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-17-1.jpg](../images/SF-17-1.jpg) |

## SF-18

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `494e90b` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-18.md). |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | /checkout · chọn địa chỉ |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Đăng nhập, có giỏ hàng và địa chỉ chứa chuỗi dài không có dấu cách (500 ký tự)<br>2. Mở checkout ở chiều rộng 390px |
| **Mong đợi** | Địa chỉ xuống dòng trong khung, trang không cuộn ngang |
| **Thực tế** | Chuỗi địa chỉ chạy qua mép phải màn hình |
| **Bằng chứng (status/body)** | Ảnh dựng lại lỗi trên code trước bản sửa theo bàn giao; đã kiểm tra nội dung ảnh. Không phải ảnh chụp bản hiện tại. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-18-1.png) |

## SF-19

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `093e1bd` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-19.md). |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | /checkout |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Đăng nhập, thêm sách vào giỏ<br>2. Mở trang thanh toán trên desktop |
| **Mong đợi** | Nội dung có khoảng cách hai bên và căn theo container chung của website |
| **Thực tế** | Nội dung thanh toán sát mép, không thẳng hàng với header |
| **Bằng chứng (status/body)** | Ảnh người dùng cung cấp; đã kiểm tra nội dung ảnh. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-19-1.webp) |

## SF-20

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `0e497d7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-20.md). |
| **Luồng** | Giao diện điện thoại |
| **Endpoint / Màn hình** | Header · NotificationsMenu / AccountMenu |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở storefront trên điện thoại<br>2. Bấm biểu tượng thông báo trên header |
| **Mong đợi** | Khung thông báo nằm trọn trong viewport, đọc và bấm được nội dung |
| **Thực tế** | Khung lệch ra ngoài mép trái, nội dung bị cắt |
| **Bằng chứng (status/body)** | Ảnh người dùng cung cấp; đã kiểm tra nội dung ảnh. Ảnh minh họa thông báo; phạm vi sửa còn bao gồm khung tài khoản. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-20-1.png) |

## SF-21

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `ee742a1` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-21.md). |
| **Luồng** | 2 - Danh mục, thêm giỏ |
| **Endpoint / Màn hình** | /books · BookCard |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở danh mục sách trên điện thoại cảm ứng<br>2. Quan sát và thao tác trên thẻ sách |
| **Mong đợi** | Có thể nhìn thấy và bấm nút yêu thích, thêm giỏ mà không cần hover |
| **Thực tế** | Các nút bị ẩn khi không hover; điện thoại không có thao tác rê chuột |
| **Bằng chứng (status/body)** | Ảnh cho thấy thẻ sách không có nút thao tác; nguyên nhân được đối chiếu trong diff commit. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-21-1.jpg) |

## SF-22

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-22.md). |
| **Luồng** | Đơn hàng và đổi/trả |
| **Endpoint / Màn hình** | /orders · bộ lọc đơn hàng, đổi/trả |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Đăng nhập, mở /vi/orders<br>2. Xem chip lọc ở tab Đơn hàng và Đổi/Trả |
| **Mong đợi** | Nhãn trạng thái tiếng Việt; URL/API vẫn dùng mã trạng thái |
| **Thực tế** | Chip hiển thị mã PENDING, CONFIRMED, PROCESSING… |
| **Bằng chứng (status/body)** | Ảnh minh họa tab Đơn hàng; diff xác nhận sửa cả bộ lọc đổi/trả. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-22-1.jpg) |

## SF-23

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-23.md). |
| **Luồng** | 2 - Chi tiết sách |
| **Endpoint / Màn hình** | /detail/[...slug] · breadcrumb |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở chi tiết sách có tên và danh mục dài<br>2. Thu viewport xuống 375px |
| **Mong đợi** | Các mục breadcrumb tách rõ, được xuống dòng khi thiếu chỗ |
| **Thực tế** | Tên danh mục và tên sách chồng lên nhau |
| **Bằng chứng (status/body)** | Ảnh minh họa chi tiết sách Tư Duy Python ở viewport điện thoại. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-23-1.jpg) |

## SF-24

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-24.md). |
| **Luồng** | Đơn hàng và thông báo |
| **Endpoint / Màn hình** | /orders · menu thông báo |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Đăng xuất hoặc mở phiên khách<br>2. Mở /vi/orders<br>3. Mở menu thông báo |
| **Mong đợi** | Nhắc đăng nhập và có liên kết đăng nhập |
| **Thực tế** | Hiển thị “Bạn chưa có đơn hàng”, “Bạn chưa có thông báo” như tài khoản đã đăng nhập nhưng chưa có dữ liệu |
| **Bằng chứng (status/body)** | Hai ảnh từ phiên khách theo bàn giao; ảnh riêng lẻ không tự chứng minh trạng thái phiên. Diff xác nhận nhánh giao diện trước đây thiếu phân biệt khách. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-24-1.jpg), [Ảnh 2](../images/SF-24-2.jpg) |

## SF-25

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-25.md). |
| **Luồng** | 8 - Giao diện điện thoại |
| **Endpoint / Màn hình** | Header · thanh điều hướng phụ |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở trang chủ ở chiều rộng khoảng 375–413px<br>2. Xem hàng “Tất cả danh mục”, “Theo dõi đơn”, “Hỗ trợ” |
| **Mong đợi** | Tên danh mục không bị bẻ dòng khó đọc, các liên kết truy cập được bằng cuộn ngang khi thiếu chỗ |
| **Thực tế** | “Tất cả danh mục” xuống dòng, các mục còn lại chật và bị cắt ở cuối |
| **Bằng chứng (status/body)** | Ảnh SF-25-1.jpg; triệu chứng cũng đã được ghi chú trong luồng giao diện điện thoại của đợt 10/11. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-25-1.jpg) |

## SF-26

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-26.md). |
| **Luồng** | Điều hướng, xử lý trang không tồn tại |
| **Endpoint / Màn hình** | Đường dẫn không tồn tại dưới /vi |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở một đường dẫn không tồn tại, ví dụ /vi/khong-co-trang-nay |
| **Mong đợi** | Trang lỗi của Velora có thông báo tiếng Việt và điều hướng của cửa hàng |
| **Thực tế** | Trang 404 mặc định của Next.js, không có header của cửa hàng |
| **Bằng chứng (status/body)** | Ảnh 320×240 hiển thị “404 / This page could not be found.”; ảnh không chứa URL, đường dẫn tái hiện dựa trên test trong commit. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | [Ảnh 1](../images/SF-26-1.jpg) |

## SF-27

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](../fix-plans/storefront/SF-27.md). |
| **Luồng** | Điều hướng và tiêu đề trang |
| **Endpoint / Màn hình** | /cart, /orders, /search, /login, /register |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở lần lượt giỏ, đơn hàng, tìm kiếm, đăng nhập và đăng ký<br>2. Đọc document.title hoặc dùng await page.title() |
| **Mong đợi** | Mỗi trang có tiêu đề riêng gắn với Velora |
| **Thực tế** | Các trang dùng tiêu đề mặc định chung do không khai báo metadata riêng |
| **Bằng chứng (status/body)** | Không có ảnh và chưa lưu kết quả page.title(). Bằng chứng nguồn: layout locale đặt title chung; commit b771af7 bổ sung 5 layout metadata. Test đơn hàng có assertion toHaveTitle("Đơn hàng &#124; Velora"); chưa chạy lại trong đợt ghi nhận này. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | Không có; xem bằng chứng nguồn ở kế hoạch, cần bổ sung kết quả page.title(). |

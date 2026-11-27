# SF-06: Email xác thực đến không ổn định

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Xác định điểm gián đoạn của luồng gửi mail |
| **Repo** | `taschen-platform`, `taschen-backend` nếu xác nhận lỗi tại consumer hoặc SMTP |
| **Khối lượng** | Cấu hình |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-06), [Ảnh 1](../../images/SF-06-1.jpg) |

## Nguyên nhân (nghi ngờ, chưa xác nhận)

Trong lúc kiểm thử, chỉ 1 trong 4 lần đăng ký có email về Mailpit, và trong Mailpit còn có email gửi cho một địa chỉ lạ không thuộc đợt test. Điều này cho thấy queue trên CloudAMQP đang được chia sẻ: nhiều notification-service của máy khác cùng tiêu thụ một queue, và sự kiện nào rơi vào máy khác thì không tới Mailpit của máy này.

Chưa có quyền xem danh sách consumer, nên đây vẫn là suy luận.

## Thay đổi

### 1. Đối chiếu luồng và xác nhận trên trang quản trị CloudAMQP

Theo một lần đăng ký qua `UserRegisteredEvent`, lần nhận ở notification-service và kết quả SMTP/Mailpit. Ghi ID tương quan và thời gian từng bước.

Mở queue của notification-service và xem số consumer. Nếu lớn hơn 1 khi chỉ một máy đang chạy service, nguyên nhân đã được xác nhận.

### 2. `taschen-platform/.env` (tệp trên máy, không commit)

Tạo vhost riêng cho môi trường này trên CloudAMQP, rồi đặt biến `RABBITMQ_VHOST` sang vhost đó. `dev.ps1:90` và `.env.example:50` đã hỗ trợ biến này.

**Vì sao không sửa code:** logic gửi email chạy đúng ở những lần sự kiện tới đúng máy. Đổi vhost tách hoàn toàn hàng đợi, không cần đổi tên exchange hay queue. Mọi service phải chuyển vhost cùng lúc, nếu không bên phát và bên nhận sẽ không gặp nhau.

### 3. Xử lý theo bước thất bại

Nếu cấu hình hoặc binding sai, sửa ở cấu hình tương ứng. Nếu xác nhận SMTP hoặc consumer thất bại tạm thời, dùng cơ chế thử lại sẵn có trước khi thêm mới. Kiểm việc nhận lại cùng sự kiện và tránh gửi trùng.

## File mới

Không có.

## Kiểm thử lại

- Sau khi đổi vhost, số consumer của queue là 1.
- Đăng ký 4 tài khoản liên tiếp, Mailpit phải nhận đủ 4 email và không có email lạ.
- Thử gián đoạn SMTP trong môi trường test rồi khôi phục. Ghi thời gian nhận và kiểm số thư cho từng tài khoản.
- Chạy lại luồng 1 trong [HD Đăng ký](../../storefront/hd-dang-ky.md).

## Tuân thủ quy tắc

`.env` không vào git. Không dán chuỗi kết nối CloudAMQP vào PR hay báo cáo.

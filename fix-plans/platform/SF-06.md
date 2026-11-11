# SF-06: Email xác thực đến không ổn định

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. **Không cần sửa code**, cần xác nhận hạ tầng |
| **Repo** | Không có thay đổi code. Chỉ đổi `taschen-platform/.env` trên máy |
| **Khối lượng** | Cấu hình |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-06), [Ảnh 1](../../images/SF-06-1.jpg) |

## Nguyên nhân (nghi ngờ, chưa xác nhận)

Trong lúc kiểm thử, chỉ 1 trong 4 lần đăng ký có email về Mailpit, và trong Mailpit còn có email gửi cho một địa chỉ lạ không thuộc đợt test. Điều này cho thấy queue trên CloudAMQP đang được chia sẻ: nhiều notification-service của máy khác cùng tiêu thụ một queue, và sự kiện nào rơi vào máy khác thì không tới Mailpit của máy này.

Chưa có quyền xem danh sách consumer, nên đây vẫn là suy luận.

## Thay đổi

### 1. Xác nhận trên trang quản trị CloudAMQP

Mở queue của notification-service và xem số consumer. Nếu lớn hơn 1 khi chỉ một máy đang chạy service, nguyên nhân đã được xác nhận.

### 2. `taschen-platform/.env` (tệp trên máy, không commit)

Tạo vhost riêng cho môi trường này trên CloudAMQP, rồi đặt biến `RABBITMQ_VHOST` sang vhost đó. `dev.ps1:90` và `.env.example:50` đã hỗ trợ biến này.

**Vì sao không sửa code:** logic gửi email chạy đúng ở những lần sự kiện tới đúng máy. Đổi vhost tách hoàn toàn hàng đợi, không cần đổi tên exchange hay queue. Mọi service phải chuyển vhost cùng lúc, nếu không bên phát và bên nhận sẽ không gặp nhau.

## File mới

Không có.

## Kiểm thử lại

- Sau khi đổi vhost, số consumer của queue là 1.
- Đăng ký 4 tài khoản liên tiếp, Mailpit phải nhận đủ 4 email và không có email lạ.
- Chạy lại luồng 1 trong [HD Đăng ký](../../storefront/hd-dang-ky.md).

## Tuân thủ quy tắc

`.env` không vào git. Không dán chuỗi kết nối CloudAMQP vào PR hay báo cáo.

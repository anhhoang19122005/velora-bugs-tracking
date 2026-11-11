# SF-09: Link trong email xác thực trỏ tới địa chỉ giả

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend` (`1364ff5`), `taschen-platform` (`44f48b2`) |
| **Nhánh đề xuất** | `fix/verify-email-link` ở từng repo |
| **Khối lượng** | 4 dòng cấu hình |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-09), [Ảnh 1](../../images/SF-09-1.jpg) |

## Nguyên nhân

`notification-service/application.yml:48` đọc biến `VERIFY_URL_PREFIX`, nếu thiếu thì dùng `https://api.taschen.example/...`. `dev.ps1` không truyền biến này nên email có link không tồn tại.

`docker-compose.yml:455` có đặt biến, nhưng lại trỏ thẳng vào API gateway. Người dùng bấm link sẽ thấy JSON thô, không phải trang web.

Storefront đã có trang đúng: `verify-email/page.tsx:30-37` đọc `token` trên URL và tự gọi API xác thực. Phần `&userId=` do `EmailServiceImpl.java:35` nối thêm thì trang này bỏ qua, không gây lỗi.

## Thay đổi

### 1. `taschen-backend/dev.ps1`, sau dòng 98

```diff
   VNPAY_RETURN_URL = $envVars.VNPAY_RETURN_URL
+  VERIFY_URL_PREFIX = $envVars.VERIFY_URL_PREFIX
```

**Vì sao:** bảng biến dùng chung này là nơi duy nhất đưa biến từ `.env` vào service. Vòng lặp ở dòng 105 bỏ qua biến rỗng, nên `.env` cũ không gây lỗi mới.

### 2. `taschen-platform/.env.example`, thêm cạnh khối cấu hình mail

```text
VERIFY_URL_PREFIX=http://localhost:3000/vi/verify-email?token=   # storefront page; the service appends the token
```

Thêm dòng tương tự vào `taschen-platform/.env` trên máy. Nếu storefront chạy port khác thì đổi port theo.

### 3. `taschen-platform/docker-compose.yml`, dòng 455

```diff
-      VERIFY_URL_PREFIX: "http://localhost:8080/api/v1/auth/verify?token="
+      VERIFY_URL_PREFIX: ${VERIFY_URL_PREFIX:-http://localhost:3000/vi/verify-email?token=}
```

**Vì sao trỏ tới storefront:** trang này hiển thị kết quả và có nút gửi lại email, còn API chỉ trả JSON.

**Vì sao không đổi giá trị mặc định trong `application.yml:48` và `EmailServiceImpl.java:30`:** mỗi môi trường có domain khác nhau, nên đây phải là cấu hình theo môi trường. Việc cần ghi nhớ là khi deploy phải đặt biến này.

## File mới

Không có.

## Kiểm thử lại

- Đăng ký tài khoản, mở email trong Mailpit, link phải bắt đầu bằng địa chỉ storefront.
- Bấm link: trang báo xác thực thành công, đăng nhập được.
- Chạy lại luồng 1, test case liên quan trong [HD Đăng ký](../../storefront/hd-dang-ky.md).
- `e2e/api/storefront.spec.ts:91` đang kiểm tra trang này, chạy lại để chắc chắn.

## Tuân thủ quy tắc

Chỉ `.env.example` được commit, `.env` thì không. API không đổi nên không cần sinh lại contract.

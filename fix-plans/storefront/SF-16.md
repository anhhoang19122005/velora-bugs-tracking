# SF-16: Mật khẩu 5 ký tự vẫn được gửi lên API khi đăng nhập

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | **Đã đóng** ngày 2026-11-10, lý do: hoạt động đúng, lỗi nằm ở test case |
| **Repo** | Không đổi code |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-16), [Ảnh 1](../../images/SF-16-1.jpg) |

## Vì sao đóng

Form đăng nhập không có quy tắc độ dài mật khẩu ở bất kỳ đâu:

- `src/app/[locale]/(auth)/login/page.tsx:34` chỉ yêu cầu không để trống.
- `LoginRequest` của identity-service chỉ có `@NotBlank` cho mật khẩu.
- `taschen-documents` (`activity/auth/login.md`, `sequence/auth/login.md`, README xác thực) không ghi giới hạn độ dài khi đăng nhập.

## Vì sao từng bị ghi là bug

TC09 được thiết kế với mong đợi "báo tối thiểu 6 ký tự, không gọi API", mà không đối chiếu với yêu cầu. Con số 6 nhiều khả năng lấy từ `min(6)` tại `src/modules/auth/components/login-form.tsx:25`, là component không còn được dùng.

## Đã cập nhật

| Nơi | Thay đổi |
|---|---|
| [Danh sách lỗi](../../storefront/loi.md#sf-16) | Đánh dấu đã đóng, giữ lại để tra cứu |
| [HD Đăng nhập](../../storefront/hd-dang-nhap.md) | Sửa bảng phân tích và TC09, TC09 thành Pass |
| [Tổng kết](../../tong-ket.md) | Lỗi Minor 13, hộp đen Pass 91 và Fail 16 |

## Thay đổi code

Không có. Nếu sau này có yêu cầu chặn độ dài khi đăng nhập, sửa `.min(1, ...)` tại `login/page.tsx:34` và mở bug mới.

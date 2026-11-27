# SF-34: Ô mã khuyến mãi phân biệt hoa thường

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa, cần xác nhận nghiệp vụ |
| **Repo** | promotion-service, `taschen-storefront` |
| **Bug** | [Chi tiết SF-34](../../storefront/loi.md#sf-34) |
| **Điểm vào source** | `PromotionServiceImpl`, `form mã giảm giá` |

## Nguyên nhân

Cùng một mã có thể được lưu với chữ thường nhưng checkout lại tìm theo cách phân biệt hoa thường.

## Thay đổi

1. Đề xuất chuẩn hóa bằng trim và viết hoa với Locale.ROOT tại biên Promotion, dùng cùng quy tắc cho tạo/sửa/tìm. Hiển thị quy tắc bên UI sau khi được duyệt.
2. Rà va chạm mã cũ, xử lý danh sách xung đột trước khi migration hoặc thêm uniqueness. Phối hợp giới hạn ký tự/độ dài ở BO-08.
3. Nếu giữ phân biệt hoa thường, làm rõ chính sách ở form thay vì chuẩn hóa mã đã lưu.

## Kiểm thử lại

Theo chính sách được duyệt, mã viết thường và viết hoa tra cùng chương trình hoặc UI báo rõ quy tắc. Kiểm mã cũ, mã trùng sau chuẩn hóa và mã có khoảng trắng bên trong.

## Liên quan

[BO-08](../../fix-plans/backend/BO-08-promotion-code-format-length.md)

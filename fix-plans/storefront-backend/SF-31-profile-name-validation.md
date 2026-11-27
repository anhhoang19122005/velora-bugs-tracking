# SF-31: Tên hồ sơ nhận ký tự đặc biệt như `<script>`

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | identity-service, `taschen-storefront` |
| **Bug** | [Chi tiết SF-31](../../storefront/loi.md#sf-31) |
| **Điểm vào source** | `DTO cập nhật hồ sơ`, `schema form hồ sơ` |

## Nguyên nhân

Tên hồ sơ có thể lưu chuỗi đánh dấu HTML trong khi tên người nhận đã có quy tắc kiểm ở SF-10.

## Thay đổi

1. Đối chiếu quy tắc tên hồ sơ với tên người nhận. Dùng lại constraint hiện có nếu hai trường cùng quy tắc. Áp dụng ở DTO cập nhật hồ sơ.
2. Đồng bộ schema và thông báo theo trường ở form. Kiểm tên có dấu và dữ liệu hồ sơ cũ khi người dùng cập nhật.

## Kiểm thử lại

Tên có dấu hợp lệ lưu được. Chuỗi chứa markup bị từ chối. Kiểm cả UI và API.

## Liên quan

[SF-10](../../fix-plans/storefront-backend/SF-10-address-special-chars-order-fails.md)

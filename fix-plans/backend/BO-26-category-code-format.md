# BO-26: Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | catalog-service, `taschen-backoffice` |
| **Bug** | [Chi tiết BO-26](../../backoffice/loi.md#bo-26) · GM01-06, GM05-06 |
| **Điểm vào source** | `DTO danh mục`, `category.schema.ts` |

## Nguyên nhân

Phạm vi BO-26 ở đây là mã danh mục. Catalog nhận mã chữ thường và dấu cách dù form và hướng dẫn yêu cầu định dạng khác.

## Thay đổi

1. Dùng chung quy tắc đã chốt trên DTO tạo/sửa. Đồng bộ category.schema.ts và nội dung Guide me, giữ thông báo gắn với trường mã.
2. Kiểm dữ liệu cũ trước khi đổi chuẩn hoặc thêm unique. Phần mã khuyến mãi chạy theo BO-08.

## Code dự kiến

Ở DTO tạo/sửa danh mục, dùng cùng quy tắc đã chốt và nối lỗi tới trường Code. Tên hằng minh họa bộ ký tự cần thống nhất với category.schema.ts.

```java
@NotBlank
@Size(max = CategoryCodeRules.MAX_LENGTH)
@Pattern(regexp = CategoryCodeRules.FORMAT)
String code
```

## Kiểm thử lại

Mã không đúng định dạng bị từ chối theo cùng cách trên UI/API. Mã đúng tạo/sửa được. Case phần Promotion chạy theo BO-08.

## Liên quan

[BO-08](../../fix-plans/backend/BO-08-promotion-code-format-length.md)

# BO-08: Mã khuyến mãi không kiểm định dạng và độ dài

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | promotion-service, `taschen-backoffice` |
| **Bug** | [Chi tiết BO-08](../../backoffice/loi.md#bo-08) |
| **Điểm vào source** | `DTO tạo/sửa Promotion`, `promotion.schema.ts` |

## Nguyên nhân

Promotion lưu mã có khoảng trắng hoặc quá dài, trong khi checkout và hướng dẫn đòi mã có định dạng chặt hơn.

## Thay đổi

1. Chốt bộ ký tự và độ dài theo nghiệp vụ/cột dữ liệu. Đặt validation ở DTO tạo/sửa, đồng bộ Zod và lỗi tại ô Code.
2. Rà mã đang tồn tại và kiểm áp mã sau sửa. Phối hợp SF-34 đối với chính sách hoa thường.

## Code dự kiến

Trên field code của DTO create/update, dùng cùng hằng giới hạn và biểu thức đã chốt. Nếu SF-34 duyệt chuẩn hóa thì áp quy tắc ở cùng điểm trước lưu và tra cứu, đồng bộ Zod.

```java
@NotBlank
@Size(max = PromotionCodeRules.MAX_LENGTH)
@Pattern(regexp = PromotionCodeRules.FORMAT)
String code
```

## Kiểm thử lại

Mã quá dài, ký tự cấm và dấu cách ở giữa bị chặn với lỗi trường. Mã hợp lệ tạo/sửa được và áp đúng ở checkout.

## Liên quan

[SF-34](../../fix-plans/storefront-backend/SF-34-promotion-code-case-policy.md) · [B08](../../fix-plans/backend/B08-category-code-format.md)

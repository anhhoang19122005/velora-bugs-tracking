# BO-18: Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết BO-18](../../backoffice/loi.md#bo-18) · GM05-05 |
| **Điểm vào source** | `Guide me Promotion`, `promotion.schema.ts` |

## Nguyên nhân

Tip gợi ý để trống số lượt trong khi form và API bắt buộc.

## Thay đổi

1. Sửa tip tại nguồn copy của Guide me. Nêu giá trị mẫu hợp lệ và dùng cùng tên trường với form.

## Code dự kiến

Trong apps/seller/src/messages/vi.json, promotion-create.steps.quantity. Cập nhật en.json cùng khóa.

```diff
- "instruction": "Giới hạn tổng số lượt dùng.",
- "tip": "Khuyến mãi không giới hạn có thể lỗ nhiều hơn lãi nếu mã bị chia sẻ ra ngoài."
+ "instruction": "Nhập tổng số lượt dùng. Đây là trường bắt buộc.",
+ "tip": "Ví dụ, nhập 100 để phát tối đa 100 lượt dùng."
```

## Kiểm thử lại

Guide và form thống nhất khi bỏ trống hoặc nhập số lượt hợp lệ.

# UI-04: Ngày trên Promotions và Orders khác định dạng

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Tái hiện ngày 2026-11-27 trên Chromium local. |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết và bằng chứng](../../ui/loi.md#ui-04) |
| **Điểm vào source** | `promotions-config.tsx`, `orders-config.tsx`, `packages/core/src/lib/date.ts` |

## Nguyên nhân

Promotions in chuỗi YYYY-MM-DD trực tiếp. Orders dùng shortDate, gọi toLocaleDateString cho timestamp.

## Thay đổi

Dùng format hiển thị chung ở lớp UI cho hai bảng. Với ngày thuần YYYY-MM-DD, dùng UTC khi format để giữ nguyên ngày lịch. Với timestamp, dùng múi giờ hiển thị đã chọn của console. Giữ kiểu dữ liệu gốc cho input, so sánh và sắp xếp.

## Code dự kiến

```ts
// Date-only từ API luôn ở dạng YYYY-MM-DD.
const dateOnlyFormat = new Intl.DateTimeFormat(locale, {
  year: "numeric",
  month: "numeric",
  day: "numeric",
  timeZone: "UTC",
});
const label = value
  ? dateOnlyFormat.format(new Date(value + "T00:00:00Z"))
  : "—";
```

## Kiểm thử lại

1. Đăng nhập Seller, mở Promotions và Orders trong cùng phiên, so sánh cách trình bày các cột ngày.
2. Hai bảng dùng cùng quy ước theo locale đang hiển thị. Ngày hiệu lực khuyến mãi giữ đúng ngày khi đổi múi giờ.
3. Kiểm cùng ngày lịch ở các timezone Asia/Ho_Chi_Minh và America/Los_Angeles, cùng một timestamp ở hai bảng.

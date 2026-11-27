# UI-03: Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Tái hiện ngày 2026-11-27 trên Chromium local. |
| **Repo** | `taschen-storefront` |
| **Bug** | [Chi tiết và bằng chứng](../../ui/loi.md#ui-03) |
| **Điểm vào source** | `src/app/[locale]/(main)/search/page.tsx` và message catalogs `vi`/`en` |

## Nguyên nhân

SearchResults và thẻ kết quả chứa chuỗi tiếng Việt trực tiếp, chưa đọc bản dịch từ next-intl.

## Thay đổi

Dùng namespace Search theo quy ước i18n hiện tại cho tiêu đề, input, số kết quả, độ khớp và trạng thái tải/rỗng/lỗi. Dùng định dạng số nhiều của next-intl cho số kết quả và nội suy tên truy vấn.

## Code dự kiến

```tsx
const t = useTranslations("search");

<h1>{t("title")}</h1>
<p aria-live="polite">
  {t("resultCount", { count: results.length, query: debounced })}
</p>
```

## Kiểm thử lại

1. Mở `/en/search?q=sapiens`, đợi kết quả rồi đối chiếu với `/vi/search?q=sapiens`.
2. Nhãn giao diện theo locale của route. Tên sách và tác giả giữ đúng nội dung danh mục.
3. Kiểm truy vấn rỗng, có kết quả, không có kết quả và lỗi mạng ở cả hai locale.

# BO-09: Tìm kiếm khuyến mãi trả 500

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | promotion-service |
| **Bug** | [Chi tiết BO-09](../../backoffice/loi.md#bo-09) |
| **Điểm vào source** | `PromotionServiceImpl và repository tìm kiếm` |

## Nguyên nhân

API tìm kiếm gặp 500. Nhật ký truy vấn cần xác nhận giả thuyết lỗi kiểu tham số trong PostgreSQL.

## Thay đổi

1. Tái hiện bằng keyword rỗng và có giá trị, đọc exception gốc. Nếu là lỗi kiểu, tách điều kiện keyword rỗng và bind chuỗi nhất quán ở truy vấn có keyword.
2. Giữ phân trang, sắp xếp, dữ liệu hiển thị và kiểm cả trường hợp không có kết quả.

## Code dự kiến

Nếu log PostgreSQL xác nhận lỗi kiểu keyword, chỉ gọi truy vấn có điều kiện text khi keyword tồn tại. Hai truy vấn phải giữ cùng filter, thứ tự và phân trang, tên dưới đây là điểm nối minh họa.

```java
String term = keyword == null ? "" : keyword.strip();
return term.isEmpty()
    ? repository.findMatching(filters, pageable)
    : repository.findMatchingByText(filters, term, pageable);
```

## Kiểm thử lại

Keyword rỗng, có kết quả, không có kết quả và truy vấn phân trang đều trả đúng response.

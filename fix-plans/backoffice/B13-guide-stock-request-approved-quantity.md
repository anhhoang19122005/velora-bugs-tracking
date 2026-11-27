# B13: Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa, cần xác nhận nghiệp vụ |
| **Repo** | `taschen-backoffice`, inventory-service nếu đổi nghiệp vụ |
| **Bug** | [Chi tiết B13](../../test-2026-11-27/loi.md#b13) · GM08-03 |
| **Điểm vào source** | `Guide me yêu cầu nhập`, `form duyệt Admin` |

## Nguyên nhân

Hướng dẫn nói Admin đổi được số lượng, nhưng hộp thoại chỉ cho nhập lời nhắn.

## Thay đổi

1. Đề xuất sửa guide để Admin duyệt số lượng gốc và ghi lời nhắn. Nếu chốt duyệt một phần, lưu riêng số yêu cầu và số được duyệt, rồi chuyển số được duyệt sang PO.

## Kiểm thử lại

Guide, hộp thoại và số lượng trên PO khớp nhau khi làm theo hướng dẫn.

# B12: Guide me nói tiền đã hoàn ngay khi bấm Đã nhận

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết B12](../../test-2026-11-27/loi.md#b12) · GM06-04 |
| **Điểm vào source** | `Guide me xử lý trả hàng` |

## Nguyên nhân

Bấm Đã nhận chỉ mở một khoản hoàn đang chờ chi, nhưng hướng dẫn nói tiền đã được hoàn.

## Thay đổi

1. Sửa bước Đã nhận để mô tả REFUND_PENDING và khoản hoàn OPEN. Chỉ mô tả hoàn tất sau bước ghi nhận chi trả.

## Kiểm thử lại

Guide khớp màn và trạng thái trước/sau ghi nhận khoản hoàn.

# SF-28: Tham số sai kiểu trả 500 thay vì 400 hoặc 404

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend`, nhiều service |
| **Bug** | [Chi tiết SF-28](../../storefront/loi.md#sf-28) |
| **Điểm vào source** | `GlobalExceptionHandler` |

## Nguyên nhân

Lỗi chuyển kiểu path/query đang rơi vào nhánh lỗi hệ thống ở một số service.

## Thay đổi

1. Đối chiếu từng response và log để xác định exception. Dùng lại cách Inventory xử lý MethodArgumentTypeMismatchException và NoResourceFoundException ở nơi phù hợp.
2. Giữ 400 cho sai kiểu, 404 cho route hoặc tài nguyên không có, và chạy lại các điểm Catalog, Order, Identity, Promotion, Notification trong báo cáo.

## Kiểm thử lại

ID/query sai kiểu trả 400. Route hoặc tài nguyên không tồn tại trả 404. Lỗi hệ thống thật vẫn là 500.

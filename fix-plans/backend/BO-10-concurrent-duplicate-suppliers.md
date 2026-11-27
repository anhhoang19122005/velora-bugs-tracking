# BO-10: Nhà cung cấp trùng khi tạo đồng thời

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service |
| **Bug** | [Chi tiết BO-10](../../backoffice/loi.md#bo-10) |
| **Điểm vào source** | `SupplierServiceImpl`, `SupplierRepository`, `Flyway` |

## Nguyên nhân

Kiểm existsByNameIgnoreCase có thể trả false đồng thời cho nhiều request. Database còn thiếu chốt duy nhất tương ứng.

## Thay đổi

1. Rà bản ghi trùng theo quy tắc tên hiện có. Xử lý va chạm có đối soát liên kết trước khi thêm unique index.
2. Ánh xạ vi phạm constraint cụ thể sang 409 ở đường tạo và đổi tên. Giữ kiểm tra sớm để báo lỗi rõ.

## Kiểm thử lại

Năm lần tạo đồng thời cùng tên chỉ có một bản ghi. Khác hoa/thường theo cùng quy tắc. Sửa sang tên đã có cũng bị chặn.

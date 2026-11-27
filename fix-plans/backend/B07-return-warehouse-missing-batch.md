# B07: Duyệt trả kho cho sách chưa có lô không cộng tồn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service |
| **Bug** | [Chi tiết B07](../../test-2026-11-27/loi.md#b07) · GM11-03 |
| **Điểm vào source** | `BatchServiceImpl.restockReturnedUnits` |

## Nguyên nhân

Khi không có lô đúng biến thể, logic có thể lấy lô của biến thể khác hoặc chỉ ghi log. Phiếu vẫn được duyệt dù tồn chưa tăng đúng.

## Thay đổi

1. Yêu cầu tìm lô theo đúng sách và biến thể. Nếu thiếu lô phù hợp, ném lỗi nghiệp vụ 409 trước khi giao dịch duyệt commit.
2. Giữ cập nhật tất cả dòng trong cùng giao dịch B01. Xác minh điều kiện rollback với exception đang dùng.
3. Giữ phiếu PENDING để kho xử lý. Việc tạo lô riêng cần quyết định giá vốn và quy tắc truy vết.

## Kiểm thử lại

Duyệt phiếu có dòng thiếu lô giữ PENDING, tồn mọi dòng giữ nguyên kể cả khi dòng trước có lô. Phiếu đủ lô cộng đúng lượng vào đúng biến thể.

## Liên quan

[B01](../../fix-plans/backend/B01-return-warehouse-duplicate-rma.md)

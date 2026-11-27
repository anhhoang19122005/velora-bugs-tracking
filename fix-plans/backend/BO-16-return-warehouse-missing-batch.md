# BO-16: Duyệt trả kho cho sách chưa có lô không cộng tồn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service |
| **Bug** | [Chi tiết BO-16](../../backoffice/loi.md#bo-16) · GM11-03 |
| **Điểm vào source** | `BatchServiceImpl.restockReturnedUnits` |

## Nguyên nhân

Khi không có lô đúng biến thể, logic có thể lấy lô của biến thể khác hoặc chỉ ghi log. Phiếu vẫn được duyệt dù tồn chưa tăng đúng.

## Thay đổi

1. Yêu cầu tìm lô theo đúng sách và biến thể. Nếu thiếu lô phù hợp, ném lỗi nghiệp vụ 409 trước khi giao dịch duyệt commit.
2. Giữ cập nhật tất cả dòng trong cùng giao dịch BO-13. Xác minh điều kiện rollback với exception đang dùng.
3. Giữ phiếu PENDING để kho xử lý. Việc tạo lô riêng cần quyết định giá vốn và quy tắc truy vết.

## Code dự kiến

Trong BatchServiceImpl.restockReturnedUnits, giữ phép cộng tồn hiện có. Bỏ vòng tìm lô khác biến thể. Khi phiếu cũ thiếu variantId, giữ chính sách hiện có tới khi nghiệp vụ xác nhận quy tắc cụ thể.

```java
List<Batch> candidates = variantId != null
    ? batchRepository.findByBookIdAndVariantIdOrderByCreatedAtDesc(bookId, variantId)
    : batchRepository.findByBookIdOrderByCreatedAtDesc(bookId);
if (candidates.isEmpty()) {
    throw new AppException(ErrorCode.CONFLICT, "No stock batch matches the return");
}
restock(candidates.get(0).getId(), quantity);
```

## Kiểm thử lại

Duyệt phiếu có dòng thiếu lô giữ PENDING, tồn mọi dòng giữ nguyên kể cả khi dòng trước có lô. Phiếu đủ lô cộng đúng lượng vào đúng biến thể.

## Liên quan

[BO-13](../../fix-plans/backend/BO-13-return-warehouse-duplicate-rma.md)

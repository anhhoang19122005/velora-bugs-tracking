# SF-46: Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | catalog-service, inventory-service, `taschen-backoffice` |
| **Bug** | [Chi tiết SF-46](../../storefront/loi.md#sf-46) · GM03-02 |
| **Điểm vào source** | `BookVariantServiceImpl`, `StockChangedEventListener` |

## Nguyên nhân

Form có thể ghi 10 cuốn vào Catalog trong khi kho có 0. Bản sao tồn trên Catalog vì vậy báo còn hàng dù Inventory từ chối đơn.

## Thay đổi

1. Đặt tồn biến thể mới bằng 0 và bỏ quyền ghi tồn ở đường sửa biến thể. Rà các caller đang gửi stockQuantity, rồi cập nhật form Backoffice và sinh lại contract nếu DTO đổi.
2. Tiếp tục dùng event tồn từ Inventory và kết hợp SF-35 để cập nhật cache sau commit.
3. Chạy báo cáo so lệch theo bookId/variantId, duyệt kết quả và đồng bộ lại Catalog theo số liệu Inventory.

## Code dự kiến

Trong BookVariantServiceImpl, thay đường gán tồn lúc tạo và bỏ đường gán từ DTO lúc sửa. StockChangedEventListener tiếp tục là nơi đồng bộ thay đổi tồn.

```diff
- .stockQuantity(request.stockQuantity() != null ? request.stockQuantity() : 0)
+ .stockQuantity(0)

- if (request.stockQuantity() != null) {
-     bookVariant.setStockQuantity(request.stockQuantity());
- }
```

## Kiểm thử lại

Tạo biến thể khi Inventory bằng 0 thì Storefront hiện hết hàng. Nhập kho 10 thì cùng biến thể hiển thị 10 sau đồng bộ. Tồn thật và số hiển thị khớp sau giữ hàng hoặc trả hàng.

## Liên quan

[SF-35](../../fix-plans/backend/SF-35-catalog-stock-cache-stale.md)

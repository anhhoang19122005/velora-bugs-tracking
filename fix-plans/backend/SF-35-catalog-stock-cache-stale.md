# SF-35: Tồn kho hiển thị cũ do cache catalog

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | catalog-service, inventory-service |
| **Bug** | [Chi tiết SF-35](../../storefront/loi.md#sf-35) |
| **Điểm vào source** | `StockChangedEventListener`, `BookServiceImpl` |

## Nguyên nhân

Catalog lưu bản sao tồn và cache kết quả chi tiết sách. Một lần cập nhật tồn có thể chưa được phản ánh ở API đọc qua cache.

## Thay đổi

1. Xác nhận DB Catalog đã đổi khi Inventory phát event. Sau giao dịch, xóa những cache chứa tồn theo ID, slug hoặc danh sách có thật trong source.
2. Dùng bản ghi Inventory để xác định tồn chuẩn khi đối soát event bị thiếu hoặc đến muộn. Phối hợp SF-46 để loại bỏ đường ghi tồn từ form biến thể.

## Code dự kiến

Ở listener, tách thời điểm lưu kho khỏi thời điểm xóa cache. Ví dụ dùng event nội bộ và listener AFTER_COMMIT nếu giao dịch hiện tại chưa có cơ chế tương đương. Giữ cơ chế redelivery/đối soát cho lỗi cache.

```java
@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
void evictStockViews(CatalogStockUpdated event) {
    bookCache.evict(event.bookId());
    bookSlugCache.evict(event.slug());
}
```

## Kiểm thử lại

Sau đặt đơn, trả hàng và nhập kho, chi tiết/list hiển thị tồn mới. Lặp event không làm sai số. Xác nhận phép đo với cache đã làm nóng.

## Liên quan

[SF-46](../../fix-plans/backend/SF-46-variant-stock-initialization.md)

# B06: API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service, `taschen-backoffice` |
| **Bug** | [Chi tiết B06](../../test-2026-11-27/loi.md#b06) · GM07-03 |
| **Điểm vào source** | `PurchaseOrderServiceImpl` |

## Nguyên nhân

Ô chọn chỉ hiện nhà cung cấp đang hoạt động nhưng hai đường tạo PO phía server chỉ tìm theo ID.

## Thay đổi

1. Dùng chung kiểm tra nhà cung cấp khi tạo PO trực tiếp và khi tạo từ yêu cầu nhập. Giữ hàm lấy nhà cung cấp dùng cho truy vấn lịch sử với trách nhiệm hiện tại.
2. Ánh xạ lỗi theo contract cho trường hợp không tồn tại hoặc đã ngừng. Hiển thị lỗi nếu trạng thái thay đổi khi người dùng đang mở form.

## Code dự kiến

Trong PurchaseOrderServiceImpl, cả create và createFromStockRequest gọi chung phần kiểm supplier. Giữ 404 hiện có khi thiếu ID.

```java
private Supplier getActiveSupplierOrThrow(Long id) {
    Supplier supplier = getSupplierOrThrow(id);
    if (!supplier.isActive()) {
        throw new AppException(ErrorCode.CONFLICT, "Supplier is inactive");
    }
    return supplier;
}
```

## Kiểm thử lại

Nhà cung cấp đang hoạt động tạo PO được. Nhà cung cấp đã ngừng bị từ chối cả khi nhập từ yêu cầu và khi được chọn trên form trước lúc bị ngừng.

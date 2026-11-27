# B05: Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service, `taschen-backoffice` |
| **Bug** | [Chi tiết B05](../../test-2026-11-27/loi.md#b05) · GM09-12 |
| **Điểm vào source** | `CreatePurchaseOrderRequest`, `CreatePurchaseOrderFromStockRequestRequest`, `purchase-order.schema.ts` |

## Nguyên nhân

Giá 0 đi qua kiểm tra đầu vào rồi bị Bean Validation ở entity chặn lúc lưu, dẫn đến lỗi 500.

## Thay đổi

1. Đặt điều kiện lớn hơn 0 trên hai DTO tạo PO bằng @DecimalMin với inclusive=false. Rà DTO tạo phiếu nhập vì entity cũng đòi giá dương.
2. Áp dụng cùng quy tắc cho Zod hiện có và dùng cơ chế hiển thị lỗi theo dòng hàng.

## Cấu hình Bean Validation

```java
@DecimalMin(value = "0.0", inclusive = false, message = "Import price must be greater than 0")
```

Đặt annotation ở đầu vào API để Spring trả lỗi trường trước khi đi vào nghiệp vụ. Entity tiếp tục bảo vệ dữ liệu khi có đường ghi khác.

## Kiểm thử lại

Giá 0 hoặc âm trả 400 tại đúng trường, không sinh PO/phiếu. Giá dương hợp lệ vẫn lưu. Test cả hai lối tạo PO.

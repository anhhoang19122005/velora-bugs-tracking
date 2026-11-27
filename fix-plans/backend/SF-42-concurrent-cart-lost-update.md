# SF-42: Giỏ hàng mất cập nhật khi thêm đồng thời

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | order-service |
| **Bug** | [Chi tiết SF-42](../../storefront/loi.md#sf-42) |
| **Điểm vào source** | `CartServiceImpl` |

## Nguyên nhân

Nhiều thao tác cùng đọc lượng cũ rồi ghi cùng một kết quả, nên báo thêm thành công nhưng chỉ có một cuốn.

## Thay đổi

1. Khóa hàng giỏ trước khi đọc và sửa mục hàng, phối hợp thứ tự khóa và phiên bản giỏ với SF-37.
2. Giữ khóa duy nhất của dòng theo sách/biến thể. Cộng số lượng trong giao dịch và kiểm số dòng, tổng số lượng khi thao tác đồng thời.

## Kiểm thử lại

Năm request thành công thì tổng tăng đúng năm. Chạy thêm đồng thời với checkout và kiểm giỏ mới sau checkout được giữ.

## Liên quan

[SF-37](../../fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md)

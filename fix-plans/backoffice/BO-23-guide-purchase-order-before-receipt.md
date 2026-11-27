# BO-23: Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết BO-23](../../backoffice/loi.md#bo-23) · GM09-03 |
| **Điểm vào source** | `Guide me đơn mua` |

## Nguyên nhân

Người dùng có thể thử nhập ở APPROVED và gặp 409 vì đơn mua chưa sang ORDERED.

## Thay đổi

1. Chèn bước Đánh dấu đã đặt giữa duyệt và nhập. Dùng đúng tên nút và mô tả vai trò thực hiện theo phiên bản đang chạy.

## Code dự kiến

Trong apps/warehouse/src/messages/vi.json, sửa po-from-stock-request.steps.approve.instruction và steps.pay.instruction, cùng import-stock.needsNoun. Task đã có bước pay nên dùng lại, cập nhật en.json và kiểm flow với vai trò Admin/Warehouse.

```json
{
  "approve": "Quản trị bấm Duyệt để xác nhận đơn mua.",
  "pay": "Quản trị bấm Đánh dấu đã đặt. Khi đơn sang Đã đặt hàng, kho mới lập phiếu nhập được.",
  "needsNoun": "một đơn mua đã đặt hàng"
}
```

## Kiểm thử lại

Ở `APPROVED` chưa nhập được. Sau khi đơn sang `ORDERED`, Warehouse lập phiếu và nhận đúng quy trình.

## Liên quan

[BO-11](../../fix-plans/backend/BO-11-concurrent-purchase-order-imports.md) · [BO-22](../../fix-plans/backoffice/BO-22-guide-stock-request-status.md)

# SF-32: Nút Đã nhận hàng không hỏi xác nhận

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-storefront` |
| **Bug** | [Chi tiết SF-32](../../storefront/loi.md#sf-32) |
| **Điểm vào source** | `src/app/[locale]/(main)/orders/[number]/page.tsx` |

## Nguyên nhân

Nút Đã nhận hàng gọi mutation ngay, đồng thời thay đổi trạng thái đơn và thanh toán COD.

## Thay đổi

1. Dùng mẫu hộp thoại đang có cho Huỷ đơn trong màn chi tiết. Gọi confirmReceived từ nút xác nhận và khóa thao tác khi mutation đang gửi.
2. Giữ quy trình refresh dữ liệu và thông báo của mutation hiện tại.

## Kiểm thử lại

Bấm nút mở hộp thoại. Đóng hộp thoại giữ nguyên trạng thái. Bấm xác nhận gửi đúng một request và đọc lại trạng thái đơn.

## Liên quan

[SF-15](../../fix-plans/storefront/SF-15-cancel-order-no-confirmation.md)

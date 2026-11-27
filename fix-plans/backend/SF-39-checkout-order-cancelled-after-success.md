# SF-39: Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor (đính chính ngày 14/11: lúc đầu ghi là "bán vượt tồn kho", Major) |
| **Trạng thái** | Chưa sửa, không bắt buộc |
| **Repo** | `taschen-backend` (`order-service`) và `taschen-storefront`, số dòng theo `develop` `e090ed4` |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-39) và Storefront-Bất biến (kịch bản 18) |

## Đính chính

Lúc test ban đầu mình ghi là bán vượt tồn kho: tồn 43, hai người đặt 26 cuốn cùng lúc, cả hai nhận 201. Đối chiếu lại thời điểm cập nhật đơn cho thấy:

- Đơn 64: tạo lúc 02:27:11.558, **hệ thống tự hủy** lúc 02:27:12.472 (sau khoảng 0,9 giây).
- Đơn 63: tạo lúc 02:27:11.536, bị hủy lúc 02:27:26 do mình dọn dữ liệu.
- Inventory chỉ trừ 26 cuốn (43 xuống 17).

Tức là saga giữ hàng đã làm đúng: chỉ một đơn giữ được hàng, đơn kia bị hủy bù. **Không có bán vượt.**

## Vấn đề còn lại

`checkout` kiểm tra tồn kho đồng bộ (`ensureInventoryStock`, `OrderServiceImpl.java:253-260`), nhưng việc giữ hàng là bất đồng bộ qua `OrderPlacedEvent`. Hai request cùng qua bước kiểm tra, nên khách thứ hai thấy "Đặt hàng thành công", rồi một giây sau đơn chuyển Đã hủy. Lý do không được lưu: `handleStockReservedFailure` (dòng 586-595) chỉ ghi log `reason`.

Đây là giới hạn có sẵn của thiết kế saga, chỉ xảy ra khi hai người tranh đúng phần hàng cuối. Vì vậy hạ xuống Minor.

## Hướng sửa (không bắt buộc)

1. Storefront phân biệt đơn vừa tạo, đang chờ giữ hàng và đã xác nhận. Dùng trạng thái trả về từ API đơn và cơ chế làm mới dữ liệu hiện có. Thông báo sau 201 là đã tiếp nhận nếu đơn còn `PENDING`.
2. Khi chuyển trạng thái vì kho báo hết hàng, hiển thị lý do theo mã nghiệp vụ nếu đã có. Nếu API chưa có, lưu và trả lý do có cấu trúc từ Order rồi sinh lại contract. Dùng bản dịch phía Storefront cho thông báo.
3. Giữ quy trình giữ hàng bất đồng bộ. [SF-44](SF-44-order-event-lost-stuck-pending.md) xử lý trường hợp đơn chờ do mất sự kiện.

## Code dự kiến

Trong màn kết quả đặt hàng, derive nội dung từ trạng thái đọc lại bằng API. Dùng khóa dịch hiện có hoặc mở rộng namespace orders. Đơn hủy bởi kho hiển thị lý do theo mã có cấu trúc khi API trả về.

```tsx
if (order.status === OrderStatus.PENDING) {
  return <OrderNotice>{t("waitingForStock")}</OrderNotice>;
}
if (order.status === OrderStatus.CANCELLED) {
  return <OrderNotice>{cancellationMessage(order)}</OrderNotice>;
}
// Dùng nhánh kết quả phù hợp cho các trạng thái còn lại.
```

## Kiểm thử lại

Kịch bản 18: hai khách tranh lượng hàng cuối. Chỉ khách giữ được hàng thấy đơn xác nhận. Khách còn lại thấy đơn chờ rồi thông báo hết hàng. Kiểm COD và nhánh đồng bộ với trạng thái thanh toán.

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

- **Nhỏ nhất:** lưu lý do hủy vào đơn (cột `cancelReason`, cần migration Flyway) khi giữ hàng thất bại. Storefront hiện "Đơn đã bị hủy vì sản phẩm vừa hết hàng" ở trang chi tiết đơn.
- **Triệt để:** giữ hàng đồng bộ (gọi inventory-service giữ hàng trước khi lưu đơn). Cách này đổi kiến trúc saga, không đề xuất cho Minor.

## Kiểm thử lại

Kịch bản 18: khách thứ hai thấy đơn bị hủy kèm lý do hết hàng, không còn chỉ thấy "Đã hủy" mà không rõ vì sao.

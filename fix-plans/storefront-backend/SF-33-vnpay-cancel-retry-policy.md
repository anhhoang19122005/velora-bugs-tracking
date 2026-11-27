# SF-33: Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được

> **Cập nhật 2026-11-27:** Không còn áp dụng: VNPay đã bỏ (REQ-007), thanh toán online là SePay. Giữ file làm lịch sử.

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa, cần xác nhận nghiệp vụ |
| **Repo** | order-service, payment-service, `taschen-storefront` |
| **Bug** | [Chi tiết SF-33](../../storefront/loi.md#sf-33) |
| **Điểm vào source** | `PaymentServiceImpl`, `OrderServiceImpl`, `payment-result` |

## Nguyên nhân

Sau khi khách hủy ở VNPay, UI thấy đơn đã hủy và không có cách thử lại. Cần chốt thời hạn và trạng thái cho phép thanh toán tiếp.

## Thay đổi

1. Đề xuất giữ đơn có thể thanh toán đến lúc hết hạn. Nếu được duyệt, tách trạng thái lần thanh toán và đơn hàng, nối vào cơ chế một lần đang hoạt động theo SF-43.
2. Cho người dùng thử lại từ trang kết quả hoặc chi tiết đơn. Đối chiếu callback đến muộn và mốc hết hạn trước khi hủy.
3. Nếu hủy cả đơn là hành vi mong muốn, sửa thông báo và hướng dẫn tương ứng.

## Code dự kiến

Nhánh dưới chỉ áp dụng nếu duyệt cho phép thử lại. Kiểm quyết định khi đã khóa đơn và đối soát lần thanh toán hiện tại. Các predicate minh họa quy tắc cần nối với model hiện có.

```java
if (order.isPayableAt(clock.instant()) && paymentAttempt.isTerminalFailure()) {
    return initiateOrReuseActiveAttempt(order);
}
throw new AppException(ErrorCode.CONFLICT, "Order is not payable");
```

## Kiểm thử lại

Hủy ở sandbox hoặc thất bại có hành vi theo quyết định. Kiểm lần thử lại, hết hạn và tình huống phản hồi đến muộn để tránh thu tiền hai lần.

## Liên quan

[SF-43](../../fix-plans/backend/SF-43-duplicate-active-vnpay-payment.md) · [SF-44](../../fix-plans/backend/SF-44-order-event-lost-stuck-pending.md)

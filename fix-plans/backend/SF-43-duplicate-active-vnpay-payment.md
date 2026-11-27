# SF-43: Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán

> **Cập nhật 2026-11-27:** VNPay đã bỏ (REQ-007). Bản sửa BUG-021 (`5b8445f`) giữ một payment PENDING mỗi đơn cho SePay; kế hoạch này chỉ còn giá trị lịch sử, chờ retest với SePay.

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | payment-service, order-service |
| **Bug** | [Chi tiết SF-43](../../storefront/loi.md#sf-43) |
| **Điểm vào source** | `PaymentServiceImpl`, `PaymentRepository` |

## Nguyên nhân

Các request khởi tạo đồng thời có thể cùng không thấy lần thanh toán hiện tại và tạo nhiều bản ghi PENDING.

## Thay đổi

1. Dùng khóa theo đơn hoặc cơ chế ghi nguyên tử hiện có, thêm ràng buộc phù hợp để bảo vệ một lần thanh toán còn hiệu lực. Khi cạnh tranh, đọc lại bản ghi thắng và trả cùng link còn hạn.
2. Giữ lịch sử các lần đã kết thúc, đối soát trước khi mở lần mới và giữ xử lý callback lặp theo mã giao dịch.

## Code dự kiến

Tại bước khởi tạo trong PaymentServiceImpl, thao tác tìm/tạo chạy dưới chốt đồng thời theo đơn. Xác định attempt còn hiệu lực theo trạng thái và hạn phiên. Nếu retry sau tranh chấp unique, đọc lại bằng transaction mới.

```java
return activeAttemptRepository.findForOrder(orderId)
    .map(this::reuseInitiationResponse)
    .orElseGet(() -> createActiveAttempt(orderId, request));
```

## Kiểm thử lại

Ba request đồng thời trả về cùng lần thanh toán hiệu lực. Callback lặp chỉ ghi nhận tiền một lần. Kiểm lần mới hợp lệ sau phiên cũ hết hạn theo quy tắc SF-33.

## Liên quan

[SF-33](../../fix-plans/storefront-backend/SF-33-vnpay-cancel-retry-policy.md)

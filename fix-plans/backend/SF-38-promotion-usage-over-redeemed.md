# SF-38: Mã giảm giá được cấp cho nhiều đơn hơn số lượt

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Đã chốt phương án B ngày 14/11. [B02](../../test-2026-11-27/loi.md#b02) tái hiện ngày 27/11. |
| **Repo** | `taschen-backend` (`order-service`, `promotion-service`), đối chiếu `develop` `d5b6ac2` |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38`, phối hợp với [SF-37](../storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md). |
| **Khối lượng** | Cần sửa luồng checkout, lưu trạng thái bù trừ và kiểm thử lỗi giữa hai service. |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-38) và Storefront-Bất biến (kịch bản 15 đến 17) |

## Hiện tượng

- Mã còn 1 lượt, 2 người đặt cùng lúc: cả 2 đơn đều giảm 19.300 đ (đơn 58, 59).
- Một người, mã còn 3 lượt, bấm đặt 3 lần cùng lúc: cả 3 đơn đều giảm, số lượng mã chỉ giảm từ 3 xuống 2 (đơn 60, 61, 62).
- Số lượng mã không xuống âm; lỗi là giảm giá được cấp vượt số lượt.

## Nguyên nhân

`checkout` kiểm tra mã và tính giá giảm trước khi giữ lượt. `advanceToConfirmed` xác nhận đơn rồi gọi `recordPromotionUsageBestEffort`. Khi ghi lượt bị từ chối hoặc lỗi kết nối, order-service ghi log và đơn giữ nguyên giá giảm. Đợt 27/11 ghi nhận hai đơn cùng xác nhận và cùng giảm 18.900đ với mã còn một lượt.

`PromotionRepository.decrementQuantityAt` giảm lượt bằng một UPDATE có điều kiện `quantity > 0`. Điều kiện này bảo vệ bộ đếm. Giá giảm vẫn có thể cấp quá lượt vì order-service chưa buộc phải giữ lượt thành công trước khi chấp nhận đơn. `recordUsageAttempt` còn có thể trả về lượt cũ của cùng khách và mã. Nếu lượt cũ thuộc đơn khác thì checkout phải từ chối.

## Quy tắc đã chốt ngày 14/11

- Giữ lượt khi đặt hàng. Chỉ chấp nhận giá giảm sau khi xác nhận lượt thuộc đúng đơn.
- Nhân viên hoặc hệ thống hủy thì hoàn lượt. Khách tự hủy thì giữ nguyên lượt đã dùng.

## Thiết kế đề xuất

1. **Ghi lần checkout trước khi gọi giữ lượt.** Sinh và lưu mã tham chiếu ổn định cho lần checkout, liên kết với dấu chống trùng của SF-37 và đơn dự kiến. Promotion-service giảm lượt và lưu chủ sở hữu của lượt trong cùng transaction. Gọi lại theo cùng tham chiếu phải trả đúng kết quả. Lượt thuộc đơn khác phải bị từ chối.
2. **Chốt đơn sau khi giữ lượt.** Đọc kết quả giữ lượt thay vì bỏ qua response. Khi hết lượt hoặc khách đã dùng mã cho đơn khác, trả lỗi mã và giữ giỏ. Khi timeout mà chưa rõ lượt đã giữ hay chưa, tra lại bằng cùng tham chiếu. Đánh dấu lần checkout hoàn tất cùng transaction tạo đơn. Bỏ bước ghi lượt ở lúc chuyển `CONFIRMED` cho luồng mới.
3. **Bù trừ lần checkout thất bại.** Tác vụ đối soát đọc các lần checkout bỏ dở đã lưu. Chỉ hoàn lượt sau khi xác nhận không có đơn đã commit và chốt lần checkout sang trạng thái thất bại để worker tạo đơn không thể commit muộn. Promotion-service lưu kết quả hủy theo tham chiếu kể cả khi chưa thấy lượt giữ, để request giữ đến muộn bị từ chối. `saveAndFlush` có thể phát hiện lỗi lưu sớm. Transaction đơn vẫn có thể rollback sau khi promotion-service đã giữ lượt.
4. **Hoàn lượt có thể thử lại.** Ghi yêu cầu hoàn trong cùng transaction hủy của nhân viên hoặc hệ thống. Worker thử lại khi promotion-service lỗi hoặc mất phản hồi. Endpoint hoàn dùng tham chiếu ổn định và chỉ cộng lại một lần, cùng transaction xóa hoặc đánh dấu lượt đã hoàn. Đơn kẹt xử lý theo [SF-44](SF-44-order-event-lost-stuck-pending.md).

## Code dự kiến

Trong Promotion, phép lấy lượt theo checkout ref phải chạy chung transaction với ghi chủ sở hữu. Điều kiện UPDATE bảo vệ lượt cuối giữa nhiều customer, còn unique theo checkoutRef và giới hạn theo user bảo vệ gọi lặp. Hình dưới dùng tên hàm minh họa.

```java
var previous = reservationRepository.findByReference(checkoutRef);
if (previous.isPresent()) {
    return resolveExistingReservation(previous.get(), orderRef);
}
if (promotionRepository.decrementAvailableIfPositive(promotionId) != 1) {
    return ReservationResult.exhausted();
}
return storeReservation(promotionId, checkoutRef, orderRef, customerId);
```

## Kiểm thử cần có

| Tình huống | Kết quả mong đợi |
|---|---|
| Hai khách tranh lượt cuối | Một đơn được giảm. Khách còn lại nhận lỗi mã và giữ giỏ. |
| Cùng khách dùng mã cho hai đơn | Chỉ lần giữ lượt đầu hợp lệ. Retry của chính lần đó nhận cùng kết quả. |
| Giữ lượt thành công rồi transaction đơn rollback hoặc tiến trình dừng | Đối soát hoàn đúng một lượt. Không hoàn nếu tìm thấy đơn đã commit. |
| Giữ lượt hoặc hoàn lượt bị timeout sau khi phía khuyến mãi đã commit | Retry bằng cùng tham chiếu. Số lượt chỉ giảm hoặc tăng một lần. |
| Request giữ lượt đến sau khi đã bù trừ lần checkout thất bại | Từ chối giữ lượt và giữ nguyên số lượt hiện tại. |
| Nhân viên hoặc hệ thống hủy, promotion-service tạm thời lỗi | Đơn được hủy. Yêu cầu hoàn còn chờ và phục hồi khi service hoạt động lại. |
| Khách tự hủy đơn | Lượt không tăng. |

Khi triển khai, cập nhật contract nội bộ cho giữ, tra cứu và hoàn lượt. Chạy lại kịch bản 15–17 của [Storefront-Bất biến](../../storefront/bat-bien.md) và B02. Chưa có bản sửa từ kế hoạch này.

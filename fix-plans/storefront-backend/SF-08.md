# SF-08: Đặt hàng có mã khuyến mãi trả 400

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại |
| **Repo có bản sửa** | `taschen-backend` và `taschen-storefront` |
| **Nhánh thực hiện** | `fix/checkout-flow-sf-02-03-07-08-10` ở hai repo |
| **Bug và ảnh trước sửa** | [Chi tiết bug](../../storefront/loi.md#sf-08), [Ảnh 1](../../images/SF-08-1.jpg), [Ảnh 2](../../images/SF-08-2.jpg) |

## Nguyên nhân trước khi sửa

Order-service lưu promotionId nhưng gọi `POST /validate` và `POST /usages` mà promotion-service chưa cung cấp. API có sẵn dùng code ở `GET /validate/{code}` và `POST /{code}/usages`. Lỗi gọi validate bị đổi thành VALIDATION_ERROR, khiến mã vừa kiểm tra hợp lệ vẫn không đặt được đơn.

Đường ghi nhận lượt dùng cũng sai endpoint, còn exception bị hàm best-effort bắt lại. Ngoài ra, response validation thực có `valid=false` cho mã không dùng được; client cũ chưa đọc cờ này.

## Thay đổi đã có

| Thành phần | Hành vi đã merge |
|---|---|
| promotion-service | Thêm `GET /api/v1/promotions/{id}/validate` với userId/orderSubtotal; phần id giới hạn chữ số để tránh xung đột route theo code. |
| promotion-service | Thêm `POST /api/v1/promotions/usages` với promotionId/userId/orderId; dùng lại logic recordUsage theo code. |
| Bảo vệ endpoint | SecurityConfig cho lời gọi đi qua lớp security; InternalTokenInterceptor tại WebMvcConfig kiểm tra token nội bộ trên cả hai đường dẫn mới. permitAll không có nghĩa bỏ bảo vệ token. |
| Order client/service | Feign gọi validate theo ID; DTO nhận `valid` và `reason`; từ chối mã khi valid=false. Xóa DTO ValidatePromotionRequest không còn dùng. |
| Storefront checkout | Khi đặt đơn có promotionId gặp VALIDATION_ERROR, thông báo mã không còn dùng được và gọi kiểm tra mã lại để hiện lý do dưới ô nhập. |

Giữ thời điểm ghi lượt dùng sau thanh toán thành công. Hàm `recordPromotionUsageBestEffort` vẫn có thể bắt lỗi; sửa endpoint không chứng minh mọi lượt dùng luôn được ghi thành công khi dependency lỗi. Không ghi token nội bộ vào tài liệu.

## Commit và bằng chứng merge

- Backend `e4b317a`: endpoint theo ID, logic dùng lại, bảo vệ endpoint và test; `afaec9a`: sửa client/service phía order.
- Storefront `0bfd28a`: giải thích lỗi khi mã không còn áp dụng được lúc đặt hàng.
- `c32643e` sinh lại `services/promotion-service/contract/openapi.yaml` trong backend. Chưa xác minh repo `taschen-contracts` riêng đã đồng bộ.
- Backend: [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`.
- Storefront: [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`.
- Đối chiếu source, lịch sử commit và đầu nhánh remote ngày **2026-11-12**.

## Test có trong source — chưa chạy lại

- `OrderServiceTest.checkout_promotionMarkedInvalid_throwsValidationError`: phản hồi valid=false bị từ chối; client được mock.
- `PromotionServiceTest`: ID không tồn tại trả lỗi; ID hợp lệ áp dụng quy tắc giá tương ứng validate theo code.
- `PromotionControllerIT`: validate theo ID và ghi lượt dùng có token nội bộ; thiếu token bị từ chối ở cả hai endpoint.
- `e2e/api/storefront.spec.ts`: mã hợp lệ lúc áp dụng nhưng không còn dùng được lúc đặt đơn hiển thị thông báo/lý do; test dùng API mock.

## Kiểm thử lại còn lại

- Đặt đơn qua stack thật với mã hợp lệ: 201, promotionId/tổng tiền/giảm giá đúng.
- Thử mã hết hạn, đã dùng, không đủ điều kiện và ID không tồn tại; đối chiếu status/code cụ thể.
- Thanh toán thành công, kiểm tra lượt dùng tăng đúng; gửi lại cùng nghiệp vụ để kiểm tra chống trùng.
- Gọi hai endpoint mới qua gateway không có/sai token nội bộ phải bị từ chối; không lưu giá trị token trong bằng chứng.
- Chạy lại luồng 7 và các test Fail/Blocked trong HT Áp mã/HT Checkout.

Chưa chạy ứng dụng/test trong lần cập nhật này. Chưa xác nhận toàn luồng hoặc cơ chế ghi lượt dùng khi dependency lỗi; giữ nguyên response/ảnh và kết quả test lịch sử.

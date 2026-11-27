# B11: Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa, cần xác nhận nghiệp vụ |
| **Repo** | `taschen-backoffice`, order-service nếu đổi nghiệp vụ |
| **Bug** | [Chi tiết B11](../../test-2026-11-27/loi.md#b11) · GM06-03 |
| **Điểm vào source** | `Guide me xử lý trả hàng` |

## Nguyên nhân

Yêu cầu bị từ chối kết thúc, nhưng khách có thể tạo yêu cầu khác khi đơn còn đủ điều kiện.

## Thay đổi

1. Đề xuất mô tả cả hai trạng thái trong Guide me. Kiểm màn khách và Seller để dùng đúng câu chữ.
2. Nếu chốt cấm gửi lại, cập nhật rule Order, phản hồi API và trạng thái thao tác ở UI.

## Code dự kiến

Trong apps/seller/src/messages/vi.json, order-return-process.steps.approve.deeper. Áp dụng câu dưới đây nếu chốt cho gửi lại và sửa cùng B12 vì hai lỗi nằm trong một chuỗi.

```text
Từ chối kết thúc yêu cầu hiện tại. Khách có thể gửi yêu cầu khác nếu đơn còn hạn và vẫn đủ điều kiện trả hàng.
```

## Kiểm thử lại

Kiểm yêu cầu bị từ chối, gửi lại trong hạn, quá hạn và đang có một yêu cầu mở.

## Liên quan

[SF-40](../../fix-plans/backend/SF-40-return-concurrent-duplicate-requests.md)

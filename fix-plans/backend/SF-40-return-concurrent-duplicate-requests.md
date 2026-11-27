# SF-40: Gửi đồng thời tạo nhiều yêu cầu đổi trả cho cùng một cuốn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa trong code trên `develop`, chờ retest |
| **Bản sửa** | [Backend PR #121](https://github.com/VELORA-MICRO/taschen-backend/pull/121), commit `3fd69ed` (BUG-005), merge `6cd3a1a`. Đối chiếu tại `d5b6ac2`. |
| **Bug** | [SF-40](../../storefront/loi.md#sf-40), [Storefront-Bất biến](../../storefront/bat-bien.md) |

## Hiện tượng

Đơn 57 đã hoàn tất, có 1 cuốn. Gửi 5 request `POST /api/v1/returns` cho cùng dòng hàng cùng lúc thì cả 5 yêu cầu được tạo (RMA-20261114-000006 đến -000010). Cả 5 đều duyệt và nhận hàng được. Dòng hàng ghi `returnedQuantity` 5 trên số lượng 1. **Mỗi yêu cầu có `refundAmount` 193.000 đ, bằng toàn bộ tiền đơn**, tổng ghi nhận hoàn 965.000 đ cho đơn 193.000 đ. Hiện payment-service không nghe `OrderReturnedEvent` (chỉ notification-service nghe), nên chưa có tiền bị chuyển tự động. Nhưng số liệu hoàn tiền đã sai, và việc hoàn tiền thủ công dựa trên số này sẽ sai theo. Gửi lần lượt thì yêu cầu thứ hai bị 409.

## Thay đổi đã merge

`ReturnRequestServiceImpl.create` lấy khóa ghi trên dòng đơn thuộc khách trong cùng transaction. Sau khi lấy khóa, code kiểm tra yêu cầu `PENDING` hoặc `APPROVED` còn mở, xác thực dòng hàng và tính tiền hoàn rồi mới lưu. Request thứ hai của cùng đơn chờ khóa và đọc được yêu cầu vừa tạo sau khi request đầu commit.

Source có `ReturnRequestConcurrencyIT` cho nhiều request tạo đồng thời. Chưa chạy lại test này trong lần cập nhật tài liệu.

## Kiểm thử lại

- Với đơn `COMPLETED` có một cuốn đủ điều kiện trả, gửi năm request tạo yêu cầu. Mong đợi một HTTP 201 và bốn HTTP 409, chỉ một yêu cầu trong DB và tổng tiền hoàn đề nghị không vượt tiền của dòng hàng.
- Gửi lại sau khi tạo thành công. Mong đợi 409 khi yêu cầu trước còn mở. Sau khi trả một phần hoàn tất, thử tạo yêu cầu cho số lượng còn lại và thử vượt số còn lại.
- Bản ghi lịch sử đã tạo trùng cần đối soát riêng. Kết quả tạo an toàn sau bản sửa chưa xác nhận được tình trạng của dữ liệu cũ.
- [BO-13](../../backoffice/loi.md#bo-13) theo dõi bước lập nhiều **phiếu trả về kho** từ một yêu cầu đã nhận hàng. Duyệt hoặc nhận cùng một phiếu đổi trả đồng thời thuộc SF-41.

# BO-13: Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service, order-service |
| **Bug** | [Chi tiết BO-13](../../backoffice/loi.md#bo-13) · GM06-07, GM06-08, GM11-04 |
| **Điểm vào source** | `ReturnToWarehouseRequestServiceImpl` |

## Nguyên nhân

Một yêu cầu trả một cuốn có thể làm kho cộng nhiều lần. Khi tạo phiếu, service lưu ID RMA nhưng chưa xác minh dòng hàng với Order. Khi duyệt, bước đọc trạng thái và cộng tồn chưa khóa cùng phiếu.

## Thay đổi

1. Đọc RMA tham chiếu từ API nội bộ của Order bằng client hiện có hoặc mở rộng contract nội bộ nếu thiếu dữ liệu. Kiểm đúng đơn, đã nhận hàng, đúng sách/biến thể. Cộng các dòng trùng trước khi so với lượng thực trả.
2. Đối soát phiếu và lịch sử cộng tồn trước khi thêm unique index theo RMA cho nguồn CUSTOMER_RETURN. Trả 409 khi đúng ràng buộc này bị vi phạm.
3. Khóa phiếu ở bước duyệt, đọc lại trạng thái và cộng tồn trong một giao dịch cùng BO-16.

## Code dự kiến

Trong bước tạo phiếu khách trả, xác minh RMA với Order. Các tên hàm dưới đây biểu diễn phần cần nối với client và mapper hiện có.

```java
var receivedReturn = orderClient.getReceivedReturn(request.returnRequestId());
validateOrderAndReturnedQuantities(request, receivedReturn);
return requestRepository.save(newCustomerReturn(request));
```

Trong Flyway, sau khi đối soát dữ liệu cũ, bảo vệ cùng RMA ở PostgreSQL. Khi duyệt, dùng truy vấn có khóa trước khi kiểm PENDING và gọi restock trong cùng transaction.

```sql
CREATE UNIQUE INDEX uq_customer_return_warehouse_rma
    ON return_to_warehouse_requests (return_request_id)
    WHERE source = 'CUSTOMER_RETURN' AND return_request_id IS NOT NULL;
```

## Kiểm thử lại

GM06-07/08, GM11-04. Trả 1 đơn vị thì tồn tăng đúng 1. Phiếu trùng, sai đơn, sai biến thể hoặc yêu cầu vượt số trả bị từ chối. Duyệt đồng thời cùng phiếu chỉ ghi nhận một lần.

## Liên quan

[BO-16](../../fix-plans/backend/BO-16-return-warehouse-missing-batch.md) · [SF-40](../../fix-plans/backend/SF-40-return-concurrent-duplicate-requests.md)

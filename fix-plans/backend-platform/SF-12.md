# SF-12: Gợi ý sách và sự kiện hành vi lỗi 500

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | **Đã sửa** theo xác nhận của người dùng ngày 2026-11-12; chưa đối chiếu commit/PR, chưa kiểm thử lại trong lần cập nhật này |
| **Repo** | `taschen-backend`, `taschen-platform` |
| **Khối lượng** | 3 dòng trong `dev.ps1`, cộng cấu hình Atlas |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-12), [Ảnh 1](../../images/SF-12-1.jpg) |

## Ghi chú cập nhật

Trạng thái hiện tại dựa trên xác nhận của người dùng. Nội dung kỹ thuật bên dưới là kế hoạch và ghi nhận trước khi xác nhận đã sửa; các mục còn việc phải làm, chưa commit hoặc tạm hoãn chỉ phản ánh thời điểm lập kế hoạch, không còn là trạng thái hiện tại. Chưa có thông tin để xác nhận chính xác cách sửa đã thực hiện hoặc tình trạng merge.

## Nguyên nhân (ghi nhận trước khi sửa)

Gateway định tuyến `/recommendations/*` và `POST /events` tới `tracking-service`, nhưng `dev.ps1` không khởi động service này. Khi thử chạy riêng, service gặp lỗi TLS tới cụm Atlas riêng của nó. Nghi ngờ do danh sách IP được phép trên Atlas, **chưa xác nhận** vì chưa có quyền truy cập.

## Việc cần làm khi tiếp tục

### 1. Trên Atlas

Xác nhận IP của máy nằm trong danh sách được phép của cụm tracking. Đặt biến `TRACKING_MONGO_URI` trong `taschen-platform/.env`.

### 2. `taschen-backend/dev.ps1`, dòng 26, 42-43 và 60-61

```diff
-  8080..8087 | ForEach-Object {
+  8080..8088 | ForEach-Object {
```

```diff
-         "inventory-service", "promotion-service", "notification-service", "api-gateway")
+         "inventory-service", "promotion-service", "notification-service", "tracking-service", "api-gateway")
```

```diff
-           "inventory-service", "promotion-service", "notification-service")
+           "inventory-service", "promotion-service", "notification-service", "tracking-service")
```

**Vì sao:** cả 3 chỗ phải sửa cùng nhau: dừng đúng port, khởi động service, và ánh xạ tên miền trong tệp hosts (`dev.ps1:60-71`). Biến `TRACKING_MONGO_URI` đã được truyền từ dòng 96.

## Không làm khi chưa xong

Không thêm `tracking-service` vào `dev.ps1` khi kết nối Atlas chưa thông, vì mọi lần `dev start` sẽ có một tab service bị lỗi.

## File mới

Không có.

## Kiểm thử lại

- `./dev.ps1 start tracking`: service lên, kết nối được Mongo.
- Trang chủ và chi tiết sách không còn lỗi 500 ở `/recommendations/*`, `POST /events`.
- Chạy lại các luồng liên quan.

## Tuân thủ quy tắc

Không commit chuỗi kết nối. API không đổi nên không cần sinh lại contract.

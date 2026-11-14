# SF-04: notification-service không khởi động vì thiếu biến Mongo

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | **Đã sửa** theo xác nhận của người dùng ngày 2026-11-12; chưa đối chiếu commit/PR, chưa kiểm thử lại trong lần cập nhật này |
| **Repo** | `taschen-backend` (`1364ff5` + thay đổi chưa commit), `taschen-platform` (`44f48b2`) |
| **Nhánh đề xuất** | `fix/notification-mongo-env` ở từng repo |
| **Khối lượng** | 2 dòng còn phải sửa |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-04), [Ảnh 1](../../images/SF-04-1.png) |

## Ghi chú cập nhật

Trạng thái hiện tại dựa trên xác nhận của người dùng. Nội dung kỹ thuật bên dưới là kế hoạch và ghi nhận trước khi xác nhận đã sửa; các mục còn việc phải làm, chưa commit hoặc tạm hoãn chỉ phản ánh thời điểm lập kế hoạch, không còn là trạng thái hiện tại. Chưa có thông tin để xác nhận chính xác cách sửa đã thực hiện hoặc tình trạng merge.

## Nguyên nhân (ghi nhận trước khi sửa)

`notification-service/application.yml:13` đọc biến `NOTIFICATION_MONGO_URI`, nhưng cả `dev.ps1` lẫn `docker-compose.yml` chỉ truyền `MONGO_URI`. Service rơi về giá trị mặc định `localhost:27017`, không có Mongo ở đó nên bị crash.

## Thay đổi

### 1. `taschen-backend/dev.ps1`, dòng 94-96 (đã làm)

```powershell
  # Each service reads its own Mongo variable; an older .env may only have MONGO_URI.
  NOTIFICATION_MONGO_URI = $(if ($envVars.NOTIFICATION_MONGO_URI) { $envVars.NOTIFICATION_MONGO_URI } else { $envVars.MONGO_URI })
  TRACKING_MONGO_URI = $(if ($envVars.TRACKING_MONGO_URI) { $envVars.TRACKING_MONGO_URI } else { $envVars.MONGO_URI })
```

**Vì sao:** dùng biến riêng nếu `.env` có, nếu không thì dùng `MONGO_URI` để `.env` cũ vẫn chạy. Đã kiểm chứng notification-service khởi động được. Việc còn lại chỉ là commit.

`git diff` của repo này còn có 4 file `pom.xml`, `.idea/` và `scripts/` không liên quan. Khi commit chỉ `git add dev.ps1`.

### 2. `taschen-platform/docker-compose.yml`, dòng 436

```diff
-      MONGO_URI: ${MONGO_URI}
+      NOTIFICATION_MONGO_URI: ${NOTIFICATION_MONGO_URI:-${MONGO_URI}}
```

**Vì sao:** cùng lỗi với `dev.ps1`, nhưng ở đường chạy bằng Docker. Giá trị dự phòng lồng nhau giữ cách hoạt động giống `dev.ps1`.

### 3. `taschen-platform/.env.example`, sau dòng 42

```diff
 MONGO_URI=                               # mongodb+srv://user:pass@cluster.mongodb.net/taschen_notification
+NOTIFICATION_MONGO_URI=                  # optional; falls back to MONGO_URI
```

**Vì sao:** người mới sao chép `.env.example` sẽ biết có biến này. Chỉ thêm tên biến, không có giá trị thật.

## File mới

Không có.

## Kiểm thử lại

- `./dev.ps1 start notification`: service lên, không có lỗi kết nối Mongo.
- `docker compose config` trong `taschen-platform`: `notification-service` có `NOTIFICATION_MONGO_URI`.
- Không in giá trị biến ra log hay dán vào PR.

## Tuân thủ quy tắc

Không commit thông tin bí mật, `.env` không đưa vào git. Không đổi API nên không cần sinh lại contract.

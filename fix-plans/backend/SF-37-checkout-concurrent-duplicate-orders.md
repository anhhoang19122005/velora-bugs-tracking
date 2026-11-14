# SF-37: Gửi đặt hàng đồng thời tạo nhiều đơn từ một giỏ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend`, số dòng theo `develop` `e090ed4` |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38-40`, tách từ `develop` (chung nhánh với SF-38, SF-40) |
| **Khối lượng** | Khoảng 15 dòng code, 1 unit test, 1 integration test |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-37) và Storefront-Bất biến (kịch bản 1 đến 5) |

## Hiện tượng

Giỏ có 1 cuốn. Gửi 2, 3 hoặc 10 request `POST /api/v1/orders` giống nhau cùng lúc thì tạo đúng 2, 3, 10 đơn, và inventory trừ kho bấy nhiêu lần (đo ngày 14/11: tồn 44 xuống 34 với 10 request). Gửi lần lượt thì không bị. Trên giao diện, click 3 lần liên tiếp chỉ ra 1 request vì nút đã khóa, nên lỗi lọt qua khi khách mở 2 tab, bấm lại lúc mạng chậm, hoặc proxy gửi lại request.

## Nguyên nhân

`OrderServiceImpl.checkout` (dòng 103-148) đọc giỏ ở dòng 107, kiểm tra và lưu đơn ở dòng 141, rồi mới xóa giỏ ở dòng 144. Không có khóa nào giữa bước đọc và bước xóa. Các request đồng thời đều đọc thấy giỏ đầy đủ trước khi request nào kịp xóa, nên mỗi request tạo một đơn. Mỗi đơn phát `OrderPlacedEvent` (dòng 145), inventory-service giữ hàng cho từng đơn, nên kho bị trừ nhiều lần.

Giỏ là một giá trị JSON ở khóa Redis `cart:{userId}` (`CartServiceImpl.java:32`, `:92-106`), đọc rồi ghi lại toàn bộ, không có thao tác nguyên tử.

## Thay đổi

File `services/order-service/src/main/java/vn/edu/iuh/fit/taschen/order/service/impl/OrderServiceImpl.java`: khóa checkout theo người dùng bằng Redis `SET NX` có TTL, giữ trong suốt thân hàm.

```diff
+    private static final Duration CHECKOUT_LOCK_TTL = Duration.ofSeconds(30);
+    private final StringRedisTemplate redisTemplate;
 
     @Override
     @Transactional
     public OrderResponse checkout(CreateOrderRequest request) {
         Long userId = CurrentUserProvider.currentUserId();
+        // One checkout per user at a time: concurrent submits of the same cart must not each create an order.
+        String lockKey = "checkout-lock:" + userId;
+        String token = UUID.randomUUID().toString();
+        if (!Boolean.TRUE.equals(redisTemplate.opsForValue().setIfAbsent(lockKey, token, CHECKOUT_LOCK_TTL))) {
+            throw new AppException(ErrorCode.CONFLICT, "A checkout is already in progress for this cart");
+        }
+        try {
             CartResponse cart = cartService.getMyCart();
             ... (thân hàm giữ nguyên) ...
             return toOrderResponse(saved);
+        } finally {
+            if (token.equals(redisTemplate.opsForValue().get(lockKey))) {
+                redisTemplate.delete(lockKey);
+            }
+        }
     }
```

**Vì sao cách này:**

- Giỏ đã nằm trong Redis, `order-service` đã có `spring-boot-starter-data-redis` (`pom.xml:75`), nên `StringRedisTemplate` được Spring Boot tự cấu hình. Không thêm thư viện, không cần migration.
- Khóa nhả trong `finally`, trước khi transaction commit. Như vậy vẫn đúng, vì giỏ đã bị xóa ở dòng 144 (lệnh xóa Redis có hiệu lực ngay, không theo transaction). Request chờ sau sẽ đọc thấy giỏ trống và nhận 409 "Cart is empty" như hiện nay.
- So token trước khi xóa để không xóa nhầm khóa của request khác khi TTL đã hết.
- Request bị chặn nhận 409 CONFLICT, cùng mã storefront đang xử lý cho lỗi đặt hàng.

**Không chọn:** header `Idempotency-Key`. Cách đó cần sửa storefront và nơi lưu kết quả request, trong khi khóa theo người dùng đã đủ cho lỗi này.

## Test

- `OrderServiceTest`: thêm mock `StringRedisTemplate`. Ca `checkout_lockHeld_throwsConflictWithoutSaving`: `setIfAbsent` trả `false` thì ném CONFLICT, không gọi `orderRepository.save` và `cartService.clearCart`. Ca thường thêm stub `setIfAbsent` trả `true`.
- `CartAndOrderIT` (đã có Postgres và Redis container): `checkout_concurrentSubmits_createOneOrder`. Thêm 1 cuốn vào giỏ, gửi 5 request checkout qua `ExecutorService` và `CountDownLatch`, kiểm tra đúng 1 response 201, còn lại 409, và chỉ có 1 bản ghi `orders` của user.

## Kiểm thử lại

- Chạy lại kịch bản 1 đến 3 ở trang Storefront-Bất biến: 2, 3, 10 request cùng lúc chỉ ra 1 đơn, tồn kho chỉ trừ 1 lần.
- Kịch bản 5 (click 3 lần trên giao diện) vẫn ra 1 đơn.
- `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `order-service`.

## Tuân thủ quy tắc

Java 4 dấu cách, Spotless. Không đổi contract (vẫn là 409 đã có trong catalog lỗi), không cần sinh lại OpenAPI.

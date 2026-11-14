# SF-37: Gửi đặt hàng đồng thời tạo nhiều đơn từ một giỏ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Hướng sửa đã chốt ngày 14/11: Idempotency-Key kết hợp khóa theo người dùng |
| **Repo** | `taschen-backend` (`order-service`) và `taschen-storefront`, số dòng theo `develop` `e090ed4` (backend) và `cdb599a` (storefront) |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38-40`, tách từ `develop` (chung nhánh với SF-38, SF-40; storefront dùng nhánh cùng tên) |
| **Khối lượng** | Khoảng 110 dòng backend, 20 dòng storefront, 6 unit test, 3 integration test |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-37) và Storefront-Bất biến (kịch bản 1 đến 5) |

## Hiện tượng

Giỏ có 1 cuốn. Gửi 2, 3 hoặc 10 request `POST /api/v1/orders` giống nhau cùng lúc thì tạo đúng 2, 3, 10 đơn, và inventory trừ kho bấy nhiêu lần (đo ngày 14/11: tồn 44 xuống 34 với 10 request). Gửi lần lượt thì không bị. Trên giao diện, click 3 lần liên tiếp chỉ ra 1 request vì nút đã khóa, nên lỗi lọt qua khi khách mở 2 tab, bấm lại lúc mạng chậm, hoặc có lớp mạng gửi lại request.

Có thêm một vấn đề liên quan, không phải đơn trùng. Nếu request đã tạo đơn nhưng **phản hồi bị mất** (mạng đứt), khách bấm lại sẽ nhận 409 "Cart is empty" và chỉ thấy toast "Đặt hàng thất bại", trong khi đơn đã có ở trang Đơn hàng.

## Nguyên nhân

`OrderServiceImpl.checkout` (dòng 103-148) đọc giỏ ở dòng 107, kiểm tra và lưu đơn ở dòng 141, rồi mới xóa giỏ ở dòng 144. Không có khóa nào giữa bước đọc và bước xóa. Các request đồng thời đều đọc thấy giỏ đầy đủ trước khi request nào kịp xóa, nên mỗi request tạo một đơn. Mỗi đơn phát `OrderPlacedEvent` (dòng 145), inventory-service giữ hàng cho từng đơn, nên kho bị trừ nhiều lần.

Giỏ là một giá trị JSON ở khóa Redis `cart:{userId}` (`CartServiceImpl.java:32`, `:92-106`), đọc rồi ghi lại toàn bộ, không có thao tác nguyên tử.

Server không có khái niệm "request này đã xử lý rồi": server xử lý xong dù khách mất kết nối, và lần gửi lại chỉ thấy giỏ trống.

## Vì sao không dùng riêng khóa theo người dùng (Redis `SET NX`, TTL 30 giây)

Phương án đầu của plan này. Kịch bản kiểm tra ngày 14/11 cho thấy nó thiếu hai chỗ:

- **Request chạy lâu hơn TTL.** `order-service` không cấu hình timeout riêng cho Feign, nên dùng mặc định (đọc tối đa khoảng 60 giây mỗi lần gọi, chưa kiểm chứng giá trị chạy thật). Nếu inventory hoặc catalog treo, request đầu còn chạy khi khóa đã hết hạn, giỏ chưa bị xóa, và click thứ hai tạo đơn trùng.
- **Mất phản hồi.** Khóa đã nhả khi request đầu xong. Lần bấm lại 45 giây sau nhận "Cart is empty", không biết đơn đã tạo.

Cả hai được giải quyết bằng Idempotency-Key: server nhớ kết quả của từng lần đặt và trả lại đúng đơn cũ khi nhận lại cùng key. Khóa theo người dùng vẫn giữ để chặn trường hợp hai tab dùng hai key khác nhau.

## Thiết kế

Mỗi lần đặt hàng của storefront mang một header `Idempotency-Key` (UUID). Server xử lý theo bảng:

| Tình huống | Kết quả |
|---|---|
| Key mới | Đặt hàng bình thường, lưu kết quả theo key trong 24 giờ |
| Cùng key, đã xong, cùng nội dung | Trả lại **đúng đơn cũ**, HTTP 201, kèm header `Idempotent-Replayed: true`, không tạo đơn |
| Cùng key, đã xong, nội dung khác (ví dụ đổi địa chỉ rồi bấm lại) | 400 `VALIDATION_ERROR` |
| Cùng key, đang xử lý | 409 `CONFLICT` |
| Key khác, trong lúc người đó đang có một lần đặt chạy | 409 `CONFLICT` (khóa theo người dùng) |
| Không gửi header | Chỉ có khóa theo người dùng (client cũ vẫn chạy) |
| Đặt hàng thất bại | Xóa key và nhả khóa, gửi lại cùng key được xử lý như lần mới |

Redis (dùng `StringRedisTemplate`, order-service đã có `spring-boot-starter-data-redis`, `pom.xml:75`):

- `checkout-idem:{userId}:{key}` = `PENDING:{hash}` (TTL 120 giây) rồi `DONE:{orderId}:{hash}` (TTL 24 giờ).
- `checkout-lock:{userId}` = token ngẫu nhiên (TTL 120 giây).

`hash` là SHA-256 của `addressId`, `promotionId`, `paymentMethod` và danh sách `bookId:variantId:quantity` đã sắp xếp. Không đưa `aiAssisted` vào vì nó không đổi nội dung đơn.

**Phải điều phối bên ngoài transaction.** `OrderServiceImpl.checkout` có `@Transactional`; nếu ghi `DONE` hoặc nhả khóa bên trong nó thì có thể ghi `DONE` cho một đơn chưa commit hoặc bị rollback. Vì vậy thêm một lớp điều phối không có `@Transactional`, gọi `checkout` (commit xảy ra khi nó trả về), rồi mới ghi `DONE`.

## Các trường hợp đã cover

Ký hiệu K là Idempotency-Key của một lần đặt hàng; "cùng K" nghĩa là storefront gửi lại đúng key đó với cùng nội dung đơn.

### Kịch bản mất phản hồi (ví dụ đã nêu)

Khách bấm Đặt hàng, request đã tới server và đơn được tạo, nhưng mạng đứt nên khách không nhận phản hồi và không thấy gì.

| Thời điểm | Chuyện xảy ra | Kết quả |
|---|---|---|
| t = 0 | Bấm Đặt hàng, gửi K | Server ghi `PENDING:K`, giữ khóa theo người dùng, tạo đơn #123 |
| t ≈ 1 giây | Đơn commit, server ghi `DONE:123:K` (24 giờ), nhả khóa. Mạng đứt nên phản hồi mất | Khách không biết đơn đã tạo |
| t = 45 giây, **mạng vẫn đứt** | Khách bấm lại | Request không tới được server, giao diện báo lỗi. Server không đổi gì |
| t = 65 giây, **mạng đã về** | Khách bấm lại, giao diện vẫn dùng K | Server thấy `DONE:123:K` cùng nội dung, trả lại **đơn #123** (201, `Idempotent-Replayed: true`). Giao diện chuyển tới đơn, không tạo đơn mới |
| t = 10 phút | Khách bấm lại cùng K | Như trên. `DONE` còn hiệu lực 24 giờ |
| Khách tải lại trang rồi bấm lại | Nhờ lưu K trong `sessionStorage`, vẫn gửi K | Như trên. Nếu không lưu K thì sinh K mới, giỏ trống, nhận 409 và thông báo "mở trang Đơn hàng để kiểm tra" (không trùng đơn) |

Vì khóa chỉ giữ trong lúc request chạy (tối đa 120 giây) còn kết quả giữ 24 giờ, không còn chuyện "khóa hết hạn sau 30 giây rồi bấm lại thì sao".

### Bảng đầy đủ

| # | Tình huống | Cơ chế xử lý | Kết quả | Kiểm bằng |
|---|---|---|---|---|
| 1 | Hai đến mười request giống hệt, cùng K, gửi cùng lúc (bấm nhanh, proxy hoặc trình duyệt gửi lại) | `SET NX` trên key | Đúng 1 đơn. Request còn lại 409 (đang xử lý) hoặc 201 replay cùng đơn | IT `checkout_concurrentSubmitsSameKey_createOneOrder` |
| 2 | Cùng lúc nhưng khác K (hai tab, hai thiết bị) | Khóa theo người dùng | Đúng 1 đơn, request còn lại 409. Khi tab kia xong, tab này nhận 409 "Cart is empty": không trùng, giao diện nhắc kiểm tra Đơn hàng | IT `checkout_concurrentSubmitsDifferentKeys_createOneOrder` |
| 3 | Không gửi header (client cũ) cùng lúc | Khóa theo người dùng | Đúng 1 đơn. Không có khả năng nhận lại đơn khi mất phản hồi | Unit `checkout_noKeyLockHeld_throwsConflict`, kịch bản 1 đến 3 |
| 4 | Request đầu chưa tới server, khách bấm lại | Không có key hay khóa nào được ghi | Tạo đơn bình thường, không mất gì | Kịch bản mất phản hồi, dòng t = 45 giây |
| 5 | Request đầu chạy lâu (inventory hoặc catalog chậm), khách bấm lại cùng K trong lúc đó | `PENDING:K` (120 giây) và khóa (120 giây); Feign timeout 10 giây | 409 "đang xử lý", không trùng. Khi xong, bấm lại trả đơn đã tạo | Kiểm thử lại thủ công (làm chậm inventory) |
| 6 | Request đầu chạy lâu, khách bấm lại với K khác | Khóa theo người dùng | 409, không trùng | Như dòng 2 |
| 7 | Gửi lại cùng K nhưng nội dung đã đổi (địa chỉ, phương thức, mã, số lượng) | So `hash` nội dung | 400 `VALIDATION_ERROR`. Giao diện đổi chữ ký nên tự dùng K mới và đặt được | Unit `checkout_keyDoneWithDifferentRequest_throwsValidationError` |
| 8 | Lần thử đầu thất bại (hết hàng, mã không hợp lệ, lỗi hệ thống) rồi thử lại cùng K | Xóa key và nhả khóa khi lỗi | Lần sau chạy như lần mới, không bị kẹt "đang xử lý" | Unit `checkout_orderServiceFails_deletesKeyAndReleasesLock` |
| 9 | Người dùng A và B dùng cùng K | Key có `userId` trong tên | Hai bên độc lập, không nhìn thấy đơn của nhau | Nằm trong thiết kế; thêm 1 ca vào `CartAndOrderIT` nếu cần |
| 10 | Replay trả trạng thái hiện tại của đơn (đã hủy hoặc đã đổi trạng thái sau khi tạo) | Replay đọc lại đơn bằng `getOrder` thay vì lưu bản sao | Khách thấy đơn đúng trạng thái hiện tại | Nằm trong thiết kế |
| 11 | `DONE` được ghi trước khi đơn commit | Điều phối ngoài transaction, ghi `DONE` sau khi `checkout` trả về | Không bao giờ trỏ tới đơn bị rollback | Unit `checkout_success_storesDoneOnlyAfterCheckoutReturned` |
| 12 | Redis lỗi | Giỏ hàng cũng nằm ở Redis | Checkout vốn đã không chạy được, không thêm lỗi mới | Không cần ca riêng |
| 13 | Bấm nhanh trên cùng một tab | Nút bị khóa khi đang gửi | 1 request. Nếu lọt qua thì rơi vào dòng 1 | Kịch bản 5 ở trang Storefront-Bất biến |

### Chưa cover (biết trước)

| # | Tình huống | Hệ quả | Hướng xử lý nếu cần |
|---|---|---|---|
| A | Request chạy lâu hơn 120 giây (mọi lệnh gọi Feign đều treo gần hết timeout, giỏ nhiều dòng) rồi khách bấm lại | Key và khóa hết hạn khi request đầu còn chạy, đơn trùng có thể xảy ra | Gia hạn khóa theo từng dòng giỏ; hoặc giảm timeout Feign |
| B | Tiến trình `order-service` chết giữa lúc đơn đã commit và lúc ghi `DONE` | Key kẹt `PENDING` 120 giây, sau đó bấm lại nhận 409 "Cart is empty" | Hiếm; chấp nhận. Muốn triệt để thì lưu `idempotencyKey` vào cột của bảng `orders` |
| C | Khách dùng client không gửi header và mất phản hồi | Không nhận lại được đơn | Chỉ storefront mới gửi key |
| D | Mất phản hồi ở bước khởi tạo thanh toán VNPay (`POST /orders/{id}/payments/initiate`) sau khi đặt hàng thành công | Giao diện báo "Đơn đã tạo, mở đơn hàng để thử thanh toán lại". Bước khởi tạo thanh toán đồng thời còn tạo nhiều bản ghi thanh toán (xem SF-43) | Sửa ở SF-43, không thuộc plan này |
| E | Sự kiện `OrderPlacedEvent` bị inventory xử lý hai lần (RabbitMQ giao ít nhất một lần) | Có thể giữ hàng hai lần cho một đơn | Ngoài phạm vi; kiểm tra tính bất biến của listener inventory |

## Thay đổi backend

### 1. Lớp điều phối mới

`services/order-service/src/main/java/vn/edu/iuh/fit/taschen/order/service/CheckoutCoordinator.java`:

```java
package vn.edu.iuh.fit.taschen.order.service;

@Service
@RequiredArgsConstructor
public class CheckoutCoordinator {

    private static final Duration IN_FLIGHT_TTL = Duration.ofSeconds(120);
    private static final Duration DONE_TTL = Duration.ofHours(24);
    private static final Pattern KEY_FORMAT = Pattern.compile("[A-Za-z0-9_-]{8,64}");
    private static final RedisScript<Long> RELEASE_LOCK = RedisScript.of(
            "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",
            Long.class);

    private final StringRedisTemplate redis;
    private final OrderService orderService;

    public record Result(OrderResponse order, boolean replayed) {}

    // Runs outside any transaction on purpose: OrderService#checkout commits when it returns, and only then
    // is the result remembered, so a replay can never point at an order that was rolled back.
    public Result checkout(CreateOrderRequest request, String idempotencyKey) {
        Long userId = CurrentUserProvider.currentUserId();
        String keyRedis = null;
        String hash = fingerprint(request);
        if (idempotencyKey != null) {
            if (!KEY_FORMAT.matcher(idempotencyKey).matches()) {
                throw new AppException(ErrorCode.VALIDATION_ERROR, "Idempotency-Key must be 8-64 letters, digits, '-' or '_'");
            }
            keyRedis = "checkout-idem:" + userId + ":" + idempotencyKey;
            Result replay = claimOrReplay(keyRedis, hash);
            if (replay != null) {
                return replay;
            }
        }
        String lockKey = "checkout-lock:" + userId;
        String token = UUID.randomUUID().toString();
        if (!Boolean.TRUE.equals(redis.opsForValue().setIfAbsent(lockKey, token, IN_FLIGHT_TTL))) {
            forget(keyRedis);
            throw new AppException(ErrorCode.CONFLICT, "Another checkout is already in progress for this user");
        }
        try {
            OrderResponse order = orderService.checkout(request);
            if (keyRedis != null) {
                redis.opsForValue().set(keyRedis, "DONE:" + order.id() + ":" + hash, DONE_TTL);
            }
            return new Result(order, false);
        } catch (RuntimeException e) {
            forget(keyRedis); // a failed attempt must not block the retry with the same key
            throw e;
        } finally {
            redis.execute(RELEASE_LOCK, List.of(lockKey), token);
        }
    }

    // Returns the stored order for a finished attempt, null when this call owns the key now.
    private Result claimOrReplay(String keyRedis, String hash) {
        if (Boolean.TRUE.equals(redis.opsForValue().setIfAbsent(keyRedis, "PENDING:" + hash, IN_FLIGHT_TTL))) {
            return null;
        }
        String stored = redis.opsForValue().get(keyRedis);
        if (stored == null) { // expired between the two calls: take it
            return claimOrReplay(keyRedis, hash);
        }
        String[] parts = stored.split(":");
        if (!parts[parts.length - 1].equals(hash)) {
            throw new AppException(ErrorCode.VALIDATION_ERROR, "Idempotency-Key was already used for a different request");
        }
        if ("PENDING".equals(parts[0])) {
            throw new AppException(ErrorCode.CONFLICT, "This checkout is still being processed");
        }
        return new Result(orderService.getOrder(Long.parseLong(parts[1])), true);
    }

    private void forget(String keyRedis) {
        if (keyRedis != null) {
            redis.delete(keyRedis);
        }
    }

    private static String fingerprint(CreateOrderRequest request) {
        String items = request.items().stream()
                .map(i -> i.bookId() + ":" + i.variantId() + ":" + i.quantity())
                .sorted()
                .collect(Collectors.joining(","));
        String raw = request.addressId() + "|" + request.promotionId() + "|" + request.paymentMethod() + "|" + items;
        return HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256").digest(raw.getBytes(StandardCharsets.UTF_8)));
    }
}
```

`MessageDigest.getInstance` ném `NoSuchAlgorithmException` (checked): bọc trong `try/catch` rồi ném `IllegalStateException`. Đoạn trên rút gọn để dễ đọc.

### 2. Controller

`OrderController.java:30-35`:

```diff
     @PostMapping
     @Operation(summary = "Checkout: place an order from the current user's cart")
     @SecurityRequirement(name = "bearerAuth")
-    public ResponseEntity<ApiResponse<OrderResponse>> checkout(@Valid @RequestBody CreateOrderRequest request) {
-        OrderResponse response = orderService.checkout(request);
-        return ResponseEntity.status(HttpStatus.CREATED).body(ApiResponse.ok(response, "Order placed"));
+    public ResponseEntity<ApiResponse<OrderResponse>> checkout(
+            @Valid @RequestBody CreateOrderRequest request,
+            @Parameter(description = "Same key on a retry returns the order already created")
+                    @RequestHeader(value = "Idempotency-Key", required = false) String idempotencyKey) {
+        CheckoutCoordinator.Result result = checkoutCoordinator.checkout(request, idempotencyKey);
+        ResponseEntity.BodyBuilder response = ResponseEntity.status(HttpStatus.CREATED);
+        if (result.replayed()) {
+            response.header("Idempotent-Replayed", "true");
+        }
+        return response.body(ApiResponse.ok(result.order(), "Order placed"));
     }
```

Thêm field `private final CheckoutCoordinator checkoutCoordinator;`. `OrderService.checkout` giữ nguyên, nên các test hiện có không phải sửa.

### 3. Timeout cho Feign

Để một request không thể chạy lâu hơn khóa. `services/order-service/src/main/resources/application.yml`:

```yaml
spring:
  cloud:
    openfeign:
      client:
        config:
          default:
            connect-timeout: 3000
            read-timeout: 10000
```

Với 10 giây mỗi lần gọi, một giỏ vài dòng chạy tối đa khoảng 1 phút khi mọi lần gọi đều treo, nằm trong TTL 120 giây. Giỏ rất nhiều dòng mà mọi lần gọi đều treo có thể vượt; chấp nhận được vì lúc đó checkout đã hỏng. Nếu cần chặt hơn thì gia hạn khóa theo từng dòng.

## Thay đổi storefront

`src/modules/orders/api/order.api.ts:40-41`:

```diff
-  placeOrder: (payload: PlaceOrderPayload) =>
-    http.post<GetOrderResponse>("orders", payload),
+  placeOrder: (payload: PlaceOrderPayload, idempotencyKey?: string) =>
+    http.post<GetOrderResponse>(
+      "orders",
+      payload,
+      idempotencyKey ? { headers: { "Idempotency-Key": idempotencyKey } } : undefined,
+    ),
```

`checkout/_components/CheckoutScreen.tsx`, quanh dòng 122: giữ cùng một key cho các lần thử lại của cùng một đơn.

```diff
+      // One key per order attempt: a retry after a lost response gets the order already created back.
+      const signature = JSON.stringify(payload);
+      if (attempt.current?.signature !== signature) {
+        attempt.current = { key: crypto.randomUUID(), signature };
+      }
-      const order = await orderService.placeOrder(payload);
+      const order = await orderService.placeOrder(payload, attempt.current.key);
+      attempt.current = null; // done: the next order gets a new key
```

với `const attempt = React.useRef<{ key: string; signature: string } | null>(null);` cạnh các `useState` (dòng 74-76). Không xóa key khi lỗi: server tự bỏ key của lần thất bại, và key giữ nguyên chính là thứ giúp lần bấm lại nhận lại đơn.

Tải lại trang thì `useRef` mất key. Muốn lần bấm sau khi tải lại vẫn nhận lại đơn cũ thì lưu `{ key, signature }` vào `sessionStorage` (bọc `try/catch`, đọc khi khởi tạo, xóa khi đặt xong). Thêm khoảng 8 dòng; nên làm vì mất mạng thường đi kèm tải lại trang.

Nhánh `catch` (dòng 157-169): thêm trường hợp 409 để khách biết kiểm tra đơn thay vì chỉ thấy "thất bại". Server không trả lý do riêng cho 409 (`CONFLICT` dùng chung câu mặc định), nên dùng một thông báo chung:

```diff
+      } else if ((error as { code?: string } | null)?.code === "CONFLICT") {
+        toast.error("Đơn đang được xử lý hoặc đã được tạo. Mở trang Đơn hàng để kiểm tra trước khi đặt lại.");
```

Proxy `src/app/api/[...path]/route.ts` chuyển tiếp mọi header trừ nhóm trong `STRIP` (dòng 26-38), nên `Idempotency-Key` đi qua. Gateway cho phép mọi header (`CorsConfig.java:30`). Kiểm tra `http.post` nhận tham số thứ ba là `config` (đã thấy chữ ký `post = <T>(path, data, config)`, `http.ts:162-167`).

## Test

**`CheckoutCoordinatorTest` (Mockito, mock `StringRedisTemplate` và `ValueOperations`)**
- `checkout_noKeyLockHeld_throwsConflict`
- `checkout_keyAlreadyDone_returnsStoredOrderWithoutCheckout`
- `checkout_keyDoneWithDifferentRequest_throwsValidationError`
- `checkout_keyPending_throwsConflict`
- `checkout_orderServiceFails_deletesKeyAndReleasesLock`
- `checkout_success_storesDoneOnlyAfterCheckoutReturned`: `InOrder` kiểm tra `orderService.checkout` chạy trước lệnh ghi `DONE`.

**`CartAndOrderIT` (đã có Postgres và Redis container)**
- `checkout_sameKeyTwice_returnsSameOrderAndOneRow`: gọi hai lần cùng key, hai response cùng `id`, lần hai có header `Idempotent-Replayed`, bảng `orders` chỉ có 1 dòng của người dùng.
- `checkout_concurrentSubmitsDifferentKeys_createOneOrder`: 5 request cùng lúc với 5 key khác nhau qua `ExecutorService` và `CountDownLatch`: đúng 1 response 201, các request còn lại 409, 1 dòng `orders`.
- `checkout_concurrentSubmitsSameKey_createOneOrder`: 5 request cùng key: đúng 1 đơn được tạo; các request còn lại là 409 (đang xử lý) hoặc 201 replay cùng `id`.

## Kiểm thử lại

- Kịch bản 1 đến 3 ở trang Storefront-Bất biến (2, 3, 10 request cùng lúc, không gửi key): chỉ ra 1 đơn, tồn chỉ trừ 1 lần.
- **Mất phản hồi:** gửi request với key K, bỏ qua phản hồi, gửi lại cùng K và cùng nội dung ở giây 45 và ở phút 10: cả hai trả đúng đơn đầu tiên, không có đơn thứ hai.
- **Request chạy lâu:** làm inventory-service chậm hơn 30 giây (ví dụ tạm dừng tiến trình), gửi lại cùng K trong lúc đó: nhận 409, không tạo đơn trùng; sau khi xong, gửi lại cùng K trả đơn đã tạo.
- Đổi địa chỉ rồi bấm lại cùng key: 400, và giao diện (đã đổi chữ ký payload) tự dùng key mới nên vẫn đặt được.
- Kịch bản 5 (click 3 lần liên tiếp trên giao diện) vẫn ra 1 đơn.
- `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `order-service`; `pnpm lint` và `pnpm typecheck` trong storefront.

## Giới hạn còn lại

- Nếu tiến trình `order-service` chết giữa lúc đơn đã commit và lúc ghi `DONE`, key kẹt ở `PENDING` đến hết 120 giây; sau đó gửi lại sẽ nhận "Cart is empty" như hiện nay. Khe này rất hẹp (hai lệnh liên tiếp), chấp nhận.
- Key chỉ có tác dụng với client gửi header. Client cũ vẫn được khóa theo người dùng chặn đơn trùng, nhưng không có tính năng nhận lại đơn cũ.
- Hai tab khác nhau có key khác nhau: tab nào bấm sau bị 409 trong lúc tab kia còn đang chạy, và nhận "Cart is empty" khi tab kia đã xong, đúng như hiện nay.

## Tuân thủ quy tắc

- Java 4 dấu cách, Spotless. TypeScript theo ESLint của storefront.
- Header mới nằm trong OpenAPI nên sinh lại contract: `./mvnw.cmd -Popenapi` để cập nhật `services/order-service/contract/openapi.yaml`. Không sửa tay file sinh ra. Không cần migration.
- Dùng cùng kiểu mã lỗi hiện có (`CONFLICT`, `VALIDATION_ERROR`), không thêm mã mới vào `ErrorCode`, nên không đổi danh mục lỗi trong `taschen-contracts`.

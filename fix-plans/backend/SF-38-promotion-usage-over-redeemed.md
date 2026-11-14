# SF-38: Mã giảm giá được cấp cho nhiều đơn hơn số lượt

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Đã chốt phương án B ngày 14/11 |
| **Repo** | `taschen-backend` (`order-service`, `promotion-service`), số dòng theo `develop` `e090ed4` |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38-40`, chung nhánh với SF-37, SF-40 |
| **Khối lượng** | Khoảng 70 dòng code, 3 DTO mới, 1 endpoint nội bộ mới, 10 unit test, 2 integration test |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-38) và Storefront-Bất biến (kịch bản 15 đến 17) |

## Hiện tượng

- Mã còn 1 lượt, 2 người đặt cùng lúc: cả 2 đơn đều giảm 19.300 đ (đơn 58, 59).
- Một người, mã còn 3 lượt, bấm đặt 3 lần cùng lúc: cả 3 đơn đều giảm, số lượng mã chỉ giảm từ 3 xuống 2 (đơn 60, 61, 62).
- Số lượng mã không xuống âm; lỗi là giảm giá được cấp vượt số lượt.

## Nguyên nhân

Có hai bước tách rời nhau:

1. Lúc đặt hàng, `checkout` chỉ **kiểm tra** mã (`OrderServiceImpl.java:115-116`, gọi `validate`, chỉ đọc) rồi ghi `discountAmount` vào đơn.
2. Lượt dùng chỉ được **ghi** khi đơn chuyển CONFIRMED: `advanceToConfirmed` (dòng 636-642) gọi `recordPromotionUsageBestEffort` (dòng 659-672), và hàm này nuốt mọi lỗi.

Phía promotion-service, `recordUsageAttempt` (`PromotionServiceImpl.java:311-350`) đã an toàn khi chạy đồng thời: có `@Version` và kiểm tra lại số lượng. Khi người dùng đã có lượt dùng, nó trả lại bản ghi cũ mà không báo lỗi (dòng 325-330). Nhưng order-service không đọc kết quả (Feign khai báo `ApiResponse<Void>`, `PromotionServiceClient.java:28-29`) và nuốt cả lỗi 409 khi mã hết lượt. Vì vậy đơn thứ hai trở đi vẫn giữ giảm giá.

Lỗi không chỉ xảy ra khi gửi đồng thời. Với VNPay, đơn đang chờ thanh toán chưa ghi lượt dùng, nên khách có thể đặt đơn thứ hai bằng cùng mã trước khi thanh toán đơn đầu, và `validate` vẫn cho qua. Đây là suy luận từ code, chưa chạy thử.

## Quy tắc đã chốt (phương án B)

- Lượt dùng được **giữ ngay lúc đặt hàng**. Đây là thay đổi chủ ý cũ ở `PromotionServiceClient.java:14-18` (chỉ ghi lượt cho đơn đã thanh toán).
- **Hệ thống hủy** đơn thì hoàn lượt: giữ hàng thất bại, thanh toán VNPay thất bại, sai số tiền thanh toán.
- **Nhân viên hủy** (`updateStatus` sang CANCELLED) cũng hoàn lượt (chốt ngày 14/11).
- **Khách tự hủy** thì không hoàn, đúng quy tắc đã chốt ngày 14/11.

## Thay đổi

### 1. promotion-service: endpoint nội bộ hoàn lượt theo đơn

`repository/PromotionUsageRepository.java`:

```java
    // One usage per order (an order carries at most one promotion); used to release a system-cancelled order's claim.
    Optional<PromotionUsage> findByOrderId(Long orderId);
```

`service/PromotionService.java` và `service/impl/PromotionServiceImpl.java`:

```java
    @Override
    public void releaseUsageByOrder(Long orderId) {
        // Same retry-on-optimistic-lock loop as recordUsage, since a concurrent claim may bump the version.
        for (int attempt = 1; attempt <= MAX_USAGE_ATTEMPTS; attempt++) {
            try {
                usageTransactionTemplate.executeWithoutResult(status -> promotionUsageRepository
                        .findByOrderId(orderId)
                        .ifPresent(usage -> {
                            Promotion promotion = usage.getPromotion();
                            promotion.setQuantity(promotion.getQuantity() + 1);
                            promotionRepository.saveAndFlush(promotion);
                            promotionUsageRepository.delete(usage);
                        }));
                return;
            } catch (OptimisticLockingFailureException e) {
                if (attempt == MAX_USAGE_ATTEMPTS) {
                    throw new AppException(ErrorCode.CONFLICT, "Could not release promotion usage for order " + orderId, e);
                }
            }
        }
    }
```

Thao tác này lặp lại an toàn: nếu không còn lượt dùng của đơn (đã hoàn, hoặc đơn không có mã) thì không làm gì. Xóa bản ghi lượt dùng cũng xóa luôn ràng buộc "mỗi người một lượt" (`uk_promotion_usage_user_promo`), nên khách dùng lại được mã.

`controller/PromotionController.java`, cạnh `recordUsageById` (dòng 156):

```java
    @PostMapping("/usages/release")
    @Operation(summary = "Service-to-service: give back the usage a system-cancelled order claimed"
            + " (requires the X-Internal-Token shared secret)")
    public ResponseEntity<ApiResponse<Void>> releaseUsage(@Valid @RequestBody ReleasePromotionUsageRequest request) {
        promotionService.releaseUsageByOrder(request.orderId());
        return ResponseEntity.ok(ApiResponse.ok(null));
    }
```

DTO mới `dto/request/ReleasePromotionUsageRequest.java`: `record ReleasePromotionUsageRequest(@NotNull @Positive Long orderId)`.

Chặn bằng token nội bộ giống các endpoint usages khác:

- `config/WebMvcConfig.java:15-24`: thêm `"/api/v1/promotions/usages/release"` vào `addPathPatterns`.
- `config/SecurityConfig.java:28-29`: thêm đường dẫn này vào nhóm `HttpMethod.POST ... permitAll()`. Ở đó permitAll chỉ để qua lớp kiểm tra danh tính của gateway; token nội bộ vẫn do interceptor kiểm.

### 2. order-service: đọc kết quả và giữ lượt lúc đặt hàng

DTO mới `client/dto/PromotionUsageResult.java`: `record PromotionUsageResult(Long id, Long userId, Long promotionId, Long orderId)`.
DTO mới `client/dto/ReleasePromotionUsageFeignRequest.java`: `record ReleasePromotionUsageFeignRequest(Long orderId)`.

`PromotionServiceClient.java`:

```diff
     @PostMapping("/usages")
-    ApiResponse<Void> recordUsage(@RequestBody RecordPromotionUsageFeignRequest request);
+    ApiResponse<PromotionUsageResult> recordUsage(@RequestBody RecordPromotionUsageFeignRequest request);
+
+    @PostMapping("/usages/release")
+    ApiResponse<Void> releaseUsage(@RequestBody ReleasePromotionUsageFeignRequest request);
```

Sửa ghi chú dòng 14-18 theo quy tắc mới: giữ lượt lúc đặt hàng, hoàn lượt khi hệ thống hủy.

`OrderServiceImpl.checkout`, dòng 141-145. Giữ lượt sau khi đơn có id và trước khi xóa giỏ:

```diff
-        Order saved = orderRepository.save(order);
+        Order saved = orderRepository.saveAndFlush(order);
+        if (saved.getPromotionId() != null) {
+            claimPromotion(saved);
+        }
 
         // Checkout always consumes the whole cart; clear it from Redis.
         cartService.clearCart();
```

```java
    // Claims the promotion for this order before the order commits; any refusal rolls the order back,
    // so no order keeps a discount the promotion did not grant.
    private void claimPromotion(Order order) {
        ApiResponse<PromotionUsageResult> response;
        try {
            response = promotionServiceClient.recordUsage(
                    new RecordPromotionUsageFeignRequest(order.getUserId(), order.getPromotionId(), order.getId()));
        } catch (FeignException.Conflict e) {
            throw new AppException(ErrorCode.VALIDATION_ERROR, "Promotion no longer usable: " + order.getPromotionId(), e);
        } catch (FeignException e) {
            throw new AppException(ErrorCode.INTERNAL_ERROR, "Could not claim promotion " + order.getPromotionId(), e);
        }
        if (response == null || response.data() == null || !order.getId().equals(response.data().orderId())) {
            // promotion-service hands back the existing usage when this user already redeemed the code.
            throw new AppException(ErrorCode.VALIDATION_ERROR, "Promotion already used by this user: " + order.getPromotionId());
        }
    }
```

Bỏ việc ghi lượt lúc xác nhận: xóa nhánh `recordPromotionUsageBestEffort` trong `advanceToConfirmed` (dòng 639-641), và xóa luôn hàm đó (dòng 659-672).

### 3. order-service: hoàn lượt khi hệ thống hoặc nhân viên hủy

```java
    // System (stock, payment) and staff cancellations give the promotion back; a customer's own cancel does not.
    // Runs after commit so a rolled-back cancellation never releases a claim, and a promotion-service
    // outage never blocks the cancellation (the order would then just keep the claim, as before).
    private void releasePromotionAfterCommit(Order order) {
        if (order.getPromotionId() == null) {
            return;
        }
        Runnable release = () -> {
            try {
                promotionServiceClient.releaseUsage(new ReleasePromotionUsageFeignRequest(order.getId()));
            } catch (Exception e) {
                log.error("Failed to release promotion {} for cancelled order {}", order.getPromotionId(), order.getId(), e);
            }
        };
        if (TransactionSynchronizationManager.isSynchronizationActive()) {
            TransactionSynchronizationManager.registerSynchronization(new TransactionSynchronization() {
                @Override
                public void afterCommit() {
                    release.run();
                }
            });
        } else {
            release.run();
        }
    }
```

Gọi `releasePromotionAfterCommit(...)` ngay cạnh `publishOrderCancelled(...)` ở bốn chỗ:

- `handleStockReservedFailure`, dòng 594.
- `handlePaymentCompleted`, nhánh sai số tiền, dòng 618.
- `handlePaymentFailed`, dòng 687.
- `updateStatus` khi nhân viên chuyển sang CANCELLED, dòng 537-538 (gọi với `saved`).

**Không** gọi ở `cancel` (khách tự hủy, dòng 455).

**Vì sao:**

- `saveAndFlush` để lỗi CSDL (nếu có) xảy ra trước khi gọi promotion-service, nên gần như không còn trường hợp đã trừ lượt mà đơn không được lưu.
- Khi mã hết lượt hoặc người dùng đã dùng mã, `AppException` làm rollback cả đơn và giỏ chưa bị xóa. Mã lỗi là 400 `VALIDATION_ERROR`, cùng mã `validatePromotion` (dòng 294, 300) đang dùng cho mã không hợp lệ. Storefront đã có sẵn nhánh cho đúng mã này: báo "Mã khuyến mãi không còn dùng được..." và áp lại mã (`CheckoutScreen.tsx:160-165`, bản sửa SF-08). Vì vậy không cần sửa storefront.
- Kết hợp với khóa của SF-37, một người chỉ có một checkout tại một thời điểm. Khi hai người tranh lượt cuối, `@Version` ở promotion-service đảm bảo chỉ một người thắng.
- Hoàn lượt sau commit, theo cùng cách `publishPromotionApprovedEvent` (`PromotionServiceImpl.java:352-376`) và `eventPublisher.publishAfterCommit` đang làm.

## Test

**promotion-service**

- `PromotionServiceTest`:
  - `releaseUsageByOrder_restoresQuantityAndDeletesUsage`
  - `releaseUsageByOrder_noUsage_isNoOp`
- `PromotionControllerIT`:
  - `releaseUsage_withoutInternalToken_isRejected`
  - `releaseUsage_withToken_givesTheCodeBack`: ghi lượt, hoàn lượt, rồi `GET /validate/{code}` cho cùng user trả `valid:true` và số lượng tăng lại 1.

**order-service, `OrderServiceTest`**

- `checkout_withPromotion_claimsUsageForThisOrder`: `recordUsage` được gọi một lần, với đúng `orderId` vừa lưu.
- `checkout_promotionClaimReturnsOtherOrder_throwsValidationErrorAndKeepsCart`: không gọi `clearCart`.
- `checkout_promotionExhausted_throwsValidationError`: `recordUsage` ném `FeignException.Conflict`.
- `handlePaymentFailed_withPromotion_releasesUsage`, `handleStockReservedFailure_withPromotion_releasesUsage`.
- `updateStatus_staffCancelWithPromotion_releasesUsage`.
- `cancel_withPromotion_doesNotReleaseUsage`.

Hiện `OrderServiceTest` chưa có ca nào kiểm việc ghi lượt khi xác nhận (không có `recordUsage`), nên không phải sửa test cũ.

## Kiểm thử lại

- Kịch bản 15: mã 1 lượt, 2 người đặt cùng lúc. Chỉ 1 đơn được tạo, người kia nhận 400 `VALIDATION_ERROR` và giao diện báo mã không còn dùng được.
- Kịch bản 16: một người bấm 3 lần với mã 3 lượt. Chỉ 1 đơn, số lượng mã còn 2.
- Kịch bản 17 (đặt lần lượt đơn thứ hai bằng mã đã dùng) vẫn bị chặn.
- Đơn VNPay có mã: hủy ở cổng thanh toán thì số lượng mã tăng lại và khách dùng lại được mã.
- Seller hủy một đơn có mã: số lượng mã tăng lại và khách dùng lại được mã.
- Khách tự hủy đơn COD có mã: không hoàn.
- `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `promotion-service` và `order-service`.

## Tuân thủ quy tắc

- Java 4 dấu cách, Spotless.
- promotion-service có endpoint mới, nên sinh lại contract: `./mvnw.cmd -Popenapi` để cập nhật `services/promotion-service/contract/openapi.yaml`. Không sửa tay file sinh ra.
- Không cần migration: dùng cột `order_id` đã có (`V1__init_promotion.sql:43`).

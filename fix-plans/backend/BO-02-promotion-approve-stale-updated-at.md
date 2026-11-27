# BO-02: Duyệt khuyến mãi trả updatedAt cũ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend` (`promotion-service`), đối chiếu `develop` `d5b6ac2` |
| **Nhánh đề xuất** | `fix/promotion-fresh-updated-at`, tách từ `develop` |
| **Khối lượng** | 4 dòng code, 1 test |
| **Bug và ảnh** | [Chi tiết bug](../../backoffice/loi.md#bo-02), [Ảnh 1](../../images/BO-02-1.jpg) |

## Nguyên nhân

`PromotionServiceImpl` đổi trạng thái rồi `promotionRepository.save(promotion)` và map ra response ngay, ở dòng `114` (approve), `130` (reject), `141` (pause), `152` (resume).

`updatedAt` trong `BaseEntity.java:35-37` là `@LastModifiedDate`, chỉ được ghi khi Hibernate flush. Việc flush xảy ra lúc transaction commit, tức là sau khi response đã được map. Vì vậy response luôn mang `updatedAt` cũ, còn DB thì đúng. Không riêng approve: cả 4 thao tác đều dính lỗi này.

## Thay đổi

File: `services/promotion-service/src/main/java/vn/edu/iuh/fit/taschen/promotion/service/impl/PromotionServiceImpl.java`, dòng 114, 130, 141, 152:

```diff
-        Promotion saved = promotionRepository.save(promotion);
+        Promotion saved = promotionRepository.saveAndFlush(promotion);
```

**Vì sao:** `saveAndFlush` cho auditing ghi `updatedAt` trước khi map response. Luồng ghi lượt hiện cập nhật `updatedAt` ngay trong câu lệnh giảm số lượng. Sự kiện duyệt vẫn được gửi sau commit.

**Không cần sửa:** `createPromotion`. Bản ghi mới có `createdAt` bằng `updatedAt` là đúng.

## Test

Thêm vào `PromotionControllerIT.java`: `approvePromotion_returnsUpdatedAtAfterCreatedAt`. Tạo một khuyến mãi, chờ khoảng 10 ms, duyệt, rồi kiểm tra `$.data.updatedAt` khác `$.data.createdAt`.

## Kiểm thử lại

- Duyệt, tạm dừng, tiếp tục, từ chối một khuyến mãi: `updatedAt` trong response bằng giá trị đọc lại bằng `GET /api/v1/promotions/{id}`.
- `./mvnw.cmd spotless:apply`, `./mvnw.cmd clean verify -Dapi.version=1.44` trong `promotion-service`.

## Tuân thủ quy tắc

Java 4 dấu cách, Spotless. Contract không đổi nên không cần sinh lại.

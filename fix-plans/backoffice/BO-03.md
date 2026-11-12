# BO-03: Khuyến mãi quá hạn vẫn hiện Active / Pending

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa, **cần chốt quy tắc hiển thị** |
| **Repo** | `taschen-backoffice`, số dòng theo `develop` `02da243d` |
| **Nhánh đề xuất** | `fix/promotion-expired-badge`, tách từ `develop` |
| **Khối lượng** | Khoảng 15 dòng code, 1 test, 2 khoá i18n |
| **Bug và ảnh** | [Chi tiết bug](../../backoffice/loi.md#bo-03), [Ảnh 1](../../images/BO-03-1.jpg) |

## Nguyên nhân

Backend không có trạng thái hết hạn. `PromotionStatus` chỉ gồm `PENDING`, `ACTIVE`, `PAUSED`, `REJECTED`, và không có job nào đổi trạng thái khi qua `endDate`. Mã quá hạn vẫn bị chặn đúng lúc checkout (`PromotionServiceImpl.java:290`, `PromotionRepository.java:23-25`), nên đây chỉ là vấn đề **hiển thị**.

`apps/seller/src/features/promotion/ui/promotions-config.tsx:143-163` vẽ badge thẳng từ `row.status`, nên khuyến mãi đã quá `endDate` vẫn hiện "Active" hoặc "Pending".

## Đề xuất quy tắc (cần bạn chốt)

| Trạng thái lưu | `endDate` < hôm nay | Hiển thị |
|---|---|---|
| ACTIVE, PAUSED, PENDING | Có | **Hết hạn** (badge xám) |
| REJECTED | Có hoặc không | Đã từ chối (giữ nguyên) |
| Bất kỳ | Không | Giữ nguyên |

Chỉ suy ra lúc hiển thị, không ghi gì về backend: không cần migration, không cần job định kỳ. Bộ lọc trạng thái giữ nguyên 4 giá trị của backend.

## Thay đổi

### 1. `promotions-config.tsx`, cạnh `statusVariant` (dòng 38-40)

```ts
// The service keeps no EXPIRED status; a code past its end date is shown as expired, not as its stored status.
export const isExpired = (row: Pick<Promotion, "status" | "endDate">) =>
  row.status !== "REJECTED" &&
  !!row.endDate &&
  row.endDate < new Date().toISOString().slice(0, 10);
```

### 2. `promotions-config.tsx`, `render` của cột `status` (dòng 158-162)

```diff
-      render: (row) => (
-        <Badge variant={statusVariant[row.status]}>
-          {t(`status.${row.status}`)}
-        </Badge>
-      ),
+      render: (row) =>
+        isExpired(row) ? (
+          <Badge variant="secondary">{t("status.EXPIRED")}</Badge>
+        ) : (
+          <Badge variant={statusVariant[row.status]}>
+            {t(`status.${row.status}`)}
+          </Badge>
+        ),
```

`getPromotionViewFields` dùng lại các trường của danh sách, nên panel chi tiết tự đổi theo.

### 3. i18n `apps/seller/src/messages/{vi,en}.json`

Thêm `promotion.status.EXPIRED`: "Hết hạn" / "Expired".

### 4. Việc tuỳ chọn ở backend, chỉ làm nếu bạn muốn

Hiện vẫn duyệt hoặc tiếp tục được một khuyến mãi đã quá hạn. Có thể chặn ở `approvePromotion` / `resumePromotion` bằng `CONFLICT`. Việc này tách thành plan riêng nếu chốt.

## Test

`apps/seller/src/features/promotion/__tests__/` (hoặc cạnh `books-config.test.ts`): `isExpired` cho 4 trường hợp: ACTIVE quá hạn → true, REJECTED quá hạn → false, ACTIVE còn hạn → false, `endDate` rỗng → false.

## Kiểm thử lại

- Danh sách khuyến mãi ở seller: các mã có `endDate` 2026-09-21 hiện "Hết hạn". `MINORDER1110` (hạn 2026-11-30) vẫn hiện "Active".
- `pnpm lint`, `pnpm typecheck`, `pnpm test`.

## Tuân thủ quy tắc

Biome; badge dùng variant có sẵn của VUI, không thêm màu mới.

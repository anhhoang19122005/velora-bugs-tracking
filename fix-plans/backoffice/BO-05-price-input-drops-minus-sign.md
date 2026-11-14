# BO-05: Ô giá tự bỏ dấu trừ, lưu -1 thành 1

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã chấp nhận, không sửa (người dùng xác nhận ngày 2026-11-12). Giữ lại để tham khảo nếu sau này đổi ý.
| **Repo** | `taschen-backoffice`, số dòng theo `develop` `02da243d` |
| **Nhánh đề xuất** | `fix/money-input-negative`, tách từ `develop` |
| **Khối lượng** | Khoảng 10 dòng code, cập nhật 2 file test |
| **Bug và ảnh** | [Chi tiết bug](../../backoffice/loi.md#bo-05), [Ảnh 1](../../images/BO-05-1.jpg) |
| **Test case** | [HD Tạo sách](../../backoffice/hd-tao-sach.md) TC12, [HD Đơn mua](../../backoffice/hd-don-mua.md) TC10 |

## Nguyên nhân

`packages/core/src/lib/money.ts:41-46` `parseVND` giữ lại **chỉ chữ số** (`/\D/g`), nên "-1" thành 1. `packages/ui/src/money-input.tsx:66-69` đưa mọi thứ gõ vào qua hàm đó. Vì vậy giá âm âm thầm thành giá dương, không có lỗi nào để form hay backend bắt.

`MoneyInput` được dùng ở 6 nơi: `variant-prices.tsx` (giá theo định dạng khi tạo sách), `stock-lines-input.tsx` (giá nhập trong đơn mua), `order-from-request-fields.tsx`, `batches-config.tsx`, `book-variants-config.tsx`, `promotions-config.tsx`.

## Thay đổi

### 1. `packages/core/src/lib/money.ts:41-46`: giữ dấu trừ ở đầu

```diff
 export function parseVND(typed: string): number | null {
   const digits = typed.replace(/\D/g, "");
   if (!digits) return null;
-  const value = Number(digits);
+  // A leading minus is kept so a negative amount reaches validation instead of becoming positive.
+  const value = typed.trim().startsWith("-") ? -Number(digits) : Number(digits);
   return Number.isFinite(value) ? value : null;
 }
```

`groupDigits` dùng `Intl.NumberFormat`, nên số âm tự hiện thành "-1".

### 2. `packages/ui/src/money-input.tsx`: tự báo đỏ khi âm

`aria-invalid={invalid || (amount != null && amount < 0) || undefined}`. Còn chặn Lưu là việc của form.

### 3. Chặn Lưu: hai form trong bug đã có sẵn quy tắc, chỉ thiếu dấu trừ

Hai form trong bug tự chặn được khi bước 1 xong, vì quy tắc giá âm đã có:

| Form | Quy tắc có sẵn |
|---|---|
| Tạo sách | `books-config.tsx:341`: `validate` của `variantPrices` có `Number(r.price) < 0` |
| Đơn mua | `packages/ui/src/stock-lines.ts:60-61`: `isMoney` có `Number(v) >= 0`, được `stockLinesProblem` dùng |

Những nơi `MoneyInput` là một trường riêng thì cần thêm một quy tắc `< 0`:

| Nơi | Cách chặn |
|---|---|
| `batches-config.tsx`, `book-variants-config.tsx`, `order-from-request-fields.tsx` | `validate: (v) => (v !== "" && Number(v) < 0 ? <thông báo> : undefined)`; kiểm tra từng chỗ khi sửa vì có thể đã có |
| `promotions-config.tsx` `priceOrderActive` | Thêm `validate` < 0 ở đây (BO-04 đã sửa phần thông báo, chưa đụng ô tiền) |

Schema BFF: `book.schema.ts:12` và `book-variant.schema.ts:11,18` đã có `nonnegative`. `apps/warehouse/src/validation/inventory/purchase-order.schema.ts:12` (`createPurchaseOrderSchema`) còn `importPrice: z.number()`, cần thêm `.min(0)` giống `createPurchaseOrderFromStockRequestSchema` ở dòng 28.

## Test

- `packages/core/src/lib/money.test.ts`: `parseVND("-1") === -1`, `parseVND("-15.000") === -15000`, `parseVND("1-") === 1`.
- `packages/ui/src/stock-lines` (test có sẵn hoặc thêm): `stockLinesProblem` với `importPrice` "-1" trả `priceNeeded`.

## Kiểm thử lại

- TC12 tạo sách với giá -1: ô hiện "-1" viền đỏ, không lưu được, báo giá không được âm.
- TC10 đơn mua với giá nhập -1: như trên.
- Ô tiền vẫn nhóm "15.000" khi gõ số dương.
- `pnpm lint`, `pnpm typecheck`, `pnpm test`.

## Tuân thủ quy tắc

Biome. Sửa một lần ở `parseVND` dùng chung thay vì từng form.

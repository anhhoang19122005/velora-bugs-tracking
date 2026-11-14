# SF-15: Bấm "Huỷ đơn" là huỷ ngay, không hỏi lại

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | **Đã sửa** trên `fix/storefront-bugs` (merge `be16d74`), commit `62d90a1`. Đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11 |
| **Repo** | `taschen-storefront`, số dòng theo commit `ebfeecd` |
| **Nhánh** | `fix/sf-15-order-cancel-confirm` |
| **Khối lượng** | Khoảng 18 dòng code, 1 test |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-15), [Ảnh 1](../../images/SF-15-1.jpg) |

## Nguyên nhân

Nút "Huỷ đơn" tại `orders/[number]/page.tsx:182` gọi thẳng `onCancel`, là `cancel.mutate()` ở dòng 111. Huỷ đơn không hoàn tác được, nên một lần bấm nhầm là mất đơn.

## Thay đổi

File: `src/app/[locale]/(main)/orders/[number]/page.tsx`

### 1. Dòng 9, thêm import

```diff
 import { Button, buttonVariants } from "@viliha/vui-react/button";
+import { ConfirmDialog } from "@viliha/vui-react/confirm-dialog";
 import { EmptyState } from "@viliha/vui-react/empty-state";
```

**Vì sao:** `ConfirmDialog` có sẵn trong VUI (`src/vendor/vui/components/confirm-dialog.tsx`), đã xử lý Escape, bấm nền và focus.

### 2. Dòng 131, thêm state trong `OrderDetail`

```diff
 }) {
+  const [confirmingCancel, setConfirmingCancel] = React.useState(false);
   const subtotal = order.lines.reduce((sum, line) => sum + line.lineTotal, 0);
```

### 3. Dòng 181-185

```diff
           {canCancel ? (
-            <Button variant="outline" disabled={busy} onClick={onCancel}>
-              Huỷ đơn
-            </Button>
+            <>
+              <Button
+                variant="outline"
+                disabled={busy}
+                onClick={() => setConfirmingCancel(true)}
+              >
+                Huỷ đơn
+              </Button>
+              <ConfirmDialog
+                open={confirmingCancel}
+                title="Huỷ đơn hàng này?"
+                description="Đơn đã huỷ không thể khôi phục."
+                confirmLabel="Huỷ đơn"
+                cancelLabel="Giữ đơn"
+                destructive
+                onConfirm={() => {
+                  setConfirmingCancel(false);
+                  onCancel();
+                }}
+                onCancel={() => setConfirmingCancel(false)}
+              />
+            </>
           ) : null}
```

**Vì sao đặt state trong `OrderDetail`:** chỉ nút này cần đến nó. `cancel` mutation ở dòng 66-73 và các thông báo giữ nguyên. Hộp thoại đóng lại trước khi gọi API, nút vẫn bị khoá nhờ `busy`, nên không thể gửi hai lần.

## Test

Thêm vào test "login, server cart, checkout and order detail use real request shapes" trong `e2e/api/storefront.spec.ts`, sau dòng 265. Test này kết thúc ở trang chi tiết của một đơn `PENDING`, nên nút "Huỷ đơn" có sẵn:

```ts
  // Cancelling asks first, and backing out keeps the order.
  await page.getByRole("button", { name: "Huỷ đơn", exact: true }).click();
  const dialog = page.getByRole("dialog");
  await dialog.getByRole("button", { name: "Giữ đơn", exact: true }).click();
  await expect(dialog).toBeHidden();
  expect(calls.some((call) => call.method === "PATCH")).toBe(false);
```

**Vì sao không thêm vào `e2e/orders.spec.ts`:** file đó viết cho bản prototype (mã đơn dạng `ODH012344`), còn trang chi tiết đơn hiện chỉ nhận id số và gọi API thật, nên test ở đó không chạy được với trang hiện tại.

`Dialog` trả về `null` khi đóng (`dialog.tsx:107`), nên lúc chưa bấm chỉ có một nút "Huỷ đơn" trên trang.

## File mới

Không có.

## Kiểm thử lại

- Bấm "Huỷ đơn": hiện hộp thoại, chưa có request nào.
- "Giữ đơn" và Escape: đơn không đổi.
- Xác nhận huỷ: đơn chuyển trạng thái, có thông báo.
- Chạy lại luồng 5. `pnpm lint`, `pnpm typecheck`, `pnpm test:e2e e2e/api`.

## Tuân thủ quy tắc

TypeScript 2 dấu cách, ESLint, tái sử dụng component có sẵn. API không đổi nên không cần sinh lại contract.

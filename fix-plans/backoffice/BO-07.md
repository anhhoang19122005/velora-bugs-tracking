# BO-07: Dòng hàng của đơn mua phải cuộn ngang ở 1024px

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice`, số dòng theo `develop` `02da243d` |
| **Nhánh đề xuất** | `fix/stock-lines-wrap`, tách từ `develop` |
| **Khối lượng** | Khoảng 4 dòng class, kiểm tra trên trình duyệt |
| **Bug và ảnh** | [Chi tiết bug](../../backoffice/loi.md#bo-07), [Ảnh 1](../../images/BO-07-1.jpg) |

## Nguyên nhân

`packages/ui/src/stock-lines-input.tsx:134` vẽ mỗi dòng hàng là một hàng flex không xuống dòng (`flex w-full items-center gap-2`). Các ô bên cạnh có độ rộng cố định:

| Ô | Dòng | Độ rộng |
|---|---|---|
| Format | 183 | `w-44 shrink-0` (176px) |
| Số lượng | 202 | `w-28` |
| Giá nhập | 222 | `w-32` |
| Nút xoá | — | cố định |

Riêng ô Book ở dòng 160 là `min-w-0 flex-1`, nên nó chịu mất chỗ. Ở 1024px, cột nhập liệu của form (sau sidebar và cột nhãn 11rem) không đủ chỗ cho khoảng 500px cố định, nên ô Book co lại hoặc bị đẩy khỏi tầm nhìn.

Component dùng chung cho đơn mua, phiếu nhập kho và yêu cầu kho, nên sửa một chỗ là đủ.

## Thay đổi

Cho dòng tự xuống hàng theo **độ rộng của chính field** (container query của Tailwind v4, `apps/seller/package.json` đang là `^4.3.0`), không phải theo màn hình:

```diff
-    <div ref={rootRef} className="flex w-full flex-col gap-2" ...>
+    <div ref={rootRef} className="@container flex w-full flex-col gap-2" ...>
-        <div key={index} className="flex w-full items-center gap-2">
+        <div key={index} className="flex w-full flex-wrap items-center gap-2 @2xl:flex-nowrap">
-            className="min-w-0 flex-1"            // RecordPicker (Book)
+            className="min-w-0 basis-full @2xl:basis-0 @2xl:flex-1"
```

- **Field hẹp** (dưới `@2xl`, 42rem): ô Book chiếm cả hàng đầu; Format, Số lượng, Giá, Xoá xuống hàng thứ hai.
- **Field rộng** (1600px): giữ nguyên một hàng như hiện tại.

**Cần kiểm tra khi sửa:** `alignTo=".vui-picker-anchor"` của picker vẫn canh panel đúng bằng ô Book khi ô này chiếm cả hàng. Nút "Thêm dòng" (`SectionAction`) vẫn đúng vị trí.

## Test

Thay đổi chỉ là layout, nên kiểm tra trên trình duyệt ở 1024px, 1280px và 1600px. Ghi ảnh trước và sau vào PR.

## Kiểm thử lại

- Form đơn mua ở 1024px: không còn cuộn ngang, chọn được Book và Format không nhầm.
- Phiếu nhập kho và yêu cầu kho (cùng component) hiển thị đúng ở 1024px.
- `pnpm lint`, `pnpm typecheck`.

## Tuân thủ quy tắc

Biome; chỉ dùng utility của Tailwind, không giá trị tuỳ ý, không sửa theme.

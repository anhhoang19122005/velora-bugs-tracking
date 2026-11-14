# SF-19: Nội dung checkout sát mép màn hình

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `093e1bd` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `093e1bd` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-19), [Ảnh 1](../../images/SF-19-1.webp) |

## Nguyên nhân

`checkout/page.tsx` render trực tiếp `CheckoutScreen`, thiếu container bao ngoài.

## Thay đổi đã có

- Bọc `CheckoutScreen` trong `div` có `vui-container py-8` tại `checkout/page.tsx`.
- Đổi wrapper lời nhắc đăng nhập trong `CheckoutScreen.tsx` sang `py-4` để tránh container lồng nhau.

## Bằng chứng

Ảnh người dùng cung cấp; đã kiểm tra nội dung ảnh.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: tại viewport 1280px, kiểm tra mép trái liên kết “Quay lại giỏ” lớn hơn 16px.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Checkout ở desktop và điện thoại có khoảng cách hai bên hợp lý.
- Kiểm tra cả khách chưa đăng nhập và tài khoản đã có giỏ hàng.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

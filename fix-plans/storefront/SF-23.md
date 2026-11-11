# SF-23: Breadcrumb chồng chữ trên điện thoại

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-23), [Ảnh 1](../../images/SF-23-1.jpg) |

## Nguyên nhân

Breadcrumb của VUI giữ các mục trên cùng một hàng, thiếu wrap cho tên dài.

## Thay đổi đã có

- Trong `src/app/globals.css`, thêm `.vui-breadcrumbs-nav { flex-wrap: wrap; }` trong `@layer components`.
- Dùng CSS chung cho các breadcrumb, không sửa mã vendor.

## Bằng chứng

Ảnh minh họa chi tiết sách Tư Duy Python ở viewport điện thoại.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: mock tên sách/danh mục dài ở 375px, kiểm tra hình chữ nhật của các mục breadcrumb không giao chồng.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Chi tiết sách có tên dài ở 375px: không chồng chữ.
- Kiểm tra breadcrumb ở danh mục, giỏ, đơn hàng trên mobile và desktop vì CSS áp dụng chung.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

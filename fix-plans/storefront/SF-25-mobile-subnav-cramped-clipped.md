# SF-25: Menu phụ điện thoại bị chật và cắt chữ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-25), [Ảnh 1](../../images/SF-25-1.jpg) |

## Nguyên nhân

Padding, khoảng cách và font của hàng điều hướng chiếm quá nhiều chỗ; vùng danh mục có thể co lại.

## Thay đổi đã có

- Trong `Header/index.tsx`, giảm gap và cỡ chữ trên mobile, phục hồi kích thước ở breakpoint `sm`.
- Cho liên kết danh mục `shrink-0 whitespace-nowrap`; nav dùng `min-w-0 overflow-x-auto`, giảm khoảng cách icon và chữ.

## Bằng chứng

Ảnh SF-25-1.jpg; triệu chứng cũng đã được ghi chú trong luồng giao diện điện thoại của đợt 10/11.

## Kiểm thử trong commit

Chưa có assertion riêng cho độ chật của menu trong commit. `e2e/responsive.spec.ts` có kiểm tra trang không cuộn ngang; cần kiểm tra trực quan và cuộn bên trong nav.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Ở 375px, 390px, 413px: tên danh mục liền dòng; cuộn để bấm được liên kết cuối.
- Desktop giữ khoảng cách và cỡ chữ theo breakpoint cũ.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

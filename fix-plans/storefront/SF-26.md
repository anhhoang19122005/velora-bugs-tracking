# SF-26: Đường dẫn không tồn tại hiển thị trang 404 mặc định

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-26), [Ảnh 1](../../images/SF-26-1.jpg) |

## Nguyên nhân

Đường dẫn không khớp route chưa đi vào nhóm `(main)`, nên không dùng trang not-found của nhóm.

## Thay đổi đã có

- Thêm `(main)/[...rest]/page.tsx` gọi `notFound()` và khai báo metadata.
- Thêm `(main)/not-found.tsx` tái xuất trang not-found theo locale đang có.

## Bằng chứng

Ảnh 320×240 hiển thị “404 / This page could not be found.”; ảnh không chứa URL, đường dẫn tái hiện dựa trên test trong commit.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: mở /vi/khong-co-trang-nay, xác nhận thông báo 404 tiếng Việt, header VELORA và title riêng.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- URL không tồn tại dưới /vi hiển thị 404 của cửa hàng và liên kết điều hướng dùng được.
- Kiểm tra route hợp lệ, chi tiết sách và locale khác không bị catch-all bắt nhầm.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

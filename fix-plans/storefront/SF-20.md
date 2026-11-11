# SF-20: Khung thông báo bị cắt ở điện thoại

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `0e497d7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `0e497d7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-20), [Ảnh 1](../../images/SF-20-1.png) |

## Nguyên nhân

Panel rộng cố định 360px (thông báo) hoặc 340px (tài khoản), neo vào biểu tượng sát bên phải.

## Thay đổi đã có

- Trong `Header/NotificationsMenu.tsx` và `Header/AccountMenu.tsx`, dùng `max-sm:fixed max-sm:inset-x-4 max-sm:top-[76px] max-sm:w-auto`.
- Giữ cách neo panel hiện có trên màn hình lớn; cập nhật locator test theo DOM thật.

## Bằng chứng

Ảnh người dùng cung cấp; đã kiểm tra nội dung ảnh. Ảnh minh họa thông báo; phạm vi sửa còn bao gồm khung tài khoản.

## Kiểm thử trong commit

`e2e/responsive.spec.ts`: kiểm tra panel thông báo có mép trái >= 0, mép phải <= 390 và trang không cuộn ngang. Commit `b771af7` cập nhật tiếp locator cho lời nhắc đăng nhập.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Mở/đóng thông báo và tài khoản ở 375px, 390px và desktop.
- Kiểm tra khách và tài khoản đã đăng nhập; các nút trong panel bấm được.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

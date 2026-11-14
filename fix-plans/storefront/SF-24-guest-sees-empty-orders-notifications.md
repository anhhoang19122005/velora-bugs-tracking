# SF-24: Khách chưa đăng nhập thấy trạng thái rỗng của đơn hàng và thông báo

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-24), [Ảnh 1](../../images/SF-24-1.jpg), [Ảnh 2](../../images/SF-24-2.jpg) |

## Nguyên nhân

Trang đơn và panel thông báo dùng trạng thái rỗng mà không phân biệt có tài khoản đăng nhập hay không.

## Thay đổi đã có

- Trong `orders/page.tsx`, dùng `useAuth`: chờ tải bằng Skeleton, chỉ render `History` khi có user, còn khách thấy EmptyState và nút đăng nhập.
- Trong `Header/NotificationsMenu.tsx`, khách thấy lời nhắc đăng nhập; chỉ bật query danh sách khi mở panel và có user, ẩn thao tác dành cho tài khoản.

## Bằng chứng

Hai ảnh từ phiên khách theo bàn giao; ảnh riêng lẻ không tự chứng minh trạng thái phiên. Diff xác nhận nhánh giao diện trước đây thiếu phân biệt khách.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: mock API 401, kiểm tra lời nhắc đăng nhập ở đơn hàng và không còn thông báo chưa có đơn. `e2e/responsive.spec.ts` dùng lời nhắc đăng nhập ở thông báo để định vị panel.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Khách thấy lời nhắc ở cả hai nơi, nút dẫn đến trang đăng nhập.
- Tài khoản có/không có dữ liệu vẫn thấy đúng danh sách hoặc trạng thái rỗng; lúc tải không lóe lịch sử trống.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

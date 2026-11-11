# SF-22: Chip lọc trạng thái đơn hàng hiển thị tiếng Anh

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-22), [Ảnh 1](../../images/SF-22-1.jpg) |

## Nguyên nhân

`StatusFilter` in trực tiếp giá trị enum thay vì nhãn dịch.

## Thay đổi đã có

- Thêm prop `labelOf` cho `StatusFilter` trong `orders/_components/History.tsx`.
- Dùng `useTranslations("orders")` cho trạng thái đơn và `RETURN_STATUS_LABELS` cho đổi/trả; dịch cả câu trạng thái rỗng.

## Bằng chứng

Ảnh minh họa tab Đơn hàng; diff xác nhận sửa cả bộ lọc đổi/trả.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: mock tài khoản đã đăng nhập, xác nhận có “Chờ xác nhận” và không có “PENDING” trong bộ lọc đơn.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Xem từng chip ở hai tab, chọn trạng thái và kiểm tra query URL không đổi định dạng.
- Trạng thái rỗng dùng nhãn dễ hiểu; kiểm tra locale tiếng Anh cho bộ lọc đơn.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

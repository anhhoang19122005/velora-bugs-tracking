# SF-27: Nhiều trang dùng chung tiêu đề tab

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `b771af7` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-27) |

## Nguyên nhân

Các trang client kế thừa metadata mặc định từ layout locale, chưa có server layout khai báo title riêng.

## Thay đổi đã có

- Thêm `layout.tsx` cho `(auth)/login`, `(auth)/register`, `(main)/cart`, `(main)/orders`, `(main)/search`; mỗi layout trả nguyên children.
- Khai báo lần lượt “Đăng nhập”, “Đăng ký”, “Giỏ hàng”, “Đơn hàng”, “Tìm kiếm” kèm ` | Velora`.

## Bằng chứng

Không có ảnh và chưa lưu kết quả page.title(). Bằng chứng nguồn: layout locale đặt title chung; commit b771af7 bổ sung 5 layout metadata. Test đơn hàng có assertion toHaveTitle("Đơn hàng | Velora"); chưa chạy lại trong đợt ghi nhận này.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: test khách xem đơn hàng có `toHaveTitle("Đơn hàng | Velora")`. Chưa có assertion riêng cho cả 5 trang trong commit.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Dùng page.title() ghi lại tiêu đề trên cả 5 URL, đối chiếu metadata từng layout.
- Kiểm tra tiêu đề chi tiết đơn và trang con để phát hiện kế thừa ngoài ý muốn.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

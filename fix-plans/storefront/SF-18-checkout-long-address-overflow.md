# SF-18: Địa chỉ dài tràn màn hình checkout

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `494e90b` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `494e90b` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-18), [Ảnh 1](../../images/SF-18-1.png) |

## Nguyên nhân

Các vùng hiển thị địa chỉ không cho phép ngắt chuỗi dài không có dấu cách.

## Thay đổi đã có

- Thêm `[overflow-wrap:anywhere]` vào `Choice` của `CheckoutScreen.tsx` và địa chỉ giao trong `orders/[number]/page.tsx`.
- Áp dụng cùng cách ngắt dòng cho `ModalSelectAddress`, `AddressCard` và `AddressStats`, giữ nguyên dữ liệu địa chỉ.

## Bằng chứng

Ảnh dựng lại lỗi trên code trước bản sửa theo bàn giao; đã kiểm tra nội dung ảnh. Không phải ảnh chụp bản hiện tại.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: fixture địa chỉ 500 ký tự; assertion chiều rộng phần tử và trang không vượt viewport 390px.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Checkout với địa chỉ dài có/không có dấu cách ở 390px: xuống dòng, không cuộn ngang.
- Kiểm tra lại modal chọn địa chỉ, sổ địa chỉ và chi tiết đơn; địa chỉ thường vẫn dễ đọc.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

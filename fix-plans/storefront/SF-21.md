# SF-21: Nút yêu thích và thêm giỏ không hiện trên cảm ứng

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `ee742a1` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. |
| **Repo** | `taschen-storefront` |
| **Nhánh / commit** | `fix/storefront-bugs` / `ee742a1` |
| **Bug và ảnh** | [Chi tiết bug](../../storefront/loi.md#sf-21), [Ảnh 1](../../images/SF-21-1.jpg) |

## Nguyên nhân

Lớp nút trên bìa sách chỉ chuyển từ `opacity-0` sang hiện khi `group-hover`.

## Thay đổi đã có

- Trong `BookCard/index.tsx`, thêm `group-focus-within:opacity-100`, `max-md:opacity-100` và `[@media(hover:none)]:opacity-100`.
- Giữ hiệu ứng hover trên desktop; cập nhật chú thích mô tả hành vi.

## Bằng chứng

Ảnh cho thấy thẻ sách không có nút thao tác; nguyên nhân được đối chiếu trong diff commit.

## Kiểm thử trong commit

`e2e/api/storefront.spec.ts`: kiểm tra opacity của nhóm nút là 1 ở 390px và 0 ở 1280px khi chưa hover. Test này kiểm tra theo viewport, chưa chứng minh trên thiết bị cảm ứng thật.

Đã đọc diff và test; chưa chạy lại test hoặc xác nhận trên môi trường triển khai trong lần cập nhật tài liệu này.

## Kiểm thử lại

- Ở điện thoại, nút luôn hiện và bấm được; Tab bàn phím làm hiện nhóm nút.
- Ở desktop có chuột, hover vẫn hiện nút; kiểm tra thêm giỏ và yêu thích theo trạng thái đăng nhập.

Chạy kiểm tra phù hợp trong repo storefront: `pnpm lint`, `pnpm typecheck`, rồi các test liên quan ở `e2e/api/storefront.spec.ts` hoặc `e2e/responsive.spec.ts` với cấu hình môi trường tương ứng.

## Phạm vi

Bản sửa giao diện, không đổi API nên không cần sinh lại contract. Bản cập nhật repo bug này chỉ ghi tài liệu và thêm ảnh đã có.

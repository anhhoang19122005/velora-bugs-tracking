# UI-02: Header tràn ngang và cắt nút Tài khoản ở 320 px

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Tái hiện ngày 2026-11-27 trên Chromium local. |
| **Repo** | `taschen-storefront` |
| **Bug** | [Chi tiết và bằng chứng](../../ui/loi.md#ui-02) |
| **Điểm vào source** | `src/app/[locale]/(main)/_components/Header/index.tsx` và `Header/Actions` |

## Nguyên nhân

Logo và cụm thao tác đều dùng shrink-0. Tổng chiều rộng cùng khoảng cách và lề vượt 320 px.

## Thay đổi

Giảm khoảng cách giữa hai cụm ở màn hẹp và giữ kích thước vùng bấm. Nếu chiều rộng vẫn thiếu khi có badge dài, cho nhóm điều hướng tự xuống hàng theo bố cục hiện có.

## Code dự kiến

```diff
- <div className="vui-container flex h-[76px] items-center gap-4 sm:gap-6">
+ <div className="vui-container flex h-[76px] items-center gap-2 sm:gap-6">
```

## Kiểm thử lại

1. Mở tìm kiếm, giỏ hàng hoặc đăng nhập ở 320 px và quan sát hàng chứa logo, thông báo, yêu thích, giỏ và tài khoản.
2. Tất cả nút nằm trong viewport và mở được bằng chuột, cảm ứng hoặc bàn phím.
3. Đo scrollWidth ở 320 và 375 px, gồm cả trạng thái giỏ hoặc thông báo có badge.

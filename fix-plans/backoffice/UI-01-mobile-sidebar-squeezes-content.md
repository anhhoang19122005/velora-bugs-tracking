# UI-01: Sidebar chiếm chỗ nội dung ở 375 px

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Tái hiện ngày 2026-11-27 trên Chromium local. |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết và bằng chứng](../../ui/loi.md#ui-01) |
| **Điểm vào source** | `packages/vui/src/design-core.ts`, shell Backoffice dùng chung |

## Nguyên nhân

Shell dùng chiều rộng sidebar 290 px ở màn hẹp. Vùng làm việc còn quá ít để hiển thị toolbar và bảng.

## Thay đổi

Dùng breakpoint sẵn có ở shell để sidebar mở đè ở màn hẹp. Dùng lại trạng thái điều hướng hiện tại và cho vùng chính chiếm toàn bộ chiều rộng khi drawer đóng. Kiểm nút mở, Escape và trả focus về nút mở.

## Code dự kiến

Minh họa bố cục của drawer. Dùng class hoặc component shell đang có khi triển khai.

```css
/* Áp dụng trong shell chung tại breakpoint hẹp đang dùng. */
.shell-main { min-width: 0; width: 100%; }
.shell-mobile-navigation {
  position: fixed;
  inset-block: 0;
  inset-inline-start: 0;
  max-width: calc(100vw - 3rem);
}
```

## Kiểm thử lại

1. Mở lần lượt Admin Users, Seller Orders và Warehouse Suppliers trực tiếp ở 375 px với sidebar ở trạng thái mặc định.
2. Điều hướng, bảng và thao tác chính dùng được ở 375 px. Sidebar desktop vẫn mở và thu gọn được.
3. Chạy với cả ba vai trò ở 375, 768 và 1440 px, kiểm mở/đóng sidebar và focus.

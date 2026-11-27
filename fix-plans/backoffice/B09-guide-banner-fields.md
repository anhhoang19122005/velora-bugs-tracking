# B09: Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết B09](../../test-2026-11-27/loi.md#b09) · GM04-02 |
| **Điểm vào source** | `Guide me banner`, `banner.schema.ts` |

## Nguyên nhân

Guide đang mô tả nút và trường ngoài form. Người dùng làm theo sẽ không tìm được bước tương ứng.

## Thay đổi

1. Đối chiếu cấu hình task, mô tả dùng chung, quyền và form hiện hành. Cập nhật thứ tự tới đúng màn và hai trường Tên, URL ảnh.

## Code dự kiến

Trong apps/seller/src/messages/vi.json, các khóa banner-create.summary và steps.save.instruction. Sửa bản en tương ứng. Task đang có bước Tên, Ảnh và Lưu.

```diff
- "summary": "Ảnh lớn trên trang chủ. Dẫn khách tới nơi bạn muốn họ xem.",
+ "summary": "Thêm ảnh lớn hiển thị trên trang chủ.",

- "instruction": "Bấm Lưu. Banner tắt vẫn lưu được — bật lên khi ảnh và đường dẫn đã đúng."
+ "instruction": "Kiểm tra tên và URL ảnh, rồi bấm Lưu."
```

## Kiểm thử lại

Chạy từng bước Guide me trên màn banner, khớp trường Tên và URL ảnh cùng vai trò có quyền tạo.

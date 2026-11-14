# BO-06: Form sách và đơn mua không chỉ ra trường quá dài

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên nhánh local, đã kiểm thử form sách trên trình duyệt; **chưa commit, chưa merge** |
| **Repo có bản sửa** | `taschen-backoffice` (backend không đổi) |
| **Nhánh thực hiện** | `fix/bo-04-06-clear-error-messages`, tách từ `develop` `02da243d` (chung với [BO-04](BO-04-promotion-form-generic-error-data-lost.md)) |
| **Bug và ảnh trước sửa** | [Chi tiết bug](../../backoffice/loi.md#bo-06), [Ảnh 1](../../images/BO-06-1.jpg) |
| **Test case** | [HD Tạo sách](../../backoffice/hd-tao-sach.md) TC10, TC11; [HD Đơn mua](../../backoffice/hd-don-mua.md) TC11 |

## Nguyên nhân trước khi sửa

- Các trường `title`, `author`, `description`, `imageUrl` của form sách và `note` của form đơn mua không có giới hạn độ dài, nên form gửi lên và backend trả 400.
- BFF bỏ mất `fieldErrors` của backend (xem [BO-04](BO-04-promotion-form-generic-error-data-lost.md)), nên toast chỉ có câu chung "The request contains invalid data.".

## Thay đổi đã có

| Thành phần | Thay đổi |
|---|---|
| `apps/seller/src/features/book/ui/books-config.tsx` | `max` khớp `CreateBookRequest`: tên 255, tác giả 100, mô tả 2000, URL ảnh 1000. Form sửa sách dùng chung các trường này. |
| `apps/warehouse/src/features/purchase-order/ui/purchase-orders-config.tsx` | `note` tối đa 1000 ký tự, khớp `CreatePurchaseOrderRequest`. |
| `packages/core/src/api/bff.ts`, `fail.ts` | Chung với BO-04: lỗi chỉ backend mới biết vẫn nêu đúng trường trong toast (dòng phụ có sẵn của `useListMutation` và trang tạo sách). |

Lỗi độ dài được VUI báo tại chính ô nhập (viền đỏ, icon, tooltip), đúng cách các form khác của backoffice đang báo lỗi.

**Không làm so với kế hoạch ban đầu:** không thêm giới hạn vào schema zod ở BFF, cùng lý do như BO-04.

## Kiểm thử đã chạy (2026-11-12)

Trình duyệt, app seller `localhost:3002` với backend local, tài khoản `seller@taschen.test`:

| Case | Kết quả |
|---|---|
| TC10 (tên 266 ký tự) + TC11 (tác giả 101 ký tự), form tạo sách | Không gửi request. Báo tại từng ô: "Title must be at most 255 characters", "Author must be at most 100 characters". |

Test tự động: `books-config.test.ts` kiểm tra đủ 4 giới hạn (đúng bằng giới hạn thì qua, dư 1 ký tự thì bị chặn). Toàn bộ test backoffice pass.

## Kiểm thử lại còn lại

- TC11 đơn mua (ghi chú 1001 ký tự) chưa chạy trên trình duyệt vì app warehouse chưa bật; cơ chế giống form sách.

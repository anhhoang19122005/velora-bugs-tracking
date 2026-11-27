# BO-12: Điều hướng Admin mất tiền tố /admin và mất phiên

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã merge, chưa kiểm thử lại |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết BO-12](../../backoffice/loi.md#bo-12) |
| **Điểm vào source** | Admin `proxy.ts`, PR #369 (`fe73d47f`) |

## Nguyên nhân

Điều hướng có thể đưa người đang ở console Admin sang đường dẫn của console thường, nơi phiên Admin không áp dụng.

## Thay đổi đã thực hiện

Proxy chuyển các đường dẫn console tương ứng về dưới `/admin/<console>/…` theo logic đã merge.

## Kiểm thử lại

1. Trên môi trường triển khai, mở trực tiếp danh sách và chi tiết đơn mua từ console Admin, rồi chạy lại bằng điều hướng nội bộ và tải lại trang.
2. Kiểm URL giữ tiền tố `/admin`, phiên vẫn hợp lệ và quyền admin/seller/warehouse vẫn được áp dụng theo từng console.

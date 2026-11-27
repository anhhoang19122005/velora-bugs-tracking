# SF-30: Đăng nhập sai nhiều lần không bị giới hạn

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã merge, chưa kiểm thử lại |
| **Repo** | `taschen-backend` (Gateway) |
| **Bug** | [Chi tiết SF-30](../../storefront/loi.md#sf-30) |
| **Điểm vào source** | Gateway, PR #140 (`e06e334`) |

## Nguyên nhân

Gateway trước đó cho các lần đăng nhập sai đi qua liên tiếp.

## Thay đổi đã thực hiện

Gateway giới hạn theo IP và email qua Redis. Khi Redis lỗi, request vẫn được chuyển tiếp theo chính sách hiện tại.

## Kiểm thử lại

1. Với Redis hoạt động, chạy bộ test đăng nhập theo ngưỡng đã cấu hình. Kiểm response khi vượt ngưỡng, đăng nhập hợp lệ sau khi cửa sổ chờ hết và kiểm hai email/IP độc lập theo contract.
2. Thử cấu hình Redis lỗi trong môi trường test và đối chiếu hành vi tiếp tục phục vụ với log Gateway.

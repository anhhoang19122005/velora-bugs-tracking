# Báo cáo bug Velora

Chuyển từ `manual-2026-11-10-v2.xlsx`, mỗi sheet là một file Markdown. Toàn bộ ảnh bằng chứng nằm trong [images](images/) và được bug liên kết tới.

- **Bug:** 34, gồm 16 đang mở, 17 đã sửa và đã vào `origin/develop` qua PR #77 (merge `b3444b9`), 1 đã đóng (SF-16)
- **Ảnh:** 37 (SF-27 chưa có ảnh; dùng bằng chứng nguồn, chưa có kết quả đo tiêu đề được lưu)
- **Kế hoạch sửa:** [fix-plans](fix-plans/), 27 file cho SF-01–SF-27, chia theo repo cần sửa; BO-01–BO-07 chưa có kế hoạch riêng

Bổ sung ngày 2026-11-11: SF-18–SF-27 là 10 bug giao diện Minor. Đã đối chiếu ảnh và commit sửa; chưa chạy kiểm thử lại. Trạng thái đã vào `origin/develop` được xác nhận bằng Git sau khi fetch. [Tổng kết](tong-ket.md) giữ nguyên kết quả đợt test 2026-11-10, chưa bao gồm 10 bug mới. SF-27 tiếp nối phần tiêu đề riêng từng trang từng được để tùy chọn ở SF-14.

| Sheet | Bên | File |
|---|---|---|
| Tổng kết | Chung | [tong-ket.md](tong-ket.md) |
| Storefront-Luồng | Storefront | [storefront/luong.md](storefront/luong.md) |
| Storefront-Lỗi | Storefront | [storefront/loi.md](storefront/loi.md) |
| Storefront-HD-Đăng nhập | Storefront | [storefront/hd-dang-nhap.md](storefront/hd-dang-nhap.md) |
| Storefront-HD-Đăng ký | Storefront | [storefront/hd-dang-ky.md](storefront/hd-dang-ky.md) |
| Storefront-HD-Địa chỉ | Storefront | [storefront/hd-dia-chi.md](storefront/hd-dia-chi.md) |
| Storefront-HD-Đặt hàng | Storefront | [storefront/hd-dat-hang.md](storefront/hd-dat-hang.md) |
| Storefront-HD-Đổi trả | Storefront | [storefront/hd-doi-tra.md](storefront/hd-doi-tra.md) |
| Storefront-HT-Checkout | Storefront | [storefront/ht-checkout.md](storefront/ht-checkout.md) |
| Storefront-HT-Áp mã | Storefront | [storefront/ht-ap-ma.md](storefront/ht-ap-ma.md) |
| Storefront-HT-VNPAY | Storefront | [storefront/ht-vnpay.md](storefront/ht-vnpay.md) |
| Backoffice-Luồng | Backoffice | [backoffice/luong.md](backoffice/luong.md) |
| Backoffice-Lỗi | Backoffice | [backoffice/loi.md](backoffice/loi.md) |
| Backoffice-HD-Tạo khuyến mãi | Backoffice | [backoffice/hd-tao-khuyen-mai.md](backoffice/hd-tao-khuyen-mai.md) |
| Backoffice-HD-Tạo sách | Backoffice | [backoffice/hd-tao-sach.md](backoffice/hd-tao-sach.md) |
| Backoffice-HD-Đơn mua | Backoffice | [backoffice/hd-don-mua.md](backoffice/hd-don-mua.md) |
| Backoffice-HD-Nhập kho | Backoffice | [backoffice/hd-nhap-kho.md](backoffice/hd-nhap-kho.md) |
| Backoffice-HD-Yêu cầu trả kho | Backoffice | [backoffice/hd-yeu-cau-tra-kho.md](backoffice/hd-yeu-cau-tra-kho.md) |

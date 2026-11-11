# Bug UI — Storefront

Thư mục phân loại **bug giao diện (UI)** SF-18–SF-27: bố cục, hiển thị, thao tác cảm ứng, thông báo cho khách và tiêu đề trang. Các mã này đã nằm trong tổng số 34 bug, không tính thêm lần nữa.

Chi tiết tái hiện và trạng thái được giữ tại [danh sách lỗi Storefront](../loi.md#sf-18); bảng dưới dẫn tới từng bug, ảnh bằng chứng và kế hoạch sửa.

| Mã | Bug UI | Bằng chứng | Kế hoạch sửa |
|---|---|---|---|
| [SF-18](../loi.md#sf-18) | Địa chỉ dài tràn màn hình checkout | [Ảnh 1](../../images/SF-18-1.png) | [Kế hoạch](../../fix-plans/storefront/SF-18.md) |
| [SF-19](../loi.md#sf-19) | Nội dung checkout sát mép màn hình | [Ảnh 1](../../images/SF-19-1.webp) | [Kế hoạch](../../fix-plans/storefront/SF-19.md) |
| [SF-20](../loi.md#sf-20) | Khung thông báo bị cắt ở điện thoại | [Ảnh 1](../../images/SF-20-1.png) | [Kế hoạch](../../fix-plans/storefront/SF-20.md) |
| [SF-21](../loi.md#sf-21) | Nút yêu thích và thêm giỏ không hiện trên cảm ứng | [Ảnh 1](../../images/SF-21-1.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-21.md) |
| [SF-22](../loi.md#sf-22) | Chip lọc trạng thái đơn hàng hiển thị tiếng Anh | [Ảnh 1](../../images/SF-22-1.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-22.md) |
| [SF-23](../loi.md#sf-23) | Breadcrumb chồng chữ trên điện thoại | [Ảnh 1](../../images/SF-23-1.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-23.md) |
| [SF-24](../loi.md#sf-24) | Khách chưa đăng nhập thấy trạng thái rỗng của đơn hàng và thông báo | [Ảnh 1](../../images/SF-24-1.jpg), [Ảnh 2](../../images/SF-24-2.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-24.md) |
| [SF-25](../loi.md#sf-25) | Menu phụ điện thoại bị chật và cắt chữ | [Ảnh 1](../../images/SF-25-1.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-25.md) |
| [SF-26](../loi.md#sf-26) | Đường dẫn không tồn tại hiển thị trang 404 mặc định | [Ảnh 1](../../images/SF-26-1.jpg) | [Kế hoạch](../../fix-plans/storefront/SF-26.md) |
| [SF-27](../loi.md#sf-27) | Nhiều trang dùng chung tiêu đề tab | [Bằng chứng nguồn](../../fix-plans/storefront/SF-27.md#bằng-chứng) | [Kế hoạch](../../fix-plans/storefront/SF-27.md) |

Các bản sửa đã vào `origin/develop` qua PR #77 (`b3444b9`), theo lần kiểm tra Git ngày 2026-11-11. Chưa chạy lại kiểm thử giao diện trong đợt ghi tài liệu; SF-27 chưa có ảnh hoặc kết quả `page.title()` được lưu.

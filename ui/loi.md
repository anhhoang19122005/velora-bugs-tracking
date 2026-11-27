# Lỗi giao diện VELORA

Theo dõi responsive, bố cục, bản dịch và định dạng trên Storefront và Backoffice. Trạng thái hiện hành tra ở [bảng trạng thái](../trang-thai.md).

Đợt rà 27/11 chạy Chromium qua Playwright trên local. Storefront `0a72cc4` được kiểm ở 320–1440 px với phiên khách. Backoffice `8e1ecfbe` được kiểm ở 375–1440 px với Admin, Seller và Warehouse. Trang chủ Storefront bị B03 chặn nên phần bố cục trang chủ còn chờ kiểm tra. Checkout có sản phẩm và phiên khách hàng đã đăng nhập nằm ngoài phạm vi đợt này.

## Lỗi UI ghi nhận trong đợt rà

| Mã | Mức độ | Khu vực | Lỗi | Ảnh | Kế hoạch |
| --- | --- | --- | --- | --- | --- |
| [UI-01](#ui-01) | Major | Backoffice | Sidebar chiếm chỗ nội dung ở 375 px | [Ảnh 1](evidence/2026-11-27/cold-admin-admin-accounts-375.png) · [Ảnh 2](evidence/2026-11-27/cold-seller-seller-orders-375.png) · [Ảnh 3](evidence/2026-11-27/cold-warehouse-warehouse-suppliers-375.png) | [Kế hoạch](../fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md) |
| [UI-02](#ui-02) | Minor | Storefront | Header tràn ngang và cắt nút Tài khoản ở 320 px | [Ảnh 1](evidence/2026-11-27/verify-storefront-vi-cart-320.png) | [Kế hoạch](../fix-plans/storefront/UI-02-header-account-overflow-320px.md) |
| [UI-03](#ui-03) | Minor | Storefront | Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt | [Ảnh 1](evidence/2026-11-27/storefront-search-en-375-confirmed.png) | [Kế hoạch](../fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md) |
| [UI-04](#ui-04) | Minor | Backoffice (Seller) | Ngày trên Promotions và Orders khác định dạng | [Ảnh 1](evidence/2026-11-27/seller-date-promotions.png) · [Ảnh 2](evidence/2026-11-27/seller-date-orders.png) | [Kế hoạch](../fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md) |

## UI-01

**Sidebar chiếm chỗ nội dung ở 375 px**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Major |
| Khu vực | Backoffice |
| Bước tái hiện | Mở lần lượt Admin Users, Seller Orders và Warehouse Suppliers trực tiếp ở 375 px với sidebar ở trạng thái mặc định. |
| Thực tế | Sidebar rộng 290 px. Vùng nội dung chính bắt đầu tại x = 290 và chỉ còn 85 px. Tài liệu rộng 395–476 px trên các màn đo được. |
| Mong đợi | Điều hướng, bảng và thao tác chính dùng được ở 375 px. Sidebar desktop vẫn mở và thu gọn được. |
| Bằng chứng | [Ảnh 1](evidence/2026-11-27/cold-admin-admin-accounts-375.png) · [Ảnh 2](evidence/2026-11-27/cold-seller-seller-orders-375.png) · [Ảnh 3](evidence/2026-11-27/cold-warehouse-warehouse-suppliers-375.png) |
| Kế hoạch | [Kế hoạch](../fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md) |

## UI-02

**Header tràn ngang và cắt nút Tài khoản ở 320 px**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Storefront |
| Bước tái hiện | Mở tìm kiếm, giỏ hàng hoặc đăng nhập ở 320 px và quan sát hàng chứa logo, thông báo, yêu thích, giỏ và tài khoản. |
| Thực tế | Tài liệu rộng 326 px ở viewport 320 px. Nút Tài khoản nằm từ x = 282 đến x = 326. Ở 375 px, không đo được phần tràn này. |
| Mong đợi | Tất cả nút nằm trong viewport và mở được bằng chuột, cảm ứng hoặc bàn phím. |
| Bằng chứng | [Ảnh 1](evidence/2026-11-27/verify-storefront-vi-cart-320.png) |
| Kế hoạch | [Kế hoạch](../fix-plans/storefront/UI-02-header-account-overflow-320px.md) |

## UI-03

**Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Storefront |
| Bước tái hiện | Mở `/en/search?q=sapiens`, đợi kết quả rồi đối chiếu với `/vi/search?q=sapiens`. |
| Thực tế | Trang có lang=en nhưng tiêu đề, số kết quả, nhãn độ khớp và một số thông báo vẫn dùng tiếng Việt. |
| Mong đợi | Nhãn giao diện theo locale của route. Tên sách và tác giả giữ đúng nội dung danh mục. |
| Bằng chứng | [Ảnh 1](evidence/2026-11-27/storefront-search-en-375-confirmed.png) |
| Kế hoạch | [Kế hoạch](../fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md) |

## UI-04

**Ngày trên Promotions và Orders khác định dạng**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Backoffice (Seller) |
| Bước tái hiện | Đăng nhập Seller, mở Promotions và Orders trong cùng phiên, so sánh cách trình bày các cột ngày. |
| Thực tế | Trong cùng phiên Seller tiếng Anh, Promotions hiển thị 2026-11-27 ở Starts, còn Orders hiển thị 11/11/2026 ở Placed. |
| Mong đợi | Hai bảng dùng cùng quy ước theo locale đang hiển thị. Ngày hiệu lực khuyến mãi giữ đúng ngày khi đổi múi giờ. |
| Bằng chứng | [Ảnh 1](evidence/2026-11-27/seller-date-promotions.png) · [Ảnh 2](evidence/2026-11-27/seller-date-orders.png) |
| Kế hoạch | [Kế hoạch](../fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md) |

## Lỗi UI đã có mã

- [SF-18–SF-27](../storefront/ui/README.md) có danh mục, ảnh và kế hoạch từ đợt trước.
- [BO-01](../backoffice/loi.md#bo-01) ghi nhận hộp Guided Tasks trống ở trang bị từ chối truy cập.

### B03

[Mã B03](../test-2026-11-27/loi.md#b03) tiếp tục theo dõi ảnh lỗi. Kiểm lại ngày 27/11, trang chủ rơi vào màn “Something broke on our end”. Technical details báo `Invalid src prop` với hostname `x.test`. Trên Search, cùng hostname làm một thẻ hiện ảnh hỏng, trong khi danh sách vẫn dùng được. Thêm case Search vào nghiệm thu B03. [Trang chủ](evidence/2026-11-27/verify-storefront-vi-375.png) · [Kết quả tìm kiếm](evidence/2026-11-27/storefront-search-en-375-confirmed.png) · [Kế hoạch B03](../fix-plans/storefront-backend/B03-catalog-image-host-crashes-storefront.md)

### BO-07

[Mã BO-07](../backoffice/loi.md#bo-07) tái hiện ở Warehouse → Purchase Orders → New tại 1024 px với sidebar mở. Ô Book bị ép hẹp. Ô Import price và nút xóa dòng có chiều rộng hiển thị bằng 0 trong vùng bị cắt. Hai thao tác hiện đầy đủ ở 1440 px khi đo lại. [Ảnh ở 1024 px](evidence/2026-11-27/cold-warehouse-warehouse-purchase-orders-new-1024.png) · [Kế hoạch BO-07](../fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md)

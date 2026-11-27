# Link cho Jira

Dán các link dưới đây vào Jira. Repo là nơi giữ nội dung lỗi; Jira chỉ giữ việc (người phụ trách, tiến độ). Link dùng nhánh `main` nên luôn trỏ tới bản mới nhất. Repo đang **private**: người fix cần được cấp quyền đọc repo trên GitHub.

## Link tổng hợp

Dán vào mô tả Epic (hoặc ticket tổng) trên Jira:

```text
Link tổng hợp các lỗi (trạng thái, người phụ trách, kế hoạch): https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
Chi tiết lỗi Storefront: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md
Chi tiết lỗi Backoffice: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md
Chi tiết lỗi giao diện: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md
Kế hoạch sửa (theo repo cần sửa): https://github.com/anhhoang19122005/velora-bugs-tracking/tree/main/fix-plans
Đợt test 27/11 (Guide me, phân quyền): https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/test-2026-11-27/README.md
Báo cáo test phân quyền: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/test-2026-11-27/phan-quyen/README.md
Cách đọc và cập nhật bảng trạng thái: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md#cập-nhật-bảng-này
```

## Mẫu cho từng ticket

Tiêu đề ticket bắt đầu bằng mã lỗi trong repo, ví dụ `[SF-38] Mã giảm giá được cấp vượt số lượt`, để tìm được hai chiều. Phần mô tả:

```text
Mã lỗi: SF-38
Chi tiết lỗi (bước tái hiện, mong đợi, thực tế, ảnh, API response): https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-38
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-38-promotion-usage-over-redeemed.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

Khi tạo xong ticket, ghi mã Jira vào cột **Phụ trách** hoặc **Ghi chú** của dòng tương ứng trong `trang-thai.md`. Khi sửa, đặt tên nhánh và commit có mã Jira (ví dụ `fix/VEL-123-sf-38-promotion-usage`) để Jira tự gắn commit vào ticket nếu đã nối Jira với GitHub.

## Từng lỗi chưa đóng (49 lỗi)

Lấy từ hai nhóm **Cần sửa** và **Cần xác nhận** của bảng trạng thái. Mỗi lỗi một ticket: chép tiêu đề và khối link của dòng đó.

### Cần sửa

**[SF-45] Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ** (Major)

```text
Mã lỗi: SF-45
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-45
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront-backend/SF-45-catalog-image-host-crashes-storefront.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-13] Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu** (Major)

```text
Mã lỗi: BO-13
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-13
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-13-return-warehouse-duplicate-rma.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-16] Duyệt trả kho cho sách chưa có lô không cộng tồn** (Major)

```text
Mã lỗi: BO-16
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-16
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-16-return-warehouse-missing-batch.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-37] Đặt hàng đồng thời tạo nhiều đơn từ một giỏ** (Major)

```text
Mã lỗi: SF-37
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-37
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-38] Mã giảm giá được cấp vượt số lượt** (Major)

```text
Mã lỗi: SF-38
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-38
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-38-promotion-usage-over-redeemed.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-46] Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0** (Major)

```text
Mã lỗi: SF-46
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-46
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-46-variant-stock-initialization.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-09] Link trong email xác thực trỏ tới địa chỉ giả** (Major)

```text
Mã lỗi: SF-09
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-09
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend-platform/SF-09-verify-email-link-fake-domain.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-14] Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500** (Major)

```text
Mã lỗi: BO-14
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-14
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-14-purchase-order-zero-import-price.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-15] API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động** (Major)

```text
Mã lỗi: BO-15
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-15
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-15-purchase-order-inactive-supplier.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[UI-01] Sidebar chiếm chỗ nội dung ở 375 px** (Major)

```text
Mã lỗi: UI-01
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-01
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-01
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-47] Role USER không còn trên DB dùng chung: đăng ký mới sẽ lỗi** (Major)

```text
Mã lỗi: SF-47
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-47
Kế hoạch sửa: chưa có
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/test-2026-11-27/phan-quyen/README.md#4-phát-hiện
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-24] Admin mất 2 quyền chuyển khoản SePay trên DB dùng chung** (Major)

```text
Mã lỗi: BO-24
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-24
Kế hoạch sửa: chưa có
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/test-2026-11-27/phan-quyen/README.md#31-admin-bị-chặn-ở-chức-năng-của-chính-mình
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-04] notification-service không khởi động vì thiếu biến Mongo** (Major)

```text
Mã lỗi: SF-04
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-04
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend-platform/SF-04-dev-script-notification-missing-mongo-env.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-42] Giỏ hàng mất cập nhật khi thêm đồng thời** (Minor)

```text
Mã lỗi: SF-42
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-42
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-42-concurrent-cart-lost-update.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-43] Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán** (Minor)

```text
Mã lỗi: SF-43
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-43
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-43-duplicate-active-vnpay-payment.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-11] Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời** (Minor)

```text
Mã lỗi: BO-11
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-11
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-11-concurrent-purchase-order-imports.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-35] Tồn kho hiển thị cũ do cache catalog** (Minor)

```text
Mã lỗi: SF-35
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-35
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-35-catalog-stock-cache-stale.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-39] Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối** (Minor)

```text
Mã lỗi: SF-39
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-39
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-39-checkout-order-cancelled-after-success.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-07] Dòng hàng của đơn mua phải cuộn ngang ở 1024px** (Minor)

```text
Mã lỗi: BO-07
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-07
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[UI-02] Header tràn ngang và cắt nút Tài khoản ở 320 px** (Minor)

```text
Mã lỗi: UI-02
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-02
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/UI-02-header-account-overflow-320px.md
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-02
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[UI-03] Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt** (Minor)

```text
Mã lỗi: UI-03
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-03
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-03
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[UI-04] Ngày trên Promotions và Orders khác định dạng** (Minor)

```text
Mã lỗi: UI-04
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-04
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/ui/loi.md#ui-04
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-28] Tham số sai kiểu trả 500 thay vì 400 hoặc 404** (Minor)

```text
Mã lỗi: SF-28
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-28
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-28-invalid-request-parameter-http-status.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-29] Body JSON hỏng hoặc enum sai trả 500** (Minor)

```text
Mã lỗi: SF-29
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-29
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-29-malformed-json-http-400.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-31] Tên hồ sơ nhận ký tự đặc biệt như `<script>`** (Minor)

```text
Mã lỗi: SF-31
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-31
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront-backend/SF-31-profile-name-validation.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-32] Nút Đã nhận hàng không hỏi xác nhận** (Minor)

```text
Mã lỗi: SF-32
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-32
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/SF-32-confirm-before-marking-order-received.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-41] Request trùng đồng thời trả 500 thay vì 409** (Minor)

```text
Mã lỗi: SF-41
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-41
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-41-concurrent-business-conflict-http-409.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-01] Hộp Guided tasks trống phủ lên trang không có quyền** (Minor)

```text
Mã lỗi: BO-01
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-01
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-02] Duyệt khuyến mãi trả updatedAt cũ** (Minor)

```text
Mã lỗi: BO-02
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-02
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-08] Mã khuyến mãi không kiểm định dạng và độ dài** (Minor)

```text
Mã lỗi: BO-08
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-08
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-08-promotion-code-format-length.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-09] Tìm kiếm khuyến mãi trả 500** (Minor)

```text
Mã lỗi: BO-09
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-09
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-09-promotion-search-http-500.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-10] Nhà cung cấp trùng khi tạo đồng thời** (Minor)

```text
Mã lỗi: BO-10
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-10
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-10-concurrent-duplicate-suppliers.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-26] Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn** (Minor)

```text
Mã lỗi: BO-26
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-26
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/BO-26-category-code-format.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-17] Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có** (Minor)

```text
Mã lỗi: BO-17
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-17
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-17-guide-banner-fields.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-18] Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi** (Minor)

```text
Mã lỗi: BO-18
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-18
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-18-guide-promotion-required-quantity.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-20] Guide me nói tiền đã hoàn ngay khi bấm Đã nhận** (Minor)

```text
Mã lỗi: BO-20
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-20
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-20-guide-refund-pending-after-received.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-22] Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập** (Minor)

```text
Mã lỗi: BO-22
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-22
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-22-guide-stock-request-status.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-23] Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng** (Minor)

```text
Mã lỗi: BO-23
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-23
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-23-guide-purchase-order-before-receipt.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-25] Khách đăng nhập ứng dụng quản trị không được báo vì sao bị từ chối** (Minor)

```text
Mã lỗi: BO-25
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-25
Kế hoạch sửa: chưa có
Bằng chứng: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/test-2026-11-27/phan-quyen/README.md#21-đăng-nhập-nhầm-ứng-dụng
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-13] Giao diện hiện thương hiệu Taschen thay vì Velora** (Minor)

```text
Mã lỗi: SF-13
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-13
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/SF-13-branding-taschen-instead-of-velora.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-14] Tiêu đề tab là Book Store và trạng thái đơn hiện mã tiếng Anh** (Minor)

```text
Mã lỗi: SF-14
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-14
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/SF-14-tab-title-book-store-english-status.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-27] Nhiều trang dùng chung tiêu đề tab** (Minor)

```text
Mã lỗi: SF-27
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-27
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront/SF-27-pages-share-same-tab-title.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

### Cần xác nhận

**[SF-06] Email xác thực đến không ổn định** (Major)

```text
Mã lỗi: SF-06
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-06
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/platform/SF-06-verify-email-delivery-unreliable.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-44] Mất event thì đơn có thể kẹt PENDING** (Major)

```text
Mã lỗi: SF-44
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-44
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backend/SF-44-order-event-lost-stuck-pending.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-33] Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được** (Minor)

```text
Mã lỗi: SF-33
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-33
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront-backend/SF-33-vnpay-cancel-retry-policy.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[SF-34] Ô mã khuyến mãi phân biệt hoa thường** (Minor)

```text
Mã lỗi: SF-34
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/storefront/loi.md#sf-34
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/storefront-backend/SF-34-promotion-code-case-policy.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-03] Khuyến mãi quá hạn vẫn hiện Active hoặc Pending** (Minor)

```text
Mã lỗi: BO-03
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-03
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-03-promotion-expired-still-active.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-19] Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới** (Minor)

```text
Mã lỗi: BO-19
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-19
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-19-guide-return-request-after-rejection.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

**[BO-21] Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn** (Minor)

```text
Mã lỗi: BO-21
Chi tiết lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/backoffice/loi.md#bo-21
Kế hoạch sửa: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/fix-plans/backoffice/BO-21-guide-stock-request-approved-quantity.md
Link tổng hợp các lỗi: https://github.com/anhhoang19122005/velora-bugs-tracking/blob/main/trang-thai.md
```

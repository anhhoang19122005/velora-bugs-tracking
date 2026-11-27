# Theo dõi lỗi VELORA

Bảng trạng thái hiện hành của repo, cập nhật ngày 2026-11-27. Mỗi bug có một mã theo dõi. Chi tiết nằm ở [Storefront](storefront/loi.md), [Backoffice](backoffice/loi.md), [UI](ui/loi.md) hoặc [đợt Guide me ngày 27/11](test-2026-11-27/README.md).

Mốc đối chiếu source ngày 27/11 gồm Backend `d5b6ac2`, Backoffice `8e1ecfbe` và Storefront `0a72cc4`. Bảng giữ kết quả trước đó ở những lỗi chưa có bằng chứng mới.

## Tóm tắt

| Nhóm | Số lỗi | Trong đó Major |
| --- | --- | --- |
| [Cần sửa](#cần-sửa) | 38 | 12 |
| [Cần xác nhận](#cần-xác-nhận) | 7 | 2 |
| [Chờ retest](#chờ-retest) | 19 | 3 |
| [Đã đóng](#đã-đóng) | 13 | 6 |
| **Tổng** | **77** | **23** |

Lỗi của [đợt test 27/11](test-2026-11-27/README.md) mang mã SF/BO; mã trong đợt (B.., P..) ghi ở hồ sơ từng lỗi. B02 là bằng chứng bổ sung của SF-38. BO-26 theo dõi mã danh mục, phần mã khuyến mãi thuộc BO-08. SF-45 và BO-07 có bằng chứng UI mới và tiếp tục dùng mã cũ. Mục UI bổ sung bốn lỗi có mã UI-01–UI-04. Xem [bằng chứng và phân loại UI](ui/loi.md).

## Cần sửa

Xếp Major trước. Dùng kế hoạch trong từng dòng để giao việc. Cột Phụ trách ghi tên thành viên sau khi nhóm phân công.

| Mã | Mức độ | Lỗi | Khu vực | Phụ trách | Kết quả gần nhất | Kế hoạch / bằng chứng | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [SF-45](storefront/loi.md#sf-45) | Major | Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ | storefront, catalog-service | — | Còn lỗi, đã retest UI ngày 27/11 | [kế hoạch](fix-plans/storefront-backend/SF-45-catalog-image-host-crashes-storefront.md) · [Retest UI](ui/loi.md#sf-45) | API nhận URL ảnh, `next/image` từ chối hostname khi render. |
| [BO-13](backoffice/loi.md#bo-13) | Major | Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu | inventory-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/BO-13-return-warehouse-duplicate-rma.md) | Khách trả 1 cuốn, duyệt hai phiếu làm tồn tăng 14 → 16. API cũng cho tạo phiếu khai 50 cuốn. |
| [BO-16](backoffice/loi.md#bo-16) | Major | Duyệt trả kho cho sách chưa có lô không cộng tồn | inventory-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/BO-16-return-warehouse-missing-batch.md) | Phiếu chuyển APPROVED, tồn vẫn bằng 0. |
| [SF-37](storefront/loi.md#sf-37) | Major | Đặt hàng đồng thời tạo nhiều đơn từ một giỏ | backend, order-service và storefront | — | Còn lỗi ở lần retest trước | [kế hoạch](fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) | 10 request cùng lúc ra 10 đơn. Code hiện tại vẫn đọc giỏ, lưu đơn rồi mới xóa giỏ. |
| [SF-38](storefront/loi.md#sf-38) | Major | Mã giảm giá được cấp vượt số lượt | backend, order-service và promotion-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/SF-38-promotion-usage-over-redeemed.md) | [B02](test-2026-11-27/guide-me/loi.md#b02): mã còn 1 lượt nhưng hai đơn đều xác nhận và giảm 18.900đ mỗi đơn. Quy tắc hoàn lượt đã chốt theo phương án B. |
| [SF-46](storefront/loi.md#sf-46) | Major | Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0 | catalog-service, inventory-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/SF-46-variant-stock-initialization.md) | Storefront hiện còn 10, đặt hàng trả 409. Liên quan [SF-35](storefront/loi.md#sf-35). |
| [SF-09](storefront/loi.md#sf-09) | Major | Link trong email xác thực trỏ tới địa chỉ giả | notification-service (cấu hình link) | — | Còn lỗi ở lần retest trước | [kế hoạch](fix-plans/backend-platform/SF-09-verify-email-link-fake-domain.md) | Khi chạy native, `dev.ps1` chưa truyền `VERIFY_URL_PREFIX`, nên thiếu cấu hình sẽ dùng `api.taschen.example`. Compose có giá trị riêng. Chưa kiểm link trên môi trường triển khai. |
| [BO-14](backoffice/loi.md#bo-14) | Major | Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500 | inventory-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/BO-14-purchase-order-zero-import-price.md) | Request chấp nhận 0, lớp lưu yêu cầu giá lớn hơn 0. |
| [BO-15](backoffice/loi.md#bo-15) | Major | API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động | inventory-service | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/BO-15-purchase-order-inactive-supplier.md) | Ô chọn trên UI đã ẩn nhà cung cấp, API vẫn trả 201. |
| [UI-01](ui/loi.md#ui-01) | Major | Sidebar chiếm chỗ nội dung ở 375 px | Backoffice | — | Tái hiện trên Chromium local | [Kế hoạch](fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md) · [Bằng chứng](ui/loi.md#ui-01) | Sidebar rộng 290 px. Vùng nội dung chính bắt đầu tại x = 290 và chỉ còn 85 px. Tài liệu rộng 395–476 px trên các màn đo được. |
| [SF-47](storefront/loi.md#sf-47) | Major | Role USER không còn trên DB dùng chung: đăng ký mới sẽ lỗi | DB dùng chung (identity) | — | Tái hiện ngày 27/11 | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#4-phát-hiện) | Chạy lại seed V2 hoặc tìm người đã xoá; không phải lỗi code |
| [BO-24](backoffice/loi.md#bo-24) | Major | Admin mất 2 quyền chuyển khoản SePay trên DB dùng chung | DB dùng chung (identity) | — | Tái hiện ngày 27/11 | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#31-admin-bị-chặn-ở-chức-năng-của-chính-mình) | Chạy lại seed V18; không phải lỗi code |
| [SF-42](storefront/loi.md#sf-42) | Minor | Giỏ hàng mất cập nhật khi thêm đồng thời | backend, order-service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-42-concurrent-cart-lost-update.md) | — |
| [SF-43](storefront/loi.md#sf-43) | Minor | Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán | backend, payment-service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-43-duplicate-active-vnpay-payment.md) | — |
| [BO-11](backoffice/loi.md#bo-11) | Minor | Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời | backend, inventory-service | — | Tái hiện | [kế hoạch](fix-plans/backend/BO-11-concurrent-purchase-order-imports.md) | Chỉ một phiếu nhận được hàng |
| [SF-35](storefront/loi.md#sf-35) | Minor | Tồn kho hiển thị cũ do cache catalog | backend, catalog-service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-35-catalog-stock-cache-stale.md) | Inventory báo 49 cuốn, API sách báo 50 |
| [SF-39](storefront/loi.md#sf-39) | Minor | Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối | backend, order-service (và storefront) | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-39-checkout-order-cancelled-after-success.md) | Không bán vượt tồn kho; chỉ trải nghiệm |
| [BO-07](backoffice/loi.md#bo-07) | Minor | Dòng hàng của đơn mua phải cuộn ngang ở 1024px | backoffice | — | Còn lỗi, đã retest UI ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md) · [Retest UI](ui/loi.md#bo-07) | — |
| [UI-02](ui/loi.md#ui-02) | Minor | Header tràn ngang và cắt nút Tài khoản ở 320 px | Storefront | — | Tái hiện trên Chromium local | [Kế hoạch](fix-plans/storefront/UI-02-header-account-overflow-320px.md) · [Bằng chứng](ui/loi.md#ui-02) | Tài liệu rộng 326 px ở viewport 320 px. Nút Tài khoản nằm từ x = 282 đến x = 326. Ở 375 px, không đo được phần tràn này. |
| [UI-03](ui/loi.md#ui-03) | Minor | Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt | Storefront | — | Tái hiện trên Chromium local | [Kế hoạch](fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md) · [Bằng chứng](ui/loi.md#ui-03) | Trang có lang=en nhưng tiêu đề, số kết quả, nhãn độ khớp và một số thông báo vẫn dùng tiếng Việt. |
| [UI-04](ui/loi.md#ui-04) | Minor | Ngày trên Promotions và Orders khác định dạng | Backoffice (Seller) | — | Tái hiện trên Chromium local | [Kế hoạch](fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md) · [Bằng chứng](ui/loi.md#ui-04) | Trong cùng phiên Seller tiếng Anh, Promotions hiển thị 2026-11-27 ở Starts, còn Orders hiển thị 11/11/2026 ở Placed. |
| [SF-28](storefront/loi.md#sf-28) | Minor | Tham số sai kiểu trả 500 thay vì 400 hoặc 404 | backend, nhiều service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-28-invalid-request-parameter-http-status.md) | — |
| [SF-29](storefront/loi.md#sf-29) | Minor | Body JSON hỏng hoặc enum sai trả 500 | backend, order-service và promotion-service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-29-malformed-json-http-400.md) | — |
| [SF-31](storefront/loi.md#sf-31) | Minor | Tên hồ sơ nhận ký tự đặc biệt như `<script>` | backend, identity-service | — | Tái hiện | [kế hoạch](fix-plans/storefront-backend/SF-31-profile-name-validation.md) | — |
| [SF-32](storefront/loi.md#sf-32) | Minor | Nút Đã nhận hàng không hỏi xác nhận | storefront | — | Tái hiện | [kế hoạch](fix-plans/storefront/SF-32-confirm-before-marking-order-received.md) | — |
| [SF-41](storefront/loi.md#sf-41) | Minor | Request trùng đồng thời trả 500 thay vì 409 | backend, nhiều service | — | Tái hiện | [kế hoạch](fix-plans/backend/SF-41-concurrent-business-conflict-http-409.md) | Dữ liệu đúng, chỉ sai mã trả về |
| [BO-01](backoffice/loi.md#bo-01) | Minor | Hộp Guided tasks trống phủ lên trang không có quyền | backoffice | — | Tái hiện | [kế hoạch](fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md) | — |
| [BO-02](backoffice/loi.md#bo-02) | Minor | Duyệt khuyến mãi trả updatedAt cũ | backend, promotion-service | — | Tái hiện | [kế hoạch](fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md) | — |
| [BO-08](backoffice/loi.md#bo-08) | Minor | Mã khuyến mãi không kiểm định dạng và độ dài | backend, promotion-service | — | Tái hiện | [kế hoạch](fix-plans/backend/BO-08-promotion-code-format-length.md) | [BO-26](backoffice/loi.md#bo-26) xác nhận phần định dạng: mã có chữ thường và dấu cách vẫn được lưu. |
| [BO-09](backoffice/loi.md#bo-09) | Minor | Tìm kiếm khuyến mãi trả 500 | backend, promotion-service | — | Tái hiện | [kế hoạch](fix-plans/backend/BO-09-promotion-search-http-500.md) | — |
| [BO-10](backoffice/loi.md#bo-10) | Minor | Nhà cung cấp trùng khi tạo đồng thời | backend, inventory-service | — | Tái hiện | [kế hoạch](fix-plans/backend/BO-10-concurrent-duplicate-suppliers.md) | — |
| [BO-26](backoffice/loi.md#bo-26) | Minor | Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn | catalog-service, Backoffice | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/BO-26-category-code-format.md) | Dòng này theo dõi phần danh mục. |
| [BO-17](backoffice/loi.md#bo-17) | Minor | Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có | Backoffice Guide me | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-17-guide-banner-fields.md) | Form và API chỉ có tên và URL ảnh. |
| [BO-18](backoffice/loi.md#bo-18) | Minor | Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi | Backoffice Guide me | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-18-guide-promotion-required-quantity.md) | Số lượt là trường bắt buộc. |
| [BO-20](backoffice/loi.md#bo-20) | Minor | Guide me nói tiền đã hoàn ngay khi bấm Đã nhận | Backoffice Guide me | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-20-guide-refund-pending-after-received.md) | Đơn ở REFUND_PENDING, khoản hoàn OPEN và chờ ghi nhận chi trả. |
| [BO-22](backoffice/loi.md#bo-22) | Minor | Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập | Backoffice Guide me | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-22-guide-stock-request-status.md) | Yêu cầu dừng ở ORDERED, đơn mua mới chuyển RECEIVED. |
| [BO-23](backoffice/loi.md#bo-23) | Minor | Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng | Backoffice Guide me | — | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backoffice/BO-23-guide-purchase-order-before-receipt.md) | Đơn APPROVED chưa nhập được. Phải sang ORDERED. |
| [BO-25](backoffice/loi.md#bo-25) | Minor | Khách đăng nhập ứng dụng quản trị không được báo vì sao bị từ chối | backoffice | — | Tái hiện ngày 27/11 | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#21-đăng-nhập-nhầm-ứng-dụng) | — |

## Cần xác nhận

Cần thêm bằng chứng hoặc cần chốt nghiệp vụ trước khi sửa.

| Mã | Mức độ | Lỗi | Khu vực | Phụ trách | Việc tiếp theo | Kế hoạch | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [SF-06](storefront/loi.md#sf-06) | Major | Email xác thực đến không ổn định | hạ tầng / backend | — | Chạy nhiều lượt đăng ký và kiểm log gửi email | [kế hoạch](fix-plans/platform/SF-06-verify-email-delivery-unreliable.md) | Một lần đăng ký nhận email sau khoảng 30 giây. Chưa xác minh độ ổn định của luồng gửi hiện tại. |
| [SF-44](storefront/loi.md#sf-44) | Major | Mất event thì đơn có thể kẹt PENDING | backend, order-service | — | Tái hiện mất sự kiện trong môi trường test | [kế hoạch](fix-plans/backend/SF-44-order-event-lost-stuck-pending.md) | Code gửi sự kiện sau commit và chỉ ghi log khi gửi lỗi. Chưa thấy cơ chế gửi lại hoặc xử lý đơn kẹt cho luồng đặt hàng. |
| [SF-33](storefront/loi.md#sf-33) | Minor | Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được | order-service, payment-service | — | Chốt có cho thử thanh toán lại sau lỗi VNPay | [kế hoạch](fix-plans/storefront-backend/SF-33-vnpay-cancel-retry-policy.md) | Chưa rõ có phải chủ đích |
| [SF-34](storefront/loi.md#sf-34) | Minor | Ô mã khuyến mãi phân biệt hoa thường | storefront, promotion-service | — | Chốt quy tắc viết hoa và chuẩn hóa mã | [kế hoạch](fix-plans/storefront-backend/SF-34-promotion-code-case-policy.md) | Cần xác nhận |
| [BO-03](backoffice/loi.md#bo-03) | Minor | Khuyến mãi quá hạn vẫn hiện Active hoặc Pending | seller, promotion-service | — | Đối chiếu trạng thái trước và sau mốc hết hạn | [kế hoạch](fix-plans/backoffice/BO-03-promotion-expired-still-active.md) | Chưa xác nhận lại |
| [BO-19](backoffice/loi.md#bo-19) | Minor | Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới | Backoffice Guide me, order-service | — | Chốt cách gửi lại yêu cầu trả hàng | [kế hoạch](fix-plans/backoffice/BO-19-guide-return-request-after-rejection.md) | Đã tạo được yêu cầu mới sau khi bị từ chối. Cần chốt quy tắc gửi lại. |
| [BO-21](backoffice/loi.md#bo-21) | Minor | Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn | Backoffice Guide me, inventory-service | — | Chốt quyền sửa số lượng khi duyệt yêu cầu nhập | [kế hoạch](fix-plans/backoffice/BO-21-guide-stock-request-approved-quantity.md) | Cần chốt Admin có được sửa số lượng ở bước duyệt hay không. |

## Chờ retest

Đã ghi nhận bản sửa hoặc xác nhận một phần. Chạy lại đúng môi trường và phạm vi còn thiếu trước khi đóng.

| Mã | Mức độ | Lỗi | Bản sửa | Phụ trách | Kết quả gần nhất | Việc tiếp theo | Kế hoạch | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [SF-03](storefront/loi.md#sf-03) | Major | order-service không ghi log khi trả lỗi | backend PR #117 (`e090ed4`) | — | Chưa xác nhận | Đối chiếu traceId với log service khi có 500 | [Kế hoạch](fix-plans/backend/SF-03-order-service-no-error-log.md) | Đã có trong code và unit test; chưa đọc log của service đang chạy |
| [SF-04](storefront/loi.md#sf-04) | Major | notification-service không khởi động vì thiếu biến Mongo | backend `dev.ps1` trên `develop` | — | Đã xác nhận với chạy native | Kiểm notification-service và gửi mail bằng Compose | [Kế hoạch](fix-plans/backend-platform/SF-04-dev-script-notification-missing-mongo-env.md) | Phạm vi đã sửa là `dev.ps1`. Docker Compose vẫn truyền `MONGO_URI`, trong khi service đọc `NOTIFICATION_MONGO_URI`. Chưa kiểm thử Compose. |
| [SF-40](storefront/loi.md#sf-40) | Major | Đổi trả đồng thời tạo nhiều yêu cầu cho một cuốn | backend PR #121 (`3fd69ed`) | — | Chưa xác nhận lại | Kiểm tạo yêu cầu đổi trả đồng thời | [Kế hoạch](fix-plans/backend/SF-40-return-concurrent-duplicate-requests.md) | Khóa đơn trong giao dịch trước khi kiểm yêu cầu trả hàng đang mở. Có `ReturnRequestConcurrencyIT` trong source. BO-13 theo dõi bước tạo phiếu trả về kho. |
| [SF-11](storefront/loi.md#sf-11) | Minor | Mọi lỗi 403 khi đăng nhập đều báo chưa xác thực email | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-11-login-403-wrong-unverified-message.md) | — |
| [SF-13](storefront/loi.md#sf-13) | Minor | Giao diện hiện thương hiệu Taschen thay vì Velora | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-13-branding-taschen-instead-of-velora.md) | — |
| [SF-14](storefront/loi.md#sf-14) | Minor | Tiêu đề tab là Book Store và trạng thái đơn hiện mã tiếng Anh | storefront PR #77 (`b3444b9`) | — | Xác nhận một phần | Đo tiêu đề trang chủ và payment-result theo locale | [Kế hoạch](fix-plans/storefront/SF-14-tab-title-book-store-english-status.md) | Trạng thái đã tiếng Việt; trang chủ và payment-result vẫn dùng tiêu đề chung |
| [SF-17](storefront/loi.md#sf-17) | Minor | Chi tiết sách hiện 0 trang, năm 0, 0 g | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-17-book-detail-zero-pages-year-weight.md) | — |
| [SF-18](storefront/loi.md#sf-18) | Minor | Địa chỉ dài tràn màn hình checkout | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-18-checkout-long-address-overflow.md) | — |
| [SF-19](storefront/loi.md#sf-19) | Minor | Nội dung checkout sát mép màn hình | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-19-checkout-content-touches-edge.md) | — |
| [SF-20](storefront/loi.md#sf-20) | Minor | Khung thông báo bị cắt ở điện thoại | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-20-toast-cut-off-mobile.md) | — |
| [SF-21](storefront/loi.md#sf-21) | Minor | Nút yêu thích và thêm giỏ không hiện trên cảm ứng | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-21-wishlist-cart-buttons-hidden-touch.md) | — |
| [SF-22](storefront/loi.md#sf-22) | Minor | Chip lọc trạng thái đơn hàng hiển thị tiếng Anh | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-22-order-status-chip-english.md) | — |
| [SF-23](storefront/loi.md#sf-23) | Minor | Breadcrumb chồng chữ trên điện thoại | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-23-breadcrumb-overlap-mobile.md) | — |
| [SF-24](storefront/loi.md#sf-24) | Minor | Khách chưa đăng nhập thấy trạng thái rỗng của đơn hàng và thông báo | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-24-guest-sees-empty-orders-notifications.md) | — |
| [SF-25](storefront/loi.md#sf-25) | Minor | Menu phụ điện thoại bị chật và cắt chữ | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-25-mobile-subnav-cramped-clipped.md) | 9 trang chính không cuộn ngang ở 375px |
| [SF-26](storefront/loi.md#sf-26) | Minor | Đường dẫn không tồn tại hiển thị trang 404 mặc định | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Chạy lại case gốc | [Kế hoạch](fix-plans/storefront/SF-26-unknown-route-default-404.md) | — |
| [SF-27](storefront/loi.md#sf-27) | Minor | Nhiều trang dùng chung tiêu đề tab | storefront PR #77 (`b3444b9`) | — | Chưa xác nhận lại | Đo tiêu đề từng route bằng page.title() | [Kế hoạch](fix-plans/storefront/SF-27-pages-share-same-tab-title.md) | — |
| [SF-30](storefront/loi.md#sf-30) | Minor | Đăng nhập sai nhiều lần không bị giới hạn | backend PR #140 (`e06e334`) | — | Chưa xác nhận lại | Kiểm giới hạn đăng nhập và hành vi khi Redis lỗi | [Kế hoạch](fix-plans/backend/SF-30-login-rate-limit.md) | Gateway giới hạn theo IP và email. Khi Redis lỗi, Gateway cho request đi qua. |
| [BO-12](backoffice/loi.md#bo-12) | Minor | Điều hướng Admin làm mất tiền tố /admin, mất phiên | backoffice PR #369 (merge `fe73d47f`, BUG-001) | — | Chưa xác nhận lại | Kiểm điều hướng, tải lại và phiên dưới /admin | [Kế hoạch](fix-plans/backoffice/BO-12-admin-prefix-session.md) | Sửa ở lớp bảo vệ `proxy.ts`: đường dẫn thường được chuyển về `/admin/<console>/…`; chưa chạy lại trên giao diện |

## Đã đóng

Kết luận ghi rõ trường hợp đã xác nhận bằng kiểm thử, đã chấp nhận hoặc đóng theo thiết kế. Với kết quả có giới hạn phạm vi, xem ghi chú của từng lỗi.

| Mã | Mức độ | Lỗi | Bản sửa | Kết luận | Bằng chứng / lý do |
| --- | --- | --- | --- | --- | --- |
| [SF-01](storefront/loi.md#sf-01) | Major | Proxy chuyển tiếp header Origin nên gateway trả 403 | storefront PR #77 (`b3444b9`) | Đã xác nhận | Gọi thẳng gateway với Origin :3003 vẫn 403, cần đặt `CORS_ALLOWED_ORIGINS` |
| [SF-02](storefront/loi.md#sf-02) | Major | Số điện thoại sai được lưu ở địa chỉ, đặt hàng lỗi 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-05](storefront/loi.md#sf-05) | Major | Nhấn F5 mất phiên đăng nhập và giỏ hàng | storefront PR #77 (`b3444b9`) | Đã xác nhận | — |
| [SF-07](storefront/loi.md#sf-07) | Major | Khởi tạo thanh toán VNPay trả 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Đã tới cổng sandbox và nhánh hủy; chưa test thanh toán thành công bằng thẻ |
| [SF-08](storefront/loi.md#sf-08) | Major | Đặt hàng có mã khuyến mãi trả 400 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Một phần của lỗi vẫn còn ở SF-38 (cấp mã vượt lượt khi đồng thời) |
| [SF-10](storefront/loi.md#sf-10) | Major | Địa chỉ chấp nhận ký tự đặc biệt, rồi đặt hàng lỗi | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-12](storefront/loi.md#sf-12) | Minor | Gợi ý sách và sự kiện hành vi lỗi 500 | backend PR #139 (`760c5e5`) | Đã xác nhận ở lần retest trước | `dev.ps1` trên `develop` khởi động tracking-service và truyền `TRACKING_MONGO_URI`. Lần retest trước, `/recommendations/trending` trả 200. |
| [SF-15](storefront/loi.md#sf-15) | Minor | Bấm Huỷ đơn là huỷ ngay, không hỏi lại | storefront PR #77 (`b3444b9`) | Đã xác nhận | Nút Đã nhận hàng vẫn không hỏi: SF-32 |
| [BO-04](backoffice/loi.md#bo-04) | Minor | Form tạo khuyến mãi báo lỗi chung và mất dữ liệu | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Báo lỗi tại từng ô, không gửi request khi chưa hợp lệ |
| [BO-06](backoffice/loi.md#bo-06) | Minor | Form sách và đơn mua không chỉ ra trường quá dài | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Kiểm trên form sách; đơn mua kiểm ở lần trước |
| [BO-05](backoffice/loi.md#bo-05) | Minor | Ô giá tự bỏ dấu trừ, lưu -1 thành 1 | — | Chấp nhận | Người dùng xác nhận ngày 2026-11-12 là hợp lý; chưa kiểm tra lưu sau chuẩn hóa |
| [SF-16](storefront/loi.md#sf-16) | Minor | Mật khẩu 5 ký tự vẫn được gửi lên API khi đăng nhập | — | Đã đóng | Đúng thiết kế: form đăng nhập không được nêu quy tắc mật khẩu |
| [SF-36](storefront/loi.md#sf-36) | Minor | Hủy đơn không hoàn lượt mã | — | Đã đóng | Đúng quy tắc: khách tự hủy thì không hoàn (hệ thống và nhân viên hủy thì hoàn, xem SF-38) |

## Cập nhật bảng này

1. Tìm mã hiện có trước khi thêm bug. Gắn một lần tái hiện mới vào mã cũ nếu cùng vấn đề.
2. Khi nhận việc, ghi người phụ trách. Sau merge, chuyển dòng sang Chờ retest, ghi PR hoặc commit và phạm vi cần chạy lại.
3. Khi retest xác nhận, chuyển dòng sang Đã đóng và ghi môi trường, case đã chạy và kết quả. Nếu vẫn tái hiện, chuyển về Cần sửa. Nếu chấp nhận hành vi, ghi quyết định và lý do.
4. Cập nhật số lượng trong Tóm tắt và chi tiết trạng thái trong hồ sơ bug tương ứng. Lưu kết quả và ảnh theo đợt test để giữ lịch sử.

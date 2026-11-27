# Theo dõi lỗi: đã sửa và chưa sửa

Cập nhật ngày 2026-11-27. Đối chiếu code trên `develop` của Backend `d5b6ac2`, Backoffice `8e1ecfbe` và Storefront `0a72cc4` với [báo cáo đợt test 27/11](https://github.com/anhhoang19122005/velora-bugs-tracking/tree/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27). Các trạng thái không có bằng chứng mới giữ theo lần kiểm tra trước. Xem chi tiết tại [Storefront](storefront/loi.md), [Backoffice](backoffice/loi.md) và [kế hoạch sửa](fix-plans/).

## Tóm tắt

| Trạng thái | Số lỗi | Trong đó Major |
|---|---|---|
| **Chưa sửa** | 38 | 11 |
| **Đã sửa** | 29 | 9 |
| **Đã đóng hoặc chấp nhận** | 3 | 0 |
| **Tổng** | 70 | 20 |

Đợt 27/11 bổ sung 14 dòng (6 Major, 8 Minor). B02 bổ sung bằng chứng cho SF-38. B08 chỉ bổ sung dòng mã danh mục, phần mã khuyến mãi ghi tại BO-08. SF-40 và SF-30 đã có bản sửa trên `develop` và chờ retest.

Cách đọc cột **Retest**: *Đã xác nhận* là chạy lại và thấy đã hết lỗi. *Chưa xác nhận lại* là code đã sửa nhưng chưa chạy lại. *Còn lỗi* là chạy lại và vẫn tái hiện. *Chưa tái hiện* là mới thấy qua đọc code. *Cần xác nhận* là chưa rõ đúng hay sai theo nghiệp vụ.

## Chưa sửa

Xếp theo mức độ, Major trước.

| # | Mức độ | Lỗi | Nơi cần sửa | Retest | Kế hoạch | Ghi chú |
|---|---|---|---|---|---|---|
| [SF-06](storefront/loi.md#sf-06) | Major | Email xác thực đến không ổn định | hạ tầng / backend | Không tái hiện ở lần retest trước | [kế hoạch](fix-plans/platform/SF-06-verify-email-delivery-unreliable.md) | Một lần đăng ký nhận email sau khoảng 30 giây. Chưa xác minh độ ổn định của luồng gửi hiện tại. |
| [SF-09](storefront/loi.md#sf-09) | Major | Link trong email xác thực trỏ tới địa chỉ giả | notification-service (cấu hình link) | Còn lỗi ở lần retest trước | [kế hoạch](fix-plans/backend-platform/SF-09-verify-email-link-fake-domain.md) | Khi chạy native, `dev.ps1` chưa truyền `VERIFY_URL_PREFIX`, nên thiếu cấu hình sẽ dùng `api.taschen.example`. Compose có giá trị riêng. Chưa kiểm link trên môi trường triển khai. |
| [SF-37](storefront/loi.md#sf-37) | Major | Đặt hàng đồng thời tạo nhiều đơn từ một giỏ | backend, order-service và storefront | Còn lỗi ở lần retest trước | [kế hoạch](fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) | 10 request cùng lúc ra 10 đơn. Code hiện tại vẫn đọc giỏ, lưu đơn rồi mới xóa giỏ. |
| [SF-38](storefront/loi.md#sf-38) | Major | Mã giảm giá được cấp vượt số lượt | backend, order-service và promotion-service | Còn lỗi ngày 27/11 | [kế hoạch](fix-plans/backend/SF-38-promotion-usage-over-redeemed.md) | [B02](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b02): mã còn 1 lượt nhưng hai đơn đều xác nhận và giảm 18.900đ mỗi đơn. Quy tắc hoàn lượt đã chốt theo phương án B. |
| [SF-44](storefront/loi.md#sf-44) | Major | Mất event thì đơn có thể kẹt PENDING | backend, order-service | Chưa tái hiện | [kế hoạch](fix-plans/backend/SF-44-order-event-lost-stuck-pending.md) | Code gửi sự kiện sau commit và chỉ ghi log khi gửi lỗi. Chưa thấy cơ chế gửi lại hoặc xử lý đơn kẹt cho luồng đặt hàng. |
| [B01](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b01) | Major | Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu | inventory-service | Còn lỗi ngày 27/11 | chưa có | Khách trả 1 cuốn, duyệt hai phiếu làm tồn tăng 14 → 16. API cũng cho tạo phiếu khai 50 cuốn. |
| [B03](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b03) | Major | Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ | storefront, catalog-service | Còn lỗi ngày 27/11 | chưa có | API nhận URL ảnh, `next/image` từ chối hostname khi render. |
| [B04](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b04) | Major | Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0 | catalog-service, inventory-service | Còn lỗi ngày 27/11 | chưa có | Storefront hiện còn 10, đặt hàng trả 409. Liên quan [SF-35](storefront/loi.md#sf-35). |
| [B05](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b05) | Major | Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500 | inventory-service | Còn lỗi ngày 27/11 | chưa có | Request chấp nhận 0, lớp lưu yêu cầu giá lớn hơn 0. |
| [B06](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b06) | Major | API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động | inventory-service | Còn lỗi ngày 27/11 | chưa có | Ô chọn trên UI đã ẩn nhà cung cấp, API vẫn trả 201. |
| [B07](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b07) | Major | Duyệt trả kho cho sách chưa có lô không cộng tồn | inventory-service | Còn lỗi ngày 27/11 | chưa có | Phiếu chuyển APPROVED, tồn vẫn bằng 0. |
| [SF-28](storefront/loi.md#sf-28) | Minor | Tham số sai kiểu trả 500 thay vì 400 hoặc 404 | backend, nhiều service | Còn lỗi | chưa có |  |
| [SF-29](storefront/loi.md#sf-29) | Minor | Body JSON hỏng hoặc enum sai trả 500 | backend, order-service và promotion-service | Còn lỗi | chưa có |  |
| [SF-31](storefront/loi.md#sf-31) | Minor | Tên hồ sơ nhận ký tự đặc biệt như `<script>` | backend, identity-service | Còn lỗi | chưa có |  |
| [SF-32](storefront/loi.md#sf-32) | Minor | Nút Đã nhận hàng không hỏi xác nhận | storefront | Còn lỗi | chưa có |  |
| [SF-33](storefront/loi.md#sf-33) | Minor | Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được | order-service, payment-service | Cần xác nhận | chưa có | Chưa rõ có phải chủ đích |
| [SF-34](storefront/loi.md#sf-34) | Minor | Ô mã khuyến mãi phân biệt hoa thường | storefront, promotion-service | Cần xác nhận | chưa có |  |
| [SF-35](storefront/loi.md#sf-35) | Minor | Tồn kho hiển thị cũ do cache catalog | backend, catalog-service | Còn lỗi | chưa có | Inventory báo 49 cuốn, API sách báo 50 |
| [SF-39](storefront/loi.md#sf-39) | Minor | Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối | backend, order-service (và storefront) | Còn lỗi | [kế hoạch](fix-plans/backend/SF-39-checkout-order-cancelled-after-success.md) | Không bán vượt tồn kho; chỉ trải nghiệm |
| [SF-41](storefront/loi.md#sf-41) | Minor | Request trùng đồng thời trả 500 thay vì 409 | backend, nhiều service | Còn lỗi | chưa có | Dữ liệu đúng, chỉ sai mã trả về |
| [SF-42](storefront/loi.md#sf-42) | Minor | Giỏ hàng mất cập nhật khi thêm đồng thời | backend, order-service | Còn lỗi | chưa có |  |
| [SF-43](storefront/loi.md#sf-43) | Minor | Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán | backend, payment-service | Còn lỗi | chưa có |  |
| [BO-01](backoffice/loi.md#bo-01) | Minor | Hộp Guided tasks trống phủ lên trang không có quyền | backoffice | Còn lỗi | [kế hoạch](fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md) |  |
| [BO-02](backoffice/loi.md#bo-02) | Minor | Duyệt khuyến mãi trả updatedAt cũ | backend, promotion-service | Còn lỗi | [kế hoạch](fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md) |  |
| [BO-03](backoffice/loi.md#bo-03) | Minor | Khuyến mãi quá hạn vẫn hiện Active hoặc Pending | seller, promotion-service | Chưa xác nhận lại | [kế hoạch](fix-plans/backoffice/BO-03-promotion-expired-still-active.md) |  |
| [BO-07](backoffice/loi.md#bo-07) | Minor | Dòng hàng của đơn mua phải cuộn ngang ở 1024px | backoffice | Còn lỗi | [kế hoạch](fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md) |  |
| [BO-08](backoffice/loi.md#bo-08) | Minor | Mã khuyến mãi không kiểm định dạng và độ dài | backend, promotion-service | Còn lỗi | chưa có | [B08](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b08) xác nhận phần định dạng: mã có chữ thường và dấu cách vẫn được lưu. |
| [BO-09](backoffice/loi.md#bo-09) | Minor | Tìm kiếm khuyến mãi trả 500 | backend, promotion-service | Còn lỗi | chưa có |  |
| [BO-10](backoffice/loi.md#bo-10) | Minor | Nhà cung cấp trùng khi tạo đồng thời | backend, inventory-service | Còn lỗi | chưa có |  |
| [BO-11](backoffice/loi.md#bo-11) | Minor | Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời | backend, inventory-service | Còn lỗi | chưa có | Chỉ một phiếu nhận được hàng |
| [B08](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b08) | Minor | Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn | catalog-service, Backoffice | Còn lỗi ngày 27/11 | chưa có | Dòng này theo dõi phần danh mục. |
| [B09](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b09) | Minor | Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có | Backoffice Guide me | Còn lỗi ngày 27/11 | chưa có | Form và API chỉ có tên và URL ảnh. |
| [B10](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b10) | Minor | Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi | Backoffice Guide me | Còn lỗi ngày 27/11 | chưa có | Số lượt là trường bắt buộc. |
| [B11](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b11) | Minor | Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới | Backoffice Guide me, order-service | Cần xác nhận nghiệp vụ | chưa có | Đã tạo được yêu cầu mới sau khi bị từ chối. Cần chốt quy tắc gửi lại. |
| [B12](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b12) | Minor | Guide me nói tiền đã hoàn ngay khi bấm Đã nhận | Backoffice Guide me | Còn lỗi ngày 27/11 | chưa có | Đơn ở REFUND_PENDING, khoản hoàn OPEN và chờ ghi nhận chi trả. |
| [B13](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b13) | Minor | Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn | Backoffice Guide me, inventory-service | Cần xác nhận nghiệp vụ | chưa có | Cần chốt Admin có được sửa số lượng ở bước duyệt hay không. |
| [B14](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b14) | Minor | Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập | Backoffice Guide me | Còn lỗi ngày 27/11 | chưa có | Yêu cầu dừng ở ORDERED, đơn mua mới chuyển RECEIVED. |
| [B15](https://github.com/anhhoang19122005/velora-bugs-tracking/blob/0c859c7034774de2a9e8414707227df1ca6af025/test-2026-11-27/loi.md#b15) | Minor | Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng | Backoffice Guide me | Còn lỗi ngày 27/11 | chưa có | Đơn APPROVED chưa nhập được. Phải sang ORDERED. |

## Đã sửa

| # | Mức độ | Lỗi | Đã sửa ở | Retest | Ghi chú |
|---|---|---|---|---|---|
| [SF-01](storefront/loi.md#sf-01) | Major | Proxy chuyển tiếp header Origin nên gateway trả 403 | storefront PR #77 (`b3444b9`) | Đã xác nhận | Gọi thẳng gateway với Origin :3003 vẫn 403, cần đặt `CORS_ALLOWED_ORIGINS` |
| [SF-02](storefront/loi.md#sf-02) | Major | Số điện thoại sai được lưu ở địa chỉ, đặt hàng lỗi 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-03](storefront/loi.md#sf-03) | Major | order-service không ghi log khi trả lỗi | backend PR #117 (`e090ed4`) | Chưa xác nhận | Đã có trong code và unit test; chưa đọc log của service đang chạy |
| [SF-04](storefront/loi.md#sf-04) | Major | notification-service không khởi động vì thiếu biến Mongo | backend `dev.ps1` trên `develop` | Đã xác nhận với chạy native | Phạm vi đã sửa là `dev.ps1`. Docker Compose vẫn truyền `MONGO_URI`, trong khi service đọc `NOTIFICATION_MONGO_URI`. Chưa kiểm thử Compose. |
| [SF-05](storefront/loi.md#sf-05) | Major | Nhấn F5 mất phiên đăng nhập và giỏ hàng | storefront PR #77 (`b3444b9`) | Đã xác nhận |  |
| [SF-07](storefront/loi.md#sf-07) | Major | Khởi tạo thanh toán VNPay trả 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Đã tới cổng sandbox và nhánh hủy; chưa test thanh toán thành công bằng thẻ |
| [SF-08](storefront/loi.md#sf-08) | Major | Đặt hàng có mã khuyến mãi trả 400 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Một phần của lỗi vẫn còn ở SF-38 (cấp mã vượt lượt khi đồng thời) |
| [SF-10](storefront/loi.md#sf-10) | Major | Địa chỉ chấp nhận ký tự đặc biệt, rồi đặt hàng lỗi | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-40](storefront/loi.md#sf-40) | Major | Đổi trả đồng thời tạo nhiều yêu cầu cho một cuốn | backend PR #121 (`3fd69ed`) | Chưa xác nhận lại | Khóa đơn trong giao dịch trước khi kiểm yêu cầu trả hàng đang mở. Có `ReturnRequestConcurrencyIT` trong source. B01 theo dõi bước tạo phiếu trả về kho. |
| [SF-11](storefront/loi.md#sf-11) | Minor | Mọi lỗi 403 khi đăng nhập đều báo chưa xác thực email | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-12](storefront/loi.md#sf-12) | Minor | Gợi ý sách và sự kiện hành vi lỗi 500 | backend PR #139 (`760c5e5`) | Đã xác nhận ở lần retest trước | `dev.ps1` trên `develop` khởi động tracking-service và truyền `TRACKING_MONGO_URI`. Lần retest trước, `/recommendations/trending` trả 200. |
| [SF-13](storefront/loi.md#sf-13) | Minor | Giao diện hiện thương hiệu Taschen thay vì Velora | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-14](storefront/loi.md#sf-14) | Minor | Tiêu đề tab là Book Store và trạng thái đơn hiện mã tiếng Anh | storefront PR #77 (`b3444b9`) | Xác nhận một phần | Trạng thái đã tiếng Việt; trang chủ và payment-result vẫn dùng tiêu đề chung |
| [SF-15](storefront/loi.md#sf-15) | Minor | Bấm Huỷ đơn là huỷ ngay, không hỏi lại | storefront PR #77 (`b3444b9`) | Đã xác nhận | Nút Đã nhận hàng vẫn không hỏi: SF-32 |
| [SF-17](storefront/loi.md#sf-17) | Minor | Chi tiết sách hiện 0 trang, năm 0, 0 g | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-18](storefront/loi.md#sf-18) | Minor | Địa chỉ dài tràn màn hình checkout | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-19](storefront/loi.md#sf-19) | Minor | Nội dung checkout sát mép màn hình | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-20](storefront/loi.md#sf-20) | Minor | Khung thông báo bị cắt ở điện thoại | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-21](storefront/loi.md#sf-21) | Minor | Nút yêu thích và thêm giỏ không hiện trên cảm ứng | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-22](storefront/loi.md#sf-22) | Minor | Chip lọc trạng thái đơn hàng hiển thị tiếng Anh | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-23](storefront/loi.md#sf-23) | Minor | Breadcrumb chồng chữ trên điện thoại | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-24](storefront/loi.md#sf-24) | Minor | Khách chưa đăng nhập thấy trạng thái rỗng của đơn hàng và thông báo | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-25](storefront/loi.md#sf-25) | Minor | Menu phụ điện thoại bị chật và cắt chữ | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại | 9 trang chính không cuộn ngang ở 375px |
| [SF-26](storefront/loi.md#sf-26) | Minor | Đường dẫn không tồn tại hiển thị trang 404 mặc định | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-27](storefront/loi.md#sf-27) | Minor | Nhiều trang dùng chung tiêu đề tab | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-30](storefront/loi.md#sf-30) | Minor | Đăng nhập sai nhiều lần không bị giới hạn | backend PR #140 (`e06e334`) | Chưa xác nhận lại | Gateway giới hạn theo IP và email. Khi Redis lỗi, Gateway cho request đi qua. |
| [BO-04](backoffice/loi.md#bo-04) | Minor | Form tạo khuyến mãi báo lỗi chung và mất dữ liệu | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Báo lỗi tại từng ô, không gửi request khi chưa hợp lệ |
| [BO-06](backoffice/loi.md#bo-06) | Minor | Form sách và đơn mua không chỉ ra trường quá dài | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Kiểm trên form sách; đơn mua kiểm ở lần trước |
| [BO-12](backoffice/loi.md#bo-12) | Minor | Điều hướng Admin làm mất tiền tố /admin, mất phiên | backoffice PR #369 (merge `fe73d47f`, BUG-001) | Chưa xác nhận lại | Sửa ở lớp bảo vệ `proxy.ts`: đường dẫn thường được chuyển về `/admin/<console>/…`; chưa chạy lại trên giao diện |

## Đã đóng hoặc chấp nhận

| # | Mức độ | Lỗi | Kết luận | Lý do |
|---|---|---|---|---|
| [BO-05](backoffice/loi.md#bo-05) | Minor | Ô giá tự bỏ dấu trừ, lưu -1 thành 1 | Chấp nhận | Người dùng xác nhận ngày 2026-11-12 là hợp lý; chưa kiểm tra lưu sau chuẩn hóa |
| [SF-16](storefront/loi.md#sf-16) | Minor | Mật khẩu 5 ký tự vẫn được gửi lên API khi đăng nhập | Đã đóng | Đúng thiết kế: form đăng nhập không được nêu quy tắc mật khẩu |
| [SF-36](storefront/loi.md#sf-36) | Minor | Hủy đơn không hoàn lượt mã | Đã đóng | Đúng quy tắc: khách tự hủy thì không hoàn (hệ thống và nhân viên hủy thì hoàn, xem SF-38) |

## Cập nhật bảng này

Khi một lỗi đổi trạng thái, chuyển dòng của nó giữa ba bảng ở trên, cập nhật các con số ở phần Tóm tắt, rồi sửa trạng thái trong `loi.md` tương ứng. Kết quả test từng đợt nằm ở file Excel `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`.

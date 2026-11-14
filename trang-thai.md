# Theo dõi lỗi: đã sửa và chưa sửa

Cập nhật ngày 2026-11-14. Đây là bảng tóm tắt để xem nhanh; chi tiết từng lỗi nằm ở [storefront/loi.md](storefront/loi.md) và [backoffice/loi.md](backoffice/loi.md), kế hoạch sửa ở [fix-plans](fix-plans/).

## Tóm tắt

| Trạng thái | Số lỗi | Trong đó Major |
|---|---|---|
| **Chưa sửa** | 26 | 5 |
| **Đã sửa** | 26 | 8 |
| **Đã đóng hoặc chấp nhận** | 3 | 0 |
| **Tổng** | 55 | 13 |

Trong 26 lỗi đã sửa: 11 lỗi đã được retest xác nhận ngày 2026-11-14, 2 lỗi mới sửa ở `dev.ps1` chưa commit, phần còn lại chưa retest lại.

Cách đọc cột **Retest**: *Đã xác nhận* là chạy lại và thấy đã hết lỗi. *Chưa xác nhận lại* là code đã sửa nhưng chưa chạy lại. *Còn lỗi* là chạy lại và vẫn tái hiện. *Cần xác nhận* là chưa rõ đúng hay sai theo nghiệp vụ.

## Chưa sửa

Xếp theo mức độ, Major trước.

| # | Mức độ | Lỗi | Nơi cần sửa | Retest | Kế hoạch | Ghi chú |
|---|---|---|---|---|---|---|
| [SF-06](storefront/loi.md#sf-06) | Major | Email xác thực đến không ổn định | hạ tầng / backend | Không tái hiện | [kế hoạch](fix-plans/platform/SF-06-verify-email-delivery-unreliable.md) | 1 lần đăng ký nhận 1 email, đến sau khoảng 30 giây |
| [SF-09](storefront/loi.md#sf-09) | Major | Link trong email xác thực trỏ tới địa chỉ giả | notification-service (cấu hình link) | Còn lỗi | [kế hoạch](fix-plans/backend-platform/SF-09-verify-email-link-fake-domain.md) |  |
| [SF-37](storefront/loi.md#sf-37) | Major | Đặt hàng đồng thời tạo nhiều đơn từ một giỏ | backend, order-service và storefront | Còn lỗi | [kế hoạch](fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) | 10 request cùng lúc ra 10 đơn |
| [SF-38](storefront/loi.md#sf-38) | Major | Mã giảm giá được cấp vượt số lượt | backend, order-service và promotion-service | Còn lỗi | [kế hoạch](fix-plans/backend/SF-38-promotion-usage-over-redeemed.md) | Đã chốt quy tắc hoàn lượt (phương án B) |
| [SF-40](storefront/loi.md#sf-40) | Major | Đổi trả đồng thời tạo nhiều yêu cầu cho một cuốn | backend, order-service và storefront | Còn lỗi | [kế hoạch](fix-plans/backend/SF-40-return-concurrent-duplicate-requests.md) | 5 yêu cầu RECEIVED cho 1 cuốn, mỗi yêu cầu hoàn toàn bộ tiền đơn |
| [SF-28](storefront/loi.md#sf-28) | Minor | Tham số sai kiểu trả 500 thay vì 400 hoặc 404 | backend, nhiều service | Còn lỗi | chưa có |  |
| [SF-29](storefront/loi.md#sf-29) | Minor | Body JSON hỏng hoặc enum sai trả 500 | backend, order-service và promotion-service | Còn lỗi | chưa có |  |
| [SF-30](storefront/loi.md#sf-30) | Minor | Đăng nhập sai nhiều lần không bị giới hạn | backend, identity-service hoặc gateway | Còn lỗi | chưa có | Nên cân nhắc nâng mức trước khi lên môi trường thật |
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
| [BO-08](backoffice/loi.md#bo-08) | Minor | Mã khuyến mãi không kiểm định dạng và độ dài | backend, promotion-service | Còn lỗi | chưa có |  |
| [BO-09](backoffice/loi.md#bo-09) | Minor | Tìm kiếm khuyến mãi trả 500 | backend, promotion-service | Còn lỗi | chưa có |  |
| [BO-10](backoffice/loi.md#bo-10) | Minor | Nhà cung cấp trùng khi tạo đồng thời | backend, inventory-service | Còn lỗi | chưa có |  |
| [BO-11](backoffice/loi.md#bo-11) | Minor | Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời | backend, inventory-service | Còn lỗi | chưa có | Chỉ một phiếu nhận được hàng |
| [BO-12](backoffice/loi.md#bo-12) | Minor | Điều hướng Admin làm mất tiền tố /admin, mất phiên | backoffice | Còn lỗi | chưa có | Chưa có kế hoạch. Mức độ tạm đặt Minor, có thể nâng |

## Đã sửa

| # | Mức độ | Lỗi | Đã sửa ở | Retest | Ghi chú |
|---|---|---|---|---|---|
| [SF-01](storefront/loi.md#sf-01) | Major | Proxy chuyển tiếp header Origin nên gateway trả 403 | storefront PR #77 (`b3444b9`) | Đã xác nhận | Gọi thẳng gateway với Origin :3003 vẫn 403, cần đặt `CORS_ALLOWED_ORIGINS` |
| [SF-02](storefront/loi.md#sf-02) | Major | Số điện thoại sai được lưu ở địa chỉ, đặt hàng lỗi 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-03](storefront/loi.md#sf-03) | Major | order-service không ghi log khi trả lỗi | backend PR #117 (`e090ed4`) | Chưa xác nhận | Đã có trong code và unit test; chưa đọc log của service đang chạy |
| [SF-04](storefront/loi.md#sf-04) | Major | notification-service không khởi động vì thiếu biến Mongo | backend `dev.ps1` **chưa commit** | Đã xác nhận | Máy khác chạy vẫn gặp lỗi cũ cho đến khi commit `dev.ps1` |
| [SF-05](storefront/loi.md#sf-05) | Major | Nhấn F5 mất phiên đăng nhập và giỏ hàng | storefront PR #77 (`b3444b9`) | Đã xác nhận |  |
| [SF-07](storefront/loi.md#sf-07) | Major | Khởi tạo thanh toán VNPay trả 500 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Đã tới cổng sandbox và nhánh hủy; chưa test thanh toán thành công bằng thẻ |
| [SF-08](storefront/loi.md#sf-08) | Major | Đặt hàng có mã khuyến mãi trả 400 | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Một phần của lỗi vẫn còn ở SF-38 (cấp mã vượt lượt khi đồng thời) |
| [SF-10](storefront/loi.md#sf-10) | Major | Địa chỉ chấp nhận ký tự đặc biệt, rồi đặt hàng lỗi | backend PR #117 (`e090ed4`) và storefront PR #78 (`cdb599a`) | Đã xác nhận | Kiểm bằng API |
| [SF-11](storefront/loi.md#sf-11) | Minor | Mọi lỗi 403 khi đăng nhập đều báo chưa xác thực email | storefront PR #77 (`b3444b9`) | Chưa xác nhận lại |  |
| [SF-12](storefront/loi.md#sf-12) | Minor | Gợi ý sách và sự kiện hành vi lỗi 500 | backend `dev.ps1` **chưa commit** (người dùng xác nhận) | Đã xác nhận | Trang chủ gọi `/recommendations/trending` trả 200 |
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
| [BO-04](backoffice/loi.md#bo-04) | Minor | Form tạo khuyến mãi báo lỗi chung và mất dữ liệu | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Báo lỗi tại từng ô, không gửi request khi chưa hợp lệ |
| [BO-06](backoffice/loi.md#bo-06) | Minor | Form sách và đơn mua không chỉ ra trường quá dài | backoffice PR #367 (`8bc1ee53`) | Đã xác nhận | Kiểm trên form sách; đơn mua kiểm ở lần trước |

## Đã đóng hoặc chấp nhận

| # | Mức độ | Lỗi | Kết luận | Lý do |
|---|---|---|---|---|
| [BO-05](backoffice/loi.md#bo-05) | Minor | Ô giá tự bỏ dấu trừ, lưu -1 thành 1 | Chấp nhận | Người dùng xác nhận ngày 2026-11-12 là hợp lý; chưa kiểm tra lưu sau chuẩn hóa |
| [SF-16](storefront/loi.md#sf-16) | Minor | Mật khẩu 5 ký tự vẫn được gửi lên API khi đăng nhập | Đã đóng | Đúng thiết kế: form đăng nhập không được nêu quy tắc mật khẩu |
| [SF-36](storefront/loi.md#sf-36) | Minor | Hủy đơn không hoàn lượt mã | Đã đóng | Đúng quy tắc: khách tự hủy thì không hoàn (hệ thống và nhân viên hủy thì hoàn, xem SF-38) |

## Cập nhật bảng này

Khi một lỗi đổi trạng thái, chuyển dòng của nó giữa ba bảng ở trên, cập nhật các con số ở phần Tóm tắt, rồi sửa trạng thái trong `loi.md` tương ứng. Kết quả test từng đợt nằm ở file Excel `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`.

# Lỗi hiện tại

Mỗi lỗi gồm: trạng thái theo dõi (từ bảng trạng thái), rồi hồ sơ lỗi nguyên văn (bước tái hiện, mong đợi, thực tế, API response, ảnh). Link trong file đã chỉnh để mở đúng từ thư mục gốc của repo.

## Mục lục

Chia hai loại. **Logic**: quy tắc nghiệp vụ, dữ liệu, API, đồng thời, cấu hình, điều hướng. **Giao diện**: bố cục, hiển thị, chữ, bản dịch, thao tác trên màn hình, và lời hướng dẫn Guide me khác với màn hình. Phân loại khai báo trong `UI_CODES` của script.

### Lỗi logic (31)

| Mã | Mức độ | Nhóm | Lỗi |
| --- | --- | --- | --- |
| [BO-13](#bo-13) | Major | Cần sửa | Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu |
| [BO-14](#bo-14) | Major | Cần sửa | Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500 |
| [BO-15](#bo-15) | Major | Cần sửa | API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động |
| [BO-16](#bo-16) | Major | Cần sửa | Duyệt trả kho cho sách chưa có lô không cộng tồn |
| [BO-24](#bo-24) | Major | Cần sửa | Admin mất 2 quyền chuyển khoản SePay trên DB dùng chung |
| [SF-04](#sf-04) | Major | Cần sửa | notification-service không khởi động vì thiếu biến Mongo |
| [SF-09](#sf-09) | Major | Cần sửa | Link trong email xác thực trỏ tới địa chỉ giả |
| [SF-37](#sf-37) | Major | Cần sửa | Đặt hàng đồng thời tạo nhiều đơn từ một giỏ |
| [SF-38](#sf-38) | Major | Cần sửa | Mã giảm giá được cấp vượt số lượt |
| [SF-45](#sf-45) | Major | Cần sửa | Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ |
| [SF-46](#sf-46) | Major | Cần sửa | Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0 |
| [SF-47](#sf-47) | Major | Cần sửa | Role USER không còn trên DB dùng chung: đăng ký mới sẽ lỗi |
| [BO-02](#bo-02) | Minor | Cần sửa | Duyệt khuyến mãi trả updatedAt cũ |
| [BO-08](#bo-08) | Minor | Cần sửa | Mã khuyến mãi không kiểm định dạng và độ dài |
| [BO-09](#bo-09) | Minor | Cần sửa | Tìm kiếm khuyến mãi trả 500 |
| [BO-10](#bo-10) | Minor | Cần sửa | Nhà cung cấp trùng khi tạo đồng thời |
| [BO-11](#bo-11) | Minor | Cần sửa | Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời |
| [BO-26](#bo-26) | Minor | Cần sửa | Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn |
| [SF-28](#sf-28) | Minor | Cần sửa | Tham số sai kiểu trả 500 thay vì 400 hoặc 404 |
| [SF-29](#sf-29) | Minor | Cần sửa | Body JSON hỏng hoặc enum sai trả 500 |
| [SF-31](#sf-31) | Minor | Cần sửa | Tên hồ sơ nhận ký tự đặc biệt như `<script>` |
| [SF-35](#sf-35) | Minor | Cần sửa | Tồn kho hiển thị cũ do cache catalog |
| [SF-39](#sf-39) | Minor | Cần sửa | Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối |
| [SF-41](#sf-41) | Minor | Cần sửa | Request trùng đồng thời trả 500 thay vì 409 |
| [SF-42](#sf-42) | Minor | Cần sửa | Giỏ hàng mất cập nhật khi thêm đồng thời |
| [SF-43](#sf-43) | Minor | Cần sửa | Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán |
| [SF-06](#sf-06) | Major | Cần xác nhận | Email xác thực đến không ổn định |
| [SF-44](#sf-44) | Major | Cần xác nhận | Mất event thì đơn có thể kẹt PENDING |
| [BO-03](#bo-03) | Minor | Cần xác nhận | Khuyến mãi quá hạn vẫn hiện Active hoặc Pending |
| [SF-33](#sf-33) | Minor | Cần xác nhận | Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được |
| [SF-34](#sf-34) | Minor | Cần xác nhận | Ô mã khuyến mãi phân biệt hoa thường |

### Lỗi giao diện (18)

| Mã | Mức độ | Nhóm | Lỗi |
| --- | --- | --- | --- |
| [UI-01](#ui-01) | Major | Cần sửa | Sidebar chiếm chỗ nội dung ở 375 px |
| [BO-01](#bo-01) | Minor | Cần sửa | Hộp Guided tasks trống phủ lên trang không có quyền |
| [BO-07](#bo-07) | Minor | Cần sửa | Dòng hàng của đơn mua phải cuộn ngang ở 1024px |
| [BO-17](#bo-17) | Minor | Cần sửa | Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có |
| [BO-18](#bo-18) | Minor | Cần sửa | Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi |
| [BO-20](#bo-20) | Minor | Cần sửa | Guide me nói tiền đã hoàn ngay khi bấm Đã nhận |
| [BO-22](#bo-22) | Minor | Cần sửa | Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập |
| [BO-23](#bo-23) | Minor | Cần sửa | Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng |
| [BO-25](#bo-25) | Minor | Cần sửa | Khách đăng nhập ứng dụng quản trị không được báo vì sao bị từ chối |
| [SF-13](#sf-13) | Minor | Cần sửa | Giao diện hiện thương hiệu Taschen thay vì Velora |
| [SF-14](#sf-14) | Minor | Cần sửa | Tiêu đề tab là Book Store và trạng thái đơn hiện mã tiếng Anh |
| [SF-27](#sf-27) | Minor | Cần sửa | Nhiều trang dùng chung tiêu đề tab |
| [SF-32](#sf-32) | Minor | Cần sửa | Nút Đã nhận hàng không hỏi xác nhận |
| [UI-02](#ui-02) | Minor | Cần sửa | Header tràn ngang và cắt nút Tài khoản ở 320 px |
| [UI-03](#ui-03) | Minor | Cần sửa | Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt |
| [UI-04](#ui-04) | Minor | Cần sửa | Ngày trên Promotions và Orders khác định dạng |
| [BO-19](#bo-19) | Minor | Cần xác nhận | Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới |
| [BO-21](#bo-21) | Minor | Cần xác nhận | Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn |

## Cần sửa

### BO-13

**Nhiều phiếu trả về kho cho cùng RMA, số lượng không được đối chiếu**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | inventory-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-13-return-warehouse-duplicate-rma.md) |
| Ghi chú | Khách trả 1 cuốn, duyệt hai phiếu làm tồn tăng 14 → 16. API cũng cho tạo phiếu khai 50 cuốn. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B01). **Retest 2026-11-27: đã xác nhận.** Danh sách → mở đơn → tải lại → mở đơn APPROVED → Mark ordered: URL giữ /admin/warehouse và phiên Admin ở mọi bước (:3001/admin/warehouse/purchase-orders \| :3001/admin/warehouse/purchase-orders/PO-20261127-000051 \| :3001/admin/warehouse/purchase-orders/PO-20261127-000051 \| :3001/admin/warehouse/purchase-orders/PO-20261127-000045 \| :3001/admin/warehouse/purchase-orders). Bấm Mark ordered cho PO-20261127-000045; trạng thái sau: ORDERED. Xem [bằng chứng](test-2026-11-27/retest/README.md#bo-12). |
| **Luồng** | Trả hàng → trả về kho |
| **Endpoint / Màn hình** | POST /api/v1/inventory/return-to-warehouse · PATCH .../{id}/approve |
| **Nghi ngờ thuộc** | inventory-service (bảng chống trùng processed_order_returns đã bị xoá ở migration V12) |
| **Bước tái hiện** | 1. Khách trả 1 cuốn Sapiens (RMA-20261127-000064), Seller duyệt và bấm Đã nhận<br>2. Seller lập phiếu trả về kho 1 cuốn (RTW-...066)<br>3. Seller lập thêm phiếu thứ hai cho cùng yêu cầu (RTW-...067) và phiếu khai 50 cuốn (RTW-...068)<br>4. Warehouse duyệt RTW-066 rồi RTW-067 |
| **Mong đợi** | Chỉ một phiếu trả về kho cho mỗi yêu cầu trả hàng, số lượng không vượt số khách trả; tồn tăng đúng 1 |
| **Thực tế** | Cả ba phiếu đều tạo được (201). Duyệt hai phiếu: tồn bìa mềm 14 → 15 → 16, tức cộng 2 cuốn cho 1 cuốn khách trả. Phiếu 50 cuốn cũng duyệt được nếu Warehouse không để ý |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-07, GM06-08, GM11-04 ([B01](test-2026-11-27/guide-me/loi.md#b01)). Response đầy đủ: [GM06-07](test-2026-11-27/guide-me/api/GM06-07.txt), [GM06-08](test-2026-11-27/guide-me/api/GM06-08.txt), [GM11-04](test-2026-11-27/guide-me/api/GM11-04.txt) |
| **API Response** | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Khách trả 1 cuốn, sách còn nguyên seal, đưa lại lên kệ",<br>  "items": [<br>    {<br>      "bookId": 67,<br>      "variantId": 1,<br>      "quantity": 1<br>    }<br>  ],<br>  "returnRequestId": 64,<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-13-1.png](images/BO-13-1.png)<br>[BO-13-2.png](images/BO-13-2.png) |

### BO-14

**Giá nhập bằng 0 khi tạo đơn mua trả HTTP 500**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | inventory-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-14-purchase-order-zero-import-price.md) |
| Ghi chú | Request chấp nhận 0, lớp lưu yêu cầu giá lớn hơn 0. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B05). |
| **Luồng** | Đơn mua |
| **Endpoint / Màn hình** | POST /api/v1/purchase-orders/from-stock-request |
| **Nghi ngờ thuộc** | inventory-service |
| **Bước tái hiện** | 1. Yêu cầu nhập đã duyệt<br>2. Lên đơn mua với importPrice = 0 |
| **Mong đợi** | 400 với thông báo rõ (hoặc chấp nhận nếu nghiệp vụ cho phép) |
| **Thực tế** | 500 INTERNAL_ERROR. Log: request cho phép &gt;= 0 nhưng entity PurchaseOrderItem yêu cầu &gt; 0, lỗi bung ra lúc lưu DB |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM09-12 ([B05](test-2026-11-27/guide-me/loi.md#b05)). Response đầy đủ: [GM09-12](test-2026-11-27/guide-me/api/GM09-12.txt) |
| **API Response** | <pre>POST /api/v1/purchase-orders/from-stock-request<br>Request body:<br>{<br>  "stockRequestId": 17,<br>  "supplierId": 36,<br>  "importPrice": 0,<br>  "note": "Hàng tặng kèm"<br>}<br>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-14-1.png](images/BO-14-1.png) |

### BO-15

**API tạo được đơn mua với nhà cung cấp đã ngừng hoạt động**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | inventory-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-15-purchase-order-inactive-supplier.md) |
| Ghi chú | Ô chọn trên UI đã ẩn nhà cung cấp, API vẫn trả 201. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B06). |
| **Luồng** | Nhà cung cấp → Đơn mua |
| **Endpoint / Màn hình** | POST /api/v1/purchase-orders |
| **Nghi ngờ thuộc** | inventory-service |
| **Bước tái hiện** | 1. Admin ngừng hoạt động "Công ty Cổ phần Văn hóa Phương Đông"<br>2. Gọi tạo đơn mua với supplierId đó |
| **Mong đợi** | Bị từ chối (nhà cung cấp ngừng hoạt động không dùng được) |
| **Thực tế** | 201, đơn mua được tạo. Giao diện ẩn nhà cung cấp khỏi danh sách chọn nhưng API không kiểm |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM07-03 ([B06](test-2026-11-27/guide-me/loi.md#b06)). Response đầy đủ: [GM07-03](test-2026-11-27/guide-me/api/GM07-03.txt) |
| **API Response** | <pre>DELETE /api/v1/suppliers/38<br>HTTP 204<br>{}<br><br>POST /api/v1/purchase-orders<br>Request body:<br>{<br>  "supplierId": 38,<br>  "note": "Đặt bổ sung tháng 12",<br>  "items": [<br>    {<br>      "bookId": 1,<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-15-1.png](images/BO-15-1.png) |

### BO-16

**Duyệt trả kho cho sách chưa có lô không cộng tồn**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | inventory-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-16-return-warehouse-missing-batch.md) |
| Ghi chú | Phiếu chuyển APPROVED, tồn vẫn bằng 0. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B07). |
| **Luồng** | Duyệt trả về kho |
| **Endpoint / Màn hình** | PATCH /api/v1/inventory/return-to-warehouse/{id}/approve |
| **Nghi ngờ thuộc** | inventory-service (BatchServiceImpl.restockReturnedUnits) |
| **Bước tái hiện** | 1. Seller lập phiếu trả về kho 1 cuốn "Tuổi Trẻ Đáng Giá Bao Nhiêu" (chưa từng nhập lô)<br>2. Warehouse duyệt |
| **Mong đợi** | Báo lỗi hoặc tạo lô mới; không được báo thành công khi tồn không đổi |
| **Thực tế** | 200 APPROVED, tồn kho sau duyệt vẫn 0 (code chỉ ghi log cảnh báo rồi bỏ qua) |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM11-03 ([B07](test-2026-11-27/guide-me/loi.md#b07)). Response đầy đủ: [GM11-03](test-2026-11-27/guide-me/api/GM11-03.txt) |
| **API Response** | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Khách trả cuốn sách chưa từng nhập kho qua phiếu nhập",<br>  "items": [<br>    {<br>      "bookId": 70,<br>      "variantId": 1,<br>      "quantity": 1<br>    }<br>  ],<br>  "returnRequestId": 64<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-16-1.png](images/BO-16-1.png) |

### BO-24

**Admin mất 2 quyền chuyển khoản SePay trên DB dùng chung**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | DB dùng chung (identity) |
| Kết quả gần nhất | Tái hiện ngày 27/11 |
| Kế hoạch / bằng chứng | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#31-admin-bị-chặn-ở-chức-năng-của-chính-mình) |
| Ghi chú | Chạy lại seed V18; không phải lỗi code |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test phân quyền, mã trong đợt: P2). |
| **Luồng** | Tài chính (Admin) |
| **Endpoint / Màn hình** | POST /api/v1/payments/transfers/{sepayId}/apply · POST /api/v1/payments/transfers/{sepayId}/refunds |
| **Nghi ngờ thuộc** | DB dùng chung (identity, ma trận quyền), không phải lỗi code |
| **Bước tái hiện** | 1. Đăng nhập Admin<br>2. Gọi POST /payments/transfers/{id}/apply hoặc /refunds (id bất kỳ) |
| **Mong đợi** | Qua được gateway (400/404 với id không tồn tại); quyền PAYMENT_TRANSFER_APPLY, PAYMENT_UNAPPLIED_REFUND được seed ở V18 |
| **Thực tế** | Gateway trả 403 "no granting permission". GET /api/v1/permissions không có hai quyền này; Admin không áp được chuyển khoản vào đơn, không hoàn được khoản chuyển nhầm |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, phần phân quyền ([P2](test-2026-11-27/phan-quyen/README.md#31-admin-bị-chặn-ở-chức-năng-của-chính-mình)), [results.json](test-2026-11-27/phan-quyen/data/results.json) |
| **API Response** | <pre>POST /api/v1/payments/transfers/999999999/apply<br>HTTP 403<br>{ "code": "FORBIDDEN", "message": "You do not have permission to perform this action" }</pre> |
| **Ảnh bằng chứng** | Không có |

### SF-04

**notification-service không khởi động vì thiếu biến Mongo**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | taschen-platform (docker-compose) |
| Kết quả gần nhất | Retest 27/11: xác nhận một phần |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/backend-platform/SF-04-dev-script-notification-missing-mongo-env.md) · [bằng chứng](test-2026-11-27/retest/README.md#sf-04) |
| Ghi chú | Còn: Docker Compose vẫn truyền `MONGO_URI` cho notification-service, service đọc `NOTIFICATION_MONGO_URI`; dev.ps1 đã đúng. Bản sửa đã có: backend `dev.ps1` trên `develop` |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa theo xác nhận của người dùng ngày 2026-11-12; chưa đối chiếu commit/PR, chưa kiểm thử lại trong lần cập nhật này. Xem [kế hoạch](fix-plans/backend-platform/SF-04-dev-script-notification-missing-mongo-env.md). Bước tái hiện, response và ảnh dưới đây là bằng chứng trước khi sửa. **Retest 2026-11-27: xác nhận một phần.** Chạy native với biến như dev.ps1 (NOTIFICATION_MONGO_URI): service khởi động (có), health UP. Docker Compose vẫn truyền MONGO_URI cho notification-service (service đọc NOTIFICATION_MONGO_URI), chưa chạy Compose. Xem [bằng chứng](test-2026-11-27/retest/README.md#sf-04). |
| **Luồng** | Khởi động môi trường |
| **Endpoint / Màn hình** | taschen-backend/dev.ps1 |
| **Nghi ngờ thuộc** | backend (dev.ps1) |
| **Bước tái hiện** | Chạy ./dev.ps1 start |
| **Mong đợi** | notification-service chạy với Mongo trong taschen-platform/.env |
| **Thực tế** | Crash: kết nối localhost:27017. dev.ps1 chỉ đặt MONGO_URI, service đọc NOTIFICATION_MONGO_URI |
| **Bằng chứng (status/body)** | MongoSocketOpenException, Application run failed |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-04-1.png](images/SF-04-1.png) |

### SF-09

**Link trong email xác thực trỏ tới địa chỉ giả**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | notification-service (cấu hình link) |
| Kết quả gần nhất | Còn lỗi ở lần retest trước |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend-platform/SF-09-verify-email-link-fake-domain.md) |
| Ghi chú | Khi chạy native, `dev.ps1` chưa truyền `VERIFY_URL_PREFIX`, nên thiếu cấu hình sẽ dùng `api.taschen.example`. Compose có giá trị riêng. Chưa kiểm link trên môi trường triển khai. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Luồng** | 1 - Xác thực email |
| **Endpoint / Màn hình** | Email xác thực · notification-service |
| **Nghi ngờ thuộc** | notification-service (cấu hình link) |
| **Bước tái hiện** | 1. Đăng ký<br>2. Mở email trong Mailpit, bấm liên kết |
| **Mong đợi** | Liên kết mở được hệ thống đang chạy |
| **Thực tế** | Liên kết trỏ tới https://api.taschen.example/... là địa chỉ giả, không mở được. Phải dùng mã trong email |
| **Bằng chứng (status/body)** | Nội dung email trong Mailpit |
| **API Response** | <pre>GET /auth/verify qua proxy local<br>HTTP 200<br>{<br>  "success": true,<br>  "data": null,<br>  "message": "OK"<br>}</pre> |
| **Ảnh bằng chứng** | [SF-09-1.jpg](images/SF-09-1.jpg) |

### SF-37

**Đặt hàng đồng thời tạo nhiều đơn từ một giỏ**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | backend, order-service và storefront |
| Kết quả gần nhất | Còn lỗi ở lần retest trước |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) |
| Ghi chú | 10 request cùng lúc ra 10 đơn. Code hiện tại vẫn đọc giỏ, lưu đơn rồi mới xóa giỏ. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. Xem [kế hoạch](fix-plans/storefront-backend/SF-37-checkout-concurrent-duplicate-orders.md) |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | POST /api/v1/orders · order-service |
| **Nghi ngờ thuộc** | order-service (không khóa giỏ, không có idempotency key) |
| **Bước tái hiện** | 1. Giỏ có 1 cuốn sách id 4<br>2. Gửi 2, 3 hoặc 10 request POST /orders giống hệt nhau cùng một lúc |
| **Mong đợi** | Chỉ 1 đơn được tạo, tồn kho trừ 1 lần |
| **Thực tế** | Tạo đúng bấy nhiêu đơn (2, 3, 10 đơn), tồn kho bị trừ bấy nhiêu lần (49 xuống 47, 47 xuống 44, 44 xuống 34). Gửi lần lượt thì giỏ được dọn nên không trùng. Click 3 lần trên giao diện thì chỉ có 1 request (giao diện đã chặn) |
| **Bằng chứng (status/body)** | Script chạy request song song. n=2: 201 x2, đơn 40 và 41. n=10: 201 x10, đơn 45 đến 54 |
| **API Response** | <pre>HTTP 201 x10 / mỗi lần một đơn ORD-... khác nhau</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-38

**Mã giảm giá được cấp vượt số lượt**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | backend, order-service và promotion-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-38-promotion-usage-over-redeemed.md) |
| Ghi chú | [B02](test-2026-11-27/guide-me/loi.md#b02): mã còn 1 lượt nhưng hai đơn đều xác nhận và giảm 18.900đ mỗi đơn. Quy tắc hoàn lượt đã chốt theo phương án B. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. Xem [kế hoạch](fix-plans/backend/SF-38-promotion-usage-over-redeemed.md) Retest 2026-11-27 (GM05-12): **còn lỗi**, mã 1 lượt vẫn được 2 đơn đặt cùng lúc dùng (ORD-20261127-000190, 000191). Xem [B02](test-2026-11-27/guide-me/loi.md#b02). |
| **Luồng** | 7 - Khuyến mãi |
| **Endpoint / Màn hình** | POST /api/v1/orders có promotionId · promotion-service |
| **Nghi ngờ thuộc** | order-service / promotion-service |
| **Bước tái hiện** | 1. Mã còn 1 lượt, 2 người cùng đặt COD bằng mã<br>2. Một người, mã còn 3 lượt, bấm đặt 3 lần cùng lúc |
| **Mong đợi** | Chỉ 1 đơn được giảm. Mỗi người chỉ dùng mã 1 lần |
| **Thực tế** | Mã 1 lượt: cả 2 đơn đều giảm 19.300 đ. Mã 3 lượt, một người: cả 3 đơn giảm 19.300 đ, số lượng mã chỉ giảm 3 xuống 2. Số lượng không âm nhưng giảm giá bị cấp quá lượt |
| **Bằng chứng (status/body)** | Đơn 58 và 59 cùng promotionId 47 đều discountAmount 19300; đơn 60, 61, 62 cùng promotionId 48 |
| **API Response** | <pre>HTTP 201 x2 / discountAmount 19300.0 trên cả hai đơn</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-45

**Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | storefront, catalog-service |
| Kết quả gần nhất | Còn lỗi, đã retest UI ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/storefront-backend/SF-45-catalog-image-host-crashes-storefront.md) · [Retest UI](#sf-45) |
| Ghi chú | API nhận URL ảnh, `next/image` từ chối hostname khi render. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B03). |
| **Luồng** | Storefront · Trang chủ |
| **Endpoint / Màn hình** | GET /vi (storefront) · POST /api/v1/books (imageUrl tự do) |
| **Nghi ngờ thuộc** | taschen-storefront (next/image), catalog-service (không kiểm host của imageUrl) |
| **Bước tái hiện** | 1. Có một sách với imageUrl https://x.test/qa.png (sách id 61 "QA-BOOK-20261127", không do đợt này tạo)<br>2. Mở trang chủ storefront (đăng nhập hay không đều vậy) |
| **Mong đợi** | Trang chủ hiển thị bình thường; ảnh lỗi chỉ ảnh hưởng ô của sách đó |
| **Thực tế** | Toàn bộ trang chủ báo "Something broke on our end". next/image: Invalid src prop ... hostname "x.test" is not configured. API tạo sách chấp nhận mọi URL ảnh |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM13-03 ([B03](test-2026-11-27/guide-me/loi.md#b03)). Response đầy đủ: [GM13-03](test-2026-11-27/guide-me/api/GM13-03.txt) |
| **API Response** | <pre>GET /api/v1/banners<br>HTTP 200<br>{<br>  "success": true,<br>  "data": [<br>    {<br>      "id": 1,<br>      "name": "[GM-TEST-11271102] Sale tháng 12",<br>      "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>    }<br>  ],<br>  "message": "OK",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [SF-45-1.png](images/SF-45-1.png)<br>[SF-45-2.png](images/SF-45-2.png) |

#### Ghi chú thêm (ui/loi.md)

[Mã SF-45](#sf-45) tiếp tục theo dõi ảnh lỗi. Kiểm lại ngày 27/11, trang chủ rơi vào màn “Something broke on our end”. Technical details báo `Invalid src prop` với hostname `x.test`. Trên Search, cùng hostname làm một thẻ hiện ảnh hỏng, trong khi danh sách vẫn dùng được. Thêm case Search vào nghiệm thu SF-45. [Trang chủ](ui/evidence/2026-11-27/verify-storefront-vi-375.png) · [Kết quả tìm kiếm](ui/evidence/2026-11-27/storefront-search-en-375-confirmed.png) · [Kế hoạch SF-45](fix-plans/storefront-backend/SF-45-catalog-image-host-crashes-storefront.md)

### SF-46

**Tồn ban đầu của phiên bản hiển thị có hàng dù Inventory bằng 0**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | catalog-service, inventory-service |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-46-variant-stock-initialization.md) |
| Ghi chú | Storefront hiện còn 10, đặt hàng trả 409. Liên quan [SF-35](#sf-35). |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B04). |
| **Luồng** | Phiên bản &amp; giá → Storefront |
| **Endpoint / Màn hình** | POST /api/v1/book-variants (stockQuantity) · POST /api/v1/orders |
| **Nghi ngờ thuộc** | catalog-service (book_variants.stock_quantity tách khỏi inventory) |
| **Bước tái hiện** | 1. Seller thêm phiên bản Bìa cứng với tồn ban đầu 10 cho một sách chưa nhập kho<br>2. Khách xem trang chi tiết và đặt 1 cuốn |
| **Mong đợi** | Storefront không hiện hàng khi kho (inventory) chưa có lô, hoặc ô tồn ban đầu không tồn tại |
| **Thực tế** | Trang chi tiết ghi "Bìa cứng · còn 10", thêm giỏ được (200) nhưng đặt hàng trả 409 "Not enough stock". Inventory báo tổng 0 |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM03-02 ([B04](test-2026-11-27/guide-me/loi.md#b04)). Response đầy đủ: [GM03-02](test-2026-11-27/guide-me/api/GM03-02.txt) |
| **API Response** | <pre>GET /api/v1/books/60<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 60,<br>    "slug": "gm-test-11271102-sach-ton-ao",<br>    "title": "[GM-TEST-11271102] Sách tồn ảo",<br>    "author": "GM Tác giả",<br>    "description": "Sách test của đợt GM-TEST-11271102",<br>    "publicationYear": 2020,<br>    "weightGrams": null,<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [SF-46-1.png](images/SF-46-1.png)<br>[SF-46-2.png](images/SF-46-2.png) |

### SF-47

**Role USER không còn trên DB dùng chung: đăng ký mới sẽ lỗi**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | DB dùng chung (identity) |
| Kết quả gần nhất | Tái hiện ngày 27/11 |
| Kế hoạch / bằng chứng | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#4-phát-hiện) |
| Ghi chú | Chạy lại seed V2 hoặc tìm người đã xoá; không phải lỗi code |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test phân quyền, mã trong đợt: P1). |
| **Luồng** | 1 - Đăng ký, đăng nhập |
| **Endpoint / Màn hình** | POST /api/v1/auth/register · GET /api/v1/roles/code/USER |
| **Nghi ngờ thuộc** | DB dùng chung (identity), không phải lỗi code |
| **Bước tái hiện** | 1. Đăng nhập bằng một tài khoản khách đã có<br>2. Xem claim roles trong token và GET /api/v1/users/me<br>3. Admin gọi GET /api/v1/roles/code/USER |
| **Mong đợi** | Khách có role USER; role USER tồn tại (seed V2__seed_roles.sql) |
| **Thực tế** | Token và /users/me có roles rỗng; GET /roles/code/USER trả 404. AuthServiceImpl.findDefaultRole bắt buộc có role này nên đăng ký mới sẽ báo lỗi. Trên DB còn role lạ QA-ROLE-20261127 không do đợt test tạo |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, phần phân quyền ([P1](test-2026-11-27/phan-quyen/README.md#4-phát-hiện)). Flyway báo schema bản 19, repo chỉ có đến V18 |
| **API Response** | <pre>GET /api/v1/roles/code/USER<br>HTTP 404<br>{ "code": "RESOURCE_NOT_FOUND" }</pre> |
| **Ảnh bằng chứng** | Không có |

### UI-01

**Sidebar chiếm chỗ nội dung ở 375 px**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Major |
| Khu vực | Backoffice |
| Kết quả gần nhất | Tái hiện trên Chromium local |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md) · [Bằng chứng](#ui-01) |
| Ghi chú | Sidebar rộng 290 px. Vùng nội dung chính bắt đầu tại x = 290 và chỉ còn 85 px. Tài liệu rộng 395–476 px trên các màn đo được. |

Hồ sơ lỗi (ui/loi.md):

**Sidebar chiếm chỗ nội dung ở 375 px**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Major |
| Khu vực | Backoffice |
| Bước tái hiện | Mở lần lượt Admin Users, Seller Orders và Warehouse Suppliers trực tiếp ở 375 px với sidebar ở trạng thái mặc định. |
| Thực tế | Sidebar rộng 290 px. Vùng nội dung chính bắt đầu tại x = 290 và chỉ còn 85 px. Tài liệu rộng 395–476 px trên các màn đo được. |
| Mong đợi | Điều hướng, bảng và thao tác chính dùng được ở 375 px. Sidebar desktop vẫn mở và thu gọn được. |
| Bằng chứng | [Ảnh 1](ui/evidence/2026-11-27/cold-admin-admin-accounts-375.png) · [Ảnh 2](ui/evidence/2026-11-27/cold-seller-seller-orders-375.png) · [Ảnh 3](ui/evidence/2026-11-27/cold-warehouse-warehouse-suppliers-375.png) |
| Kế hoạch | [Kế hoạch](fix-plans/backoffice/UI-01-mobile-sidebar-squeezes-content.md) |

### BO-01

**Hộp Guided tasks trống phủ lên trang không có quyền**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backoffice |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md) |
| **Luồng** | 6 - Phân quyền |
| **Endpoint / Màn hình** | /forbidden · console admin |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Đăng nhập seller ở console admin |
| **Mong đợi** | Trang không có quyền hiển thị gọn |
| **Thực tế** | Hộp Guided tasks trống phủ lên trang không có quyền |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [BO-01-1.jpg](images/BO-01-1.jpg) |

### BO-02

**Duyệt khuyến mãi trả updatedAt cũ**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, promotion-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md) |
| **Luồng** | Storefront 7 - Khuyến mãi |
| **Endpoint / Màn hình** | PATCH /promotions/{id}/approve |
| **Nghi ngờ thuộc** | promotion-service |
| **Bước tái hiện** | Admin duyệt khuyến mãi |
| **Mong đợi** | Response của PATCH approve trả updatedAt mới |
| **Thực tế** | Response của PATCH approve trả updatedAt cũ, trùng createdAt. Dữ liệu lưu vẫn đúng: GET /api/promotions sau đó trả updatedAt 03:43:53 |
| **Bằng chứng (status/body)** | Ảnh GET /api/promotions, bản ghi id 27 (MANUAL1110): createdAt 03:41:50, updatedAt 03:43:53. Response approve xem ở cột API Response |
| **API Response** | <pre>HTTP 200<br>{<br>  "id": 27,<br>  "code": "MANUAL1110",<br>  "discountPercent": 10,<br>  "status": "ACTIVE",<br>  "createdByUserId": 96,<br>  "approvedByUserId": 95,<br>  "createdAt": "2026-11-10T03:41:50.714442Z",<br>  "updatedAt": "2026-11-10T03:41:50.714442Z"<br>}<br>(đã rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-02-1.jpg](images/BO-02-1.jpg) |

### BO-07

**Dòng hàng của đơn mua phải cuộn ngang ở 1024px**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backoffice |
| Kết quả gần nhất | Còn lỗi, đã retest UI ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md) · [Retest UI](#bo-07) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md) |
| **Luồng** | 3 - Đơn mua |
| **Endpoint / Màn hình** | Form đơn mua ở màn hình 1024px |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Mở form đơn mua ở chiều rộng 1024px |
| **Mong đợi** | Các ô của dòng hàng đều bấm được |
| **Thực tế** | Dòng hàng phải cuộn ngang, ô Book bị đẩy khỏi tầm nhìn, dễ bấm nhầm ô Format |
| **Bằng chứng (status/body)** | Kiểm tra ở 1024px, bình thường ở 1600px |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [BO-07-1.jpg](images/BO-07-1.jpg) |

#### Ghi chú thêm (ui/loi.md)

[Mã BO-07](#bo-07) tái hiện ở Warehouse → Purchase Orders → New tại 1024 px với sidebar mở. Ô Book bị ép hẹp. Ô Import price và nút xóa dòng có chiều rộng hiển thị bằng 0 trong vùng bị cắt. Hai thao tác hiện đầy đủ ở 1440 px khi đo lại. [Ảnh ở 1024 px](ui/evidence/2026-11-27/cold-warehouse-warehouse-purchase-orders-new-1024.png) · [Kế hoạch BO-07](fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md)

### BO-08

**Mã khuyến mãi không kiểm định dạng và độ dài**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, promotion-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-08-promotion-code-format-length.md) |
| Ghi chú | [BO-26](#bo-26) xác nhận phần định dạng: mã có chữ thường và dấu cách vẫn được lưu. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. Ngày 2026-11-27 (GM05-06): còn lỗi. Phần mã **danh mục** (cùng kiểu lỗi) theo dõi riêng ở [BO-26](#bo-26). |
| **Luồng** | Tạo khuyến mãi |
| **Endpoint / Màn hình** | POST /promotions · form tạo khuyến mãi seller |
| **Nghi ngờ thuộc** | promotion-service |
| **Bước tái hiện** | 1. Tạo mã có khoảng trắng và ký tự &lt;&gt; (A B&lt;&gt;), mã chữ thường, mã 51 ký tự |
| **Mong đợi** | Từ chối mã sai định dạng hoặc quá dài |
| **Thực tế** | 201, lưu mã bất kỳ độ dài và ký tự. Mã có khoảng trắng gõ không được ở ô áp mã |
| **Bằng chứng (status/body)** | Mã A B&lt;&gt; (id 42), lowercase1 (id 43), mã 51 chữ A (id 44) đều 201 |
| **API Response** | <pre>HTTP 201 / { "code": "A B&lt;&gt;", "status": "PENDING" }</pre> |
| **Ảnh bằng chứng** | [BO-08-1.jpg](images/BO-08-1.jpg) |

### BO-09

**Tìm kiếm khuyến mãi trả 500**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, promotion-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-09-promotion-search-http-500.md) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | Khuyến mãi |
| **Endpoint / Màn hình** | GET /promotions/search?keyword= |
| **Nghi ngờ thuộc** | promotion-service |
| **Bước tái hiện** | 1. Admin gọi GET /api/v1/promotions/search?keyword=deep |
| **Mong đợi** | Trả danh sách khớp |
| **Thực tế** | 500 INTERNAL_ERROR (nghi lower(bytea) trong truy vấn khi keyword rỗng hoặc có giá trị) |
| **Bằng chứng (status/body)** | GET /promotions/search?keyword=deep: 500 |
| **API Response** | <pre>HTTP 500 / { "code": "INTERNAL_ERROR" }</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### BO-10

**Nhà cung cấp trùng khi tạo đồng thời**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, inventory-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-10-concurrent-duplicate-suppliers.md) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. |
| **Luồng** | Nhà cung cấp |
| **Endpoint / Màn hình** | POST /api/v1/suppliers |
| **Nghi ngờ thuộc** | inventory-service |
| **Bước tái hiện** | 1. Gửi 5 request tạo nhà cung cấp cùng tên và email cùng lúc |
| **Mong đợi** | 1 nhà cung cấp, các request còn lại 409 |
| **Thực tế** | Tạo cả 5 nhà cung cấp trùng nhau (id 25 đến 29). Gửi lần lượt thì lần 2 bị 409, nên chỉ kiểm ở mức ứng dụng, thiếu ràng buộc duy nhất ở CSDL |
| **Bằng chứng (status/body)** | 201 x5, đã xóa sau khi test |
| **API Response** | <pre>HTTP 201 x5</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### BO-11

**Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, inventory-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-11-concurrent-purchase-order-imports.md) |
| Ghi chú | Chỉ một phiếu nhận được hàng |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. |
| **Luồng** | Đơn mua, nhập kho |
| **Endpoint / Màn hình** | POST /api/v1/inventory/import-stocks |
| **Nghi ngờ thuộc** | inventory-service |
| **Bước tái hiện** | 1. PO đã duyệt và thanh toán<br>2. Gửi 3 request tạo phiếu nhập cùng một PO cùng lúc |
| **Mong đợi** | 1 phiếu nhập cho 1 PO |
| **Thực tế** | Tạo 3 phiếu nhập. Nhận hàng chỉ thành công 1 phiếu (tồn tăng đúng +1), hai phiếu còn lại bị 409. Gửi lần lượt thì lần 2 bị 409 |
| **Bằng chứng (status/body)** | Phiếu nhập 6, 7, 8 cho một PO; chỉ một phiếu nhận được hàng |
| **API Response** | <pre>HTTP 201 x3</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### BO-17

**Guide me mô tả nút bật/tắt và đường dẫn banner mà form không có**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-17-guide-banner-fields.md) |
| Ghi chú | Form và API chỉ có tên và URL ảnh. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B09). |
| **Luồng** | Guide me: Đăng banner |
| **Endpoint / Màn hình** | (giao diện) form banner · BannerRequest |
| **Nghi ngờ thuộc** | taschen-backoffice (guide seller), catalog-service |
| **Bước tái hiện** | Mở form banner (Admin trong ứng dụng Seller) |
| **Mong đợi** | Form có bật/tắt và ô đường dẫn như bước Lưu mô tả |
| **Thực tế** | Form chỉ có Name và Image URL; API cũng chỉ có name, imageUrl |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM04-02 ([B09](test-2026-11-27/guide-me/loi.md#b09)). Response đầy đủ: [GM04-02](test-2026-11-27/guide-me/api/GM04-02.txt) |
| **API Response** | <pre>GET /api/v1/banners/1<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 1,<br>    "name": "[GM-TEST-11271102] Sale tháng 12",<br>    "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>  },<br>  "message": "OK",<br>  "timestamp": "2026-11-27T04:37:46.077658900Z"<br>}<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-17-1.png](images/BO-17-1.png)<br>[BO-17-2.png](images/BO-17-2.png) |

### BO-18

**Guide me ngụ ý có thể bỏ trống số lượt khuyến mãi**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-18-guide-promotion-required-quantity.md) |
| Ghi chú | Số lượt là trường bắt buộc. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B10). |
| **Luồng** | Guide me: Tạo khuyến mãi |
| **Endpoint / Màn hình** | POST /api/v1/promotions (quantity trống) |
| **Nghi ngờ thuộc** | taschen-backoffice (guide seller) |
| **Bước tái hiện** | Bỏ trống số lượt khi tạo khuyến mãi |
| **Mong đợi** | Lời hướng dẫn khớp với hệ thống |
| **Thực tế** | 400 Quantity is required |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM05-05 ([B10](test-2026-11-27/guide-me/loi.md#b10)). Response đầy đủ: [GM05-05](test-2026-11-27/guide-me/api/GM05-05.txt) |
| **API Response** | <pre>POST /api/v1/promotions<br>Request body:<br>{<br>  "name": "Tri ân khách hàng",<br>  "code": "TRIAN2026",<br>  "discountPercent": 5,<br>  "priceOrderActive": 200000,<br>  "startDate": "2026-11-27",<br>  "endDate": "2026-11-28"<br>}<br>HTTP 400<br>{<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-18-1.png](images/BO-18-1.png)<br>[BO-18-2.png](images/BO-18-2.png) |

### BO-20

**Guide me nói tiền đã hoàn ngay khi bấm Đã nhận**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-20-guide-refund-pending-after-received.md) |
| Ghi chú | Đơn ở REFUND_PENDING, khoản hoàn OPEN và chờ ghi nhận chi trả. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B12). |
| **Luồng** | Guide me: Xử lý trả hàng |
| **Endpoint / Màn hình** | PATCH /api/v1/returns/{id}/received |
| **Nghi ngờ thuộc** | taschen-backoffice (guide seller) |
| **Bước tái hiện** | Seller bấm Đã nhận cho yêu cầu đã duyệt |
| **Mong đợi** | Lời hướng dẫn nói rõ còn bước chi trả |
| **Thực tế** | Đơn REFUND_PENDING, khoản hoàn RFD-20261127-000012 OPEN 160.650đ, chưa chi |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-04 ([B12](test-2026-11-27/guide-me/loi.md#b12)). Response đầy đủ: [GM06-04](test-2026-11-27/guide-me/api/GM06-04.txt) |
| **API Response** | <pre>PATCH /api/v1/returns/64/received<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 64,<br>    "returnCode": "RMA-20261127-000064",<br>    "orderId": 184,<br>    "reasonCode": "DEFECTIVE",<br>    "description": "Sách bị rách gáy và bong trang 45 đến 60 ngay khi mở hộp nhận hàng",<br>    "responseNote": "Đồng ý nhận lại, vui lòng gửi hàng về kho Quận 7",<br>    "status": "RECEIVED",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-20-1.png](images/BO-20-1.png) |

### BO-22

**Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-22-guide-stock-request-status.md) |
| Ghi chú | Yêu cầu dừng ở ORDERED, đơn mua mới chuyển RECEIVED. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B14). |
| **Luồng** | Guide me: Yêu cầu nhập hàng |
| **Endpoint / Màn hình** | GET /api/v1/inventory/stock-requests/{id} |
| **Nghi ngờ thuộc** | inventory-service hoặc guide warehouse |
| **Bước tái hiện** | Theo dõi yêu cầu nhập sau khi đơn mua đã nhận đủ |
| **Mong đợi** | Yêu cầu chuyển Đã nhận, hoặc sửa lời hướng dẫn |
| **Thực tế** | Yêu cầu dừng ở ORDERED dù đơn mua RECEIVED |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM08-04 ([B14](test-2026-11-27/guide-me/loi.md#b14)). Response đầy đủ: [GM08-04](test-2026-11-27/guide-me/api/GM08-04.txt) |
| **API Response** | <pre>GET /api/v1/inventory/stock-requests/6<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 6,<br>    "requestCode": "STK-20261127-000022",<br>    "quantity": 20,<br>    "reason": "Còn 2 cuốn trên kệ, mỗi tuần bán khoảng 5 cuốn",<br>    "status": "ORDERED",<br>    "createdAt": "2026-11-27T04:18:10.834603Z",<br>    "processedAt": "2026-11-27T04:18:11.333682Z",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-22-1.png](images/BO-22-1.png) |

### BO-23

**Guide me bỏ qua bước Đánh dấu đã đặt trước khi nhận hàng**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backoffice/BO-23-guide-purchase-order-before-receipt.md) |
| Ghi chú | Đơn APPROVED chưa nhập được. Phải sang ORDERED. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B15). |
| **Luồng** | Guide me: Đơn mua |
| **Endpoint / Màn hình** | POST /api/v1/inventory/import-stocks |
| **Nghi ngờ thuộc** | taschen-backoffice (guide warehouse) |
| **Bước tái hiện** | Admin duyệt đơn mua rồi Warehouse lập phiếu nhập ngay |
| **Mong đợi** | Lời hướng dẫn khớp quy trình |
| **Thực tế** | 409: đơn phải ORDERED mới nhận hàng được (hệ thống đúng, lời hướng dẫn sai) |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM09-03 ([B15](test-2026-11-27/guide-me/loi.md#b15)). Response đầy đủ: [GM09-03](test-2026-11-27/guide-me/api/GM09-03.txt) |
| **API Response** | <pre>POST /api/v1/inventory/import-stocks<br>Request body:<br>{<br>  "supplierId": 36,<br>  "purchaseOrderId": 15,<br>  "details": [<br>    {<br>      "bookId": 67,<br>      "variantId": 1,<br>      "supplierId": 36,<br>      "quantity": 20,<br>      "importPrice": 118000<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-23-1.png](images/BO-23-1.png) |

### BO-25

**Khách đăng nhập ứng dụng quản trị không được báo vì sao bị từ chối**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backoffice |
| Kết quả gần nhất | Tái hiện ngày 27/11 |
| Kế hoạch / bằng chứng | [Bằng chứng](test-2026-11-27/phan-quyen/README.md#21-đăng-nhập-nhầm-ứng-dụng) |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test phân quyền, mã trong đợt: P3). |
| **Luồng** | 6 - Phân quyền |
| **Endpoint / Màn hình** | Trang /signin của admin, seller, warehouse |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | 1. Mở http://localhost:3002/signin<br>2. Đăng nhập bằng tài khoản khách |
| **Mong đợi** | Báo tài khoản không có quyền vào ứng dụng quản trị |
| **Thực tế** | API đăng nhập trả 200, màn hình quay lại form đăng nhập trống, không có thông báo. Lặp lại ở cả 3 ứng dụng |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, phần phân quyền ([P3](test-2026-11-27/phan-quyen/README.md#4-phát-hiện)) |
| **API Response** | Không áp dụng: lỗi giao diện |
| **Ảnh bằng chứng** | [BO-25-1.png](images/BO-25-1.png) |

### BO-26

**Mã danh mục nhận chữ thường và dấu cách, khác hướng dẫn**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | catalog-service, Backoffice |
| Kết quả gần nhất | Còn lỗi ngày 27/11 |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/BO-26-category-code-format.md) |
| Ghi chú | Dòng này theo dõi phần danh mục. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B08). Phần mã khuyến mãi của cùng lỗi thuộc [BO-08](#bo-08). |
| **Luồng** | Guide me: Tạo danh mục |
| **Endpoint / Màn hình** | POST /api/v1/categories · form danh mục |
| **Nghi ngờ thuộc** | catalog-service |
| **Bước tái hiện** | 1. Admin tạo danh mục với mã chữ thường có dấu cách, ví dụ `gm 11271102 ky nang` |
| **Mong đợi** | Từ chối, vì Guide me hướng dẫn mã viết hoa, nối bằng gạch dưới |
| **Thực tế** | 201, mã được lưu nguyên dạng chữ thường và dấu cách |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM01-06 ([B08](test-2026-11-27/guide-me/loi.md#b08)). Response đầy đủ: [GM01-06](test-2026-11-27/guide-me/api/GM01-06.txt) |
| **API Response** | <pre>POST /api/v1/categories<br>Request body:<br>{<br>  "name": "[GM-TEST-11271102] Kỹ năng sống",<br>  "code": "gm 11271102 ky nang"<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 10,<br>    "slug": "gm-test-11271102-ky-nang-song",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-26-1.png](images/BO-26-1.png) |

### SF-13

**Giao diện hiện thương hiệu Taschen thay vì Velora**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | storefront (footer) |
| Kết quả gần nhất | Retest 27/11: xác nhận một phần |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/storefront/SF-13-branding-taschen-instead-of-velora.md) · [bằng chứng](test-2026-11-27/retest/README.md#sf-13) |
| Ghi chú | Còn: Email liên hệ `hello@taschen.vn` ở footer mọi trang. Bản sửa đã có: storefront PR #77 (`b3444b9`) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `278146b`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](fix-plans/storefront/SF-13-branding-taschen-instead-of-velora.md) **Retest 2026-11-27: xác nhận một phần.** Tên thương hiệu và tiêu đề trang Tài khoản đã là Velora ("Velora — Nhà sách trực tuyến"). Còn email liên hệ hello@taschen.vn ở footer mọi trang. Xem [bằng chứng](test-2026-11-27/retest/README.md#sf-13). |
| **Luồng** | Hồ sơ |
| **Endpoint / Màn hình** | /vi/profile |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Mở Tài khoản của tôi |
| **Mong đợi** | Thương hiệu Velora trên toàn bộ giao diện, tiêu đề đúng |
| **Thực tế** | Header, footer và tiêu đề tab ghi "Taschen", trong khi trang hồ sơ ghi "Velora". Tiêu đề "Hồ sơ của tôi" lỗi hiển thị dấu |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-13-1.png](images/SF-13-1.png) |

### SF-14

**Tiêu đề tab là Book Store và trạng thái đơn hiện mã tiếng Anh**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | storefront (tiêu đề trang) |
| Kết quả gần nhất | Retest 27/11: xác nhận một phần |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/storefront/SF-14-tab-title-book-store-english-status.md) · [bằng chứng](test-2026-11-27/retest/README.md#sf-14) |
| Ghi chú | Còn: Trang success và bản /en dùng tiêu đề chung tiếng Việt; tiêu đề trang chủ chờ SF-45. Bản sửa đã có: storefront PR #77 (`b3444b9`) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên `fix/storefront-bugs` (merge `278146b`), đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Xem [kế hoạch](fix-plans/storefront/SF-14-tab-title-book-store-english-status.md) **Retest 2026-11-27: xác nhận một phần.** Trạng thái đơn đã tiếng Việt. Tiêu đề /vi, /vi/success, /en/success đều là tiêu đề chung "Velora — Nhà sách trực tuyến"; /en vẫn tiêu đề tiếng Việt. Trang chủ đang lỗi do SF-45 nên chưa đo được tiêu đề thật của trang chủ. Xem [bằng chứng](test-2026-11-27/retest/README.md#sf-14). |
| **Luồng** | Nhiều trang |
| **Endpoint / Màn hình** | login, cart, orders · chi tiết đơn |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | Xem tiêu đề tab, trạng thái đơn |
| **Mong đợi** | Tiêu đề riêng từng trang, trạng thái tiếng Việt |
| **Thực tế** | Tiêu đề tab là "Book Store". Trạng thái hiện PENDING, UNPAID |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-14-1.jpg](images/SF-14-1.jpg) |

### SF-27

**Nhiều trang dùng chung tiêu đề tab**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | storefront (tiêu đề trang) |
| Kết quả gần nhất | Retest 27/11: còn lỗi |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/storefront/SF-27-pages-share-same-tab-title.md) · [bằng chứng](test-2026-11-27/retest/README.md#sf-27) |
| Ghi chú | Còn: Đăng nhập và đăng ký vẫn dùng tiêu đề chung. Bản sửa đã có: storefront PR #77 (`b3444b9`) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `b771af7` trên `fix/storefront-bugs`; đã vào `origin/develop` qua PR #77 (merge `b3444b9`), kiểm tra Git ngày 2026-11-11. Chưa kiểm thử lại trong đợt cập nhật tài liệu này. Xem [kế hoạch](fix-plans/storefront/SF-27-pages-share-same-tab-title.md). **Retest 2026-11-27: còn lỗi.** /vi/cart = "Giỏ hàng \| Velora"; /vi/orders = "Đơn hàng \| Velora"; /vi/search?q=python = "Tìm kiếm \| Velora"; /vi/login = "Velora — Nhà sách trực tuyến"; /vi/register = "Velora — Nhà sách trực tuyến". Giỏ, đơn hàng, tìm kiếm đã có tiêu đề riêng; đăng nhập và đăng ký vẫn dùng tiêu đề chung. Xem [bằng chứng](test-2026-11-27/retest/README.md#sf-27). |
| **Luồng** | Điều hướng và tiêu đề trang |
| **Endpoint / Màn hình** | /cart, /orders, /search, /login, /register |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở lần lượt giỏ, đơn hàng, tìm kiếm, đăng nhập và đăng ký<br>2. Đọc document.title hoặc dùng await page.title() |
| **Mong đợi** | Mỗi trang có tiêu đề riêng gắn với Velora |
| **Thực tế** | Các trang dùng tiêu đề mặc định chung do không khai báo metadata riêng |
| **Bằng chứng (status/body)** | Không có ảnh và chưa lưu kết quả page.title(). Bằng chứng nguồn: layout locale đặt title chung; commit b771af7 bổ sung 5 layout metadata. Test đơn hàng có assertion toHaveTitle("Đơn hàng &#124; Velora"); chưa chạy lại trong đợt ghi nhận này. |
| **API Response** | Không áp dụng: lỗi giao diện; không dùng HTTP status làm bằng chứng đã sửa. |
| **Ảnh bằng chứng** | Không có; xem bằng chứng nguồn ở kế hoạch, cần bổ sung kết quả page.title(). |

### SF-28

**Tham số sai kiểu trả 500 thay vì 400 hoặc 404**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, nhiều service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-28-invalid-request-parameter-http-status.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | Nhiều luồng |
| **Endpoint / Màn hình** | GET /books/abc, /orders/abc, /users/abc, /promotions/abc, /categories/abc, ?categoryId=abc, ?sort=zzz, /notifications/1 |
| **Nghi ngờ thuộc** | catalog, order, identity, promotion, notification |
| **Bước tái hiện** | 1. Gọi một trong các URL bên cạnh với id hoặc tham số sai kiểu |
| **Mong đợi** | 400 hoặc 404 có mã lỗi rõ ràng |
| **Thực tế** | 500 INTERNAL_ERROR. Chỉ inventory-service xử lý MethodArgumentTypeMismatch và NoResourceFound |
| **Bằng chứng (status/body)** | GET /api/v1/books/abc: 500. /books/5/nonexistent: 500. /books?sort=zzz: 500. /orders/99999999 đúng là 404 |
| **API Response** | <pre>HTTP 500 / { "success": false, "code": "INTERNAL_ERROR", "message": "Something went wrong. Please try again later." }</pre> |
| **Ảnh bằng chứng** | [SF-28-1.jpg](images/SF-28-1.jpg) |

### SF-29

**Body JSON hỏng hoặc enum sai trả 500**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, order-service và promotion-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-29-malformed-json-http-400.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | Nhiều luồng |
| **Endpoint / Màn hình** | POST /orders, POST /carts/me/items, PATCH /orders/{id}/status, POST /returns, POST /promotions |
| **Nghi ngờ thuộc** | order-service, promotion-service (GlobalExceptionHandler) |
| **Bước tái hiện** | 1. Gửi body JSON hỏng, hoặc enum sai (paymentMethod BITCOIN, status FOO, reasonCode FOO), hoặc quantity là chuỗi |
| **Mong đợi** | 400 MALFORMED_REQUEST như identity-service và catalog-service |
| **Thực tế** | 500 INTERNAL_ERROR ở order-service và promotion-service. Số lượng khuyến mãi 2147483648 cũng 500 |
| **Bằng chứng (status/body)** | POST /orders với body { : 500; POST /carts/me/items với quantity "abc": 500; login với body hỏng: 400 MALFORMED_REQUEST |
| **API Response** | <pre>HTTP 500 / { "success": false, "code": "INTERNAL_ERROR" }</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-31

**Tên hồ sơ nhận ký tự đặc biệt như `<script>`**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, identity-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/storefront-backend/SF-31-profile-name-validation.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | Hồ sơ |
| **Endpoint / Màn hình** | PUT /users/me |
| **Nghi ngờ thuộc** | identity-service |
| **Bước tái hiện** | 1. Cập nhật hồ sơ với firstName là &lt;script&gt; |
| **Mong đợi** | Từ chối ký tự đặc biệt như tên người nhận ở địa chỉ |
| **Thực tế** | 200, lưu tên &lt;script&gt;. Địa chỉ thì chặn tên có ký tự đặc biệt, hai nơi không đồng nhất |
| **Bằng chứng (status/body)** | PUT /users/me với firstName &lt;script&gt;: 200 |
| **API Response** | <pre>HTTP 200 / { "success": true, "data": { "firstName": "&lt;script&gt;" } }</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-32

**Nút Đã nhận hàng không hỏi xác nhận**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | storefront |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/storefront/SF-32-confirm-before-marking-order-received.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | 5 - Đơn hàng |
| **Endpoint / Màn hình** | Chi tiết đơn storefront · PATCH /orders/{id}/confirm-received |
| **Nghi ngờ thuộc** | storefront |
| **Bước tái hiện** | 1. Mở đơn ở trạng thái Đang giao<br>2. Bấm Đã nhận hàng |
| **Mong đợi** | Hỏi xác nhận như nút Huỷ đơn |
| **Thực tế** | Đơn chuyển Completed và Đã thanh toán ngay sau một lần bấm, không hỏi |
| **Bằng chứng (status/body)** | Đơn ORD-20261114-000041 |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-35

**Tồn kho hiển thị cũ do cache catalog**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, catalog-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-35-catalog-stock-cache-stale.md) |
| Ghi chú | Inventory báo 49 cuốn, API sách báo 50 |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | GET /books/{id} sau khi đặt đơn |
| **Nghi ngờ thuộc** | catalog-service (cache) |
| **Bước tái hiện** | 1. Đặt đơn 1 cuốn sách id 4 và 5<br>2. Gọi lại GET /books/4 |
| **Mong đợi** | Tồn kho giảm tương ứng |
| **Thực tế** | Tồn vẫn 50 sau khi đặt. Nghi do catalog cache Redis 10 phút không bị xóa khi tồn kho đổi; chưa xác nhận bằng inventory-service |
| **Bằng chứng (status/body)** | GET /books/4 và /books/5 stockQuantity 50 sau khi đặt đơn 520.116 đ |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-39

**Đơn báo thành công rồi tự hủy khi hai người tranh số hàng cuối**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, order-service (và storefront) |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-39-checkout-order-cancelled-after-success.md) |
| Ghi chú | Không bán vượt tồn kho; chỉ trải nghiệm |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. Xem [kế hoạch](fix-plans/backend/SF-39-checkout-order-cancelled-after-success.md) |
| **Luồng** | 3 - Checkout COD |
| **Endpoint / Màn hình** | POST /api/v1/orders · inventory-service |
| **Nghi ngờ thuộc** | order-service (kiểm tra tồn kho đồng bộ nhưng giữ hàng bất đồng bộ qua OrderPlacedEvent) |
| **Bước tái hiện** | 1. Sách id 4 còn 43 cuốn trong inventory-service<br>2. Hai người, mỗi người một giỏ 26 cuốn, đặt cùng lúc |
| **Mong đợi** | Chỉ 1 đơn được nhận; đơn còn lại báo hết hàng ngay khi đặt |
| **Thực tế** | Cả 2 request trả 201 và giao diện báo đặt hàng thành công. Inventory chỉ giữ hàng cho 1 đơn (tồn 43 xuống 17); đơn còn lại tự hủy sau khoảng 0,9 giây (đơn 64: tạo 02:27:11.558, hủy 02:27:12.472) do giữ hàng thất bại. Không bán vượt tồn kho; lỗi là khách được báo thành công rồi đơn bị hủy mà không có lý do |
| **Bằng chứng (status/body)** | Đơn 63 và 64, mỗi đơn 26 cuốn. Đơn 64 bị hệ thống hủy, đơn 63 do mình hủy khi dọn dữ liệu |
| **API Response** | <pre>HTTP 201 x2</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-41

**Request trùng đồng thời trả 500 thay vì 409**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, nhiều service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-41-concurrent-business-conflict-http-409.md) |
| Ghi chú | Dữ liệu đúng, chỉ sai mã trả về |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. |
| **Luồng** | Nhiều luồng |
| **Endpoint / Màn hình** | Hủy đơn, đổi trạng thái, đã nhận hàng, duyệt đổi trả, đăng ký, xác thực email, địa chỉ mặc định, duyệt khuyến mãi |
| **Nghi ngờ thuộc** | order-service, identity-service, promotion-service, inventory-service (GlobalExceptionHandler) |
| **Bước tái hiện** | 1. Gửi 3 đến 5 request giống nhau cùng lúc cho một trong các thao tác bên cạnh |
| **Mong đợi** | 1 request thành công, các request còn lại 409 CONFLICT. Dữ liệu chỉ đổi một lần |
| **Thực tế** | Dữ liệu đổi đúng một lần, nhưng các request còn lại trả 500 INTERNAL_ERROR (4 trên 5, hoặc 2 trên 3). Nghi lỗi khóa lạc quan hoặc ràng buộc duy nhất chưa được xử lý. Cùng nhóm ở backoffice: duyệt khuyến mãi, duyệt và thanh toán đơn mua, nhận hàng nhập kho, duyệt đổi trả |
| **Bằng chứng (status/body)** | Hủy đơn x5: 200 x1, 500 x4. Đăng ký x5: 201 x1, 500 x4. Xác thực x5: 200 x1, 500 x4. Địa chỉ mặc định x3: 201 x1, 500 x2 |
| **API Response** | <pre>HTTP 500 / { "code": "INTERNAL_ERROR" }</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-42

**Giỏ hàng mất cập nhật khi thêm đồng thời**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, order-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-42-concurrent-cart-lost-update.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. |
| **Luồng** | 2 - Giỏ hàng |
| **Endpoint / Màn hình** | POST /api/v1/carts/me/items |
| **Nghi ngờ thuộc** | order-service (cập nhật giỏ không khóa) |
| **Bước tái hiện** | 1. Giỏ trống<br>2. Gửi 5 request thêm cùng một sách, mỗi lần 1 cuốn, cùng lúc |
| **Mong đợi** | Giỏ có 5 cuốn |
| **Thực tế** | Cả 5 request trả 200 nhưng giỏ chỉ có 1 cuốn (mất cập nhật) |
| **Bằng chứng (status/body)** | GET /carts/me sau đó: sách id 4, quantity 1 |
| **API Response** | <pre>HTTP 200 x5</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### SF-43

**Khởi tạo VNPay đồng thời tạo nhiều bản ghi thanh toán**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | backend, payment-service |
| Kết quả gần nhất | Tái hiện |
| Kế hoạch / bằng chứng | [kế hoạch](fix-plans/backend/SF-43-duplicate-active-vnpay-payment.md) |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi test tính bất biến. |
| **Luồng** | 4 - Checkout VNPAY |
| **Endpoint / Màn hình** | POST /api/v1/orders/{id}/payments/initiate |
| **Nghi ngờ thuộc** | payment-service |
| **Bước tái hiện** | 1. Tạo đơn VNPAY<br>2. Gửi 3 request initiate cùng lúc |
| **Mong đợi** | Một bản ghi thanh toán cho một đơn |
| **Thực tế** | Tạo 3 bản ghi PENDING (id 9, 10, 11), nghĩa là có 3 link thanh toán đều trả được. Gửi lần lượt thì dùng lại 1 bản ghi |
| **Bằng chứng (status/body)** | GET /payments/order/{id}: 3 bản ghi PENDING |
| **API Response** | <pre>HTTP 200 x3</pre> |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |

### UI-02

**Header tràn ngang và cắt nút Tài khoản ở 320 px**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Storefront |
| Kết quả gần nhất | Tái hiện trên Chromium local |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/storefront/UI-02-header-account-overflow-320px.md) · [Bằng chứng](#ui-02) |
| Ghi chú | Tài liệu rộng 326 px ở viewport 320 px. Nút Tài khoản nằm từ x = 282 đến x = 326. Ở 375 px, không đo được phần tràn này. |

Hồ sơ lỗi (ui/loi.md):

**Header tràn ngang và cắt nút Tài khoản ở 320 px**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Storefront |
| Bước tái hiện | Mở tìm kiếm, giỏ hàng hoặc đăng nhập ở 320 px và quan sát hàng chứa logo, thông báo, yêu thích, giỏ và tài khoản. |
| Thực tế | Tài liệu rộng 326 px ở viewport 320 px. Nút Tài khoản nằm từ x = 282 đến x = 326. Ở 375 px, không đo được phần tràn này. |
| Mong đợi | Tất cả nút nằm trong viewport và mở được bằng chuột, cảm ứng hoặc bàn phím. |
| Bằng chứng | [Ảnh 1](ui/evidence/2026-11-27/verify-storefront-vi-cart-320.png) |
| Kế hoạch | [Kế hoạch](fix-plans/storefront/UI-02-header-account-overflow-320px.md) |

### UI-03

**Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Storefront |
| Kết quả gần nhất | Tái hiện trên Chromium local |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md) · [Bằng chứng](#ui-03) |
| Ghi chú | Trang có lang=en nhưng tiêu đề, số kết quả, nhãn độ khớp và một số thông báo vẫn dùng tiếng Việt. |

Hồ sơ lỗi (ui/loi.md):

**Trang tìm kiếm tiếng Anh hiển thị nhãn tiếng Việt**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Storefront |
| Bước tái hiện | Mở `/en/search?q=sapiens`, đợi kết quả rồi đối chiếu với `/vi/search?q=sapiens`. |
| Thực tế | Trang có lang=en nhưng tiêu đề, số kết quả, nhãn độ khớp và một số thông báo vẫn dùng tiếng Việt. |
| Mong đợi | Nhãn giao diện theo locale của route. Tên sách và tác giả giữ đúng nội dung danh mục. |
| Bằng chứng | [Ảnh 1](ui/evidence/2026-11-27/storefront-search-en-375-confirmed.png) |
| Kế hoạch | [Kế hoạch](fix-plans/storefront/UI-03-search-english-uses-vietnamese-copy.md) |

### UI-04

**Ngày trên Promotions và Orders khác định dạng**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần sửa |
| Mức độ | Minor |
| Khu vực | Backoffice (Seller) |
| Kết quả gần nhất | Tái hiện trên Chromium local |
| Kế hoạch / bằng chứng | [Kế hoạch](fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md) · [Bằng chứng](#ui-04) |
| Ghi chú | Trong cùng phiên Seller tiếng Anh, Promotions hiển thị 2026-11-27 ở Starts, còn Orders hiển thị 11/11/2026 ở Placed. |

Hồ sơ lỗi (ui/loi.md):

**Ngày trên Promotions và Orders khác định dạng**

| Mục | Nội dung |
| --- | --- |
| Mức độ | Minor |
| Khu vực | Backoffice (Seller) |
| Bước tái hiện | Đăng nhập Seller, mở Promotions và Orders trong cùng phiên, so sánh cách trình bày các cột ngày. |
| Thực tế | Trong cùng phiên Seller tiếng Anh, Promotions hiển thị 2026-11-27 ở Starts, còn Orders hiển thị 11/11/2026 ở Placed. |
| Mong đợi | Hai bảng dùng cùng quy ước theo locale đang hiển thị. Ngày hiệu lực khuyến mãi giữ đúng ngày khi đổi múi giờ. |
| Bằng chứng | [Ảnh 1](ui/evidence/2026-11-27/seller-date-promotions.png) · [Ảnh 2](ui/evidence/2026-11-27/seller-date-orders.png) |
| Kế hoạch | [Kế hoạch](fix-plans/backoffice/UI-04-seller-table-date-format-inconsistent.md) |


## Cần xác nhận

### SF-06

**Email xác thực đến không ổn định**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần xác nhận |
| Mức độ | Major |
| Khu vực | hạ tầng / backend |
| Việc tiếp theo | Chạy nhiều lượt đăng ký và kiểm log gửi email |
| Kế hoạch | [kế hoạch](fix-plans/platform/SF-06-verify-email-delivery-unreliable.md) |
| Ghi chú | Một lần đăng ký nhận email sau khoảng 30 giây. Chưa xác minh độ ổn định của luồng gửi hiện tại. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Luồng** | 1 - Đăng ký |
| **Endpoint / Màn hình** | Mailpit · notification-service |
| **Nghi ngờ thuộc** | backend / hạ tầng |
| **Bước tái hiện** | 1. Đăng ký tài khoản mới<br>2. Mở Mailpit |
| **Mong đợi** | Có email xác thực |
| **Thực tế** | Đăng ký 201 nhưng chỉ 1 trong 4 email đến Mailpit, các email còn lại không thấy. Nghi có consumer khác trên CloudAMQP dùng chung nhận mất, chưa xác nhận |
| **Bằng chứng (status/body)** | Mailpit có 1 thư (tc09@taschen.test) sau 4 lần đăng ký |
| **API Response** | POST /auth/register: 201. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [SF-06-1.jpg](images/SF-06-1.jpg) |

### SF-44

**Mất event thì đơn có thể kẹt PENDING**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần xác nhận |
| Mức độ | Major |
| Khu vực | backend, order-service |
| Việc tiếp theo | Tái hiện mất sự kiện trong môi trường test |
| Kế hoạch | [kế hoạch](fix-plans/backend/SF-44-order-event-lost-stuck-pending.md) |
| Ghi chú | Code gửi sự kiện sau commit và chỉ ghi log khi gửi lỗi. Chưa thấy cơ chế gửi lại hoặc xử lý đơn kẹt cho luồng đặt hàng. |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Chưa tái hiện, phát hiện khi đọc code ngày 2026-11-14. Xem [kế hoạch](fix-plans/backend/SF-44-order-event-lost-stuck-pending.md) |
| **Luồng** | 3 - Checkout COD, 4 - Checkout VNPAY |
| **Endpoint / Màn hình** | EventPublisher · OrderPlacedEvent, StockReservedEvent (RabbitMQ) |
| **Nghi ngờ thuộc** | order-service (gửi event sau commit, không có outbox, không có tác vụ quét) |
| **Bước tái hiện** | 1. Chặn kết nối RabbitMQ của order-service<br>2. Đặt một đơn COD<br>3. Khôi phục kết nối, đợi vài phút |
| **Mong đợi** | Đơn được giữ hàng và xác nhận, hoặc bị hủy sau một thời hạn |
| **Thực tế** | Dự đoán từ code: đơn ở PENDING, stockReserved = false mãi; không giữ hàng, không bị hủy, không ai được báo. Đơn có mã giữ luôn lượt mã |
| **Bằng chứng (status/body)** | `EventPublisher.send` chỉ ghi log khi gửi lỗi; order-service không có outbox, không bật publisher confirm và không có `@Scheduled` (payment-service thì có `PaymentOutboxScheduler`). Ngày 14/11 `GET /orders?status=PENDING` trả 0 đơn, nên chưa có đơn kẹt thật |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | Không có. Chưa tái hiện |

### BO-03

**Khuyến mãi quá hạn vẫn hiện Active hoặc Pending**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần xác nhận |
| Mức độ | Minor |
| Khu vực | seller, promotion-service |
| Việc tiếp theo | Đối chiếu trạng thái trước và sau mốc hết hạn |
| Kế hoạch | [kế hoạch](fix-plans/backoffice/BO-03-promotion-expired-still-active.md) |
| Ghi chú | Chưa xác nhận lại |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](fix-plans/backoffice/BO-03-promotion-expired-still-active.md) |
| **Luồng** | Storefront 7 - Khuyến mãi |
| **Endpoint / Màn hình** | Danh sách khuyến mãi |
| **Nghi ngờ thuộc** | seller / promotion-service |
| **Bước tái hiện** | Xem các khuyến mãi có ngày kết thúc 2026-09-21 |
| **Mong đợi** | Khuyến mãi quá hạn không còn hiện Active |
| **Thực tế** | Vẫn hiện Active và Pending. Cần xác nhận quy tắc hiển thị |
| **Bằng chứng (status/body)** | Bảng danh sách ngày 2026-11-10 |
| **API Response** | GET /api/promotions: 200. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [BO-03-1.jpg](images/BO-03-1.jpg) |

### BO-19

**Guide me nói từ chối sẽ đóng luồng trả hàng, khách vẫn gửi được yêu cầu mới**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần xác nhận |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me, order-service |
| Việc tiếp theo | Chốt cách gửi lại yêu cầu trả hàng |
| Kế hoạch | [kế hoạch](fix-plans/backoffice/BO-19-guide-return-request-after-rejection.md) |
| Ghi chú | Đã tạo được yêu cầu mới sau khi bị từ chối. Cần chốt quy tắc gửi lại. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B11). |
| **Luồng** | Guide me: Xử lý trả hàng |
| **Endpoint / Màn hình** | POST /api/v1/returns |
| **Nghi ngờ thuộc** | order-service hoặc nội dung guide |
| **Bước tái hiện** | 1. Seller từ chối yêu cầu trả của đơn ORD-...<br>2. Khách tạo yêu cầu mới cho cùng đơn (còn trong 7 ngày) |
| **Mong đợi** | Lời hướng dẫn khớp hành vi (hoặc hệ thống chặn) |
| **Thực tế** | 201, yêu cầu mới RMA-20261127-000066 |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-03 ([B11](test-2026-11-27/guide-me/loi.md#b11)). Response đầy đủ: [GM06-03](test-2026-11-27/guide-me/api/GM06-03.txt) |
| **API Response** | <pre>POST /api/v1/returns<br>Request body:<br>{<br>  "orderId": 188,<br>  "reasonCode": "WRONG_ITEM",<br>  "description": "Gửi lại yêu cầu kèm ảnh tem đơn hàng ghi bản bìa cứng như đã đặt",<br>  "items": [<br>    {<br>      "orderDetailId": 206,<br>      "quantity": 1<br>    }<br>  ],<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-19-1.png](images/BO-19-1.png) |

### BO-21

**Guide me nói Admin quyết số lượng nhập khi duyệt, hộp thoại chỉ có lời nhắn**

| Theo dõi | |
| --- | --- |
| Loại | Giao diện |
| Nhóm | Cần xác nhận |
| Mức độ | Minor |
| Khu vực | Backoffice Guide me, inventory-service |
| Việc tiếp theo | Chốt quyền sửa số lượng khi duyệt yêu cầu nhập |
| Kế hoạch | [kế hoạch](fix-plans/backoffice/BO-21-guide-stock-request-approved-quantity.md) |
| Ghi chú | Cần chốt Admin có được sửa số lượng ở bước duyệt hay không. |

Hồ sơ lỗi (backoffice/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B13). |
| **Luồng** | Guide me: Yêu cầu nhập hàng |
| **Endpoint / Màn hình** | PATCH /api/v1/inventory/stock-requests/{id}/approve |
| **Nghi ngờ thuộc** | inventory-service, taschen-backoffice |
| **Bước tái hiện** | Admin mở hộp thoại duyệt yêu cầu nhập; thử gửi quantity qua API |
| **Mong đợi** | Có ô sửa số lượng, hoặc sửa lời hướng dẫn |
| **Thực tế** | Hộp thoại chỉ có lời nhắn; API bỏ qua quantity |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM08-03 ([B13](test-2026-11-27/guide-me/loi.md#b13)). Response đầy đủ: [GM08-03](test-2026-11-27/guide-me/api/GM08-03.txt) |
| **API Response** | <pre>PATCH /api/v1/inventory/stock-requests/10/approve<br>Request body:<br>{<br>  "quantity": 3,<br>  "responseMessage": "Chỉ duyệt 3 cuốn"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 10,<br>    "requestCode": "STK-20261127-000026",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-21-1.png](images/BO-21-1.png)<br>[BO-21-2.png](images/BO-21-2.png) |

### SF-33

**Hủy ở cổng VNPay thì đơn tự hủy, không thanh toán lại được**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần xác nhận |
| Mức độ | Minor |
| Khu vực | order-service, payment-service |
| Việc tiếp theo | Chốt có cho thử thanh toán lại sau lỗi VNPay |
| Kế hoạch | [kế hoạch](fix-plans/storefront-backend/SF-33-vnpay-cancel-retry-policy.md) |
| Ghi chú | Chưa rõ có phải chủ đích |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | 4 - Checkout VNPAY |
| **Endpoint / Màn hình** | Trang kết quả thanh toán · chi tiết đơn |
| **Nghi ngờ thuộc** | order-service / payment-service (cần xác nhận) |
| **Bước tái hiện** | 1. Đặt hàng VNPay<br>2. Bấm hủy ở cổng sandbox |
| **Mong đợi** | Thanh toán thất bại được thử lại (theo luồng 4) |
| **Thực tế** | Đơn tự thành Đã hủy, không có nút thanh toán lại. Cần xác nhận đây là chủ đích |
| **Bằng chứng (status/body)** | Đơn ORD-20261114-000040: CANCELLED, FAILED |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [SF-33-1.jpg](images/SF-33-1.jpg) |

### SF-34

**Ô mã khuyến mãi phân biệt hoa thường**

| Theo dõi | |
| --- | --- |
| Loại | Logic |
| Nhóm | Cần xác nhận |
| Mức độ | Minor |
| Khu vực | storefront, promotion-service |
| Việc tiếp theo | Chốt quy tắc viết hoa và chuẩn hóa mã |
| Kế hoạch | [kế hoạch](fix-plans/storefront-backend/SF-34-promotion-code-case-policy.md) |
| Ghi chú | Cần xác nhận |

Hồ sơ lỗi (storefront/loi.md):

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
| **Luồng** | 7 - Khuyến mãi |
| **Endpoint / Màn hình** | Ô mã khuyến mãi ở checkout |
| **Nghi ngờ thuộc** | storefront / promotion-service (cần xác nhận) |
| **Bước tái hiện** | 1. Nhập deep1114 (chữ thường) và bấm Áp dụng |
| **Mong đợi** | Mã không phân biệt hoa thường, hoặc báo rõ cần nhập chữ hoa |
| **Thực tế** | Báo "Không tìm thấy mã khuyến mãi". Backend lại nhận cả mã chữ thường khi tạo (BO-08) |
| **Bằng chứng (status/body)** | deep1114 không tìm thấy, DEEP1114 hợp lệ |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | Không có. Lỗi được tìm bằng script gửi request nên chưa có ảnh. |


## Chờ retest

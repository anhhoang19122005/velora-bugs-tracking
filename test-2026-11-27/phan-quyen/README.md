[← Đợt test 2026-11-27](../README.md)

# Test phân quyền: vai trò làm việc không được phép

> Chạy ngày 27/11/2026 trên máy local, nối DB và broker dùng chung (`taschen-platform/.env`). Backend `d5b6ac2`, backoffice `8e1ecfbe`. Bổ sung cho 17 API đã test trong phần Guide me ([GM14](../guide-me/test-case/hd-phan-quyen-gm14.md)). Bằng chứng: ảnh và kết quả API ở [`images/`](images/) và [`data/`](data/). Video không đưa lên repo.

## 1. Kết luận

| Hạng mục | Phạm vi | Kết quả |
|---|---|---|
| API: vai trò bị cấm gọi thẳng | 110 API, 548 request (5 vai trò mỗi API) | **379/379** lần gọi của vai trò bị cấm bị chặn (401/403). **0 lỗ hổng** |
| API: vai trò được phép | Gọi bằng id không tồn tại | Admin bị chặn sai ở **3 API** (mục 3) |
| Giao diện: đăng nhập nhầm ứng dụng | 12 lần (4 vai trò × 3 ứng dụng) | Đạt; khách bị từ chối nhưng **không có thông báo** |
| Giao diện: gõ thẳng URL của vai trò khác | 96 trang | Đạt: Seller, Warehouse, chưa đăng nhập đều không vào được; Admin vào được (đúng thiết kế) |
| Giao diện: nút bấm theo vai trò | 58 lần mở trang, 29 màn hình | Đạt: nút duyệt, từ chối, huỷ, tạo danh mục, tạo banner chỉ hiện cho Admin |

**Không tìm thấy trường hợp nào vai trò bị cấm làm được việc không được phép**, cả qua API lẫn trên giao diện.

## 2. Giao diện

### 2.1 Đăng nhập nhầm ứng dụng

| Vai trò | Ứng dụng đăng nhập | Kết quả | Ảnh |
|---|---|---|---|
| Admin | admin | Vào :3000/admin/dashboard | [ảnh](images/A-admin-signin-admin.png) |
| Admin | seller | Vào :3000/admin/dashboard | [ảnh](images/A-admin-signin-seller.png) |
| Admin | warehouse | Vào :3000/admin/dashboard | [ảnh](images/A-admin-signin-warehouse.png) |
| Seller | admin | Vào :3002/seller/dashboard | [ảnh](images/A-seller-signin-admin.png) |
| Seller | seller | Vào :3002/seller/dashboard | [ảnh](images/A-seller-signin-seller.png) |
| Seller | warehouse | Vào :3002/seller/dashboard | [ảnh](images/A-seller-signin-warehouse.png) |
| Warehouse | admin | Vào :3001/warehouse/dashboard | [ảnh](images/A-warehouse-signin-admin.png) |
| Warehouse | seller | Vào :3001/warehouse/dashboard | [ảnh](images/A-warehouse-signin-seller.png) |
| Warehouse | warehouse | Vào :3001/warehouse/dashboard | [ảnh](images/A-warehouse-signin-warehouse.png) |
| Khách | admin | Ở lại trang đăng nhập, không thông báo | [ảnh](images/A-customer-signin-admin.png) |
| Khách | seller | Ở lại trang đăng nhập, không thông báo | [ảnh](images/A-customer-signin-seller.png) |
| Khách | warehouse | Ở lại trang đăng nhập, không thông báo | [ảnh](images/A-customer-signin-warehouse.png) |

Seller và Warehouse đăng nhập ứng dụng khác bị đưa về ứng dụng của mình. Khách (không có vai trò nhân viên) đăng nhập thành công ở API (200) nhưng màn hình vẫn là form đăng nhập trống, **không báo vì sao** (xem mục 4).

### 2.2 Gõ thẳng URL của vai trò khác

| Vai trò | Khu vực gõ vào | Số trang | Kết quả |
|---|---|---|---|
| Chưa đăng nhập | /admin/… | 9 | 9 về trang đăng nhập |
| Chưa đăng nhập | /seller/… | 12 | 12 về trang đăng nhập |
| Chưa đăng nhập | /warehouse/… | 11 | 11 về trang đăng nhập |
| Seller | /admin/… | 9 | 9 về trang đăng nhập |
| Seller | /warehouse/… | 11 | 11 về trang đăng nhập |
| Warehouse | /admin/… | 9 | 9 về trang đăng nhập |
| Warehouse | /seller/… | 12 | 12 về trang đăng nhập |
| Admin | /seller/… | 12 | 12 mở được |
| Admin | /warehouse/… | 11 | 11 mở được |

Ảnh của 96 trang này không đưa lên repo (gần như cùng một trang đăng nhập); dữ liệu từng trang nằm ở [`data/ui-b.json`](data/ui-b.json). Trên máy local mỗi ứng dụng một cổng và phiên đăng nhập lưu theo từng ứng dụng, nên vai trò sai được đưa về trang đăng nhập của ứng dụng kia thay vì trang "không có quyền". Không trang nào hiện dữ liệu.

### 2.3 Nút thao tác: vai trò bị giới hạn so với Admin trên cùng màn hình

| Màn hình | Vai trò | Nút chỉ Admin thấy | Nhận xét | Ảnh |
|---|---|---|---|---|
| seller/books | Seller | - | Không lấy được màn hình Admin để so (menu Actions quá thời gian); bên vai trò này không có nút ngoài quyền | [ảnh](images/C-seller-seller-books.png) |
| seller/books/{chi-tiết} | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-books-detail.png) |
| seller/categories | Seller | Add Category, row: Delete, row: Edit | Đúng: danh mục chỉ Admin tạo, sửa, xoá | [ảnh](images/C-seller-seller-categories.png) |
| seller/variants | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-variants.png) |
| seller/banners | Seller | Add Banner | Đúng: banner chỉ Admin tạo | [ảnh](images/C-seller-seller-banners.png) |
| seller/promotions | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-promotions.png) |
| seller/promotions#pending | Seller | Approve, Reject | Đúng: duyệt, từ chối khuyến mãi là của Admin | [ảnh](images/C-seller-seller-promotions-pending.png) |
| seller/orders | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-orders.png) |
| seller/orders/ORD-20261112-000035 | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-orders-ord-20261112-000035.png) |
| seller/returns | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-returns.png) |
| seller/returns/ORD-20261110-000024 | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-returns-ord-20261110-000024.png) |
| seller/stock-returns | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-stock-returns.png) |
| seller/payments | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-payments.png) |
| seller/payments/PAY-20261125-000042 | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-payments-pay-20261125-000042.png) |
| seller/refunds | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-refunds.png) |
| seller/refunds/ORD-20261112-000031 | Seller | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-seller-seller-refunds-ord-20261112-000031.png) |
| warehouse/suppliers | Warehouse | - | Không lấy được màn hình Admin để so (menu Actions quá thời gian); bên vai trò này không có nút ngoài quyền | [ảnh](images/C-warehouse-warehouse-suppliers.png) |
| warehouse/stock-requests | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-stock-requests.png) |
| warehouse/stock-requests/STK-20261127-000027 | Warehouse | Approve, Reject | Đúng: duyệt yêu cầu nhập là của Admin | [ảnh](images/C-warehouse-warehouse-stock-requests-stk-20261127-000027.png) |
| warehouse/purchase-orders | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-purchase-orders.png) |
| warehouse/purchase-orders/PO-20261127-000048 | Warehouse | Approve, Reject | Đúng: duyệt đơn mua là của Admin | [ảnh](images/C-warehouse-warehouse-purchase-orders-po-20261127-000048.png) |
| warehouse/purchase-orders/{đã duyệt} | Warehouse | Cancel order, Mark ordered | Đúng: đặt hàng (chi tiền) và huỷ đơn mua là của Admin | [ảnh](images/C-warehouse-warehouse-purchase-orders-approved.png) |
| warehouse/import-stocks | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-import-stocks.png) |
| warehouse/import-stocks/IMP-20261127-000036 | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-import-stocks-imp-20261127-000036.png) |
| warehouse/batches | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-batches.png) |
| warehouse/disposals | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-disposals.png) |
| warehouse/disposals/DSP-20261127-000018 | Warehouse | Approve, Reject | Đúng: duyệt thanh lý là của Admin | [ảnh](images/C-warehouse-warehouse-disposals-dsp-20261127-000018.png) |
| warehouse/return-to-warehouse | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-return-to-warehouse.png) |
| warehouse/return-to-warehouse/RTW-20261127-000071 | Warehouse | không có | Hai vai trò thấy cùng các nút | [ảnh](images/C-warehouse-warehouse-return-to-warehouse-rtw-20261127-000071.png) |

Các nút Seller có thật sự được phép: Thêm sách, Sửa sách, Ngừng bán, Thêm định dạng, Sửa định dạng, Thêm khuyến mãi, Bắt đầu xử lý và Huỷ đơn, Trả về kho. Đối chiếu với `@PreAuthorize` ở backend thì đều khớp (catalog, order cho `ADMIN,SELLER`). Warehouse thấy Duyệt và Từ chối ở phiếu trả về kho: đúng, vì backend cho `ADMIN,WAREHOUSE_STAFF`. Nút `Edit` trên các danh sách kho chỉ mở cùng ngăn chi tiết như `View`, không có thao tác sửa.

## 3. API

Mỗi API gọi bằng 5 vai trò (chưa đăng nhập, Khách, Seller, Warehouse, Admin), id trên đường dẫn không tồn tại để không đổi dữ liệu. Với API tạo mới, vai trò bị cấm được gửi thêm một lần với dữ liệu hợp lệ (vì kiểm dữ liệu có thể chạy trước kiểm quyền); vai trò được phép không gửi dữ liệu hợp lệ. Kết quả đầy đủ: [`results.json`](data/results.json).

### 3.1 Admin bị chặn ở chức năng của chính mình

| API | Mã | Nguyên nhân |
|---|---|---|
| `POST /api/v1/inventory/stats/cogs` | 403 (gateway) | Không có quyền nào ở gateway cho `POST`. API này chỉ được order-service gọi thẳng qua Feign (không qua gateway), nên đây là đúng thiết kế |
| `POST /api/v1/payments/transfers/{sepayId}/apply` | 403 (gateway) | Quyền `PAYMENT_TRANSFER_APPLY` (migration V18) **không còn trên DB dùng chung**, dù flyway báo schema bản 19. Repo chỉ có đến V18, nên có người đã chạy migration nhánh khác hoặc xoá quyền. Admin bấm "Áp vào đơn" ở màn tài chính sẽ bị 403 |
| `POST /api/v1/payments/transfers/{sepayId}/refunds` | 403 (gateway) | Như trên: thiếu `PAYMENT_UNAPPLIED_REFUND` |

### 3.2 Từng API

| API | Được phép | Chưa đăng nhập | Khách | Seller | Warehouse | Admin |
|---|---|---|---|---|---|---|
| `DELETE /api/v1/banners/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/banners/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/book-variants` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/book-variants/book/{bookId}` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/book-variants/variant/{variantId}` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `DELETE /api/v1/book-variants/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/book-variants/{id}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `PUT /api/v1/book-variants/{id}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `POST /api/v1/books/embeddings/reindex` | ADMIN | 401 | 403 | 403 | 403 | không gọi |
| `GET /api/v1/books/trash` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `DELETE /api/v1/books/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/books/{id}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `PATCH /api/v1/books/{id}/restore` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/books/{id}/status` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `DELETE /api/v1/categories/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/categories/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `POST /api/v1/uploads/image` | ADMIN, SELLER | 401 | 403 | 500 | 403 | 500 |
| `POST /api/v1/variants` | ADMIN, SELLER | 401 | 403 | 400 | 403 | 400 |
| `DELETE /api/v1/variants/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/variants/{id}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/permissions` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `POST /api/v1/permissions` | ADMIN | 401 | 403 | 403 | 403 | 400 |
| `DELETE /api/v1/permissions/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/permissions/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/permissions/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/roles` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `POST /api/v1/roles` | ADMIN | 401 | 403 | 403 | 403 | 400 |
| `GET /api/v1/roles/code/{code}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `DELETE /api/v1/roles/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/roles/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/roles/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PUT /api/v1/roles/{id}/permissions` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/users` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/users/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/users/{id}/activate` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/users/{id}/deactivate` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/users/{id}/role` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/inventory/batches` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `POST /api/v1/inventory/batches` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 400 | 400 |
| `GET /api/v1/inventory/batches/fifo-preview` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `GET /api/v1/inventory/batches/stock-total` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `GET /api/v1/inventory/batches/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/disposals` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `POST /api/v1/inventory/disposals` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 400 | 400 |
| `GET /api/v1/inventory/disposals/code/{code}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/disposals/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `PATCH /api/v1/inventory/disposals/{id}/reject` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/inventory/import-stocks` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `POST /api/v1/inventory/import-stocks` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 400 | 400 |
| `GET /api/v1/inventory/import-stocks/code/{code}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/import-stocks/pending` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `DELETE /api/v1/inventory/import-stocks/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/import-stocks/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/return-to-warehouse` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `GET /api/v1/inventory/return-to-warehouse/code/{code}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/return-to-warehouse/mine` | ADMIN, SELLER, WAREHOUSE_STAFF | 401 | 403 | 200 | 200 | 200 |
| `GET /api/v1/inventory/return-to-warehouse/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `PATCH /api/v1/inventory/return-to-warehouse/{id}/reject` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `POST /api/v1/inventory/stats/cogs` | ADMIN | 401 | 403 | 403 | 403 | 403 ⚠ |
| `GET /api/v1/inventory/stats/purchasing` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/inventory/stats/stock-value` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/inventory/stock-requests` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `GET /api/v1/inventory/stock-requests/code/{code}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/inventory/stock-requests/mine` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `GET /api/v1/inventory/stock-requests/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `PATCH /api/v1/inventory/stock-requests/{id}/reject` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/purchase-orders` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 200 | 200 |
| `POST /api/v1/purchase-orders` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 400 | 400 |
| `GET /api/v1/purchase-orders/code/{code}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `POST /api/v1/purchase-orders/from-stock-request` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 400 | 400 |
| `GET /api/v1/purchase-orders/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `PATCH /api/v1/purchase-orders/{id}/cancel` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/purchase-orders/{id}/reject` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/suppliers` | ADMIN, WAREHOUSE_STAFF, SELLER | 401 | 403 | 200 | 200 | 200 |
| `DELETE /api/v1/suppliers/{id}` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `GET /api/v1/suppliers/{id}` | ADMIN, WAREHOUSE_STAFF, SELLER | 401 | 403 | 404 | 404 | 404 |
| `PATCH /api/v1/suppliers/{id}` | ADMIN, WAREHOUSE_STAFF | 401 | 403 | 403 | 404 | 404 |
| `GET /api/v1/orders/completed-monthly` | SELLER, ADMIN | 401 | 403 | 200 | 403 | 200 |
| `POST /api/v1/orders/finance-backfill` | ADMIN | 401 | 403 | 403 | 403 | không gọi |
| `GET /api/v1/orders/stats` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/orders/stats/month` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `PATCH /api/v1/orders/{id}/status` | SELLER, ADMIN | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/returns` | SELLER, ADMIN | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/returns/code/{returnCode}` | SELLER, ADMIN | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/returns/{id}` | SELLER, ADMIN | 401 | 403 | 404 | 403 | 404 |
| `PATCH /api/v1/returns/{id}/received` | SELLER, ADMIN | 401 | 403 | 404 | 403 | 404 |
| `PATCH /api/v1/returns/{id}/reject` | SELLER, ADMIN | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/payments` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/payments/code/{paymentCode}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/payments/order/{orderId}` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/payments/overpaid` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/payments/refunds` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/payments/refunds/code/{refundCode}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `GET /api/v1/payments/refunds/summary` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/payments/refunds/{refundId}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `POST /api/v1/payments/refunds/{refundId}/records` | ADMIN, SELLER | 401 | 403 | 400 | 403 | 400 |
| `POST /api/v1/payments/transfers/{sepayId}/apply` | ADMIN | 401 | 403 | 403 | 403 | 403 ⚠ |
| `POST /api/v1/payments/transfers/{sepayId}/refunds` | ADMIN | 401 | 403 | 403 | 403 | 403 ⚠ |
| `GET /api/v1/payments/unapplied` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/payments/underpaid` | ADMIN | 401 | 403 | 403 | 403 | 200 |
| `GET /api/v1/payments/{paymentId}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `POST /api/v1/payments/{paymentId}/cancel-underpaid` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `POST /api/v1/payments/{paymentId}/remind` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `POST /api/v1/payments/{paymentId}/transfer-refunds` | ADMIN | 401 | 403 | 403 | 403 | 400 |
| `GET /api/v1/promotions` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/promotions/search` | ADMIN, SELLER | 401 | 403 | 200 | 403 | 200 |
| `GET /api/v1/promotions/{id}` | ADMIN, SELLER | 401 | 403 | 404 | 403 | 404 |
| `PATCH /api/v1/promotions/{id}/pause` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/promotions/{id}/reject` | ADMIN | 401 | 403 | 403 | 403 | 404 |
| `PATCH /api/v1/promotions/{id}/resume` | ADMIN | 401 | 403 | 403 | 403 | 404 |

⚠ = khác mong đợi. `POST /uploads/image`: vai trò được phép trả 500 vì lần gọi gửi thân rỗng, không phải lỗi quyền. `finance-backfill` và `embeddings/reindex` không gọi bằng Admin vì sẽ chạy tác vụ hàng loạt thật.

## 4. Phát hiện

| # | Mã theo dõi | Mức | Phát hiện | Bằng chứng |
|---|---|---|---|---|
| P1 | [SF-47](../../storefront/loi.md#sf-47) | Major (dữ liệu dùng chung) | Role `USER` không còn trên DB dùng chung. Token và `/users/me` của khách có danh sách vai trò rỗng; `GET /roles/code/USER` trả 404. Code đăng ký bắt buộc có role này (`AuthServiceImpl.findDefaultRole`), nên **người đăng ký mới sẽ lỗi**. Trên DB còn role lạ `QA-ROLE-20261127` không do đợt này tạo | `results.json`, lệnh kiểm tra ghi trong mục 5 |
| P2 | [BO-24](../../backoffice/loi.md#bo-24) | Major (dữ liệu dùng chung) | Hai quyền chuyển khoản SePay của Admin (V18) mất trên DB dùng chung: Admin không áp được chuyển khoản vào đơn, không hoàn được khoản chuyển nhầm | Mục 3.1 |
| P3 | [BO-25](../../backoffice/loi.md#bo-25) | Minor (giao diện) | Khách đăng nhập ứng dụng quản trị: API 200 nhưng màn hình quay về form đăng nhập trống, không có thông báo "tài khoản không có quyền vào đây" | [ảnh](images/A-customer-signin-seller.png) |

P1, P2 là do dữ liệu trên DB dùng chung bị đổi, không phải lỗi code; nhưng chúng làm hỏng đăng ký và tài chính cho mọi người đang dùng DB này. Cần người quản lý DB chạy lại seed (V2, V18) hoặc xác nhận ai đã đổi.

## 5. Giới hạn

- Gọi qua gateway nên mỗi lần 403 có thể đến từ gateway hoặc `@PreAuthorize`; chưa tách riêng lớp service (gọi thẳng service cần token nội bộ).
- Chưa test quyền sở hữu: khách A xem hoặc huỷ đơn của khách B.
- Ở 2.3, chỉ so nút trên các màn hình có dữ liệu sẵn; với đơn mua đã duyệt, phiếu chờ duyệt đều dùng bản ghi có trên DB dùng chung.
- Admin của danh sách sách và nhà cung cấp không chụp được (menu Actions quá thời gian), nên hai màn hình đó chỉ kiểm phía Seller và Warehouse.
- notification-service không bật nên mọi trang có lỗi 500 ở `/api/notifications`; không liên quan phân quyền.

## 6. Video

14 video WebM quay các phiên trình duyệt không đưa lên repo; file nằm ở máy chạy test.

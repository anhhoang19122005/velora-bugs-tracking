# Danh sách lỗi - Backoffice

Ghi nhận ngày 2026-11-14: **BO-08–BO-11** là lỗi mới tìm thấy khi retest và khi test tính bất biến.

Ghi nhận ngày 2026-11-27: **BO-13–BO-26** là lỗi mới từ đợt test theo Guide me và test phân quyền ([test-2026-11-27](../test-2026-11-27/README.md)). Mỗi lỗi ghi kèm mã trong đợt (B.., P..).

| # | Mức độ | Luồng | Endpoint / Màn hình | Nghi ngờ thuộc | Ảnh |
|---|---|---|---|---|---|
| [BO-01](#bo-01) | Minor | 6 - Phân quyền | /forbidden · console admin | backoffice | [Ảnh 1](../images/BO-01-1.jpg) |
| [BO-02](#bo-02) | Minor | Storefront 7 - Khuyến mãi | PATCH /promotions/{id}/approve | promotion-service | [Ảnh 1](../images/BO-02-1.jpg) |
| [BO-03](#bo-03) | Minor | Storefront 7 - Khuyến mãi | Danh sách khuyến mãi | seller / promotion-service | [Ảnh 1](../images/BO-03-1.jpg) |
| [BO-04](#bo-04) | Minor (đã sửa) | Tạo khuyến mãi | Form tạo khuyến mãi seller | seller app | [Ảnh 1](../images/BO-04-1.jpg) |
| [BO-05](#bo-05) | Minor (chấp nhận) | 2, 3 - Sách, đơn mua | Ô giá của form tạo sách và đơn mua | backoffice | [Ảnh 1](../images/BO-05-1.jpg) |
| [BO-06](#bo-06) | Minor (đã sửa) | 2, 3 - Sách, đơn mua | Form tạo sách, đơn mua | backoffice | [Ảnh 1](../images/BO-06-1.jpg) |
| [BO-07](#bo-07) | Minor | 3 - Đơn mua | Form đơn mua ở màn hình 1024px | backoffice | [Ảnh 1](../images/BO-07-1.jpg) |
| [BO-08](#bo-08) | Minor | Tạo khuyến mãi | POST /promotions · form tạo khuyến mãi seller | promotion-service | [Ảnh 1](../images/BO-08-1.jpg) |
| [BO-09](#bo-09) | Minor | Khuyến mãi | GET /promotions/search?keyword= | promotion-service | Không có |
| [BO-10](#bo-10) | Minor | Nhà cung cấp | POST /api/v1/suppliers | inventory-service | Không có |
| [BO-11](#bo-11) | Minor | Đơn mua, nhập kho | POST /api/v1/inventory/import-stocks | inventory-service | Không có |
| [BO-12](#bo-12) | Minor (đã sửa một phần, chờ retest) | 3 - Đơn mua (Admin) | Danh sách và chi tiết đơn mua ở console Admin | backoffice | [Ảnh 1](../images/BO-12-1.png), [Ảnh 2](../images/BO-12-2.png) |
| [BO-13](#bo-13) | Major | Trả hàng → trả về kho | POST /api/v1/inventory/return-to-warehouse · PATCH .../{id}/approve | inventory-service (bảng chống trùng processed_order_returns đã bị xoá ở migration V12) | [Ảnh 1](../images/BO-13-1.png), [Ảnh 2](../images/BO-13-2.png) |
| [BO-14](#bo-14) | Major | Đơn mua | POST /api/v1/purchase-orders/from-stock-request | inventory-service | [Ảnh 1](../images/BO-14-1.png) |
| [BO-15](#bo-15) | Major | Nhà cung cấp → Đơn mua | POST /api/v1/purchase-orders | inventory-service | [Ảnh 1](../images/BO-15-1.png) |
| [BO-16](#bo-16) | Major | Duyệt trả về kho | PATCH /api/v1/inventory/return-to-warehouse/{id}/approve | inventory-service (BatchServiceImpl.restockReturnedUnits) | [Ảnh 1](../images/BO-16-1.png) |
| [BO-17](#bo-17) | Minor | Guide me: Đăng banner | (giao diện) form banner · BannerRequest | taschen-backoffice (guide seller), catalog-service | [Ảnh 1](../images/BO-17-1.png), [Ảnh 2](../images/BO-17-2.png) |
| [BO-18](#bo-18) | Minor | Guide me: Tạo khuyến mãi | POST /api/v1/promotions (quantity trống) | taschen-backoffice (guide seller) | [Ảnh 1](../images/BO-18-1.png), [Ảnh 2](../images/BO-18-2.png) |
| [BO-19](#bo-19) | Minor | Guide me: Xử lý trả hàng | POST /api/v1/returns | order-service hoặc nội dung guide | [Ảnh 1](../images/BO-19-1.png) |
| [BO-20](#bo-20) | Minor | Guide me: Xử lý trả hàng | PATCH /api/v1/returns/{id}/received | taschen-backoffice (guide seller) | [Ảnh 1](../images/BO-20-1.png) |
| [BO-21](#bo-21) | Minor | Guide me: Yêu cầu nhập hàng | PATCH /api/v1/inventory/stock-requests/{id}/approve | inventory-service, taschen-backoffice | [Ảnh 1](../images/BO-21-1.png), [Ảnh 2](../images/BO-21-2.png) |
| [BO-22](#bo-22) | Minor | Guide me: Yêu cầu nhập hàng | GET /api/v1/inventory/stock-requests/{id} | inventory-service hoặc guide warehouse | [Ảnh 1](../images/BO-22-1.png) |
| [BO-23](#bo-23) | Minor | Guide me: Đơn mua | POST /api/v1/inventory/import-stocks | taschen-backoffice (guide warehouse) | [Ảnh 1](../images/BO-23-1.png) |
| [BO-24](#bo-24) | Major | Tài chính (Admin) | POST /api/v1/payments/transfers/{sepayId}/apply · POST /api/v1/payments/transfers/{sepayId}/refunds | DB dùng chung (identity, ma trận quyền), không phải lỗi code | Không có |
| [BO-25](#bo-25) | Minor | 6 - Phân quyền | Trang /signin của admin, seller, warehouse | backoffice | [Ảnh 1](../images/BO-25-1.png) |
| [BO-26](#bo-26) | Minor | Guide me: Tạo danh mục | POST /api/v1/categories | catalog-service | [Ảnh 1](../images/BO-26-1.png) |

## BO-01

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-01-forbidden-page-empty-guided-tasks.md) |
| **Luồng** | 6 - Phân quyền |
| **Endpoint / Màn hình** | /forbidden · console admin |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Đăng nhập seller ở console admin |
| **Mong đợi** | Trang không có quyền hiển thị gọn |
| **Thực tế** | Hộp Guided tasks trống phủ lên trang không có quyền |
| **Bằng chứng (status/body)** | Ảnh |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [BO-01-1.jpg](../images/BO-01-1.jpg) |

## BO-02

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backend/BO-02-promotion-approve-stale-updated-at.md) |
| **Luồng** | Storefront 7 - Khuyến mãi |
| **Endpoint / Màn hình** | PATCH /promotions/{id}/approve |
| **Nghi ngờ thuộc** | promotion-service |
| **Bước tái hiện** | Admin duyệt khuyến mãi |
| **Mong đợi** | Response của PATCH approve trả updatedAt mới |
| **Thực tế** | Response của PATCH approve trả updatedAt cũ, trùng createdAt. Dữ liệu lưu vẫn đúng: GET /api/promotions sau đó trả updatedAt 03:43:53 |
| **Bằng chứng (status/body)** | Ảnh GET /api/promotions, bản ghi id 27 (MANUAL1110): createdAt 03:41:50, updatedAt 03:43:53. Response approve xem ở cột API Response |
| **API Response** | <pre>HTTP 200<br>{<br>  "id": 27,<br>  "code": "MANUAL1110",<br>  "discountPercent": 10,<br>  "status": "ACTIVE",<br>  "createdByUserId": 96,<br>  "approvedByUserId": 95,<br>  "createdAt": "2026-11-10T03:41:50.714442Z",<br>  "updatedAt": "2026-11-10T03:41:50.714442Z"<br>}<br>(đã rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-02-1.jpg](../images/BO-02-1.jpg) |

## BO-03

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-03-promotion-expired-still-active.md) |
| **Luồng** | Storefront 7 - Khuyến mãi |
| **Endpoint / Màn hình** | Danh sách khuyến mãi |
| **Nghi ngờ thuộc** | seller / promotion-service |
| **Bước tái hiện** | Xem các khuyến mãi có ngày kết thúc 2026-09-21 |
| **Mong đợi** | Khuyến mãi quá hạn không còn hiện Active |
| **Thực tế** | Vẫn hiện Active và Pending. Cần xác nhận quy tắc hiển thị |
| **Bằng chứng (status/body)** | Bảng danh sách ngày 2026-11-10 |
| **API Response** | GET /api/promotions: 200. Status ghi nhận từ tab Network. Body không lưu được vì đã chuyển trang trước khi đọc. |
| **Ảnh bằng chứng** | [BO-03-1.jpg](../images/BO-03-1.jpg) |

## BO-04

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa, đã merge vào `develop` qua PR #367 (merge `8bc1ee53`); kiểm thử lại trên trình duyệt ngày 2026-11-14. Xem [kế hoạch](../fix-plans/backoffice/BO-04-promotion-form-generic-error-data-lost.md) |
| **Luồng** | Tạo khuyến mãi |
| **Endpoint / Màn hình** | Form tạo khuyến mãi seller |
| **Nghi ngờ thuộc** | seller app |
| **Bước tái hiện** | Gửi dữ liệu sai: trùng mã, ngày sai, giảm 0 hoặc 101, số lượng 0 |
| **Mong đợi** | Báo đúng trường bị sai, giữ nguyên dữ liệu đã nhập |
| **Thực tế** | Chỉ báo chung "invalid data" hoặc "conflicts", form đóng và mất dữ liệu |
| **Bằng chứng (status/body)** | Backoffice-HD-Tạo khuyến mãi TC03-05, TC09-11 |
| **API Response** | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "7dfd215b-4401-419f-92e7-5cfddbf8dfdf"<br>}</pre> |
| **Ảnh bằng chứng** | [BO-04-1.jpg](../images/BO-04-1.jpg) |

## BO-05

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor (chấp nhận) |
| **Trạng thái** | Đã chấp nhận, không sửa: người dùng xác nhận ngày 2026-11-12 rằng việc chuẩn hóa -1 thành 1 là hợp lý (ghi trong báo cáo retest Backoffice, đã xóa khỏi repo, còn trong commit `e6e2057`; chưa kiểm tra lưu sau chuẩn hóa). Xem [kế hoạch](../fix-plans/backoffice/BO-05-price-input-drops-minus-sign.md) |
| **Luồng** | 2, 3 - Sách, đơn mua |
| **Endpoint / Màn hình** | Ô giá của form tạo sách và đơn mua |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Nhập giá -1 vào ô giá |
| **Mong đợi** | Báo giá không được âm |
| **Thực tế** | Ô giá tự bỏ dấu trừ. Sách được lưu với giá 1 đ mà không báo gì |
| **Bằng chứng (status/body)** | Backoffice-HD-Tạo sách TC12, Backoffice-HD-Đơn mua TC10 |
| **API Response** | <pre>HTTP 201<br>{<br>  "id": 49,<br>  "price": 1<br>}</pre> |
| **Ảnh bằng chứng** | [BO-05-1.jpg](../images/BO-05-1.jpg) |

## BO-06

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa, đã merge vào `develop` qua PR #367 (merge `8bc1ee53`); kiểm thử lại form sách trên trình duyệt ngày 2026-11-14. Xem [kế hoạch](../fix-plans/backoffice/BO-06-book-purchase-order-form-field-too-long.md) |
| **Luồng** | 2, 3 - Sách, đơn mua |
| **Endpoint / Màn hình** | Form tạo sách, đơn mua |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Nhập tên 256 ký tự, tác giả 101 ký tự, hoặc ghi chú 1001 ký tự rồi lưu |
| **Mong đợi** | Báo đúng trường bị sai |
| **Thực tế** | 400, chỉ báo chung lỗi dữ liệu, không chỉ ra trường sai |
| **Bằng chứng (status/body)** | Backoffice-HD-Tạo sách TC10, TC11; Backoffice-HD-Đơn mua TC11 |
| **API Response** | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "5115812f-d3df-44a1-8b56-846e46232f89"<br>}</pre> |
| **Ảnh bằng chứng** | [BO-06-1.jpg](../images/BO-06-1.jpg) |

## BO-07

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-07-purchase-order-lines-horizontal-scroll.md) |
| **Luồng** | 3 - Đơn mua |
| **Endpoint / Màn hình** | Form đơn mua ở màn hình 1024px |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Mở form đơn mua ở chiều rộng 1024px |
| **Mong đợi** | Các ô của dòng hàng đều bấm được |
| **Thực tế** | Dòng hàng phải cuộn ngang, ô Book bị đẩy khỏi tầm nhìn, dễ bấm nhầm ô Format |
| **Bằng chứng (status/body)** | Kiểm tra ở 1024px, bình thường ở 1600px |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [BO-07-1.jpg](../images/BO-07-1.jpg) |

## BO-08

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
| **Ảnh bằng chứng** | [BO-08-1.jpg](../images/BO-08-1.jpg) |

## BO-09

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

## BO-10

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

## BO-11

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

## BO-12

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trong commit `80960bbe` (BUG-001) qua PR #369 (merge `fe73d47f`), đã vào `develop`, đối chiếu Git ngày 2026-11-20. Bản sửa nằm ở lớp bảo vệ `packages/core/src/api/proxy.ts`: yêu cầu tới đường dẫn thường của một console mà người dùng chưa có phiên ở console đó nhưng có phiên Admin sẽ được chuyển về `/admin/<console>/…`. Các liên kết vẫn dùng đường dẫn thường. Nếu trình duyệt có phiên của console đích, proxy chọn phiên đó trước khi xét chuyển về phiên Admin. Cần retest mở chi tiết PO và quay lại danh sách trong hai trường hợp: chỉ có phiên Admin và có đồng thời phiên Admin cùng Warehouse. **Chưa có kết quả retest riêng cho hai trường hợp này.** Ghi nhận ban đầu từ báo cáo retest Backoffice ngày 2026-11-12 (đã xóa khỏi repo, còn trong commit `e6e2057`)
| **Luồng** | 3 - Đơn mua (Admin) |
| **Endpoint / Màn hình** | Danh sách và chi tiết đơn mua ở console Admin, cổng 3001 |
| **Nghi ngờ thuộc** | backoffice (đường dẫn danh sách cố định trong `useListMutation`, không giữ tiền tố `/admin`) |
| **Bước tái hiện** | 1. Đăng nhập Admin (chỉ Admin, chưa đăng nhập Warehouse)<br>2. Mở `http://localhost:3001/admin/warehouse/purchase-orders`<br>3. Bấm mở một đơn mua<br>4. Với đơn APPROVED, mở thẳng `/admin/warehouse/purchase-orders/{id}` rồi bấm Mark ordered |
| **Mong đợi** | Mở chi tiết và quay về danh sách giữ nguyên tiền tố `/admin`, vẫn là phiên Admin |
| **Thực tế** | Bấm mở đơn mua dẫn tới `/warehouse/purchase-orders/3` (mất `/admin`) và ứng dụng chuyển sang đăng nhập Warehouse. Mở thẳng đường dẫn có `/admin` thì giữ đúng phiên và Mark ordered thành công, nhưng sau đó ứng dụng lại chuyển về `/warehouse/purchase-orders` và đòi đăng nhập Warehouse |
| **Bằng chứng (status/body)** | Tái hiện qua trình duyệt tích hợp, chưa thu HTTP status/body. Ảnh 2 là lần Admin bị từ chối khi duyệt đơn mua ("You do not have permission"); báo cáo gốc ghi chưa chứng minh nó cùng nguyên nhân |
| **API Response** | Không áp dụng: lỗi điều hướng giao diện |
| **Ảnh bằng chứng** | [BO-12-1.png](../images/BO-12-1.png)<br>[BO-12-2.png](../images/BO-12-2.png) |

## BO-13

| Trường | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-27 (test theo Guide me, mã trong đợt: B01). **Retest 2026-11-27: đã xác nhận.** Danh sách → mở đơn → tải lại → mở đơn APPROVED → Mark ordered: URL giữ /admin/warehouse và phiên Admin ở mọi bước (:3001/admin/warehouse/purchase-orders \| :3001/admin/warehouse/purchase-orders/PO-20261127-000051 \| :3001/admin/warehouse/purchase-orders/PO-20261127-000051 \| :3001/admin/warehouse/purchase-orders/PO-20261127-000045 \| :3001/admin/warehouse/purchase-orders). Bấm Mark ordered cho PO-20261127-000045; trạng thái sau: ORDERED. Xem [bằng chứng](../test-2026-11-27/retest/README.md#bo-12). |
| **Luồng** | Trả hàng → trả về kho |
| **Endpoint / Màn hình** | POST /api/v1/inventory/return-to-warehouse · PATCH .../{id}/approve |
| **Nghi ngờ thuộc** | inventory-service (bảng chống trùng processed_order_returns đã bị xoá ở migration V12) |
| **Bước tái hiện** | 1. Khách trả 1 cuốn Sapiens (RMA-20261127-000064), Seller duyệt và bấm Đã nhận<br>2. Seller lập phiếu trả về kho 1 cuốn (RTW-...066)<br>3. Seller lập thêm phiếu thứ hai cho cùng yêu cầu (RTW-...067) và phiếu khai 50 cuốn (RTW-...068)<br>4. Warehouse duyệt RTW-066 rồi RTW-067 |
| **Mong đợi** | Chỉ một phiếu trả về kho cho mỗi yêu cầu trả hàng, số lượng không vượt số khách trả; tồn tăng đúng 1 |
| **Thực tế** | Cả ba phiếu đều tạo được (201). Duyệt hai phiếu: tồn bìa mềm 14 → 15 → 16, tức cộng 2 cuốn cho 1 cuốn khách trả. Phiếu 50 cuốn cũng duyệt được nếu Warehouse không để ý |
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-07, GM06-08, GM11-04 ([B01](../test-2026-11-27/guide-me/loi.md#b01)). Response đầy đủ: [GM06-07](../test-2026-11-27/guide-me/api/GM06-07.txt), [GM06-08](../test-2026-11-27/guide-me/api/GM06-08.txt), [GM11-04](../test-2026-11-27/guide-me/api/GM11-04.txt) |
| **API Response** | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Khách trả 1 cuốn, sách còn nguyên seal, đưa lại lên kệ",<br>  "items": [<br>    {<br>      "bookId": 67,<br>      "variantId": 1,<br>      "quantity": 1<br>    }<br>  ],<br>  "returnRequestId": 64,<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-13-1.png](../images/BO-13-1.png)<br>[BO-13-2.png](../images/BO-13-2.png) |

## BO-14

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM09-12 ([B05](../test-2026-11-27/guide-me/loi.md#b05)). Response đầy đủ: [GM09-12](../test-2026-11-27/guide-me/api/GM09-12.txt) |
| **API Response** | <pre>POST /api/v1/purchase-orders/from-stock-request<br>Request body:<br>{<br>  "stockRequestId": 17,<br>  "supplierId": 36,<br>  "importPrice": 0,<br>  "note": "Hàng tặng kèm"<br>}<br>HTTP 500<br>{<br>  "success": false,<br>  "code": "INTERNAL_ERROR",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-14-1.png](../images/BO-14-1.png) |

## BO-15

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM07-03 ([B06](../test-2026-11-27/guide-me/loi.md#b06)). Response đầy đủ: [GM07-03](../test-2026-11-27/guide-me/api/GM07-03.txt) |
| **API Response** | <pre>DELETE /api/v1/suppliers/38<br>HTTP 204<br>{}<br><br>POST /api/v1/purchase-orders<br>Request body:<br>{<br>  "supplierId": 38,<br>  "note": "Đặt bổ sung tháng 12",<br>  "items": [<br>    {<br>      "bookId": 1,<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-15-1.png](../images/BO-15-1.png) |

## BO-16

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM11-03 ([B07](../test-2026-11-27/guide-me/loi.md#b07)). Response đầy đủ: [GM11-03](../test-2026-11-27/guide-me/api/GM11-03.txt) |
| **API Response** | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Khách trả cuốn sách chưa từng nhập kho qua phiếu nhập",<br>  "items": [<br>    {<br>      "bookId": 70,<br>      "variantId": 1,<br>      "quantity": 1<br>    }<br>  ],<br>  "returnRequestId": 64<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-16-1.png](../images/BO-16-1.png) |

## BO-17

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM04-02 ([B09](../test-2026-11-27/guide-me/loi.md#b09)). Response đầy đủ: [GM04-02](../test-2026-11-27/guide-me/api/GM04-02.txt) |
| **API Response** | <pre>GET /api/v1/banners/1<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 1,<br>    "name": "[GM-TEST-11271102] Sale tháng 12",<br>    "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>  },<br>  "message": "OK",<br>  "timestamp": "2026-11-27T04:37:46.077658900Z"<br>}<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-17-1.png](../images/BO-17-1.png)<br>[BO-17-2.png](../images/BO-17-2.png) |

## BO-18

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM05-05 ([B10](../test-2026-11-27/guide-me/loi.md#b10)). Response đầy đủ: [GM05-05](../test-2026-11-27/guide-me/api/GM05-05.txt) |
| **API Response** | <pre>POST /api/v1/promotions<br>Request body:<br>{<br>  "name": "Tri ân khách hàng",<br>  "code": "TRIAN2026",<br>  "discountPercent": 5,<br>  "priceOrderActive": 200000,<br>  "startDate": "2026-11-27",<br>  "endDate": "2026-11-28"<br>}<br>HTTP 400<br>{<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-18-1.png](../images/BO-18-1.png)<br>[BO-18-2.png](../images/BO-18-2.png) |

## BO-19

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-03 ([B11](../test-2026-11-27/guide-me/loi.md#b11)). Response đầy đủ: [GM06-03](../test-2026-11-27/guide-me/api/GM06-03.txt) |
| **API Response** | <pre>POST /api/v1/returns<br>Request body:<br>{<br>  "orderId": 188,<br>  "reasonCode": "WRONG_ITEM",<br>  "description": "Gửi lại yêu cầu kèm ảnh tem đơn hàng ghi bản bìa cứng như đã đặt",<br>  "items": [<br>    {<br>      "orderDetailId": 206,<br>      "quantity": 1<br>    }<br>  ],<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-19-1.png](../images/BO-19-1.png) |

## BO-20

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM06-04 ([B12](../test-2026-11-27/guide-me/loi.md#b12)). Response đầy đủ: [GM06-04](../test-2026-11-27/guide-me/api/GM06-04.txt) |
| **API Response** | <pre>PATCH /api/v1/returns/64/received<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 64,<br>    "returnCode": "RMA-20261127-000064",<br>    "orderId": 184,<br>    "reasonCode": "DEFECTIVE",<br>    "description": "Sách bị rách gáy và bong trang 45 đến 60 ngay khi mở hộp nhận hàng",<br>    "responseNote": "Đồng ý nhận lại, vui lòng gửi hàng về kho Quận 7",<br>    "status": "RECEIVED",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-20-1.png](../images/BO-20-1.png) |

## BO-21

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM08-03 ([B13](../test-2026-11-27/guide-me/loi.md#b13)). Response đầy đủ: [GM08-03](../test-2026-11-27/guide-me/api/GM08-03.txt) |
| **API Response** | <pre>PATCH /api/v1/inventory/stock-requests/10/approve<br>Request body:<br>{<br>  "quantity": 3,<br>  "responseMessage": "Chỉ duyệt 3 cuốn"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 10,<br>    "requestCode": "STK-20261127-000026",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-21-1.png](../images/BO-21-1.png)<br>[BO-21-2.png](../images/BO-21-2.png) |

## BO-22

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM08-04 ([B14](../test-2026-11-27/guide-me/loi.md#b14)). Response đầy đủ: [GM08-04](../test-2026-11-27/guide-me/api/GM08-04.txt) |
| **API Response** | <pre>GET /api/v1/inventory/stock-requests/6<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 6,<br>    "requestCode": "STK-20261127-000022",<br>    "quantity": 20,<br>    "reason": "Còn 2 cuốn trên kệ, mỗi tuần bán khoảng 5 cuốn",<br>    "status": "ORDERED",<br>    "createdAt": "2026-11-27T04:18:10.834603Z",<br>    "processedAt": "2026-11-27T04:18:11.333682Z",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-22-1.png](../images/BO-22-1.png) |

## BO-23

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM09-03 ([B15](../test-2026-11-27/guide-me/loi.md#b15)). Response đầy đủ: [GM09-03](../test-2026-11-27/guide-me/api/GM09-03.txt) |
| **API Response** | <pre>POST /api/v1/inventory/import-stocks<br>Request body:<br>{<br>  "supplierId": 36,<br>  "purchaseOrderId": 15,<br>  "details": [<br>    {<br>      "bookId": 67,<br>      "variantId": 1,<br>      "supplierId": 36,<br>      "quantity": 20,<br>      "importPrice": 118000<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-23-1.png](../images/BO-23-1.png) |

## BO-24

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, phần phân quyền ([P2](../test-2026-11-27/phan-quyen/README.md#31-admin-bị-chặn-ở-chức-năng-của-chính-mình)), [results.json](../test-2026-11-27/phan-quyen/data/results.json) |
| **API Response** | <pre>POST /api/v1/payments/transfers/999999999/apply<br>HTTP 403<br>{ "code": "FORBIDDEN", "message": "You do not have permission to perform this action" }</pre> |
| **Ảnh bằng chứng** | Không có |

## BO-25

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, phần phân quyền ([P3](../test-2026-11-27/phan-quyen/README.md#4-phát-hiện)) |
| **API Response** | Không áp dụng: lỗi giao diện |
| **Ảnh bằng chứng** | [BO-25-1.png](../images/BO-25-1.png) |

## BO-26

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
| **Bằng chứng (status/body)** | Đợt test 2026-11-27, case GM01-06 ([B08](../test-2026-11-27/guide-me/loi.md#b08)). Response đầy đủ: [GM01-06](../test-2026-11-27/guide-me/api/GM01-06.txt) |
| **API Response** | <pre>POST /api/v1/categories<br>Request body:<br>{<br>  "name": "[GM-TEST-11271102] Kỹ năng sống",<br>  "code": "gm 11271102 ky nang"<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 10,<br>    "slug": "gm-test-11271102-ky-nang-song",<br>(rút gọn)</pre> |
| **Ảnh bằng chứng** | [BO-26-1.png](../images/BO-26-1.png) |

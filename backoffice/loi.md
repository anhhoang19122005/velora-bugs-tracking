# Danh sách lỗi - Backoffice

Ghi nhận ngày 2026-11-14: **BO-08–BO-11** là lỗi mới tìm thấy khi retest và khi test tính bất biến.

| # | Mức độ | Luồng | Endpoint / Màn hình | Nghi ngờ thuộc | Ảnh |
|---|---|---|---|---|---|
| [BO-01](#bo-01) | Minor | 6 - Phân quyền | /forbidden · console admin | backoffice | [Ảnh 1](../images/BO-01-1.jpg) |
| [BO-02](#bo-02) | Minor | Storefront 7 - Khuyến mãi | PATCH /promotions/{id}/approve | promotion-service | [Ảnh 1](../images/BO-02-1.jpg) |
| [BO-03](#bo-03) | Minor | Storefront 7 - Khuyến mãi | Danh sách khuyến mãi | seller / promotion-service | [Ảnh 1](../images/BO-03-1.jpg) |
| [BO-04](#bo-04) | Minor (đã sửa, chưa merge) | Tạo khuyến mãi | Form tạo khuyến mãi seller | seller app | [Ảnh 1](../images/BO-04-1.jpg) |
| [BO-05](#bo-05) | Minor | 2, 3 - Sách, đơn mua | Ô giá của form tạo sách và đơn mua | backoffice | [Ảnh 1](../images/BO-05-1.jpg) |
| [BO-06](#bo-06) | Minor (đã sửa, chưa merge) | 2, 3 - Sách, đơn mua | Form tạo sách, đơn mua | backoffice | [Ảnh 1](../images/BO-06-1.jpg) |
| [BO-07](#bo-07) | Minor | 3 - Đơn mua | Form đơn mua ở màn hình 1024px | backoffice | [Ảnh 1](../images/BO-07-1.jpg) |
| [BO-08](#bo-08) | Minor | Tạo khuyến mãi | POST /promotions · form tạo khuyến mãi seller | promotion-service | [Ảnh 1](../images/BO-08-1.jpg) |
| [BO-09](#bo-09) | Minor | Khuyến mãi | GET /promotions/search?keyword= | promotion-service | Không có |
| [BO-10](#bo-10) | Minor | Nhà cung cấp | POST /api/v1/suppliers | inventory-service | Không có |
| [BO-11](#bo-11) | Minor | Đơn mua, nhập kho | POST /api/v1/inventory/import-stocks | inventory-service | Không có |

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
| **Trạng thái** | Đã sửa trên nhánh local `fix/bo-04-06-clear-error-messages` của backoffice, đã kiểm thử trên trình duyệt ngày 2026-11-12; chưa commit, chưa merge. Xem [kế hoạch](../fix-plans/backoffice/BO-04-promotion-form-generic-error-data-lost.md) |
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
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-05-price-input-drops-minus-sign.md) |
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
| **Trạng thái** | Đã sửa trên nhánh local `fix/bo-04-06-clear-error-messages` của backoffice, đã kiểm thử form sách trên trình duyệt ngày 2026-11-12; chưa commit, chưa merge. Xem [kế hoạch](../fix-plans/backoffice/BO-06-book-purchase-order-form-field-too-long.md) |
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
| **Trạng thái** | Chưa sửa. Phát hiện ngày 2026-11-14 khi retest. |
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

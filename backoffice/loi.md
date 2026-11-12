# Danh sách lỗi - Backoffice

| # | Mức độ | Luồng | Endpoint / Màn hình | Nghi ngờ thuộc | Ảnh |
|---|---|---|---|---|---|
| [BO-01](#bo-01) | Minor | 6 - Phân quyền | /forbidden · console admin | backoffice | [Ảnh 1](../images/BO-01-1.jpg) |
| [BO-02](#bo-02) | Minor | Storefront 7 - Khuyến mãi | PATCH /promotions/{id}/approve | promotion-service | [Ảnh 1](../images/BO-02-1.jpg) |
| [BO-03](#bo-03) | Minor | Storefront 7 - Khuyến mãi | Danh sách khuyến mãi | seller / promotion-service | [Ảnh 1](../images/BO-03-1.jpg) |
| [BO-04](#bo-04) | Minor (đã sửa, chưa merge) | Tạo khuyến mãi | Form tạo khuyến mãi seller | seller app | [Ảnh 1](../images/BO-04-1.jpg) |
| [BO-05](#bo-05) | Minor | 2, 3 - Sách, đơn mua | Ô giá của form tạo sách và đơn mua | backoffice | [Ảnh 1](../images/BO-05-1.jpg) |
| [BO-06](#bo-06) | Minor (đã sửa, chưa merge) | 2, 3 - Sách, đơn mua | Form tạo sách, đơn mua | backoffice | [Ảnh 1](../images/BO-06-1.jpg) |
| [BO-07](#bo-07) | Minor | 3 - Đơn mua | Form đơn mua ở màn hình 1024px | backoffice | [Ảnh 1](../images/BO-07-1.jpg) |

## BO-01

| Trường | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-01.md) |
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
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backend/BO-02.md) |
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
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-03.md) |
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
| **Trạng thái** | Đã sửa trên nhánh local `fix/bo-04-06-clear-error-messages` của backoffice, đã kiểm thử trên trình duyệt ngày 2026-11-12; chưa commit, chưa merge. Xem [kế hoạch](../fix-plans/backoffice/BO-04.md) |
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
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-05.md) |
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
| **Trạng thái** | Đã sửa trên nhánh local `fix/bo-04-06-clear-error-messages` của backoffice, đã kiểm thử form sách trên trình duyệt ngày 2026-11-12; chưa commit, chưa merge. Xem [kế hoạch](../fix-plans/backoffice/BO-06.md) |
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
| **Trạng thái** | Chưa sửa. Xem [kế hoạch](../fix-plans/backoffice/BO-07.md) |
| **Luồng** | 3 - Đơn mua |
| **Endpoint / Màn hình** | Form đơn mua ở màn hình 1024px |
| **Nghi ngờ thuộc** | backoffice |
| **Bước tái hiện** | Mở form đơn mua ở chiều rộng 1024px |
| **Mong đợi** | Các ô của dòng hàng đều bấm được |
| **Thực tế** | Dòng hàng phải cuộn ngang, ô Book bị đẩy khỏi tầm nhìn, dễ bấm nhầm ô Format |
| **Bằng chứng (status/body)** | Kiểm tra ở 1024px, bình thường ở 1600px |
| **API Response** | Không áp dụng |
| **Ảnh bằng chứng** | [BO-07-1.jpg](../images/BO-07-1.jpg) |

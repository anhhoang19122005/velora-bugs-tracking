# Seller tạo khuyến mãi

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Tên | 1 đến 255 ký tự | Rỗng |  |  |
| Mã | 1 đến 100 ký tự, chưa tồn tại | Rỗng |  |  |
| Mã |  | Đã tồn tại |  |  |
| Giảm % | Từ 1 đến 100 | Rỗng | Giảm % = 1 | Giảm % = 0 |
| Giảm % |  |  | Giảm % = 100 | Giảm % = 101 |
| Số lượng | Số lượng &gt;= 1 | Rỗng | Số lượng = 1 | Số lượng = 0 |
| Ngày | Bắt đầu &lt;= Kết thúc, Kết thúc &gt;= hôm nay | Bắt đầu &gt; Kết thúc | Kết thúc = hôm nay |  |
| Ngày |  | Kết thúc đã qua |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Tên | Data Input: Mã | Data Input: Giảm % | Data Input: Số lượng | Data Input: Bắt đầu | Data Input: Kết thúc | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Tạo khuyến mãi hợp lệ | Manual Test Promo | MANUAL1110 | 10 | 5 | 2026-11-10 | 2026-11-30 | 201, trạng thái PENDING chờ duyệt | 201, status PENDING, toast "Promotion created" | Pass | <pre>HTTP 201<br>{<br>  "id": 27,<br>  "code": "MANUAL1110",<br>  "discountPercent": 10,<br>  "quantity": 5,<br>  "status": "PENDING"<br>}</pre> |
| 2 | Invalid Partition | TC02 - Tên rỗng | "" | TC02CODE | 10 | 5 | 2026-11-10 | 2026-11-30 | Báo lỗi tại ô tên, không lưu | Hiện "Name is required", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Mã đã tồn tại | Trung ma | MANUAL1110 | 10 | 5 | 2026-11-10 | 2026-11-30 | Báo mã đã tồn tại (409) | 409, nhưng toast chỉ báo chung "conflicts with the current state", form đóng và mất dữ liệu đã nhập (Bug BO-04) | Fail | <pre>HTTP 409<br>{<br>  "error": "The request conflicts with the current state of the resource.",<br>  "code": "CONFLICT",<br>  "traceId": "ae3d30c7-effa-41da-b717-4be5cf98b0d4"<br>}</pre> |
| 4 | Invalid Partition | TC04 - Ngày bắt đầu sau ngày kết thúc | Sai ngay | TC04CODE | 10 | 5 | 2026-11-30 | 2026-11-10 | Báo lỗi ngày, không lưu | Không lưu, nhưng chỉ báo chung "invalid data", form đóng (Bug BO-04) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "7dfd215b-4401-419f-92e7-5cfddbf8dfdf"<br>}</pre> |
| 5 | Invalid Partition | TC05 - Ngày kết thúc đã qua | Qua han | TC05CODE | 10 | 5 | 2026-10-01 | 2026-10-31 | Báo ngày kết thúc phải từ hôm nay | Không lưu, nhưng chỉ báo chung "invalid data", form đóng (Bug BO-04) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "a6335f2e-b00f-4dc6-b871-a83d08ca8f6f"<br>}</pre> |
| 6 | Valid Boundary | TC06 - Giảm 1% | Bien 1 | TC06CODE | 1 | 5 | 2026-11-10 | 2026-11-30 | 201, tạo thành công | 201, trạng thái PENDING (id 28) | Pass | HTTP 201, id 28, code TC06CODE, status PENDING |
| 7 | Valid Boundary | TC07 - Giảm 100% | Bien 100 | TC07CODE | 100 | 5 | 2026-11-10 | 2026-11-30 | 201, tạo thành công | 201, trạng thái PENDING (id 29) | Pass | HTTP 201, id 29, code TC07CODE, status PENDING |
| 8 | Valid Boundary | TC08 - Số lượng 1 | So luong 1 | TC08CODE | 10 | 1 | 2026-11-10 | 2026-11-30 | 201, tạo thành công | 201, trạng thái PENDING (id 30) | Pass | HTTP 201, id 30, code TC08CODE, status PENDING |
| 9 | Invalid Boundary | TC09 - Giảm 0% | Bien 0 | TC09CODE | 0 | 5 | 2026-11-10 | 2026-11-30 | Báo giảm giá tối thiểu 1% | Không lưu, nhưng chỉ báo chung "invalid data", form đóng (Bug BO-04) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "3efe72a0-06da-4e9a-a0a5-f93c651f38f5"<br>}</pre> |
| 10 | Invalid Boundary | TC10 - Giảm 101% | Bien 101 | TC10CODE | 101 | 5 | 2026-11-10 | 2026-11-30 | Báo giảm giá tối đa 100% | Không lưu, nhưng chỉ báo chung "invalid data", form đóng (Bug BO-04) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "c4e8a60f-6b34-4355-84b9-00de7cef85f8"<br>}</pre> |
| 11 | Invalid Boundary | TC11 - Số lượng 0 | So luong 0 | TC11CODE | 10 | 0 | 2026-11-10 | 2026-11-30 | Báo số lượng tối thiểu 1 | Không lưu, nhưng chỉ báo chung "invalid data", form đóng (Bug BO-04) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "f3942dc1-f665-49a6-8d04-f1bd3074daef"<br>}</pre> |

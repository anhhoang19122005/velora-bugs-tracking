# Warehouse tạo đơn mua

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Nhà cung cấp | Đã chọn | Chưa chọn |  |  |
| Dòng hàng | Có sách và định dạng | Không có dòng hợp lệ |  |  |
| Dòng hàng |  | Thiếu sách hoặc định dạng |  |  |
| Số lượng | &gt;= 1 |  | Số lượng = 1 | Số lượng = 0 |
| Số lượng |  |  |  | Số lượng = -1 |
| Giá nhập | &gt;= 0 | Rỗng |  | Giá nhập = -1 |
| Ghi chú | &lt;= 1000 ký tự |  | &#124;ghi chú&#124; = 1000 | &#124;ghi chú&#124; = 1001 |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: NCC | Data Input: Sách, định dạng | Data Input: Số lượng | Data Input: Giá nhập | Data Input: Ghi chú | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Tạo đơn mua hợp lệ | Bảo Châu Books | Sach Hop Le, Bìa mềm | 10 | 50000 | 'n' x 1000 | 201, đơn ở trạng thái chờ duyệt | 201, PO-20261110-000025, PENDING | Pass | <pre>HTTP 201<br>{<br>  "id": 1,<br>  "poCode": "PO-20261110-000025",<br>  "status": "PENDING"<br>}</pre> |
| 2 | Invalid Partition | TC02 - Chưa chọn nhà cung cấp | "" | "" | "" | "" | "" | Báo lỗi tại ô nhà cung cấp | Hiện "Supplier is required", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Không có dòng hàng | Bảo Châu Books | "" | "" | "" | "" | Báo cần ít nhất một dòng | Hiện "An order needs at least one line." | Pass | Không gọi API |
| 4 | Invalid Partition | TC04 - Thiếu sách và định dạng | Bảo Châu Books | "" | 0 | 50000 | "" | Báo mỗi dòng cần sách và định dạng | Hiện "Every line needs a book and a format." | Pass | Không gọi API |
| 5 | Invalid Partition | TC05 - Giá nhập rỗng | Bảo Châu Books | Sach Hop Le, Bìa mềm | 10 | "" | 'n' x 1000 | Báo cần giá nhập | Hiện "Every line needs an import price." | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - Warehouse tự duyệt đơn | PO id 1 |  |  |  |  | 403, chỉ admin được duyệt | 403 FORBIDDEN | Pass | <pre>HTTP 403<br>{<br>  "error": "You do not have permission to perform this action",<br>  "code": "FORBIDDEN"<br>}</pre> |
| 7 | Valid Boundary | TC07 - Ghi chú đúng 1000 ký tự | Bảo Châu Books | Sach Hop Le, Bìa mềm | 10 | 50000 | 'n' x 1000 | 201, tạo thành công | 201, cùng lần với TC01 | Pass | <pre>HTTP 201<br>{<br>  "id": 1,<br>  "poCode": "PO-20261110-000025"<br>}</pre> |
| 8 | Invalid Boundary | TC08 - Số lượng 0 | Bảo Châu Books | Sach Hop Le, Bìa mềm | 0 | 50000 | "" | Báo số lượng tối thiểu 1 | Hiện "Every line needs a quantity of at least 1." | Pass | Không gọi API |
| 9 | Invalid Boundary | TC09 - Số lượng -1 | Bảo Châu Books | Sach Hop Le, Bìa mềm | -1 | 50000 | "" | Báo số lượng tối thiểu 1 | Hiện "Every line needs a quantity of at least 1." | Pass | Không gọi API |
| 10 | Invalid Boundary | TC10 - Giá nhập -1 | Bảo Châu Books | "" | 10 | -1 | "" | Báo giá nhập không được âm | Ô giá nhập tự đổi -1 thành 1 (Bug BO-05) | Fail | Không gọi API |
| 11 | Invalid Boundary | TC11 - Ghi chú 1001 ký tự | Bảo Châu Books | Sach Hop Le, Bìa mềm | 10 | 50000 | 'n' x 1001 | Báo ghi chú tối đa 1000 ký tự | 400, toast "invalid data". Chỉ báo chung lỗi dữ liệu, không chỉ ra trường sai (Bug BO-06) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "513ed059691647b9"<br>}</pre> |

# Seller tạo sách

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Tên sách | 1 đến 255 ký tự | Rỗng | &#124;tên&#124; = 255 | &#124;tên&#124; = 256 |
| Tác giả | 1 đến 100 ký tự | Rỗng |  | &#124;tác giả&#124; = 101 |
| Nhà cung cấp | Đã chọn | Chưa chọn |  |  |
| Danh mục | Có ít nhất 1 | Chưa chọn |  |  |
| Định dạng, giá | Có ít nhất 1 định dạng, giá &gt;= 0 | Chưa chọn định dạng | Giá = 0 | Giá = -1 |
| Ảnh | Đã tải ảnh | Chưa có ảnh |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Tên sách | Data Input: Tác giả | Data Input: NCC | Data Input: Danh mục | Data Input: Định dạng, giá | Data Input: Ảnh | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Tạo sách hợp lệ và hiện trên storefront | Sach Hop Le Manual 1110 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm, 99000 | PNG | 201, sách hiện đúng tên, giá, danh mục trên storefront | 201, id 50. Storefront hiện đúng tên, 99.000 đ, Kỹ năng sống | Pass | <pre>HTTP 201<br>{<br>  "id": 50,<br>  "slug": "sach-hop-le-manual-1110",<br>  "price": 99000,<br>  "stockQuantity": 0<br>}</pre> |
| 2 | Invalid Partition | TC02 - Tên rỗng | "" | "" | "" | "" | "" | "" | Báo lỗi tại ô tên, không gọi API | Hiện "Title is required", không gọi API | Pass | Không gọi API |
| 3 | Invalid Partition | TC03 - Tác giả rỗng | Sach Test Manual 1110 | "" | "" | "" | "" | "" | Báo lỗi tại ô tác giả | Hiện "Author is required", không gọi API | Pass | Không gọi API |
| 4 | Invalid Partition | TC04 - Chưa chọn nhà cung cấp | Sach Test Manual 1110 | Tac Gia Test | "" | "" | "" | "" | Báo lỗi tại ô nhà cung cấp | Hiện "Supplier is required", không gọi API | Pass | Không gọi API |
| 5 | Invalid Partition | TC05 - Chưa chọn danh mục | Sach Test Manual 1110 | Tac Gia Test | Bảo Châu Books | "" | "" | "" | Báo lỗi tại ô danh mục | Hiện "Categories is required", không gọi API | Pass | Không gọi API |
| 6 | Invalid Partition | TC06 - Chưa chọn định dạng | Sach Test Manual 1110 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | "" | "" | Báo lỗi tại dòng định dạng | Hiện "Every row needs a format.", không gọi API | Pass | Không gọi API |
| 7 | Invalid Partition | TC07 - Chưa có ảnh | Sach Test Manual 1110 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm | "" | Báo lỗi tại ô ảnh | Hiện "Image URL is required", không gọi API | Pass | Không gọi API |
| 8 | Valid Boundary | TC08 - Tên đúng 255 ký tự | 'T' x 255 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm, 0 | PNG | 201, tạo thành công | 201, id 51 | Pass | <pre>HTTP 201<br>{<br>  "id": 51,<br>  "title": "T x 255"<br>}</pre> |
| 9 | Valid Boundary | TC09 - Giá bằng 0 | 'T' x 255 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm, 0 | PNG | 201, tạo thành công | 201, id 51, giá 0 | Pass | <pre>HTTP 201<br>{<br>  "id": 51,<br>  "price": 0<br>}</pre> |
| 10 | Invalid Boundary | TC10 - Tên 256 ký tự | 't' x 256 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm, 99000 | PNG | Báo tên tối đa 255 ký tự | 400, không lưu. Chỉ báo chung lỗi dữ liệu, không chỉ ra trường sai (Bug BO-06) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "5115812f-d3df-44a1-8b56-846e46232f89"<br>}</pre> |
| 11 | Invalid Boundary | TC11 - Tác giả 101 ký tự | Sach Hop Le Manual 1110 | 'a' x 101 | Bảo Châu Books | Kỹ năng sống | Bìa mềm, 99000 | PNG | Báo tác giả tối đa 100 ký tự | 400, không lưu. Chỉ báo chung lỗi dữ liệu, không chỉ ra trường sai (Bug BO-06) | Fail | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "1dc4bc27-10b6-45df-ae9c-67cdaf48a578"<br>}</pre> |
| 12 | Invalid Boundary | TC12 - Giá âm | Sach Test Manual 1110 | Tac Gia Test | Bảo Châu Books | Kỹ năng sống | Bìa mềm, -1 | PNG | Báo giá không được âm, không lưu | Ô giá tự bỏ dấu trừ, lưu sách giá 1 đ, id 49 (Bug BO-05) | Fail | <pre>HTTP 201<br>{<br>  "id": 49,<br>  "slug": "sach-test-manual-1110",<br>  "price": 1<br>}</pre> |

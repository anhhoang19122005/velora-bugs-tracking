# HD-Phân quyền

[← Kết quả Guide me](../README.md)

Ma trận quyền cho các việc trong Guide me (4 vai trò). Gọi API qua gateway

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Vai trò | Đúng vai trò | Sai vai trò: 403 |  |  |
|  |  |  | Chưa đăng nhập: 401 |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: API | Data Input: Customer | Data Input: Seller | Data Input: Warehouse | Data Input: Admin | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM14-01 - Tạo danh mục | POST /api/v1/categories | 403 | 403 | 403 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:403, Admin:400 | Pass |  |
| 2 |  | GM14-02 - Tạo banner | POST /api/v1/banners | 403 | 403 | 403 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:403, Admin:400 | Pass |  |
| 3 |  | GM14-03 - Tạo sách | POST /api/v1/books | 403 | 201 | 403 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:400, Warehouse:403, Admin:400 | Pass |  |
| 4 |  | GM14-04 - Thêm phiên bản | POST /api/v1/book-variants | 403 | 201 | 403 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:400, Warehouse:403, Admin:400 | Pass |  |
| 5 |  | GM14-05 - Tạo khuyến mãi | POST /api/v1/promotions | 403 | 201 | 403 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:400, Warehouse:403, Admin:400 | Pass |  |
| 6 |  | GM14-06 - Duyệt khuyến mãi | PATCH /api/v1/promotions/{id}/approve | 403 | 403 | 403 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:403, Admin:404 | Pass |  |
| 7 |  | GM14-07 - Duyệt phiếu trả hàng | PATCH /api/v1/returns/{id}/approve | 403 | 200 | 403 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:404, Warehouse:403, Admin:404 | Pass |  |
| 8 |  | GM14-08 - Lập phiếu trả về kho | POST /api/v1/inventory/return-to-warehouse | 403 | 201 | Ghi thực tế (code: 403) | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:400, Warehouse:403, Admin:400 | Pass |  |
| 9 |  | GM14-09 - Duyệt trả về kho | PATCH /api/v1/inventory/return-to-warehouse/{id}/approve | 403 | 403 | 200 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:404, Admin:404 | Pass |  |
| 10 |  | GM14-10 - Thêm nhà cung cấp | POST /api/v1/suppliers | 403 | 403 | 201 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:400, Admin:400 | Pass |  |
| 11 |  | GM14-11 - Tạo yêu cầu nhập | POST /api/v1/inventory/stock-requests | 403 | 403 | 201 | 201 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:400, Admin:400 | Pass |  |
| 12 |  | GM14-12 - Duyệt yêu cầu nhập | PATCH /api/v1/inventory/stock-requests/{id}/approve | 403 | 403 | 403 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:403, Admin:404 | Pass |  |
| 13 |  | GM14-13 - Duyệt / đặt đơn mua | PATCH /api/v1/purchase-orders/{id}/approve, pay | 403 | 403 | 403 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Customer:403, Seller:403, Seller:403, Warehouse:403, Warehouse:403, Admin:404, Admin:404 | Pass |  |
| 14 |  | GM14-14 - Nhận hàng | POST /api/v1/inventory/import-stocks/{id}/receive | 403 | 403 | 200 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:404, Admin:404 | Pass |  |
| 15 |  | GM14-15 - Duyệt thanh lý | PATCH /api/v1/inventory/disposals/{id}/approve | 403 | 403 | 403 | 200 | Đúng theo bảng. | Đúng theo bảng. Vai trò không được phép gửi dữ liệu hợp lệ (phải 403); vai trò được phép gửi dữ liệu rỗng hoặc id không tồn tại (400/404 nghĩa là đã qua phân quyền, không tạo bản ghi). Mã: Customer:403, Seller:403, Warehouse:403, Admin:404 | Pass |  |
| 16 | Invalid Partition | GM14-16 - Chưa đăng nhập gọi các API trên | tất cả API trên | 401 | 401 | 401 | 401 | Không có token: 401, không đổi dữ liệu. | Tất cả trả 401 | Pass |  |

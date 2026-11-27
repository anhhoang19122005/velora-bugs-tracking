# HD-Nút Guide me

[← Tổng quan đợt test](README.md)

Bản thân chức năng Guide me

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Hiển thị | Seller, Warehouse có nút ? | Admin: chưa có bài nào nên không có nút ? |  |  |
|  | Điều kiện trước | Đủ dữ liệu | Thiếu: gợi ý bài tạo trước |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Ứng dụng / Vai trò | Data Input: Bài hướng dẫn | Data Input: Thao tác | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM15-01 - Danh sách bài của Seller | Seller | Nút ? | Mở danh sách | Có bài thêm sách, phiên bản, khuyến mãi, trả hàng và luồng đăng bán. Bài danh mục và banner không dành cho tài khoản chỉ có vai trò Seller. | Các bài với tài khoản Seller: ['Add a book', 'Add a format and its price', 'Create a promotion', 'Process a customer return', 'List a book for sale', "I'll look around myself"]. Không có bài danh mục và banner (đúng, đó là việc của Admin) | Pass |  |
| 2 |  | GM15-02 - Danh sách bài của Warehouse | Warehouse | Nút ? | Mở danh sách | Có bài nhà cung cấp, yêu cầu, đơn mua, nhận hàng, trả về kho, thanh lý và luồng đầy đủ. | Các bài: ['Add a supplier', 'Raise a stock request', 'Turn a request into a purchase order', 'Receive goods into the warehouse', 'Approve goods coming back', 'Write stock off', 'Restocking, end to end', "I'll look around myself"] | Pass |  |
| 3 |  | GM15-03 - Bước của Admin hiện cho Warehouse | Warehouse | Yêu cầu nhập hàng | Chạy tới bước duyệt | Bước duyệt hiện như thông tin, không yêu cầu Warehouse bấm; tên bài có thể là bản xem lại. | Bắt đầu bài "Raise a stock request" bằng tài khoản Warehouse; tour dừng ở bước cần thao tác thật (lưu phiếu) nên chỉ đi được: ['Step 1 of 10']. Không xác minh được hiển thị bước duyệt của Admin bằng tự động hoá<br>[Ảnh 1](images/GM15-03-1.png) | Blocked |  |
| 4 |  | GM15-04 - Đi hết một bài có lưu dữ liệu | Seller | Thêm sách | Làm theo từng bước | Khung chỉ đúng ô; chỉ sang bước tiếp sau khi lưu thành công; cuối bài chỉ vào đúng dòng vừa tạo. | Đi bài "Add a supplier" (thay cho bài Thêm sách vì bài đó cần tải ảnh bìa và chọn nhiều ô phức tạp) bằng tài khoản Warehouse, có ảnh từng bước. Diễn biến: ['1/8 Open the supplier form', '2/8 Company name', '3/8 Email', '4/8 Phone', '5/8 Address', '6/8 Active', '7/8 Save it', 'Lưu: HTTP 201', '8/8 This one is yours']. Nhà cung cấp được tạo: True; dòng mới trên danh sách: False | Pass |  |
| 5 | Invalid Partition | GM15-05 - Lưu thất bại giữa bài | Seller | Thêm sách | Bỏ ảnh bìa rồi bấm Lưu | Bài không nhảy sang bước sau; lỗi form vẫn nhìn thấy, không bị khung che. | Bỏ trống tên, bấm Lưu ở bước 7: Lưu: form chặn, không gửi request. Thẻ hướng dẫn vẫn ở bước 7 (không nhảy bước); ô tên báo lỗi: True (xem ảnh) | Pass |  |
| 6 |  | GM15-06 - Thiếu điều kiện trước | Warehouse | Yêu cầu nhập khi chưa có nhà cung cấp | Bắt đầu bài | Được gợi ý chạy bài Thêm nhà cung cấp trước. | Không chạy: phải xoá hết nhà cung cấp trên cơ sở dữ liệu dùng chung mới tạo được điều kiện này | Blocked |  |
| 7 |  | GM15-07 - Admin app | Admin | (không có) | Tìm nút ? | Không có nút (danh sách bài đang rỗng). Bài của Admin chưa được viết. | Nút trên thanh trên cùng của ứng dụng Admin: ['Notifications, 9 unread', 'Account menu']. Không có nút Guide (đúng với mã nguồn: danh sách bài của Admin đang rỗng) | Pass |  |

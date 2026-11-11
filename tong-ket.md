# Báo cáo kiểm thử manual

Ô màu vàng là ô cần điền. Các số trong phần Kết quả tự tính từ sheet Luồng và Lỗi, không sửa tay.

## Thông tin đợt test

| Mục | Giá trị |
|---|---|
| Đợt test / phạm vi | Manual  test for  storefront và backoffice - đợt 1: đã chạy 13/14 luồng, 1 luồng Backoffice chưa chạy theo yêu cầu |
| Ngày (YYYY-MM-DD) | 2026-11-10 |
| Người test | Hà Hoàng Anh &amp; Claude. Remote Browser for testing |
| Môi trường | local |
| URL storefront | http://localhost:3003 |
| URL admin | http://localhost:3000 |
| URL seller | http://localhost:3002 |
| URL warehouse | http://localhost:3001 |
| URL gateway | http://localhost:8080 |
| Commit backend | 1364ff5 |
| Commit backoffice | 02da243d |
| Commit storefront | ebfeecd |
| Stack build mới từ nhánh đang test | Có |
| Trình duyệt / kích thước màn hình | Built-in browser, 1024x768 và 375x812 |
| Tài khoản test theo vai trò (không ghi mật khẩu) | Khách: testing2@gmail.com. Seller: seller@gmail.com. Admin: admin@gmail.com. Warehouse: warehouse@gmail.com |

## Kết quả (tự tính)

| Mục | Giá trị |
|---|---|
| Tổng số luồng | 14 |
| Pass | 11 |
| Fail | 2 |
| Blocked | 0 |
| Chưa chạy | 1 |
| Luồng chưa chọn trạng thái | 0 |
| Lỗi Blocker | 0 |
| Lỗi Major | 10 |
| Lỗi Minor | 13 |
| Kết luận | Không đạt |
| Kết luận | Không đạt |
| Rủi ro còn lại / phần chưa test | • Luồng số 5 ở Backoffice-Luồng (quản lý tài khoản, quyền) chưa chạy.<br>• 3 test case Blocked (WB05 Checkout, WB06 và WB07 Áp mã).<br>• VNPAY không chuyển được sang cổng.<br>• Mã giảm giá không dùng được khi đặt hàng.<br>• Email xác thực đến không ổn định. |
| Ghi chú | CẤU HÌNH (đặt qua biến môi trường, không sửa code)<br>• CORS_ALLOWED_ORIGINS cổng 3000-3003 cho gateway<br>• NOTIFICATION_MONGO_URI = MONGO_URI<br>• SPRING_MVC_LOG_RESOLVED_EXCEPTION=true cho order-service<br><br>DỮ LIỆU TEST TRONG DB CLOUD – ĐỢT 1<br>• Đơn ORD-20261110-000020 (Returned, RMA-20261110-000002), -000021 và -000022 (Cancelled)<br>• Địa chỉ id 24<br>• Khuyến mãi MANUAL1110 (id 27, ACTIVE)<br>• Tài khoản manual-20261110@taschen.test (chưa xác thực)<br><br>ĐỢT CHẠY THÊM<br>• Đơn -000023 (Cancelled), -000024 và -000025 (Completed, RMA -000003 và -000004 chờ duyệt)<br>• Địa chỉ id 25-27<br>• Khuyến mãi TC06CODE, TC07CODE, TC08CODE (PENDING), MINORDER1110 (ACTIVE)<br>• Tài khoản tc09 (đã xác thực), tc10 (chưa xác thực)<br><br>ĐỢT LUỒNG 9-11<br>• Sách id 49, 50, 51<br>• PO-20261110-000025, -000026<br>• Phiếu nhập IMP-20261110-000017, -000018<br>• Yêu cầu kho id 1 (PENDING, tạo dư do lỗi script kiểm thử) và STK-20261110-000018<br>• RTW-20261110-000020<br>• Tồn sách id 50 là 12, tồn sách id 46 tăng thêm 1<br>• 3 ảnh test trên R2<br><br>CÁCH CHẠY<br>• API Response đã bỏ timestamp để gọn.<br>• Một số ca nhập dữ liệu bằng script chạy ngay trong trang của trình duyệt thật, hộp trắng gọi API từ trình duyệt.<br>• Form tạo sách và đơn mua chạy trên giao diện; nhập kho, yêu cầu kho, trả kho gọi API của console từ trình duyệt. |

## Test case hộp đen (tự tính)

| Mục | Giá trị |
|---|---|
| Pass | 91 |
| Fail | 16 |
| Blocked | 0 |
| Chưa chạy | 0 |

## Test case hộp trắng (tự tính)

| Mục | Giá trị |
|---|---|
| Pass | 16 |
| Fail | 4 |
| Blocked | 3 |
| Chưa chạy | 0 |

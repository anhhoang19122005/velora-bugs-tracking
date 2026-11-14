# Kết quả test tính bất biến - Storefront và Backoffice

Ngày 2026-11-14. Gửi request đồng thời bằng script gọi API, trừ kịch bản 5 chạy trên giao diện. Dữ liệu test đã được hủy hoặc dọn; chi tiết nằm ở trang Tổng kết của file Excel.

| # | Kịch bản | Cách chạy | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Bug # | Chi tiết / API Response |
|---|---|---|---|---|---|---|---|
| 1 | Đặt hàng COD, 2 request giống nhau cùng lúc | Script gửi request song song (barrier) x2 | 1 đơn, tồn trừ 1 lần | 2 đơn, tồn 49 xuống 47 | Fail | SF-37 | 201 x2, đơn 40 và 41 |
| 2 | Đặt hàng COD, 3 request cùng lúc | Script gửi request song song (barrier) x3 | 1 đơn | 3 đơn, tồn 47 xuống 44 | Fail | SF-37 | 201 x3, đơn 42 đến 44 |
| 3 | Đặt hàng COD, 10 request cùng lúc | Script gửi request song song (barrier) x10 | 1 đơn | 10 đơn, tồn 44 xuống 34 | Fail | SF-37 | 201 x10, đơn 45 đến 54 |
| 4 | Đặt hàng, body có số lượng khác giỏ | Script gửi request song song (barrier) x3 (số lượng 1, 2, 3) | Chỉ số lượng khớp giỏ được tạo | 1 đơn, 2 request 400 | Pass | 'Storefront-Lỗi'!A9:L9 | 201 x1, 400 x2 |
| 5 | Giao diện: click chuột 3 lần liên tiếp nút Đặt hàng | Trình duyệt, triple click | 1 đơn | 1 request POST /orders, 1 đơn (đơn 67) | Pass | 'Storefront-Lỗi'!A17:L17 | Nút đã chặn click lặp trên giao diện |
| 6 | Hủy cùng một đơn 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409, tồn hoàn 1 lần | Đơn CANCELLED, tồn 33 xuống 32 rồi về 33 (đúng); 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 7 | Seller chuyển PROCESSING 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Đổi trạng thái một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 8 | Seller chuyển DELIVERING 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Đổi trạng thái một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 9 | Khách bấm Đã nhận hàng 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Đơn COMPLETED và PAID đúng một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 10 | Tạo yêu cầu đổi trả 5 lần cùng lúc cho 1 dòng hàng | Script gửi request song song (barrier) x5 | 1 yêu cầu | Tạo 5 yêu cầu (RMA -000006 đến -000010) | Fail | SF-40 | 201 x5 |
| 11 | Duyệt yêu cầu đổi trả 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Duyệt một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 12 | Nhận hàng trả 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Đơn RETURNED và REFUNDED một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 13 | Duyệt và nhận hàng 4 yêu cầu đổi trả trùng còn lại | Script gửi lần lượt | Bị từ chối vì dòng hàng đã trả hết | Cả 4 duyệt và nhận được; dòng hàng returnedQuantity 5 trên 1 | Fail | SF-40 | 200 x8 |
| 14 | Tạo yêu cầu đổi trả thứ hai cho cùng dòng hàng | Script gửi lần lượt | 409 | 409 | Pass |  | Lần lượt thì bị chặn |
| 15 | Mã còn 1 lượt, 2 người đặt cùng lúc | Script gửi request song song (barrier) x2 (hai tài khoản) | 1 đơn được giảm | Cả 2 đơn giảm 19.300 đ | Fail | SF-38 | 201 x2, quantity mã về 0 |
| 16 | Một người, mã còn 3 lượt, đặt 3 lần cùng lúc | Script gửi request song song (barrier) x3 | 1 đơn được giảm | 3 đơn giảm, quantity mã 3 xuống 2 | Fail | SF-38 | 201 x3 |
| 17 | Đặt đơn thứ hai bằng mã đã dùng | Script gửi lần lượt | 400 | 400 | Pass |  | Lần lượt thì bị chặn |
| 18 | Tồn 43, hai người mỗi người đặt 26 cuốn cùng lúc | Script gửi request song song (barrier) x2 (hai tài khoản) | 1 đơn thành công, đơn kia báo hết hàng ngay | 2 request 201; inventory chỉ giữ hàng 1 đơn (43 xuống 17), đơn còn lại tự hủy sau 0,9 giây. Không bán vượt, nhưng khách bị báo thành công trước | Fail | SF-39 | 201 x2 |
| 19 | Tồn 17, một người đặt 26 cuốn 3 lần cùng lúc | Script gửi request song song (barrier) x3 | 409 | 409 x3 | Pass |  | Không bán vượt khi tồn đã thấp hơn số đặt |
| 20 | Hủy 16 đơn, kiểm sổ tồn kho | Script gửi lần lượt | Tồn hoàn đúng | Hoàn đúng từng đơn | Pass |  | Tồn 48 sau khi hủy, khớp số trừ |
| 21 | Đăng ký cùng email 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 tài khoản, 4 request 409 | 1 tài khoản, 1 email xác thực; 4 request trả 500 | Fail | SF-41 | 201 x1, 500 x4 |
| 22 | Xác thực email 5 lần cùng lúc với một token | Script gửi request song song (barrier) x5 | 1 request 200 | Xác thực một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 23 | Tạo 3 địa chỉ mặc định cùng lúc | Script gửi request song song (barrier) x3 | Chỉ 1 địa chỉ mặc định | Còn 1 địa chỉ mặc định; 2 request trả 500 | Fail | SF-41 | 201 x1, 500 x2 |
| 24 | Thêm cùng một sách vào giỏ 5 lần cùng lúc | Script gửi request song song (barrier) x5 | Giỏ có 5 cuốn | Cả 5 request 200 nhưng giỏ chỉ có 1 cuốn | Fail | SF-42 | 200 x5 |
| 25 | Khởi tạo thanh toán VNPay 3 lần cùng lúc | Script gửi request song song (barrier) x3 | 1 bản ghi thanh toán | 3 bản ghi PENDING | Fail | SF-43 | 200 x3, payments id 9, 10, 11 |
| 26 | Khởi tạo thanh toán VNPay 3 lần lần lượt | Script gửi lần lượt | 1 bản ghi thanh toán | 1 bản ghi PENDING (dùng lại) | Pass |  | 200 x3, 1 bản ghi |
| 27 | Duyệt cùng một khuyến mãi 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | ACTIVE một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 28 | Tạo nhà cung cấp cùng tên và email 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 nhà cung cấp | 5 nhà cung cấp trùng | Fail | BO-10 | 201 x5, đã xóa sau test |
| 29 | Duyệt đơn mua 5 lần cùng lúc (admin) | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Duyệt một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 30 | Thanh toán đơn mua 5 lần cùng lúc (admin) | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Thanh toán một lần; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 31 | Tạo 3 phiếu nhập cho cùng một đơn mua cùng lúc | Script gửi request song song (barrier) x3 | 1 phiếu nhập | 3 phiếu nhập; chỉ 1 phiếu nhận được hàng | Fail | BO-11 | 201 x3 |
| 32 | Tạo phiếu nhập thứ hai cho cùng đơn mua | Script gửi lần lượt | 409 | 409 | Pass |  | Lần lượt thì bị chặn |
| 33 | Nhận hàng 5 lần cùng lúc trên một phiếu nhập | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | Tồn tăng đúng +1; 4 request trả 500 | Fail | SF-41 | 200 x1, 500 x4 |
| 34 | Duyệt yêu cầu trả hàng về kho 5 lần cùng lúc | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | 200 x1, 409 x4, tồn +1 | Pass |  | Đúng như kỳ vọng |
| 35 | Hủy đơn mua 5 lần cùng lúc (admin) | Script gửi request song song (barrier) x5 | 1 request 200, còn lại 409 | 409 x5 vì đơn mua chưa ở trạng thái hủy được; chưa xác định điều kiện | Blocked |  | Cần PO ở trạng thái cho phép hủy |

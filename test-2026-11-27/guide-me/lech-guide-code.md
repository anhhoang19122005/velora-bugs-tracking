# Chỗ lời hướng dẫn Guide me khác với code

[← Kết quả Guide me](README.md)

Danh sách được suy ra từ đọc code trước khi test; cột cuối là kết luận sau khi chạy.

| Mã | Guide me nói | Code làm | Case ở sheet | Kết luận sau khi test |
|---|---|---|---|---|
| G-01 | Yêu cầu nhập đi: Chờ xử lý, Đã duyệt, Đã đặt hàng, Đã nhận | StockRequestStatus chỉ có PENDING, APPROVED, REJECTED, ORDERED | HD-Yêu cầu nhập | Xác nhận (GM08-04) |
| G-02 | Quản trị quyết số lượng cuối cùng | API duyệt yêu cầu chỉ nhận lời nhắn | HD-Yêu cầu nhập | Xác nhận (GM08-03) |
| G-03 | Khuyến mãi áp dụng từ ngày bắt đầu | Tạo ra ở PENDING, cần Admin duyệt; guide không nhắc | HD-Khuyến mãi | Xác nhận (mã PENDING, khách chưa dùng được; guide không nhắc duyệt) (GM05-01) |
| G-04 | Khuyến mãi không giới hạn có thể lỗ (ngụ ý được để trống) | quantity bắt buộc, &gt;= 1 | HD-Khuyến mãi | Xác nhận (GM05-05) |
| G-05 | Mã viết hoa, không dấu cách (danh mục, khuyến mãi) | Request chỉ kiểm rỗng và độ dài; không thấy chuẩn hoá chữ hoa | HD-Danh mục, HD-Khuyến mãi | Xác nhận (GM01-06, GM05-06) |
| G-06 | Danh mục: không nói là bắt buộc | Sách bắt buộc ít nhất 1 danh mục | HD-Thêm sách | Hệ thống báo lỗi rõ; chỉ thiếu ở lời hướng dẫn (GM02-03) |
| G-07 | Phiên bản có ô tồn kho ban đầu | Catalog nhận stockQuantity nhưng kho thật là lô ở inventory; request tạo sách ghi tồn bắt đầu từ 0 | HD-Phiên bản &amp; giá | Xác nhận: tồn ảo trên storefront (GM03-02) |
| G-08 | Lý do thanh lý một dòng | Bắt buộc 30 đến 1000 ký tự | HD-Thanh lý | Form báo rõ "at least 30 characters"; chỉ thiếu ở lời hướng dẫn (GM12-05) |
| G-09 | Bấm Đã nhận thì tiền đã hoàn | Chỉ mở khoản hoàn; chi trả phải ghi nhận tay | HD-Xử lý trả hàng | Xác nhận (GM06-04) |
| G-10 | (không nói) | Không thấy chặn lập nhiều phiếu về kho cho một yêu cầu trả; bảng chống trùng đã bị xoá ở migration V12; không đối chiếu số lượng | HD-Xử lý trả hàng, HD-Duyệt trả về kho | Xác nhận: tồn bị cộng 2 lần cho 1 cuốn trả (GM06-07, GM06-08, GM11-04) |
| G-11 | Duyệt thì tồn tăng ngay | Nếu sách không có lô nào, bỏ qua cộng kho nhưng phiếu vẫn APPROVED | HD-Duyệt trả về kho | Xác nhận (GM11-03) |
| G-12 | Nhà cung cấp ngừng hoạt động không chọn được trên đơn mua | Không thấy kiểm trạng thái khi tạo đơn mua ở API | HD-Nhà cung cấp | Xác nhận (qua API) (GM07-03) |
| G-13 | Bước duyệt: chỉ khi đó mới nhận hàng về được | Phải ORDERED (sau bước Thanh toán) mới nhận được | HD-Đơn mua | Xác nhận (GM09-03) |
| G-15 | Banner tắt vẫn lưu được, bật khi ảnh và đường dẫn đúng | BannerRequest chỉ có name và imageUrl | HD-Banner | Xác nhận (GM04-02) |
| G-16 | Từ chối: đơn đóng lại ở đó | Khách vẫn tạo được phiếu mới vì chỉ chặn khi còn phiếu PENDING/APPROVED | HD-Xử lý trả hàng | Xác nhận (GM06-03) |
| G-17 | Mỗi phiên bản có tồn kho riêng | order.placed gửi variantId = null, kho trừ theo sách | HD-Khách kiểm chứng | Không tái hiện: checkout chặn đúng theo định dạng (GM13-09) |

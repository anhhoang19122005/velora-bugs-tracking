# Đợt test 2026-11-27: nghiệp vụ 4 vai trò theo Guide me

Bộ case dựng từ chức năng Guide me (Customer, Seller, Warehouse, Admin). Đợt này để riêng, chưa gộp vào [bảng trạng thái chung](../trang-thai.md) và không đổi mã bug SF/BO đã có.

## Kết quả

| Tổng case | Pass | Fail | Blocked | Lỗi | Major | Minor |
|---|---|---|---|---|---|---|
| 162 | 141 | 18 | 3 | 15 | 7 | 8 |

## Lỗi

| # | Mức độ | Loại | Lỗi | Liên quan bug cũ |
|---|---|---|---|---|
| [B01](loi.md#b01) | Major | Lỗi chức năng | Một yêu cầu trả hàng lập được nhiều phiếu trả về kho, và số lượng không được đối chiếu: tồn kho bị cộng nhiều lần | Gần giống [SF-40](../storefront/loi.md#sf-40) (trùng yêu cầu đổi trả), nhưng lỗi này nằm ở bước lập phiếu trả về kho |
| [B02](loi.md#b02) | Major | Lỗi chức năng | Mã khuyến mãi chỉ còn 1 lượt nhưng 2 khách đặt cùng lúc đều được giảm | Trùng [SF-38](../storefront/loi.md#sf-38): ngày 2026-11-27 vẫn còn lỗi |
| [B03](loi.md#b03) | Major | Lỗi chức năng | Trang chủ storefront sập hoàn toàn khi một sách có ảnh bìa từ host không khai báo |  |
| [B04](loi.md#b04) | Major | Lỗi chức năng | Tồn kho ban đầu nhập ở phiên bản hiện "còn 10" trên storefront nhưng không có hàng thật | Gần giống [SF-35](../storefront/loi.md#sf-35) (tồn hiển thị sai), nhưng SF-35 nghi do cache |
| [B05](loi.md#b05) | Major | Lỗi chức năng | Giá nhập bằng 0 gây lỗi 500 thay vì báo lỗi kiểm tra |  |
| [B06](loi.md#b06) | Major | Lỗi chức năng | Tạo được đơn mua với nhà cung cấp đã ngừng hoạt động (qua API) |  |
| [B07](loi.md#b07) | Major | Lỗi chức năng | Duyệt trả về kho cho sách chưa có lô: phiếu báo APPROVED nhưng hàng không vào kho, không có lỗi |  |
| [B08](loi.md#b08) | Minor | Lỗi chức năng | Mã danh mục và mã khuyến mãi nhận chữ thường và dấu cách, trái với hướng dẫn | Trùng một phần [BO-08](../backoffice/loi.md#bo-08) (mã khuyến mãi); phần mã danh mục là mới |
| [B09](loi.md#b09) | Minor | Nội dung Guide me | Guide me nói banner có nút bật/tắt và đường dẫn, nhưng form không có |  |
| [B10](loi.md#b10) | Minor | Nội dung Guide me | Tip số lượt ngụ ý được tạo khuyến mãi không giới hạn, nhưng hệ thống bắt buộc số lượt |  |
| [B11](loi.md#b11) | Minor | Nội dung Guide me | Guide me nói từ chối thì đơn đóng lại, nhưng khách vẫn gửi được yêu cầu mới |  |
| [B12](loi.md#b12) | Minor | Nội dung Guide me | Guide me nói bấm Đã nhận thì "tiền đã hoàn", thực tế chỉ mở khoản hoàn chờ chi |  |
| [B13](loi.md#b13) | Minor | Nội dung Guide me | Guide me nói Admin quyết số lượng cuối cùng, nhưng không có chỗ sửa số lượng khi duyệt |  |
| [B14](loi.md#b14) | Minor | Nội dung Guide me | Guide me mô tả trạng thái cuối "Đã nhận" cho yêu cầu nhập, hệ thống không có trạng thái này |  |
| [B15](loi.md#b15) | Minor | Nội dung Guide me | Guide me bước duyệt nói duyệt xong là nhận hàng được, thực tế phải qua bước Thanh toán |  |

## Các file

| File | Nội dung | Pass | Fail | Blocked |
|---|---|---|---|---|
| [loi.md](loi.md) | Chi tiết 15 lỗi |  |  |  |
| [luong.md](luong.md) | 6 luồng đầu-cuối |  |  |  |
| [lech-guide-code.md](lech-guide-code.md) | Guide me khác code |  |  |  |
| [hd-danh-muc.md](hd-danh-muc.md) | HD-Danh mục | 8 | 1 | 0 |
| [hd-them-sach.md](hd-them-sach.md) | HD-Thêm sách | 13 | 0 | 0 |
| [hd-phien-ban-gia.md](hd-phien-ban-gia.md) | HD-Phiên bản & giá | 7 | 1 | 0 |
| [hd-banner.md](hd-banner.md) | HD-Banner | 4 | 1 | 1 |
| [hd-khuyen-mai.md](hd-khuyen-mai.md) | HD-Khuyến mãi | 13 | 3 | 0 |
| [hd-xu-ly-tra-hang.md](hd-xu-ly-tra-hang.md) | HD-Xử lý trả hàng | 9 | 4 | 0 |
| [hd-nha-cung-cap.md](hd-nha-cung-cap.md) | HD-Nhà cung cấp | 8 | 1 | 0 |
| [hd-yeu-cau-nhap.md](hd-yeu-cau-nhap.md) | HD-Yêu cầu nhập | 10 | 2 | 0 |
| [hd-don-mua.md](hd-don-mua.md) | HD-Đơn mua | 11 | 2 | 0 |
| [hd-nhan-hang.md](hd-nhan-hang.md) | HD-Nhận hàng | 12 | 0 | 0 |
| [hd-duyet-tra-ve-kho.md](hd-duyet-tra-ve-kho.md) | HD-Duyệt trả về kho | 5 | 2 | 0 |
| [hd-thanh-ly.md](hd-thanh-ly.md) | HD-Thanh lý | 11 | 0 | 0 |
| [hd-khach-kiem-chung.md](hd-khach-kiem-chung.md) | HD-Khách kiểm chứng | 9 | 1 | 0 |
| [hd-phan-quyen.md](hd-phan-quyen.md) | HD-Phân quyền | 16 | 0 | 0 |
| [hd-nut-guide-me.md](hd-nut-guide-me.md) | HD-Nút Guide me | 5 | 0 | 2 |

Ảnh của các case Fail và Blocked nằm ở [images](images/). API response của từng case nằm ở [api](api/).

## Môi trường

| Mục | Chi tiết |
|---|---|
| Hệ thống | Local: 9 service chạy native (profile dev) nối vào Neon, Upstash, MongoDB Atlas, CloudAMQP dùng chung trong taschen-platform/.env; Mailpit trong Docker |
| Commit backend | develop d5b6ac2 |
| Commit backoffice | develop 8e1ecfbe |
| Commit storefront | develop 0a72cc4 |
| Công cụ | Playwright (Chromium 1440×900) cho giao diện, script gọi API qua gateway cho kiểm tra biên và phân quyền |
| Người test | Claude Code (chạy tự động bằng Playwright và API qua gateway), theo yêu cầu của người dùng |

## Case bị chặn

| Case | Lý do |
|---|---|
| GM04-03 | Bỏ qua phần hiển thị cắt ảnh (cần ảnh dọc thật); lưu banner hoạt động như case 1 |
| GM15-03 | Bắt đầu bài "Raise a stock request" bằng tài khoản Warehouse; tour dừng ở bước cần thao tác thật (lưu phiếu) nên chỉ đi được: ['Step 1 of 10']. Không xác minh được hiển thị bước duyệt của Admin bằng tự động hoá |
| GM15-06 | Không chạy: phải xoá hết nhà cung cấp trên cơ sở dữ liệu dùng chung mới tạo được điều kiện này |

## Lưu ý

- CloudAMQP dùng chung có một máy khác cùng nghe hàng đợi của notification, catalog và payment, nên kết quả liên quan đến sự kiện có thể bị ảnh hưởng.
- Lỗi B03 lộ ra do sách id 61 `QA-BOOK-20261127` (ảnh ở host `x.test`) không do đợt test này tạo.
- Chưa test thanh toán SePay và ghi nhận chi trả hoàn tiền.
- Sau khi chạy, nhóm dữ liệu đầu đợt có tên `[GM-TEST-11271102]` đã được dọn (sách xoá mềm, banner và danh mục đã xoá, 3 tài khoản bị vô hiệu hoá). Ảnh và API response vẫn phản ánh trạng thái lúc test.
- Video quay phiên test không đưa lên repo; file nằm ở máy chạy test.

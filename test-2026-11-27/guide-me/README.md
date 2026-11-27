# Guide me: nghiệp vụ 4 vai trò

[← Đợt test 2026-11-27](../README.md)

Bộ case dựng từ chức năng Guide me (Customer, Seller, Warehouse, Admin). Mỗi lỗi B01–B15 đã có mã theo dõi SF/BO trong [bảng trạng thái chung](../../trang-thai.md); B02 và B08 trùng lỗi đã có nên ghi vào mã cũ.

## Kết quả

| Tổng case | Pass | Fail | Blocked | Lỗi | Major | Minor |
|---|---|---|---|---|---|---|
| 162 | 141 | 18 | 3 | 15 | 7 | 8 |


## Lỗi

| # | Mã theo dõi | Mức độ | Loại | Lỗi | Liên quan bug cũ |
|---|---|---|---|---|---|
| [B01](loi.md#b01) | [BO-13](../../backoffice/loi.md#bo-13) | Major | Lỗi chức năng | Một yêu cầu trả hàng lập được nhiều phiếu trả về kho, và số lượng không được đối chiếu: tồn kho bị cộng nhiều lần | Gần giống [SF-40](../../storefront/loi.md#sf-40) (trùng yêu cầu đổi trả), nhưng lỗi này nằm ở bước lập phiếu trả về kho |
| [B02](loi.md#b02) | [SF-38](../../storefront/loi.md#sf-38) | Major | Lỗi chức năng | Mã khuyến mãi chỉ còn 1 lượt nhưng 2 khách đặt cùng lúc đều được giảm | Trùng [SF-38](../../storefront/loi.md#sf-38): ngày 2026-11-27 vẫn còn lỗi |
| [B03](loi.md#b03) | [SF-45](../../storefront/loi.md#sf-45) | Major | Lỗi chức năng | Trang chủ storefront sập hoàn toàn khi một sách có ảnh bìa từ host không khai báo |  |
| [B04](loi.md#b04) | [SF-46](../../storefront/loi.md#sf-46) | Major | Lỗi chức năng | Tồn kho ban đầu nhập ở phiên bản hiện "còn 10" trên storefront nhưng không có hàng thật | Gần giống [SF-35](../../storefront/loi.md#sf-35) (tồn hiển thị sai), nhưng SF-35 nghi do cache |
| [B05](loi.md#b05) | [BO-14](../../backoffice/loi.md#bo-14) | Major | Lỗi chức năng | Giá nhập bằng 0 gây lỗi 500 thay vì báo lỗi kiểm tra |  |
| [B06](loi.md#b06) | [BO-15](../../backoffice/loi.md#bo-15) | Major | Lỗi chức năng | Tạo được đơn mua với nhà cung cấp đã ngừng hoạt động (qua API) |  |
| [B07](loi.md#b07) | [BO-16](../../backoffice/loi.md#bo-16) | Major | Lỗi chức năng | Duyệt trả về kho cho sách chưa có lô: phiếu báo APPROVED nhưng hàng không vào kho, không có lỗi |  |
| [B08](loi.md#b08) | [BO-26](../../backoffice/loi.md#bo-26) | Minor | Lỗi chức năng | Mã danh mục và mã khuyến mãi nhận chữ thường và dấu cách, trái với hướng dẫn | Trùng một phần [BO-08](../../backoffice/loi.md#bo-08) (mã khuyến mãi); phần mã danh mục là mới |
| [B09](loi.md#b09) | [BO-17](../../backoffice/loi.md#bo-17) | Minor | Nội dung Guide me | Guide me nói banner có nút bật/tắt và đường dẫn, nhưng form không có |  |
| [B10](loi.md#b10) | [BO-18](../../backoffice/loi.md#bo-18) | Minor | Nội dung Guide me | Tip số lượt ngụ ý được tạo khuyến mãi không giới hạn, nhưng hệ thống bắt buộc số lượt |  |
| [B11](loi.md#b11) | [BO-19](../../backoffice/loi.md#bo-19) | Minor | Nội dung Guide me | Guide me nói từ chối thì đơn đóng lại, nhưng khách vẫn gửi được yêu cầu mới |  |
| [B12](loi.md#b12) | [BO-20](../../backoffice/loi.md#bo-20) | Minor | Nội dung Guide me | Guide me nói bấm Đã nhận thì "tiền đã hoàn", thực tế chỉ mở khoản hoàn chờ chi |  |
| [B13](loi.md#b13) | [BO-21](../../backoffice/loi.md#bo-21) | Minor | Nội dung Guide me | Guide me nói Admin quyết số lượng cuối cùng, nhưng không có chỗ sửa số lượng khi duyệt |  |
| [B14](loi.md#b14) | [BO-22](../../backoffice/loi.md#bo-22) | Minor | Nội dung Guide me | Guide me mô tả trạng thái cuối "Đã nhận" cho yêu cầu nhập, hệ thống không có trạng thái này |  |
| [B15](loi.md#b15) | [BO-23](../../backoffice/loi.md#bo-23) | Minor | Nội dung Guide me | Guide me bước duyệt nói duyệt xong là nhận hàng được, thực tế phải qua bước Thanh toán |  |

## Các file

| File | Nội dung | Pass | Fail | Blocked |
|---|---|---|---|---|
| [loi.md](loi.md) | Chi tiết 15 lỗi |  |  |  |
| [luong.md](luong.md) | 6 luồng đầu-cuối |  |  |  |
| [lech-guide-code.md](lech-guide-code.md) | Guide me khác code |  |  |  |
| [hd-danh-muc.md](test-case/hd-danh-muc.md) | HD-Danh mục | 8 | 1 | 0 |
| [hd-them-sach.md](test-case/hd-them-sach.md) | HD-Thêm sách | 13 | 0 | 0 |
| [hd-phien-ban-gia.md](test-case/hd-phien-ban-gia.md) | HD-Phiên bản & giá | 7 | 1 | 0 |
| [hd-banner.md](test-case/hd-banner.md) | HD-Banner | 4 | 1 | 1 |
| [hd-khuyen-mai.md](test-case/hd-khuyen-mai.md) | HD-Khuyến mãi | 13 | 3 | 0 |
| [hd-xu-ly-tra-hang.md](test-case/hd-xu-ly-tra-hang.md) | HD-Xử lý trả hàng | 9 | 4 | 0 |
| [hd-nha-cung-cap.md](test-case/hd-nha-cung-cap.md) | HD-Nhà cung cấp | 8 | 1 | 0 |
| [hd-yeu-cau-nhap.md](test-case/hd-yeu-cau-nhap.md) | HD-Yêu cầu nhập | 10 | 2 | 0 |
| [hd-don-mua.md](test-case/hd-don-mua.md) | HD-Đơn mua | 11 | 2 | 0 |
| [hd-nhan-hang.md](test-case/hd-nhan-hang.md) | HD-Nhận hàng | 12 | 0 | 0 |
| [hd-duyet-tra-ve-kho.md](test-case/hd-duyet-tra-ve-kho.md) | HD-Duyệt trả về kho | 5 | 2 | 0 |
| [hd-thanh-ly.md](test-case/hd-thanh-ly.md) | HD-Thanh lý | 11 | 0 | 0 |
| [hd-khach-kiem-chung.md](test-case/hd-khach-kiem-chung.md) | HD-Khách kiểm chứng | 9 | 1 | 0 |
| [hd-phan-quyen-gm14.md](test-case/hd-phan-quyen-gm14.md) | HD-Phân quyền | 16 | 0 | 0 |
| [hd-nut-guide-me.md](test-case/hd-nut-guide-me.md) | HD-Nút Guide me | 5 | 0 | 2 |

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

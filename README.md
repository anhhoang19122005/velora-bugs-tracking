# Báo cáo bug Velora

**Theo dõi công việc hiện tại tại [trang-thai.md](trang-thai.md).**

**Mọi lỗi chưa đóng trong một file (cho người fix và agent): [loi-hien-tai.md](loi-hien-tai.md).** File tự sinh bằng `python scripts/build_loi_hien_tai.py`; sửa nguồn (`trang-thai.md`, các `loi.md`) rồi chạy lại.

Chuyển từ `manual-2026-11-10-v2.xlsx`, mỗi sheet là một file Markdown. Ảnh của đợt manual đầu nằm trong [images](images/) và được liên kết từ từng bug.

- **Chi tiết lỗi** · [Storefront](storefront/loi.md), [Backoffice](backoffice/loi.md) và [lỗi giao diện](ui/loi.md).
- **Kế hoạch sửa và retest** · [fix-plans](fix-plans/), chia theo repo cần sửa. Mở từng kế hoạch từ [bảng trạng thái](trang-thai.md).
- **Bằng chứng** · [Ảnh đợt đầu](images/), [đợt test 27/11: Guide me và phân quyền](test-2026-11-27/README.md) và [ảnh rà UI 27/11](ui/loi.md).

Khi triển khai bản sửa, dùng lại thành phần hoặc quy tắc đang có (DRY), chọn thay đổi nhỏ nhất giải quyết được nguyên nhân (KISS) và giữ trách nhiệm của từng lớp rõ ràng (SOLID). UI hướng dẫn và báo lỗi, service sở hữu quy tắc nghiệp vụ, cơ sở dữ liệu bảo vệ tính nhất quán khi có nhiều request. Mỗi PR cần test hồi quy tại lớp xảy ra lỗi; thay đổi API thì sinh lại contract và kiểu client. Các sửa liên quan dữ liệu cũ cần đối soát trước migration.

Bổ sung ngày 2026-11-11: SF-18–SF-27 là 10 bug giao diện Minor. Đã đối chiếu ảnh và commit sửa; chưa chạy kiểm thử lại. Trạng thái đã vào `origin/develop` được xác nhận bằng Git sau khi fetch. [Tổng kết](tong-ket.md) giữ nguyên kết quả đợt test 2026-11-10, chưa bao gồm 10 bug mới. SF-27 tiếp nối phần tiêu đề riêng từng trang từng được để tùy chọn ở SF-14.

Cập nhật ngày 2026-11-12: **SF-02, SF-03, SF-07, SF-08, SF-10 đã sửa, đã merge vào `develop`; chưa kiểm thử lại**. Backend: [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`. Storefront: [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a` (SF-03 chỉ có bản sửa backend). Đã đối chiếu source, commit và đầu nhánh remote ngày 2026-11-12.

Trong 24 bug đã sửa, **17 bug** đã vào develop qua PR #77 (merge `b3444b9`), **5 bug** thuộc đợt merge mới trên; **SF-04 và SF-12** được người dùng xác nhận đã giải quyết ngày 2026-11-12. Hai bug này chưa được đối chiếu commit/PR hoặc kiểm thử lại trong lần cập nhật này. Cập nhật này phản ánh trạng thái code, **không phải kết quả retest**. Tổng kết, luồng, test case Pass/Fail/Blocked, ảnh và response của đợt manual 2026-11-10 được giữ nguyên làm bằng chứng lịch sử. Các kế hoạch SF-07/SF-08 được chuyển sang nhóm `fix-plans/storefront-backend` vì bản sửa chạm cả hai repo.

Bổ sung ngày 2026-11-14: **SF-28–SF-44 và BO-08–BO-12** (22 bug) từ đợt retest và test tính bất biến, có 4 Major ở backend (SF-37 đặt hàng trùng, SF-38 mã giảm giá dùng quá lượt, SF-40 đổi trả trùng, SF-44 mất event làm đơn kẹt PENDING, chưa tái hiện) và kế hoạch sửa tương ứng. Trang mới [Storefront-Bất biến](storefront/bat-bien.md). Trạng thái từng bug cũ sau retest, luồng và test case vẫn giữ nguyên kết quả đợt 1; xem file Excel.

Bổ sung ngày 2026-11-27: **SF-45–SF-47 và BO-13–BO-26** (17 lỗi) từ [đợt test 2026-11-27](test-2026-11-27/README.md), trước đó theo dõi bằng mã trong đợt B01–B15. B02 ghi vào SF-38. SF-47 và BO-24 là do dữ liệu trên DB dùng chung bị đổi (mất role `USER` và 2 quyền chuyển khoản của Admin), không phải lỗi code.

Bổ sung ngày 2026-11-27: đợt kiểm thử theo Guide me có 162 case. Bảng trạng thái bổ sung 14 mục và liên kết bằng chứng trùng với các lỗi cũ. [Báo cáo đợt test](test-2026-11-27/README.md).

| Sheet | Bên | File |
|---|---|---|
| Tổng kết | Chung | [tong-ket.md](tong-ket.md) |
| Storefront-Luồng | Storefront | [storefront/luong.md](storefront/luong.md) |
| Storefront-Lỗi | Storefront | [storefront/loi.md](storefront/loi.md) |
| Storefront-Bug UI | Storefront | [storefront/ui/](storefront/ui/README.md) |
| Storefront-HD-Đăng nhập | Storefront | [storefront/hd-dang-nhap.md](storefront/hd-dang-nhap.md) |
| Storefront-HD-Đăng ký | Storefront | [storefront/hd-dang-ky.md](storefront/hd-dang-ky.md) |
| Storefront-HD-Địa chỉ | Storefront | [storefront/hd-dia-chi.md](storefront/hd-dia-chi.md) |
| Storefront-HD-Đặt hàng | Storefront | [storefront/hd-dat-hang.md](storefront/hd-dat-hang.md) |
| Storefront-HD-Đổi trả | Storefront | [storefront/hd-doi-tra.md](storefront/hd-doi-tra.md) |
| Storefront-HT-Checkout | Storefront | [storefront/ht-checkout.md](storefront/ht-checkout.md) |
| Storefront-HT-Áp mã | Storefront | [storefront/ht-ap-ma.md](storefront/ht-ap-ma.md) |
| Storefront-HT-VNPAY | Storefront | [storefront/ht-vnpay.md](storefront/ht-vnpay.md) |
| Storefront-Bất biến | Storefront | [storefront/bat-bien.md](storefront/bat-bien.md) |
| Backoffice-Luồng | Backoffice | [backoffice/luong.md](backoffice/luong.md) |
| Backoffice-Lỗi | Backoffice | [backoffice/loi.md](backoffice/loi.md) |
| Backoffice-HD-Tạo khuyến mãi | Backoffice | [backoffice/hd-tao-khuyen-mai.md](backoffice/hd-tao-khuyen-mai.md) |
| Backoffice-HD-Tạo sách | Backoffice | [backoffice/hd-tao-sach.md](backoffice/hd-tao-sach.md) |
| Backoffice-HD-Đơn mua | Backoffice | [backoffice/hd-don-mua.md](backoffice/hd-don-mua.md) |
| Backoffice-HD-Nhập kho | Backoffice | [backoffice/hd-nhap-kho.md](backoffice/hd-nhap-kho.md) |
| Backoffice-HD-Yêu cầu trả kho | Backoffice | [backoffice/hd-yeu-cau-tra-kho.md](backoffice/hd-yeu-cau-tra-kho.md) |

## Retest Backoffice ngày 2026-11-12

Báo cáo và bằng chứng của đợt này đã được xóa khỏi repo (còn trong lịch sử Git, commit `e6e2057`). Hai điều rút ra từ đó được giữ lại: BO-05 được người dùng chấp nhận và lỗi điều hướng Admin được ghi thành BO-12.

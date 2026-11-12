# Retest Backoffice — 2026-11-12

> **Cập nhật sau khi chạy lại 13 case Blocked:** tổng hợp hiện tại **53 Pass (UI/API), 2 Accepted, 0 Blocked**. [Chi tiết, giới hạn và dữ liệu tạo thêm](blocked-rerun.md). Lỗi điều hướng Admin chưa sửa; các bảng bên dưới giữ nguyên kết quả lần chạy đầu. [results.json](results.json) đã tổng hợp lần chạy bổ sung, có lưu `previousResult` và [snapshot cũ](results-before-blocked-rerun.json).

## Phạm vi và cách đọc kết quả

Chạy bằng in-app browser trên Admin `localhost:3000`, Warehouse `localhost:3001`, Seller `localhost:3002`. Storefront được khởi động tại `localhost:3003` để đối chiếu sách và tồn kho. Đăng nhập các tài khoản mẫu theo `DemoUserSeeder` trong backend; không lưu mật khẩu hoặc token vào báo cáo.

Backoffice lúc kiểm tra ở nhánh `develop`, HEAD `2f36205d`, ahead 2 và có thay đổi chưa commit. Đây là kết quả trên checkout đang chạy, không chứng minh bản remote/deployed có cùng hành vi.

55 case từ năm bảng thiết kế: **40 Pass về hành vi UI, 2 Accepted (người dùng chấp nhận), 13 Blocked/chưa đủ bằng chứng; không còn case được phân loại Fail trong báo cáo này**. `Accepted` ghi nhận quyết định chấp nhận của người dùng ngày 2026-11-12 đối với việc chuẩn hóa giá âm thành số dương. Hai case chưa được chuyển thành Pass vì chưa kiểm tra thao tác lưu sau chuẩn hóa. Expected Result và kết quả lịch sử vẫn giữ nguyên để truy vết. Không thu HTTP status/body từ Network trong lần này. `Pass` xác nhận hành vi trên giao diện (chặn dữ liệu, thông báo, lưu và đọc lại), không xác nhận các mã 201/400/403/409 ghi trong Expected Result. Case chỉ kiểm tra cưỡng bức quyền hoặc gọi lại API được để Blocked khi UI không cung cấp đường thực hiện.

Không thay bảng Actual Result lịch sử ngày 2026-11-10, danh sách bug, kế hoạch sửa hoặc thống kê tracker. Không chạy unit test/build và không sửa source ứng dụng.

## Kết quả nổi bật

- Sách TC12 và đơn mua TC10: nhập `-1`, ô giá tự thành `1`. Người dùng xác nhận hành vi này hợp lý, nên hai case được ghi **Accepted**, không còn tính là Fail trong lần retest này. Chưa thực hiện lưu sau chuẩn hóa. [Ảnh form sách](book-negative-price.png).
- Khuyến mãi: 11 case đạt hành vi UI; bốn mã mới được đọc lại ở trạng thái Pending, đúng mức giảm và số lượng. Trùng mã báo `That promotion code is already taken. Use another one.` và giữ form/dữ liệu.
- Sách: tên 256, tác giả 101 ký tự được báo riêng tại trường; sách hợp lệ hiện trên Storefront đúng giá 99.000 đ và danh mục Kỹ năng sống. [Ảnh Storefront](storefront-new-book.png).
- Đơn mua: ghi chú 1001 bị chặn tại trường; 1000 được lưu. Admin mẫu vẫn không duyệt được PO mới sau khi đăng nhập lại: `Couldn’t approve purchase order / You do not have permission to perform this action`. PO vẫn Pending. Đây là quan sát UI, chưa kết luận nguyên nhân hay HTTP status. [Ảnh](admin-po-approve-denied.png).
- Nhập kho: picker báo `No placed order matches that.`; không có PO ORDERED và không thể chuẩn bị mới qua bước duyệt bị từ chối. [Ảnh](no-ordered-po.png).
- Yêu cầu kho mới được Admin duyệt; Admin/Warehouse cùng hiển thị Approved và số lượng 5.

## Dữ liệu thay thế và kiểm tra bổ sung

Ngày bắt đầu hợp lệ dùng 2026-11-12, ngày kết thúc 2026-11-30. Mã hợp lệ dùng mã riêng thay mã cũ; case trùng dùng mã vừa tạo. Sách `Sach Hop Le` không có trong kết quả tìm picker nên đơn mua dùng `Python Cơ Bản`. Tên `T`×255 đã có dữ liệu cũ và gây conflict; đổi thành `RETEST1211-` + `T`×244, vẫn đúng 255 ký tự, để kiểm tra biên độc lập. Ảnh PNG dùng logo công khai của repo.

Form trả kho hiện tại không có trường RMA/Order; đã chạy bổ sung nguồn **Manual**, không coi nó thay thế case gốc nguồn CUSTOMER_RETURN. RTW-20261112-000021 được tạo Pending, Warehouse duyệt, Seller thấy Approved; tồn Python Cơ Bản trên Storefront tăng **50 → 51**. [Trước](python-stock-before.png), [sau](python-stock-after.png). TC03/TC04 gốc vẫn Blocked do chưa thực hiện với CUSTOMER_RETURN/RMA 2/đơn 17.

Phiên đăng nhập Warehouse/Seller hết hạn trong quá trình kiểm tra; đã đăng nhập lại trước khi tiếp tục. Thử thiếu Book sau khi đăng nhập mới nhận `Book ID must be positive`. Không coi lần lỗi xác thực trước đó là lỗi validation của sản phẩm.

## Chi tiết 55 test case

| Nhóm | Pass UI | Accepted | Blocked | Tổng |
|---|---:|---:|---:|---:|
| Khuyến mãi | 11 | 0 | 0 | 11 |
| Đơn mua | 9 | 1 | 1 | 11 |
| Sách | 11 | 1 | 0 | 12 |
| Yêu cầu kho và trả kho | 9 | 0 | 5 | 14 |
| Nhập kho | 0 | 0 | 7 | 7 |

### Khuyến mãi

Nguồn thiết kế: [hd-tao-khuyen-mai.md](../../backoffice/hd-tao-khuyen-mai.md).

| Case | Kết quả | Thực tế lần chạy này |
|---|---|---|
| TC01 - Tạo khuyến mãi hợp lệ | Pass | Tạo RETEST1211A thành công; panel đóng; mã bị chặn khi tạo lại |
| TC02 - Tên rỗng | Pass | Name is required; form giữ mở |
| TC03 - Mã đã tồn tại | Pass | That promotion code is already taken. Use another one; panel giữ dữ liệu |
| TC04 - Ngày bắt đầu sau ngày kết thúc | Pass | The end date must be on or after the start date; dữ liệu giữ nguyên |
| TC05 - Ngày kết thúc đã qua | Pass | End date cannot be in the past |
| TC06 - Giảm 1% | Pass | RETEST1211B giảm 1%: Promotion created |
| TC07 - Giảm 100% | Pass | RETEST1211C giảm 100%: Promotion created |
| TC08 - Số lượng 1 | Pass | RETEST1211D số lượng 1: Promotion created |
| TC09 - Giảm 0% | Pass | Discount % must be at least 1 |
| TC10 - Giảm 101% | Pass | Discount % must be at most 100 |
| TC11 - Số lượng 0 | Pass | Quantity must be at least 1 |

### Đơn mua

Nguồn thiết kế: [hd-don-mua.md](../../backoffice/hd-don-mua.md).

| Case | Kết quả | Thực tế lần chạy này |
|---|---|---|
| TC01 - Tạo đơn mua hợp lệ | Pass | PO-20261112-000027 tạo thành công, Pending; sách thay thế Python Cơ Bản |
| TC02 - Chưa chọn nhà cung cấp | Pass | Supplier is required |
| TC03 - Không có dòng hàng | Pass | An order needs at least one line. |
| TC04 - Thiếu sách và định dạng | Pass | Every line needs a book and a format. |
| TC05 - Giá nhập rỗng | Pass | Every line needs an import price. |
| TC06 - Warehouse tự duyệt đơn | Blocked | Warehouse không có nút Approve; chưa gọi API để xác nhận HTTP 403 |
| TC07 - Ghi chú đúng 1000 ký tự | Pass | Ghi chú n×1000 được lưu trong PO-20261112-000027 |
| TC08 - Số lượng 0 | Pass | Every line needs a quantity of at least 1. |
| TC09 - Số lượng -1 | Pass | Every line needs a quantity of at least 1. |
| TC10 - Giá nhập -1 | Accepted | Nhập -1, ô Import price tự thành 1; chưa thực hiện lưu sau chuẩn hóa; người dùng chấp nhận hành vi |
| TC11 - Ghi chú 1001 ký tự | Pass | Note must be at most 1000 characters |

### Sách

Nguồn thiết kế: [hd-tao-sach.md](../../backoffice/hd-tao-sach.md).

| Case | Kết quả | Thực tế lần chạy này |
|---|---|---|
| TC01 - Tạo sách hợp lệ và hiện trên storefront | Pass | Book created; Storefront /vi/detail/retest-book-1211 hiện đúng tên, tác giả, giá 99.000đ, Kỹ năng sống và ảnh PNG |
| TC02 - Tên rỗng | Pass | Title is required |
| TC03 - Tác giả rỗng | Pass | Author is required |
| TC04 - Chưa chọn nhà cung cấp | Pass | Supplier is required |
| TC05 - Chưa chọn danh mục | Pass | Categories is required |
| TC06 - Chưa chọn định dạng | Pass | Every row needs a format. |
| TC07 - Chưa có ảnh | Pass | Image URL is required |
| TC08 - Tên đúng 255 ký tự | Pass | Tên RETEST1211- + T×244 (255 ký tự), giá 0: Book created; T×255 ban đầu trùng dữ liệu cũ |
| TC09 - Giá bằng 0 | Pass | Giá 0 được lưu cùng case TC08 |
| TC10 - Tên 256 ký tự | Pass | Title must be at most 255 characters; các trường khác hợp lệ |
| TC11 - Tác giả 101 ký tự | Pass | Author must be at most 100 characters; các trường khác hợp lệ |
| TC12 - Giá âm | Accepted | Nhập -1 tự thành 1; chưa thực hiện lưu sau chuẩn hóa; người dùng chấp nhận hành vi |

### Yêu cầu kho và trả kho

Nguồn thiết kế: [hd-yeu-cau-tra-kho.md](../../backoffice/hd-yeu-cau-tra-kho.md).

| Case | Kết quả | Thực tế lần chạy này |
|---|---|---|
| TC01 - Tạo yêu cầu kho | Pass | STK-20261112-000019, số lượng 5, Pending; sách Retest Book 1211 |
| TC02 - Admin duyệt yêu cầu kho, kho thấy kết quả | Pass | Admin duyệt STK-20261112-000019; Admin và Warehouse cùng Approved, số lượng 5 |
| TC03 - Seller tạo yêu cầu trả kho | Blocked | Case gốc cần RMA 2 + đơn 17 (CUSTOMER_RETURN); UI tạo thủ công không có hai trường này. Đã kiểm tra bổ sung RTW-20261112-000021 nguồn Manual thành công nhưng không thay thế case gốc. |
| TC04 - Kho duyệt trả kho, tồn tăng | Blocked | Chưa có yêu cầu CUSTOMER_RETURN mới theo fixture gốc. Luồng Manual bổ sung đã duyệt, tồn Python Cơ Bản tăng 50→51 và Seller thấy Approved. |
| TC05 - Yêu cầu kho thiếu sách | Pass | Thiếu sách: Couldn’t create stock request / Book ID must be positive; panel giữ mở; chưa thu HTTP status |
| TC06 - Warehouse duyệt yêu cầu kho | Blocked | UI Warehouse không cung cấp nút duyệt yêu cầu kho; chưa gửi request trực tiếp để xác minh HTTP 403. |
| TC07 - Trả kho lý do rỗng | Pass | Reason is required; UI chặn sớm, chưa đo HTTP 400 |
| TC08 - Trả kho không có dòng hàng | Pass | A return needs at least one line.; dữ liệu giữ nguyên |
| TC09 - Có RMA nhưng thiếu Đơn | Blocked | UI trả kho không có trường RMA/Order để tạo cặp thiếu; chưa gửi request trực tiếp để xác minh HTTP 400. |
| TC10 - Duyệt trả kho lần hai | Blocked | Yêu cầu đã Approved không còn nút Approve; chưa gửi request lần hai để xác minh HTTP 409. |
| TC11 - Yêu cầu kho số lượng 0 | Pass | Quantity must be at least 1 |
| TC12 - Yêu cầu kho lý do 1001 ký tự | Pass | Reason must be at most 1000 characters |
| TC13 - Trả kho số lượng 0 | Pass | Every line needs a quantity of at least 1. |
| TC14 - Trả kho lý do 1001 ký tự | Pass | Reason must be at most 1000 characters |

### Nhập kho

Nguồn thiết kế: [hd-nhap-kho.md](../../backoffice/hd-nhap-kho.md).

| Case | Kết quả | Thực tế lần chạy này |
|---|---|---|
| TC01 - Nhập đủ đơn mua và nhận hàng | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC02 - Đơn mua chưa thanh toán | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC03 - Chi tiết rỗng | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC04 - Giá nhập âm | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC05 - Số lượng bằng số đặt | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC06 - Số lượng 0 | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |
| TC07 - Vượt số lượng đặt | Blocked | Không có PO ORDERED: picker hiện No placed order matches that. PO mới Pending vì Admin bị từ chối duyệt; chưa thực hiện yêu cầu nhập/API 400/409. |

## Dữ liệu đã tạo và giới hạn

- Khuyến mãi: RETEST1211A (10%, 5), RETEST1211B (1%, 5), RETEST1211C (100%, 5), RETEST1211D (10%, 1), cùng Pending.
- Hai sách: `Retest Book 1211` giá 99.000 đ; tên dài `RETEST1211-` + `T`×244 giá 0; cùng có PNG và danh mục Kỹ năng sống.
- PO-20261112-000027: Python Cơ Bản/Bìa mềm, 10 × 50.000 đ, ghi chú 1000 ký tự, Pending.
- STK-20261112-000019: Retest Book 1211, số lượng 5, Approved.
- RTW-20261112-000021: Python Cơ Bản/Bìa mềm, số lượng 1, nguồn Manual, Approved. Tồn đã tăng một đơn vị.
- Các bản ghi trên được giữ lại để đối chiếu; không xóa dữ liệu hoặc hoàn tác tồn kho.
- Không chạy sáu luồng tổng hợp trong `luong.md` thành một đợt end-to-end riêng; báo cáo này bao phủ năm bảng 55 case. Không kiểm tra mở rộng BO-01/BO-07 responsive ngoài các bảng đó.
- [Dữ liệu kết quả JSON](results.json). Chưa commit/push.

## Đối chiếu bổ sung — phiên Admin khi xử lý PO

- Từ danh sách `http://localhost:3001/admin/warehouse/purchase-orders`, mở PO-20261112-000027 dẫn tới `/warehouse/purchase-orders/3` (mất `/admin`). Với browser chỉ đăng nhập Admin, ứng dụng chuyển sang đăng nhập Warehouse. Đây là lỗi mất ngữ cảnh phiên khi điều hướng, đã tái hiện qua in-app browser.
- Mở trực tiếp `/admin/warehouse/purchase-orders/3` giữ đúng phiên Admin; PO khi đối chiếu đã là APPROVED. Thao tác Mark ordered thành công; đọc lại PO thấy ORDERED và nút Import stock. Không thu HTTP status/body. Điều này xác nhận tài khoản Admin có thể thực hiện thao tác này với đúng ngữ cảnh phiên; chưa chứng minh mọi lỗi quyền trước đó có cùng nguyên nhân.
- Sau khi Mark ordered thành công, ứng dụng chuyển về `/warehouse/purchase-orders` và lại yêu cầu đăng nhập Warehouse. Source dùng đường dẫn danh sách cố định trong `useListMutation`, cùng kiểu mất tiền tố như mở chi tiết.
- Dữ liệu thay đổi ở lần đối chiếu bổ sung: PO-20261112-000027 (ID 3), APPROVED → ORDERED. Chưa tạo phiếu nhập hoặc Receive; chưa tăng tồn kho từ PO này. Các bảng kết quả phía trên giữ nguyên là lịch sử lần chạy trước.
- [Bằng chứng PO Ordered với phiên Admin](po-ordered-admin-scope.png). Chưa sửa source ứng dụng.

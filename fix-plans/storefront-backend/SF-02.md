# SF-02: Số điện thoại được lưu ở địa chỉ nhưng làm đặt hàng lỗi 500

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Đã sửa, đã merge vào `develop`; chưa kiểm thử lại |
| **Repo có bản sửa** | `taschen-backend` và `taschen-storefront` |
| **Nhánh thực hiện** | `fix/checkout-flow-sf-02-03-07-08-10`; chứa các bản sửa địa chỉ đã gộp vào nhánh này |
| **Bug và ảnh trước sửa** | [Chi tiết bug](../../storefront/loi.md#sf-02), [Ảnh 1](../../images/SF-02-1.jpg) |

## Nguyên nhân trước khi sửa

Địa chỉ từng nhận `^0[0-9]{9}$`, còn `Order` yêu cầu đầu số 02/03/05/07/08/09. Vì thế `0123456789` lưu được nhưng bị entity validation từ chối khi tạo đơn. Handler cũ không xử lý `ConstraintViolationException` nên trả 500 thay vì lỗi dữ liệu 400.

## Thay đổi đã có

- `CreateAddressRequest` và `UpdateAddressRequest` của identity-service dùng `^(03|05|07|08|09|02)[0-9]{8}$`: **đúng 10 chữ số**, đầu 02/03/05/07/08/09. Đây là tập con quy tắc của Order, không phải sao chép nguyên biểu thức cho phép 10–11 chữ số.
- Schema địa chỉ storefront dùng cùng phạm vi đầu số và độ dài; thông báo form phản ánh quy tắc mới.
- Checkout gọi `orderAcceptsAddress` để chặn địa chỉ đã lưu từ trước nhưng không hợp lệ, khóa nút đặt hàng và dẫn người dùng tới hồ sơ để sửa.
- `GlobalExceptionHandler` của order-service xử lý `ConstraintViolationException` thành HTTP 400, code `VALIDATION_ERROR` và `fieldErrors`. Đây là lớp bảo vệ cho dữ liệu cũ; không có bước tự sửa toàn bộ địa chỉ đã lưu.

| Ví dụ | Kết quả theo quy tắc đã merge |
|---|---|
| `0912345678` | Đạt quy tắc số điện thoại |
| `0212345678` | Đạt quy tắc 10 chữ số đầu 02 |
| `0123456789`, `0412345678` | Bị từ chối vì đầu số |
| `02412345678` hoặc số 11 chữ số khác | Bị từ chối vì độ dài |

Bảng này mô tả ràng buộc trong source, không phải kết quả gọi API mới. Đính chính kế hoạch cũ: không còn phương án cho phép số máy bàn 11 chữ số.

## Commit và bằng chứng merge

- Backend: `e3f5aad` thêm ràng buộc địa chỉ/handler; `0324996` chốt số điện thoại 10 chữ số và bổ sung test.
- Storefront: `b59c5c6` đồng bộ schema và chặn địa chỉ cũ ở checkout.
- Backend: [PR #117](https://github.com/VELORA-MICRO/taschen-backend/pull/117), merge `e090ed4`.
- Storefront: [PR #78](https://github.com/VELORA-MICRO/taschen-storefront/pull/78), merge `cdb599a`.
- `c32643e` sinh lại `services/identity-service/contract/openapi.yaml` trong repo backend. Chưa xác minh cập nhật tương ứng ở repo `taschen-contracts` riêng.
- Đối chiếu source, lịch sử commit và đầu nhánh remote ngày **2026-11-12**.

## Test có trong source — chưa chạy lại

- `AddressRequestValidationTest`: địa chỉ hợp lệ qua create/update; dữ liệu Order từ chối bị chặn; test tham số kiểm tra độ dài và đầu số điện thoại.
- `GlobalExceptionHandlerTest.handleConstraintViolation_invalidEntity_returns400WithFieldErrors` kiểm tra status 400, code và tên trường `recipientPhone`.
- `e2e/api/storefront.spec.ts`: form sửa địa chỉ chặn tên/số điện thoại sai; checkout chặn địa chỉ cũ không hợp lệ. Các ca này mock API, chưa chứng minh tích hợp backend thật.

## Kiểm thử lại còn lại

- Thử tạo/sửa địa chỉ qua cả form và API với số 9, 10, 11 chữ số, đầu số hợp lệ/sai và khoảng trắng.
- Với địa chỉ cũ sai, kiểm tra checkout khóa đặt hàng và có đường sửa trong hồ sơ.
- Gọi checkout backend với địa chỉ cũ sai: kiểm tra status thực tế là 400, có `fieldErrors` và không tạo đơn.
- Với địa chỉ hợp lệ, kiểm tra đặt COD thành công.

Chưa chạy ứng dụng/test trong lần cập nhật tracker này. Ảnh và response gốc được giữ tại bản ghi bug; chưa có bằng chứng live sau sửa.

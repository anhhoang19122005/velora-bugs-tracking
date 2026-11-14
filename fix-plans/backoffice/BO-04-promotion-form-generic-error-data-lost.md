# BO-04: Form tạo khuyến mãi báo lỗi chung và mất dữ liệu

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Đã sửa trên nhánh local, đã kiểm thử trên trình duyệt; **chưa commit, chưa merge** |
| **Repo có bản sửa** | `taschen-backoffice` (backend không đổi) |
| **Nhánh thực hiện** | `fix/bo-04-06-clear-error-messages`, tách từ `develop` `02da243d` |
| **Bug và ảnh trước sửa** | [Chi tiết bug](../../backoffice/loi.md#bo-04), [Ảnh 1](../../images/BO-04-1.jpg) |
| **Test case** | [HD Tạo khuyến mãi](../../backoffice/hd-tao-khuyen-mai.md) TC03, TC04, TC05, TC09, TC10, TC11 |

## Nguyên nhân trước khi sửa

1. **Mất chi tiết lỗi ở BFF:** backend trả `fieldErrors` theo từng trường. `bffError` (`packages/core/src/api/bff.ts`) chỉ chuyển tiếp `error`, `code`, `traceId`; `fail()` (`packages/core/src/api/fail.ts`) cũng không đọc `fieldErrors`. Vì vậy mọi form chỉ có được câu chung "The request contains invalid data.".
2. **Form không có quy tắc:** các trường tạo khuyến mãi chỉ có `required`, dù `RecordField` của VUI hỗ trợ sẵn `min`, `max`, `dateRange`, `validate`.
3. **Form đóng trước khi có kết quả:** panel VUI chạy hiệu ứng đóng và xoá bản nháp ngay khi bấm Lưu, sau đó mới gọi `onSave`. Backend từ chối thì dữ liệu đã nhập không còn.

## Thay đổi đã có

| Thành phần | Thay đổi |
|---|---|
| `packages/core/src/api/bff.ts` | Lỗi 4xx chuyển tiếp thêm `fieldErrors` của backend. Lỗi 5xx vẫn che chi tiết như cũ. |
| `packages/core/src/api/fail.ts` | Có `fieldErrors` thì dùng chính câu backend báo cho từng trường làm `message`, và gắn `fieldErrors` lên lỗi. Sửa một chỗ dùng chung cho cả 3 console. |
| `promotions-config.tsx` | Quy tắc khớp `CreatePromotionRequest`: tên ≤ 255, mã ≤ 100, giảm 1–100%, số lượng ≥ 1, ngày kết thúc từ hôm nay (`dateRange: "future"`) và không trước ngày bắt đầu. |
| `promotions-view.tsx` | Nút Save của form tạo dùng `formActions`: `onAct` chờ `createPromotion`, lỗi thì trả `false` để giữ form mở với dữ liệu; thành công mới đóng. 409 báo "Mã khuyến mãi đã tồn tại. Hãy dùng mã khác." |
| `apps/seller/src/messages/{vi,en}.json` | Thêm `promotion.toast.codeTaken`, `promotion.validation.endBeforeStart`. |

Giữ nguyên dòng phụ của toast (`description: err.message`): đây là cách dev đã làm sẵn ở khoảng 25 chỗ trong 3 console, không thuộc phạm vi lỗi này.

**Không làm so với kế hoạch ban đầu:**
- Không thêm giới hạn vào schema zod ở BFF: backend vẫn chặn, và lỗi theo trường của nó giờ đã đi tới form.
- Quy tắc `priceOrderActive` không âm chuyển sang [BO-05](BO-05-price-input-drops-minus-sign.md), vì ô tiền hiện vẫn bỏ dấu trừ.

## Kiểm thử đã chạy (2026-11-12)

Trình duyệt, app seller `localhost:3002` với backend local, tài khoản `seller@taschen.test`:

| Case | Kết quả |
|---|---|
| TC09 (giảm 0%), TC11 (số lượng 0), TC04 (ngày kết thúc 2026-11-15 trước ngày bắt đầu 2026-11-20), nhập cùng lúc | Không gửi request. Báo tại từng ô: "Discount % must be at least 1", "Quantity must be at least 1", "The end date must be on or after the start date." Form giữ dữ liệu. |
| TC03 (mã `MANUAL1110` đã tồn tại) | Backend 409. Toast "That promotion code is already taken. Use another one."; form vẫn mở với dữ liệu đã nhập. |
| Mã hợp lệ `BO04TEST1112` | Tạo được, form đóng, danh sách 34 → 35. Để lại một khuyến mãi chờ duyệt tên "BO-04 test". |

Test tự động: `bff.test.ts` (chuyển tiếp `fieldErrors`), `fail.test.ts` (thông báo nêu trường). Toàn bộ test backoffice pass, typecheck và Biome sạch.

## Kiểm thử lại còn lại

- TC05 (ngày kết thúc đã qua) và TC10 (giảm 101%) chưa chạy trên trình duyệt; quy tắc tương ứng là `dateRange: "future"` và `max: 100`.
- App seller đang hiển thị tiếng Anh; chưa xem các câu tiếng Việt mới trên giao diện.

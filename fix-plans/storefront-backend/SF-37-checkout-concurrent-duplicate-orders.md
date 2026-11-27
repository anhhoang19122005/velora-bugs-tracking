# SF-37: Gửi đặt hàng đồng thời tạo nhiều đơn từ một giỏ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa. Hướng sửa đã chốt ngày 14/11: Idempotency-Key kết hợp khóa theo người dùng |
| **Repo** | `taschen-backend` (`order-service`) `d5b6ac2` và `taschen-storefront` `0a72cc4` |
| **Nhánh đề xuất** | `fix/checkout-idempotency-sf-37-38`, tách từ `develop`. Phối hợp SF-38 ở bước giữ lượt. |
| **Khối lượng** | Cần thêm lưu kết quả cùng transaction và kiểm thử các điểm gián đoạn. |
| **Bug** | `taschen-e2e/docs/bugs/manual-2026-11-10-v2.xlsx`, trang Storefront-Lỗi (SF-37) và Storefront-Bất biến (kịch bản 1 đến 5) |

## Hiện tượng

Giỏ có 1 cuốn. Gửi 2, 3 hoặc 10 request `POST /api/v1/orders` giống nhau cùng lúc thì tạo đúng 2, 3, 10 đơn, và inventory trừ kho bấy nhiêu lần (đo ngày 14/11: tồn 44 xuống 34 với 10 request). Gửi lần lượt thì không bị. Trên giao diện, click 3 lần liên tiếp chỉ ra 1 request vì nút đã khóa, nên lỗi lọt qua khi khách mở 2 tab, bấm lại lúc mạng chậm, hoặc có lớp mạng gửi lại request.

Có thêm một vấn đề liên quan, không phải đơn trùng. Nếu request đã tạo đơn nhưng **phản hồi bị mất** (mạng đứt), khách bấm lại sẽ nhận 409 "Cart is empty" và chỉ thấy toast "Đặt hàng thất bại", trong khi đơn đã có ở trang Đơn hàng.

## Nguyên nhân

`OrderServiceImpl.checkout` đọc giỏ ở dòng 115, lưu đơn trong `TransactionTemplate` ở dòng 131–152, rồi mới xóa giỏ Redis ở dòng 155. Nhiều request có thể cùng đọc một giỏ trước khi bất kỳ request nào xóa nó. Mỗi đơn đã lưu phát sự kiện giữ hàng riêng.

## Thiết kế đề xuất

Storefront tạo một `Idempotency-Key` cho mỗi ý định đặt hàng và dùng lại key nếu phản hồi bị mất. Đổi dữ liệu đơn thì sinh key mới. Backend gắn key với người dùng và dấu vân tay của payload gồm địa chỉ, phương thức thanh toán, mã khuyến mãi và các dòng hàng. Cùng key và payload trả lại đơn cũ với HTTP 201. Cùng key nhưng khác payload trả 400. Request đồng thời đang xử lý trả 409.

1. **Lưu kết quả cùng transaction tạo đơn.** Ràng buộc duy nhất cho cặp người dùng và key. Khi thử lại, tra bản ghi đã commit trước khi đọc giỏ. Redis `DONE` có thể làm bộ nhớ đệm. Kết quả đã commit trong DB là căn cứ khi Redis lỗi hoặc tiến trình chết giữa commit và ghi `DONE`.
2. **Chặn hai key cùng dùng một giỏ.** Giữ khóa theo người dùng trong lúc xử lý và lưu dấu phiên bản giỏ đã dùng cùng transaction tạo đơn. Ràng buộc duy nhất theo người dùng và phiên bản giỏ là lớp bảo vệ khi khóa Redis hết hạn hoặc request gửi key khác. Mỗi thay đổi giỏ sinh phiên bản mới. Client cũ vẫn đi qua chốt phiên bản giỏ.
3. **Dọn giỏ theo phiên bản.** Sau commit, chỉ xóa nếu giỏ vẫn là phiên bản đã dùng. Khi tiến trình chết trước khi xóa, lần thử lại đọc đơn cũ hoặc nhận xung đột trên phiên bản giỏ cũ. Giỏ đã được khách sửa sau đó vẫn còn.
4. **Phân biệt trạng thái lỗi.** Chỉ cho thử lại như lần mới khi biết transaction đã rollback. Nếu chưa rõ commit thành công hay chưa, đọc dấu đã lưu trong DB. Nhả khóa Redis bằng phép so token và xóa nguyên tử. Giới hạn thời gian chạy hoặc gia hạn khóa theo token. Chốt DB vẫn phải đúng khi khóa hết hạn.

Storefront chuyển tới trang đơn bằng `orderCode` theo tuyến hiện tại. Cần chuyển tiếp key qua BFF và khai báo header trong OpenAPI khi triển khai.

## Liên quan RabbitMQ và khuyến mãi

Chống tạo đơn trùng áp dụng ở bước checkout. Một đơn đã commit vẫn có thể kẹt khi mất sự kiện giữ hàng. Phát lại sự kiện và xử lý đơn kẹt theo [SF-44](../backend/SF-44-order-event-lost-stuck-pending.md). Giữ và hoàn lượt mã theo [SF-38](../backend/SF-38-promotion-usage-over-redeemed.md).

## Kiểm thử cần có

| Tình huống | Kết quả mong đợi |
|---|---|
| 2, 3 và 10 request cùng giỏ, cùng key hoặc khác key | Một đơn cho phiên bản giỏ đó. Kho giữ một lần. Các request còn lại trả lại đơn cũ nếu cùng key và đã xử lý xong, hoặc 409. |
| Client cũ gửi nhiều request cùng giỏ | Một đơn. |
| Mất phản hồi, gửi lại ở giây 45 và phút 10 | Cùng ID và mã đơn. Cùng key nhưng đổi địa chỉ hoặc dòng hàng trả 400. |
| Dừng tiến trình sau commit, trước khi xóa giỏ hoặc ghi Redis `DONE` | Cùng key đọc đúng đơn cũ từ DB. Key khác với phiên bản giỏ cũ bị chặn. |
| Khóa Redis hết hạn khi request đầu còn chạy | Ràng buộc DB vẫn bảo đảm một đơn cho phiên bản giỏ đó. |
| Đổi giỏ sau khi đặt đơn | Dọn phiên bản cũ không xóa những gì khách vừa thêm. |
| Transaction rollback trước commit | Lần thử lại hợp lệ có thể đặt. Giỏ và lượt mã được xử lý theo kết quả giao dịch. |

## Phạm vi triển khai

Cần migration cho dấu checkout hoặc bảng tương đương, cập nhật contract cho header và kiểm thử qua gateway, BFF và Storefront. Khởi tạo thanh toán trùng theo dõi riêng ở SF-43. Đây là thiết kế đề xuất, chưa có bản sửa.

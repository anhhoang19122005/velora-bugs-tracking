# BO-11: Nhiều phiếu nhập cho một đơn mua khi tạo đồng thời

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | inventory-service |
| **Bug** | [Chi tiết BO-11](../../backoffice/loi.md#bo-11) |
| **Điểm vào source** | `ImportStockServiceImpl` |

## Nguyên nhân

Khi tạo nhiều phiếu cùng lúc, mỗi giao dịch có thể đọc cùng hạn mức của PO. Kho vẫn cần hỗ trợ nhiều đợt nhập hợp lệ.

## Thay đổi

1. Khóa PO trước khi tính số đã dành và tạo phiếu, rồi kiểm tổng theo từng sách/biến thể. Giữ cơ chế trừ hạn mức hiện có.
2. Khi nhận, khóa theo thứ tự PO → phiếu → lô. Đọc lại trạng thái và tổng đã nhận. Chỉ cộng tồn và cập nhật trạng thái trong cùng giao dịch.
3. Đối soát phiếu cũ vượt hạn mức và chỉ đóng PO khi đã nhận đủ.

## Tuân thủ quy tắc

Dùng lại phép tính hạn mức từng dòng và repository khóa phù hợp. Service điều phối giao dịch, repository chỉ đảm nhận đọc có khóa. Hạn mức nằm trên PO nên khóa theo PO để các PO khác vẫn xử lý song song.

## Kiểm thử lại

Ba phiếu đồng thời cùng đòi toàn bộ một PO chỉ một phiếu được tạo. Các đợt nhập một phần còn trong số lượng đặt vẫn thành công. Nhận đồng thời hoặc lặp lại không cộng vượt tồn và chỉ đóng PO khi đã nhận đủ.

# HD-Duyệt trả về kho

[← Tổng quan đợt test](README.md)

Guide me: Duyệt hàng trả về kho

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Trạng thái | PENDING → APPROVED / REJECTED | Xử lý phiếu đã xử lý |  |  |
|  | Vai trò | Admin, Warehouse | Seller |  |  |
|  |  |  | Khách |  |  |
|  | Lô hàng | Có lô của đúng định dạng | Sách chưa từng có lô |  |  |
|  |  |  | Phiếu MANUAL không xác định được lô |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Vai trò | Data Input: Phiếu (nguồn / sách / SL) | Data Input: Tình trạng lô | Data Input: Thao tác | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM11-01 - Duyệt phiếu khách trả | Warehouse | CUSTOMER_RETURN / sách A / 1 | Có lô | Duyệt | APPROVED; tồn +1 vào lô mới nhất khớp định dạng; storefront cập nhật. | Duyệt 200 → APPROVED; tồn kho 14 → 15; storefront 14 → 15 | Pass | <pre>PATCH /api/v1/inventory/return-to-warehouse/47/approve<br>Request body:<br>{<br>  "responseNote": "Đã kiểm hàng, sách còn tốt"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 47,<br>    "returnCode": "RTW-20261127-000066",<br>    "reason": "Khách trả 1 cuốn, sách còn nguyên seal, đưa lại lên kệ",<br>    "responseNote": "Đã kiểm hàng, sách còn tốt",<br>    "status": "APPROVED",<br>… (rút gọn)</pre> |
| 2 |  | GM11-02 - Từ chối hàng hỏng | Warehouse | CUSTOMER_RETURN / sách A / 1 | Có lô | Từ chối | REJECTED, tồn không đổi. | Từ chối phiếu (50 cuốn khai sai): 200 → REJECTED; tồn không đổi: 16 | Pass | <pre>PATCH /api/v1/inventory/return-to-warehouse/49/reject<br>Request body:<br>{<br>  "responseNote": "Số lượng không khớp với hàng nhận được"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 49,<br>    "returnCode": "RTW-20261127-000068",<br>    "reason": "Khai số lượng lớn hơn số khách thật sự trả",<br>    "responseNote": "Số lượng không khớp với hàng nhận được",<br>    "status": "REJECTED",<br>… (rút gọn)</pre> |
| 3 |  | GM11-03 - Duyệt khi sách không có lô nào [Nghi vấn G-11] | Warehouse | CUSTOMER_RETURN / sách chưa có lô / 1 | Không có lô | Duyệt | Code bỏ qua cộng kho nhưng phiếu vẫn APPROVED. Ghi lại tồn và cảnh báo. | Sách "Tuổi Trẻ Đáng Giá Bao Nhiêu" chưa có lô. Phiếu trả về kho 1 cuốn: tạo 201, duyệt 200 → APPROVED; tồn kho sau duyệt: 0. Phiếu báo đã duyệt nhưng hàng không vào kho, không có thông báo lỗi<br>Bug [B07](loi.md#b07)<br>[Ảnh 1](images/GM11-03-1.png) | Fail | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Khách trả cuốn sách chưa từng nhập kho qua phiếu nhập",<br>  "items": [<br>    {<br>      "bookId": 70,<br>      "variantId": 1,<br>      "quantity": 1<br>    }<br>  ],<br>  "returnRequestId": 64<br>}<br>HTTP 201<br>… (rút gọn)</pre><br>[Đầy đủ](api/GM11-03.txt) |
| 4 |  | GM11-04 - Duyệt hai phiếu trùng cho một yêu cầu trả [Nghi vấn G-10] | Warehouse | 2 phiếu cùng returnRequest / 1 mỗi phiếu | Có lô | Duyệt cả hai | Kỳ vọng chỉ cộng 1. Nếu cộng 2 là lỗi nghiêm trọng. | Khách trả 1 cuốn. Duyệt phiếu thứ nhất: tồn 14 → 15; duyệt phiếu trùng: HTTP 200, tồn 15 → 16. Tổng cộng 2 cuốn được cộng vào kho cho 1 cuốn khách trả<br>Bug [B01](loi.md#b01)<br>[Ảnh 1](images/GM11-04-1.png) | Fail | <pre>PATCH /api/v1/inventory/return-to-warehouse/47/approve<br>Request body:<br>{<br>  "responseNote": "Đã kiểm hàng, sách còn tốt"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 47,<br>    "returnCode": "RTW-20261127-000066",<br>    "reason": "Khách trả 1 cuốn, sách còn nguyên seal, đưa lại lên kệ",<br>    "responseNote": "Đã kiểm hàng, sách còn tốt",<br>    "status": "APPROVED",<br>… (rút gọn)</pre><br>[Đầy đủ](api/GM11-04.txt) |
| 5 | Invalid Partition | GM11-05 - Duyệt lại phiếu đã duyệt | Warehouse | APPROVED | — | Duyệt (API) | 409, tồn không đổi. | HTTP 409 | Pass | <pre>PATCH /api/v1/inventory/return-to-warehouse/47/approve<br>Request body:<br>{<br>  "responseNote": "Duyệt lại"<br>}<br>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "2001c6d4cdf54afc",<br>  "path": "/api/v1/inventory/return-to-warehouse/47/approve",<br>  "timestamp": "2026-11-27T04:24:57.325660400Z"<br>}</pre> |
| 6 |  | GM11-06 - Seller tự duyệt | Seller | PENDING | — | Duyệt | 403. | HTTP 403 | Pass | <pre>PATCH /api/v1/inventory/return-to-warehouse/51/approve<br>Request body:<br>{<br>  "responseNote": "Seller duyệt"<br>}<br>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to perform this action"<br>}</pre> |
| 7 |  | GM11-07 - Phiếu MANUAL không chọn định dạng, sách nhiều định dạng | Warehouse | MANUAL / sách 2 định dạng / 1 | Có lô cả hai | Duyệt | Báo lỗi vì không xác định được lô; phiếu vẫn PENDING. | Phiếu MANUAL 1 cuốn Sapiens không ghi định dạng (sách có lô bìa mềm và bìa cứng): tạo 201, duyệt 409 The request conflicts with the current state of the resource.; phiếu PENDING | Pass | <pre>POST /api/v1/inventory/return-to-warehouse<br>Request body:<br>{<br>  "reason": "Điều chỉnh tồn kho sau kiểm kê, không rõ định dạng",<br>  "items": [<br>    {<br>      "bookId": 67,<br>      "quantity": 1<br>    }<br>  ]<br>}<br>HTTP 201<br>{<br>  "success": true,<br>… (rút gọn)</pre> |

# HD-Thanh lý

[← Tổng quan đợt test](README.md)

Guide me: Lập phiếu thanh lý (Warehouse lập, Admin duyệt)

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Lý do | 30 đến 1000 ký tự | Rỗng | 30 | 29 |
|  |  |  |  | 1000 | 1001 |
|  | Số lượng | 1 đến tồn của lô | 0 | Bằng tồn lô | Tồn lô + 1 |
|  |  |  | Vượt tồn lô |  |  |
|  | Duyệt | Admin | Warehouse tự duyệt |  |  |
|  |  |  | Duyệt lần hai |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Vai trò | Data Input: Lý do | Data Input: Lô (tồn còn) | Data Input: Số lượng | Data Input: Thao tác | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM12-01 - Lập phiếu thanh lý | Warehouse | Ướt nước khi vận chuyển, hỏng 6 cuốn | Lô A (20) | 6 | Lưu | 201, PENDING; tồn chưa đổi. | HTTP 201, PENDING, tồn lô trước/sau khi lập: 40/40 | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 6<br>    }<br>  ]<br>}<br>HTTP 201<br>{<br>  "success": true,<br>… (rút gọn)</pre> |
| 2 |  | GM12-02 - Admin duyệt | Admin | (phiếu trên) | Lô A (20) | 6 | Duyệt | APPROVED; tồn lô còn 14; storefront giảm 6; ghi số còn lại sau thanh lý. | HTTP 200; tồn lô 40 → 34; storefront 40 → 34; ghi số còn lại sau thanh lý: [34] | Pass | <pre>PATCH /api/v1/inventory/disposals/3/approve<br>Request body:<br>{<br>  "responseNote": "Đã kiểm tra, đồng ý thanh lý"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 3,<br>    "disposalCode": "DSP-20261127-000011",<br>    "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>    "responseNote": "Đã kiểm tra, đồng ý thanh lý",<br>    "status": "APPROVED",<br>… (rút gọn)</pre> |
| 3 |  | GM12-03 - Admin từ chối | Admin | (phiếu PENDING) | Lô A | 6 | Từ chối | REJECTED, tồn không đổi. | HTTP 200, REJECTED | Pass | <pre>PATCH /api/v1/inventory/disposals/4/reject<br>Request body:<br>{<br>  "responseNote": "Hàng vẫn bán được, chuyển sang khu giảm giá"<br>}<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 4,<br>    "disposalCode": "DSP-20261127-000012",<br>    "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>    "responseNote": "Hàng vẫn bán được, chuyển sang khu giảm giá",<br>    "status": "REJECTED",<br>… (rút gọn)</pre> |
| 4 |  | GM12-04 - Tồn giảm giữa lúc lập và lúc duyệt | Admin | Phiếu 14 cuốn | Lô A bị bán còn 10 | 14 | Duyệt | Duyệt thất bại, không trừ gì; phiếu vẫn PENDING. | Phiếu 34 cuốn lập khi lô còn 34, sau đó lô bị trừ 4. Duyệt: HTTP 409; phiếu còn PENDING | Pass | <pre>PATCH /api/v1/inventory/disposals/5/approve<br>Request body:<br>{<br>  "responseNote": "Đồng ý"<br>}<br>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "f78899fb1f244e62",<br>  "path": "/api/v1/inventory/disposals/5/approve",<br>  "timestamp": "2026-11-27T04:19:02.283039400Z"<br>}<br>… (rút gọn)</pre> |
| 5 | Invalid Partition | GM12-05 - Lý do ngắn như thói quen [Nghi vấn G-08] | Warehouse | Hỏng | Lô A (20) | 1 | Lưu | 400: lý do phải 30-1000 ký tự. Guide không nói mức tối thiểu; kiểm form có báo rõ. | API: HTTP 400 "Reason must be between 30 and 1000 characters". Form: ô lý do bị viền đỏ, không gửi; khung bên phải ghi rõ "at least 30 characters" (xem ảnh). Hệ thống báo rõ; riêng Guide me gợi ý ghi "một dòng" mà không nói mức 30 ký tự | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Hỏng",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 1<br>    }<br>  ]<br>}<br>HTTP 400<br>{<br>  "success": false,<br>… (rút gọn)</pre> |
| 6 |  | GM12-06 - Warehouse tự duyệt | Warehouse | (phiếu PENDING) | Lô A | 6 | Duyệt | 403. | HTTP 403 | Pass | <pre>PATCH /api/v1/inventory/disposals/7/approve<br>Request body:<br>{<br>  "responseNote": "Tự duyệt"<br>}<br>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to perform this action"<br>}</pre> |
| 7 | Valid Boundary | GM12-07 - Lý do đúng 30 ký tự | Warehouse | 30 ký tự | Lô A (20) | 1 | Lưu | 201. | Lý do "Bìa bị rách khi xếp lên kệ số " (30 ký tự): HTTP 201 | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Bìa bị rách khi xếp lên kệ số ",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 1<br>    }<br>  ]<br>}<br>HTTP 201<br>{<br>  "success": true,<br>… (rút gọn)</pre> |
| 8 |  | GM12-08 - Số lượng bằng tồn lô | Warehouse | Lý do hợp lệ trên 30 ký tự | Lô A (20) | 20 | Lưu rồi duyệt | Tồn lô = 0. | Thanh lý hết 30 cuốn của lô BATCH-BIAMEM-261127-001: duyệt 200, còn 0 | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 30<br>    }<br>  ]<br>}<br>HTTP 201<br>{<br>  "success": true,<br>… (rút gọn)</pre> |
| 9 | Invalid Boundary | GM12-09 - Lý do 29 ký tự | Warehouse | 29 ký tự | Lô A (20) | 1 | Lưu | 400. | Lý do "Bìa bị rách khi xếp lên kệ số" (29 ký tự): HTTP 400 {'reason': 'Reason must be between 30 and 1000 characters'} | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Bìa bị rách khi xếp lên kệ số",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 1<br>    }<br>  ]<br>}<br>HTTP 400<br>{<br>  "success": false,<br>… (rút gọn)</pre><br>[Đầy đủ](api/GM12-09.txt) |
| 10 |  | GM12-10 - Vượt tồn lô | Warehouse | Lý do hợp lệ trên 30 ký tự | Lô A (20) | 21 | Lưu | 409: insufficient remaining stock. | Lô còn 0, xin 1: HTTP 409 | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 1<br>    }<br>  ]<br>}<br>HTTP 409<br>{<br>  "success": false,<br>… (rút gọn)</pre> |
| 11 |  | GM12-11 - Số lượng = 0 | Warehouse | Lý do hợp lệ trên 30 ký tự | Lô A (20) | 0 | Lưu | 400. | HTTP 400 | Pass | <pre>POST /api/v1/inventory/disposals<br>Request body:<br>{<br>  "reason": "Sách bị ướt nước mưa khi vận chuyển từ kho Quận 7, hỏng bìa và gáy",<br>  "items": [<br>    {<br>      "batchId": 60,<br>      "quantity": 0<br>    }<br>  ]<br>}<br>HTTP 400<br>{<br>  "success": false,<br>… (rút gọn)</pre> |

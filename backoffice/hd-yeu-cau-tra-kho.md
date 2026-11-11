# Yêu cầu kho và trả hàng về kho

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Sách | Có bookId | Thiếu bookId |  |  |
| Số lượng | &gt;= 1 |  |  | Số lượng = 0 |
| Lý do | Trả kho: 1 đến 1000 ký tự | Trả kho: rỗng |  | &#124;lý do&#124; = 1001 |
| Dòng hàng trả kho | Có ít nhất 1 | Rỗng |  |  |
| RMA và Đơn | Có cả hai, hoặc không có cả hai | Có RMA, thiếu Đơn |  |  |
| Quyền xử lý | Admin duyệt yêu cầu kho, kho duyệt trả kho | Warehouse duyệt yêu cầu kho |  |  |
| Quyền xử lý |  | Duyệt lần hai |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Loại | Data Input: Sách | Data Input: Số lượng | Data Input: Lý do | Data Input: RMA, Đơn | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Tạo yêu cầu kho | Yêu cầu kho | id 50 | 5 | Yeu cau kho kiem thu thu cong |  | 201, trạng thái PENDING | 201, STK-20261110-000018, PENDING | Pass | <pre>HTTP 201<br>{<br>  "id": 2,<br>  "requestCode": "STK-20261110-000018",<br>  "quantity": 5,<br>  "status": "PENDING"<br>}</pre> |
| 2 | Valid Partition | TC02 - Admin duyệt yêu cầu kho, kho thấy kết quả | Yêu cầu kho | id 50 | 5 | Duyet kiem thu |  | APPROVED, warehouse thấy cùng trạng thái và số lượng | 200 APPROVED. Warehouse đọc lại: APPROVED, số lượng 5 | Pass | <pre>HTTP 200<br>{<br>  "id": 2,<br>  "requestCode": "STK-20261110-000018",<br>  "status": "APPROVED",<br>  "responseMessage": "Duyet kiem thu"<br>}</pre> |
| 3 | Valid Partition | TC03 - Seller tạo yêu cầu trả kho | Trả kho | id 46 | 1 | Tra ve kho kiem thu thu cong | RMA 2, Đơn 17 | 201, seller thấy Pending | 201, RTW-20261110-000020, seller thấy Pending | Pass | <pre>HTTP 201<br>{<br>  "id": 1,<br>  "returnCode": "RTW-20261110-000020",<br>  "status": "PENDING",<br>  "source": "CUSTOMER_RETURN"<br>}</pre> |
| 4 | Valid Partition | TC04 - Kho duyệt trả kho, tồn tăng | Trả kho | id 46 | 1 | Kho da nhan | RMA 2, Đơn 17 | APPROVED, tồn tăng 1, seller thấy Approved | 200 APPROVED. Tồn sách id 46 tăng 49 → 50, seller thấy Approved | Pass | <pre>HTTP 200<br>{<br>  "id": 1,<br>  "returnCode": "RTW-20261110-000020",<br>  "status": "APPROVED",<br>  "responseNote": "Kho da nhan"<br>}</pre> |
| 5 | Invalid Partition | TC05 - Yêu cầu kho thiếu sách | Yêu cầu kho | "" | 5 | x |  | 400, không tạo | 400, bookId bắt buộc | Pass | <pre>HTTP 400<br>{<br>  "error": "bookId: Invalid input: expected number, received undefined"<br>}</pre> |
| 6 | Invalid Partition | TC06 - Warehouse duyệt yêu cầu kho | Yêu cầu kho | id 50 | 5 |  |  | 403, chỉ admin được duyệt | 403 FORBIDDEN | Pass | <pre>HTTP 403<br>{<br>  "error": "You do not have permission to perform this action",<br>  "code": "FORBIDDEN"<br>}</pre> |
| 7 | Invalid Partition | TC07 - Trả kho lý do rỗng | Trả kho | id 46 | 1 | "" | RMA 2, Đơn 17 | 400, không tạo | 400, reason tối thiểu 1 ký tự | Pass | <pre>HTTP 400<br>{<br>  "error": "reason: Too small: expected string to have &gt;=1 characters"<br>}</pre> |
| 8 | Invalid Partition | TC08 - Trả kho không có dòng hàng | Trả kho | "" | "" | Tra ve kho | RMA 2, Đơn 17 | 400, không tạo | 400, items phải có ít nhất 1 dòng | Pass | <pre>HTTP 400<br>{<br>  "error": "items: Too small: expected array to have &gt;=1 items"<br>}</pre> |
| 9 | Invalid Partition | TC09 - Có RMA nhưng thiếu Đơn | Trả kho | id 46 | 1 | Tra ve kho | RMA 2, Đơn rỗng | 400, không tạo | 400, returnRequestId và orderId phải đi cùng nhau | Pass | <pre>HTTP 400<br>{<br>  "error": "returnRequestId: returnRequestId and orderId travel together"<br>}</pre> |
| 10 | Invalid Partition | TC10 - Duyệt trả kho lần hai | Trả kho | RTW id 1 |  | lan 2 |  | 409, không duyệt lại | 409 CONFLICT | Pass | <pre>HTTP 409<br>{<br>  "error": "The request conflicts with the current state of the resource.",<br>  "code": "CONFLICT",<br>  "traceId": "7059a77a44d54e60"<br>}</pre> |
| 11 | Invalid Boundary | TC11 - Yêu cầu kho số lượng 0 | Yêu cầu kho | id 50 | 0 | Yeu cau kho |  | 400, không tạo | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "9229b4b7f31a46d7"<br>}</pre> |
| 12 | Invalid Boundary | TC12 - Yêu cầu kho lý do 1001 ký tự | Yêu cầu kho | id 50 | 5 | 'r' x 1001 |  | 400, không tạo | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "d7f51346168640de"<br>}</pre> |
| 13 | Invalid Boundary | TC13 - Trả kho số lượng 0 | Trả kho | id 46 | 0 | Tra ve kho | RMA 2, Đơn 17 | 400, không tạo | 400, quantity tối thiểu 1 | Pass | <pre>HTTP 400<br>{<br>  "error": "items.0.quantity: Too small: expected number to be &gt;=1"<br>}</pre> |
| 14 | Invalid Boundary | TC14 - Trả kho lý do 1001 ký tự | Trả kho | id 46 | 1 | 'r' x 1001 | RMA 2, Đơn 17 | 400, không tạo | 400, reason tối đa 1000 ký tự | Pass | <pre>HTTP 400<br>{<br>  "error": "reason: Too big: expected string to have &lt;=1000 characters"<br>}</pre> |

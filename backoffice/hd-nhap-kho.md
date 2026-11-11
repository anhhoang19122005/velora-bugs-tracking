# Nhập kho theo đơn mua

Hộp đen. Lập Bảng phân tích trước, sau đó mới thiết kế test case. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt.

## Bảng phân tích

| Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|
| Trạng thái đơn mua | ORDERED | APPROVED, chưa thanh toán |  |  |
| Chi tiết nhập | Có ít nhất 1 dòng | Rỗng |  |  |
| Số lượng | 1 đến số lượng đặt |  | Bằng số lượng đặt | Số lượng = 0 |
| Số lượng |  |  |  | Lớn hơn số lượng đặt |
| Giá nhập | &gt;= 0 | Âm |  |  |

## Bảng thiết kế test case

| ID | Condition | Test case name | Data Input: Đơn mua | Data Input: Số lượng | Data Input: Giá nhập | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | TC01 - Nhập đủ đơn mua và nhận hàng | PO 1 (đặt 10, ORDERED) | 10 | 50000 | Tồn kho tăng đúng số nhập | Tồn sách id 50 tăng 0 → 10, storefront hết nhãn hết hàng | Pass | <pre>HTTP 200<br>{<br>  "id": 1,<br>  "importCode": "IMP-20261110-000017",<br>  "received": true<br>}</pre> |
| 2 | Invalid Partition | TC02 - Đơn mua chưa thanh toán | PO 1 (APPROVED) | 5 | 50000 | 409, không cho nhập | 409 CONFLICT | Pass | <pre>HTTP 409<br>{<br>  "error": "The request conflicts with the current state of the resource.",<br>  "code": "CONFLICT",<br>  "traceId": "1b028d67f2b2408e"<br>}</pre> |
| 3 | Invalid Partition | TC03 - Chi tiết rỗng | PO 1 | Không có dòng |  | 400, không cho nhập | 400, details phải có ít nhất 1 dòng | Pass | <pre>HTTP 400<br>{<br>  "error": "details: Too small: expected array to have &gt;=1 items"<br>}</pre> |
| 4 | Invalid Partition | TC04 - Giá nhập âm | PO 1 | 5 | -1 | 400, không cho nhập | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "d285c414c0144840"<br>}</pre> |
| 5 | Valid Boundary | TC05 - Số lượng bằng số đặt | PO 2 (đặt 2) | 2 | 50000 | 201, sau khi nhận hàng tồn tăng 2 | 201, nhận hàng 200. Tồn 10 → 12, storefront hiện "Còn 12 cuốn" | Pass | <pre>HTTP 200<br>{<br>  "id": 2,<br>  "importCode": "IMP-20261110-000018",<br>  "received": true<br>}</pre> |
| 6 | Invalid Boundary | TC06 - Số lượng 0 | PO 1 | 0 | 50000 | 400, không cho nhập | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "error": "The request contains invalid data.",<br>  "code": "VALIDATION_ERROR",<br>  "traceId": "f11c146162194770"<br>}</pre> |
| 7 | Invalid Boundary | TC07 - Vượt số lượng đặt | PO 2 (đặt 2) | 3 | 50000 | 409, không cho nhập | 409 CONFLICT | Pass | <pre>HTTP 409<br>{<br>  "error": "The request conflicts with the current state of the resource.",<br>  "code": "CONFLICT",<br>  "traceId": "0597599b95db4603"<br>}</pre> |

# HD-Phiên bản & giá

[← Tổng quan đợt test](README.md)

Guide me: Thêm phiên bản và giá

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Định dạng | Định dạng sách chưa có | Định dạng sách đã có |  |  |
|  |  |  | Không chọn |  |  |
|  | Giá | &gt;= 0 | Âm | 0 | -1 |
|  |  |  | Trống |  |  |
|  | Tồn ban đầu | Trống hoặc &gt;= 0 | Âm | 0 | -1 |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Vai trò | Data Input: Sách | Data Input: Định dạng | Data Input: Giá | Data Input: Tồn kho ban đầu | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM03-01 - Thêm phiên bản bìa cứng | Seller | Nhà Giả Kim (đã có bìa mềm) | Bìa cứng | 159.000 | (trống) | 201. Hai phiên bản hiện riêng, giá riêng; storefront chọn được cả hai. | POST 201; định dạng công khai: [('Bìa mềm', 79000.0), ('Bìa cứng', 159000.0)] | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 56,<br>  "variantId": 3,<br>  "price": 159000<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 61,<br>    "bookId": 56,<br>    "variantId": 3,<br>… (rút gọn)</pre> |
| 2 |  | GM03-02 - Nhập tồn kho ban đầu &gt; 0 [Nghi vấn G-07] | Seller | Sách mới chưa nhập kho | Ebook | 30.000 | 10 | Ghi lại: catalog hiện tồn 10 nhưng kho (inventory) không có lô. Đặt hàng 1 cuốn: kỳ vọng bị báo hết hàng. Xác nhận hành vi và hỏi nghiệp vụ. | Phiên bản Bìa cứng tạo kèm tồn 10: storefront hiện stockQuantity=10 cho định dạng này, trong khi kho (inventory) báo {'bookId': 60, 'variantId': None, 'totalQuantity': 0}. Thêm giỏ: HTTP 200. Đặt hàng: HTTP 409 Not enough stock to fulfil this request.<br>Bug [B04](loi.md#b04)<br>[Ảnh 1](images/GM03-02-1.png)<br>[Ảnh 2](images/GM03-02-2.png) | Fail | <pre>GET /api/v1/books/60<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 60,<br>    "slug": "gm-test-11271102-sach-ton-ao",<br>    "title": "[GM-TEST-11271102] Sách tồn ảo",<br>    "author": "GM Tác giả",<br>    "description": "Sách test của đợt GM-TEST-11271102",<br>    "publicationYear": 2020,<br>    "weightGrams": null,<br>    "pageCount": 227,<br>    "price": 30000.0,<br>… (rút gọn)</pre><br>[Đầy đủ](api/GM03-02.txt) |
| 3 | Invalid Partition | GM03-03 - Trùng định dạng | Seller | Nhà Giả Kim | Bìa mềm (đã có) | 90.000 | — | 409: BookVariant already exists. | HTTP 409 The request conflicts with the current state of the resource. | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 56,<br>  "variantId": 1,<br>  "price": 90000<br>}<br>HTTP 409<br>{<br>  "success": false,<br>  "code": "CONFLICT",<br>  "message": "The request conflicts with the current state of the resource.",<br>  "traceId": "bab5af8c-6148-400f-9a7b-382b86901a3a",<br>  "path": "/api/v1/book-variants",<br>… (rút gọn)</pre> |
| 4 |  | GM03-04 - Không nhập giá | Seller | Nhà Giả Kim | Ebook | (trống) | — | 400, báo ở ô giá. | HTTP 400 | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 57,<br>  "variantId": 3<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "f5d47307-b76b-414c-9fe4-4e42c3d60d16",<br>  "path": "/api/v1/book-variants",<br>  "timestamp": "2026-11-27T04:07:02.865242400Z",<br>… (rút gọn)</pre> |
| 5 |  | GM03-05 - Warehouse sửa phiên bản | Warehouse | Nhà Giả Kim | Ebook | 50.000 | — | 403. | HTTP 403 | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 57,<br>  "variantId": 3,<br>  "price": 50000<br>}<br>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to perform this action"<br>}</pre> |
| 6 | Valid Boundary | GM03-06 - Giá = 0 | Seller | Nhà Giả Kim | Ebook | 0 | 0 | Code cho phép. Ghi nhận và hỏi nghiệp vụ. | HTTP 201: hệ thống chấp nhận giá 0 (cần nghiệp vụ xác nhận) | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 57,<br>  "variantId": 3,<br>  "price": 0,<br>  "stockQuantity": 0<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 64,<br>    "bookId": 57,<br>… (rút gọn)</pre> |
| 7 | Invalid Boundary | GM03-07 - Giá = -1 | Seller | Nhà Giả Kim | Ebook | -1 | — | 400. | HTTP 400 | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 58,<br>  "variantId": 3,<br>  "price": -1<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "7a04e983-a4f3-411c-bc8f-c4d182f3606f",<br>  "path": "/api/v1/book-variants",<br>… (rút gọn)</pre> |
| 8 |  | GM03-08 - Tồn ban đầu = -1 | Seller | Nhà Giả Kim | Ebook | 30.000 | -1 | 400. | HTTP 400 | Pass | <pre>POST /api/v1/book-variants<br>Request body:<br>{<br>  "bookId": 58,<br>  "variantId": 3,<br>  "price": 30000,<br>  "stockQuantity": -1<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "abfe0090-a722-48ad-842c-bdd763f7cd3b",<br>… (rút gọn)</pre> |

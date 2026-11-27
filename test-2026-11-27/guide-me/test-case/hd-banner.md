# HD-Banner

[← Kết quả Guide me](../README.md)

Guide me: Đăng một banner (chỉ Admin thấy các bước)

Hộp đen. Actual Result chỉ ghi khi đã chạy thật trên trình duyệt. API Response ghi mã HTTP và body khi trình duyệt không cho thấy lỗi. Mã G-xx: xem sheet Lệch Guide-Code.

## Bảng phân tích

|   | Condition | Valid Partition | Invalid Partition | Valid Boundary | Invalid Boundary |
|---|---|---|---|---|---|
|  | Vai trò | Admin | Seller |  |  |
|  |  |  | Khách |  |  |
|  | Tên | 1-255 | Rỗng | 255 | 256 |
|  | Ảnh | URL &lt;= 500 ký tự | Thiếu | 500 | 501 |
|  |  |  | Không phải ảnh |  |  |
| Bảng thiết kế test case |  |  |  |  |  |

## Test case

| ID | Condition | Test case name | Data Input: Vai trò | Data Input: Tên banner | Data Input: Ảnh | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Valid Partition | GM04-01 - Admin đăng banner | Admin | Sale tháng 12 | banner ngang 1600x500.jpg | 201. Banner hiện trên trang chủ storefront. | POST 201; banner trong danh sách công khai: True | Pass | <pre>POST /api/v1/banners<br>Request body:<br>{<br>  "name": "[GM-TEST-11271102] Sale tháng 12",<br>  "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>}<br>HTTP 201<br>{<br>  "success": true,<br>  "data": {<br>    "id": 1,<br>    "name": "[GM-TEST-11271102] Sale tháng 12",<br>    "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>  },<br>… (rút gọn)</pre> |
| 2 |  | GM04-02 - Tìm nút bật / tắt và ô đường dẫn như guide mô tả [Nghi vấn G-15] | Admin | Banner thử | banner.jpg | Guide nói banner tắt vẫn lưu được và có đường dẫn. API chỉ nhận tên và ảnh. Ghi lại form có hai thứ này không và có tác dụng không. | Form banner chỉ có các ô: ['field-name', 'field-imageUrl'] (xem ảnh). Không có nút bật/tắt và không có ô đường dẫn như bước Lưu của Guide me nói ("Banner tắt vẫn lưu được — bật lên khi ảnh và đường dẫn đã đúng"). API BannerRequest cũng chỉ có name, imageUrl<br>Bug [B09](../loi.md#b09)<br>[Ảnh 1](../images/GM04-02-1.png)<br>[Ảnh 2](../images/GM04-02-2.png)<br>[Ảnh 3](../images/GM04-02-3.png) | Fail | <pre>GET /api/v1/banners/1<br>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "id": 1,<br>    "name": "[GM-TEST-11271102] Sale tháng 12",<br>    "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>  },<br>  "message": "OK",<br>  "timestamp": "2026-11-27T04:37:46.077658900Z"<br>}</pre><br>[Đầy đủ](../api/GM04-02.txt) |
| 3 |  | GM04-03 - Ảnh dọc | Admin | Banner dọc | ảnh dọc 600x1200.jpg | Lưu được; trang chủ cắt thành dải ngang như tip nói. Ghi ảnh chụp. | Bỏ qua phần hiển thị cắt ảnh (cần ảnh dọc thật); lưu banner hoạt động như case 1 | Blocked |  |
| 4 | Invalid Partition | GM04-04 - Seller đăng banner | Seller | Banner seller | banner.jpg | Không thấy nút; API trả 403. | HTTP 403 | Pass | <pre>POST /api/v1/banners<br>Request body:<br>{<br>  "name": "[GM-TEST-11271102] Banner seller",<br>  "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>}<br>HTTP 403<br>{<br>  "success": false,<br>  "code": "FORBIDDEN",<br>  "message": "You do not have permission to perform this action"<br>}</pre> |
| 5 |  | GM04-05 - Thiếu ảnh | Admin | Không ảnh | (trống) | 400. | HTTP 400 | Pass | <pre>POST /api/v1/banners<br>Request body:<br>{<br>  "name": "[GM-TEST-11271102] Không ảnh",<br>  "imageUrl": ""<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "eebf1712-4b65-41f5-bba2-9cc902a36fbe",<br>  "path": "/api/v1/banners",<br>  "timestamp": "2026-11-27T04:07:12.854309Z",<br>… (rút gọn)</pre> |
| 6 | Invalid Boundary | GM04-06 - Tên 256 ký tự | Admin | 256 ký tự | banner.jpg | 400. | HTTP 400 | Pass | <pre>POST /api/v1/banners<br>Request body:<br>{<br>  "name": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",<br>  "imageUrl": "https://pub-51c65cc9b6514e65ab4891a65fc437cf.r2.dev/images/dbca62fc-9090-4523-b4d8-dbf533c72e5b.webp"<br>}<br>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "29ac444c-8048-4c68-b0a8-45a1e353608f",<br>  "path": "/api/v1/banners",<br>  "timestamp": "2026-11-27T04:07:12.860756500Z",<br>… (rút gọn)</pre> |

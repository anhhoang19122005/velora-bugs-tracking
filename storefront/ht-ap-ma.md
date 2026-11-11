# PromotionServiceImpl.validateCode

Hộp trắng. Vẽ workflow của code trước, sau đó thiết kế test case phủ từng nhánh. Actual Result chỉ ghi khi nhánh đó đã chạy thật.

## Workflow code

Bắt đầu → N1 mã rỗng hoặc &gt; 100 ký tự? → N2 subtotal hợp lệ? → N3 tìm thấy mã? → N4 đang ACTIVE? → N5 trong thời hạn? → N6 còn lượt? → N7 người dùng đã dùng? → N8 đủ giá trị tối thiểu? → N9 tính giảm giá → valid:true

| Node | Loại | Điều kiện / Hành động | Vị trí code | Nếu đúng | Nếu sai |
|---|---|---|---|---|---|
| N1 | Quyết định | normalizedCode rỗng hoặc dài hơn 100 | PromotionServiceImpl.java:177 | 400 VALIDATION_ERROR | Đi N2 |
| N2 | Quyết định | orderSubtotal null hoặc âm | PromotionServiceImpl.java:180 | 400 VALIDATION_ERROR | Đi N3 |
| N3 | Quyết định | findByCode có kết quả | PromotionServiceImpl.java:183-185 | Đi N4 | valid:false "Promotion code not found" |
| N4 | Quyết định | isActive = true và status = ACTIVE | PromotionServiceImpl.java:271 | Đi N5 | valid:false "Promotion is not active" |
| N5 | Quyết định | startDate &lt;= hôm nay &lt;= endDate | PromotionServiceImpl.java:276 | Đi N6 | valid:false "outside its redeemable window" |
| N6 | Quyết định | quantity &gt; 0 | PromotionServiceImpl.java:280 | Đi N7 | valid:false "fully redeemed" |
| N7 | Quyết định | Người dùng đã dùng mã này | PromotionServiceImpl.java:252 | valid:false "already redeemed" | Đi N8 |
| N8 | Quyết định | subtotal &gt;= priceOrderActive | PromotionServiceImpl.java:255,288 | Đi N9 | valid:false "does not meet the minimum" |
| N9 | Kết thúc | Tính discountAmount, trả valid:true | PromotionServiceImpl.java:262-264 | valid:true |  |

## Bảng thiết kế test case theo đường đi

| ID | Đường đi (Node) | Test case name | Data Input | Expected Result | Actual Result | Status | API Response |
|---|---|---|---|---|---|---|---|
| 1 | N1(đúng) | WB01 - Mã toàn khoảng trắng | code "   ", subtotal 25000 | 400 VALIDATION_ERROR | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "728b6479-4973-4787-9976-85c2ea7fc843",<br>  "path": "/api/v1/promotions/validate/%20%20%20"<br>}</pre> |
| 2 | N1(sai) → N2(đúng) | WB02 - Subtotal âm | code MANUAL1110, subtotal -1 | 400 VALIDATION_ERROR | 400 VALIDATION_ERROR | Pass | <pre>HTTP 400<br>{<br>  "success": false,<br>  "code": "VALIDATION_ERROR",<br>  "message": "The request contains invalid data.",<br>  "traceId": "12a6c3d9-b3ce-41f2-8f37-594e43b78a3a",<br>  "path": "/api/v1/promotions/validate/MANUAL1110"<br>}</pre> |
| 3 | N3(sai) | WB03 - Mã không tồn tại | code SAIMA123, userId 104, subtotal 25000 | valid:false, "Promotion code not found" | valid:false, reason "Promotion code not found" | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": false,<br>    "promotionId": null,<br>    "code": "SAIMA123",<br>    "discountPercent": null,<br>    "discountAmount": null,<br>    "reason": "Promotion code not found"<br>  },<br>  "message": "OK"<br>}</pre> |
| 4 | N3 → N4(sai) | WB04 - Mã chưa duyệt | Mã đang PENDING | valid:false, "Promotion is not active" | valid:false, "Promotion is not active" | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": false,<br>    "promotionId": 1,<br>    "code": "PROMO1787397035424952",<br>    "reason": "Promotion is not active"<br>  },<br>  "message": "OK"<br>}</pre> |
| 5 | N4 → N5(sai) | WB05 - Mã hết hạn | Mã ACTIVE, endDate đã qua | valid:false, "outside its redeemable window" | valid:false, "Promotion is outside its redeemable window" | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": false,<br>    "promotionId": 4,<br>    "code": "PROMO1787397038060993",<br>    "reason": "Promotion is outside its redeemable window"<br>  },<br>  "message": "OK"<br>}</pre> |
| 6 | N5 → N6(sai) | WB06 - Mã hết lượt | Mã ACTIVE, quantity 0 | valid:false, "fully redeemed" | Không có mã ACTIVE nào quantity 0, và form không cho tạo số lượng 0 | Blocked | Không gọi API |
| 7 | N6 → N7(đúng) | WB07 - Người dùng đã dùng mã | userId đã có bản ghi sử dụng | valid:false, "already redeemed" | Không tạo được điều kiện: lượt dùng chỉ ghi sau khi đơn có mã được thanh toán, mà đặt hàng có mã đang lỗi (Bug SF-08) | Blocked | Không gọi API |
| 8 | N7 → N8(sai) | WB08 - Chưa đủ giá trị tối thiểu | priceOrderActive 100000, subtotal 25000 | valid:false, "does not meet the minimum" | valid:false, "does not meet the minimum" với mã MINORDER1110 | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": false,<br>    "promotionId": 31,<br>    "code": "MINORDER1110",<br>    "reason": "Order subtotal does not meet the minimum required for this promotion"<br>  },<br>  "message": "OK"<br>}</pre> |
| 9 | N1 → N2 → N3 → N4 → N5 → N6 → N7 → N8 → N9 | WB09 - Mã hợp lệ | code MANUAL1110, userId 104, subtotal 25000 | valid:true, discountAmount 2500 | valid:true, discountPercent 10.00, discountAmount 2500.00 | Pass | <pre>HTTP 200<br>{<br>  "success": true,<br>  "data": {<br>    "valid": true,<br>    "promotionId": 27,<br>    "code": "MANUAL1110",<br>    "discountPercent": 10.0,<br>    "discountAmount": 2500.0,<br>    "reason": null<br>  },<br>  "message": "OK"<br>}</pre> |

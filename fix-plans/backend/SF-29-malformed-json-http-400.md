# SF-29: Body JSON hỏng hoặc enum sai trả 500

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | order-service, promotion-service |
| **Bug** | [Chi tiết SF-29](../../storefront/loi.md#sf-29) |
| **Điểm vào source** | `GlobalExceptionHandler` |

## Nguyên nhân

Spring/Jackson báo lỗi đọc body trước khi chạy nghiệp vụ, nhưng handler hiện trả 500 cho một số lỗi đọc request.

## Thay đổi

1. Dùng cách Identity/Catalog ánh xạ HttpMessageNotReadableException thành MALFORMED_REQUEST 400. Dùng định dạng lỗi chung đang có.
2. Thêm test JSON hỏng, enum sai và số vượt kiểu, cùng control request hợp lệ.

## Code dự kiến

Trong Order/Promotion advice, dùng cùng cách dựng 400 MALFORMED_REQUEST hiện có của Identity/Catalog.

```java
@ExceptionHandler(HttpMessageNotReadableException.class)
ResponseEntity<?> handleUnreadableBody(HttpMessageNotReadableException ex) {
    return malformedRequest();
}
```

## Kiểm thử lại

JSON lỗi cú pháp, enum sai và số vượt kiểu trả 400. Request hợp lệ giữ hành vi hiện tại.

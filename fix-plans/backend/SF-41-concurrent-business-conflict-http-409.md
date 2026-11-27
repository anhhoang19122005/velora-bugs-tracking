# SF-41: Request trùng đồng thời trả 500 thay vì 409

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backend`, nhiều service |
| **Bug** | [Chi tiết SF-41](../../storefront/loi.md#sf-41) |
| **Điểm vào source** | `GlobalExceptionHandler và constraint của từng service` |

## Nguyên nhân

Dữ liệu chỉ đổi một lần, nhưng các request thua có thể trả lỗi 500 dù nguyên nhân là xung đột nghiệp vụ.

## Thay đổi

1. Xác định loại exception theo từng luồng qua log/test. Thêm ánh xạ 409 ở service sở hữu cho lỗi phiên bản hoặc constraint nghiệp vụ đã xác định.
2. Giữ API vốn trả kết quả cũ khi gọi lại theo đúng contract. Lỗi DB bất ngờ tiếp tục ghi log và trả lỗi hệ thống.

## Code dự kiến

Trong handler của service sở hữu, chỉ trả 409 khi gặp đúng constraint nghiệp vụ đã xác định. Dùng response và ghi log chung đang có.

```java
if (isKnownConflictConstraint(exception)) {
    return conflictResponse();
}
return logAndReturnInternalError(exception);
```

## Kiểm thử lại

Gửi đồng thời trên các endpoint trong tracker. Mỗi thao tác chỉ đổi dữ liệu một lần. Request thua trả 409 hoặc kết quả idempotent theo API. Lỗi DB bất ngờ vẫn ghi log và trả 500.

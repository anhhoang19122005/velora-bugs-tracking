# B14: Guide me mô tả trạng thái Đã nhận cho yêu cầu nhập

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice` |
| **Bug** | [Chi tiết B14](../../test-2026-11-27/loi.md#b14) · GM08-04 |
| **Điểm vào source** | `Guide me yêu cầu nhập` |

## Nguyên nhân

Guide gán trạng thái RECEIVED cho yêu cầu nhập trong khi trạng thái này thuộc đơn mua.

## Thay đổi

1. Đổi mô tả theo đối tượng: yêu cầu dừng ở ORDERED, còn PO chuyển sang RECEIVED khi nhận đủ hàng.

## Code dự kiến

Trong apps/warehouse/src/messages/vi.json, stock-request-create.steps.status.tip. Dùng câu riêng để phân biệt đơn mua và yêu cầu nhập.

```diff
- "tip": "Chờ xử lý → Đã duyệt → Đã đặt hàng → Đã nhận là trọn đường đi. Bị từ chối thì dừng ở đó. Không bước nào tự chạy — mỗi bước đều là một người bấm nút."
+ "tip": "Yêu cầu nhập đi từ Chờ xử lý đến Đã duyệt rồi Đã đặt hàng. Khi nhận đủ hàng, xem trạng thái Đã nhận trên đơn mua."
```

## Kiểm thử lại

Khi nhập đủ, đối chiếu riêng trạng thái của yêu cầu nhập và đơn mua.

## Liên quan

[B15](../../fix-plans/backoffice/B15-guide-purchase-order-before-receipt.md)

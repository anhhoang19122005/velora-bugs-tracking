# Đợt test 2026-11-27

Chạy trên máy local, nối DB và broker dùng chung (`taschen-platform/.env`). Backend `d5b6ac2`, backoffice `8e1ecfbe`, storefront `0a72cc4`.

| Phần | Nội dung | Kết quả |
|---|---|---|
| [Guide me](guide-me/README.md) | Nghiệp vụ 4 vai trò theo chức năng Guide me: 162 case, 6 luồng đầu-cuối | 141 Pass, 18 Fail, 3 Blocked; 15 lỗi |
| [Phân quyền](phan-quyen/README.md) | Vai trò làm việc không được phép: 110 API và 166 lần mở trang | Không vai trò nào vượt quyền; 3 lỗi (2 do dữ liệu DB dùng chung) |
| [Retest](retest/README.md) | Chạy lại 19 lỗi chờ retest | 15 đã xác nhận, 3 một phần, 1 còn lỗi |

## Lỗi và mã theo dõi

Lỗi được đánh mã trong đợt (B.., P..) rồi đưa vào danh sách chung với mã SF/BO; trạng thái theo dõi ở [trang-thai.md](../trang-thai.md).

| Mã trong đợt | Mã theo dõi |
|---|---|
| [B01](guide-me/loi.md#b01) | [BO-13](../backoffice/loi.md#bo-13) |
| [B02](guide-me/loi.md#b02) | [SF-38](../storefront/loi.md#sf-38) (đã có) |
| [B03](guide-me/loi.md#b03) | [SF-45](../storefront/loi.md#sf-45) |
| [B04](guide-me/loi.md#b04) | [SF-46](../storefront/loi.md#sf-46) |
| [B05](guide-me/loi.md#b05) | [BO-14](../backoffice/loi.md#bo-14) |
| [B06](guide-me/loi.md#b06) | [BO-15](../backoffice/loi.md#bo-15) |
| [B07](guide-me/loi.md#b07) | [BO-16](../backoffice/loi.md#bo-16) |
| [B08](guide-me/loi.md#b08) | [BO-26](../backoffice/loi.md#bo-26) |
| [B09](guide-me/loi.md#b09) | [BO-17](../backoffice/loi.md#bo-17) |
| [B10](guide-me/loi.md#b10) | [BO-18](../backoffice/loi.md#bo-18) |
| [B11](guide-me/loi.md#b11) | [BO-19](../backoffice/loi.md#bo-19) |
| [B12](guide-me/loi.md#b12) | [BO-20](../backoffice/loi.md#bo-20) |
| [B13](guide-me/loi.md#b13) | [BO-21](../backoffice/loi.md#bo-21) |
| [B14](guide-me/loi.md#b14) | [BO-22](../backoffice/loi.md#bo-22) |
| [B15](guide-me/loi.md#b15) | [BO-23](../backoffice/loi.md#bo-23) |
| [P1](phan-quyen/README.md#4-phát-hiện) | [SF-47](../storefront/loi.md#sf-47) |
| [P2](phan-quyen/README.md#4-phát-hiện) | [BO-24](../backoffice/loi.md#bo-24) |
| [P3](phan-quyen/README.md#4-phát-hiện) | [BO-25](../backoffice/loi.md#bo-25) |

## Cấu trúc

```text
test-2026-11-27/
├── guide-me/
│   ├── README.md          kết quả, môi trường, case bị chặn
│   ├── loi.md · luong.md · lech-guide-code.md
│   ├── test-case/         15 bảng test case (hd-*.md)
│   ├── images/            ảnh của case Fail và Blocked
│   └── api/               API response từng case
├── phan-quyen/
│   ├── README.md          báo cáo
│   ├── images/            ảnh đăng nhập nhầm ứng dụng và so sánh nút
│   └── data/              kết quả API và giao diện (JSON)
└── retest/
    ├── README.md          kết quả chạy lại 19 lỗi
    └── <mã lỗi>/          ảnh và API response
```

Video quay các phiên test không đưa lên repo.

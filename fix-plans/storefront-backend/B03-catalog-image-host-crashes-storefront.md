# B03: Ảnh bìa từ host ngoài cấu hình làm lỗi toàn bộ trang chủ

| Mục | Nội dung |
|---|---|
| **Mức độ** | Major |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-storefront`, catalog-service, `taschen-backoffice` |
| **Bug** | [Chi tiết B03](../../test-2026-11-27/loi.md#b03) · GM13-03 |
| **Điểm vào source** | `next.config.ts`, `BookCard`, `ProductGallery` |

## Nguyên nhân

Một ảnh bìa sai làm lỗi cả trang. next/image kiểm remotePatterns khi render, trong khi Catalog hiện nhận được URL mà Storefront không hỗ trợ.

## Thay đổi

1. Tách cấu hình ảnh Next.js dùng chung trong Storefront để cùng một danh sách cấp cho remotePatterns và bộ kiểm URL trước khi render. Áp dụng ở các ảnh Catalog đang dùng next/image, bắt đầu từ thẻ sách trang chủ, rồi rà danh sách, chi tiết và các màn dùng lại ảnh bìa.
2. Dùng ảnh thay thế ngay khi URL thiếu/sai/ngoài cấu hình. Dùng onError ở thành phần client cho ảnh hợp lệ nhưng tải lỗi, và đặt lại trạng thái khi URL đổi.
3. Trong PR Catalog/Backoffice riêng, kiểm URL ở điểm ghi dữ liệu, đồng bộ cấu hình host được hỗ trợ theo môi trường, và trả lỗi tại ô URL ảnh. Kiểm tra các URL cũ cần thay thế.

## Tuân thủ quy tắc

Kiểm URL bằng danh sách cấu hình duy nhất trong Storefront. Giữ logic ảnh thay thế ở lớp hiển thị, validation lưu URL ở Catalog. Ưu tiên các component ảnh hiện có, giới hạn helper mới vào phần kiểm URL dùng chung. Dùng danh sách host cụ thể theo môi trường.

## Code dự kiến

Trong cấu hình ảnh Storefront, chuyển danh sách host hiện có thành danh sách nguồn duy nhất. Chạy bộ lọc ở server hoặc truyền cùng danh sách đã phân giải sang client để khớp giá trị R2 lúc build. Trong Catalog, dùng cùng chính sách với validator URL của request tạo/sửa.

```tsx
const remotePatterns = allowedImageOrigins.map(({ protocol, hostname, port = "" }) => ({
  protocol, hostname, port,
}));

function resolveCatalogImage(value: string | null): string | null {
  if (!value) return null;
  try {
    const url = new URL(value);
    const allowed = allowedImageOrigins.some(({ protocol, hostname, port }) =>
      url.protocol === protocol + ":" && url.hostname === hostname && url.port === port && !url.username && !url.password,
    );
    return allowed ? url.href : null;
  } catch {
    return null;
  }
}

const src = resolveCatalogImage(book.imageUrl);
return <BookCover key={src ?? "placeholder"} src={src} />;
```

Trong BookCover, dùng bố cục ảnh hiện có. Khi bình thường giữ kích thước và alt của ảnh; khi lỗi tải chuyển sang phần giữ chỗ.

```tsx
const [failed, setFailed] = useState(false);
return src && !failed
  ? <Image src={src} alt={title} fill onError={() => setFailed(true)} />
  : <BookCoverPlaceholder />;
```

## Kiểm thử lại

GM13-03. Một bìa lỗi ở trang chủ, danh sách hoặc chi tiết chỉ ảnh hưởng chỗ đặt ảnh. Kiểm URL rỗng, sai cú pháp, sai host, ảnh 404 và ảnh R2 hợp lệ. API trả 4xx có lỗi trường khi lưu URL ngoài danh sách; bản ghi cũ vẫn hiển thị bằng ảnh thay thế.

Chạy thêm Search với từ khóa sapiens và ảnh từ x.test. Thẻ sách dùng ảnh thay thế khi ảnh gốc tải lỗi. Danh sách vẫn hiện và điều hướng sang chi tiết được. Rà đường render ảnh thường trong Search để áp cùng hành vi ảnh thay thế. [Bằng chứng retest 27/11](../../ui/loi.md#b03)

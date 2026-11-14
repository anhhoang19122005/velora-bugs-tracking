# BO-01: Hộp Guided tasks trống phủ lên trang không có quyền

| Mục | Nội dung |
|---|---|
| **Mức độ** | Minor |
| **Trạng thái** | Chưa sửa |
| **Repo** | `taschen-backoffice`, số dòng theo `develop` `02da243d` |
| **Nhánh đề xuất** | `fix/guide-no-empty-chooser`, tách từ `develop` |
| **Khối lượng** | Khoảng 6 dòng code, 1 test |
| **Bug và ảnh** | [Chi tiết bug](../../backoffice/loi.md#bo-01), [Ảnh 1](../../images/BO-01-1.jpg) |

## Nguyên nhân

`packages/ui/src/guide/guide.tsx:157-162`: ở lần đăng nhập đầu, `GuideProvider` ghi nhận "đã mời" rồi tự mở hộp chọn (`view = chooser`) mà không xét console này có tác vụ nào cho vai trò của người đọc hay không. Dòng `310` vẽ hộp chọn chỉ dựa vào `view.kind === "chooser"`.

Seller đăng nhập ở console admin: `GUIDE_TASKS` của admin lọc theo vai trò `SELLER` ra danh sách rỗng, nên hộp Guided tasks trống hiện đè lên trang `/forbidden`. Ngoài ra lời mời bị ghi là đã dùng, nên khi seller sang đúng console của mình sẽ không còn được mời nữa.

## Thay đổi

File: `packages/ui/src/guide/guide.tsx`

### 1. Dòng 157-162: không mời khi không có gì để mời

```diff
-      // First sign-in: offer the tasks once, and only once. ...
-      const offered = { ...FRESH_PROGRESS, dismissed: true };
+      // First sign-in: offer the tasks once, and only once. ...
+      // A console with nothing for these roles has nothing to offer; keep the offer for one that does.
+      if (!registry.some((task) => hasSomethingFor(roles, registry, task))) {
+        setProgress(FRESH_PROGRESS);
+        return;
+      }
+      const offered = { ...FRESH_PROGRESS, dismissed: true };
```

**Vì sao:** dùng lại đúng `hasSomethingFor` mà `tasks` (dòng 184-197) đang dùng để lọc, nên hai chỗ không lệch nhau. Không lưu `dismissed`, để lời mời còn nguyên cho console của chính người đó.

### 2. Dòng 310: không vẽ hộp chọn rỗng

```diff
-      {view.kind === "chooser" && (
+      {view.kind === "chooser" && tasks.length > 0 && (
```

**Vì sao:** chặn mọi đường khác dẫn tới hộp rỗng, không chỉ lần đăng nhập đầu.

## Test

`packages/ui/src/guide/` chưa có test cho `GuideProvider`. Thêm `guide.test.tsx` (Vitest + Testing Library): render `GuideProvider` với `roles={["SELLER"]}` và một registry chỉ có tác vụ của `ADMIN`, giả lập `loadGuideProgress` trả `null` (lần đầu). Kỳ vọng: không có dialog nào, và `saveGuideProgress` không được gọi.

## Kiểm thử lại

- Đăng nhập seller, mở console admin: trang `/forbidden` hiện gọn, không có hộp Guided tasks.
- Sang console seller: hộp Guided tasks vẫn được mời lần đầu.
- `pnpm lint`, `pnpm typecheck`, `pnpm test` ở gốc backoffice.

## Tuân thủ quy tắc

Biome, 2 dấu cách. Thay đổi nằm trong `packages/ui`, không import code của app.

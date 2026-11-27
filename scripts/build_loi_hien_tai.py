# -*- coding: utf-8 -*-
"""Build loi-hien-tai.md: every bug that is not closed, in one file, for people and agents.

Sources (edit those, not the output):
  - trang-thai.md                  which bugs are open and their tracking state
  - storefront/loi.md, backoffice/loi.md, ui/loi.md   the full record of each bug

Run from the repo root:  python scripts/build_loi_hien_tai.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = "loi-hien-tai.md"
GROUPS = ["Cần sửa", "Cần xác nhận", "Chờ retest"]
SOURCES = ["storefront/loi.md", "backoffice/loi.md", "ui/loi.md"]
CODE = re.compile(r"^[A-Z]{2}-\d\d$")

# Bugs fixed in the front end's look, layout, wording or interaction. Every UI-xx code is UI as well.
# Everything else is logic: business rules, data, API contracts, concurrency, configuration, routing.
# Add a code here when a new UI bug is recorded under an SF/BO code.
UI_CODES = {
    "SF-11", "SF-13", "SF-14", "SF-17", "SF-18", "SF-19", "SF-20", "SF-21", "SF-22", "SF-23", "SF-24", "SF-25",
    "SF-26", "SF-27", "SF-32",
    "BO-01", "BO-07", "BO-25",
    # Guide me wording that disagrees with what the screens do
    "BO-17", "BO-18", "BO-19", "BO-20", "BO-21", "BO-22", "BO-23",
}
KINDS = ["Logic", "Giao diện"]


def kind(code):
    return "Giao diện" if code.startswith("UI-") or code in UI_CODES else "Logic"


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def split_row(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def status_rows():
    """{code: (group, {column: cell})} from the open sections of the status board."""
    text = read("trang-thai.md")
    rows = {}
    for group in GROUPS:
        start = text.index(f"## {group}\n")
        end = text.find("\n## ", start + 3)
        header = None
        for line in text[start:end if end > 0 else None].split("\n"):
            if not line.startswith("|") or set(line) <= set("|- "):
                continue
            cells = split_row(line)
            if cells[0] == "Mã":
                header = cells
                continue
            code = re.match(r"\[([A-Z]{2}-\d\d)\]", cells[0])
            if header and code:
                rows[code[1]] = (group, dict(zip(header, cells)))
    return rows


def records():
    """{code: (source file, section text)} for every '## CODE' section, plus UI notes kept under '### CODE'."""
    out, notes = {}, {}
    for src in SOURCES:
        text = read(src)
        parts = re.split(r"(?m)^(#{2,3}) ([A-Z]{2}-\d\d)\s*$", text)
        for i in range(1, len(parts), 3):
            level, code, body = parts[i], parts[i + 1], parts[i + 2]
            body = re.split(r"(?m)^## ", body)[0].rstrip()
            if level == "##" and code not in out:
                out[code] = (src, body)
            elif level == "###":
                notes.setdefault(code, []).append((src, body))
    return out, notes


def relink(body, src, included):
    """Make links from a source file correct from the repo root; keep in-file anchors when the target is here."""
    base = os.path.dirname(src)

    def fix(m):
        text, target = m[1], m[2]
        if re.match(r"[a-z]+:", target):
            return m[0]
        path, _, anchor = target.partition("#")
        if anchor and anchor.upper() in included and (not path or path.endswith("loi.md")):
            return f"[{text}](#{anchor})"
        full = os.path.normpath(os.path.join(base, path or os.path.basename(src))).replace("\\", "/")
        return f"[{text}]({full}{'#' + anchor if anchor else ''})"

    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", fix, body)


def main():
    status = status_rows()
    found, notes = records()
    included = {c for c in status if c in found}
    order = {"Major": 0, "Minor": 1}
    lines = [
        "# Lỗi hiện tại",
        "",
        "Mỗi lỗi gồm: trạng thái theo dõi (từ bảng trạng thái), rồi hồ sơ lỗi nguyên văn (bước tái hiện, mong đợi, "
        "thực tế, API response, ảnh). Link trong file đã chỉnh để mở đúng từ thư mục gốc của repo.",
        "",
        "## Mục lục",
        "",
        "Chia hai loại. **Logic**: quy tắc nghiệp vụ, dữ liệu, API, đồng thời, cấu hình, điều hướng. "
        "**Giao diện**: bố cục, hiển thị, chữ, bản dịch, thao tác trên màn hình, và lời hướng dẫn Guide me khác với màn hình. "
        "Phân loại khai báo trong `UI_CODES` của script.",
    ]
    ordered = sorted(status, key=lambda c: (GROUPS.index(status[c][0]), order.get(status[c][1].get("Mức độ"), 2), c))
    for k in KINDS:
        mine = [c for c in ordered if kind(c) == k]
        lines += ["", f"### Lỗi {k.lower()} ({len(mine)})", "", "| Mã | Mức độ | Nhóm | Lỗi |", "| --- | --- | --- | --- |"]
        for code in mine:
            group, row = status[code]
            lines.append(f"| [{code}](#{code.lower()}) | {row.get('Mức độ', '')} | {group} | {row.get('Lỗi', '')} |")
    missing = [c for c in ordered if c not in found]
    for group in GROUPS:
        lines += ["", f"## {group}", ""]
        for code in [c for c in ordered if status[c][0] == group]:
            _, row = status[code]
            lines += [f"### {code}", "", f"**{row.get('Lỗi', '')}**", "", "| Theo dõi | |", "| --- | --- |",
                      f"| Loại | {kind(code)} |", f"| Nhóm | {group} |"]
            for key, val in row.items():
                if key in ("Mã", "Lỗi") or not val or val == "—":
                    continue
                lines.append(f"| {key} | {relink(val, 'trang-thai.md', included)} |")
            lines.append("")
            if code in found:
                src, body = found[code]
                lines += [f"Hồ sơ lỗi ({src}):", "", relink(body.strip(), src, included), ""]
            else:
                lines += ["Chưa có hồ sơ lỗi trong các file `loi.md`.", ""]
            for src, body in notes.get(code, []):
                lines += [f"#### Ghi chú thêm ({src})", "", relink(body.strip(), src, included), ""]
    with open(os.path.join(ROOT, OUT), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"{OUT}: {len(ordered)} lỗi, thiếu hồ sơ: {missing or 'không'}")


if __name__ == "__main__":
    main()

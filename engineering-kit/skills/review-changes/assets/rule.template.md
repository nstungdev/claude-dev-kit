---
stage: <stage-name>
stack: <ví dụ: .NET 8 Web API>
updated: <YYYY-MM-DD>
---

# Rule review: <stage-name>

<Một đoạn ngắn: stage này gồm những thư mục nào, kiến trúc chính
(ví dụ Clean Architecture, CQRS với MediatR), và những thứ linter đã bắt
nên KHÔNG lặp lại ở đây.>

## Rule

<Mỗi rule một mục. ID có dạng <PREFIX>-NN, PREFIX viết hoa theo stage
(ví dụ API-01, PORTAL-03). Không đổi ID của rule đã có; rule bỏ đi thì
xóa hẳn, không dùng lại ID.

Trục là một trong: Vòng đời & hiệu suất · Convention · Đặt tên · Business ·
Bảo mật · Kiểm thử.

Mức mặc định là P1. Chỉ dùng P0 cho rule mà vi phạm chắc chắn gây sai
business, mất dữ liệu hoặc lỗ hổng bảo mật. Dùng P2 cho rule thuần style.>

### <PREFIX>-01: <tiêu đề ngắn, dạng mệnh lệnh>

- **Trục:** <trục>
- **Mức:** <P0 | P1 | P2>
- **Rule:** <phát biểu cụ thể, kiểm tra được bằng cách đọc code>
- **Vì sao:** <hậu quả nếu vi phạm>
- **Nguồn:** <`CLAUDE.md` / ADR / cấu hình linter / file mẫu `src/.../Foo.cs`>

Sai:

```<lang>
<đoạn code ngắn vi phạm>
```

Đúng:

```<lang>
<đoạn code ngắn đúng chuẩn>
```

## Ngoại lệ

<Các trường hợp team đã chấp nhận, không báo khi review. Skill chỉ thêm
mục vào đây khi coder đồng ý ở Bước 6. Khi sinh lại file rule, giữ
nguyên toàn bộ mục này.

Mỗi dòng: rule ID · phạm vi (file, glob hoặc mô tả tình huống) · lý do · ngày thêm.>

- <PREFIX>-01 · `src/Legacy/**` · <lý do> · <YYYY-MM-DD>

# Setup: tạo hoặc cập nhật cấu hình code review

Mục tiêu: tạo `.claude/review-changes/` ở gốc repo, gồm:

- `config.yaml`, theo [../assets/config.template.yaml](../assets/config.template.yaml). Giữ nguyên `version` của template và các comment giải thích.
- các file rule theo stage
- `rules/domain.md`

Phần lớn thông tin phải được **dò từ repo**. Coder chủ yếu bấm xác nhận. Câu hỏi mở chỉ dành cho thứ không dò được.

Mọi câu hỏi đều hỏi bằng `AskUserQuestion`, theo nguyên tắc chung trong SKILL.md.

## Chế độ cập nhật

Nếu `config.yaml` đã tồn tại:

1. Tóm tắt cấu hình hiện tại cho coder: các stage, lệnh build/test, nguồn tài liệu, `fix_policy`.
2. Nếu `version` của config nhỏ hơn template, liệt kê các key mới hoặc đổi tên, và đưa việc nâng cấp schema vào phần cập nhật.
3. Hỏi muốn cập nhật phần nào (`multiSelect`): *Stage và phạm vi*, *Lệnh build/test*, *Nguồn tài liệu*, *Sinh lại rule*.
4. Chỉ chạy các bước tương ứng bên dưới. Không ghi đè phần coder không chọn.
5. Khi sinh lại một file rule, giữ nguyên mục "Ngoại lệ" và ID của các rule cũ còn áp dụng.

## Bước S1: Quét repo (chưa hỏi gì)

Thu thập các thông tin sau.

**Stack.** Dò theo manifest, ví dụ:

- `*.sln`, `*.slnx`, `*.csproj`
- `package.json`, `angular.json`, `tsconfig.json`
- `pom.xml`, `build.gradle`
- `go.mod`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `composer.json`

Một repo có thể có nhiều stack, mỗi stack ở một thư mục.

**Lệnh build, test, lint.** Lấy theo thứ tự ưu tiên:

1. CI: `.github/workflows/*`, `azure-pipelines.yml`, `.gitlab-ci.yml`.
2. `scripts` trong `package.json`.
3. `Makefile`.
4. README.

Lấy đúng lệnh team đang dùng, đừng tự nghĩ ra lệnh. Mỗi stack có lệnh riêng, chạy được từ gốc repo (ví dụ `npm --prefix src/Portal run build`), để khi review chỉ build những stage có thay đổi.

**Convention đã được ghi lại:** `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `.editorconfig`, cấu hình linter và formatter, thư mục `docs/adr`.

**Thứ nên loại trừ:**

- thư mục build output
- thư mục dependency
- file generated: `*.Designer.cs`, migration snapshot, lock file, code sinh từ OpenAPI…

**Dấu hiệu nguồn tài liệu:**

- mã ticket trong tên branch và trong `git log --oneline -50` (ví dụ `ABC-123`)
- link Jira, Confluence hoặc Linear trong README và commit message

**Connector đang dùng được:** kiểm tra tool Jira, Confluence, Linear… có trong phiên hiện tại không. Tool có thể đang ở dạng deferred, nên tìm bằng `ToolSearch` (ví dụ từ khóa "jira", "confluence") trước khi kết luận là không có.

## Bước S2: Hỏi lượt 1 — phạm vi và lệnh

Hỏi trong một lượt (tối đa 4 câu), dựa trên kết quả S1:

1. **Stage** (`multiSelect`): liệt kê các stack đã dò, mỗi stack kèm thư mục. Ví dụ: "`.NET` – `src/Api`", "`Angular` – `src/Portal`".
2. **Range mặc định:** *Thay đổi chưa commit (khuyến nghị)* / *Toàn bộ branch so với `<base>`*. Lấy `<base>` từ `git symbolic-ref refs/remotes/origin/HEAD` nếu có (ví dụ `origin/main`), và lưu dạng ref remote vào `review.base_branch`.
3. **Lệnh build/test:** với mỗi stack, đưa lệnh lấy từ CI làm lựa chọn đầu tiên. Coder sửa lại qua "Other" nếu cần. Nhiều stack thì gộp thành một lựa chọn "Dùng lệnh từ CI cho tất cả" và liệt kê từng lệnh trong phần mô tả.
4. **Chạy test khi review:** *Có, chạy test (khuyến nghị nếu test nhanh)* / *Không, chỉ build*.

## Bước S3: Hỏi lượt 2 — nguồn tài liệu và chính sách

1. **Nguồn tài liệu** (`multiSelect`): chỉ liệt kê những nguồn có dấu hiệu ở S1 hoặc có connector. Ví dụ: *Jira*, *Confluence*, *Tài liệu trong repo (`docs/`)*, *Không dùng*.
2. **Chính sách sửa code:** *Chỉ báo cáo, coder tự sửa* / *Claude sửa sau khi coder chọn mục*.
3. **Lưu báo cáo ra file:** *Không, chỉ trả trong chat (khuyến nghị)* / *Có, lưu vào `reports/code-review/`*.

Với mỗi nguồn được chọn:

1. Thử gọi connector một lần, ví dụ đọc một ticket có mã tìm thấy ở S1. Nếu không được, báo coder biết và vẫn lưu cấu hình.
2. Hỏi thêm thông tin còn thiếu: project key, regex mã ticket, Confluence space. Đưa giá trị đã dò được làm lựa chọn đầu tiên.

## Bước S4: Sinh file rule theo stage

Mỗi stage được chọn có một file `rules/<stage>.md`, theo [../assets/rule.template.md](../assets/rule.template.md). Mỗi rule có ID, trục, mức và nguồn như trong template.

**Nguồn rule**, theo thứ tự ưu tiên:

1. Convention đã được ghi lại: CLAUDE.md, AGENTS.md, CONTRIBUTING.md, ADR, cấu hình linter.
2. Pattern suy ra từ code. Đọc 5–10 file tiêu biểu thuộc nhiều module khác nhau. Ưu tiên file sửa gần đây (`git log --name-only`), vì code mới phản ánh chuẩn hiện tại tốt hơn code cũ.
3. Kiến thức chung về framework và version đang dùng. Chỉ đưa vào những rule thực sự áp dụng cho repo này.

**Không chép lại những gì linter đã bắt.** Rule tập trung vào thứ công cụ không bắt được:

- vòng đời
- kiến trúc
- cách xử lý lỗi
- cách gọi API
- quy ước đặt tên theo domain

**Ghi nguồn cho mỗi rule.** Rule suy từ code phải trỏ tới file làm mẫu.

**Code không thống nhất thì hỏi, đừng tự chọn.** Nếu thấy hai cách làm cùng tồn tại, hỏi coder cách nào là chuẩn. Ví dụ: nửa repo dùng `async` pipe, nửa còn `subscribe` thủ công.

## Bước S5: Sinh `rules/domain.md`

Theo [../assets/domain.template.md](../assets/domain.template.md). Nguồn gồm:

- tên entity và service trong code
- README
- tài liệu đã chọn ở S3

Hỏi coder 1–2 câu (`multiSelect`) về bất biến business quan trọng nhất. Đưa lựa chọn suy từ code, ví dụ: *Số dư không được âm*, *Mỗi đơn chỉ thanh toán một lần*, *Tiền tệ làm tròn 2 chữ số*. Chỉ ghi vào mục "Bất biến business" những gì coder xác nhận. Điền thêm mục "Luồng nhạy cảm" từ các module đụng tới tiền, phân quyền, xóa dữ liệu.

## Bước S6: Duyệt và ghi file

1. Tóm tắt bản nháp trong chat:
   - các thay đổi chính của config
   - số rule theo từng file và theo từng trục
   - các bất biến trong `domain.md`
2. Hỏi: *Ghi file (khuyến nghị)* / *Xem toàn bộ nội dung trước* / *Sửa lại phần…*.
3. Ghi file sau khi coder đồng ý:

   ```
   .claude/review-changes/
   ├── config.yaml
   └── rules/
       ├── <stage>.md
       └── domain.md
   ```

4. Đề xuất coder commit thư mục này để cả team dùng chung.
5. Hỏi có muốn thêm các lệnh trong `stages[].commands` vào allowlist ở `.claude/settings.json` không. Mục đích: lần sau không phải xác nhận quyền mỗi lần build. Chỉ sửa `settings.json` khi coder đồng ý rõ ràng.

## Bước S7: Kiểm tra lại

1. Chạy các bước kiểm tra của Bước 0 trong SKILL.md trên config vừa tạo.
2. Nếu setup được gọi bằng tham số `setup` thì dừng ở đây.
3. Nếu không, hỏi coder có muốn review thay đổi hiện tại luôn không.
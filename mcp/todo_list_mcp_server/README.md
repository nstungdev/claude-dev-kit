# todo-list-mcp-server

MCP server quản lý todo list (add/list/complete/update/delete), lưu dữ liệu vào file JSON local.

## Cách chạy

### 1. Dev mode — `uv run` (khuyên dùng khi đang phát triển)

Luôn chạy trực tiếp từ source, không cần build lại khi sửa code:

```powershell
uv run todo-list-mcp-server
```

Đăng ký với Claude Code (scope project, chạy ở repo root):

```powershell
claude mcp add todo-list -s project -- uv run --directory "P:/nstungdev/repos/claude-dev-kit/mcp/todo_list_mcp_server" todo-list-mcp-server
```

### 2. Đóng gói — `uv tool install` (khi bản đã ổn định)

Build và cài như một CLI tool độc lập, executable `todo-list-mcp-server` được thêm vào PATH:

```powershell
uv tool install --force .
```

Đăng ký với Claude Code (gọn hơn, không cần `--directory`):

```powershell
claude mcp add todo-list -s project -- todo-list-mcp-server
```

Lưu ý: mỗi lần sửa code phải chạy lại `uv tool install --force .` để cập nhật bản đã cài; nếu quên, Claude Code vẫn dùng bản cũ.

Muốn build ra file phân phối (wheel) thay vì cài thẳng:

```powershell
uv build
```

Ra `dist/todo_list_mcp_server-<version>-py3-none-any.whl`, cài bằng `pip install <file>.whl` hoặc `uv pip install <file>.whl`.

## Test bằng MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) là công cụ debug/test server qua web UI, không cần cấu hình vào client thật (Claude Desktop, Claude Code...).

```powershell
uv sync
npx @modelcontextprotocol/inspector uv run todo-list-mcp-server
```

Lệnh trên in ra một URL kiểu `http://localhost:6274?...token...` — mở bằng trình duyệt. Trong tab **Tools**, bạn có thể gọi thử từng tool (`add_todo`, `list_todos`, `complete_todo`, `delete_todo`, `update_todo`) với input tùy ý và xem kết quả trả về ngay, kèm panel xem raw JSON-RPC request/response để debug.

Lưu ý: dữ liệu được lưu trực tiếp vào `src/todo_list_mcp_server/todo.json`, test qua Inspector sẽ ghi đè file này. Backup trước nếu không muốn mất data:

```powershell
cp src/todo_list_mcp_server/todo.json src/todo_list_mcp_server/todo.json.bak
```

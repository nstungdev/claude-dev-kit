# claude-dev-kit

A personal toolkit of Claude Code extensions — spec-driven SDLC skills
and MCP servers, built to make working with Claude Code on real projects
more structured and repeatable.

## What's in this repo

| Resource | Description |
|---|---|
| [`sdlc-dev-kit/`](sdlc-dev-kit/README.md) | Claude Code Skills implementing a spec-driven SDLC workflow — `setup-dev-kit` → `generate-spec` → `generate-plan` → `generate-task` → `implement-task` → `inspect` — with mandatory TDD and an independent review gate before any task counts as done. Packaged as an installable Claude Code plugin. |
| [`mcp/todo_list_mcp_server/`](mcp/todo_list_mcp_server/README.md) | A Python MCP server for managing a local todo list (add/list/complete/update/delete), backed by a local JSON file. README in Vietnamese. |

## Installing the plugins

This repo also doubles as a Claude Code plugin marketplace
(`.claude-plugin/marketplace.json`). Install any plugin listed here with:

```bash
/plugin marketplace add nstungdev/claude-dev-kit
/plugin install sdlc-dev-kit@claude-dev-kit
```

## License

MIT — see [LICENSE](LICENSE).

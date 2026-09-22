# sdlc-dev-kit

A set of **Claude Code Skills** implementing a spec-driven software
development workflow: every code change must originate from a
**spec.md** (single source of truth), flow through a concrete plan and
task, be implemented under **mandatory TDD**, and only be considered
done once an **independent inspect step** confirms it — no shortcut of
"just code it the way it was verbally requested".

## Why this kit exists

Working directly with an AI agent with no process in place easily leads to:

- **Spec drift** — the code does more (or something different) than what
  the original requirement describes, and nobody remembers why that logic
  is there.
- **No evidence** — a task is reported "done" but it's unclear whether
  real tests were actually run, or whether they truly cover the
  Acceptance Criteria.
- **Conflicts when running in parallel** — multiple tasks/agents editing
  the same file without declaring a dependency between them.
- **Repeated or contradictory architecture decisions** — every
  implementation makes its own call, with nobody tracking what was
  decided before or why.

sdlc-dev-kit addresses this by splitting the lifecycle of a change into 5
sequential skills, each doing exactly one job and recording its result to
a file the next skill reads — no skill is allowed to "skip ahead" or
infer the work of another skill.

## Workflow

```
setup-dev-kit (run once)
        │
        ▼
generate-spec → generate-plan → generate-task → implement-task → inspect
        ▲                                                            │
        └──────────────── new/changed requirement ───────────────────┘
```

`implement-task` ↔ `inspect` repeats for each task (Rejected → fix →
inspect again) until every task in `tasks-XXX.md` is `Done`.

## Skills

| Skill | When to use | Main input | Output |
|---|---|---|---|
| [`setup-dev-kit`](skills/setup-dev-kit/SKILL.md) | First time adopting the kit for a project | Scans an existing project, or asks directly for a new one | `CLAUDE.md`, `docs/architecture.md`, the `docs/specs/` folder |
| [`generate-spec`](skills/generate-spec/SKILL.md) | A new requirement, or a change to an existing feature's requirement | A prompt, meeting notes, a document... | `docs/specs/<feature>/spec.md` + `CHANGELOG.md` (plus an empty `architecture.md` if the feature is brand new) |
| [`generate-plan`](skills/generate-plan/SKILL.md) | After spec.md was just updated, need a technical approach | The most recent `CHANGELOG.md` entry without a plan yet | `plans/plan-XXX.md` |
| [`generate-task`](skills/generate-task/SKILL.md) | After a plan exists, need concrete units of work to code | `plan-XXX.md` | `tasks/tasks-XXX.md` |
| [`implement-task`](skills/implement-task/SKILL.md) | Code one specific task | A task at `Backlog` status | Code + passing tests (via TDD) |
| [`inspect`](skills/inspect/SKILL.md) | Review one task that was just coded | The implemented task + the code diff | Task moves to `Done` or `Rejected` (with a reason) |

## Files the kit creates in a project

```
<project-root>/
├── CLAUDE.md                          # short dispatch guide, points to the workflow + hard rules
├── docs/
│   ├── architecture.md                # project-wide tech stack, conventions, build/test commands
│   └── specs/
│       └── <feature-name>/
│           ├── spec.md                # Requirement IDs, the feature's single source of truth
│           ├── architecture.md        # feature-specific Architecture Decisions (AD-01, AD-02...)
│           ├── CHANGELOG.md           # each change to spec.md, numbered [001], [002]...
│           ├── plans/
│           │   └── plan-001.md        # 1 plan = 1 CHANGELOG entry
│           └── tasks/
│               └── tasks-001.md       # T1, T2... matching plan-001.md
```

## Quick start

1. Install `sdlc-dev-kit` for your project (see [Installation](#installation) below).
2. Run `setup-dev-kit` — only once, when first adopting the kit.
3. For each requirement → run `generate-spec` → `generate-plan` →
   `generate-task` → `implement-task` → `inspect` per task, repeating
   `implement-task`/`inspect` until every task in `tasks-XXX.md` is done.
4. New or changed requirement → go back to `generate-spec`.

## Hard rules

- Never code directly without a matching task in `tasks-XXX.md`.
- Never edit `spec.md`/`architecture.md` while coding — if a gap is found,
  stop and run `generate-spec` to update it first.
- A task is only `Done` once `inspect` confirms it — no other skill may
  set this status itself.
- `implement-task` must follow TDD (RED → GREEN → REFACTOR), except for
  config/documentation-only tasks (no code logic).
- `inspect` must re-read the full context from scratch (spec, plan,
  architecture, diff) — never rely on what it just remembers from coding.

## Installation

**Option 1 — copy directly (fast, for personal use):**
Copy the whole `skills/` folder into a project's `.claude/skills/` (scoped
to that project), or into `~/.claude/skills/` (available in every
project). No packaging needed — Claude Code discovers each `SKILL.md`
automatically.

**Option 2 — install as a Claude Code Plugin (recommended for sharing with a team):**

```bash
/plugin marketplace add nstungdev/claude-dev-kit
/plugin install sdlc-dev-kit@claude-dev-kit
```

When installed this way, skills are invoked with the plugin prefix, e.g.
`/sdlc-dev-kit:generate-spec`. See
[code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins.md)
for full plugin packaging details.

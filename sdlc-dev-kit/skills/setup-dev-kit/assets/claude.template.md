# Dev-kit — Quick Guide

This project uses a spec-driven dev-kit. EVERY change (new feature, fix
to an existing one) must go through the sequence below — never code
directly and skip these steps.

## Workflow

generate-spec → generate-plan → generate-task → implement-task → inspect


| Step | When to use | Output |
|---|---|---|
| `generate-spec` | New/changed requirement for a feature | `docs/specs/<feature>/spec.md` + `CHANGELOG.md` |
| `generate-plan` | After spec is updated, need a technical plan | `plans/plan-XXX.md` |
| `generate-task` | After a plan exists, need concrete work items | `tasks/tasks-XXX.md` |
| `implement-task` | Code one specific task (TDD) | Code + passing tests |
| `inspect` | Review one completed task | Task Status: Done/Rejected |

## Reference

- **Project-wide technical conventions** (tech stack, build/test
  commands): `docs/architecture.md` — ALWAYS read this before coding or
  reviewing any task.
- **Spec/plan/tasks per feature:** `docs/specs/<feature>/`

## Hard rules

- Never code directly without a matching task in `tasks-XXX.md`.
- Never edit `spec.md`/`architecture.md` while coding — if a gap is
  found, stop and run `generate-spec` to update it first.
- A task is only `Done` once `inspect` confirms it — never set the
  Status yourself.
---
plan_ref: plan-<XXX>
feature: <feature-name>
created: <YYYY-MM-DD>
---

# Tasks <XXX>: <Short name, matching Plan <XXX>>

<!--
  Every task MUST have:
  - A unique ID within this file (T1, T2, T3...)
  - Depends on: which task must be Done first (write "none" if there is
    no dependency). If two tasks touch the same file/module, they MUST
    have a Depends on relationship between them — no task is allowed to
    "share a file" and still run in parallel.
  - Related Requirement: cite the ID from spec.md so the Inspector can
    cross-check against it
  - Acceptance Criteria: specific, verifiable conditions (not vague)
  - Status: use only one of these 4 predefined values:
      Backlog     — not started yet
      In Progress — the builder is actively working on it
      Done        — accepted by the Inspector
      Rejected    — reviewed and rejected by the Inspector; do NOT edit
                    this task again — create a new task (next number) to
                    fix it, referencing "Depends on: <the rejected task>"
                    or the reason in the new task's description

  Tasks marked Done or Rejected: do NOT delete or edit their content —
  they are evidence of what was built/reviewed, kept for traceability. If
  a bug is found in a Done task later, create a new task to fix it; never
  reopen the old one.
-->

## T1: <Name of this unit of work>

**Depends on:** none

**Related Requirement:** <PREFIX>-0X

**Description:** <The concrete work to do — clear enough that the builder
doesn't have to guess intent>

**Acceptance Criteria:**
- [ ] <Verifiable criterion 1 — e.g. "Test case X passes">
- [ ] <Verifiable criterion 2>

**Status:** Backlog

---

## T2: <Name of this unit of work>

**Depends on:** T1

**Related Requirement:** <PREFIX>-0Y

**Description:** <...>

**Acceptance Criteria:**
- [ ] <...>

**Status:** Backlog
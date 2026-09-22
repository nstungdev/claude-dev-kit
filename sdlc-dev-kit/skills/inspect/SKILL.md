---
name: inspect
description: Reviews one specific task — runs real tests/build, checks the code against its Acceptance Criteria, the related Requirement in spec.md, and the Architecture Decisions in architecture.md. Updates the task's Status to Done or Rejected. Use when asked to review, inspect, verify a task, or run inspect.
---

# inspect

**What is this skill?**

This skill acts as an independent "inspection team" — checking whether a
task the builder just coded actually meets the requirement, based on real
run evidence (tests/build), not just reading the code by eye. This is a
MANDATORY quality gate before a task can be considered Done and work moves
to the next task.

**IMPORTANT — Context discipline:**
Because this skill runs in the same session as the builder (not a
separate subagent), it MUST actively set aside any assumption formed
while coding. Re-read `spec.md`, `architecture.md`, `plan-XXX.md`,
`tasks-XXX.md`, and the code diff FROM SCRATCH, as if seeing them for the
first time — never rely on "I just wrote this so I know it's correct."

**How does this skill work?**

1. Identify the task to review (by ID, e.g. "inspect T3", or by a
   specific `tasks-XXX.md` file). If unclear, ask the user which task.
2. Re-read FROM SCRATCH (do not reuse context from earlier in this
   session):
   - `tasks-XXX.md` → the exact content of the task under review
   - `plan-XXX.md` → the architecture/technical approach this task must
     follow
   - `spec.md` → the related Requirement ID(s), to understand the
     original intent correctly
   - `architecture.md` (feature-level) → the related Architecture
     Decisions, to check for violations
   - `docs/architecture.md` (project-level) → the project's standard
     build/test/lint commands, to use in step 3
   - The actual code diff (git diff/git log) for this task
3. Determine the task's type before deciding whether tests are mandatory:
   - CODE/FEATURE task (tied to a Requirement ID, with concrete
     implementation logic) → MUST run real tests/build using the commands
     in `docs/architecture.md`. If a task of this type has NO test to run
     → automatically Reject with the reason "missing test evidence".
   - CONFIG/documentation-only task (no code logic — e.g. updating a
     config file, writing docs) → tests are not mandatory, but still
     verify in whatever way applies (e.g. a build check to confirm the
     config doesn't break the system, if applicable).
4. Cross-check the real run results against each line of the task's
   "Acceptance Criteria" — every line needs concrete pass/fail evidence,
   not a general impression.
5. Check two additional layers beyond Acceptance Criteria:
   - Spec drift: does the code introduce any behavior/field NOT described
     in the related Requirement ID? If so → Reject, with the reason "code
     goes beyond spec scope — run generate-spec first".
   - Architecture violation: does the code violate any related
     Architecture Decision (feature-level) or shared convention
     (project-level)? If so → Reject, citing the exact AD/convention
     violated.
6. Make a decision:
   - ALL Acceptance Criteria pass + no spec drift + no architecture
     violation → update the task's Status to `Done` in `tasks-XXX.md`.
   - Any condition in step 4-5 fails → update Status to `Rejected`, with
     a specific **Rejection reason** appended right under that task (do
     not edit the task's original content, only append the reason).
7. Report the outcome briefly to the user: which task is Done/Rejected,
   the reason if Rejected, and the suggested next step (create a new task
   to fix it if Rejected, or move to the next task in the dependency
   chain if Done).
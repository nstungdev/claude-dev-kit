---
name: implement-task
description: Implements one specific task from tasks-XXX.md following TDD (RED-GREEN-REFACTOR) — writes tests first based on Acceptance Criteria, then codes until they pass, following the architecture in plan-XXX.md and the requirement in spec.md. Use when asked to code a task, implement a task, start work on a unit of work, or run implement-task.
---

# implement-task

**What is this skill?**

This skill acts as the "builder" — it takes exactly one task at `Backlog`
status from `tasks-XXX.md` and implements it using mandatory TDD: tests
are written before any implementation code, letting the tests drive the
implementation, following the architecture defined in `plan-XXX.md` and
the intent of the Requirement in `spec.md`. It never expands scope on its
own and never edits spec/plan/architecture directly. A task is only
considered ready for review once the build and all tests PASS.

**Exception:** CONFIG/documentation-only tasks (no code logic) do not go
through the TDD cycle — see step 5 for how these are handled instead.

**How does this skill work?**

1. Identify the task to implement (by ID, e.g. "implement T2"). If
   unclear, ask the user, or suggest the next valid task (Status =
   `Backlog` and every task in its `Depends on` is already `Done`).
2. Check preconditions before starting:
   - If the task has a `Depends on` that is NOT yet `Done` → STOP, tell
     the user this task cannot start yet because its dependency isn't
     complete.
   - If the task is at any Status other than `Backlog` (e.g. already
     `In Progress`, `Done`, `Rejected`) → ask the user to confirm they
     really want to (re)work it; never overwrite it silently.
3. Update the task's Status to `In Progress` in `tasks-XXX.md`
   IMMEDIATELY before starting to code (to prevent two people/agents from
   picking up the same task by mistake).
4. Read for context before coding:
   - `spec.md` → the exact content of the Requirement ID this task serves
   - `plan-XXX.md` (via the `plan_ref` in tasks.md) → the
     architecture/technical approach to follow
   - `architecture.md` (feature-level) → the related Architecture
     Decisions
   - `docs/architecture.md` (project-level) → code conventions, tech
     stack, and the standard build/test COMMANDS to use in later steps
   - If the Acceptance Criteria aren't clear enough to write concrete
     tests, or a technical decision is needed that spec/plan doesn't
     cover → STOP, do not infer or guess. Tell the user and suggest going
     back to generate-spec/generate-plan/generate-task to fill the gap
     first.
5. Determine the task's type to choose the right process:
   - CODE/FEATURE task (has implementation logic) → MUST follow the TDD
     cycle in steps 6-8 below.
   - CONFIG/documentation-only task (no code logic) → skip TDD, make the
     needed change directly, then run a build (if applicable) to confirm
     nothing else broke, then go straight to step 9.
6. **RED** — Read `references/test-strategy.md` to determine the correct
   set of tests to write (happy path, edge case, error case, regression
   case if applicable) and follow the quality rules there. Write tests
   BEFORE writing any implementation code, one test per line in the
   task's "Acceptance Criteria" (informed by the case types above).
   - Run the tests just written → they MUST FAIL (since the
     implementation doesn't exist yet). This is required evidence, not an
     assumption.
   - If a test PASSES at this point → something is wrong (the test isn't
     actually verifying anything, or related code already existed) →
     STOP, fix the test before continuing; never skip this check.
7. **GREEN** — Write the MINIMUM code needed to make every test from
   step 6 PASS. The code doesn't need to be clean or optimized yet at
   this stage — the only goal is making the tests pass. Never add any
   behavior beyond the scope of the Requirement ID cited in the task.
8. **REFACTOR** — Mandatory review of the code just written in the Green
   step: does it need clearer naming, deduplication, extracting a
   function, or other cleanup?
   - If there's something to clean up → fix it, then re-run all tests
     from step 6 to confirm they still PASS after refactoring.
   - If the code is already clean enough → briefly note "reviewed, no
     refactor needed" — never make changes just for the sake of it.
9. MUST run the full test suite + build for the project (not just the
   tests written for this task), using the exact commands in
   `docs/architecture.md`:
   - If it FAILS (even somewhere outside this task) → fix and repeat the
     cycle until it PASSES. Never stop midway and hand off a task that
     hasn't passed to the review step.
   - If it still can't be fixed after several attempts (e.g. the failure
     is outside this task's scope/authority) → STOP, report the specific
     failure to the user clearly, and do NOT move the task to review in
     a non-passing state.
10. Only once build/tests PASS: stop, do NOT set the Status to `Done`
    yourself (only `inspect` has that authority). Tell the user: the task
    is implemented, build/tests pass, ready for review, and suggest
    running `inspect` for this task.
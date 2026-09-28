---
name: implement-task
description: Implements every pending task in tasks-XXX.md in a loop — TDD (RED-GREEN-REFACTOR) per task, then automatically runs inspect; on Done it moves straight to the next eligible task without waiting for the user, on Rejected it stops and hands the decision back. Use when asked to code a task, implement a task, implement all tasks, start work on a unit of work, or run implement-task.
---

# implement-task

**What is this skill?**

This skill acts as the "builder" and drives the implement→inspect loop
over `tasks-XXX.md` end to end. For each task at `Backlog` status it
implements it using mandatory TDD — tests are written before any
implementation code, letting the tests drive the implementation,
following the architecture defined in `plan-XXX.md` and the intent of the
Requirement in `spec.md` — and once build/tests PASS it automatically
invokes `inspect` on that exact task in the same run, with no manual
step in between. If `inspect` marks the task `Done`, this skill
immediately moves on to the next eligible `Backlog` task and repeats the
whole cycle, continuing autonomously until there is no eligible task
left. If `inspect` marks a task `Rejected`, the loop STOPS at that task
and hands the decision back to the user (see step 12) — it never expands
scope on its own and never edits spec/plan/architecture directly.

**Exception:** CONFIG/documentation-only tasks (no code logic) do not go
through the TDD cycle — see step 5 for how these are handled instead.

**How does this skill work?**

1. Identify the task to implement:
   - First iteration: use the task ID the user named (e.g. "implement
     T2"). If none was named, or once picking up after a `Done` verdict
     in step 11, pick the next valid task — Status = `Backlog` and every
     task in its `Depends on` is already `Done`.
   - If no eligible task remains anywhere in `tasks-XXX.md` → stop the
     loop here, this is a normal end state (see step 12).
   - If it's genuinely ambiguous which task to start with (e.g. several
     independent Backlog tasks with no dependency between them and the
     user gave no hint), ask the user once, then run the loop for the
     rest without asking again.
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
10. Only once build/tests PASS: do NOT set the Status to `Done` yourself
    (only `inspect` has that authority) and do NOT stop to ask the user.
    Immediately invoke the `inspect` skill for this exact task, in the
    same run, passing it the task ID.
11. Handle `inspect`'s verdict:
    - **Done** → report a brief one-line progress note (e.g. "T2: Done"),
      then go back to step 1 to pick up the next eligible `Backlog` task
      automatically — no confirmation needed. Keep repeating steps 1-11
      until step 1 finds no eligible task left.
    - **Rejected** → STOP the loop right here (do not continue to other
      tasks, even independent ones — a rejection can mean spec drift or
      an architecture violation that needs a human decision, not just a
      code fix). Go to step 12.
12. When the loop stops, report clearly to the user:
    - **All tasks Done** (step 1 found nothing left) → list every task
      completed in this run; this is success, nothing more to do.
    - **Stopped on a Rejected task** → name the task, quote the
      Rejection reason `inspect` appended, list any tasks already marked
      Done earlier in this run, and suggest the next step per the
      `tasks-XXX.md` convention (create a new task, `Depends on:` the
      rejected one, to fix it — never edit the rejected task itself).
      Wait for the user's direction before touching that task further.
    - **Stopped on an earlier hard blocker** (unclear Acceptance
      Criteria, a missing technical decision, or a build/test failure
      that couldn't be fixed after several attempts, per steps 4 and 9)
      → report the specific blocker the same way, and do not silently
      skip the task or move on to others that depend on it.
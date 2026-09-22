---
name: generate-task
description: Breaks down a plan-XXX.md file into a concrete list of implementation tasks (tasks-XXX.md), following the template in assets/tasks.template.md. Use when asked to break down a plan into tasks, create a task list, or run generate-task.
---

# generate-task

**What is this skill?**

This skill turns one `plan-XXX.md` (the architecture/technical approach
for one specific change) into a list of discrete "units of work" (tasks),
each kept at minimal complexity (easy to code, easy to test, easy to
review), with clear Acceptance Criteria for the Inspector to check against
during review. Tasks with no dependency between them can be worked on IN
PARALLEL by multiple builders. Each run of this skill creates EXACTLY ONE
`tasks-XXX.md` file, matching the `plan-XXX.md` with the same number.

**How does this skill work?**

1. Identify the `plan-XXX.md` to break down (if the user doesn't specify
   one, find the most recent plan that doesn't yet have a matching
   `tasks-XXX.md` in the `tasks/` folder).
   - If multiple plans have no tasks yet → ask the user which plan to
     break down.
   - If a `tasks-XXX.md` already exists for that plan → ask the user
     whether to overwrite it; never overwrite on your own.
2. Read `plan-XXX.md`, especially the "Requirement → File/Module Mapping"
   section, to find the natural boundaries between units of work.
3. Break the work into tasks following these principles:
   - Prioritize MINIMAL complexity per task — split as small as makes
     sense, as long as each task remains one complete unit that can be
     coded, tested, and reviewed independently. Never bundle unrelated
     Requirement IDs into one task just to reduce the task count.
   - Determine **Depends on** between tasks based on two kinds of
     constraint:
     a) LOGICAL dependency (this task needs the result of another task
        to be doable)
     b) SHARED FILE/MODULE dependency — if two tasks touch the same
        file/module (per the "Requirement → File/Module Mapping" in
        plan.md), they MUST declare a Depends on relationship between
        them to prevent conflicts when run in parallel, even if they have
        no logical relationship.
   - Every task MUST cite the exact Requirement ID (from spec.md, via
     plan.md) it serves.
4. Write `tasks/tasks-XXX.md` following the structure in
   `assets/tasks.template.md`:
   - Task ID (T1, T2...), Depends on, Related Requirement, Description,
     Acceptance Criteria (specific, verifiable bullets), Status
     (always initialized to `Backlog`).
5. Stop and show `tasks-XXX.md` to the user for confirmation. Clearly
   point out which tasks have NO Depends on relationship with each other
   — these are the ones that can be assigned to multiple builders to work
   on in parallel right away.
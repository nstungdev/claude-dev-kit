---
name: generate-plan
description: Generates a technical plan file (plan-XXX.md) for one specific change recorded in a feature's CHANGELOG.md, based on the current spec.md and architecture.md. Use when asked to create a plan, write a technical plan for a feature/change, or run generate-plan.
---

# generate-plan

**What is this skill?**

This skill turns one specific change in `spec.md` (recorded as an entry in
`CHANGELOG.md`) into a concrete technical plan — describing the
architecture, components, and files that need to be touched to implement
that change. Each run of this skill creates EXACTLY ONE new `plan-XXX.md`
file, following the template in `assets/plan.template.md`, corresponding
to one CHANGELOG entry. Each plan is independent from other plans — it
does not reference or repeat the content of previous plans — but it MUST
follow the foundational architecture decisions already locked in the
feature's `architecture.md`, and it must NEVER introduce a technical
decision that goes beyond what `spec.md` describes.

**How does this skill work?**

1. Read the feature's `CHANGELOG.md` and find the most recent entry that
   does NOT yet have a corresponding `plan-XXX.md` in the `plans/` folder.
   - If multiple entries have no plan yet → ask the user which entry to
     plan for (never pick one on your own when there's more than one).
   - If no entry needs a plan → tell the user and stop.
2. Read the current `spec.md` and identify the exact Requirement ID(s)
   related to the entry being processed (based on the "Change" content of
   that entry).
3. Read the feature's `architecture.md` (already scaffolded by
   generate-spec).
4. Design the architecture for this specific change only, staying strictly
   within the content of the related Requirement ID(s) in spec.md, and
   following every constraint already recorded in architecture.md. Do NOT
   read any previous plan-XXX.md files.
5. Cross-check the technical decision just made against spec.md:
   - If the architecture introduces a decision that goes BEYOND or
     CONFLICTS WITH what the current Requirement ID describes (e.g. it
     requires an extra data field, a behavior, or a constraint spec.md
     never mentioned) → STOP IMMEDIATELY. Do not infer or "just add it" to
     the plan. Tell the user: this technical decision emerged but spec.md
     doesn't describe it — run `generate-spec` first to update the
     relevant Requirement ID (or add a new one), then come back to
     generate-plan.
   - If the architecture fully matches what spec.md already describes →
     continue to step 6.
6. Write `plans/plan-XXX.md` (XXX = the matching CHANGELOG entry ID),
   following the structure in `assets/plan.template.md`:
   - The Requirement ID(s) this plan implements
   - The applicable Architecture Decision(s) from architecture.md
   - The architecture/technical approach (components, services,
     libraries...)
   - A mapping of Requirement ID → file/module expected to be created or
     modified
   - Risks/notes, if any worth flagging
7. If the architecture just designed adds a NEW foundational constraint
   (long-lasting, beyond the scope of this one change) → update
   `architecture.md` at the same time as writing plan-XXX.md.
8. Stop and show `plan-XXX.md` (and `architecture.md` if it was just
   updated) to the user for confirmation before moving on to tasking.
   Suggest running `generate-task` to continue and generate
   `tasks/tasks-XXX.md`.
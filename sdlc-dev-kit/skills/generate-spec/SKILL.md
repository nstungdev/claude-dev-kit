---
name: generate-spec
description: Normalizes any requirement source (user prompt, meeting notes, internal or external docs) into a feature's spec.md following the template in assets/spec.template.md. Use when asked to write a spec, create or update spec.md for a feature, or run generate-spec.
---

# generate-spec

**What is this skill?**

This skill turns ANY requirement source (a user prompt, meeting notes, an
external document, a verbal description written down...) into a `spec.md`
file that follows the standard format in `assets/spec.template.md`. It is
the "intake" step of the whole dev-kit — every requirement must pass through
this step before moving on to planning or tasking, so it gets normalized
into a single source of truth with stable Requirement IDs that is easy to
read and easy to diff against later.

**How does this skill work?**

1. Receive input from the user (a prompt, pasted text, a document link...).
2. Determine whether this is a NEW feature or an UPDATE to a feature that
   already has a spec.md.
   - If a spec.md already exists → read it first before making any change.
3. If the input is incomplete or ambiguous → ask the user for clarification.
   Never guess or infer missing requirements.
4. Write or update spec.md following the structure in
   assets/spec.template.md:
   - New feature → create new Requirement IDs (e.g. AUTH-01)
   - Update an existing requirement → edit directly at that Requirement ID
   - Remove a requirement → delete it entirely from spec.md
5. If this is a COMPLETELY NEW feature (no prior spec.md existed) → also
   create an `architecture.md` file following the scaffold in
   `assets/architecture.template.md`, filling in only the frontmatter
   (feature, last_updated) and leaving the "Architecture Decisions"
   section EMPTY — never invent an architecture decision at this step.
   - If the feature already exists (this is an UPDATE to spec.md) → do
     NOT touch architecture.md, even if it's still empty. Adding or
     editing architecture decisions is generate-plan's job, not
     generate-spec's.
6. After updating spec.md → append one new entry to CHANGELOG.md (who,
   when, why), with a sequential ID (e.g. [001], [002]...) that
   generate-plan will later use to name the matching plan/task files.
7. Stop and show the updated spec.md (and architecture.md if it was just
   created) to the user for confirmation before moving on to planning or
   tasking. Suggest running `generate-plan` to continue to the planning
   step.
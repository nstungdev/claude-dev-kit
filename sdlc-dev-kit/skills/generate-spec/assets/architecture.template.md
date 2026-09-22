---
feature: <feature-name>
last_updated: <YYYY-MM-DD>
---

# Architecture: <Feature Name>

> This file ONLY records architecture decisions specific to this feature.
> Project-wide tech stack and conventions live in `docs/architecture.md`
> — every decision here must stay consistent with that project-level
> reference.

## Architecture Decisions

<Each decision is its own entry with a stable ID for reference. Do NOT
describe implementation detail here — only the decision and the reasoning
behind it. Concrete implementation belongs in plans/plan-XXX.md.>

### AD-01: <Short decision name>

**Decision:** <What was chosen — e.g. "Use JWT for authentication, not
session-based auth">

**Reasoning:** <Why this was chosen over the alternatives>

**Introduced by:** plan-<XXX> (the first plan that made this decision)

**Status:** active

**Constraints for future plans:** <Plain-language description of what
every future plan must follow because of this decision — e.g. "Every
authenticated endpoint must read the JWT from the Authorization header,
never from a session cookie">

### AD-02: <Short decision name — example of a superseded one>

**Decision:** <The original decision>

**Reasoning:** <The original reasoning>

**Introduced by:** plan-<XXX>

**Status:** superseded by AD-05

**Constraints for future plans:** <Keep the original content for
historical reference — no longer in effect, but not deleted>

<!--
  Add a new decision only when a plan introduces a FOUNDATIONAL decision
  (long-lasting, beyond the scope of one specific change), using the next
  sequential ID (AD-01, AD-02...) — never reuse an existing number.

  Do NOT add local implementation detail here — that belongs in the
  plan-XXX.md for that specific change.

  Never delete an outdated decision — change its Status to
  "superseded by AD-XX" and keep its content intact for historical
  reference.
-->
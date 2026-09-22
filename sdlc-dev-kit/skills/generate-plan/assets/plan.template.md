---
plan_id: <XXX>
feature: <feature-name>
changelog_ref: "[<XXX>]"
created: <YYYY-MM-DD>
---

# Plan <XXX>: <Short name describing this change>

## Related Requirements

<List the exact Requirement ID(s) from spec.md that this plan implements.
Do not restate the requirement content — just cite the ID(s); the reader
can look up spec.md for details.>

- <PREFIX>-0X
- <PREFIX>-0Y

## Applicable Architecture Constraints

<List the Architecture Decision(s) (AD) from architecture.md that this
plan must follow. If architecture.md is still empty (new feature,
plan-001) → write "No constraints — this is the feature's first plan".>

- AD-0X: <one-line summary of that constraint>

## Architecture / Implementation Approach

<Describe the concrete technical approach to implement the Requirement
ID(s) above: which component, which service, the processing flow, any
extra library needed. Describe ONLY this specific change — do not repeat
the architecture of other plans.>

## Requirement → File/Module Mapping

| Requirement ID | File/Module | Change Type |
|---|---|---|
| <PREFIX>-0X | `src/...` | Create / Modify |
| <PREFIX>-0Y | `src/...` | Create / Modify |

## Risks / Notes (optional)

<Anything worth flagging during implementation — edge cases, external
dependencies, things the builder should pay special attention to. Can be
left empty if there's nothing to note.>
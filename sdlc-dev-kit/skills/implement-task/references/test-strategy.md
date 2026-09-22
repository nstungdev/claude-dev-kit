# Unit Test Strategy

This file defines the rules for writing tests and how to determine the
set of tests a task needs, applicable across any language/framework.
`implement-task` must read this file before writing tests in the RED step.

## Part 1: How to determine the test set needed

For each line in a task's "Acceptance Criteria", consider the following
case types (not every Acceptance Criteria line needs all 4, but each type
must be deliberately considered before being skipped):

1. **Happy path** — the most basic case: valid input, behavior exactly as
   described. This case is MANDATORY for every Acceptance Criteria line.
2. **Edge case** — boundary values (empty, zero, negative, maximum, a
   single-element list, a very long string...). Derive the boundaries
   from the Requirement's content in spec.md, not from arbitrary guessing.
3. **Error case** — invalid input, behavior under error conditions
   (wrong type, missing required field, violating a business rule). If
   the Requirement mentions a specific error condition (e.g. "lock after
   5 failed attempts") → this case is MANDATORY, never skip it.
4. **Regression case** — if this task modifies or extends existing
   behavior (rather than creating something entirely new), include a
   test confirming the OLD behavior still holds and isn't broken by the
   new change (check the "Constraints for future plans" section in
   architecture.md if relevant).

If a case type (e.g. edge case) clearly doesn't apply to the Acceptance
Criteria at hand, it's fine to skip it — but that must be a deliberate
decision, not an oversight.

## Part 2: Rules for writing quality tests

1. **One test = one clear assertion.** Avoid packing multiple unrelated
   assertions into a single test — when it fails, the test name alone
   should say what went wrong, without needing to read detailed logs.

2. **Test names describe BEHAVIOR, not implementation.** A test should
   read like a statement about the business rule (e.g. "locks the
   account after 5 failed attempts" rather than "calls
   incrementFailCount 5 times").

3. **Clear three-part structure: Arrange – Act – Assert** (a.k.a.
   Given–When–Then). Don't mix data setup logic with result-checking
   logic in the same block.

4. **Tests must be independent, order-agnostic.** Never require test A
   to run before test B for correctness — each test sets up its own
   state rather than relying on state left behind by another test.

5. **Don't test internal implementation details.** Test the behavior
   observable from the outside (input → output, or a business-meaningful
   side effect), not how a private function works internally — this way
   the code can be refactored later without touching the tests, as long
   as external behavior stays the same.

6. **Mocks/stubs are only for external dependencies** (DB, API,
   filesystem, system clock). Don't mock the very logic under test — if
   testing one small unit requires mocking too much, that's a sign the
   code needs to be broken down further, not a sign more mocking is
   needed.

7. **Assertions must be specific, never vague.** Avoid generic checks
   ("no error", "returns something") — assert the exact value/state
   described in the Acceptance Criteria.

8. **Never write a test just to boost coverage.** Every test must verify
   one meaningful behavior from the Acceptance Criteria or a case in Part
   1 — don't write empty or redundant tests just to make the coverage
   number look better.
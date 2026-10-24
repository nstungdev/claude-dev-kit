# engineering-kit

Everyday engineering skills for Claude Code. Unlike `sdlc-dev-kit`, these
skills do not assume any particular workflow — they work on any git repo.

## Skills

| Skill | When to use | Main input | Output |
|---|---|---|---|
| [`review-changes`](skills/review-changes/SKILL.md) | Before committing, merging or opening a PR; or to set up/update review rules for a repo | Uncommitted changes, the current branch, or a git range | A P0/P1/P2 report in chat (optionally saved to a file); on first run, `.claude/review-changes/` with the repo's config and rules |

## review-changes

A code review that checks the change against **what the coder meant to do**
and **this repo's own conventions**, not just generic best practice.

- **First run (`setup`)** scans the repo (stacks, CI build/test commands,
  documented conventions, ticket sources), asks the coder to confirm, and
  writes:

  ```
  .claude/review-changes/
  ├── config.yaml          # stages, build/test commands per stage, sources, fix policy
  └── rules/
      ├── <stage>.md       # rules per stage, with IDs and an "Exceptions" section
      └── domain.md        # glossary, business invariants (INV-NN), sensitive flows
  ```

  Commit this folder so the whole team reviews against the same rules.

- **Each review** reads the linked ticket, asks the coder a few questions
  about intent (scaled to the diff's risk), builds and tests only the
  affected stages in the background, reviews each stage along six axes
  (lifecycle & performance, convention, naming, business gaps, security,
  testing), re-verifies every P0/P1 finding, then reports in chat.

- **After the report** the coder picks which findings to act on, and can
  mark false positives as exceptions in the rule files. With
  `fix_policy: fix_after_consent` Claude applies the chosen fixes — never
  commits.

The skill's prompts and reports are in Vietnamese by default; set
`report.language` in `config.yaml` to change the report language.

## Installation

```bash
/plugin marketplace add nstungdev/claude-dev-kit
/plugin install engineering-kit@claude-dev-kit
```

Then run `/engineering-kit:review-changes setup` once per repo.
Or copy `skills/review-changes/` into a project's `.claude/skills/`
(or `~/.claude/skills/`) and run `/review-changes setup`.

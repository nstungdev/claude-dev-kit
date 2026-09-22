---
last_updated: <YYYY-MM-DD>
---

# Architecture: Project-level

> This file contains GENERAL technical conventions applied across the
> WHOLE project. Each feature may have its own `architecture.md` (at
> docs/specs/<feature>/) containing only decisions SPECIFIC to that
> feature — decisions there must never conflict with this file.

## Tech Stack

- **Language:** <e.g. TypeScript>
- **Main framework:** <e.g. Next.js 14>
- **Database:** <e.g. PostgreSQL, via Prisma ORM>
- **Package manager:** <e.g. pnpm>

## Code Conventions

- **File naming:** <e.g. kebab-case for files, PascalCase for components>
- **Folder structure:** <e.g. feature-based, not layer-based>
- **Required libraries:** <e.g. use zod for validation, not yup>

## Build & Test Commands

<!--
  MUST be fully filled in — never leave blank or write "TBD". This is the
  single source implement-task and inspect use to run real tests/builds.
  If the project has no test framework yet, setup-dev-kit must
  propose/ask the user to pick one and set it up before completing this
  file — this section may never be left empty.
-->

- **Run all tests:** `<e.g. npm test>`
- **Run a single test file:** `<e.g. npm test -- <file>>`
- **Build:** `<e.g. npm run build>`
- **Lint:** `<e.g. npm run lint>`
- **Test coverage (if available):** `<e.g. npm run test:coverage>`
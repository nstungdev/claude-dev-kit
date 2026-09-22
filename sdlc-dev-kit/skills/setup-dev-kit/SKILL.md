---
name: setup-dev-kit
description: Sets up all project-level artifacts for the dev-kit — CLAUDE.md, docs/architecture.md, the docs/specs/ folder structure. Auto-detects a new vs existing project to scan or ask for the right information. Use when asked to set up the dev-kit, bootstrap the dev-kit for a project, or run setup-dev-kit.
---

# setup-dev-kit

**What is this skill?**

This skill bootstraps ALL project-level artifacts the rest of the dev-kit
(generate-spec, generate-plan, generate-task, implement-task, inspect)
depends on: `CLAUDE.md` (a quick dispatch guide for agents/team members),
`docs/architecture.md` (tech stack + standard build/test commands), and
the `docs/specs/` folder structure (where each feature's spec lives).
This skill runs ONLY ONCE when first adopting the dev-kit for a project
(or when a full reset is needed).

**How does this skill work?**

1. Detect the project's current state:
   - Check for a dependency manifest (e.g. package.json, pyproject.toml,
     go.mod...) AND actual code in a src/ folder (or equivalent).
   - If BOTH exist → treat as an EXISTING project, go to step 2a.
   - If NOT → treat as a NEW project, go to step 2b.

2a. **Existing project** — scan to gather information:
   - Read the dependency manifest to identify the language, main
     framework, and key libraries.
   - Look for existing test/lint/build configuration (e.g. scripts in
     package.json, a jest.config file, .eslintrc...) to find the real
     commands.
   - For EACH piece of information found (tech stack, build/test
     commands...), show it to the user and ASK FOR CONFIRMATION before
     writing it into docs/architecture.md — never write it first and ask
     afterward, since inference from scanned code can be wrong.
   - If no clear test command is found despite the project having code
     (e.g. the project has code but no tests were ever written) →
     handle the Build & Test Commands section as in step 2b for a new
     project.

2b. **New project / missing information** — ask the user:
   - Ask in turn: intended language/framework, database (if any),
     package manager.
   - For the Build & Test Commands section: if the user has no test
     framework yet, PROPOSE one suited to the chosen language (e.g. Jest
     for Node.js/TypeScript, Pytest for Python), confirm with the user,
     then guide/perform the basic setup before continuing. The Build &
     Test Commands section must NEVER be left empty in the final file.

3. Create `docs/architecture.md` following the structure in
   `assets/project-architecture.template.md`, filled in with the
   information from step 2a or 2b. Never leave any item in "Build & Test
   Commands" blank.

4. Create `CLAUDE.md` at the project root (if it doesn't already exist),
   following `assets/claude-md.template.md` — a short dispatch guide
   pointing to the workflow, docs/architecture.md, and the hard rules.

5. Create the `docs/specs/` folder structure (empty, just the folder, no
   feature yet) if it doesn't already exist.

6. Stop and show the user everything just created (`docs/architecture.md`,
   `CLAUDE.md`) for confirmation. Suggest the next step: run
   `generate-spec` to start creating a spec for the first feature.
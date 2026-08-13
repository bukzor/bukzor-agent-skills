---
status: in-progress
scope: |
  Knowledge-base style directories named `<name>.d/` whose intended
  semantic is the kb pattern (collection of related entries). Renamed
  to `<name>.kb/`. Does NOT cover `.d/` directories with different
  conventions (e.g. /etc-style config.d, build-system.d, claude-args.d)
  — those stay `.d/` by design.
originating-commits:
  - 17c768a    # bukzor-agent-skills, 2025-12-23: Rename todo.d → todo.kb, ideas.d → ideas.kb across skills
  - 62288bd    # bukzor-agent-skills, 2026-02-09: Continue .d → .kb rename
  - 2bdfb3f    # bukzor-agent-skills, 2026-01-02: Add todo: complete .d → .kb rename
  - 799eb02    # bukzor-agent-skills, 2026-05-15: complete .d -> .kb rename across complete-example and devlog
  - d59458b    # bukzor-agent-skills, 2026-05-15: mark complete-example renames done in d->kb todo
why: |
  When the kb pattern was first defined the convention used `.d/`
  (mirroring /etc/X.d/ for "collection of pieces"). Two problems
  emerged:

  1. The `.d/` suffix collided with non-kb conventions in the same
     tree (config.d/, build-system.d/, claude-args.d/), making
     identification of kb-class directories require knowledge of
     intent, not just inspection.
  2. The kb pattern grew distinctive enough to warrant its own
     suffix; `.kb/` is the visible marker.

  Multiple sweeps landed across 2025-12 → 2026-05. The work is
  substantially done for skill knowledge-base directories. The open
  residual is "which other `.d/` directories should also be `.kb/`?"
  — tracked at:

    ~/.claude/todo.kb/2026-05-15-000-rename-outmoded-d-dirs-to-kb-case-by-case-eval.md
---

# Rename knowledge-base .d/ directories to .kb/

## What's done

- All `todo.d/` → `todo.kb/` in skill directories.
- All `ideas.d/` → `ideas.kb/` in skill directories.
- Renames across `llm-kb/complete-example/` (food.d → food.kb, etc.).
- Renames across `bukzor-agent-skills/*/docs/dev/devlog/` (each devlog
  entry's sub-`.d/` → `.kb/`).
- llm-kb skill name itself: `llm.kb` → `llm-kb` (Agent Skills spec
  compliance; separate commit 71b6fca).

## What's NOT in scope

By design, these `.d/` directories stay as-is — they encode different
conventions:

- `*/config.d/` — /etc-style configuration drop-in directory
- `*/build-system.d/` (and `claude-args.d/`, etc.) — build-system
  template variants
- `*/template.python-project/*.d/` — template fragments
- `*/basics.d/` — third-party scoped notes

## What's open (case-by-case)

The residual lives in
`~/.claude/todo.kb/2026-05-15-000-rename-outmoded-d-dirs-to-kb-case-by-case-eval.md`.
Each remaining `.d/` directory needs a judgment call: kb-pattern or
not? Convert or leave?

## Algorithm

`validate.sh` lists all current `*.d/` directories with their
neighbor count (sibling files) and a quick judgment hint based on
parent context. Output format:

    <kb-or-not-hint>  <path>  <entry-count>

Heuristic:

- `kb-like`: parent contains other `.kb/` siblings, or filenames
  inside follow the `YYYY-MM-DD-NNN-*.md` shape.
- `config-like`: contains `.conf` / `.cfg` / non-markdown content.
- `template-like`: path includes `template`, `skeleton`, `copier`.
- `unknown`: doesn't match the above.

No `migrate.sh`. Conversion of any individual `.d/` requires the
case-by-case judgment from the open todo above; auto-conversion would
mis-rename the legitimate `.d/` cases.

## Idempotency

Read-only validator; trivially idempotent. Once an individual `.d`
is renamed manually via `git mv`, it disappears from the validator's
output.

## Why "applying" not "applied"

The intended-kb residual exists and is non-trivial; case-by-case
evaluation is unstarted (per the open todo).

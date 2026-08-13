---
status: verified
verified-by: |
  2026-05-26 drift check: `find ~/repo ~/.claude ~/claude -name 'CLAUDE.d' -type d`
  returns zero results. The old mechanism is gone from the skill skeleton and
  Phase-2 agent logic; no consumer projects retain the legacy form.
scope: |
  Multi-agent handoff mechanism: projects that depended on
  `CLAUDE.d/<skill>.md` discovery-via-bash-execution were migrated to
  declare dependencies via `requires:` in the project's `CLAUDE.md`
  YAML frontmatter.
originating-commits:
  - 5f316c6     # bukzor-agent-skills, 2025-12-18: Fix multi-agent handoff: use requires frontmatter over CLAUDE.d/
why: |
  Phase-2 agents weren't reliably executing the bash command to
  discover `CLAUDE.d/<skill>.md` skill-dependency declarations. The
  failure mode was silent: missing dependency, downstream errors hard
  to attribute.

  Switching to a frontmatter-declared `requires:` list moved the
  signal into a location Phase-2 sees immediately without needing
  command execution. The agent-handoff mechanism became deterministic.

  The old `CLAUDE.d/` mechanism was removed entirely; there's no drift
  path back to it.
---

# CLAUDE.d/ → requires frontmatter for multi-agent skill handoff

## Before / after

```
# Before: discovery via bash + CLAUDE.d/
project/
  CLAUDE.md
  CLAUDE.d/
    llm-kb.md        # auto-loaded by Phase 2 via shell

# After: declared in frontmatter
project/
  CLAUDE.md          # frontmatter: requires: [Skill(llm-kb)]
```

Phase-2 agents read the frontmatter directly without shelling out;
the dependency is visible at parse time.

## What landed in 5f316c6

- Test `CLAUDE.md` removed (Phase 1 creates it with proper frontmatter)
- Devlog documenting the investigation and resolution
- Test variants and infrastructure from earlier experiments

The old `CLAUDE.d/` mechanism is gone from the skill skeleton; new
projects use only the frontmatter form. Existing projects predating
2025-12-18 would carry the old form only if they were never updated
since; in practice the skill consumers were caught up in the same
period.

## Self-maintaining

Because the old mechanism no longer exists in the skill skeleton or
the agent's Phase-2 logic, drift back to the old form requires
deliberate manual recreation of `CLAUDE.d/`. Effectively impossible
by accident.

## Algorithm (informational)

No validator/migrate scripts. A drift-check would `find ~/repo -name
'CLAUDE.d' -type d` and report any matches; given the mechanism is
gone, matches would be relics rather than active failures.

## Why "complete" not "verified"

No audit of all consumer projects performed. Upgrade to `verified` if
a `find` sweep returns zero `CLAUDE.d/` directories outside historical
contexts.

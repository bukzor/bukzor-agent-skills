---
status: complete
kind: one-shot
scope: |
  Any skill that ships a full schema inside `skeleton/`. The canonical
  moves to a `jsonschema/` directory at the *skill root*; the skeleton
  ships the stub, so projects initialized from it are live-linked from
  day one.

  Live case: `incident-forensics` -- six schemas, byte-identical across
  three sites. Precedent, already applied: `llm-subtask` did exactly this
  on 2026-07-07 as part of that day's migration.

  Not in scope: skeleton files that are meant to be edited after copying
  (templates, README stubs). Only schemas.
depends-on:
  - 2026-07-07-000-schema-copies-to-ref-stubs.md
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-08-21-000-ref-rollout-beyond-todo-ideas.md
why: |
  Skeleton contents get *copied* into new projects, so a full schema in a
  skeleton mints a fresh drifting snapshot on every init -- the copy
  pattern reinstalls itself faster than any sweep removes it. This is
  already written down as house rule in `references/schema-reuse.md`
  ("canonical schemas live in a `jsonschema/` directory at the skill root,
  never inside a `skeleton/`"); the rule shipped without the sweep that
  makes existing skills conform.

  Separate entry from 2026-08-21-000 because it is a different
  transformation: that one rewrites copies into stubs against an existing
  canonical, this one *relocates* the canonical and repoints its
  dependents. Bundling them would make one script with two modes and one
  scope that cannot be stated in a sentence.
---

# Canonical schemas out of skeleton/

## Transformation

Per offending skill:

1. `git mv skeleton/**/<name>.jsonschema.yaml jsonschema/<name>.jsonschema.yaml`
   (flatten: skill-root `jsonschema/` is not nested by skeleton layout).
2. Replace each skeleton file with the stub
   `$ref: "skill://<skill>/jsonschema/<name>.jsonschema.yaml"`.
3. Repoint existing stubs elsewhere that named the old skeleton path --
   these show up as `STALE-REF` under 2026-08-21-000's classifier.
4. Stub the already-copied sites (for incident-forensics, the two
   non-skeleton copies).
5. `llm.kb-validate` the affected trees.

Idempotent by inspection: step 1 is a no-op once `jsonschema/` holds the
file, steps 2-4 rewrite to a fixed target.

## Applied so far

- 2026-07-07: `llm-subtask` (retroactive -- done under that day's entry,
  before this rule was stated separately).
- 2026-08-21: `incident-forensics` -- six schemas (`evidence`, `findings`,
  `remediations`, `reports`, `root-cause`, `timeline`) `git mv`ed from
  `skeleton/` to the new `incident-forensics/jsonschema/`; skeleton now
  holds one-line stubs. Verified byte-identical across all three live
  copy sites before touching anything: the skeleton itself, and two
  external non-repo projects that had been initialized from it --
  `~/claude/mitmproxy/proxy-memory-leak-2026-08-18/` (all six at its
  root) and `~/claude/crostini-health/` (five under
  `incidents.kb/2026-08-08-000-vm-freeze.kb/`, `remediations` at the
  project root). Both external sites stubbed the same way. No stale
  `skill://incident-forensics/skeleton/...` refs found anywhere. No
  `#base` extenders needed -- no diverged copies found. Evidence rests
  on the two external trees: `llm.kb-validate` clean on both
  (`~/claude/mitmproxy/proxy-memory-leak-2026-08-18/`: 37 files, 0
  errors; `~/claude/crostini-health/`: 66 files, 0 errors) -- these are
  the only trees with bound instances of the six schemas. The
  in-repo `llm.kb-validate incident-forensics` (0 files, 0 errors) is
  vacuous: the skill ships no bound instances of its own schemas
  in-repo, so that run confirms the stub files parse, not that any
  instance conforms.

---
managed-by: Skill(llm-subtask)
status: open
---

# Modeline sweep: draft-07 first lines over 2020-12 schemas

**Priority:** Low — cosmetic to the validator, misleading to the editor.
**Complexity:** Small, given the surviving classification.
**Context:** 2026-08-22 schema survey. Noted as a loose end by migration
`llm-kb/migrations.kb/2026-08-21-003-schema-symlinks-to-ref-stubs.md`:
"The house stub keeps a `# yaml-language-server: ...draft-07...` first
line... It is stale on every one of them: the referenced canonicals are
2020-12."

## Problem Statement

`# yaml-language-server: $schema=...draft-07...` first lines sit on files
whose actual dialect is 2020-12. The line is editor tooling only —
`llm.kb-validate` ignores it — so the cost is a language server checking
the wrong dialect, silently.

## Current Situation

The classification survived the incident: `trash/modeline-sweep/`.

- `class.json` — **229 files genuinely 2020-12, 34 genuinely draft-07,
  0 unclassifiable.** Classified by the file's own `$schema:` key and by
  what its `$ref` targets declare, not by the modeline.
- `cand.list` — the 263 draft-07-modeline files, after excluding the
  replication-run clone and the vendored litellm tree.
- `classify.py` — the classifier.

The 34 genuine draft-07 files must keep their modeline. Only the 229 flip.

## Proposed Solution

Rewrite the first line of the 229 to the 2020-12 URL. Nothing else in the
file changes; never touch a `$schema:` key.

## Implementation Steps

- [ ] Re-run `classify.py` — the corpus moved under it (reverts, erased
      history, new hand-written schemas), so the counts want refreshing
      before anything is written
- [ ] Flip the modeline on the confirmed 2020-12 set
- [ ] `llm.kb-validate` per tree — must be a no-op, the validator does
      not read the modeline
- [ ] Fold the result into migration `2026-08-21-003`, which predicted
      this sweep

## Open Questions

- Should the house `$ref` stub template stop carrying a modeline at all?
  A stub's dialect is whatever its target declares, so the stub asserting
  one is a second source of truth that can only ever go stale — which is
  precisely how this got here.

## Success Criteria

- [ ] No `*.jsonschema.yaml` declares a modeline dialect its own
      `$schema:` (or its `$ref` target's) contradicts

## Notes

**Do not delegate this the way the schema work was delegated.** The
sub-agent that destroyed the canonicals also blanket-flipped 215
modelines, 8 of them onto files whose own `$schema:` said draft-07 —
deleting that key in the same write, so the evidence of the mistake went
with it.

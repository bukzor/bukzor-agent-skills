# After Editing a Design Record

> [!DRAFT] agent-authored 2026-11-25, vetoable

You just added, changed, moved, or removed design claims. A design record is a
claims.kb, so `Skill(llm-claims-kb)`'s [after-edit] passes are due first. Then
pass over what you touched:

- a claim's body changed, or a claim moved between rungs -- [each-rung].
- a requirement or architecture claim touched, title included --
  [state-properties].
- a claim corrected -- [regression-proof].

The full sweep waits for the commit: `../before/committing-design-claims.md`.

[after-edit]: ../../../../llm-claims-kb/skill.kb/must-read.kb/after/editing-a-claims-kb.md
[each-rung]: ../../quality-passes.kb/each-rung-says-only-what-its-question-asks.md
[state-properties]: ../../quality-passes.kb/state-properties-not-mechanisms.md
[regression-proof]: ../../quality-passes.kb/regression-proof-with-principles-not-narrative.md

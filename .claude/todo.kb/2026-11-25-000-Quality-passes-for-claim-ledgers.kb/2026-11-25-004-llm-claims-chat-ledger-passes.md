---
managed-by: Skill(llm-subtask)
status: open
blocked-by:
  - 2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md
required-reading:
  - CLAUDE.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-passes-run-at-occasions.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/each-skill-keeps-passes-occasions-and-a-sweep.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-pass-occasions-form-a-ladder.md
  - ../../../llm-claims/SKILL.md
  - ../../../llm-claims/skill.kb/
  - ../../../llm-claims-kb/skill.kb/quality-passes.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/
  - 2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md
---

# `llm-claims`: quality passes for chat ledgers

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (wave
4)

## Problem Statement

`LAYOUT` asks every skill for its passes in `skill.kb/quality-passes.kb/`,
their occasions in `skill.kb/must-read.kb/`, and a sweep. `llm-claims` is the
chat-ledger notation. Its bank already holds while-writing lenses
(`before/writing-a-claim.md` and its siblings), and it has no passes
collection. A chat ledger has no commit, so the ladder's rungs fall
differently here. Settle where:

- Which of the ladder's occasions a chat ledger meets: while writing, after an
  edit, before presenting claims to the user (`before/presenting-claims-to-the-user.md`
  already exists), at a session's end (`when/the-context-or-session-is-ending.md`).
- Which passes run there. Many of `llm-claims-kb`'s passes judge the notation,
  not the files (standing honesty, ruling fidelity, corollaries), so a chat
  ledger needs them too. Don't move or copy them. Cite them from this skill's
  bank, and propose in Open Questions any that should move down to
  `llm-claims` with `llm-claims-kb` citing them instead.
- Whether `llm-claims` needs a `quality-passes.kb/` of its own at all: only if
  a pass exists that is chat-specific and no other skill holds. Subtract
  before adding; an empty collection made for symmetry is accretion.
- The sweep: where a chat ledger has one (before presenting is the likely
  occasion), as `skill.kb/procedures.kb/run-quality-passes.md`, or a reason
  in Decisions why it has none.

**Scope (only these files):** `llm-claims/SKILL.md`, `llm-claims/skill.kb/**`.
Not `llm-claims-kb/**`.

## Steps

## Decisions

## Open Questions

## Final report

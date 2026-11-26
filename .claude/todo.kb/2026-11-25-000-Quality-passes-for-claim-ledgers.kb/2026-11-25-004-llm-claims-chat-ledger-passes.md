---
managed-by: Skill(llm-subtask)
status: done
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

- [x] map the ladder's rungs and `llm-claims-kb`'s passes onto the chat bank
- [x] bank edits: cite the notation passes at their occasions
- [x] `skill.kb/CLAUDE.md`: why no `quality-passes.kb/` or sweep here
- [x] validate, commit

## Decisions

- Rungs a chat ledger meets: while writing (`before/writing-a-claim`,
  `-an-arrow`, `signing-a-claim`, as they were); after an edit folds into
  the next render (`before/showing-revisions-to-a-ledger`, and
  `after/retracting-a-claim` for propagation); before presenting stands
  where a commit would; session end is flush. Periodic and `stale-when:`
  have no chat occasion: smoothing needs the file form, and flush puts
  claims there.
- One citation added: `before/signing-a-claim.md` links `llm-claims-kb`'s
  ruling-fidelity, because a `!` is where the agent writes the user's
  ruling down. Standing honesty has no new citation: the presenting
  entry already states its chat form, and a pointer would tell the chat
  reader nothing more. Corollaries' premise half is
  `before/writing-an-arrow`; its occasion half concerns records on file.
  Confinement is already summarized in `SKILL.md` under Theories.
- No `quality-passes.kb/`: every chat-only quality is a lens with one
  occasion, already in that occasion's entry. Splitting one into a pass
  plus a pointer adds a file per lens and gets no reuse from it.
- No sweep: a sweep tiers scans, and a chat ledger has no scans to run.
  The presenting entry does the sweep's job. Both reasons are recorded,
  marked `[!DRAFT]`, in `llm-claims/skill.kb/CLAUDE.md`, so a later
  `LAYOUT` pass doesn't add a collection just for symmetry.
- `SKILL.md` unchanged: its `IMPERATIVE` block already installs the bank,
  and the core block is shared verbatim with claude.ai.

## Open Questions

- [ ] Move `confinement.md` down to `llm-claims`, with `llm-claims-kb`
      citing it: it is pure notation, and `SKILL.md`'s Theories bullet
      already condenses its five dispositions, so the rule has two homes.
- [ ] Move `ruling-fidelity.md` down too, worded without file terms
      (`authority:` and `agent` become a restated ruling and `+`): its
      quality is notation-level, and the chat bank now cites it across
      the skill boundary.
- [ ] `standing-honesty.md`: keep its frontmatter greps in `llm-claims-kb`,
      and cite `llm-claims`'s `before/presenting-claims-to-the-user.md` and
      `signing-a-claim.md` for the `agent`-is-a-resting-state rule, which
      both skills now state.
- [ ] Out of scope, already broken before this unit: `llm.kb-validate-links
      llm-claims` reports 6 files under `llm-claims/claims.kb/` whose
      `../../skill.kb/` links stop one level short of `llm-claims/skill.kb/`.

## Final report

`llm.kb-validate llm-claims`: 112 files, 0 errors. `llm.kb-validate-links
llm-claims`: 6 broken, all already there and in `claims.kb/` (see Open
Questions); 0 in the files this unit touched. The only change from the
brief is that no collection and no sweep were added. Decisions gives the
reasons, and the brief allowed both.

- Ruling-fidelity at signing: `llm-claims/skill.kb/must-read.kb/before/signing-a-claim.md`
- Why no passes collection or sweep: `llm-claims/skill.kb/CLAUDE.md`

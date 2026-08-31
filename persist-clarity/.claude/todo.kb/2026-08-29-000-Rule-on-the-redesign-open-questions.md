---
managed-by: Skill(llm-subtask)
status: done
closeout: |
  Ruled 2026-08-31 (session b00bf5bc). Accepted subset folded into
  ../../SKILL.md, ../../skill.kb/persistence.md, and ADR
  2026-08-29-000; the owner's words quoted per item below.
---

# Rule on the redesign open questions

**Priority:** next sitting — owner, 2026-08-29: "I want to return to
your open items tomorrow"
**Complexity:** rulings only; minutes of edits after
**Context:** ADR
`../../../docs/dev/adr/2026-08-29-000-Clarity-is-encoded-as-a-ledger--reviewed--then-persisted.md`

## Problem Statement

The 2026-08-29 redesign (encode → review → persist) was steelmanned
in review. Swept 2026-08-31 by `/review-open-questions` — one item
settled by check, one joined from
`./2026-08-30-000-A-run-skipped-encode-and-lost-what-review-generated.md`
— and ruled the same day.

## Owner's Call

- [x] ONTOLOGY? — settled by check, 2026-08-31, under standing veto:
      `Skill(llm-claims)` already routes a coined distinction to a
      theory's ontology ("a claim belongs to the outermost theory
      that coins every coined word its text needs"), so the encode
      beat saying so would restate a peer's law — the same
      duplication the ADR declines for review's presentation rules.
      No text lands.
- [x] MANDATE (was ENCOURAGE?) — accepted 2026-08-31: "ah yes, the
      in-chat ledger mandatory, yes." The encode beat now states the
      render's true cost: a message, not a file.
- [x] CLOSE — rejected 2026-08-31: "this sounds wrong to me. the
      operation can end at chat-ledger. The *review step* ends at
      user satisfaction. Post review step, a disk-ledger is optional,
      recommended, but user-decided." The staged last-claim closing
      rule was reverted; review and persist rewritten to the ruling.
- [x] HOMES (was Strategies framing) — ruled by criteria 2026-08-31:
      "this should be decided by documentation best practice, token
      efficiency, llm alignment principles." All three entail the
      unnamed form — concrete per-ecosystem instructions over a
      second vocabulary with no selector — so "Homes, by ecosystem"
      stands; strategy names become filenames if the tripwire ever
      promotes the file to a collection.

## Success Criteria

- [x] Each item ruled, the accepted subset edited into `../../SKILL.md`
      and `../../skill.kb/persistence.md`, rulings quoted with the edits

## Notes

Tripwire, no ruling needed: promote `skill.kb/persistence.md` to a
strategies collection when the single file outgrows itself.

Re-entry: the ADR above, then the steelman ledger in session
`b00bf5bc-214b-4952-9282-02677d77709f` (project
`-home-bukzor-claude-meta-reasoning`).

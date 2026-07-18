---
why:
  - ../030-requirements.kb/writes-name-their-read-back.md
  - ../040-design.kb/kb-spec.md
---

# Decisions Are Settled Questions

A decision is not an event to log but a question that reached an
answer, open and settled being two lifecycle stages of the spec's
synthesis-file element (`kb-spec.md`). No class-record sub-type
shadows this: `class-record.md` lists session log, incident, and
migration, and decisions are deliberately absent from it.

Event history is version control's job: "when did we decide" is the
node's git log. Where provenance must be model-visible or
multi-party, it attaches to the node rather than replacing it —
e.g. `reviewed:` frontmatter (supports ratification and fused
re-review) or a per-reviewer reviews sub-kb (existence proofs, not
prescriptions; adopt only where value beats the carry cost).

Concurrent settlement conflicting at merge is a feature: two sessions
answering the same question collide loudly at the file grain —
semantic contention surfaced where it happened, instead of coexisting
as dated records a later reader must notice and temporally resolve.

Replaces v1's dated decision logs (ADR): the read-back moment — the
next time the question arises — is exactly where a topical node is
found and a dated pile is not.

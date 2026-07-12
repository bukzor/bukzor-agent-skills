---
why:
  - writes-name-their-read-back
  - kb-spec
---

# Decisions Are Settled Questions

A decision is not an event to log but a question that reached an
answer. Open and settled are two lifecycle stages of one shape — the
spec's synthesis primitive: while open, `$question.md` states the
question and `$question.kb/` holds candidate resolutions
(sub-questions recurse the same shape); once settled, the `.md`
carries the answer on the hot path and the collection keeps the
alternatives-considered story off it. Nothing moves house at
settlement; the synthesis is rewritten, the elaboration persists.

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

Supersedes the decision sub-type of `genre-record.md` (v1 ADR): its
read-back moment — the next time the question arises — is exactly
where a topical node is found and a dated pile is not.

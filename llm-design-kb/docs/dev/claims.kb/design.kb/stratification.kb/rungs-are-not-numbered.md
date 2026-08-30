---
label: NUMS
standing: user
why:
  - priors-are-a-dag-not-a-ladder.md
---

# Rungs Are Not Numbered

Rung collections are named, never prefixed: `requirements.kb/`, not
`030-requirements.kb/`.

Order is recorded once, in the `why:` arrows, and a digit in the
filename is a second copy of it. The copy drifts in the expensive
direction: inserting a rung between `020` and `030` renames a
directory that every `why:` in the record points into, which is the
same rename-cascade objection that defeated a `-TODO` label suffix in
`skill://llm-claims/claims.kb/design.claims.kb/notation.kb/how-decided-but-unbuilt-intent-is-marked.md`.

What the digits bought was reading order from `ls`. The route for that
is `llm-claims-kb-graph`, which topologically sorts the arrows and
cannot disagree with them; at six rungs the order is also cheap to
read off the `why:` lines directly.

Superseded DIGITS, which had argued the opposite in this session --
that a rung is stable enough that its number never rots, and `ls` is
how a record is discovered. It fell to the reframing that made rungs
ordinary theories: no other theory in any ledger in the fleet is
numbered, so numbering these would make the design record a dialect
of the notation rather than an instance of it.

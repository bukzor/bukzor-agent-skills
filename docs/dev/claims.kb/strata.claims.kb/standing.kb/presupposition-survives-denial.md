---
label: DENIAL
standing: agent
why:
  - live-and-upheld-are-judged-separately.md
  - presupposition-is-a-well-founded-edge-relation.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py tests/test_derived_theorems.py tests/test_declined_readings.py -k "absorbs or polarities or morgan"
---

# Presupposition Survives Denial

`q` is a presupposition of `p` when asserting `p` and denying `p`
take `q` for granted alike. That invariance is the test, and it is
what separates a presupposition from an attack: an attack bears on
what `p` says, so it changes sign with `p`, while a presupposition
bears on there being anything for `p` to say, so it does not.

The test has two faces, and only one of them is mechanized:

- computationally, it is why a collapsed claim absorbs verdicts of
  *either* polarity. Acceptance and rejection of `p` are dropped
  together, because both presupposed the thing that failed. A rule
  that dropped only one polarity would be reading the attack
  relation, not this one.
- as a filing criterion it is an argument, not a computation.
  Whether an edge belongs in the presupposition relation is settled
  by trying the denial, and the fixpoint reads only the verdict that
  trying produced -- never the reasoning that produced it.

This is also why presupposition cannot be folded into the attack
relation, however the edges are drawn. An attack that fires when `q`
fails makes `p` false -- defeated on the merits -- and the whole
point of the second relation is that `p` was never on the merits at
all. The two relations are distinguishable exactly because their
values are, so any encoding of one as the other has to spend the
distinction to buy the edge.

The declined alternative is to admit only the attack relation and
recover collapse by convention -- read `false` as "defeated or
collapsed, see the prose". It saves an edge set and costs every
downstream reader the one question they came to ask.

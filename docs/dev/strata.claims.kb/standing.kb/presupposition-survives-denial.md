---
label: DENIAL
standing: agent
why:
  - sense-and-content-are-judged-separately.md
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

- computationally, it is why a moot claim absorbs content-acts of
  *either* polarity. Acceptance and rejection of `p` are dropped
  together, because both presupposed the thing that failed. A rule
  that dropped only one polarity would be reading the attack
  relation, not this one.
- as a filing criterion it is discipline, unmechanized like
  confinement. Whether an edge belongs in the presupposition
  relation is settled by trying the denial in prose, and nothing
  checks that the answer was honest.

This is also why presupposition cannot be folded into the attack
relation, however the edges are drawn. An attack that fires when `q`
fails takes `p` to `out` -- defeated on the merits -- and the whole
point of the second relation is that `p` was never on the merits at
all. The two relations are distinguishable exactly because their
values are, so any encoding of one as the other has to spend the
distinction to buy the edge.

The declined alternative is to admit only the attack relation and
recover mootness by convention -- read `out` as "defeated or moot,
see the prose". It saves an edge set and costs every downstream
reader the one question they came to ask.

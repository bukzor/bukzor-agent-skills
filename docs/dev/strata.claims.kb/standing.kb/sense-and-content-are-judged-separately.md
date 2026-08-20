---
label: SENSE
standing: agent
why:
  - defeat-is-evidence-for-an-approximator.md
  - presupposition-is-a-well-founded-edge-relation.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py tests/test_declined_readings.py -k "disputed_presupposition or collapse_climbs or no_content or never_also or truth_functional"
---

# Sense and Content Are Judged Separately

A claim answers two questions, not one -- has it a sense at all, and
is what it says upheld -- and each is answered on the same interval:
`in`, `contested`, `out`. Standing is that pair. Neither coordinate
bounds the other, so a claim whose presupposition is in dispute can
still be settled on its own terms, and both facts are recorded at
once instead of one displacing the other.

Three commitments make that computable:

- sense is read from the same acts as content, by the same defeat
  rule. Sense is `out` where a presupposition is surely defeated,
  `contested` where one is merely disputed, `in` otherwise: two seeds
  into one collapse, not a second rule.
- collapse propagates. Each bound is the least fixpoint of
  "presupposes something defeated, or something already collapsed",
  so it climbs a presupposition chain without a rule about chains.
- where sense is `out` there is no content at all. The claim is
  *moot*: its truth question does not arise, so the second coordinate
  is absent rather than valued. Mootness is a gap in what standing is
  defined on, never a fourth point ranked against the other three.

The declined alternative folds the presupposition into the content,
so that a claim with nothing to talk about comes out plainly `out`.
It costs the distinction the whole apparatus exists for: a claim
beaten on the evidence and a claim that never reached evidence would
carry one word, and no reader could tell them apart. Keeping them
apart is also what makes the exclusion structural -- no value of the
pair is both moot and defeated, so nothing needs a precedence rule to
say which wins.

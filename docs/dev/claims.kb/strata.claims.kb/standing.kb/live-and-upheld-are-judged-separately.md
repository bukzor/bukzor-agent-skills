---
label: SPLIT
standing: agent
why:
  - defeat-is-evidence-for-an-approximator.md
  - presupposition-is-a-well-founded-edge-relation.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py tests/test_declined_readings.py -k "disputed_presupposition or collapse_climbs or no_truth_question or never_also or truth_functional"
---

# Live and Upheld Are Judged Separately

A claim answers to two propositions, not one: it is *live* -- there is
a subject for it to be about -- and what it says is *upheld*. The
record answers each with true, false, or unknown, and standing is that
pair. Neither coordinate bounds the other, so a claim whose
presupposition is in dispute can still be settled on its own terms,
and both facts are recorded at once instead of one displacing the
other.

Three commitments make that computable:

- liveness is read from the same acts as merit, by the same defeat
  rule. A claim is not live where a presupposition is surely defeated,
  unknown where one is merely disputed, live otherwise: two seeds into
  one collapse, not a second rule.
- collapse propagates. Each bound is the least fixpoint of
  "presupposes something defeated, or something already collapsed", so
  it climbs a presupposition chain without a rule about chains.
- a claim that is not live has no truth question. `upheld` reads
  unknown there, and the reading is a gap in what standing is defined
  on rather than a fourth point ranked against the other three. The
  two situations `unknown` covers -- a dispute the record does not
  settle, and a question that does not arise -- are told apart by the
  other coordinate, never by `upheld` alone.

The declined alternative folds the presupposition into the merits, so
that a claim with nothing to talk about comes out plainly false. It
costs the distinction the whole apparatus exists for: a claim beaten
on the evidence and a claim that never reached evidence would carry
one word, and no reader could tell them apart. Keeping them apart is
also what makes the exclusion structural -- no value of the pair is
both collapsed and defeated, so nothing needs a precedence rule to say
which wins.

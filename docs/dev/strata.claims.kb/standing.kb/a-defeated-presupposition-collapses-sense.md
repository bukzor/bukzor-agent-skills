---
label: SENSE
standing: agent
why:
  - defeat-is-evidence-for-an-approximator.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
  - ../reference.kb/key-valued-fields-present-a-quiver.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "moot_propagates"
---

# A Defeated Presupposition Collapses Sense

A claim whose presupposition is defeated is *moot*: it has no
standing interval at all -- not `contested`, which is an interval
with room in it, but no content left to bound. A verdict on it
judges the framing rather than what was asserted; the ledger spells
it `verdict: dissolved`.

Three commitments make that computable:

- collapse propagates. The moot set is the least fixpoint of
  "presupposes something defeated, or something moot", so it climbs
  a presupposition tower without a second rule.
- presupposition is a second edge relation over the same nodes, read
  off the record like any other quiver -- not a status, not a
  verdict, and not something an act asserts.
- it seeds from *surely* defeated only. A merely contested
  presupposition collapses nothing yet: a reader who still believes
  the presupposition still has the question in front of them.

The declined alternative is moot as a point of the status order,
below `described`. That makes mootness comparable with content
standing, so a claim could be defeated *and* moot and a reader would
need a precedence rule to say which won. The whole content of the
color is that there is nothing there to defeat.

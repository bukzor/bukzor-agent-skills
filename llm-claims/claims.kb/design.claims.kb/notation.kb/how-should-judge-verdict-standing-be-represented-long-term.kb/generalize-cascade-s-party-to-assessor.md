---
label: CONVERGE
standing: agent
why:
  - assessor-keyed-cascade-over-continuous-axes.md
  - fields-named-by-what-discharges-them-status-computed.md
  - a-fixpoint-over-an-assessor-indexed-evidence-operator.md
---

# Generalize CASCADE's Party to Assessor

CASCADE's mechanism is the right shape, keyed one notch too narrow:
"party" (a discussion participant) where
`docs/dev/strata.claims.kb/standing.kb/verdicts-are-assessor-indexed.md`
already rules "parties and checkers are one sort" (an assessor).
Widening the key closes STRONGFORM's and MECHANIZED's judge-is-a-
proof-or-checker case in the same field CASCADE already built for
judge-is-a-person, and the two systems that reached for this
mechanism independently (`docs/dev/strata.claims.kb/fleet.kb/discourse-graph-is-the-continuous-presentation.md`)
is the warrant for treating this as the convergent answer rather than
a fifth option.

Concretely, tentatively: `standing:` stays a bare scalar in the
common, TERSE-shaped case (no assessor has needed a second entry);
it escalates to a `$all`/per-assessor map with merge-patch overrides
only once a second assessor actually writes one; a map entry's value
is a cheap discrete word by default, or the full truth/certainty/
utility triple when that resolution is actually needed. Nothing here
is built -- this is a direction, not yet a schema.

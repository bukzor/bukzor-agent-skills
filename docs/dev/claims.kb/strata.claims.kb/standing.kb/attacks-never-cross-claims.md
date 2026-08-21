---
label: LOCAL
standing: bare
why:
  - contravention-must-name-its-target.md
  - defeat-is-evidence-for-an-approximator.md
  - ../view.kb/regrounding-is-incremental.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_derived_theorems.py -k "collapse_pass"
---

# Attacks Never Cross Claims

The attack graph the interval is read off is a disjoint union, one
island per claim: a non-affirming act attacks the claim it targets
and nothing else, and two acts attack each other only where their
polarities clash on the claim they share. No act reaches a claim it
did not name.

Two things follow, and they are the reasons the shape is worth
stating:

- the collapse cycle settles in one pass. Dropping a collapsed
  claim's acts removes whole islands, so no surviving claim's bounds
  move and a second round has no further collapse to find. Reading a
  record is fold, contest, collapse, contest -- not a loop.
- re-reading after a new act is local. Only the act's own claim can
  change disposition, and after it only the claims standing on it as
  a presupposition; the rest of the corpus is untouched. That is the
  derivative REGROUND asks for, and it is what lets a corpus that
  outgrows any reader be re-read in the size of the change.

The declined alternative is global attack -- letting an act's
polarity count against claims it never named. It is what any
"this contradicts the corpus" rule amounts to, and it costs both
results above: every act would move every claim, and the collapse
cycle would need a fixpoint instead of a pass.

Standing is `bare` on the attack rule, which is where the locality
is visible; `verify:` quantifies the one-pass consequence over
generated records, bounded evidence (`../../strata.claims.md`,
Verify) rather than the proof.

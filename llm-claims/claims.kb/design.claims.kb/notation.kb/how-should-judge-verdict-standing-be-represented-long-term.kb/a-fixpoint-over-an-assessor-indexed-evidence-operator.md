---
label: MECHANIZED
standing: agent
why:
  - a-single-scalar-plus-one-open-vocabulary-mark.md
---

# A Fixpoint Over an Assessor-Indexed Evidence Operator

`docs/dev/strata.claims.kb/standing.kb/` plus its witness suite
(`design-incubators/engine_tower`, tested, and the act algebra run
over `llm-claims/design.claims.kb` itself).
Standing is *defined* as the least fixpoint of a monotone evidence
operator; values live in the antichain completion because the status
order has no join over distinct certificates -- two checkers, or two
people, can each certify the same claim without a forced merge, and
the completed value holds both. The mathematically clean answer, and
proven internally consistent by its own test suite. What the real
ledger witnesses is the act algebra underneath -- one assessor per
claim, nothing striking anything -- so the evidence operator itself
still runs over no `.claims.kb/` file.

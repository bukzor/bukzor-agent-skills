---
label: HEDGE_FORM
standing: open
why:
  - ../what-need-does-a-stored-likelihood-serve.md
  - ../../../strata.claims.kb/data-representation.kb/a-simplified-form-needs-a-complete-one-under-it.md
---

# What Represents a Partially-Certain Claim?

"even if we do, is there not a better way to represent it? ... It
seems to me that, yes, in the general case we have partially-certain
claims. What's a good representation of that?" (2026-08-16).

Candidate answers go in a `.kb/` beside this file when someone works
it. Two are on the record already, neither argued:

- **a scalar in `[0, 1]`**, as today. Cheap to write, but it is an
  answer with no question attached: 0.7 of what, judged by whom.
- **an assessor-keyed map**, with the scalar as sugar for the
  single-assessor case. That is SUGAR's shape
  (`strata.claims.kb/data-representation.kb/a-simplified-form-needs-a-complete-one-under-it.md`),
  and it answers both halves of what the scalar leaves out.

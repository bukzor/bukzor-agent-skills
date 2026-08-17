# align.claims.kb -- maintenance guide

Basal principles only at this level: the few timeless design rules
the 2026-08-16/17 batch's decisions derive from, one per file,
imperative -- a constitution -- each graded `force:` (must / should
/ may, RFC 2119 per llm-design-kb's technical-policy schema).
The grade names the kind (user, 2026-08-17): `must` is a rule and
filters the design space -- violating work is non-conforming;
`should` is a heuristic and sorts it -- deviation takes recorded
justification. A file that bundles both kinds is two files.
Derive before adding: a candidate that follows from an existing
principle is not a new file, and a specific decision a principle
motivates needs no record at all. What the principles cannot
motivate goes to the residue collections: `short-term-plan.kb/`
(the yaml settled for now; descriptive, no force) and
`long-term-plan.kb/` (deferred structures and open questions; no
force). Rulings are incorporated by refining the claim they touch
-- marginalia, once enacted, is removed with its meaning absorbed:
refine, don't accrete.

## What does NOT belong here

The design commitments themselves -- they live in their own ledgers
(`docs/dev/design.claims.kb/`, `llm-claims/design.claims.kb/`, ...),
and a ruling on one of *them* is an edit to *its* file, not a claim
here. Content/quality critique of the batch -- this census is
intent only. Restatements of already-ratified law (e.g.
`review-open-questions/SKILL.md`) -- law needs no re-review.

## Lifecycle

Per-batch: this location is durable, the contents serve one review.
Once the census is reconciled and the batch commits, the contents
have done their work (the rulings live in the real ledgers); clear
or repopulate for the next batch under review.

# principles.kb -- maintenance guide

Basal principles only: the few timeless design rules the fleet's
decisions derive from, one per file, imperative -- a constitution --
each graded `force:` (must / should / may, RFC 2119 per
llm-design-kb's technical-policy schema). The grade names the kind
(user, 2026-08-17): `must` is a rule and filters the design space --
violating work is non-conforming; `should` is a heuristic and sorts
it -- deviation takes recorded justification. A file that bundles
both kinds is two files. Derive before adding: a candidate that
follows from an existing principle is not a new file, and a specific
decision a principle motivates needs no record at all.

## What does NOT belong here

The design commitments themselves -- they live in their own ledgers
(`../`, `llm-claims/design.claims.kb/`, ...); a principle is what
those commitments derive from, not one of them. Plans and open
questions -- a question binds nobody, so it lives with its theory
(e.g. `../extension.kb/`). Restatements of already-ratified law --
law needs no re-review.

---
label: FRESH_COST
standing: bare
authority: "CAP (Gilbert & Lynch 2002); incremental view maintenance"
why:
  - a-cache-is-lawful-iff-the-triangle-commutes.md
---

# Always-Fresh Is Impossible

A distributed store cannot keep every derived value continuously
lawful. Under partition, consistency and availability trade off
outright (CAP); short of partition, freshness work scales as update
rate times dependent views, and when both grow with the corpus the
total is super-linear. Perpetual freshness is not a discipline
problem; it is priced out by arithmetic.

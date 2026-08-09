# view.kb -- maintenance guide

Auxiliary theory: derived values over a store. Exists so `standing`
and `protocol` can lean on one account of caches, refresh, and
staleness instead of each carrying their own.

- `prior:` history, purpose
- `ontology:` view, cache, derivative, refresh, recompute, staleness,
  debt, drift, stamp, reader, diff
- `defeated by:` a reader that can afford to recompute every read --
  then caches, and everything priced here, vanish

## What belongs here

A commitment about the relation between a derived value and the state
it derives from: lawfulness, refresh, the price of deferral.

## What does NOT belong here

Which values a particular stratum derives (reachability ->
`../reference.kb/`, standing -> `../standing.kb/`), or fixpoint
machinery (-> `../fixpoint.kb/`).

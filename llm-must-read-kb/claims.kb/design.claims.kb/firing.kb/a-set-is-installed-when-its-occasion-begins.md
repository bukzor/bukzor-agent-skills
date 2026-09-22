---
label: BEGIN
standing: agent
why:
  - a-bank-is-a-partition-of-triggers-indexed-by-occasions.md
---

# A Set Is Installed When Its Occasion Begins

The set at X is installed at the moment X begins, by listing it;
nothing else installs it and nothing uninstalls it. The listing is the
install -- there is no separate registration step -- which is what lets
a consumer with no runtime support meet the same semantics as one with
hooks.

Stale when: a delivery path installs a set on a condition other than
its occasion beginning (a hook, a schedule); the puller changes and the
"at begin" clause is re-read against it.

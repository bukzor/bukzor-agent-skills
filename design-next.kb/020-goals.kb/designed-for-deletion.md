---
why:
  - ../010-mission.md
---

# Designed for Deletion

Retiring any part of the system is `git rm -r` plus dangling
cross-references — and adopting any part is copying that one piece
out, alone. When we stop having the need, or find a replacement we
like better, removal is 90% of the work done; third-party users
(sometimes the operator on another day) pull the pieces they find
compelling and ignore the rest.

The structural consequence: units group by domain (subject), not by
function (technology). A domain's conventions, teaching, and tooling
live and die together; cross-domain machinery stays thin enough that
no domain's deletion strands behavior in a shared engine.

This bounds `single-source-improvement`, which pulls toward
function-concentration: DRY *within* the domain unit (one source
artifact can compile to its enforcement, its checks, and its
teaching), never by centralizing a domain's behavior into shared
infrastructure that outlives it.

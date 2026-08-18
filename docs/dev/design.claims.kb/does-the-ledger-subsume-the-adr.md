---
label: ADR_FATE
standing: open
why:
  - ../design.claims.md
---

# Does the Ledger Subsume the ADR?

FLEET_DESIGN's division of labor gave the ADR the record of a ruling
-- context, alternatives, date -- and the ledger the current standing.
With `verdict:` naming what was ruled and `authority:` naming the act
that settled it, the ledger now carries most of that record itself;
the ADR's residue is narrative -- the concerns and discussion around
the ruling -- which is what the devlog keeps. The user reads it so
(2026-08-18): ADR and devlog both predate the kb and claims systems,
and the ADR "may be entirely subsumed by design.claims.kb, now."

Deliberately punted the same day. Cheap evidence accrues on its own:
the next ruling that wants an ADR either says something no claim
field holds, or it doesn't. Ruling this retires or re-charters
`docs/dev/adr/`.

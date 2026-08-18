---
label: STORAGE
standing: agent
why:
  - ../standing.kb/standing-is-computed-not-stored.md
  - ../standing.kb/append-and-retract-are-asymmetric.md
  - ../fixpoint.kb/downward-revision-overshoots.md
---

# What May Be Stored, What Must Be Computed?

As wrestled (PRMS, as `LEAST_FIX`): may an entry's standing be written
into the entry -- and what exactly corrupts if it is?

Settled, upgraded from taste to theorem: acts only are stored;
standing is the least fixpoint of the evidence operator. The exact
corruption: after a retraction, a stored standing rests at a fixpoint
strictly above the least one -- a ring of mutual support surviving on
its own bootstraps -- and no local inspection detects it. Caching is
lawful only as a stamped view.

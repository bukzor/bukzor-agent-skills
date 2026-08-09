---
label: OVERSHOOT
standing: bare
why:
  - warm-start-is-sound-upward.md
---

# Downward Revision Overshoots

The dual of warm-start fails. If the operator shrinks (Phi' <= Phi),
the old least fixpoint x is only a post-fixed point of Phi'
(Phi'(x) <= x), and downward iteration from x converges to the
*greatest* fixpoint of Phi' below x -- in general strictly above
lfp(Phi').

Minimal witness: two points each supporting the other, external
support removed. Downward revision from the old state keeps both (they
hold each other up); the least fixpoint has both at bottom.

Consequence: shrinking the operator admits no warm start -- recompute
from bottom, or maintain enough bookkeeping (support counts) to
distinguish self-supporting loops from grounded support.

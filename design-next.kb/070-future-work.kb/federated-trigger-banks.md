---
why:
  - ../040-design.kb/delivery-boundary.md
  - ../030-requirements.kb/judgment-triggers-remain-scannable.md
trigger: A skill's own triggers must reach a consumer who did not author them — a second operator, or an install whose must-read.kb the skill's author does not control.
---

# Federated Trigger Banks

Let an installed skill contribute a bank of its own that merges into
the user-scope scan, so a trigger ships with the skill that owns it
and is still found by the one mandatory listing.

The two surfaces split today by ownership rather than by concern: the
filename-indexed bank lives in the operator's dotfiles, while a
skill's own triggers can travel only in its `description:`. That
forces a choice with no good answer — file skill triggers in the
dotfiles, and a skill's details live in a repo separate from the
skill; or leave them in the description, and carry a second surface
the host protocol must bind by hand. The 2026-08-27 migration took
the second branch and bound descriptions explicitly in the operator's
Required Reading. Federation is what would collapse the two surfaces
from the other end, without moving anything away from its owner.

Deferred because it buys nothing at n=1: one operator, one dotfiles
repo, and descriptions already reach every session for free. The cost
appears the first time a skill is installed by someone whose bank its
author cannot edit.

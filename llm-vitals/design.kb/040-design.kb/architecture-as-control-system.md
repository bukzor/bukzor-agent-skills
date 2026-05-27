---
why:
  - multi-axis-surface
  - visible-debt
  - cadence-bound-checkins
---

# Architecture as a Control System

The system is a **control system**, not a ranker. This framing
matters because it precludes a class of "obvious" alternative
architectures that would degrade the design.

## The frame

The operator allocates scarce attention across multiple competing
drives:

- **Revenue / customer** — short feedback loop; hard cash floor
- **Deep work / tech** — long feedback loop; compounding payoff
- **Maintenance** — small constant tax; ignore it and the system rots
- **Exploration** — deep-work subtype with uncertain payoff
- **Wellness** — upstream of everything else; rots silently

A control system allocates a resource across competing demands using
**budgets with feedback**, not bans or fixed quotas. Each drive has a
target floor; the controller (the picker) biases toward whichever
drive is most in debt; visible state (vitals dashboard) provides the
feedback signal.

## What this rules out

- **Single-axis rankers (WSJF, RICE, ICE)**. Single-axis collapses
  multi-drive rotting into one number; loses signal on which domain
  is failing.
- **Hard quotas** ("only 4h of tech this week"). Bans waste option
  value and produce gaming. Budgets with visible-debt feedback
  preserve agency while making imbalance impossible to ignore.
- **Hard scheduling** ("Mondays are revenue days"). Calendar
  pre-allocation can't respond to changing state. The control loop
  re-evaluates on every session-start.
- **Static priority orderings**. The drive most in debt right now
  outranks any pre-declared priority order.

## What this rules in

- Budgets per drive (tier-2 SLOs); feedback via visible debt.
- Drives compete; debt is the medium of competition.
- Runway and other master state variables can re-tune budgets
  globally (the controller updates its own setpoints; see
  `070-future-work.kb/runway-as-master-state.md`).
- Forced functions (anchoring to session-start/end) provide the
  control-loop tick.

Classical control theory has decades of refinement on multi-input
multi-output systems with floor constraints; we are reusing a
well-attested pattern, not inventing one. Future agents proposing
"let's just rank everything" should be turned back at this entry.

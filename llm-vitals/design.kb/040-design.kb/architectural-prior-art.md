---
why:
  - multi-axis-surface
---

# Architectural Prior Art — Three-Tradition Convergence

The vitals architecture is not novel. Three independent traditions
converged on **multi-axis health monitoring with per-axis thresholds**;
we are applying the well-attested pattern to a new substrate (the
one-person operator's life + business).

## The three traditions

**Balanced Scorecard** (Kaplan & Norton, 1992) — business performance
across four perspectives: financial, customer, internal process,
learning & growth. Battle-tested for organizational use over three
decades. Independent traditions cite it; consulting practices teach it.

**Wheel of Life** (origin in life-coaching, popularized by Paul Meyer
and others) — personal life balance across 8-12 segments rated on a
radial chart. Used in coaching contexts for decades; pre-dates most
"productivity app" frameworks.

**The Golden Signals** (Google SRE Book, 2016) — production-service
health across four axes: latency, traffic, errors, saturation.
Crystallized SRE practice that had been informal at Google and
elsewhere through the 2000s.

## Why this convergence matters

Three communities — management consultants, life coaches, site
reliability engineers — independently arrived at the same answer:
*you cannot represent a multi-drive rotting domain with a single
metric.* The dimensions matter; the right number of dimensions is
~3-12 (working-memory bound); each dimension needs its own threshold;
the dashboard is the primary artifact.

This is strong confidence that the architecture is on a well-trodden
path. It also tells us where to import refinements from:

- **From Balanced Scorecard**: cascading objectives (we deferred this
  to runway-as-master-state for now), strategy maps (not yet applied).
- **From Wheel of Life**: radial visualization (in
  `070-future-work.kb/wheel-of-life-visualization.md`).
- **From SRE**: error budgets, burn-rate alerts, liveness vs.
  readiness, blameless postmortems — already imported into the design.

## Where we deviate

The traditions diverge on:

- **Cadence**: SRE alerts continuously; Balanced Scorecard reviews
  quarterly; Wheel of Life is reviewed sporadically. We use
  **demand-driven** review (compiler metaphor) — recomputes per
  session.
- **Audience**: each tradition serves a different audience. We're
  designing for a *single operator self-auditing*, which removes
  social/political dynamics but adds the calibration problem
  (operator is both observer and observed).
- **Persistence**: organizational dashboards are continuously
  monitored; ours is reviewed at session boundaries. Mismatched
  cadence costs us some leading-indicator coverage; gained because
  no human can sustain continuous self-monitoring.

## Implication

When extending the design, **check what these traditions already
solved**. Most "new" mechanisms you'll propose have a precedent
under one of the three. Reusing prior art beats reinventing it.

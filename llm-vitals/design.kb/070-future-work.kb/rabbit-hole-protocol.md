---
why:
  - enable-accountable-deep-work
trigger: After ~20 day-log entries exist providing calibration baseline.
---

# Rabbit-Hole Protocol

Treat each deep-work exploration session as an investment position.
Three gates (pre-entry, mid-hole, post-hole), each lightweight, that
together produce the calibration data necessary to distinguish
productive rabbit holes from unproductive ones.

The operator's stated motivation: rabbit holes that "quietly improve
several entire fields at once" should be encouraged; rabbit holes
that don't pay off should be penalized. The operator cannot reliably
distinguish these in advance, but with accumulated postmortems can
learn their personal hit-rate per category.

## Pre-entry gate

Three required lines before starting a rabbit hole:

- **Claimed beneficiaries** — which vitals or themes could this
  help? List them. Multi-domain rabbit holes get a leverage
  multiplier later in the picker; single-domain rabbit holes don't.
- **Burn budget** — max hours before forced reassessment (e.g.,
  8h). The budget is the unit of commitment.
- **Exit signal** — what would tell me to abandon early? Often
  the negation of the thesis (e.g., "if dependency X turns out to
  block this, exit").

The act of writing these is itself a filter. Many rabbit holes
evaporate at the gate because no honest answer emerges — a sign
the operator wasn't really sure what they were chasing.

## Mid-hole intercept

At burn-budget exhaustion, the system **surfaces** (does not
terminate). Three options:

1. **Commit another tranche**, with refined claim. Usually with a
   shorter budget than the original, reflecting the
   diminishing-returns assumption.
2. **Exit with findings** — capture what was learned even if the
   original thesis didn't pan out.
3. **Exit and discard** — the rabbit hole was a dead end; no
   notable findings.

Discipline lives in the forced reassessment, not in the initial
estimate. Most people are 2-3× optimistic on initial budgets; the
re-check catches this.

## Post-hole postmortem

One line per claimed beneficiary: did it actually benefit?
Yes / no / partial.

Cheap to write (~30 seconds) — the operator already has the context.
Each yes/no/partial is one data point in the calibration model.

## Calibration over time

After ~20 logged sessions, the operator has a personal batting
average:

- **Burn-budget accuracy** — typical multiplier (often 2-3×
  optimistic). Future estimates can be auto-scaled when the
  operator says "8h" the system pre-loads 24h and asks for
  confirmation.
- **Claimed-beneficiary hit rate** — per category. Multi-theme
  claims may be 35% accurate; single-theme claims 70%. The numbers
  matter.
- **Theme leverage** — which themes the operator *actually*
  cross-leverages on vs. claims to. Surfaces honest signal about
  where rabbit holes pay off.

The system applies the operator's personal discount factor to
future predictions. When the operator claims "this 8h hole will
help 4 themes," the picker shows: *"your historical 4-theme hit
rate is 35%; expected hours-equivalent value is X."* This is the
data that makes the architecture self-improving.

## Multi-domain leverage scoring

Items and rabbit-hole proposals carry a **theme-touch list**. The
picker weighs cross-cutting items higher (their "blocker-leverage"
forward-looking cousin). Calibrated against historical N-themes-
claimed hit rate, this becomes one of the strongest signals in the
system.

If the operator's data shows they reliably make 3-theme claims pay
off, multi-theme rabbit holes deserve weight. If 3-theme claims
historically fizzle, the multiplier reverses to a discount.

## Why deferred

Useless without data. Until ~20 day-log entries exist, there's no
baseline; the postmortem prompts add friction without payoff. Once
that corpus exists, the protocol earns its keep within weeks.

Graduates when the operator has ~20 logged work sessions of any
kind, not specifically rabbit holes — postmortems on any
deep-work session contribute to the calibration data.

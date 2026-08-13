---
why:
  - decoupled-data-location
  - grow-incrementally
---

# Automation Boundary

The principle dividing what the system automates from what it leaves
to human judgment. Important for future implementation work because
the wrong side of the line collapses the system's signal.

## The rule

**Automate** where the input is observable and the output is
deterministic.

**Keep manual** where judgment is required — i.e., where the operator's
honest assessment is the data, not a derived signal.

## What this looks like, concretely

**Automate**:

- Scheduled polling of external state (financial APIs → runway;
  inbox → perishable candidates)
- Wake-condition firing detection when the trigger is objectively
  checkable (file exists, PR merged, date passed, threshold
  crossed)
- Calibration math (pure function over the postmortem log)
- Budget reallocation on runway threshold crossings
- Debt computation per vital from the day-log
- Burn-rate projection from current consumption + budget
- Status coloring (red/yellow/green) from debt + budget state

**Keep manual**:

- Postmortem scoring — did the rabbit hole actually pay off, per
  claimed beneficiary?
- Wake conditions where the trigger is "I sense the moment"
- Initial vital classification — does this item belong to revenue
  or customer? body or restoration?
- Theme membership decisions
- The check-in journal entry itself — its content is the signal

## Why this matters: LLM temptation

The seductive failure mode is **LLM-automating judgment calls**. An
LLM will produce plausible postmortem scores and reasonable-looking
theme memberships. The signal then becomes downstream of LLM
hallucination, and the calibration data is poisoned at the source.

If the operator's calibration model says "your 4-theme claims are
35% accurate," that number is only useful if the *postmortems were
the operator's*. An LLM can suggest, but the score must be the human's.

The one allowed LLM role inside the data pipeline:
`070-future-work.kb/llm-metric-extraction.md` — using an LLM to
surface *candidate* metrics from journal corpus for the operator to
confirm. Surface, not author. The operator confirms before anything
becomes data.

## Cost of getting this wrong

- **Automating judgment**: silent calibration corruption. Operator
  trusts the system's outputs, which are LLM confabulations
  presented as data.
- **Manual-izing the deterministic**: the system fails to install
  the discipline it's supposed to enable. The operator skips the
  manual step, the data stops flowing, the whole architecture
  collapses.

Lean toward automation for the deterministic; lean toward manual for
the judgment-bearing. Mistakes in the first direction are tolerable;
mistakes in the second direction are fatal.

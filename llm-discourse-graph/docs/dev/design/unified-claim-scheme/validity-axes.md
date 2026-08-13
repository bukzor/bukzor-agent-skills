# Validity Axes

## Decision

Three continuous axes for evaluating claims, collectively called
"validity" (per Habermas's Geltungsansprüche).

| Axis | Range | Default | Domain |
|---|---|---|---|
| truth | 0–1 | 1 | Ontological — assessor's best estimate of correspondence to reality |
| certainty | 0–1 | 1 | Epistemic — how confident? |
| utility | -1–1 | 1 | Pragmatic — how valuable? |

## Discussion

### Why three axes, not more?

The prior art survey identified up to seven candidate axes across
frameworks (Habermas, Toulmin, Bayesian epistemology, modal logic, etc.).
Several collapse or derive from graph structure:

- **Resilience** = function of certainty + weight of evidence (not independent)
- **Precision** = property of formulation, not epistemic status (metadata)
- **Authority dependence** = derivable from source attribution
- **Inferential robustness** = derivable from graph structure (has why[]?)
- **Analytic vs synthetic** = correlates with normativity, but independent
  for edge cases (mathematical truths, empirically-grounded norms).
  Captured by truth=1-by-construction + absence of sources/why[].

Three stored axes, with basis and analytic-ness emergent from graph
structure.

### Why truth and certainty are independent

A meteorologist can be very certain (certainty=0.95) about a low
probability (truth=0.3) of rain. Collapsing them loses this distinction.

### Why utility is -1 to 1, not 0 to 1

Nonexistent utility (0) and negative utility (-1) are qualitatively
distinct. A definition that causes confusion, a rule that produces
perverse incentives — these are actively harmful, not merely absent.

### Why defaults are all 1 (except utility range)

A claim with no explicit validity is fully accepted: true, certain,
useful. This means zero bits of denotation for the common case — a claim
that nobody contests. Validity fields only appear when something departs
from full acceptance.

### Challenge modes are emergent

A claim's position on the axes + graph structure determines which
challenges are valid. Truth/accuracy and validity (Pollock's rebutting
vs undercutting defeaters) unify into a single "correctness" challenge
whose character varies along the empirical ↔ logical basis spectrum.

Three challenge regions:
1. **Correctness** — low normativity, descriptive claims
2. **Utility** — high normativity, prescriptive claims
3. **Definitional** — truth=1 by construction, stipulative claims

## Key References

- Habermas, "validity claims" — group name and multi-dimensional framing
- Pollock, rebutting vs undercutting defeaters — unified into correctness
- Searle, direction of fit — basis for normativity axis
- Bayesian epistemology — independence of credence and certainty

## Q&A (2026-03-04 lane-mixing review)

### Q: For experiments, do truth/certainty take on exact mathematical meaning?

Truth/certainty are *informed by* statistical methods (p-values, confidence
intervals) but are not mechanically determined by them. The framework
stores the assessor's conclusion, not the methodology. A frequentist
and a Bayesian may arrive at the same truth value via different paths —
the schema is agnostic to the epistemological framework used. Statistical
rigor improves the quality of the estimate; it doesn't change what the
field represents.

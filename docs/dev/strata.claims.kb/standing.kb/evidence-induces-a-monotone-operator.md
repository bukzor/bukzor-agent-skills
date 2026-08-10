---
label: OPERATOR
standing: agent
why:
  - status-is-a-poset-with-a-fibered-top.md
  - ../reference.kb/reachability-is-a-least-fixpoint.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_phi_is_monotone_on_an_instance
---

# Evidence Induces a Monotone Operator

The evidence set -- warrants, certificates, verdicts, recorded fiats
-- determines an operator on status-assignments over the entries,
raising each entry as far as the evidence citing it (through the
reference structure) supports. Its rule format is the law: an ascent
rule grants a status once every premise stands at or above a
threshold; descent enters only as a recorded fiat or as removal of
evidence, never as a rule's conclusion. So long as defeat is absent,
the operator is monotone.

Support and defeat are separate calculi. Counter-evidence is not
negative support: an observation against a claim is evidence *for*
an attack on it, and attacks are computed in the contest calculus
(defeat-is-evidence-for-an-approximator.md), never as descent inside
this one. Mixing them -- rule-based demotion -- would make the
answer depend on processing order; the separation keeps support
canonical and contests canonical, each in its own fixpoint.

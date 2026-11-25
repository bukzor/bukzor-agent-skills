---
managed-by: Skill(llm-subtask)
status: open
blocked-by:
  - 2026-11-25-000-apply-skill-kb-layout-migration.md
required-reading:
  - CLAUDE.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/smoothing-is-a-quality-pass.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-passes-run-at-occasions.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/
  - ../../../llm-kb/skill.kb/quality-passes.kb/one-home.md
  - ../../../llm-design-kb/skill.kb/quality-passes.kb/each-rung-says-only-what-its-question-asks.md
  - ../../../llm-design-kb/docs/dev/claims.kb/design.kb/stratification.kb/every-claim-reaches-the-mission.md
---

# `smoothing`: the quality pass that walks a whole ledger

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (wave
3)

## Problem Statement

Write `llm-claims-kb/skill.kb/quality-passes.kb/smoothing.md`, the pass
`SMOOTHING` rules. It is the walk that found most of the faults in session
59b55f01 (my-own-shadertoy, 2026-11-23..25), and it is written down nowhere,
so nobody can run it again. Readers: an agent at a consolidation session, sent
here by a trigger. It must be runnable cold.

The pass, in the shape of its siblings (`PASS_AT_OCCASION`: what it improves,
how to walk, what a finding means, how it is repaired; it names no occasion):
walk the `why:` graph top-down, then bottom-up. At each node, apply the passes
that judge one node in context:

- its theory's question: confinement, and in a design tower its rung's
  question (`llm-design-kb`'s each-rung lens);
- its `why:` (`REACH`, and the `corollaries` pass);
- its siblings (`one-home`);
- the rulings it quotes (`ruling-fidelity`).

Adjust nodes and edges, then walk again, until a walk changes nothing. The
pass cites each of these and restates none of them. For the scans, it points
at the sweep, `../procedures.kb/run-quality-passes.md`, which sibling unit 001
is writing now. That sweep is where "run scans from the project root" lives.

Decided: smoothing lives in `llm-claims-kb` because every ledger needs it.
Where it names `llm-design-kb`'s rung lens, the clause says "in a design
tower". The layered skill does not own the walk.

Settle and report: whether the walk needs a stopping rule beyond "a walk
changes nothing", such as a cap, or the ledger's size as the measure. Use
judgment; 59b55f01 did not record one.

Optional, ≤10 minutes: 59b55f01's transcript shows how the walk was actually
run (`Skill(claude-code-archeology)`; session
`59b55f01-a707-409f-9f4b-78bea5090043`). Use it for method only. Don't copy
its findings into the pass.

**Scope (only these files):**
`llm-claims-kb/skill.kb/quality-passes.kb/smoothing.md`.

## Steps

## Decisions

## Open Questions

## Final report

# Run Quality Passes

> [!DRAFT] agent-authored 2026-11-25, vetoable

Sweep a design record with urgency tiers. A design record is a claims.kb, so
run `Skill(llm-claims-kb)`'s sweep first, all of it (it runs `Skill(llm-kb)`'s
in turn): `../../../llm-claims-kb/skill.kb/procedures.kb/run-quality-passes.md`.
Its blocking scans are this sweep's Tier 1, and its confinement pass over
`llm-claims-kb-ownership --trespass` is the rungs' confinement; neither is
repeated here. Then the tier below.

Skip a pass only when its applicability condition doesn't match.

## Tier 2 -- required when applicable

Findings addressed, not deferred.

| Pass | Applies when |
|---|---|
| `../quality-passes.kb/each-rung-says-only-what-its-question-asks.md` | a claim written or its body changed, or a claim moved between rungs |
| `../quality-passes.kb/state-properties-not-mechanisms.md` | a requirement or architecture claim written or changed, title included |
| `../quality-passes.kb/regression-proof-with-principles-not-narrative.md` | a claim corrected, or a touched body holds a past-tense or dated sentence |

## Completion

1. `Skill(llm-claims-kb)`'s sweep complete.
2. Every applicable pass above asked and findings recovered.

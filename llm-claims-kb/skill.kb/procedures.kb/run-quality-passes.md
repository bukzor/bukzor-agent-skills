# Run Quality Passes

> [!DRAFT] agent-authored 2026-11-25, vetoable

Sweep a claims.kb with urgency tiers. A claims.kb is a `.kb`, so run
`Skill(llm-kb)`'s sweep first, all of it:
`../../../llm-kb/skill.kb/procedures.kb/run-quality-passes.md`. Its Tier 1
`llm.kb-validate <ledger>` is the schema check here as well: it validates
every claim, roll-up included, against the ledger's `$ref` of
`jsonschema/claim.jsonschema.yaml`. Then the tiers below.

Run every scan from the project root. The ownership and mentions scans read
the ledgers under the working directory, so run inside a ledger they see
only part of the fleet, and deeper in they report "0 stipulations": a scan
run in the wrong place, not a broken tool.

Skip a pass only when its applicability condition doesn't match.

## Tier 1 -- blocking

Re-run until passing. Failure stops downstream tiers.

| Scan | Passes when |
|---|---|
| `bin/llm-claims-kb-graph <ledger>` | no `why:` drawn red on stderr; acyclic |
| `llm-claims-kb-mentions <ledger>` | 0 tokens unresolved |
| `llm-claims-kb-ownership` | no contending double your edit introduced; one is the owner's to decide, via `../quality-passes.kb/confinement.md` |

## Tier 2 -- required when applicable

Findings addressed, not deferred.

| Pass | Applies when |
|---|---|
| `../quality-passes.kb/graph-health.md` | a claim added, renamed, or removed, or a `why:` changed |
| `../quality-passes.kb/confinement.md`, over `llm-claims-kb-ownership --trespass` | a finding names a theory you touched |
| `../quality-passes.kb/ruling-fidelity.md` | a touched claim quotes a ruling |
| `../quality-passes.kb/standing-honesty.md` | a `standing:` written or changed |
| `../quality-passes.kb/corollaries.md` | a claim follows from others, or a bloat finding would strip one |

## Tier 3 -- situational

Skip if condition doesn't clearly match.

| Pass | Applies when |
|---|---|
| `../quality-passes.kb/stamp-freshness.md` | a collection under a stamped roll-up changed |
| `llm-claims-kb-ownership --idle` | a `why:` into another theory added or removed |

## Completion

1. `Skill(llm-kb)`'s sweep complete.
2. Every Tier 1 scan passes.
3. Every applicable Tier 2 pass asked and findings recovered.
4. Every applicable Tier 3 pass considered.

Smoothing, the walk over the whole ledger, is no tier of this sweep: it runs
at consolidation (`../quality-passes.md`).

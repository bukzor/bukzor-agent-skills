# Run Quality Passes

Sweep `../quality-passes.kb/` with urgency tiers.

Skip a pass only when its applicability condition doesn't match.

## Loading the passes

```bash
tail -vn99 ../quality-passes.kb/*.md
```

## Tier 1 — blocking

Re-run until passing. Failure stops downstream tiers.

| Pass | Applies when |
|---|---|
| `llm.kb-validate <path>` | always |
| `llm-triggers/bin/llm-triggers-lint <path>` | any frontmatter written or edited |
| `../quality-passes.kb/cross-references.md` | any kb file written or edited |

## Tier 2 — required when applicable

Findings addressed, not deferred.

| Pass | Applies when |
|---|---|
| `../quality-passes.kb/per-file-scope.md` | any kb file written or edited |
| `../quality-passes.kb/promotion-signals.md` | any flat `.md` written or grown |
| `../quality-passes.kb/collection-homogeneity.md` | a `.kb/` had items added or edited |
| `../quality-passes.kb/filename-discipline.md` | any file created or renamed |
| `../quality-passes.kb/bloat.md` | any file written or edited |
| `../quality-passes.kb/one-home.md` | any kb file written, edited, or cut |
| `../quality-passes.kb/claudemd-enumeration.md` | a `CLAUDE.md` was touched |
| `../quality-passes.kb/claudemd-completeness.md` | a `CLAUDE.md` was touched |
| `../quality-passes.kb/enumeration-completeness.md` | a collection was created or extended |
| `../quality-passes.kb/schema-potential.md` | a touched `.kb/` has 2+ items |
| `../quality-passes.kb/synthesis-file-value.md` | a `$CATEGORY.md` was touched |

## Tier 3 — situational

Skip if condition doesn't clearly match.

| Pass | Applies when |
|---|---|
| `../quality-passes.kb/orphan-entries.md` | content was removed |

## Completion

1. Every Tier 1 pass passes.
2. Every applicable Tier 2 pass asked and findings recovered.
3. Every applicable Tier 3 pass considered.

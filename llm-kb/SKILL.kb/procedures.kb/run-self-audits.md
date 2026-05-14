# Run Self-Audits

Sweep `../self-audit.kb/` with urgency tiers.

## When invoked

- `../must-read/after/creating-or-editing-kb-files.md`
- `../must-read/before/marking-kb-work-done.md`

Skip an audit only when its applicability condition doesn't match.

## Loading the audits

```bash
tail -vn99 ../self-audit.kb/*.md
```

## Tier 1 — blocking

Re-run until passing. Failure stops downstream tiers.

| Audit | Applies when |
|---|---|
| `bin/llm.kb-validate <path>` | always |
| `../self-audit.kb/cross-references.md` | any kb file written or edited |

## Tier 2 — required when applicable

Findings addressed, not deferred.

| Audit | Applies when |
|---|---|
| `../self-audit.kb/per-file-scope.md` | any kb file written or edited |
| `../self-audit.kb/promotion-signals.md` | any flat `.md` written or grown |
| `../self-audit.kb/collection-homogeneity.md` | a `.kb/` had items added or edited |
| `../self-audit.kb/filename-discipline.md` | any file created or renamed |
| `../self-audit.kb/bloat.md` | any file written or edited |
| `../self-audit.kb/claudemd-enumeration.md` | a `CLAUDE.md` was touched |
| `../self-audit.kb/claudemd-completeness.md` | a `CLAUDE.md` was touched |
| `../self-audit.kb/enumeration-completeness.md` | a collection was created or extended |
| `../self-audit.kb/schema-potential.md` | a touched `.kb/` has 2+ items |
| `../self-audit.kb/summary-file-value.md` | a `$CATEGORY.md` was touched |

## Tier 3 — situational

Skip if condition doesn't clearly match.

| Audit | Applies when |
|---|---|
| `../self-audit.kb/orphan-entries.md` | content was removed |

## Completion

1. Every Tier 1 audit passes.
2. Every applicable Tier 2 audit asked and findings recovered.
3. Every applicable Tier 3 audit considered.

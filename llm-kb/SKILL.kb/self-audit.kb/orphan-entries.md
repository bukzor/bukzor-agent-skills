# Self-audit: orphan entries

## Goal

Every entry has ≥1 inbound reference. 1-ref entries flagged for
inlining.

## When to run

After **removing** kb content. Skippable otherwise.

## Procedure

```bash
grep -rl $entry-slug .
```

- 0 refs → orphan
- 1 ref → single-caller

## Recovery

| Finding | Action |
|---|---|
| 0 refs, dead | Delete |
| 0 refs, pre-future-work | Keep; `TODO: caller pending` |
| 1 ref, short or caller-specific | Inline; delete file |
| 1 ref, stands alone | Keep |

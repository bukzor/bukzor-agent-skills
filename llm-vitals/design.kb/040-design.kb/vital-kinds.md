---
why:
  - support-both-vital-kinds
---

# Vital Kinds

Different vitals have different natural reporting mechanisms. Two
kinds, both fit the two-tier scheme uniformly.

## Journal-Kind

Each vital owns a `.kb/` directory of dated journal entries.

- Examples: `body`, `relationships`, `restoration`, `meaning`
- Tier 1 = "≥1 journal entry within N days"
- Tier 2 (later) = metrics extracted from entry content (e.g.,
  LLM-summarized sleep averages, mood signals)

Journals capture **texture** that hours-and-counts cannot. Sleep isn't
a task; friendship isn't a task. The unit of reporting is the
narrative entry itself, which doubles as the source of structured
metrics when richer instrumentation is added later.

## Task-Kind

Vital is referenced as a frontmatter tag on existing task items
elsewhere in the user's task system.

- Examples: `revenue`, `customer`, `tech`, `maintenance`, `ops`,
  `marketing`, `monitoring`
- Tier 1 = "day-log.jsonl mentioned this vital within N days"
- Tier 2 = aggregated hours or touch counts meet a threshold

Reuses the existing task tracking system. No journals required —
though a `.kb/` may still be created if the user wants prose
reflection in addition to task tracking.

## Why the Split

Wellness has no task-shaped output and resists hour-counting. Work has
naturally-task-shaped output and benefits from existing task
infrastructure. Forcing one shape on both produces friction in one
direction or the other. The kind dispatch costs nothing —
configuration is per-vital — and respects the natural data shape of
each domain.

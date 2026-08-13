# chatlib-index

Create or update a top-level SUMMARY.md for a cleaned/segmented conversation.

## When to use

After `chatlib-segment` and `chatlib-digest` have produced topic directories with their own SUMMARY.md files. When a latecomer (human or agent) needs a single entry point.

## Input

A `*.cleaned/` directory with numbered topic subdirectories, each containing a SUMMARY.md.

## Procedure

1. **Read all segment SUMMARY.md files.**
2. **Write a top-level SUMMARY.md** with these sections:
   - **What Happened** — 2-3 sentences. The overall arc in plain language.
   - **Sub-Conversations** — Table with: number, directory (linked), message range, one-line topic.
   - **Extractable Value** — Priority-ordered list from `chatlib-assess`, with tiers (must-extract / should-extract / background). Reference specific messages.
   - **Dependency Chain** — How the artifacts relate to each other and to implementation. Text diagram if helpful.
   - **Key Design Decisions** — Consolidated list of decisions scattered across segments. These are the constraints a builder needs to know upfront.
   - **For Latecomers** — Reading order recommendations. What to read first, what to skip, what to consult on demand.

## Style

- Write for someone who has never seen the conversation and has 2 minutes.
- Use the dependency chain to motivate reading order — don't just say "read 6 first," say *why*.
- Distinguish between what the conversation *decided* and what it *discussed*. A latecomer should know which segments contain decisions they're bound by vs. background they can skim.

## Maintenance

- Update when new segments are added or assessments change.
- If extracted artifacts exist, reference them from the Extractable Value section.

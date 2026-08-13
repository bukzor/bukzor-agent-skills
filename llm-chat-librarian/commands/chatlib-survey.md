# chatlib-survey

Analyze a conversation dump and report its structure.

## When to use

First contact with a conversation export. Before segmenting, summarizing, or extracting.

## Input

A directory containing conversation message files (.md, .json, or mixed). May include fork directories, nested structures, or flat message sequences.

## Procedure

1. **Inventory** — List all files, identify formats present (.md, .json, directories). Report counts.
2. **Identify structure** — Detect forks (timestamped directories), dead ends, linear runs. Map the conversation tree.
3. **Count semantic sub-conversations** — Group by topic, not by directory. Typo forks and truncated responses count as zero. State your grouping criteria.
4. **Identify participants and roles** — Who's talking? What are their roles/expertise?
5. **Trace the arc** — What's the overall trajectory? Where does the conversation start and end?
6. **Flag format issues** — Are .json files redundant with .md? Are there empty files, orphaned metadata, broken links?

## Output

A structured report to the user (not a file). Include:
- File/directory counts and formats
- Conversation tree (text diagram)
- Semantic sub-conversation count with one-line descriptions
- Overall arc summary
- Any format/quality issues found

## What this is NOT

- Does not create files or directories
- Does not modify the source data
- Does not summarize individual messages (that's `chatlib-digest`)
- Does not assess value (that's `chatlib-assess`)

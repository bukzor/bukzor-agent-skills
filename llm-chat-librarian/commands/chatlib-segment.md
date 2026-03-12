# chatlib-segment

Split a conversation into topical sub-conversations.

## When to use

After `chatlib-survey` has identified the semantic sub-conversations. When the conversation is too large or too tangled to work with as a unit.

## Input

- A surveyed conversation directory
- The semantic grouping from `chatlib-survey` (or user-provided topic boundaries)

## Procedure

1. **Define topics** — Name each sub-conversation with a short, descriptive slug (e.g., `03-sync-design`). Number for reading order.
2. **Map messages to topics** — Assign each message to exactly one topic. Messages at topic boundaries may appear in both (flag these).
3. **Flatten forks** — When multiple forks cover the same topic, choose the canonical one (longest, most complete, or user-specified). Skip typo forks and truncated dead ends entirely.
4. **Create directories** — One per topic, in a sibling `*.cleaned/` directory (not inside the source).
5. **Symlink, don't copy** — Create relative symlinks to the source .md files. Preserves single source of truth.
6. **Exclude metadata-only files** — Skip .json files, system messages without .md content, and other non-substantive files unless user requests otherwise.

## Output

```
<source>.cleaned/
  01-topic-name/
    NNN.role.type.md -> ../../<source>/...
  02-topic-name/
    ...
```

## Decisions to confirm with user

- Where to draw topic boundaries (especially gradual topic shifts)
- Which fork variant is canonical when multiple exist
- Whether to include dead-end forks (default: skip unless user says otherwise)

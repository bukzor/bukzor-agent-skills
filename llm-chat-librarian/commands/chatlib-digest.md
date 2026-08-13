# chatlib-digest

Write a SUMMARY.md for a directory of conversation messages.

## When to use

Any time a directory of .md message files needs a navigable entry point — whether it's a raw conversation tree, a single fork branch, or a cleaned segment.

As the first step on a raw export, digest every directory in the tree. This makes all downstream commands fast: they read summaries instead of raw messages.

## Input

A directory containing conversation message .md files. May be a raw export directory, a fork branch, or a segmented topic directory.

## Procedure

1. **Read all .md files** in the directory (NOT subdirectories): `tail -vn9999 *.md`
2. **Write SUMMARY.md** with:
   - **Metadata** — Message range (e.g., "Messages: 116–133").
   - **Gist** — 2-4 sentences. What happened, what was decided, what's the takeaway.
   - **Key Turns** — Bulleted list of pivotal messages. Format: `**NNN–NNN (topic):** one-line description`. Focus on decisions, shifts, and conclusions — not every exchange.
   - **Cross-references** — If sibling segments or parent directories exist, link to them. How does this branch depend on or enable others?
   - Note any sub-fork directories (they'll be digested separately).

## Digesting a whole tree

When digesting a raw conversation export with forks:

1. **Understand the tree structure first.** Directory names and nesting encode the fork topology. The orchestrating agent can infer parent-child relationships and branch context from this structure alone — no need to read message content yet.

2. **Launch all branches in parallel.** Every directory gets its own agent (or batch small forks into shared agents). Inject context into each agent's prompt — what the parent branch established, where this fork sits in the tree. This is faster than sequential approaches because nothing waits.

3. **Add inherited context breadcrumbs** in a second pass, after all agents complete:
   ```
   > **Inherited context (see [../SUMMARY.md](../SUMMARY.md)):**
   > [2-3 line summary of what ancestor branches established]
   ```

4. **Validate.** "Would an agent reading only the SUMMARY.md files get a holistic grasp?" If not, add missing inherited context.

### Batching

- Small forks (2-3 files) can share an agent.
- Large branches (10+ files) each get their own.

### The root summary

The root directory is special — it contains both the trunk messages and all fork directories. Its SUMMARY.md should include:
- The overall conversation arc
- A tree diagram showing the full fork structure
- The canonical/productive path marked (if one exists)

Write the root summary last, after branches are done, so it can reference their summaries.

### Agent hygiene

Digest agents should be lightweight. They read message files and write a summary — nothing else. Instruct them to skip project configuration, skill files, or other context-heavy setup that would slow them down or waste tokens.

### Agent prompt template

```
Read all .md files in this directory (NOT subdirectories) and write a
SUMMARY.md for this conversation branch.

Directory: <path>

Context: <where this branch sits in the conversation tree, what the
parent branch established>

Use `tail -vn9999 *.md` to read top-level files only.

Note any sub-fork directories that exist — they will be digested
separately.
```

## Style

- Write for a latecomer who has 30 seconds. Lead with what matters.
- Use the participants' own terminology — don't rename concepts.
- Distinguish between proposals and decisions. If something was proposed but not confirmed, say so.
- If existing SUMMARY.md files are available (e.g., from a prior digest pass), reuse good language rather than paraphrasing worse.

## What this is NOT

- Not segmentation by topic (that's `chatlib-segment`)
- Not value assessment (that's `chatlib-assess`)
- Not artifact extraction (that's `chatlib-extract`)

# chatlib-triage

Quickly assess whether files or message types are relevant to a given audience.

## When to use

Early in the process, when facing a mixed dump of files and needing to decide what to keep, skip, or investigate further. Lighter-weight than `chatlib-assess` — this is about format/type relevance, not semantic value.

## Input

A conversation directory with mixed file types (.json, .md, directories, etc.) and a stated audience (human reader, coding agent, documentation agent, etc.).

## Procedure

1. **Sample each file type** — Read 1-2 representative files of each format/type present.
2. **Determine content relationship** — Are .json and .md files redundant? Is one derived from the other? Is useful metadata only in one format?
3. **Assess per audience:**
   - **Human reader:** Can they get what they need from .md alone?
   - **Coding agent:** Do they need message IDs, timestamps, parent pointers from .json?
   - **Documentation agent:** Do they need the full conversation tree structure?
4. **Report** which file types are relevant, redundant, or skip-worthy for the stated audience. Be specific about what each type contains.

## Output

A recommendation to the user (not a file). Format:
- For each file type: keep / skip / investigate further
- Reasoning in one sentence

## What this is NOT

- Does not assess semantic value of individual messages (that's `chatlib-assess`)
- Does not create or modify files
- Does not require reading all messages — sampling is sufficient

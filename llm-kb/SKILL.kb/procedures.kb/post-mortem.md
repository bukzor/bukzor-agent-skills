# Procedure: post-mortem (capture)

Dump a failing or notable session into a case-study before context
decays. Capture only.

## Goal

Preserve first-person narrative and verbatim user signals before
context loss. Speed beats alignment.

## When to use

- After failed or partially-failed task with recurring failure mode.
- User-requested debrief.
- Context over 200k with reusable lessons (see
  `../must-read/when/context-over-200k-tokens.md`).

## Steps

1. **Verbatim signals first.** Paste user corrective quotes verbatim
   into the new case-study file. No paraphrasing.

2. **Narrative around the quotes.** First-person, chronological where
   useful. What the task was, what went wrong, what the user had to
   correct.

3. **Perceived failure-mode aliases in frontmatter.** Writer's
   perceptions, not canonical. Don't look up canonical names yet.

   ```yaml
   ---
   date: $DATE
   failure-modes:
     - <perceived-alias>
   ---
   ```

## Outputs

- A file in the project's `case-studies.kb/` collection, named
  `$DATE-NNN-$SLUG.md` (date of incident, zero-padded ordinal,
  kebab-case slug). Contains frontmatter, narrative, verbatim quotes.
  No `status:` field (absent = `raw`).

If the project lacks a `case-studies.kb/`, create one — a single-entry
collection is valid. Stub `case-studies.kb/CLAUDE.md` per the llm-kb
pattern.

## What this prevents

Loss of verbatim signals to context decay.

## Related

- The project's reconcile-case-study procedure -- the editorial pass
  that produces distilled entries from this raw capture. (For this
  skill's own methodology kb, see
  `../../docs/dev/procedures.kb/reconcile-case-study.md`.)
- The project's case-study concept definition. (Skill-internal:
  `../../docs/dev/concepts.kb/case-study.md`.)

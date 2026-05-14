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
  `../../../SKILL.kb/must-read/when/context-over-200k-tokens.md`).

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

- `../case-studies.kb/$DATE-NNN-$SLUG.md` with frontmatter, narrative,
  verbatim quotes. No `status:` field (absent = `raw`).

Filename: `$DATE-NNN-$SLUG.md` (date of incident, zero-padded ordinal,
kebab-case slug).

## What this prevents

Loss of verbatim signals to context decay.

## Related

- `reconcile-case-study.md` -- the editorial pass that produces
  distilled entries from this raw capture.
- `../concepts.kb/case-study.md` -- concept definition.

# Concept: case-study

A first-person incident narrative naming the failure modes, principles,
and methodologies the writer perceives, with verbatim user corrective
signals preserved. Raw-but-coherent input to a reconciliation pass; not
authoritative on the distilled items it names.

## Shape

Bundles four kinds of content in one file:

1. Narrative of what happened (first-person, chronological where useful).
2. Named failure modes with recognition prompts.
3. Distilled principles and methodologies the writer perceived.
4. Verbatim user corrective signals preserved as quotations.

Captured before context expires; "best-effort coherent reconciliation
the writer can produce in this session" is the standard -- not
"comprehensively reconciled with the kb."

## Authority

- Authoritative on: the narrative itself, and the verbatim user
  signals.
- NOT authoritative on: failure-mode aliases, procedure shape,
  principle phrasing. Those get reconciled by
  `../procedures.kb/reconcile-case-study.md`.

Future readers should treat the case-study's perceived items as **seeds
for re-distillation**, not as truth-of-record. The truth-of-record for
distilled items lives in the corresponding `.kb/` collections.

## Filename convention

`$DATE-NNN-$SLUG.md`:
- `$DATE` is `YYYY-MM-DD` of the incident.
- `NNN` is zero-padded ordinal within the date (`000`, `001`, ...).
- `$SLUG` is kebab-case descriptor of the incident.

## Distinguished from

- A devlog entry -- usually third-person, design-focused, session
  outcome rather than failure analysis.
- A debrief -- could be longer-form, multiple incidents; a
  case-study is one incident.
- A journal entry -- personal/temporal; case-studies are about
  reusable lessons.

## See also

- `../../../SKILL.kb/procedures.kb/post-mortem.md` -- the procedure that produces case-studies.

TODO: expand with the distinguishing examples once we have a second
case-study to compare against.

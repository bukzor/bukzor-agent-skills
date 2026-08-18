---
why:
  - ../030-requirements.kb/dated-records-are-primitive.md
---

# Class: Record

Dated, append-mostly collections instantiating the spec's
dated-record primitive. Sub-types, each a schema plus a page of
conventions:

- **incident** (v1 case-study): narrative of an instructive failure,
  feeding distillation.
- **migration**: a convention change; ships its doctor check per
  `validators-outlive-migrations`.

v1's devlog (session log) does not survive as a sub-type here: the
residue test (`llm-design-kb/principles.kb/test-the-residue-not-the-bundle.md`)
found every section of a real devlog entry already better-homed
elsewhere — narrative-of-failure → incident, decisions/alternatives →
design entries, conventions established → principles/procedures, open
items → task entries — leaving no content type this class alone would
hold, and no nameable read-back moment
(`writes-name-their-read-back.md`'s own motivating counter-example).

> [!QUESTION] Reopened 2026-08-18: does the third-place definition survive the residue test?
> The user's definition of the devlog
> (`llm-collab/references.kb/file-types.kb/devlog.md`: the narrative
> third place for what fits neither code comments nor commit
> messages) names a read-back moment the residue test found missing
> -- "what were the concerns surrounding this change?" -- and its
> content (discussion, concerns) is not obviously held by the
> better-homes above (an incident is a failure; a design entry is an
> outcome). Re-run the residue test against that definition before
> this cut lands. `ADR_FATE`
> (`docs/dev/design.claims.kb/does-the-ledger-subsume-the-adr.md`)
> leans on the answer.

One class definition carries what v1 spread across `llm-kb`
(case-studies, migrations) and their duplicated generator scripts.
`kb new incident --title …` and kin replace the per-type scripts.

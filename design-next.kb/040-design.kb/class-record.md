---
why:
  - ../030-requirements.kb/dated-records-are-primitive.md
---

# Class: Record

Dated, append-mostly collections instantiating the spec's
dated-record primitive. Sub-types, each a schema plus a page of
conventions:

- **session log** (v1 devlog): what a diff can't capture — reasoning,
  rejected paths, conventions established.
- **incident** (v1 case-study): narrative of an instructive failure,
  feeding distillation.
- **migration**: a convention change; ships its doctor check per
  `validators-outlive-migrations`.

One class definition carries what v1 spread across `llm-collab`
(devlog), `llm-kb` (case-studies, migrations), and their duplicated
generator scripts. `kb new incident --title …` and kin replace the
per-type scripts.

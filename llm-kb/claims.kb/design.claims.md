---
label: KB_DESIGN
standing: agent
ontology:
  - collection
  - roll-up
  - corpus
  - canonical
  - stub
  - guard
  - positional binding
non-claim-tokens:
  - HOME
  - SKILL
  - YAML
stale-when: frontmatter stops being where a file's data lives -- a harness that carries per-file metadata out of band leaves positional binding answering a question nobody asks
---

# llm-kb's design, as a ledger

Design commitments of the kb pattern itself: what binds a file to a
schema, what a roll-up is, what counts as corpus, and what runs to keep
those true. One claim per file, label and standing in frontmatter
(`Skill(llm-claims-kb)`). Argue with a claim by editing its file.

Division of labor with the siblings: `SKILL.md` states the settled
pattern to a reader who wants to use it; `migrations.kb/` records a
transformation with a scope and a status; this ledger holds what is
committed-but-contestable and what is still open. A commitment that
reached `SKILL.md` and nobody disputes needs no claim here.

## Scans

```bash
grep -rH '^standing:' llm-kb/claims.kb/design.claims.kb/
llm-claims-kb/bin/llm-claims-kb-graph llm-kb/claims.kb/design.claims.kb
```

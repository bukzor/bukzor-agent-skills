---
label: GOVERNANCE
standing: agent
why:
  - a-plain-directory-is-a-key-prefix.md
---

# Schema Resolves Through Plain Directories

Schema and `CLAUDE.md` for a file inside a plain directory resolve by
walking up through plain directories to the nearest `.kb/`; the
positional binding `X.kb/ <-> X.jsonschema.yaml` is unchanged, it just
reaches deeper. Transparency is only real where every tool walks --
`llm.kb-validate`, link checking, schema lookup, and `llm-must-read-ls`
-- and the owner reports that work as partially done, to be finished
as breakage is met.

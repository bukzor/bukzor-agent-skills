---
why:
  - spec-cited-never-restated
  - filesystem-as-database
  - dated-records-are-primitive
---

# Layer 0: The kb Spec

A short RFC plus schemas defining the file format and nothing else —
no procedures, no behavior, no teaching:

- **Collection**: `$CATEGORY.kb/` of homogeneous one-item files;
  `ls` is the index.
- **Entry**: markdown, optional schema-validated frontmatter.
- **Synthesis file** (`$name.md`, sibling of `$name.kb/`): the
  roll-up of its collection, never its index (`ls` is the index).
- **Maintenance guide** (`CLAUDE.md`): what belongs, never what's
  present.
- **Dated record**: `YYYY-MM-DD-NNN-title` identity, newest-wins,
  append-mostly — promoted to a first-class primitive with one
  definition.
- **Linked node**: one entry is one node; typed frontmatter arrays
  declare edges to other nodes by cross-reference path; elaboration
  is a sibling `$name.kb/`, whose synthesis file is the node itself.
  One shape, many edge vocabularies — see `genre-epistemic.md`.
- **Cross-references**: see `cross-reference-notation.md`.
- **Directives**: `requires:` frontmatter lists files that must be
  read before acting on the bearer's content — the only load
  directive.
- **Naming**: kebab-case, name-signals-content, ordering prefixes.

Everything downstream cites the spec by section; the spec never
appears restated in a skill, rule, or CLAUDE.md. A meta-schema
validates genre schemas so genres extend the spec without forking it.

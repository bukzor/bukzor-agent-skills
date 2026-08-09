# After Distilling From a Raw Source

You just produced distilled entries (failure-modes, principles,
procedures, concepts, glossary) from a raw source -- a case-study,
devlog, ADR, or incident report.

## Distilling-specific actions

- Back-link aliases canonically -- if distillation produced canonical
  names that differ from the raw source's provisional aliases, update
  the raw source's frontmatter and prose. The raw source remains
  authoritative on narrative; the distilled entries are authoritative
  on alias.
- Completeness vs source -- list every item the raw source names.
  For each, verify a distilled entry exists or you've explicitly chosen
  to defer with a TODO. None should be silently dropped.
- Cross-link siblings -- if a new distilled entry overlaps an
  existing one, add `see-also:` or merge. Two entries describing the
  same thing under different names is the failure mode this prevents.

## Generic audits

Distillation writes and edits multiple kb files at once -- run the
full sweep: `../../procedures.kb/run-self-audits.md`.

---
label: STATUS_ENUM
standing: open
---

# `status:` Is Four Enums Under One Name

`status:` appears across the corpus with incompatible vocabularies. A
todo item takes `open|deferred|blocked|not-started|done|abandoned|
duplicate|template`; a migration takes `tentative|planning|started|
in-progress|complete|verified|archival`; a discourse-graph node takes a
truth-valued word; and loose files carry `active`, `exploring`,
`complete` from no vocabulary at all.

Migration `2026-08-21-002` hit this and stopped, deliberately:
"`status` alone is four incompatible enums under one name. Its own
canonical is an open question." It excluded the whole
`status`/`blocked-on`/`superseded-by` lifecycle trio rather than pick a
winner.

The live cost is small and constant: files carrying a word from the
wrong vocabulary fail validation one at a time, and get rewritten one
at a time, which is a rename that teaches nobody anything.

The question is whether these are one concept with four dialects --
in which case there is a canonical to write and three schemas to point
at it -- or four concepts sharing a spelling, in which case the fix is
four names and no canonical at all. Nobody has argued it either way.

---
label: SELECTION_CONFLICT
standing: user
why:
  - a-file-may-name-its-own-schema.md
authority: "user, 2026-08-22: 'and make it an error for this to disagree with the .kb schema-selection convention / it's not an error if the two agree'"
---

# Explicit and Positional Selection Must Agree

Where a file both names a schema and sits where the convention binds
one, the two must be the same schema. Disagreement is an error the
validator reports.

Agreement is not an error, and is not redundancy worth removing: a
file that says out loud what its position already implies is
documentation, and it is what makes the file survive being moved.

This is what keeps the opt-in from becoming a second, competing
binding system. There is one binding; an explicit selector either
restates it or is wrong.

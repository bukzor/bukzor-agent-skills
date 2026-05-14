# When a New Entry Needs Cross-Refs That Don't Exist

You're writing a new entry that names other entries by relative path --
`mitigated-by: ../procedures.kb/foo.md`, `see also ../bar.md`, prose
references -- and one or more of the targets doesn't exist yet.

**Stub the missing targets.** See
`../../procedures.kb/stub-missing-entry.md` for the procedure, including
cascade bounding.

The key constraint: cap at one level deep per session. The cascade
trap is real -- a new failure mode wants a mitigation procedure, wants
a principle, wants a concept, wants a glossary entry. Stop at one
level; deeper TODOs become notes inside the stubs.

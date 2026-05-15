---
last-updated: "2026-05-13"
---

# self-audit -- proactive quality checks for kb work

Each file in `self-audit.kb/` is one quality check: a question to ask
of your own recent work plus a recovery when the answer is bad. Audits
are reusable -- triggers in `../must-read/` link to them, and you can
browse them directly any time you want a proactive pass.

## When to consult

- **After adding new kb content** -- `ls -RF self-audit.kb/` and scan
  for audits whose names match the work you just did.
- **Before committing** -- `must-read/before/marking-kb-work-done.md`
  aggregates the audits that matter at that juncture.
- **When a `must-read/` trigger fires** -- the trigger links to the
  audits relevant for that juncture.

## Naming convention

Filenames compose with the directory: `self-audit.kb/X.md` reads as
"self-audit X". Each filename names the thing audited, kebab-case, no
`audit-` or `scan-` prefix (the verb is implied by the directory).

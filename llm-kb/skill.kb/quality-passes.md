# quality-passes -- proactive quality checks for kb work

Each file in `quality-passes.kb/` is one quality check: a question to ask
of your own recent work plus a recovery when the answer is bad. Passes
are reusable -- triggers in `./must-read.kb/` link to them, and you can
browse them directly any time you want a proactive pass.

## When to consult

- **After adding new kb content** -- `ls -RF quality-passes.kb/` and scan
  for passes whose names match the work you just did.
- **Before committing** -- `./must-read.kb/before/marking-kb-work-done.md`
  aggregates the passes that matter at that juncture.
- **When a `must-read.kb/` trigger fires** -- the trigger links to the
  passes relevant for that juncture.

## Naming convention

Filenames compose with the directory: `quality-passes.kb/X.md` reads as
"quality pass X". Each filename names the thing passed over, kebab-case, no
`pass-` or `scan-` prefix (the verb is implied by the directory).

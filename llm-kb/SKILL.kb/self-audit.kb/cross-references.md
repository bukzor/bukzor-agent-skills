# Self-audit: cross-references

Every relative reference in a kb file -- prose paths like a relative
`foo.md` mention, frontmatter paths like `mitigated-by:`, `see-also:`
links -- must resolve to an existing file. This audit catches dangling
references before they're committed.

## Goal

No dangling references in committed kb content. Stubs count as resolved;
missing files do not.

## Procedure

Run `../../bin/llm.kb-validate-links <path>`
first -- it mechanically checks known frontmatter link fields (`why`,
`depends`, `source`, `sources`, `candidate-resolutions`, `conclusion`,
`premises`, `resolved`) and backtick-wrapped, dot-slash-prefixed relative
body links. Not wired into `bin/llm.kb-validate` yet -- see
`../../.claude/todo.kb/2026-06-03-000-validate-path-references.md` for
status.

The script only catches `../`/`./`-prefixed backtick paths in known fields.
For each file you touched, additionally scan by hand for what it misses:

- Bare relative paths without a `./`/`../` prefix (e.g. `foo.kb/bar.md`).
- Markdown link syntax: `[text](path)`.
- Frontmatter paths in fields other than the ones listed above (e.g.
  `mitigated-by:`, `see-also:`, `eliminated-by:`).

For each found path, verify the target exists.

## Recovery

For each missing target, choose one of:

1. Fix the path -- the reference points at the wrong place.
2. Stub the target -- the reference points at the right place but
   the target hasn't been written yet. See `../procedures.kb/stub-missing-entry.md`
   for the stubbing procedure.
3. Drop the reference -- the reference is incorrect and shouldn't
   exist.

If a stub introduces further dangling references, **cap at one level
deep this session**. See `../procedures.kb/stub-missing-entry.md` for the
cascade-bounding procedure.

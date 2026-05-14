# Self-audit: cross-references

Every relative reference in a kb file -- prose paths like `../foo.md`,
frontmatter paths like `mitigated-by: ../bar.md`, `see-also:` links --
must resolve to an existing file. This audit catches dangling references
before they're committed.

## Goal

No dangling references in committed kb content. Stubs count as resolved;
missing files do not.

## Procedure

For each file you touched, scan for:

- Markdown prose links: `[text](path)` and bare paths in prose.
- Frontmatter paths: anything that looks like a relative path (e.g.
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

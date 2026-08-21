# Self-audit: collection homogeneity

## Goal

Every file in a `.kb/` describes the same type-of-thing -- the type
defined by the collection's CLAUDE.md "What belongs here" rule.

## Procedure

Open the `.kb/` you touched. For each file, ask:

> Same type-of-thing as every other file in this collection?

Mixed types is the failure -- e.g., `decisions.kb/` holding both a
decision record and a roadmap plan.

If you cannot articulate the type-of-thing, run
`claudemd-completeness.md` first.

## Recovery

Split mixed types into sibling collections, named for the type each
holds. Update `What does NOT belong here` in both CLAUDE.md files to
keep the boundary explicit.

## Related

- `filename-discipline.md` -- filenames should reinforce the type.

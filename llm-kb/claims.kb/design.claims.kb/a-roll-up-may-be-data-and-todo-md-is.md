---
label: ROLLUP_FIELDS
standing: user
authority: "user, 2026-08-22: 'i like these fields. i think they deserve to live. this is the one case where X.md does not participate in X.jsonschema is false.'"
---

# A Roll-Up May Be Data, and todo.md Is

The default holds: a roll-up is prose about a collection, not a member
of one, so it carries no frontmatter. What falls is the claim that this
is *universal*.

`.claude/todo.md` is the counterexample, 47 times over. Its
`cost-benefit-sweh:` is a real aggregate -- timebox, benefit-2w and
cost-of-delay-2w, each with `@value`, `rationale` and `confidence` --
scored over a whole project's backlog, on 33 of those files. It is data
under a shape, and the shape is already written down in the sibling
`todo.jsonschema.yaml` that governs the items it summarizes.

Three fixes were considered and lost. Deleting the fields destroys 33
considered assessments. Pushing them down into `todo.kb/` fails because
what they score is the `- [ ]` checkboxes in the file, not the files in
the collection. Minting a collection of project backlogs to make the
aggregate a member of something invents a structure to satisfy a rule.

What the default lacks is not an exception. It lacks an opt-out.

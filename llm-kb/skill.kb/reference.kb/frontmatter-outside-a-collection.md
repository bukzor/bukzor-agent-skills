# Frontmatter Outside a Collection

Frontmatter is data, and data belongs under a schema. Unchecked data
drifts -- a key that used to be a list becomes a string, a date grows
quotes, a field is renamed in nine files and missed in the tenth, and
nothing says so. A validator that reports ✅ for a file it never checked
teaches you to distrust every ✅ it prints, so a file it cannot check is
an error rather than a pass.

Where the lookup reaches today is two places: a file inside `X.kb/` is
checked against `X.jsonschema.yaml` beside that directory, and `X.md`
beside `X.kb/` is checked against that same schema where the schema
exists. Read that as the current reach, not as the rule -- a file the
lookup misses is not thereby exempt, it is a file to bring within reach.

Three ways out, best first.

## Push the file down into a collection

Right when the file is one of several things of a kind, or will be.
Create `X.kb/`, move the file into it, and write `X.jsonschema.yaml`
beside the directory. `creating-a-new-kb.md` covers the rest.

The move is also the honest test of whether the frontmatter was data: if
no sibling would ever carry the same keys, the file is not a member of
anything, and one of the other two resolutions applies.

## Rename the parent to `X.kb/`

Right when the directory already holds a homogeneous set and only the
suffix is missing -- a `procedures/` of procedures, an `evidence/` of
evidence. `git mv procedures procedures.kb`, write
`procedures.jsonschema.yaml` beside it, and every member is checked from
then on.

Cheaper than it looks: the members do not move, so relative links between
them survive. Links *into* the collection from outside do not -- sweep
them in the same commit.

## Remove the frontmatter

Last resort, and legitimate only where the keys were never data: a
`title:` that restates the `#` heading, an editor's leftovers, a field
one agent invented and nothing ever read. Deleting those is a real
subtraction.

Deleting frontmatter that something reads is not a resolution, it is the
defect with the alarm switched off. If a key is load-bearing, it wants a
schema, which means one of the two resolutions above.

## The roll-up slot is under its collection's schema

`$CATEGORY.md` rolls up `$CATEGORY.kb/`, and `$CATEGORY.jsonschema.yaml`
governs it too, when it carries frontmatter and the schema exists. The
claims ledger is what forced that reach: a ledger's `X.md` beside
`X.kb/` is not only the roll-up but the ledger's defining claim -- a
member-shaped thing -- and `Skill(llm-claims-kb)`'s one claim schema
governs theories and ordinary claims alike, so the collection's schema
is exactly its law.

Where member and roll-up genuinely are different kinds, the schema says
so -- a `oneOf` naming both shapes -- or the roll-up carries no
frontmatter and is prose, which no schema is asked about. Frontmatter
the schema was never taught is still the ordinary error, not a pass: a
roll-up is welcome to be prose, but its data is not exempt for being
one level up.

## The two files that are skipped, and why that is not a fourth way out

`CLAUDE.md` and dotfiles like `.template.md` are skipped outright: both
are *forced* to live inside the collection they describe, so both are
files in a `.kb/` that cannot be members of it. Nothing else qualifies.
The test is a forced location, not an inconvenient verdict.

A file that merely sits outside every collection fails that test and
gets the ordinary error, whoever owns its keys. A skill's `SKILL.md` is
the case worth stating: its `name` and `description` are Claude Code's
format, so llm-kb defines no schema for them -- and still reports that
no schema governs them, because those are two different questions.
Saying "not mine to define" is honest; saying nothing about a file you
were handed is not.

The resolution there is neither a schema nor an exemption: don't hand a
kb validator a file that isn't kb data. If those keys want checking, the
tool that owns the format is where the check belongs.

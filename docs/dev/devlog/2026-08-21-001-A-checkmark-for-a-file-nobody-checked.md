# Devlog: 2026-08-21 — A checkmark for a file nobody checked

## Focus

`llm.kb-validate llm-kb/SKILL.md` printed ✅. It had validated nothing.
Closing that took one line of code, one reference doc, and — the part
that took the thinking — a rename, because the reason the hole was hard
to close was a naming coincidence nobody had named.

## The defect

`validate_file` ended its schema lookup with `return []`, and `[]` is
what a clean file returns. So the function said "no schema applies" in
exactly the words it used for "this passed", and the caller printed a
green checkmark either way. Every ✅ in the output was worth slightly
less than it looked.

Two populations reached that line: files outside any `.kb/`, and files
inside a hive partition (`year=2026/`), whose parent does not end in
`.kb` even though a collection plainly governs them. The second is a
lookup that should have walked up one level and never did; there are no
partitions in the fleet today, so it had never been observed.

## The rename came first, and it was not cosmetic

The obvious fix for a top-level `X.md` is to hand it `X.jsonschema.yaml`
— the schema already sitting beside it, governing `X.kb/`. Tested
against the corpus, that passes for eleven files and fails for four,
and the split is not noise: it passes exactly where the domain says the
parent is a member. A claim ledger says so outright ("a theory is a
claim like any other"), so `X.claims.md` fits the claim schema. A
`decorations.jsonschema.yaml` that opens with *"Schema for decoration
**items**"* says the opposite, and its `decorations.md` roll-up fails
it. The rule was never about the name; it was about whether the domain
identifies parent with member.

`SKILL.md` is where that shows worst. Its frontmatter is `name` and
`description` — Claude Code's contract, twenty-one times out of
twenty-one. The one frontmattered file in any `SKILL.kb/` carries
`last-updated`. **The two populations share no key at all**, so no
schema could have served both, and yet `SKILL.jsonschema.yaml` sat there
looking like the schema for `SKILL.md` because that is what the `X.md`
↔ `X.kb/` convention means everywhere else.

So: `git mv SKILL.kb skill.kb` across six skills, and
`SKILL.jsonschema.yaml` → `skill.jsonschema.yaml` with it, since the
lookup rule is `X.kb/` → `X.jsonschema.yaml`. The structural guarantee
is that `skill.md` does not exist: `skill.kb/` demonstrably has no
synthesis file, and nothing suggests the schema reaches upward.

Ninety-four files. The live sweep included the `ls -RF
skill.kb/must-read.kb/` bootstrap that six `SKILL.md` files execute on
load — a stale path there fails a skill's first action. `devlog/` and
`adr/` kept the old name, and so did the `[x]` lines of
`llm-kb/.claude/todo.md`: those record actions that happened under the
old name, and rewriting them would make them describe an event that
never occurred.

## What the error had to say

The message names the situation and spends the rest of its words on an
address, because the resolutions do not fit in an error line:

- push the file down into a collection, with a schema;
- rename the parent to `X.kb/`, with a schema;
- delete the frontmatter — legitimate only where the keys were never
  data, and never as a way to quiet the alarm.

`references/frontmatter-outside-a-collection.md` argues each one, and
carries the reason a synthesis file gets no exemption: a member and a
summary of the members are different kinds, and one schema serving both
would have to require each one's fields of the other.

## A change with a deliberately small blast radius

The walk descends only into `.kb/` directories, where a schema path is
always computed. So the fleet run is unchanged — 391 files, 0 errors —
and the new error fires only where a file is named on the command line.
That is the honest scope: 47 tracked files carry frontmatter no schema
reaches (21 `SKILL.md`, 14 beside their own `.kb/`, 10 `devlog`/`adr`,
2 other), and widening the walk to reach them turns all 47 red at once.
Each population needs its resolution first. Filed, with the counts.

`SKILL.md` is the population with no resolution available: Claude Code
requires those keys at that exact path, so it cannot move down, its
parent cannot be renamed, and the keys cannot be dropped. It wants a
fourth lookup rule — match the reserved filename against a schema
llm-kb owns — which would also check the two things nothing checks
today: that `name` equals its directory, and that `description` reads
as the discovery text it actually is.

## What the verification had to be

Both new assertions were driven to red first and failed with the
distinctive symptom — `AssertionError: []`, the silent pass itself. The
third test asserts the *absence* of the new error for a file with no
frontmatter at all; it passed on first run, so the guard was removed to
watch it fail and restored.

One thing worth knowing about this repo's tooling: the `llm.kb-validate`
on `PATH` came from a sibling project's venv and is a non-editable
install, so it kept reporting the old behavior after the source changed.
`uv run` from `llm-kb/` is what exercises the working tree.

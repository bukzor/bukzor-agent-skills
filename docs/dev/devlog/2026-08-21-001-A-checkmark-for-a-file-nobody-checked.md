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

## The population that wasn't a population

`SKILL.md` looked like the hard case: Claude Code requires those keys at
that exact path, so it cannot move down, its parent cannot be renamed,
and the keys cannot be dropped. I proposed a fourth lookup rule — match
the reserved filename against a schema llm-kb ships — on the grounds
that the keys are checkable and nothing checks them.

Wrong, and the owner named it in a sentence: *SKILL.md is outside the
purview of llm-kb, and now it's clearly so.* The error was inferring
jurisdiction from checkability. `name` and `description` are Claude
Code's format, stipulated where that format is defined; llm-kb shipping
a schema for them is the same overreach as a local schema forking a
canonical one, which this repo spent the previous day undoing.

So `SKILL.md` joins `CLAUDE.md` on the not-kb-data list — skipped, not
counted, no verdict either way — and the 47 drops to 26. Declining
jurisdiction is not the silent pass this session removed: that one
counted a file and printed ✅ over it, while this yields no result at
all and the tail reads `0 files`.

The rename is what made the ruling visible. While `SKILL.jsonschema.yaml`
sat beside `SKILL.md`, the file looked like llm-kb's business. Once the
schema is `skill.jsonschema.yaml` and there is no `skill.md`, there is
nothing left suggesting llm-kb ever reached that far.

## What the verification had to be

Both new assertions were driven to red first and failed with the
distinctive symptom — `AssertionError: []`, the silent pass itself. The
third test asserts the *absence* of the new error for a file with no
frontmatter at all; it passed on first run, so the guard was removed to
watch it fail and restored.

The `llm.kb-validate` on `PATH` reported the old behavior throughout,
because `meta-reasoning`'s venv had `llm-kb` and `llm-claims-kb` as
*copied* path dependencies. A path dependency that isn't editable is a
snapshot wearing a source tree's name — the whole reason to point at a
directory is that it gets edited. Both are `editable = true` now, and
the binary on `PATH` tracks the working tree.

Worth noticing as a class: for most of this session the tool that
verifies the work was itself stale, and nothing said so. It is the same
failure the session set out to fix, one level up — a green result whose
provenance nobody checked.

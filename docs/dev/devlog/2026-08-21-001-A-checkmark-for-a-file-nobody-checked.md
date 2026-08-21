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

The correction I then made was wrong in the mirror image: I put
`SKILL.md` on the skip list beside `CLAUDE.md`, so naming it printed
`0 files, 0 errors`. The owner caught that too, with the test that
should have been obvious — *CLAUDE.md is exempted because it needs to
appear in `.kb/`, where it's a file but not a participant. The same
isn't true of SKILL.md.* The skip list's members are there because
their **location is forced**; a file merely outside every collection
fails that test.

Both errors are one error made twice. *Whose keys are these* and
*should the tool report on this file* are independent variables, and I
kept answering them with a single move — first claiming jurisdiction,
then disclaiming existence. Separated, the answer is neither: llm-kb
defines no schema for `SKILL.md`, and says so out loud. `1 files, 1
errors`. The resolution is in a third place entirely — don't hand a kb
validator a file that isn't kb data.

This is the fused-variable trap from
`must-read.kb/when/redesigning-something-that-already-exists.md`, met
in the wild: a choice that arrived as two options, each losing
something worth keeping, because two questions had been welded into
one.

The rename is what made the first ruling visible. While
`SKILL.jsonschema.yaml` sat beside `SKILL.md`, the file looked like
llm-kb's business. Once the schema is `skill.jsonschema.yaml` and there
is no `skill.md`, nothing suggests llm-kb ever reached that far.

## The blast radius was small because the walk was

The scope above is honest but it was also the finding, unrecognized: the
walk descends only into `.kb/`, so `llm.kb-validate docs/dev/design.claims.kb`
reported `37 files, 0 errors` without ever opening `design.claims.md` —
the file that, by llm-claims-kb's own rule, *defines the theory the
collection holds*. A ledger certified clean with its root claim unread.

Three independent sources make the roll-up part of the collection rather
than a document beside it: llm-kb's anatomy lists `$CATEGORY.md` inside
the pattern, `skill.kb/self-audit.kb/synthesis-file-value.md` audits it
as kb work, and a ledger's `X.md` is a claim like any other. So the walk
takes `X.md` with `X.kb/`, stopping when the parent is itself a `.kb/` —
a nested roll-up is already a member of the collection above it.

Thirteen roll-ups now report `No schema found` in the ordinary run
rather than only when named. The live tree reads `540 files, 13 errors`,
and that is the true state.

## Folding is a failure mode with a procedure against it

The owner's counter to the reach argument was that these files are not
"unchecked" — name one and the tool reports on it. True, and my word was
wrong: I had used *unchecked* to mean *no schema applies*, which is the
exact conflation `return []` used to make. I reverted to pre-session
vocabulary and then reasoned from it.

Then I withdrew the whole position — including the half the counter
never touched. The position had two independent claims welded together
again: that the walk should **reach** `X.md`, and that `X.md` should be
**paired** with `X.jsonschema.yaml`. The objection landed on the
phrasing of the second. I dropped both.

`must-read.kb/before/retracting-or-conceding-a-claim.md` exists for
precisely this, and I did not read it before conceding. Its Arbiter role
has one job — check whether Skeptic's concession was earned — and the
concession here was not: Skeptic had a surviving argument (the walk does
not reach them) that was never voiced. Advocate/Skeptic without Arbiter
is agreement with extra steps.

The fused-variable count for one session: whose keys are these vs.
should the tool report on the file; current reach vs. what deserves
checking; reach vs. pairing. Three, all the same shape, all resolved by
separating rather than choosing.

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

One more of the family, found by tripping over it: `validate_paths` had
three branches and no `else`, so a path that is neither collection,
directory, nor file fell out of the walk silently. A three-path
invocation reported `2 files` and never mentioned that the third was
mistyped — in the very command run to settle an argument about
trustworthy output. `validate_file` had carried a `File not found`
message all along that nothing could reach.

# Sensatim, JUSTIF_ORDER, and rules that fire at write time

The owner's word is quoted **sensatim** (rather than verbatim), a rule
about where writing rules live, and a history rewrite that removed the
misstep this entry would otherwise narrate.

## The word

`VOICE` had said a quoted span is the owner's words "verbatim, with
typos mended and renamed labels retconned". The owner ruled the
enumeration out: it cannot be shown exhaustive, so name the category
instead. What replaced it is a condition -- *the words as typed,
silently emended only where they would now mislead* -- with the typo
and the renamed label demoted to instances, and the test handed to the
reader rather than the editor: would the unmended token transmit
something the owner did not send?

English has no positive word for that relation. It has negations (*no
material change*), phrases (*in substance*, *to the same effect*), and
the editorial pair *accidentals*/*substantives*, but no single term.
The owner supplied one: **sensatim**, on the model of *verbatim* and
Jerome's rule for translators (*Ep.* 57, *non verbum e verbo, sed
sensum de sensu*). It is a coinage, marked as such in `VOICE` --
unattested in the lexica, with *sensim* ("gradually") and late Latin
*sensatus* ("sensible") standing nearby and meaning other things.

The `-atim` suffix does the work: it is distributive, and names the
unit at which fidelity is owed. *Verbatim* owes it word by word;
*sensatim* owes it sense by sense. (An earlier attempt at *vocatim*,
from `VOICE`'s own name, fails on exactly this -- a voice cannot be
itemized.)

One definition, in `VOICE`'s first sentence. Every other use in the
fleet writes *sensatim (rather than verbatim)* and cites the claim --
the manual, the schema's `authority.words`, and this entry.

## JUSTIF_ORDER

A fourth stance: **what is written down is owed in the order that
justifies it, not the order it was found.** Discovery order is
contingent on who searched and what they tried first; justification
order is a property of the claims. Rewriting one into the other asserts
nothing and retracts nothing.

The rule this replaced was mine and was wrong twice over: too narrow
(it banned *history*, when discovery-order residue is not only
narrative) and too strong (history is sometimes exactly what
justifies). The owner caught both. The surviving test asks whether a
passage does justificatory work -- an alternative eliminated, a
stipulation's provenance, an expiry condition -- never whether it is
historical.

## Where a writing rule belongs

`llm-claims-kb/SKILL.md` carried five bullets of notation-level writing
advice in its "Claim bodies" section. That is the wrong layer on both
axes:

- **cost**: the manual is paid in full by every session that merely
  *reads* a ledger;
- **effect**: it arrives before the agent knows it will write anything.

The evidence was this session. That section was in context from the
first tool call, and I still wrote stenographic `[!DRAFT]` callouts
twice; what corrected me was the owner, at the moment. Cold text in an
always-loaded manual is the weakest place to instill a behavior and the
most expensive place to store it.

So the bullets moved to
`llm-claims/skill.kb/must-read.kb/before/writing-a-claim.md`, which
fires when a claim is being written and already framed the reader who
was not there. Most of them landed as clauses in paragraphs that were
already there -- that file had already named the *revision scar*, which
is `JUSTIF_ORDER`'s instance for negations.

Measured after the fact, because I asserted it before measuring: the
manual loses 9 lines (-16/+7) and the trigger file gains 17. Stored text
therefore *grew* by 8 lines; what shrank is the part every reader pays
for. The commit message (`b0d3f28`) says "fourteen off, five on", which
was an estimate I should have run `git show --stat` against before
writing it down. The behavioural argument is unaffected; the token
claim, as stated there, is wrong.

`notation.kb/CLAUDE.md` had already routed instructions this way ("the
reasoning is a tax on them and the point for you"). A parallel session
reached the same placement independently the same hour, for
`NAME_LOCUS` (`583efa2`).

## Two things the ledger's own law decided

Both times I was about to file a claim, the ledger already held it:

- the three-reader test I proposed is `FRESH_READER`, user-standing,
  already written;
- and since the process-narrative rule *follows* from it, `NO_ECHO`
  forbids filing it -- "a claim earns nothing by restating its
  premises". Zero new claims where three were planned.

`SELF_CONTAINED` is the counterweight worth remembering: *under-statement
is the characteristic failure, not verbosity*. That is why the rule had
to be about the **address** of the text and not its length. Cutting
evidence causes a lookup; cutting scaffolding cannot.

## History rewrite

Two defects, both mine, corrected on the owner's word and pushed
(`--force-with-lease`):

- `93903dc` was titled "the owner's word is faithful, not verbatim" --
  a title that never became true. Reworded to state the substance its
  diff implemented, without asserting either dead word.
- `ac93ee1` argued for a placement `9e98ff0` reversed. It was squashed
  into its successor, so the over-narrow ban never appears in the log.

Seven commits became six. Every replayed tree verified byte-identical
via `git diff-tree`, the ref moved under an old-value guard, and the
parallel session's two commits replayed untouched but with new SHAs.

One near-miss worth recording: the first push failed `stale info`, and
I read it as the remote having moved. It had not. I had **fabricated a
40-character SHA** from an abbreviation instead of resolving it, so the
lease named a nonexistent object. `git rev-parse` before every lease.

## Open

Filed in `.claude/todo.md`: this session's unruled judgment calls, and
`llm-claims-kb-graph` being unrunnable in this environment
(`edgepaint` core-dumps), which silently voids the "re-run the graph
before committing" step in the rename procedure.

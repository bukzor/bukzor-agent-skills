# The scan learns the support lens; idle queue drops to one

Session: onto-review (continuing 004/005's ownership work).

## The false-idle class

"Why are we keeping idle imports?" exposed a scan blind spot: two of
the three queued imports (formalize identification<-purpose,
run<-identification) carried machine-readable support the idle scan
never read -- interior claims citing the prior's claims by
file-relative path in their own `why:` (e.g.
`identification.kb/an-identification-cashes-out.md` citing
`../purpose.kb/a-structure-earns-its-place-by-what-it-pins-down.md`).
The scan read only the vocabulary lens (words said), so support
carried at claim level looked like idleness.

User's menu: (1) convert path citations to labels + footer links,
(2) teach the scan to read path-based claim references, (3) both.
Took option 2: `why:` paths are exactly what graph and flatten
consume, so option 1 would move live edges out of the tools' view --
the opposite of the repair.

## The change

`llm-claims-kb-ownership`: new `cites_into` + `support_witnessed` --
an import is not idle when any claim in the taker's region (theory +
descendants) has a `why:` path resolving to the prior's defining
claim or into its tree. The taker's own defining claim is excluded:
its citation IS the import under adjudication, so it cannot witness
itself. `--idle` output now annotates a prior that stipulates no
words ("vacuous" idleness: such an import can never be
vocabulary-live) and says "neither lens witnessed".

Result: 1 idle of 52, down from 3. IDLE_UNDECIDABLE and IDLE_TEST
amended to match: idle now means *neither* lens witnessed; the
keep-tell is scan-read.

## The survivor, adjudicated

SCALAR (extension.kb/what-need-does-a-stored-likelihood-serve) <-
FATE (what-becomes-of-llm-discourse-graph): correctly still queued.
Its interior (HEDGE_KEEP, HEDGE_FORM) cites only SCALAR's own
defining claim and strata's data-representation -- never FATE's
tree -- and FATE stipulates no words (vacuous class). Kept by
reading: SCALAR presumes FATE's reform ruling ("the field is carried
over unchanged until they close"), and FATE's cache-vs-testimony
analysis names SCALAR as what it bears on. Support rides the arrow
alone; that is the residue the queue exists for.

Corrections taken along the way: my "FATE stipulates no words"
defense was irrelevant to the arrow's merits (it only explains why
the scan flags it); the on-disk direction SCALAR <- FATE is correct
and my earlier "SCALAR->FATE" prose was confusion, not the file.

## Convention

A cross-theory claim-level `why:` path is a normal, load-bearing way
to write support -- it is the support lens made mechanical. Do not
"fix" such citations into prose labels to appease a scan; fix the
scan.

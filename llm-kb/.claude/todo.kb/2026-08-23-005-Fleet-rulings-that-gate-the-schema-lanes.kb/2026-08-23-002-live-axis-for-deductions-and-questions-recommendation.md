# Recommendation (2026-08-23): deductions yes — adopt claims' axis with a derived-vs-declared rule; questions no — defer again

Split ruling. `deductions` has observed instances, including one the
2026-08-21 deferral's "no observed instance" was already wrong about.
`questions` has none: all 46 open questions in the fleet are genuinely
open or dead at tree level, and no author has hand-rolled a question
death marker anywhere. All facts below re-derived from live files
2026-08-23; the survey counts I inherited were treated as leads only.

## Census

| Collection | Files | Trees | Notes |
|---|---|---|---|
| `deductions.kb/` | 30 | 8 | summer .plan 5 live + 4 archived + 3 curriculum; template-py 5; chatfs 3; vim-work 5; epistemics 4; prm 1 |
| `questions.kb/` | 79 | 15 | 33 carry `resolved:`, 46 open; includes samsung's `open-questions.kb` |

## Deductions: the observed instances

All in `~/claude/summer-programming-project/2026/.plan/`, authored
2026-07-11 — so the instance *predates* the 2026-08-21 deferral; its
"no observed instance" premise was false for deductions at the time it
was stated.

| File | State | What it shows |
|---|---|---|
| `deductions.kb/why-session-zero.md` | `status: asserted`, no marking | Its `conclusion:` target `claims.kb/session-zero-agenda.md` is `live: false` + `superseded-by:`. The stranded-deduction case, live in the tree, invisible to any grep. |
| `archive.kb/deductions.kb/` (4 files) | `status: asserted`, relocated | Deduction death expressed by *moving the file*. Frontmatter says nothing; deadness lives in the path. |
| `archive.kb/.../why-pygame-zero.md` | tag `dormant`, prose "Parked, not current: why-pyxel.md carries the live argument" | `superseded-by:` hand-rolled in prose, plus a tag — a third and fourth mechanism. |
| `deductions.kb/why-pyxel.md` | live, `depends: why-pygame-zero.md` **dangles** | The relocation broke a live edge: the target moved to `archive.kb/`. Death-by-relocation corrupts the graph it was meant to inform. |
| `deductions.kb/why-crostini.md` | live, asserted | A premise reaches into `../archive.kb/claims.kb/` — a live inference resting on a spatially-retired claim, unmarked. |

One tree, four incompatible expressions (relocation, tag, prose,
nothing). That is the "fleet already hand-rolling it" condition, and the
relocation variant demonstrably breaks links. Note also that
`llm-discourse-graph/SKILL.md`'s ratified two-axis doctrine is already
stated collection-agnostically — "`status` is whether we believe a
**node**; `live` is whether it still bears on anything" — so extending
deductions aligns the schema with standing doctrine rather than
legislating anew from one tree's evidence.

**Shape:** same as claims — `live: bool` default true, `superseded-by:
path[]`, the `dependentSchemas` tie forcing `live: false` — but with a
usage rule in the description, not a new shape: `live: false` records
*declarative* retirement only (the inference retired though its premises
stand — why-pygame-zero's premises are all still asserted; it died
because the engine changed). Death *inherited* from a dead premise or
conclusion is derived, not stored: why-session-zero should be surfaced
by a checker, not hand-marked, or the boolean goes stale the day the
claim's marking changes. No such checker exists today —
`llm-kb/bin/llm.kb-validate-links` checks path resolution only, and the
fleet's own analysis of this exact topic
(`ideation.epistemics/deductions.kb/path-breakage-propagates-retraction.md`)
observes that flag propagation "falls back to a walker that does not
exist." The walk is trivial (conclusion/premises are frontmatter paths);
recommend it as follow-up lint work, not a gate on this ruling.

## Questions: the search came back empty

The state `live:` would express is **unresolved-and-dead**. Zero
instances found. The 46 open questions partition cleanly:

- Genuinely open, some saying so explicitly: summer's
  `session-hardware.md` — "provisional, not resolved; both candidates
  stay live."
- Dead at *tree* level: scratch.vim-work's 9 (project cold since
  2026-03), samsung-debloat's 5 (a finished `current-task.kb`). Per-node
  `live: false` across a cold tree is busywork the archive/retire move
  already covers.
- The one question actually mooted by events — summer's
  `programming-environment.md`, scoped to a tablet that left the
  project — was closed with plain `resolved:` pointing at the successor
  recommendation. The existing axis absorbed the case.

No hand-rolling either: grepping every question collection for
moot/dormant/parked/stale/superseded/abandoned finds one hit, and it is
prose about a *claim* being stale. The nearest reach is samsung naming
its collection `open-questions.kb` — liveness in the directory name, at
collection scope, which is the tree-level pattern again. The 2026-08-21
deferral reason therefore still holds for questions, verbatim: no
observed instance, and legislating its shape now would be exactly the
evidence-free extension the deferral warned against.

## The declined alternative, steelmanned

**For deductions — death-by-path, not death-by-flag.** The strongest
counter is the fleet's own deduction: path-breakage-propagates-retraction
argues a flag leaves references resolving, so nothing surfaces
dependents, while a rename/move propagates for free through link
checking. It is a real argument and it is why the checker recommendation
above matters. But today's fleet refutes its operating assumption twice:
(1) 46 of the 49 MISSING deduction edges fleet-wide are path-*style*
bugs (collection-root-relative refs in template-py, chatfs, vim-work),
so death-by-breakage would drown in noise no one triages; (2) the one
tree that practiced it broke a live edge (why-pyxel) and left four
asserted-looking deductions whose retirement is stored nowhere greppable.
A second counter: the instances are one project, and one tree is thin
ground for fleet legislation — the same conflation the deferral named.
That is why the recommendation leans on SKILL.md's already-ratified
node-general doctrine, not on summer alone; if the owner weighs the
one-tree objection heavier, the fallback is defer-with-checker, not
extend-questions-for-symmetry.

**For questions — extend now for symmetry.** Cheap, uniform, and the
absence of instances may just be a small corpus. Declined because that
is precisely ruling without evidence, and questions have a working
closure axis (`resolved:`) that absorbed the one mooted case observed.

## Verdict

**Deductions yes, questions no** (user, 2026-08-27).

`deductions` adopts claims' `live:` axis under the derived-vs-declared
rule. `questions` is deferred again, on the same ground as 2026-08-21 and
now with the census to back it: 46 open questions fleet-wide, no author
has hand-rolled a death marker, so there is nothing to record. The
trigger for reopening is the first one that appears.

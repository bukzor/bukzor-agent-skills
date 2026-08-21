---
turn: 020-conjectures.md
sent: "2026-08-10T20:42:09.938Z"
replied: "2026-08-10T20:50:08.247Z"
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:87
uuid: 0ebb653d-21e7-433e-bb6d-d6c93f1f28b0
---

# 020 -- Conjectures -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/020-conjectures.md`; the operator's
verdict on it is this file's commit message.

---

## The three itchiest places

**Itch 1 — arrows refuse semantics, yet everything computes over them.**

> "It is not an entailment relation, nothing checks it, and it is not going to become checkable later — the informality is permanent, not a stage." (`arrows-are-informal.md`)

versus, three files away:

> "Take the least fixpoint: a ring stands only on what enters it from outside... This also keeps standing cheap to compute — provenness stays an inductive predicate over the claim graph." (`cycles-are-unproven.md`)

An inductive predicate over a relation *is* a semantics for that relation. Something is being computed over arrows that officially mean nothing. What, exactly, and under what law?

**Itch 2 — one sibling pair, instanced at every grain.**

> "The plan is self-similar: the working-set/collection relation (`todo.md` : `todo.kb/`) is the spec's synthesis/elaboration relation (`$slug.md` : `$slug.kb/`), and entries inside a task kb are afforded the same steps." (`class-task.md`)

Ledger rungs, promotion tiers, trigger elaboration, decision points — all look like this pair too. Either one structure is being reinvented per class, or one structure genuinely spans them and nobody has stated its laws once.

**Itch 3 — certification transports between instances, on a prose thread.**

> "Certified by review 089 in `prototype.personal-reasoning-management`, the mechanized rung, whose `WARRANT` is this same commitment; the certification transports because the content is shared." (`a-warrant-is-a-discharged-stipulation.md`)

A claim in one repo is *bare* because a check ran in a different repo, in a different formalism, connected by nothing but a sentence. This is the single most restructuring-sensitive edge in the corpus, and it is the least mechanized.

## Conjectures (cheap sketches)

**K1. Soundness as least fixpoint.** Carrier: finite graph (claims, `why:` edges) + base map judged-or-checked. Op: valuation. Laws: monotone step operator, lfp exists, sweep = recompute. Instance: the `AB <-> CD` ring. Killer: practice demanding a `!` claim go unsound when a premise falls.

**K2. Theories as vocabulary stratification.** Carrier: theory poset, effective vocabulary V(t) = own ontology ∪ priors'. Ops: place, widen, split. Laws: V monotone; confinement; conservativity; placement = minimal admitting theory. Instance: stance → purpose → good-smells → notation. Killer: two incomparable theories both admitting a claim.

**K3. Certification transport along content spans.** Carrier: multiple K1-instances + asserted shared-content edges. Op: certify-across. Laws: span is meaning-preserving; check re-runnable from the target; revocation propagates across the span. Instance: `WARRANT` ← PRM review 089. Killer: rename the source claim; nothing dangles visibly.

**K4. Grades with section–retraction pairs.** Carrier: representation grades per content class (line ⊂ file ⊂ file+kb; chat ledger ⊂ file ledger ⊂ kernel; bare trigger ⊂ elaborated trigger). Ops: elaborate e, degrade p. Laws: p∘e = id on the stated invariant; elaboration never changes floor meaning. Instance: promoted todo line whose pointer stays in place. Killer: a lossy degrade.

**K5. Ledger as join-semilattice CRDT.** Carrier: label → (text, sigil) maps; op: union-last-wins; laws: idempotent, commutative, associative merge. Instance: "every render is a patch." Killer: concurrent restatements with no order.

**K6. The fractal as a recursive tree type** (N ≅ synthesis × set(N)) with promotion as the constructor. Killer: a law that isn't already K4's.

**K7 (the reach). A cost-graded system:** every operation graded by who-pays-when in a preordered cost monoid; every design law an inequality; "cheap entry, expensive promotion" as cost localized at grade transitions. Killer: costs that never compose.

## Kills

**K5 dies.** Last-wins requires a total order on assertions. One chat has one; the mission is explicitly "10–20 parallel sessions a day," and nothing in the data supplies a cross-session order or a merge function — dated-record `NNN` sequences are per-day, per-collection, and race under concurrent writers. There is no semilattice here; the merge that would make one is *absent from the design*, and that absence is itself a finding worth filing (the fleet's concurrency story currently rests on git and luck).

**K6 dies.** The tree grammar is true and inert — rose trees with no operation beyond what K4 already states (`p∘e = id`, synthesis-is-never-index). Naming it buys zero retained properties. Folded into K4.

**K7 dies, informatively.** The corpus prices everything and *adds* nothing: no two costs are ever composed, only compared. A monoid with no composition instances in the data is rhetoric. What survives the wreck is a family of **least-element choice rules** — cheapest competent judge, lightest sufficient tier, earliest admitting theory, narrowest containing scope, least fixpoint — which I fold into K1/K2 as the recurring resolution principle. Even that is heuristic, not law: "zero-pad to twice the digits you expect" and "prefer the higher tier" are deliberate non-minimal choices.

## Survivors, worked in full

### S1. Soundness is a least fixpoint; the sigil is the base, the arrows are the induction

**Carrier.** A finite directed graph: claims C, arrows w ⊆ C×C (`why:`). A base map on claims: *stipulated* (`+`/`!` — a judge's act), *certified* (bare + `verify:`), *derived* (bare + `why:`), *open* (`?`).

**Operations.** Two computed views, both explicitly mandated as computed-not-stored:
- sound: C → {⊥,⊤}: sound(c) = ⊤ if stipulated or certified; if derived, ∧ of premises; taken as **least** fixpoint.
- warrant-mix: W(c) = its own mark if stipulated/open, else ∪ W(premises) — the set of open/agent leaves the claim ultimately rests on ("debt, priced by what rests on them").

**Laws, checked against data.**
1. The step operator is monotone on a finite lattice, so lfp exists and is reachable by finite induction — matching "provenness stays an inductive predicate" verbatim, and giving the ring exactly the `?` the data assigns it.
2. Governance propagates for free: `claim accept XY` changes one base value; both views update downstream with no writes — this is why "governance is one line over labels" can be true at all.
3. **The authoring rule is the algorithm's correctness condition.** The retraction sweep (follow arrows from the retracted node) is complete iff arrows over-approximate real dependence. `before/writing-an-arrow.md` states precisely that discipline: "point arrows at the claims whose collapse would make you revisit this one." So the resolution of Itch 1 is: arrows carry no *inferential* semantics (nothing checks entailment) but do carry an exact *operational* semantics — they are the sweep relation, and the induction runs over them. "Informal" means the entailment is unchecked, not that the relation is meaningless. The two files stop contradicting each other once you say which semantics each denies.

**Smallest instance (from data).** `DECODER <- PARSER MULTIBYTE+` with PARSER certified: W(DECODER) = {MULTIBYTE:agent} — the warrant-mix the SKILL.md example displays inline.

**Killing observation.** A user-`!` claim whose premise is retracted: under S1 it stays sound (stipulation is a base element, per `stipulation-is-a-legal-stop.md`), while `after/retracting-a-claim.md` says every dependent gets revisited. S1 survives only if the sweep is *alerting*, not *demoting* — revisit, don't recompute over judges. If practice ever auto-demotes a `!`, judges aren't base elements and this model is wrong. That is the observation to watch for.

### S2. Theories are a vocabulary-monotone stratification, and the index is inside the data

**Carrier.** Poset (T, ≤) of theories (≤ = transitive prior); V0: T → P(Words); effective vocabulary V(t) = ∪ over priors. Each claim c carries its needed words w(c).

**Operations.** place(c) = least t with w(c) ⊆ V(t); widen (edit V0, a revision to the defining claim); split (factor a shared subsection into a new common prior).

**Laws, checked.**
1. V is monotone by construction; confinement (w(c) ⊆ V(place(c))) is greppable and shipped as an audit (`confinement.md`).
2. Conservativity: extension never changes a prior's standings — repairs land in the prior's own fiber ("where it seems to, the prior was wrong; fix it there"). This is conservative extension in the model theorist's exact sense, held as a maintenance rule.
3. **The reach-flavored law, and it holds:** T is not external bookkeeping — each theory *is* a claim (`a-theory-is-defined-by-a-claim.md`), so the stratification is represented inside the carrier it stratifies, and demoting a stratum is ordinary claim governance. The data even records the experiment that forced this (llm-stet needed to demote a whole stratum, and could, "because the stratum was a claim"). This is the property that makes restructurings of the *layering itself* survivable — it should be stated as a law, not an anecdote.

**Smallest instance.** stance → purpose → good-smells → notation; SELF_CONTAINED sits in purpose because its words (ledger, line, reader) first all appear there.

**Killing observations, two, both live.**
- "Least t" presupposes a unique minimum. Every instance in the data is a chain; the first genuine poset with incomparable branches both admitting a claim makes placement ill-defined. Predicted repair: placement must become a declared choice (an act, fittingly) or the poset must guarantee meets.
- `theories.md` licenses word reuse with shifted meaning ("that shift in meaning is the interpretation, not a collision") — which breaks the words-as-strings model outright: string inclusion cannot see senses, so confinement-by-grep will one day misfile a claim whose word is admitted under the *wrong* sense. The string model is an approximation with a named expiry condition.

### S3. Certification transport — the structure is real and missing exactly one law

**Carrier.** Several S1-instances (chat ledgers, file ledgers, PRM's kernel); asserted content spans share(c, c') between claims of different instances.

**Operation.** If share(c, c′) and c′ is certified by check k, then c goes bare with verify = "re-run k in J."

**Laws.** (i) the span must be an interpretation — meaning-preserving across the two vocabularies, per S2; (ii) k must be re-runnable from the target's world; (iii) revocation must propagate across the span: retracting or invalidating c′ must sweep into c.

**Checked against data.** (ii) holds — `verify: re-run review 089...` names the check. (i) is *asserted, never checked* ("the certification transports because the content is shared" — by whose judgment? Unsigned). (iii) **fails on the data as it stands**: sweeps follow `why:` frontmatter, and the share edge lives only in prose — exactly the "arrows in prose, not in `why:`" rot that `graph-health.md` calls "the failure this skill exists to prevent," here at the one edge that crosses repo boundaries.

**Smallest instance.** `WARRANT` and `CLAIMS_ONLY`, both certified by PRM review 089.

**Killing observation — and it doubles as the retention finding.** Rename `WARRANT` in PRM, or restructure review 089 away: the transported certifications dangle with no lint, no red edge, no sweep. Given your stated purpose — properties surviving restructurings nobody re-verifies — this is the highest-value gap the survey found: the mechanism that lets rungs share verification is the one mechanism with no integrity check.

### S4. One grading structure: elaborate/degrade as section–retraction pairs

**Carrier.** Per content class, a chain of representation grades: task (line ⊂ file ⊂ file+kb), ledger (chat ⊂ files ⊂ kernel), trigger (bare bank file ⊂ `on:`-elaborated), design item (inline alternative ⊂ parallel list ⊂ sub-kb).

**Operations.** elaborate e: lo → hi; degrade p: hi → lo (flush, roll-up, floor reading).

**Laws, checked.**
1. p∘e = id on each class's stated invariant — and each class *does* state one: claims-with-standing for ledgers ("a summary of conclusions is not a substitute"); the obligation set for tasks (the promoted line's pointer stays *in place*, preserving todo.md's order, which is content); floor meaning for triggers.
2. Elaboration is meaning-invariant: "adding it never changes the floor meaning, only enables mechanical matching" (`condition-vocabulary.md`, verbatim); "the floor is not a fallback; it is the semantics" (`floor.md`); "the smallest deployment stays legal in the largest" (`one-rung-of-a-ladder.md`). Three subsystems state the same law independently — this is Itch 2's unnamed shape: not the tree, but the *grade discipline* the tree is grown and pruned under.
3. e∘p ≠ id: degrading forgets elaboration; the pairs are sections, not isomorphisms — which is why "climbing" is a category error the purpose theory warns against (a rung that grows checkable inference "has left its own" rung).

**Smallest instance.** A trigger file with and without its `on:` block.

**Killing observation.** A class whose degrade necessarily loses the invariant. The near-miss in the data is instructive: discourse-graph (five node types) has *no* degrade to the one-node ledger, and the fleet's response was to refuse the map and keep the classes separate (`class-epistemic.md`). The law thus also predicts where the system will refuse to unify — S4 fails exactly where the corpus already declined to build the pair.

## Where this leaves the run

Four survivors, each with laws that hold on the data and a named observation that would kill it: S1 (fixpoint soundness; resolves Itch 1 by splitting the semantics arrows deny from the one they carry), S2 (vocabulary stratification with an internal index; two live expiry conditions), S3 (certification transport; one law missing, and the gap is your retention risk incarnate), S4 (section–retraction grading; names Itch 2's shape and predicts its own boundary). Two informative corpses: no merge semilattice exists for parallel sessions (a design gap, not a modeling failure), and the cost calculus is comparison, not composition. Next step when you say so: stratify (the S2 poset is itself the natural spine) and file per `Skill(llm-claims-kb)`.

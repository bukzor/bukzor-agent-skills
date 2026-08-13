---
turn: 050-boil-down.md
sent: 2026-08-10T21:06:10.867Z
replied: 2026-08-10T21:10:55.082Z
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:156
uuid: a32a45c9-ccef-4417-bec0-12c45e0dc37d
---

# 050 -- Boil down, and freeze it -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/050-boil-down.md`; the operator's
verdict on it is this file's commit message.

---

Both artifacts follow, in chat only — no repo writes. Direct answer to the question first: yes, it boils down — to one maxim (DEFINABILITY), four certified law-groups (tower, grades, soundness, vocabularies), one stance (ACTS), and a quarantine for what's genuinely open (SEAMS). The layering that makes it simple is **by warrant, not by topic**: the floor of the picture is entirely certified and survives with every judgment stripped out — the account degrades the way its subject does.

---

## Artifact 1 — The one-page picture

**One sentence.** The system is a tower of levels over a single filesystem order, where every level's carrier is definable from the level below, its laws are stated at its own level, its values are computed rather than stored, and every question no computation can settle terminates in a signed act — and rot appears exactly, and only, where this is violated.

**Layer A — mechanics (all certified, no judge needed).** One substrate order does all the work: the index is `ls` (INDEX) and chronology is the lexicographic sort, kept sound by zero-padding (CHRONO). Levels are carved by schema conjunction, checkable from below (CUTOUT); engines are blind upward (BLIND). Representation grades round-trip — degrade after elaborate is the identity (ROUNDTRIP) — but only a class can say *what* the round-trip must preserve (INVARIANT), and grades are sections, not isomorphisms (NOISO).

**Layer B — epistemics (certified core, judgment at the edges).** Provenness is a least fixpoint over signed stops (SOUNDNESS): stipulations stop regress and survive fallen premises, swept but not demoted (STOP); rings are unproven until a circular premise is *replaced*, not supplemented (RING); one signature updates everything downstream with zero further writes (ONEWRITE); debt is computed on the sound fragment only (DEBT). Theories stratify vocabulary with greppable confinement (CONFINE), conservativity for pure addition (CONSERVE), and an index that is internal — demoting a stratum is ordinary claim governance (INSIDE).

**Layer C — the maxim.** Carrier below, laws at the level, values computed (DEFINABILITY). Every enforcement the corpus has exploits it; every rot spot violates it (ROT): stored likelihood, prose spans, arrow-poor ledgers. The cheapest repair in the whole account is one instance of it: store the transport span as data and the existing sweep closes the fleet's worst integrity gap (DANGLE → ONEFIELD).

**Layer D — the frontier (held open on purpose).** No total order, no merge (NOMERGE → MERGE?); four retraction mechanisms and a schema that can express none (RETRACTFORM?); single-derivation arrows (NOOR → ORQ?); stored numbers tracking nothing (STALE?).

**What I compartmentalized away, and what each costs:**

- **Content quality and judge timing → ACTS.** The picture says where judgment lives and who signed, never whether it judged well or when review happens. Cost: review cadence and prose quality are outside the model, permanently.
- **The cost calculus → dropped.** The corpus compares prices but never composes them (~~COSTMONOID~~), so the *admission criterion* for distinctions — "earns its place by what it lets us state" — survives only as informal stance. Cost: the picture can locate every structure but cannot justify adding one.
- **The mechanization ladder → folded into GRADES.** Cost: it hides that the chat rung lives off-substrate — which is precisely where NOMERGE bites. The cross-reference is kept in SEAMS so the fold doesn't silently drop the obligation.
- **Content-hash identity (the kernel rung's regime) → treated as a grade concern.** Cost: staleness-as-hash-divergence is invisible in the picture; the obligation survives as RETRACTFORM? and MERGE?, not as structure.
- **Trigger machinery → compressed to FLOOR plus a GRADES example.** Cost: condition vocabulary and sweep bounds are unmodeled; if the trigger subsystem's floor law ever diverges from the ledger's, FLOOR would paper over it.
- **Prose meaning → three laws confessed unmechanizable** (FLOOR, SPANJUDGE, sense-level confinement per SENSE) rather than approximated. Cost: they are discipline, and discipline fails silently (ORACLE).
- **Concurrency → NOT compartmentalized.** Dropping it would be the bug in the nice outfit; it stays open as MERGE?.

---

## Artifact 2 — The account as a claim ledger

* ACTS+: theory: judge, act, signature, ruling, computation. Where no computation over stored data can settle a question, the system terminates it in a signed act, and the signature (sigil, file location, dated record) is the durable record of who judged
* ~~COSTMONOID~~: operation costs compose in a graded monoid — retracted: the corpus compares prices but never adds them; comparison without composition is a stance, not a structure

* TOWER+: theory: level, artifact, engine, schema, substrate, refinement. The system is a tower of levels — substrate, generic kb, classes, instances — each a vocabulary plus engine plus laws over the artifacts of the level below <- ACTS
* CUTOUT: a level's artifacts are carved from the level below by schema conjunction, so class validity is checkable with sub-level machinery alone -- certified(stratified-model/run_tests.py: test_class_artifacts_are_cut_out_by_conjunction) <- TOWER
* BLIND: every engine runs ignorant of the levels above it; in the executable model no module imports at or above its own level -- certified(run_tests.py: test_import_graph_respects_level_order) <- TOWER
* FLOOR+: refinement never changes lower-level meaning — an elaborated artifact means what its bare form means, with more enforcement; stated independently by three subsystems, but not mechanically checkable, because prose meaning is compared by a reader, not an engine <- TOWER
* DECLARE+: an artifact's tower position is declared by its location — an act — not computed from content; the model's discourse module, importing nothing, is placeable only by declaration <- TOWER ACTS

* DEFINABILITY+: theory: carrier, law, value, stored, computed. Health invariant: each level's carrier is definable from the level below, its laws are stated at its own level, and its values are computed, never stored; rot appears exactly at violations <- TOWER
* INDEX: the kb index is defined as substrate ls, so a stale synthesis cannot corrupt enumeration -- certified(run_tests.py: test_index_is_ls_not_synthesis) <- DEFINABILITY
* CHRONO: chronology is defined as lexicographic sort of dated names; zero-padding the sequence number is the repair that keeps that definition sound, since "-10-" sorts before "-2-" -- certified(run_tests.py: test_chronology_is_definable_from_lexicographic_sort) <- DEFINABILITY
* CARRIER: the claims graph — labels, standings, arrows — parses out of generic entries' frontmatter, so class structure needs no storage of its own -- certified(run_tests.py: test_claims_carrier_is_parsed_from_l1_entries) <- DEFINABILITY CUTOUT
* ROT+: every rot spot the survey found stores a computable value or carries an edge in prose: stored likelihood, prose transport spans, an arrow-poor reference ledger <- DEFINABILITY

* GRADES+: theory: grade, elaborate, degrade, pointer, invariant. One content kind spans representation grades — line, file, file-plus-kb; bare trigger, elaborated trigger; chat ledger, file ledger, kernel — joined by elaborate/degrade pairs <- TOWER
* ROUNDTRIP: degrade after elaborate is the identity: promoting a working-set line leaves a pointer in place, and flushing restores the exact working set, order included -- certified(run_tests.py: test_promote_then_flush_is_identity_in_place) <- GRADES
* INVARIANT: the generic engine proves only content round-trip; each class names what its pointer must preserve — the task class's checkbox pointer keeps the obligation sweep-visible where the generic pointer loses it -- certified(run_tests.py: test_task_promotion_keeps_obligation_sweep_visible) <- ROUNDTRIP
* NOISO+: elaborate after degrade is not the identity — grades are sections, not isomorphisms — so degradation loses elaboration by design, and a grade that grows new checkable inference has left its grade, not climbed within it <- GRADES
* ~~ROSETREE~~: the sibling-pair fractal is a recursive tree type — retracted: true and inert; every law it could state is ROUNDTRIP or INVARIANT already

* SOUNDNESS+: theory: claim, standing, premise, arrow, stipulation, sweep, fixpoint, debt. A claims ledger computes provenness as a least fixpoint: signed stops and certified checks are sound, and a derived claim is sound iff all its premises are <- TOWER DEFINABILITY ACTS
* STOP: a stipulation is a legal stop: a user-signed claim stays sound when its premise is retracted, and the sweep flags it for revisit — alerting, never demoting -- certified(run_tests.py: test_stipulation_survives_a_fallen_premise_but_is_swept) <- SOUNDNESS ACTS
* RING: a closed ring is unproven, and outside support must replace a circular premise rather than join it: premises are conjunctive, so adding an outside claim to a ring member leaves the ring unsound -- certified(run_tests.py: test_ring_is_unproven_and_outside_support_must_rewire_not_add) <- SOUNDNESS
* ONEWRITE: governance is one write: re-signing a single premise updates all downstream soundness with no further writes, and no signing ever lowers a claim -- certified(run_tests.py: test_governance_is_one_line_and_never_lowers) <- SOUNDNESS
* DEBT: warrant-mix is computed on the sound fragment only — the agent-signed leaves a sound claim rests on; computed over all claims it would price a base-free ring at zero debt -- certified(run_tests.py: test_warrant_mix_is_computed_debt_on_the_sound_fragment) <- SOUNDNESS RING
* NOOR: an arrow list is one conjunctive derivation; the notation offers no alternative-derivations form -- authority: why: is a single list (claim schema; SKILL.md) <- SOUNDNESS
* ORACLE+: sweep completeness is discipline, not data: real dependence is stored nowhere, so a claim certified while silently assuming a premise escapes the sweep invisibly — witnessed only by handing the test an oracle the system lacks -- certified(run_tests.py: test_sweep_complete_only_relative_to_arrow_discipline) <- SOUNDNESS ROT

* VOCABULARIES+: theory: ontology, prior, confinement, conservativity, placement. Theories are vocabulary-monotone strata: effective vocabulary is own ontology plus priors', transitively, and claims live where their words are admitted <- SOUNDNESS ACTS
* CONFINE: confinement greps: a claim using a word outside its theory's effective vocabulary is mechanically detectable -- certified(run_tests.py: test_confinement_is_greppable) <- VOCABULARIES
* CONSERVE: pure addition is conservative: appending later claims that cite priors changes no prior claim's soundness -- certified(run_tests.py: test_extension_is_conservative_when_it_only_adds) <- VOCABULARIES SOUNDNESS
* CONSACT+: beyond addition, conservativity is writers' discipline: last-wins mechanics would let a later theory overwrite a prior label, so "repairs land in the prior's own fiber" is a rule, not a theorem <- CONSERVE ACTS
* LEASTACT: least-theory placement is unique on chains only: two incomparable theories admitting the same words yield two minimal placements, so choosing between them is an act -- certified(run_tests.py: test_placement_is_unique_on_chains_only) <- VOCABULARIES ACTS
* INSIDE: the stratification's index is internal: a theory's standing is its defining claim's soundness, so demoting a whole stratum is ordinary claim governance -- certified(run_tests.py: test_the_stratification_index_is_internal) <- VOCABULARIES SOUNDNESS
* SENSE+: string-level confinement cannot see senses, and the notation licenses word reuse with shifted meaning, so grep-confinement will eventually misplace a claim; LEASTACT's diamond is the first symptom <- CONFINE LEASTACT

* SPANS+: theory: instance, span, transport. Certification transports between ledger instances along shared-content spans: the target goes bare with a verify note naming the source's re-runnable check <- SOUNDNESS GRADES
* DANGLE: a span kept in prose is invisible to every engine: when the source claim falls, the transported certification survives unswept, with no lint -- certified(run_tests.py: test_prose_span_leaves_the_transported_cert_unswept) <- SPANS ROT
* ONEFIELD: storing the span as data closes the gap using the existing per-instance sweep plus one hop — one field, no new machinery -- certified(run_tests.py: test_stored_span_closes_the_gap_with_existing_sweep) <- DANGLE
* SPANJUDGE+: whether two claims in different vocabularies share content is a judgment, so a span should itself be a signed act, not an unattributed sentence <- SPANS ACTS

* SEAMS+: theory: order, session, merge, retraction, likelihood. The account's unresolved obligations, held as claims so they sweep and price like everything else <- SPANS VOCABULARIES
* NOMERGE: replaying the same restatements in different orders yields different ledgers, so without a total order on assertions last-wins defines nothing -- certified(run_tests.py: test_last_wins_is_order_dependent_so_no_merge_exists) <- SOUNDNESS
* MERGE?: parallel sessions have no shared order, so the fleet's concurrent-write story rests on git conflict surfaces; an answer — substrate merge rule, or workflow ban on cross-session restatement — settles the concurrency design <- NOMERGE
* RETRACTFORM?: the corpus carries four retraction mechanisms (chat strikethrough, standing change, filename suffix, contrary verdict) and the file schema's standing enum expresses none; an answer settles both the schema and what triggers the sweep <- SOUNDNESS
* ORQ?: does any ledger need alternative derivations for one claim? Yes forces restating the fixpoint over an AND-OR graph; no makes NOOR a law worth keeping stated <- NOOR RING
* STALE?: stored numeric likelihood updates on no event and tracks nothing -- certified(run_tests.py: test_stored_likelihood_tracks_nothing); keep it and build its missing evaluator, or cut it and let contests carry polarity? <- ROT
* ~~CRDT~~: the chat ledger is a merge semilattice under last-wins — retracted: no commutativity without an order; what survives is NOMERGE

* CORPUS+: theory: the proper nouns — discourse-graph, PRM (the Lean-mechanized rung), review 089, tred. The claims binding the account to named data; the theory to throw away when the names change <- SOUNDNESS SPANS
* POLARITY: discourse-graph's contradiction deductions make standing non-monotone — strengthening a premise can contest a conclusion — so the least-fixpoint account is false of that class member, and the two epistemic classes are rightly separate -- certified(run_tests.py: test_contradiction_polarity_is_non_monotone) <- SOUNDNESS
* NOEVAL+: discourse-graph ships stored standings and no evaluator, so its laws are unfalsifiable by its own machinery; the model had to invent a minimal evaluator just to witness POLARITY <- POLARITY ROT
* LIVEDANGLE: the live instance of DANGLE: WARRANT and CLAIMS_ONLY in the notation's own ledger are certified by "review 089" in PRM, connected only by a sentence; renaming either end breaks nothing visibly -- authority: llm-claims/design.claims.kb/notation.kb <- DANGLE
* COMPONENTS: the notation's own file ledger audited at 25 components across 27 claims — arrow poverty at the reference instance -- authority: llm-claims-kb graph-health.md <- ROT

---

Status: all `certified()` checks re-run via `python3 /home/bukzor/repo/github.com/bukzor/bukzor-agent-skills--replication-run/stratified-model/run_tests.py` (23/23 as of last run). The `?` claims are the asks — each states what an answer settles; the `+` claims stand open to veto; contamination constraint still intact (nothing under the blind read; one earlier title-level leak already reported).

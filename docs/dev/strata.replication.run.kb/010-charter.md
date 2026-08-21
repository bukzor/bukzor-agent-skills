---
turn: 010-charter.md
sent: 2026-08-10T20:36:30.502Z
replied: 2026-08-10T20:41:52.856Z
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:84
uuid: 91abe7d5-4c39-4a0e-9992-765feb040b1c
---

# 010 -- Charter and data -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/010-charter.md`; the operator's
verdict on it is this file's commit message.

---

All three explorers have reported and the local read is done. Here is the survey — findings before theory.

## Scope note, and one contamination flag

Read in full: `llm-kb` (SKILL + schemas + references + must-reads + self-audits + migrations guide), `llm-claims` (all four theories, all twelve must-reads, both schemas), `llm-claims-kb`, `llm-discourse-graph` (all five schemas), `design-next.kb` (mission, goals, requirements, design entries), `llm-design-kb` (principles), `llm-triggers` (design.kb), `llm-subtask` (todo schema, four-tier reference), `llm-collab`, `llm-must-read-kb`, `llm-vitals` mission, `llm-chat-librarian`. The three prototype repos were surveyed by delegates; their reports are folded in below.

Flag: an `ls` of `docs/dev/devlog/` showed me the **titles** of three 2026-08-09 devlog entries ("Engine-tower review — FREE-CONSERVE premise, poset-check hole", "Question theory, act review fallout, single-sigil seam", "Ledger drawing tool — tred, edgepaint, and what the lints found"). Bodies unopened. Title-level contamination only, but those titles do leak vocabulary ("engine tower", "FREE-CONSERVE", "courts are sigils" from a 2026-08-10 title). I also chose to skip `docs/dev/design.claims.kb/` (the fleet's authorship ledger) and the 2026-08-09 ADR despite their absence from your exclusion list — both are stamped 2026-08-09 and sit too close to the answer's work session; spirit over letter.

## The recurring shapes

**1. One sibling pair, everywhere.** `$name.md` + `$name.kb/` — synthesis and elaboration — is the single most-instanced shape in the corpus. It is the collection pattern, the decision point (`$ITEM.md` question + `$ITEM.kb/` options), the task tower (`todo.md` : `todo.kb/`, and recursively `$slug.md` : `$slug.kb/`), discourse elaboration, the migration entry + script bundle (deliberately non-`.kb`), the theory + its claims. `class-task.md` says it outright: "the plan is self-similar." The whole system looks like one relation — roll-up/elaborate — instanced at every grain, with per-class rules about what the roll-up owes (a synthesis is *never* the index; `ls` is the index; the order sometimes *is* content, as in todo.md).

**2. Claims-only, and status-as-projection, arrived at three times independently.** The current notation (`claims-are-the-only-node-type.md`), llm-stet (findings/contests/rulings are claims), and PRM (`CLAIMS_ONLY!`, `Verdict` lists with status *computed*, never stored) all converged. ideation.epistemics went furthest: warrant is *field presence*, lifecycle is a four-point order `described ⊑ stipulated ⊑ obligated ⊑ certified` *read off* the file, "contested" = a live contradiction-deduction aimed at you. The maxim recurs almost verbatim across repos: **standing that can be computed must not also be stored, or the two can disagree.** Meanwhile the shipped discourse-graph *stores* `status:` and a numeric `likelihood:` — the older stratum contradicting the newer principle in the live fleet.

**3. Justification terminates in an act; the sigil signs the judge.** The stance theory is the deepest layer and the most stable across attacks: authority is a property of acts, not propositions; a stipulation with a named author is a *finished* claim; the four marks (bare/`?`/`+`/`!`) exhaust "no judge needed / no judge yet / agent / user"; a certified claim goes bare because the check *stands where the judge stood* (warrant = discharged stipulation — certified across instances, notably). PRM mechanized the same thing: `Source = user | agent | checker | imported`, evidence append-only, retraction a contrary verdict, revocation *unrepresentable*.

**4. Theories as vocabulary-scoped strata.** A theory = ontology (word list) + priors + defeater, defined *by a claim* (no second node type); placement of a claim is fixed by the earliest theory admitting its words (confinement); a later theory never lowers a prior's standing (conservativity); split triggers priced by reader cost, never count. This shows up in llm-claims, llm-stet (theory files with `priors`/`ontology`/`defeated-by` frontmatter and an explicit poset), and PRM (theories as a poset by ontology inclusion, with hypothesis-bundle `Frame`s instead of axioms). Also — same shape, different clothes — the design tower's numbered layers (mission→goals→requirements→design) with `why:` pointing up, and the stance→purpose→good-smells→notation chain. Stratification with one-way citation is the corpus's favorite move.

**5. The ladder of rungs / the floor.** One meaning, many enforcement grades: chat core block → file ledger → typed kernel; the invariant (every claim sound, open, or retracted) is what survives the rungs; downward degradation must be lossless, upward must not be pre-committed (why arrows stay informal). ideation.epistemics calls the rungs "ports of one core" and makes porting-survival the kernel's validation metric. llm-triggers restates it for directives: "the floor is not a fallback; it is the *semantics*" — interception shims only strengthen delivery of the same meaning. And there is a striking operation riding on it: **certification transport** — `CLAIMS_ONLY` and `WARRANT` in the current notation are marked certified *because review 089 in PRM certified the same content in the mechanized instance*. Claims discharged in one rung's instance discharging in another's, "because the content is shared."

**6. Last-wins union, and every render a patch.** The chat ledger's whole update semantics: claim set = union over chat, last wins; a partial render is a patch; silence endorses. Dated records generalize it (newest-wins, append-mostly, `YYYY-MM-DD-NNN`). PRM instead bets on content-hash identity with mutable name pointers, staleness = hash divergence — and its own todo names the collision with dated newest-wins as unresolved.

**7. Everything is priced.** Not a metaphor — an actual cost calculus is doing design work everywhere: token economy, write economy ("no read-back, no write"), cheap entry / warrant charged at transitions, settle-at-the-cheapest-judge (with a per-mark bill of costs), distinctions pay rent by the judgment they make sayable (PARSIMONY), theory splits priced by reader cost, `+` as issued debt joining a review queue, open claims priced by what rests on them, SWEh/WSJF on tasks. The purpose theory even names the competitor: the ledger competes with *keeping no ledger*.

**8. Triggered reads.** must-read banks: filename = condition, body = directive, `ls` = index; the taxonomy before/after/when, refined in v2 to action/judgment/wake-shaped by *how the condition can be noticed*, with an admission test ("could an unaided agent notice this?"). Plus the anti-rule: recognition vocabulary cannot itself live behind a trigger.

**9. Self-application, with receipts.** Every layer is its own first instance: the notation's design is a ledger in the notation; llm-stet's `LEDGER-SELF!`; PRM's `IMAGE!` ("the design ledger is its own instance at lower fidelity"); llm-kb's methodology kb; design-next as an instance of llm-design-kb. The failures it catches are recorded too: llm-stet's ledger violated its own `RECORD-FIELDS` by hand — "history needs tooling, not discipline."

**10. Migrations and validators.** A migration = decision + idempotent transformation + scope + status; `validate.sh` read-only and permanent ("validators outlive migrations" — every migration adds a doctor check). The convention set is treated as a schema with versioned, re-runnable evolution.

## The tensions and itches

- **Arrows refuse semantics, yet everything computes over them.** `<-` is "motivation, not entailment, and the informality is *permanent*" — but retraction sweeps follow arrows, cycles get least-fixpoint semantics ("cycles are unproven — keeps provenness an inductive predicate"), the graph tool runs `tred` (which assumes transitivity, a semantic claim!), and warrant-mix is a computed view. PRM has the same fork internally: `ARROWS!` vs. a roadmap wanting edges walked out of proof terms. The corpus wants arrows both cheap and load-bearing, and pays for it in each tool.
- **Three arrow vocabularies, one shape.** `why:` (design: motivation, points at goals), `<-`/`why:` (claims: support), `premises:`/`conclusion` (discourse: entailment as a hyperedge with polarity). `shared-shape-separate-semantics.md` and `class-epistemic.md` explicitly rule *against* merging (held/desired vs truth-apt) — the itch was felt and answered with a boundary, but the claim schema then cites llm-design-kb's `why:` as its own prior art, so the boundary is already leaky at the provenance level.
- **Three identity regimes.** Label-as-locus (survives revision by design), content-hash (revision changes identity; staleness is hash divergence), and dated newest-wins (identity is the date-slug; revision is a new file). Unreconciled, and PRM's todo says so.
- **The notation's own ledger failed its own graph audit**: 25 components across 27 claims — "its arrows are in prose, not in `why:`" — named in `graph-health.md` as exactly the failure the skill exists to prevent. (The recent commits about ledger hygiene suggest this was live pain.)
- **Numbers vs judges.** discourse-graph carries `likelihood: 0..1` on claims, deductions, *and sources*; ideation admits "'propagates nowhere' is also a description of dead weight"; the claim notation replaced the scale with four judge-marks. A quiet, decided argument — probabilism lost to authorship — but the losing side still ships.
- **Questions: node type or sigil?** Five-collection graph says node type; claims says "a question is a claim marked `?`"; ideation flagged `questions.kb/` as *not derivable* and kept it on ergonomics, "flagged for fiat." Thrice-visited, still wobbling.
- **Retraction has four mechanisms**: strikethrough-in-place (chat), git-diff-minus (files), filename suffix `.retracted.md` (ideation), contrary-degree verdict (PRM, where deletion is unrepresentable). All satisfy "visible where it stood" differently; the downgrade *target* on retraction is an admitted spec gap in ideation.
- **Mechanism-over-exhortation vs. the IMPERATIVE blocks.** v1's sharpest self-diagnosis: every `WILL FAIL` warning is a defect report on a missing mechanism — and the shipped skills are full of them, including the ones stating the principle.
- **Stored lifecycle enums proliferate anyway**: todo `status:` (two-tier, closed), migration status (seven stages), decision-lifecycle (five) — each carefully reasoned, none derived, all in tension with shape #2's maxim. Some of that is honest (labor state isn't computable from the artifact), but nobody has said where the computed/stored boundary *is*.
- **The working set is the confessed unknown.** llm-stet: `WORKING-SET-DESIGN?` — "everything else is exoskeleton around this organ" — assembling a budget-bounded view from a seed. The v2 sweep's "bounded emission" is the same organ from the trigger side. Nothing anywhere solves it; two designs orbit it.

## What the three prototypes were, in one line each

- **ideation.epistemics** — the *derive-don't-store* attack: warrant lattice by field presence, invariants as build-failing audits, obligation as a reverse-dependency view.
- **prototype.personal-reasoning-management** — the *mechanized rung*: Lean kernel, content-hash identity, append-only verdicts, `WellFormed … := by decide`, depth ladder stated/described/proven.
- **prototype.llm-stet** — the *design-ledger-only* attack: theory poset in files, typed contest edges, append-only transaction log, scale regimes; killed its Datomic candidate into a proper-nouns-last theory.

The convergent core across all four attacks — claims-only, act-terminated justification, computed standing, vocabulary-stratified theories with confinement/conservativity, least-fixpoint provenness, the rung ladder with degradation — is convergent *without coordination*, which is itself the strongest empirical fact the survey produced. The tensions cluster just as clearly: arrow semantics, identity, and the stored/derived boundary are where restructurings will bite.

## Status

- **Ground truth**: surveyed as above; strata.*, engine_tower, 2026-08-09 devlogs/todos, trash untouched; one title-level leak flagged.
- **User goals**: a formal account whose worth is measured in restructuring-survival; this report is deliverable 1 of the /formalize procedure (survey); conjectures next, on your word.
- **Assumptions I'm carrying**: that design-next.kb and llm-triggers count as data (current design intent), not as answer-contaminated; that the delegates' reports are accurate (spot-checkable — they quote file paths).
- **Next**: step 2, conjectures — five-plus candidate structures, each with carrier, operations, laws, smallest instance, and killing observation.

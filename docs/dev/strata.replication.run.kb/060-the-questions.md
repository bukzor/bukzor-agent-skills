---
turn: 060-the-questions.md
sent: "2026-08-10T21:11:08.565Z"
replied: "2026-08-10T21:13:55.974Z"
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:159
uuid: f1a5b1ad-09a3-46e7-a161-dbef80ba99f7
---

# 060 -- The questions, and the bets -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/060-the-questions.md`; the operator's
verdict on it is this file's commit message.

---

## The questions you've been living with, crystallized

**Q1 — the working set.**
As experienced: *"What should todo.md look like? Why does every design of it feel wrong within a week?"* (The data's own words: WORKING-SET-DESIGN? — "everything else is exoskeleton around this organ.")
Well-posed: *What is the class invariant that the degrade map must preserve when the whole system is compressed to one attention-sized screen?* The difference is the finding: the experienced question asks for a file format; the well-posed one asks for the thing INVARIANT says only a class can supply — the generic engine has already proven everything it can (ROUNDTRIP), and no amount of restructuring todo.md will answer a question that isn't about todo.md.
Settled by: ROUNDTRIP, INVARIANT, NOISO — the *form* of the answer is settled: name what must survive the round-trip (obligation set? order? bounded emission?) and the format falls out.
Residue: which invariant attention actually needs is an act (ACTS) — not derivable from any data you have, only decidable by you and then enforceable forever after (the checkbox precedent: `- [ ]` was exactly such a ruling).

**Q2 — are questions a thing?**
As experienced: *"Do questions deserve their own node type / collection, or do I keep flip-flopping because both feel wrong?"* (The wobble is in the data three times.)
Well-posed: *Is "question" a standing or a carrier?* — i.e., is it a value in the judge dimension of an existing node, or a different node? DEFINABILITY answers on principle: anything computable from standing must not also be a stored type. A question is an open claim plus what-an-answer-settles in its text. My own SEAMS theory is the demonstration — the account's questions sweep, price, and grep like every other claim.
Settled by: DEFINABILITY, CARRIER; SEAMS as the working instance.
Residue: discourse-graph's question→candidate-resolutions wiring is real structure that "open claim" doesn't carry. Whether candidates earn a carrier is open — my bet is no (candidates are just claims the question's text names), but that's a `+`, not a proof.

**Q3 — what do arrows mean?**
As experienced: *"Am I lying when I draw an arrow nothing checks? Should arrows become checkable, and is it a failure that they never do?"*
Well-posed: *Which computations run over the arrow relation, and what authoring discipline makes each one sound?* The finding in the difference: arrows never needed entailment semantics — they have exact *operational* semantics (the sweep relation and the fixpoint's induction order), and "informal" only denies the semantics nobody uses.
Settled by: SOUNDNESS, RING (with the executable correction: outside support must *replace* a circular premise — conjunctive `why:` means adding doesn't help), NOOR.
Residue: ORACLE — completeness of the sweep is discipline whose violation is silent; and ORQ? — whether one claim ever needs alternative derivations, which would force the fixpoint onto an AND-OR graph.

**Q4 — retention across the "good idea."** (Your concrete question; worked in full below.)
As experienced: *"I keep having good ideas that restructure the system, and I want the properties I care about to survive restructurings nobody re-verifies by hand. How? Is Agda better than Lean for this?"*
Well-posed — and the split is the finding, because it's *two* questions wearing one coat: (a) *Which properties are stated as re-runnable checks over carriers that the restructuring doesn't touch?* — a design question, mostly answered without any prover. (b) *For the residue — laws about laws — which system re-verifies cheapest after a change?* — a procurement question, and much smaller than it feels.
Settled by: DEFINABILITY, CUTOUT, the migration law, INSIDE, ONEFIELD. Residue: the discipline laws (ORACLE, FLOOR, SPANJUDGE) that no validator holds.

**Q5 — what makes a claim the same claim?**
As experienced: *"When I restate, rename, or move a claim — or certify it from another repo — why does everything downstream feel fragile?"*
Well-posed: *Which identity regime does each operation need?* Locus identity (label) for governance continuity; content identity (hash) for verdict transport; temporal identity (dated record) for history. The fragility is exactly the places one regime is used where another is needed — transport needs content identity and currently rides on a prose name (DANGLE, LIVEDANGLE).
Settled by: SPANS, DANGLE, ONEFIELD, SPANJUDGE, NOMERGE.
Residue: MERGE? and RETRACTFORM? — both are identity questions in disguise (what counts as "the same assertion" across sessions; what counts as "no longer asserted"), and both are open by my account's own admission.

## Q4 answered: mechanism first, then procurement

**The mechanism.** Your theorems come in three grades, and retention works differently at each:

1. **Most properties are decidable predicates over carriers definable from below** — INDEX, CHRONO, CUTOUT, CONFINE, ROUNDTRIP, span integrity. For these the retention mechanism is not a prover; it is the DEFINABILITY invariant plus the migration law: permanent validators, re-run on every change. A restructuring that breaks one fails loudly, forever, for free. My 23-test model is this grade, in Python, built in an afternoon — that cheapness is the point.
2. **The laws about the laws** — monotonicity of the soundness operator, existence of the fixpoint, conservativity of extension, p∘e = id — are theorems, but here is the retention lever: **prove them once at the generic level, parameterized over class data.** A theorem quantified over "any class supplying an invariant" survives every restructuring that stays inside the quantifier. Genericity of the statement *is* retention. Your tower already has this shape; the prover's job is to make the quantifier real.
3. **The discipline laws** (ORACLE, FLOOR, SPANJUDGE) are retained by no system whatsoever — only by pushing their carriers down a level (ONEFIELD is the worked example) or by signed acts. Any procurement pitch claiming otherwise is selling you a hidden oracle.

**Procurement.** Lean vs Agda, on the merits of grades 1 and 2:

- **Lean 4** wins grade 1 outright: `Decidable` + `by decide`/`native_decide`, compilation to fast executables that can read your actual files, lake/CI tooling, and — decisive under my own SPANS theory — **incumbency**: PRM's review 089 already certifies WARRANT and CLAIMS_ONLY in Lean. Switching provers orphans every existing transport; DANGLE is my claim about exactly what unmaintained cross-system certifications do. For grade 2, Lean's structures-and-typeclasses do parameterized-theorem retention adequately.
- **Agda** has one genuine edge: its parameterized module system maps onto VOCABULARIES more directly than anything Lean offers — a theory as a module telescope, instantiation as application, the tower as nested parameterization. That edge is real and narrow, and it is paid for with a weaker executable/decide story, thinner tooling, no mathlib, and the transport-orphaning cost. **Verdict: no — Agda's edge is at grade 2's elegance margin, and your bottleneck is grade 1's throughput.**
- **Dark horse, seriously weighed — Alloy.** Your actual loop is "good idea → does PROPERTY survive?", and Alloy's native operation is *counterexample search over a relational carrier*: restate the restructured design, re-run, and it hands you the smallest world where the law breaks — my "killing observation," generated by machine, in seconds. Relational logic fits the arrow-graph and the tower ontology unusually well. It proves nothing (bounded search) and validates no real files, so it cannot replace Lean; it slots *below* it, exactly as GRADES predicts: grep/schema → Alloy → Lean, each rung legal without the ones above, verdicts transported upward only when a design stabilizes. I'd put Alloy, not a prover, in the inner loop of the "good idea" workflow.
- **Narrow dark horse — TLA+**, for MERGE? alone: the one question my account leaves open is a concurrency-of-sessions question, which is TLA+'s home turf. Buy it if and when you engineer the merge rule; not before.
- **Weighed and declined:** Dafny/F*-style SMT auto-reproof retains theorems by re-search after refactoring — attractive — but SMT instability makes "the proof stopped being found" a new silent failure mode, which is the exact failure class this whole system exists to eliminate. Rocq: no edge over Lean here and a worse ergonomics trendline. Idris 2: executable-first dependent types, right shape, ecosystem too thin to bet retention infrastructure on.

**One sentence:** keep Lean as the certification rung, add Alloy as the idea-testing rung, spend the freed effort enforcing DEFINABILITY (validators, stored spans) — that's where most of your retention actually comes from.

## Bets, on the record

Disclosure first: my bets are partially contaminated by the title-level leak I reported earlier (devlog titles: "engine tower," "FREE-CONSERVE," "RESTRICT lemma," "courts are sigils," "Question theory," "tred/edgepaint lints," "poset-check hole"). Bets informed by a leaked title are marked (T); the clean bets are the ones worth grading.

**Expect to survive comparison:**
- The tower-of-levels backbone (T — "engine tower" makes this near-unfair) and the least-fixpoint soundness core with STOP and RING — the corpus's own LEAST_FIX all but guarantees convergence.
- DEFINABILITY in substance — "computed, not stored" recurs too often in the data for your answer to lack it, whatever it's named.
- DANGLE/ONEFIELD — the prose-span rot is visible enough that I expect you found it too.
- Clean bets I'd stake most on as *matching or exceeding* your answer: the RING rewire-not-add correction, the warrant-mix domain restriction (DEBT), and NOMERGE — each fell out of execution, and I doubt they're all in a prose-first account.

**Expect it beats me:**
- (T) The mathematics of the level ordering. "FREE-CONSERVE" and "RESTRICT lemma" smell like an actual free/forgetful adjunction with proved conservativity and a restriction result — the categorical structure I sketched, then settled for section–retraction pairs. If your answer worked that adjunction with laws checked, it beats my S4/FLOOR on depth and probably unifies GRADES with the tower ordering, which I kept as two axes.
- (T) The judge structure. "Courts are sigils" implies a jurisdiction algebra — *which* judge may settle *what* — where my ACTS is flat and my cost-of-judges reasoning died with ~~COSTMONOID~~. I expect a real structure there that I discarded as decoration.
- (T) "Question theory" — likely a fuller resolution of Q2 than my SEAMS.

**Expect it found what I couldn't have:**
- Anything incident-driven from operating the system on 2026-08-09 itself ("act review fallout," "single-sigil seam" (T)) — my data ends where the corpus does; findings born from live use were never available to me.
- Whatever is built on the authorship/cost economics (the design.claims.md header I legitimately glimpsed prices authorship against LOAD_COST) — I retracted the cost calculus for lacking composition, so anything real standing on it is outside my account by my own recorded choice. ~~COSTMONOID~~ is my named exposure; if the reveal shows costs composing somewhere, that retraction is the first claim to re-open.
- Conversely, one artifact I'd bet your answer lacks: an executable model with per-law witnesses. If the comparison has a use for mine, it's `/home/bukzor/repo/github.com/bukzor/bukzor-agent-skills--replication-run/stratified-model/`.

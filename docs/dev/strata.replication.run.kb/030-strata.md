---
turn: 030-strata.md
sent: 2026-08-10T20:50:25.900Z
replied: 2026-08-10T20:54:50.345Z
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:92
uuid: 3292aeeb-c7f3-4601-be05-16f5a26e71e9
---

# 030 -- Stratify -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/030-strata.md`; the operator's
verdict on it is this file's commit message.

---

## What makes a level a level

Drawn from the corpus's own architecture (design-next's core-and-classes, the schema anchor pattern, the floor law), a level is a quadruple (vocabulary, artifact set, engine, laws) satisfying three conditions:

1. **Cut out from below.** The level's artifact set is a subset of the level below's, and the membership predicate is checkable *with the lower level's machinery* — implemented literally as JSON Schema conjunction (`$ref` to `skill://` URIs, strict-root/open-`#base`, 2020-12 conjunction semantics): a claim file is a valid generic kb entry AND satisfies `claim.jsonschema.yaml`.
2. **Blind upward.** The level's engine runs with zero knowledge of higher levels — the class-blind engine and discovery contract, stated as a requirement, not a preference.
3. **Conservative downward.** Higher structure never changes lower meaning: "adding it never changes the floor meaning" (triggers), "the smallest deployment stays legal in the largest" (ledger rungs), conservativity (theories). Three subsystems state this law independently; it is the tower's load-bearing wall.

**The ordering relation:** L ≤ M iff Artifacts(M) ⊆ Artifacts(L), witnessed by schema conjunction, with L-meaning invariant on the subset. Note this makes each adjacent pair an S4 section–retraction (forget refinement / elaborate), and makes the tower itself an instance of S2's laws — vocabulary-monotone, conservative — with one deliberate difference I flag below.

**A second, orthogonal axis.** The mechanization ladder (chat notation → file ledger → Lean kernel) is *not* this tower — it stratifies instances of one class by checkability, and its bottom rung isn't even on the filesystem. Every claim below is located on the tower; ladder position is flagged where it changes the verdict.

## The tower

- **L0 — filesystem.** Vocabulary: path, directory, file, name. Engine: `ls`, `grep`, `mkdir`. Laws: name uniqueness; lexicographic sort.
- **L1 — generic kb.** Vocabulary: collection, entry, synthesis, maintenance guide, dated record, directive, migration. Engine: llm-kb procedures, generic validator, migration machinery. Laws: synthesis-never-index; one-item-per-file homogeneity; `requires:` before acting; idempotent migrations with permanent validators.
- **L2 — classes.** task, epistemic (two members: claims-kb, discourse-graph), trigger, design/decision. Each = L1 + class vocabulary + class schema (conjunction) + class laws.
- **L3 — instances and between them.** design.claims.kb, todo.kb, PRM's kernel; certification-transport edges live only here.

## Survivors, located and re-checked per level

**S4 (section–retraction grading) — lives at L1; its law is parameterized by L2.**
At L1 the maps exist and the law p∘e = id holds, but only for content identity — true of everything, saying little. Each L2 class supplies the invariant that gives the law teeth, and *refines the maps*: at L2-task, the pointer left in place must be sweep-visible ("`- [ ]` is load-bearing; a bare `-` is invisible to sweeps") — L1's "leave a pointer" is insufficient at the class level. Re-checked at tower scope: every file-based class's artifacts are valid L1 entries (holds, including discourse-graph's five collections); the one violator is the chat ledger, which sits below the filesystem floor entirely — which is exactly why it's a ladder rung, not a tower level. **Definability: the promote/demote maps are defined at L1; classes define only the preserved invariant.** Genericity trade: maximum genericity, near-zero structure at L1; full structure only per class.

**S1 (fixpoint soundness) — lives at L2-claims. False one door over, under-true one rung down.**
- At L1: inexpressible, not merely false — `depends:` gives reference edges but there is no judge base; the carrier's shadow exists, the valuation cannot.
- At L2-claims: holds as worked (monotone step, lfp, sweep-completeness = the arrow-authoring rule).
- At L2-discourse-graph — the sibling class member — **two laws fail**: standing is stored (`status` + `likelihood` fields), violating computed-not-stored; and deduction polarity (`kind: contradiction`) makes the step operator non-monotone — a premise *gaining* soundness can push a conclusion down. No least fixpoint is guaranteed. S1 asserted at "the epistemic class" is simply false; the fleet's decision to keep the two as separate classes is the correct response to this falsity, now stated as one.
- At the kernel rung (PRM): S1 is true but under-describes — provenness is proof-carrying, and the roadmap wants arrows *derived from proof terms*. Descending the mechanization ladder, the arrow relation flips from authored (chat) to derived (kernel). S1 as stated is the maximal claim true across both.

**S2 (vocabulary stratification) — lives at L2-claims; its laws recur at tower scope with one substitution.**
At L2-claims: as worked (chains only in the data; two named expiry conditions stand). At tower scope, monotonicity and conservativity both hold (blindness + floor law), but **placement is not computed** — an artifact's level is declared by its L0 location, not inferred from its words. The tower replaces least-admitting-theory (the incomparability-unsafe rule) with an act, consistent with REGRESS_ACT: placement, like justification, terminates in an act. This is a structural difference between the meta-instance and the object instance, not a law failure. **Definability: the theory carrier (collection + defining claim + CLAUDE.md header) is entirely L1 primitives; only confinement and conservativity are new.**

**S3 (certification transport) — lives at L3 only, and the tower explains the rot.**
No level's engine mentions it; its carrier — the share edge — is stored in prose, hence not definable from any level's data. Laws (i)/(ii) hold by discipline; (iii) fails, as worked. The stratification converts the finding into a repair: push the carrier down one level — make share edges frontmatter (a small L2-claims vocabulary extension), and law (iii) is covered by the *existing* sweep engine, no new machinery. Cost: one field; benefit: the highest-value integrity gap closes mechanically.

## Definability from below — the load-bearing inventory

Every place a level's structure is definable from the level below, the system got enforcement for free; every rot spot is a definability failure:

1. L1 index := L0 `ls` ("`ls` is the index" — verbatim). The entire retrieval story is one L0 primitive.
2. L1 chronology := L0 lexicographic sort. Zero-padding exists solely to keep this definition sound — a *repair to a definability claim*, which is evidence the fleet already treats definability as load-bearing.
3. L2 membership := L0 path + schema conjunction (checkable below).
4. S1's soundness and warrant-mix := L2 (graph, sigil base), computed by `llm.claims-graph`; stored nowhere, per rule.
5. The arrow graph itself := L0 file-relative paths in frontmatter — which is *why* graph-health lints are possible; the 25-components failure was detectable only because this carrier lives below.
6. Kernel rung: arrows := proof terms (roadmap) — definability deepens with mechanization.
7. **Anti-example:** S3's spans := prose. Not definable, not enforced, rotting.
8. **Anti-example:** discourse-graph's `likelihood` := nothing — a stored value with no defining computation, and the explorers' own verdict ("propagates nowhere is also a description of dead weight") is the predicted symptom.

The thesis the tower yields, one line: **carrier below, laws at the level, values computed — every enforcement mechanism in the corpus exploits this pattern, and every observed rot spot violates it.** That is the invariant to carry through restructurings; it is checkable per level and it predicts where the next rot appears (any new prose-borne edge, any new stored-but-computable field).

## The corpses, located

- The missing merge (killed K5) is an L0 gap — concurrency of the substrate itself — which is why no class can repair it locally and why every class inherits it.
- The cost calculus (killed K7) turned out to be level-free comparison, never composition; its salvage (least-element choice rules) now sits inside S1/S2 at their stated levels.

Ready to boil down to the page on your word; the tower above is its natural spine.

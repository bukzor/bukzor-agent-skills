---
managed-by: Skill(llm-subtask)
status: done
blocked-by:
  - 2026-11-25-005-consolidate-my-own-shadertoy-ledger.md
required-reading:
  - CLAUDE.md
  - 2026-11-25-005-consolidate-my-own-shadertoy-ledger.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/smoothing.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/confinement.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/ruling-fidelity.md
  - ../../../llm-design-kb/skill.kb/quality-passes.kb/
---

# my-own-shadertoy: apply unit 005's repairs, then smooth to a fixpoint

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (after
wave 6; the measurement is over, so the plan is open to you now)

## Problem Statement

Unit 005 reported 14 findings and edited nothing. Apply them in
my-own-shadertoy (`~/repo/github.com/bukzor.sandbox/sandbox-repo.kb/github.com/bukzor-sandbox/my-own-shadertoy`),
then finish the smoothing pass: walk the frontier until it is empty, and run
the sweep last. Read the confinement, ruling-fidelity and design-kb passes in
full this time; 005 applied them by name.

Decisions already made:

- **Finding 1:** restore the footers. Session 4025060d removed them in a WIP
  commit, and `BREADCRUMBS` is the owner's ruling, which outranks it.
- **Findings 2, 4-8, 11-13:** apply as 005 proposed, unless the full pass text
  changes your mind. Say so in Decisions.
- **Finding 3:** drop `todo:` and the spent tripwire sentence, and fix
  `after/a-milestone-lands.md`. You decide whether it moves to
  `technical-policy.kb/`.
- **Finding 9:** apply. `FIRST_INSTANCE` is `standing: user`, so the quote stays
  verbatim and the reworded body keeps every qualifier (ruling-fidelity).
- **The missed trespass:** `'milestone'` in `goals.kb/bite-sized-increments.md:9`
  (outside the quote) gets a repair like finding 6's.
- **Every scan finding gets a disposition**: repaired, dismissed with a reason,
  or put to the owner. Report them in a table.
- **Not here:** finding 10 (`NAMES_SHOW_STRUCTURE` is a ruling, and the
  coordinator will put it to bukzor), and finding 14 (`.claude/todo.md`, which
  a peer session edited today). The dev-process-design scaffold stays as it
  is.

Commit in my-own-shadertoy as you go, path-scoped, per its `CLAUDE.md`; don't
push. A peer session may commit there too: never stage a path you didn't
change.

**Scope (only these files):** in my-own-shadertoy, `docs/dev/claims.kb/**`
(except `dev-process-design.*`) and the `.claude/must-read.kb/` entries a repair
names; this handoff file.

## Steps

- [x] Findings 1, 2, 12, 13: footers, ONE_HOME, POLICY, minor items
- [x] Finding 3: TUTORIAL_READING and its bank entry
- [x] Findings 4, 5: WEBGPU_TYPES_PACKAGE move; DEPENDENCY_DIRECTION split
- [x] Findings 6-9, 11, goals trespass: confinement and one-home repairs
- [x] Smoothing walk over the changed frontier, until it is empty
- [x] Final sweep; scan-disposition table; final report; commit

## Decisions

- **Finding 3:** moved to `technical-policy.kb/tutorial-reading.md` with `force: should`. Once `todo:` was dropped, nothing on the deliverables rung was left (no build order, no occasion), and an imperative on Claude and bukzor belongs to policy, per `design.kb/CLAUDE.md`.
- **Finding 5:** split three ways, not two:
  - `DEPENDENCY_DIRECTION` drops `todo:`, since the direction holds today;
  - a new `WEBGPU_CALL_SITES` (todo) in architecture;
  - a new `WEBGPU_CALL_LINT` (todo) tripwire in deliverables.
  The lint claim keeps the signed occasion word for word ("the first WebGPU call found outside ... adds a lint rule"). It then adds why that trips at 1.2: both pages already call WebGPU from `apps/`, which makes the two occasions agree without rewording the ruling. Its bank entry now names both pages, not only gpu-info's demos.
- **Finding 9:** the first-uses routing ("leave it off `first-uses:`, fix it, handle it as the overreach entry says") moved to `after/a-milestone-lands.md`. That is the occasion that needs it (`DERIVED_RECORD`), not a cut. Every qualifier in the quotes is kept: "relevant", "new to bukzor" (learning), throwaway parts after the first instance, and that the trailer cannot be the check.
- **The goals trespass: dismissed, against the brief.** `goals.kb/bite-sized-increments.md:9` is inside `authority.words:`, bukzor's own wording quoted, and lines 21-22 quote the same words in the body. Saying "increment" there would put words in the owner's mouth. Confinement offers no repair for a quote.
- Standing kept `user` on every reworded claim. Each edit keeps the signed meaning: a word swapped to its higher-rung synonym, or signed text moved or partitioned. The new claims are signed `user` for the same reason, since every sentence in them is signed text or follows directly from it. Say so if you would rather they be signed `agent`.
- Left alone: `DEPENDENCY_DIRECTION` and `WEBGPU_TYPES_PACKAGE` name tools (pnpm, `@webgpu/types`) on the architecture rung. With the components rung dropped, architecture is the lowest rung that describes the build. `DESIGN`'s `stale-when:` watches for this.

## Open Questions

- Should `llm-claims-kb-ownership` exempt quoted text, both `authority.words:` and `[!@...]` callouts? Without that, an owner's quote is a trespass the scan can never clear.

## Final report

Done. Commits in my-own-shadertoy (unpushed, each passed pre-commit):
1. "BREADCRUMBS: restore each design rung's skill footer"
2. "Ledger: ONE_HOME states its claim; addresses and roll-up made accurate"
3. "TUTORIAL_READING: the spent tripwire goes; the practice moves to policy"
4. "DEPENDENCY_DIRECTION splits in three; WEBGPU_TYPES_PACKAGE is architecture"
5. "Confine milestone and program to their rungs; FIRST_INSTANCE states a property"
6. "Smoothing walk: two missing premises, one rationale on the wrong rung"

The smoothing walks:
- Walk 1, over every claim touched and its neighbours, found three things:
  - `MILESTONE_LADDER` lacked a `why:` to `FIRST_INSTANCE`, now that it is the only home of the first-uses record;
  - `WEBGPU_TYPES_PACKAGE` lacked a `why:` to `WEBGPU_CALL_SITES`;
  - `PROGRAM_AS_DATA`'s "extracted, not designed ahead" is build order, so it moved to `MILESTONE_1_2` (each-rung).
- Walk 2, over those four and their neighbours, found nothing, so the frontier is empty.

Final sweep:

| Check | Result |
|---|---|
| `llm.kb-validate` | 66 files, 0 errors |
| links | 101, 0 broken |
| triggers-lint, ledger and bank | 0 errors |
| graph | acyclic, no dangling `why:` |
| mentions | 0 |
| ownership | 0 contending |
| bare claims | none without a ground |

| Scan finding (005's run) | Disposition |
|---|---|
| mentions `DERIVED_RECORD`, `TBD` in `ONE_HOME` | repaired (descriptive link text; `TBD` added to `non-claim-tokens:`) |
| trespass `milestone`: requirements (2 claims) | repaired ("increment") |
| trespass `milestone`: architecture (3 claims) | repaired (parentheticals cut; the tripwire moved to deliverables) |
| trespass `tripwire`: architecture | repaired (`WEBGPU_CALL_LINT` in deliverables) |
| trespass `program`: requirements | repaired (`SWAP_SURVIVES` reworded) |
| trespass `pass`: requirements | dismissed: the verb ("tests still pass", "passes") |
| trespass `milestone`: goals | dismissed: the owner's quote (Decisions) |
| idle imports ×2, dev-process scaffold | dismissed: out of scope, an empty open scaffold |
| grounding: `NAMES_SHOW_STRUCTURE+` weakest (28 rest on it) | put to the owner (coordinator) |
| graph: `ASSERT_LIBRARY` reaches the mission only through policy | dismissed: a foreign `why:`, reach intact |

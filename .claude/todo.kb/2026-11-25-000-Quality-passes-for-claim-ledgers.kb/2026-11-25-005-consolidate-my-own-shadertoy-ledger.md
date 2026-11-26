---
managed-by: Skill(llm-subtask)
status: done
blocked-by:
  - 2026-11-25-003-llm-design-kb-passes-and-sweep.md
required-reading:
  - CLAUDE.md
  - ~/repo/github.com/bukzor.sandbox/sandbox-repo.kb/github.com/bukzor-sandbox/my-own-shadertoy/CLAUDE.md
  - ~/repo/github.com/bukzor.sandbox/sandbox-repo.kb/github.com/bukzor-sandbox/my-own-shadertoy/docs/dev/claims.kb/technical-policy.kb/consolidation-sessions.md
---

# my-own-shadertoy: the ledger step of a consolidation session

## Problem Statement

my-own-shadertoy is due a consolidation session (its `CONSOLIDATION` policy,
above). Do one part of it: "brings this ledger ... back to what is true", for
the ledger `docs/dev/claims.kb/`. Work from the project root,
`~/repo/github.com/bukzor.sandbox/sandbox-repo.kb/github.com/bukzor-sandbox/my-own-shadertoy`,
the way a fresh session there would.

Propose; don't apply. Other sessions own that repo, and some of its claims
are the owner's rulings. Edit nothing in it. Write each finding in this file
instead: the claim's path, what is wrong, the evidence (a command and its
output, or the text), and the repair you would make.

This run is also a measurement, so take nothing from the coordinator's
side. Don't open the parent plan or the other handoff files in this
directory, and don't read past sessions' transcripts about this ledger.
Report how you decided what to check: which skills, triggers and procedures
you loaded, and what led you to each.

**Scope (only these files):** this handoff file.

## Steps

- [x] Run the sweep's scans (validate, graph, mentions, ownership, grounding)
- [x] Read the whole ledger (flatten) and the repo state it describes
- [x] Check descriptive claims against ground truth (code, git log, bank)
- [x] Smoothing walk, top-down then bottom-up (one walk; see Decisions)
- [x] Write findings; final report; commit

## Decisions

- One walk, not to a fixpoint: nothing is applied, so a second walk would judge the same text. The frontier for the applying session is every claim named below plus its premises and dependents.
- Scope is the ledger. Bank entries and `.claude/todo.md` were read only to check a claim's pairing; their own defects are listed once, under Findings' last bullet, not repaired.
- Not done (other steps of the session, need bukzor): the breadcrumb witness, the `ASK_BEFORE_EDITING_KEPT` question.

## Open Questions

- Was removing the rung footers in the `wip: scaffold dev-process-design` commit deliberate? If so, `BREADCRUMBS` needs amending instead (finding 1).
- Finding 9 rewords `FIRST_INSTANCE`, whose `author:` is unrecorded: possibly bukzor's own wording.

## Findings

Paths are relative to `docs/dev/claims.kb/`. Scans from the project root: `llm.kb-validate` 64 files 0 errors; links 79/0 broken; graph acyclic, no dangling `why:`, for all three child ledgers; mentions 2 unresolved; ownership 0 contending, 6 trespasses, 2 idle imports (the open dev-process scaffold, expected). Every `first-uses:` evidence `path:func` exists; `REPO_SCOPE`, `ONE_THING_PER_PACKAGE`, `LIFETIME_GROUPS`, `ERROR_HANDLING` (both lint rules on in `.oxlintrc.json`), `WEBGPU_TYPES_PACKAGE` (TS 7.0.2 `lib.dom.d.ts:44176 type GPUBufferUsageFlags = number`), `ASSERT_LIBRARY` (two copies) and `DOM_BUILDING` (page still `<br>`) match the code.

1. **`technical-policy.kb/breadcrumbs-to-skills.md` (BREADCRUMBS, must) is violated.** `goals.kb/`, `requirements.kb/`, `architecture.kb/`, `deliverables.kb/` have no `CLAUDE.md`, and their top files link no `SKILL.md` (`grep -L SKILL.md design.kb/{goals,requirements,architecture,deliverables}.md` lists all four). The commit "Breadcrumb each design rung's collection from its own top file" added the footers, settling the todo item "may an ancestor's `CLAUDE.md` be a collection's breadcrumb?" as no; the later commit `wip: scaffold dev-process-design` removed them ("the Conventions footer removed from every rung file"). Repair: put back the `Conventions: [llm-design-kb] over [llm-claims-kb].` footer and its two link definitions in the four files.
2. **`technical-policy.kb/one-home.md` (ONE_HOME) fails the mentions scan and opens without a subject.** `llm-claims-kb-mentions`: `ONE_HOME names DERIVED_RECORD`, `ONE_HOME names TBD`. The flattened claim reads `ONE_HOME!: Everything else links to it, ...`, so "it" points at nothing. Repair: open the body with the claim itself ("Each conclusion, and the reasoning for it, has one home, and everything else links to it; ..."); give the two fleet links descriptive text (`[the fleet's one-home principle][fleet-one-home]`, `[its derived-record corollary][fleet-derived-record]`) so that no foreign label is mentioned (both targets exist under `bukzor-agent-skills/docs/dev/claims.kb/design.claims.kb/principles.kb/`); add `TBD` to `technical-policy.md`'s `non-claim-tokens:` (it appears only inside bukzor's quote).
3. **`design.kb/deliverables.kb/tutorial-reading.md` (TUTORIAL_READING) has already tripped but still carries `todo: true`.** Its occasion, 0.1 landing, has passed and the skim is done: `.claude/todo.md` has `[x] Suggestion ... skim webgpufundamentals.org's table of contents once`, and the commit "todo: recall 3 of 4 cold, the skim done, ...". What is left is a standing per-milestone practice, not an unbuilt state. Repair: drop `todo:` and the "Tripwire: ... Then skim ..." sentence, keeping "a topic's articles are read once the milestone covering it lands ..." as the claim. Because the claim is an imperative on Claude, consider moving it to `technical-policy.kb/` (`force: should`). Separately, `after/a-milestone-lands.md` step 2 drops "After 0.1 ... suggest one skim".
4. **`design.kb/deliverables.kb/webgpu-types-package.md` (WEBGPU_TYPES_PACKAGE) is on the wrong rung.** It has no `todo:`, no occasion and no build order; it says how a workspace gets its types, which is the architecture question (`EACH_RUNG`). Its only `why:` is architecture. Repair: `git mv` it into `design.kb/architecture.kb/` and fix the link in `.claude/must-read.kb/when/typescript-lacks-a-type.md`.
5. **`design.kb/architecture.kb/dependency-direction.md` (DEPENDENCY_DIRECTION) bundles three claims.** (a) The direction already holds and is enforced today: `apps/bukzor-shadertoy/package.json` declares only `@repo/gpu-*`, the gpu packages declare no workspace deps, and root `node_modules/` has no `@repo/` (no hoisting). Yet the whole claim is `todo: true`. (b) "WebGPU calls stay in gpu and passes from 1.2 on" is the part not yet built. (c) Its last sentence is a tripwire, a deliverables word (trespass `'tripwire' ... said by: architecture.kb`). That tripwire's occasion ("the first WebGPU call found outside those groups") differs from its bank entry's (`before/starting-milestone-1.2.md`). Its "flag constants come from `@webgpu/types`" sentence restates its own dependent, WEBGPU_TYPES_PACKAGE (`ONE_HOME`). Repair: keep (a) without `todo:`; split (b) into its own `todo:` architecture claim; move (c) into a deliverables tripwire whose occasion is "milestone 1.2 starts", matching the entry; cut the `@webgpu/types` sentence.
6. **Trespass of `'milestone'` into requirements:** `requirements.kb/first-instances-are-bukzors.md:19` "at each milestone's landing", and `requirements.kb/one-job-each.md:12` "from a package to a milestone or a commit". Repair: say "increment", the word the higher rungs already use (BITE_SIZED, GREEN_INCREMENT), which DELIVERABLES defines a milestone as.
7. **Trespass of `'milestone'` into architecture:** `program-as-data.md:23` "(milestone 1.2)" and `pass-kind-extension.md:16` "(milestone 7.1)". These are schedule details: the ladder and the bank entries `before/starting-milestone-{1.2,7.1}.md` already hold them. Repair: cut the parentheticals ("until a later pass kind shows whether it hurts").
8. **Trespass of `'program'` into requirements:** `requirements.kb/swap-survives.md` "A program written by any other host runs unchanged". The `'pass'` hit in requirements is the verb "passes", which is scanner noise. Repair: "What an author writes in any other host runs on the kept parts unchanged."
9. **`requirements.kb/first-instances-are-bukzors.md` (FIRST_INSTANCE) carries mechanism, and holds it a third time.** The `first-uses:`/`evidence:` record is also in MILESTONE_LADDER's last bullet and in `milestone-ladder.jsonschema.yaml`'s description, and the routing to the bank entry is the entry's own job (`state-properties-not-mechanisms`, `ONE_HOME`). Repair: the requirement keeps the property and its check ("bukzor confirms, at each increment's landing, the first uses it brought"), and the record and routing stay in MILESTONE_LADDER and the bank. This is for the owner to rule on (Open Questions).
10. **`requirements.kb/names-show-structure.md` (NAMES_SHOW_STRUCTURE, `standing: agent`) is the ledger's weakest judge.** `llm-claims-kb-grounding` ranks it first: `rests 26`, `weakest self`. Repair: put it to bukzor first; that one ruling grounds 26 claims.
11. **Duplication between `design.kb/deliverables.md` and `deliverables.kb/milestone-ladder.md`.** Both state the `N.M` split-without-renumbering rule. Repair: keep it in the ladder (its convention), and let DELIVERABLES only define "milestone".
12. **`technical-policy.md` (POLICY) says "Each carries `force:`", but `ask-before-editing-kept.md` has none** (it is `standing: open`). Repair: "Each ruled claim carries".
13. **Minor items.** `00.1-adapter-and-device.md`: "The page is `apps/bukzor-shadertoy`", though the app now has two pages; 0.1's is `src/pages/gpu-info/`. `02.1-uniform-block-and-resize.md` quotes `[!@bukzor] 2026-11-21`, a date rather than a session or owner-commit address: cite the commit "Punt canvas resize from 0.2 to 2.1". `webgpu-types-package.md` writes its address as a full UUID where every other claim uses an 8-character prefix.
14. **Outside the ledger, not repaired.** `.claude/todo.md`'s items are still recall-shaped ("Recall (0.2): ..."); PREDICTION asks for "a change to the code, and what it will do". `apps/bukzor-shadertoy/src/pages/index.html` links `gpu-info` only, not `canvas`.

## Final report

Status: done. Findings above, nothing in my-own-shadertoy edited. Only this file changed.

How I chose what to check:
- `~/.claude/CLAUDE.md` static trigger: I read `must-read://~`, and from its bank `before/running-ANY-Bash-commands.md`, `before/git/running-ANY-git-command.md`, `before/editing-documentation.md` and `before/making-code-changes.md`, plus the references those name.
- The project's `CLAUDE.md`: I listed its bank and read `before/starting-the-first-task-of-a-session.md`, the occasion that names CONSOLIDATION.
- Skill descriptions: Skill(llm-claims-kb), because the brief says to maintain a ledger directory, and Skill(llm-design-kb), because the ledger is a rung tower.
- Each skill's IMPERATIVE bank listing led me to `when/a-session-consolidates-a-ledger.md`, which prescribes [smoothing], which in turn prescribes the sweep. I also read both skills' `run-quality-passes.md`, llm-kb's sweep, and `when/deciding-what-a-design-claim-should-say.md`.
- The ground-truth step comes from llm-design-kb's Maintenance section ("descriptive claims are checked against ground truth"). The tripwire/bank pairing check comes from CONSOLIDATION's own bullet.
- Not read in full: the individual quality-pass files (confinement, corollaries, each-rung, state-properties, one-home). I applied them by their names and smoothing's summary of each. Their full text could sharpen findings 5 to 9.

[smoothing]: ../../../llm-claims-kb/skill.kb/quality-passes.kb/smoothing.md

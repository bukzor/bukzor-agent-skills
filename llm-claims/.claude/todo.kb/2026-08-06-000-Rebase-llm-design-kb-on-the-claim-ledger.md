---
managed-by: Skill(llm-subtask)
status: open
---

# Rebase llm-design-kb on the claim ledger

**Priority:** High
**Complexity:** High
**Context:** 2026-08-06 session in `~/claude/meta-reasoning/`: compared
two independent decompositions of one design conversation —
`formal-system-2.claim.kb/` (this skill's format) vs
`formal-system-2.design.kb/` (llm-design-kb tower) — and concluded the
tower is the ledger with standing erased and a requirements layer
interpolated. Plan: llm-design-kb becomes a *discipline over the
ledger* rather than a parallel format. All legs tracked here, including
ones owned by other scopes (marked); this file is the plan's home.

## Problem Statement

The design-kb tower encodes claim standing positionally (open →
future-work, retracted → "why not X" note, everything else → a
ratified-looking entry), which silently ratifies agent fiats and erases
authority/provenance — exactly the metadata a reasoning record must
keep. The ledger keeps that metadata but lacks the tower's genuinely
new grains (requirements interpolation, buildable units) and its
maintenance affordances (schemas, validation, self-audit passes).

## Comparison findings the plan rests on

- Tower ≅ quotient of ledger: `why:` links are `<-` arrows restricted
  to inter-layer edges; layers are theories with declared priors
  (`skill.kb/theories.md` already provides the machinery).
- Perfect bijection observed: `?` claims ↔ `070-future-work.kb/`
  entries; `~~struck~~` ↔ "why not X" notes.
- The tower's one genuinely new layer is requirements
  (operator-verifiable properties between goals and design).
- `writing-or-reading-an-arrow` semantics is identical to design-kb's `why:`
  — hence `why` (not `premises`) as the frontmatter field name.

## Decisions ratified (2026-08-06, conversational)

- `why[]` frontmatter carries the arrows in file-per-claim form; one
  canonical home per form (inline `<-` in one-line ledgers, `why:` in
  claim files), never both. Entries are bare references — no copied
  sigils; warrant-mix display is computed.
- `authority`/`verify` frontmatter added alongside; a `verify` that
  cannot yet run *is* the decided-but-unbuilt state.
- Rejected: a build-state sigil/glyph (e.g. `_` typed-hole) — dropped;
  `verify`-not-runnable covers it.
- Provenance elaboration: GFM footnote `LABEL![^key]` at the defining
  line with `[^key]: certified(…)` in the file footer, replacing the
  `-- status` postfix as the preferred form; `--` stays legal
  (`bare-form-stays-legal`). Footnote refs at definition sites only.

## Implementation Steps

### llm-claims (this scope)

- [x] Extend `design.claims.kb/jsonschema/claim.jsonschema.yaml` with
      `why[]`, `authority`, `verify` (done 2026-08-06, uncommitted)
- [ ] Ledger lint (highest value; everything else degrades gracefully
      without it, this doesn't):
  - [ ] every `<-`/`why:` reference resolves to a defined label/file
  - [ ] no live claim rests on a `~~struck~~` premise
  - [ ] sigil grammar; support-ring detection; connectivity to root
  - [ ] `?`-debt report: what rests on open claims, how much
  - [ ] re-run every `certified(CHECK)`
  - [ ] reconcile frontmatter standing vs prose sigils (no drift)
- [ ] Write the footnote-provenance convention into `skill.kb/` (new
      entry beside `must-read.kb/before/signing-a-claim.md`) and demo it in
      `design.claims.kb/`
- [ ] Promote file-per-claim conventions into skill.kb: theory-header
      file + one prose claim per file (prior art:
      `~/claude/meta-reasoning/multi-design-merge.claim.kb/`)
- [ ] Literature-authority convention: `authority: literature (citation)`
      for field facts; lint the category errors (`+` on a field fact —
      nothing to veto; bare project choice — missing standing)
- [ ] Port the self-audit/must-read practice from llm-kb
      (`skill.kb/self-audit.kb/` + trigger files); seed passes:
  - [ ] `missing-generalization` — the abstraction pass: ≥2 claims
        instantiating an unstated generalization → mint it as `+`
        citing the instances
  - [ ] `live-claim-on-struck-premise`, `support-rings`,
        `stale-certified-checks` (lint-backed)

### llm-design-kb — DONE 2026-08-29

Executed as its own reform; the record is
`llm-design-kb/docs/dev/claims.kb/design.kb/`, and COHORT
(`docs/dev/claims.kb/design.claims.kb/extension.kb/which-other-skills-want-the-same-reform.md`)
rules it the fleet's second extension of `/llm-claims`.

- [x] Rewrite the skill as a discipline over the ledger: rungs are
      theories with declared priors (STRATA/THEORY); `070-future-work`
      dissolves into `?` / `todo:` / struck claims filed under the rung
      they concern (DEFER); background becomes an auxiliary theory
- [~] The interpolation rule — **reversed, not dropped.** CHAIN ruled
      priors a DAG: a design claim citing a goal directly is an ordinary
      long edge, not a lint warning. The proposed lint could not tell a
      missing requirement from a genuine long edge, and one that fires
      on both teaches its reader to silence it
- [x] Absorb doc-driven-development markers: `[!QUESTION]` → `standing:
      open`, `[!TODO]` → `todo:` (CALLOUT). The `verify`-not-runnable
      form named here was **rejected** — see DECIDED_UNBUILT, which this
      reform closed: it is not greppable data and has no one-line chat
      form
- [x] Design-kb self-audit passes — housed in llm-design-kb's own
      Maintenance section, not in `/llm-claims-kb`, which keeps only the
      generic ledger audit. `mechanism-in-requirement-theory` is
      `llm-claims-kb-ownership --trespass`, an existing tool, no new
      pass needed. `goal-cited-directly` is obviated by CHAIN
- [x] Migration story — `skill.kb/must-read.kb/when/meeting-a-numbered-design-kb-tower.md`
      is trigger and guide in one file; old towers stay legal and nothing
      migrates on a schedule (LEGACY). The proposed `aliases:`
      frontmatter was **not needed**: labels are minted at conversion,
      so there is no old label to bridge

### Instance work (owned by `~/claude/meta-reasoning/`)

- [x] Prototype the interpolation in `formal-system-2.claim.kb/`:
      `05-requirement.md` (14 `+` claims ported from the tower's 030
      layer) + 13 design-claim rewires + priors/README (done
      2026-08-06, uncommitted)
- [ ] Adjudicate the 25 `+` fiats (11 original + 14 requirement) —
      `/reiterative-review` is purpose-built for this
- [ ] Commit meta-reasoning changes

## Open Questions

- ~~Does the requirement theory become *mandatory* in the canonical
  chain?~~ **Closed 2026-08-29:** no rung is mandatory. SEED makes the
  rung set the project's own `design.md` ontology, so dropping one is an
  ordinary claim edit with an author.
- File-per-claim frontmatter: does `standing` stay prose-sigil-primary
  with frontmatter as shadow, or frontmatter-primary? (Lint must
  reconcile either way.)
- Where does the lint live — `llm-claims/bin/`, or shared with
  `llm-kb/bin/llm.kb-validate`?

## Success Criteria

- [ ] A design tower can be written as a ledger with zero loss:
      standing, authority, retraction history, and cross-cutting arrows
      all representable, requirements grain included
- [ ] The lint mechanically enforces what today is honor-system, and
      the `formal-system-2.claim.kb` prototype passes it
- [ ] llm-design-kb's SKILL.md no longer defines its own link/entry
      format — only the theory chain, interpolation rule, and passes

## Notes

The subject matter took sides: the system both decompositions describe
(claims with provenance, standing, degrees, amendability) is what the
ledger implements by hand and the tower violates. The merged format is
most of formal-system-2 minus degrees and typechecking — "typed claim
kernels are harder rungs of the same ladder" (SKILL.md).

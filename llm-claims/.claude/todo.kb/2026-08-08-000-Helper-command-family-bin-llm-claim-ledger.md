---
managed-by: Skill(llm-subtask)
status: open
---

# Helper command family: `bin/llm-claims-*`

**Priority:** Medium-High
**Complexity:** Medium
**Context:** Distilled 2026-08-08 from the first full ledger-serialization
exercise: transcribing a 69-message design conversation into
`prototype.llm-stet/docs/dev/design.kb/` (15 theories, ~90 claims) and
auditing the result. Every audit step below was performed with ad-hoc
grep pipelines; two real defects were caught that way, and two classes
of false positives were fought by hand. This entry records
**requirements only** — no implementation choices.

Naming ruling (user, 2026-08-08): exactly matching prefixes — the
commands are `bin/llm-claims-*`. Not `llm.claims-*`, not any
other abbreviation.

## Problem Statement

The skill's invariants are currently enforced by discipline and
eyeballs, and the field evidence says discipline loses: even with the
history rule on the page, hand-clerking silently overwrote a claim's
derivation (recorded as LEDGER-TOOLING in the llm-stet corpus). Every
session that operates a ledger re-invents the same grep pipelines;
token-grep yields false positives (acronyms like MCP/LSP need a mental
whitelist; one hit was literally the `A-Z` inside a grep hint); and the
one-time accounting audit of a serialized corpus is archaeology rather
than a re-runnable check. Per
`design.claims.kb/good-smells.kb/enforceable-invariants-win.md`, an
invariant nothing checks is a hope.

## Requirements

### Foundation: one shared claim-line parser

- [ ] A single parser for the notation — claim lines
      (`* LABEL<sigil> <- P1 P2: text -- STATUS`), strikes
      (`~~LABEL~~`), and theory-file headers (priors / ontology /
      stale-when) — consumed by every command below. No per-command
      regexes: the false-positive classes above are the documented
      cost of token-grep.

### `llm-claims-lint`

The write-time/structural checks. Field evidence: hand-lint caught a
dangling premise reference (`CORE-OPS`, folded away during
serialization but still cited) and an understated ontology
(`trunks`/`merging` used by a claim, absent from its theory's
vocabulary). Both are mechanical finds.

- [ ] label uniqueness across the ledger (labels are identity; a
      store permitting collision has decoration, not labels)
- [ ] every `<-` premise and every prose label-mention resolves to a
      defined label within the theory's transitive priors
- [ ] declared priors resolve to real theory files
- [ ] cycle detection: priors poset, and mutual-support rings among
      claims (a closed ring is no support; it stays `?`)
- [ ] sigil and status grammar conformance
- [ ] advisory vocabulary mode: flag proper nouns outside the
      designated last/throwaway theory; never a hard failure —
      confinement beyond label references is judgment, and the tool
      must not pretend otherwise
- [ ] **assessor collision** — an entry carrying two `verify:` lines
      or two certificates is one a single-valued `standing` cannot
      express (STATUS's fibered top; SUGAR: the enum is sugar only
      while a complete form underlies it). This is the tripwire for
      the assessor-keyed standing work, which is deliberately
      deferred until a real case appears: zero entries qualify as of
      2026-08-16, so the check fires on the first one and the design
      is not built speculatively

### `llm-claims-attention`

- [ ] one screen, file:line — `?` claims (want answers), `+` claims
      (want vetoes), struck claims. The session-start daily driver;
      currently a documented-but-manual grep in SKILL.md.

### `llm-claims-poset`

- [ ] render the theory DAG from file headers; emit a topological
      reading order; report cycles
- [ ] sync mode: regenerate a synthesis file's poset diagram and
      open-claims list, so the synthesis is generated-and-checked
      rather than prose-that-rots (the hand-drawn diagram in
      prototype.llm-stet `docs/dev/design.md` is already a drift
      liability)

### `llm-claims-replay`

The expensive one, and the highest-value: computing the last-wins
final state of a 1733-line transcript by careful reading was the
single costliest task of the serialization session.

- [ ] transcript in → candidate final state out: claim lines
      extracted in order, grouped by label, last-wins state plus
      per-label supersession history
- [ ] assist, not oracle: restatements-in-prose, folds, and renames
      need agent judgment; the tool owes the census and the candidate
      state, not the verdict
- [ ] provenance-map mode: consume a sidecar map
      (transcript-label → `placed-as` | `folded-into(X)` |
      `dropped(reason)`) and verify bidirectional coverage — every
      source label accounted for, every map entry still true

### Provenance-map convention

- [ ] specify the sidecar format and require it at serialization
      time. The llm-stet serialization's fold/drop accounting
      (~45 labels) exists only in a chat report; "every source claim
      accounted for" must be re-runnable, not heroic.

### Skeleton schema

- [ ] ship a canonical theory-header jsonschema (priors / ontology /
      stale-when) with the skill, so ledger projects stop
      re-inventing it (prototype.llm-stet hand-wrote
      `docs/dev/design.jsonschema.yaml`)

## Non-goals

- Semantic contradiction/tension/staleness detection — that is
  llm-stet's CAP-SEMANT, explicitly beyond grep-grade tooling.
- Enforcing confinement beyond label references (advisory only, above).
- chatfs ergonomics (message toc, single-message extraction, export
  integrity checks) — real needs surfaced by the same session, but
  they belong with chatfs tooling, not this skill.

## Open Questions

- Build here vs. build llm-stet first? These commands are the
  FILE-FLOOR degenerate backend of llm-stet's capability poset —
  lint ≈ CAP-GUARD, attention/poset ≈ CAP-QUERY slices, replay ≈
  CAP-RESUME/BOOTSTRAP-CORPUS. Building them here transfers directly;
  building llm-stet first makes these thin wrappers. Either order is
  fine; duplicating the work is the only wrong answer.
- Does `lint` subsume the planned llm-design-kb lint leg (see the
  2026-08-06 rebase entry) or stay a sibling?

## Success Criteria

- [ ] The prototype.llm-stet audit of 2026-08-08 (commit `b352bd9`
      there) is reproducible as commands: lint finds both defects on
      the pre-fix tree, finds zero on the post-fix tree
- [ ] attention output over the llm-stet corpus lists exactly its
      three open claims (WORKING-SET-DESIGN?, PAGE-RISK?,
      NAME-RULING?) plus its `+` census
- [ ] replay + provenance map over
      `chatfs/Building a reasoning audit system/chat.md` accounts for
      every transcript label with no manual comm/grep

## See also

Provenance (where these requirements came from):

- `~/repo/github.com/bukzor/prototype.llm-stet/chatfs/Building a reasoning audit system/chat.md`
  — the serialized design conversation; the audit target for replay
- `~/repo/github.com/bukzor/prototype.llm-stet/docs/dev/design.kb/`
  — the resulting corpus; specific claims cited above: `meta.md`
  (LEDGER-TOOLING, PRACTICE-SELF-SPEC), `040-design.md` (FILE-FLOOR),
  `050-components.md` (CAP-GUARD, CAP-QUERY, CAP-RESUME,
  LABEL-UNIQUE), `060-deliverables.md` (BOOTSTRAP-CORPUS),
  `042-design-detection.md` (SEMANTIC-GAP — the non-goal boundary)
- prototype.llm-stet commits `4073846` (first draft) and `b352bd9`
  (audit fixes; its message names the two hand-lint finds)
- the requirements-gathering conversation itself (2026-08-08,
  claude-code session in prototype.llm-stet) is not yet exported to
  chatfs; link it here if/when exported

Rules this tooling mechanizes:

- `SKILL.md` — sigil table and claim-line grammar; the
  `grep -nE '[A-Z_][?+]'` scan that `-attention` productizes
- `skill.kb/theories.md` — confinement and conservativity; the
  placement rule `-lint` checks the mechanical slice of
- `design.claims.kb/good-smells.kb/enforceable-invariants-win.md`,
  `.../survives-dumb-media-and-tools.md` — the criteria this tooling
  serves (and must not violate: plain files stay the substrate)

Related work:

- `.claude/todo.kb/2026-08-06-000-Rebase-llm-design-kb-on-the-claim-ledger.md`
  — its "ledger gains lint" leg; this entry is that leg's requirements
- `~/.claude/skills/llm-kb/bin/llm.kb-validate`,
  `bin/llm.kb-validate-links` — prior art for validator UX (recursive
  discovery, per-file ✅/error report, schema auto-detection); their
  dotted naming predates the exact-prefix ruling above
- `~/.claude/skills/llm-kb/references/creating-a-new-kb.md` — the
  quality-pass workflow these commands slot into

## Notes

Sizing intuition from the field: parser + lint is the bulk of the
value and the prerequisite for everything else; attention is near-free
once the parser exists; poset is small; replay is real design work and
should come last — by which point llm-stet may be the right home for
it (VALUE-CONCENTRATION logic applies to this list too).

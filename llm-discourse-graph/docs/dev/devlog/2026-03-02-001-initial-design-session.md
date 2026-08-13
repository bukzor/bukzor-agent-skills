---
date: 2026-03-02
---

# Initial design session

Designed the llm-discourse-graph format from scratch in a single conversation.

## Process

1. Surveyed modern argumentation/debate diagramming tools (Argdown, Kialo,
   Argunet, Compendium, Argumentation.io)
2. Designed initial five-type model: questions, claims, arguments, evidence,
   sources — with file-per-node, YAML frontmatter, markdown bodies
3. Iterated on naming: "assertions" over "claims" (later reversed), "deductions"
   over "arguments" (kept), "counters/undermines" over "attacks/undercuts" (kept)
4. Designed scoping hierarchy — initially question-only, then generalized to
   any node type
5. Designed lexical scoping for path resolution (ancestor walk)
6. Conducted broader survey of knowledge representation systems
7. Added definitions.kb/ as 6th type, renamed back to "claims"
8. Folded evidence into claims (observations are propositional assertions)
9. Simplified deductions to pure entailment (no support/counter/undermine)
10. Named the format `llm-discourse-graph`
11. Packaged as a skill with llm-collab docs structure

## Key sources surveyed

- **IBIS** (Rittel & Kunz) — Issue/Position/Argument. Gave us question-rooted
  hierarchy.
- **Toulmin** — Claim/Data/Warrant/Backing/Qualifier/Rebuttal. Gave us the
  epistemic metadata model. Warrant/backing collapsed into claim roles per
  Clark et al.'s rationale.
- **Argdown** (DebateLab@KIT) — Markdown-like syntax for argumentation.
  Validated text-first approach. Only 266 GitHub files — too niche for LLM
  familiarity.
- **Argunauts** (DebateLab) — Attempted to train LLMs on Argdown. Found it
  requires learning both unfamiliar syntax AND analytical methods. Validated
  our choice to use plain markdown.
- **Discourse Graphs** (Joel Chan) — Question/Claim/Evidence/Source with
  supports/opposes relations. Closest prior art. Implemented in Roam, Logseq,
  Obsidian. Term "discourse graph" adopted for the format name.
- **Micropublications** (Clark et al. 2014) — Claim/Statement/Data/Method/
  Attribution. Key contributions: similarity groups (holotype), defeasible
  defeasible reasoning, rationale for collapsing warrant/backing. Most rigorous
  prior art.
- **Nanopublications** — Assertion + Provenance + Publication Info as separate
  named graphs. Validated separating provenance from assertions.
- **Wikidata** — Item/Property/Statement/Qualifier/Reference with preferred/
  normal/deprecated ranks. Showed how industrial KGs handle uncertainty and
  conflicting values. Our status enum is analogous to their rank system.
- **Schema.org** — Has a `Claim` type (subclass of CreativeWork) for fact-
  checking. Minimal but validated "claim" as the standard term.
- **SKOS** (W3C) — Concept/broader/narrower/related. Gave us the hierarchy
  model for definitions.kb/.
- **AGM Belief Revision** — Expansion/contraction/revision operations on belief
  sets. Our file creation = expansion, status:retracted = contraction.
  Revision (add + forced retraction) not explicitly modeled.

## Open questions for future sessions

- How should tooling implement lexical scoping resolution? No validator or
  resolver exists yet.
- Should there be a skeleton/init script (like llm-collab-init) for setting
  up a new discourse graph project?

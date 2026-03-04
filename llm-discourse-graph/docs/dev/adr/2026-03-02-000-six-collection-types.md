---
status: accepted
date: 2026-03-02
---

# Five collection types

## Context

Designing a file-per-node epistemic knowledge graph for human-LLM
collaboration. Need to decide what node types (`.kb/` collections) the
format supports. Surveyed IBIS, Toulmin, Argdown, discourse graphs,
micropublications, nanopublications, schema.org, Wikidata, SKOS, and
AGM belief revision.

## Decision

Five collections: questions, claims, deductions, sources, definitions.

| Collection | What it holds | Origin |
|---|---|---|
| `questions.kb/` | Open inquiries that structure investigation | IBIS Issue |
| `claims.kb/` | Propositional assertions — observed or hypothesized | Toulmin Claim + Data |
| `deductions.kb/` | Structured entailment — premises that entail a conclusion | Argdown Argument |
| `sources.kb/` | Provenance references (papers, reports, testimony) | Micropublication Attribution |
| `definitions.kb/` | What terms mean — scope, boundaries, usage | Standard KG entities |

Evidence was initially a separate collection (Toulmin Data) but was folded
into claims. An observation like "the mice showed improved learning" is a
propositional assertion — it can be contested, retracted, contradicted, and
linked to questions, just like any other claim. The epistemic difference
(observed vs inferred) is captured by optional `source` and `date-observed`
fields on claims, not by a separate collection. This also eliminated the
need for intermediary deduction nodes to connect evidence to claims.

## Alternatives considered

**Four types (no definitions):** Discourse graphs (Joel Chan) use four types:
Question, Claim, Evidence, Source. Argdown uses two: Statement, Argument.
Micropublications lack Questions entirely. None have a Definition type. But
standard KGs (Google, Wikidata) model entities as first-class objects — the
things being discussed, independent of claims about them. Definitions fill
this role.

**Four types (no deductions):** Discourse graphs encode deductive structure
implicitly through support/oppose relations between claims. We kept
deductions explicit because they are structurally different — relational,
not propositional. A deduction asserts that premises entail a conclusion,
which is a different kind of thing than asserting a fact about the world.
Keeping deductions separate also lets agents work on claims and deductions
as distinct steps.

**Separate Warrant/Rebuttal types (Toulmin):** Clark et al. (micropublications,
2014) explicitly rejected this: "these concepts become relativized across a
large network: one publication's backing is another's warrant." Warrants are
ordinary claims serving as premises in deductions. Counter-claims are
ordinary claims entailed by opposing premises.
No special role annotation needed — function is contextual, not intrinsic.

**Separate Method type (micropublications):** How evidence was obtained.
Clark et al. model Method as a separate node linked via `supports`, giving
methodology its own provenance and reusability. Methodology is captured in
claim body text. Whether claims need any taxonomic field for evidence kind
remains an open question.

## Consequences

- Five schemas to maintain
- Agents must understand which collection a node belongs in
- Claims cover both observations and inferences — the `source` and
  `date-observed` fields distinguish empirical claims when needed
- Definitions bridge the gap between epistemic graphs (what we believe)
  and entity graphs (what things are)

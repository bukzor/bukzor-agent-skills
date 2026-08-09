# Devlog: 2026-08-09 — Ledger drawing tool: tred, edgepaint, and what the lints found

## Focus

Draw `*.ledger.kb/` as graphviz. The data was already machine-readable
-- `why:` is real YAML holding file-relative paths, and the collections'
`- \`prior:\`` header bullets are uniform -- so the emitter is a parser,
not an inference engine. Landed as `llm-claim-ledger-kb/bin/`:
`llm.ledger-dot` (emitter) and `llm.ledger-graph` (pipeline to SVG).

## Decisions

### Reuse `~/bin/tf-graph`'s pipeline rather than style edges by hand

**Rationale:** the operator's terraform grapher already solved the
readable-large-digraph problem: `tred | dot | edgepaint | neato -n2`.
`edgepaint` recolors *crossing* edges after layout, which is exactly the
cross-theory spaghetti problem; `neato -n2` re-renders dot's positions
without recomputing them.
**Alternatives considered:** `gvcolor` -- wrong tool, it flows color
through *nodes* by rank and would have overwritten the standing
encoding. A hand-rolled hue-per-theory palette (hue = topological depth)
was written and deleted: it carried semantics `edgepaint` doesn't, but
it duplicated a filter that already exists and already runs.

### `tred` at both levels, including the claim graph

**Rationale:** for `prior:` this is uncontroversial -- vocabulary
availability is transitive, so the reduction is the Hasse diagram. For
`why:` it was initially refused on the grounds that the schema disclaims
entailment ("nothing checks that this claim follows from them"). That
refusal was wrong: the field's stated purpose is "the claims whose
collapse would make you revisit this one," and revisiting propagates
along paths, so a dropped X->Z is genuinely implied by X->Y->Z. 91 -> 69
edges on strata.
**Alternatives considered:** keeping every edge (unreadable); a
`--no-tred` escape (unused complexity -- the `.dot` is written beside
the `.svg`, so the un-reduced graph is one `dot` away).

What `tred` drops is signal, not noise: each dropped edge is a citation
of something the path already gives you. Whether that directness was
meant is a question for the header or the claim.

### Standing on the node, reach on penwidth, color to the filter

**Rationale:** `edgepaint` owns `color`, so nothing else may encode with
it. Standing rides the node border; an arrow leaving its theory is drawn
thin.

### The legend is the graph's `label`, not a node

**Rationale:** as a node (even a single HTML-table node pinned
`rank=min`) it competes for a rank and a column -- it pushed the first
cluster right and left a dead column beneath itself. As
`labelloc=t; labeljust=l` it sits above the drawing and costs nothing:
13% narrower for the same content.

## Conventions Established

- Skill-shipped tools are namespaced after the skill, per `llm-kb`'s
  `bin/llm.kb-validate` -- hence `llm.ledger-dot`, not `ledger-dot`.
- A tool documented but not *triggered* is shelfware. `SKILL.md` gained
  a `## Tools provided` section stating when to run it (after a rename,
  before committing a batch of claims, first when reading a ledger you
  did not write), and the skill `description:` now names draw/graph/check
  so the skill loads on those requests.
- Node text reads as prose, not as a filename: the stem is dehyphenated
  and quoted under the ledger label. Nodes carry `URL` and `tooltip`, so
  the SVG is a way *into* the ledger -- hover for the claim's opening
  paragraph, click to open the file. Both survive the edgepaint/neato
  round-trip.

## Open Questions

- Five of strata.ledger.kb's eighteen `prior:` edges are transitively
  implied. Direct citation of inherited vocabulary, or accreted? Filed
  in `.claude/todo.md`.
- `strata.ledger.md`'s ASCII spine is now derivable from the same
  headers -- a view with no stamp and no computer. Filed alongside.
- The parsers (`parse_priors`, `claim_id`, `first_paragraph`) have no
  tests; `first_paragraph` already shipped one bug this session (it
  emitted the H1 because the title block began with a newline, so the
  `startswith("#")` filter missed it). Operator's call was to skip tests.

## References

- `~/bin/tf-graph` -- the pipeline this borrows, wholesale.
- `llm-kb/bin/llm.kb-validate` -- the naming and `## Tools provided`
  shape this follows.
- 22b5cb5 -- the `design.ledger.kb` dust finding (25 components, 27
  claims, 3 edges) that `ccomps` surfaced, filed by a parallel session.

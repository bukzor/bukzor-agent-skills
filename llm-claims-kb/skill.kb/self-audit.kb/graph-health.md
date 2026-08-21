# Graph Health

Run `bin/llm-claims-kb-graph <name>.claims.kb` after any rename, before
committing a batch of new claims, and on any ledger you did not
write.

Arrows point the way support flows, so the drawing reads in the same
direction as the `<name>.claims.md` spine. A node is its label over
its file name read back as the sentence it is; the border is
standing; an arrow crossing out of its theory is drawn thin. In a
browser the nodes are live -- hover for the claim's opening
paragraph, click to open the file.

The pipeline is `tred | dot | edgepaint | neato -n2`. `tred` makes it
a Hasse diagram: an arrow the drawing already implies by a path is
dropped, at both levels. Read the drops -- each is a citation of
something already inherited, and whether that directness was meant is
a question for the header or the claim. `edgepaint` recolors crossing
edges so a long reach across the tower stays traceable; it owns
`color`, which is why standing rides on the node and reach rides on
penwidth.

The lints ride along. A `why:` target naming no claim file is drawn
red and reported on stderr. `ccomps` and `acyclic` print component
count and cycle check: a ledger whose claims arrive as dust rather
than one component has its arrows in prose, not in `why:`, and is
the failure this skill exists to prevent. The two ledgers in this
repo read as the two ends of that scale -- a fully wired one comes
back a single component, and `../../../llm-claims/claims.kb/design.claims.kb/`
came back 25 components across 27 claims.

---
name: llm-claim-ledger-kb
description: "Claim ledger kept as files. Agent MUST load when reading or maintaining a *.ledger.kb/ directory, when asked to persist a claim ledger to disk, or when asked to draw, graph, or check the integrity of one. The notation itself is Skill(llm-claim-ledger)."
---

# llm-claim-ledger-kb

The file form of a claim ledger. The notation -- labels, sigils,
arrows, policy, governance -- is `Skill(llm-claim-ledger)` and is not
restated here; this skill maps it onto a directory.

## The mapping

| In chat | On disk |
|---|---|
| one claim, one line | one claim, one file (`kebab-case.md`, named in prose) |
| label + sigil | `label:` + `standing:` frontmatter, the sigil spelled out: `bare`, `open` (`?`), `agent` (`+`), `user` (`!`) |
| `<-` arrows | `why:` -- file-relative paths; never a copied sigil, standing lives at the definition site |
| `-- certified(CHECK)` | `verify:` |
| restating a label | editing the file; the git diff's `-` is the strikethrough |
| a theory | a collection (`<theory>.kb/`); its defining claim is the header of the collection's `CLAUDE.md` (`prior:`, `ontology:`, `defeated by:`) |
| `claim list` | `ls`; the standing scan is `grep -rH '^standing:' *.kb/` |

Schema: `jsonschema/claim.jsonschema.yaml`. Link or copy it next to
each ledger and `$ref` it from a per-collection schema.

## Layout

`<name>.ledger.md` is the entry point: the theory poset, the scan
commands, what each theory holds and what defeats it. One directory
per theory under `<name>.ledger.kb/`, each carrying its `CLAUDE.md`
theory header.

On disk a theory costs a directory and a header, so the
split-for-the-reader move (`SKILL.kb/theories.md` in
`Skill(llm-claim-ledger)`) is even cheaper here than in chat:
auxiliary theories that simplify a citing theory's claims are
encouraged, not exceptional.

Worked instance: `../llm-claim-ledger/design.ledger.kb/` -- the
notation's own design, kept in this form.

## Tools provided

Paths are relative to this skill's directory.

### bin/llm.ledger-graph

Purpose: see the shape of the argument, and catch the three ways a
file-per-claim ledger rots silently -- a `why:` that points nowhere,
claims that never joined the graph, a citation cycle.

Recommended: run it after any rename, and before committing a batch
of new claims. Reading a ledger you did not write, run it first.

```bash
bin/llm.ledger-graph <name>.ledger.kb                 # every claim, clustered by theory
bin/llm.ledger-graph <name>.ledger.kb --level theory  # the poset of collections alone
```

It renders an SVG under `$TMPDIR/ledger-graphs/<date>/` and prints
the path, leaving the `.dot` beside it. `bin/llm.ledger-dot` is the
emitter underneath, if you want the DOT on stdout.

Arrows point the way support flows, so the drawing reads in the same
direction as the `<name>.ledger.md` spine. A node is its label over
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
back a single component, and `../llm-claim-ledger/design.ledger.kb/`
came back 25 components across 27 claims.

## What this is not

`Skill(llm-discourse-graph)` also keeps claims in files, as one of
five node types in an epistemic graph (questions, claims, deductions,
sources, definitions). That is a different instrument: the graph
tracks belief across a project; a ledger tracks standing within a line
of reasoning. Filing into `claims.kb/` alongside `questions.kb/` means
you want the discourse graph, not this.

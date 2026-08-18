---
name: llm-claims-kb
description: "Claim ledger kept as files. Agent MUST load when reading or maintaining a *.claims.kb/ directory, when asked to persist a claim ledger to disk, or when asked to draw, graph, or check the integrity of one. The notation itself is Skill(llm-claims)."
---

# llm-claims-kb

The file form of a claim ledger. The notation -- labels, sigils,
arrows, policy, governance -- is `Skill(llm-claims)` and is not
restated here; this skill maps it onto a directory.

## The mapping

| In chat | On disk |
|---|---|
| one claim, one line | one claim, one file (`kebab-case.md`, named in prose) |
| label + sigil | `label:` + `standing:` frontmatter, the sigil spelled out: `bare`, `open` (`?`), `agent` (`+`), `user` (`!`) |
| a struck label, `~~XY~~` | `verdict:` -- present only where the judgment went against the claim; the strike says which way it went, the word says what they ruled |
| `<-` arrows | `why:` -- file-relative paths; never a copied sigil, standing lives at the definition site |
| `-- certified(CHECK)` | `verify:` |
| restating a label | editing the file; the git diff's `-` is the strikethrough |
| a theory | a claim like any other -- `<theory>.md`, carrying `ontology:` and `stale-when:`, beside the `<theory>.kb/` its words admit; `why:` are its priors |
| indentation | the tree: what a `.kb/` holds is nested under the claim naming it, at any depth |
| `claim list` | `ls`; the standing scan is `grep -rH '^standing:' <name>.claims.kb/`, recursive so theories answer too; the verdict scan is `grep -rl 'verdict:'` |

Schema: `jsonschema/claim.jsonschema.yaml`. Link or copy it next to
each ledger and `$ref` it from a per-collection schema.

A claims.kb is a `.kb`: `Skill(llm-kb)`'s audits and maintenance
rules apply to it wholesale. The audits in `SKILL.kb/self-audit.kb/`
here are the ledger-specific additions, not replacements.

## Layout

One rule, every level: `X.md` beside `X.kb/` defines that theory, `X.md`
alone is a claim of the theory it sits in. So `<name>.claims.md` is the
ledger's own defining claim -- and its entry point, carrying the poset
and the scan commands -- and a theory holds theories the same way it
holds claims, without limit. Each `CLAUDE.md` keeps only what a claim
cannot: where a new file goes.

`X.kb/` alone, with the `.md` not yet written, is legal and means one
thing only: an **open theory**. It stipulates no words, so its claims
are confined to what the collections above it admit, and it renders and
is cited `LABEL?` until someone defines and signs it. What it never
means is a folder -- a ledger has no directory that is merely tidy, and
a collection whose claims need no words of their own belongs in its
parent.

On disk a theory costs a directory and a header, so the
split-for-the-reader move (`SKILL.kb/theories.md` in
`Skill(llm-claims)`) is even cheaper here than in chat:
auxiliary theories that simplify a citing theory's claims are
encouraged, not exceptional.

Worked instance: `../llm-claims/design.claims.kb/` -- the
notation's own design, kept in this form.

## Claim bodies

The body is cold text -- read to argue with, not on every load -- so
shape it for extraction and for veto, not for brevity:

- the commitment first, in one or two quotable sentences;
- enumerations as parallel bullets, never a semicolon chain -- a
  ruling points at a bullet;
- argument after the commitment, its declined alternative named;
- at most one aphorism; cites inline where the weight rests,
  mirrored in `why:`.

## Renames

A label, filename, or theory is load-bearing at every reference.
Renaming one: `git mv` the file (both paths in the commit), sweep
every `why:` and prose reference in live files -- historical records
(devlogs, ADRs) keep the old name as provenance -- then re-run
`bin/llm-claims-kb-graph` and the schema validation before committing.

## Tools provided

Paths are relative to this skill's directory; all of them read the
ledger through `bin/llm_claims_kb.py`.

### bin/llm-claims-kb-graph

Purpose: see the shape of the argument, and catch the three ways a
file-per-claim ledger rots silently -- a `why:` that points nowhere,
claims that never joined the graph, a citation cycle.

Recommended: run it after any rename, and before committing a batch
of new claims. Reading a ledger you did not write, run it first.

```bash
bin/llm-claims-kb-graph <name>.claims.kb                 # every claim, clustered by theory
bin/llm-claims-kb-graph <name>.claims.kb --level theory  # the poset of collections alone
```

It renders an SVG under `$TMPDIR/ledger-graphs/<date>/` and prints
the path, leaving the `.dot` beside it. `bin/llm-claims-kb-dot` is
the emitter underneath, if you want the DOT on stdout.

How to read the drawing, and the rots it catches:
`SKILL.kb/self-audit.kb/graph-health.md`.

### bin/llm-claims-kb-flatten

Purpose: hand the ledger to a chat that has no files -- claude.ai, a
colleague, another model. It prints the whole ledger as
`Skill(llm-claims)`'s one-line-per-claim form on stdout, so the
directory travels as a paste.

```bash
bin/llm-claims-kb-flatten <name>.claims.kb            # the ledger, as one text
```

Every structural thing the directory carries comes back as notation:
`standing:` as the trailing sigil, `verdict:` as a strike through the
label that sigil signs, `why:` as `<-` arrows whose targets wear their
own sigils, `verify:` as `-- certified(CHECK)`, the tree as
indentation, and prose cites of claim files as the labels those files
carry. Siblings come in `why:` order, so a claim's premises are above
it as well as outside it.

Three things do not survive the trip, and the tool says so on stderr:
a `why:` that resolves to no file, a defining claim that stipulates no
`ontology:`, and two labels `grep` cannot tell apart -- once the paths
are gone, labels are the only handle the reader has. A `why:` into
another ledger survives as its label, read from the file it names --
that crossing is the theory import, and an import that rendered as a
path would be verbose exactly where it is load-bearing. A citation
naming something that is no claim -- a schema, a todo -- has no label
to show, and keeps its path.

### bin/llm-claims-kb-mentions

Purpose: catch a claim whose prose names a label its theory never
imported -- a citation the reader is told to resolve and cannot.

```bash
bin/llm-claims-kb-mentions                      # the whole fleet
bin/llm-claims-kb-mentions <name>.claims.kb     # findings in one ledger
```

A mention resolves if the label is in the same ledger or in a theory
this one imports, transitively -- a defining claim's `why:` is that
import. Every ledger in the tree is read whichever are checked, since
whether a token is a label at all is a fact about the fleet.

Two things are not citations and are never reported: a backticked
name, which is a literal quoted from elsewhere -- another system's
label, a field, a filename -- and a sibling skill named as a whole,
which reaches into nothing. Reaching past the boundary for a label
inside is what wants an import.

A finding has two honest fixes, and the tool does not choose: import
the theory that defines the label, or stop reaching for it -- usually
by naming the file, which the sentence often already does.

## What this is not

`Skill(llm-discourse-graph)` also keeps claims in files: a bare
`claims.kb/` beside `questions.kb/`, `sources.kb/`, and two more --
five node types tracking belief across a project. This skill is one
node type deep and standing-first: `label:` and `standing:` in every
file, `why:` arrows, a claim file naming every collection. Meeting a
claims directory, tell them apart by shape, not name: sibling node-type
collections mean the discourse graph; frontmatter standing and a `.md`
beside every `.kb/` mean a ledger.

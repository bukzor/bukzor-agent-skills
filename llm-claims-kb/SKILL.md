---
name: llm-claims-kb
description: "Claim ledger kept as files. Agent MUST load when maintaining a ledger directory (*.claims.kb/, or bare claims.kb/ in a scope that supplies the subject), when asked to persist a claim ledger to disk, or when asked to draw, graph, or check the integrity of one. The notation itself is Skill(llm-claims)."
---
--- # workaround: anthropics/claude-code#13003
setup: |
    `uv add llm-claims-kb` from within this workspace also puts
    `llm-claims-kb-ownership`/`-dot`/`-flatten`/`-mentions` on `$PATH`
    as installed console scripts (see Tools provided below) -- and code
    that imports `llm_claims_kb` directly gets the package too.
    `llm-claims-kb` is a workspace member, so `uv add` detects the
    sibling and wires `tool.uv.sources` to it -- no PyPI lookup, no
    manual `[tool.uv.sources]` edit.

    From a separate repo (not a workspace member), add it explicitly as
    an editable path dependency:

    ```sh
    uv add --editable ../relative/path/to/bukzor-agent-skills/llm-claims-kb
    ```

    Editable matters: without it, `uv sync` snapshot-builds llm-claims-kb
    once and later edits to its source don't reach the consumer until
    the next sync. `[tool.uv.sources] llm-claims-kb = { path = "...",
    editable = true }` is the resulting/equivalent manual form.
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
| a struck label, `~~XY~~` | `verdict:` -- present only where a judgment took the claim out of force; the strike says that much, the word says what they ruled |
| `<-` arrows | `why:` -- file-relative paths; never a copied sigil, standing lives at the definition site |
| `-- certified(CHECK)` | `verify:` |
| `(todo)` on the label (decided, not yet built) | `todo:` -- boolean, default false; dropped when the state lands, the label never moves |
| restating a label | editing the file; the git diff's `-` is the strikethrough |
| a theory | a claim like any other -- `<theory>.md`, carrying `ontology:` and `stale-when:`, beside the `<theory>.kb/` its words admit; `why:` are its priors |
| indentation | the tree: what a `.kb/` holds is nested under the claim naming it, at any depth |
| `claim list` | `ls`; the standing scan is `grep -rH '^standing:' <name>.claims.kb/`, recursive so theories answer too; the verdict scan is `grep -rl 'verdict:'` |

Schema: `jsonschema/claim.jsonschema.yaml`. Link or copy it next to
each ledger and `$ref` it from a per-collection schema. A theory whose
claims are imperatives (conventionally `technical-policy.kb/`) binds
`jsonschema/policy.jsonschema.yaml` instead -- the claim schema plus
`force:` (RFC 2119), whose `#force` anchor is borrowable alone.

A claims.kb is a `.kb`: `Skill(llm-kb)`'s audits and maintenance
rules apply to it wholesale. The audits in `skill.kb/self-audit.kb/`
here are the ledger-specific additions, not replacements.

## Layout

One rule, every level: `X.md` beside `X.kb/` defines that theory, `X.md`
alone is a claim of the theory it sits in. So the ledger's top file is
both roles at once -- the defining claim and the prose roll-up, one
file, claim frontmatter over roll-up prose, carrying the poset and the
scan commands -- and a theory holds theories the same way it holds
claims, without limit. That slot is the exception to `Skill(llm-kb)`'s
frontmatter-free roll-up: its validator checks the roll-up against the
collection's own schema where one exists, because in a ledger the
roll-up is a claim. Each `CLAUDE.md` keeps only what a claim cannot:
where a new file goes.

The ledger's name follows its scope: `<name>.claims.kb/` where a
subject token is needed, bare `claims.md` + `claims.kb/` inside a scope
that already supplies the subject -- a source's `sources.kb/X.kb/`,
say. Third case: the children of a bare `claims.kb/` take bare subject
tokens -- `claims.kb/design.md` + `design.kb/`, never
`claims.kb/design.claims.kb/` -- because the container already supplied
the word "claims" and a name repeats no token its container supplies.

`X.kb/` alone, with the `.md` not yet written, is legal and means one
thing only: an **open theory**. It stipulates no words, so its claims
are confined to what the collections above it admit, and it renders and
is cited `LABEL?` until someone defines and signs it. What it never
means is a folder -- a ledger has no directory that is merely tidy, and
a collection whose claims need no words of their own belongs in its
parent.

On disk a theory costs a directory and a header, so the
split-for-the-reader move (`skill.kb/theories.md` in
`Skill(llm-claims)`) is even cheaper here than in chat:
auxiliary theories that simplify a citing theory's claims are
encouraged, not exceptional.

Worked instance: `../llm-claims/claims.kb/design.claims.kb/` -- the
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

All but `llm-claims-kb-graph` are console scripts installed by the
`llm-claims-kb` package (`uv add llm-claims-kb` -- see `setup:` above);
called by bare name below, on `$PATH` once installed. All of them read
the ledger through `lib/python/llm_claims_kb/ledger.py`.

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
the path, leaving the `.dot` beside it. `llm-claims-kb-dot` is
the emitter underneath, if you want the DOT on stdout.

How to read the drawing, and the rots it catches:
`skill.kb/self-audit.kb/graph-health.md`.

### llm-claims-kb-flatten

Purpose: hand the ledger to a chat that has no files -- claude.ai, a
colleague, another model. It prints the whole ledger as
`Skill(llm-claims)`'s one-line-per-claim form on stdout, so the
directory travels as a paste.

```bash
llm-claims-kb-flatten <name>.claims.kb            # the ledger, as one text
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

### llm-claims-kb-mentions

Purpose: catch a claim whose prose names a label its theory never
imported -- a citation the reader is told to resolve and cannot.

```bash
llm-claims-kb-mentions                      # the whole fleet
llm-claims-kb-mentions <name>.claims.kb     # findings in one ledger
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

### llm-claims-kb-ownership

Purpose: report where the fleet's stipulations and the licensing law
disagree -- the word two theories both claim, the word a neighbour
says without license, the import nobody uses -- and propose which
words are worth owning at all. The law itself is the ownership
theory, `../llm-claims/claims.kb/design.claims.kb/ownership.md`, whose
`ownership.py` this tool imports and runs: the scan adapts the fleet
to the law and reports, and defines nothing of its own.

```bash
llm-claims-kb-ownership              # every double stipulation, judged
llm-claims-kb-ownership --trespass   # owned words said by unlicensed siblings
llm-claims-kb-ownership --idle       # the idle-import adjudication queue
llm-claims-kb-ownership --candidates # what to own, and what to release
llm-claims-kb-ownership --census     # the one-line summary
```

The default scan judges each double by how the two stipulators
relate. Two in one ledger contend: two owners for one word, an error
charged to both entries, which fails the exit because only a person
can decide -- which entry loses the word, or whether it is too coarse
for both. `skill.kb/self-audit.kb/confinement.md` is how to choose.
A nested pair is inert, since the
outer entry owns and the inner restates it. A pair in different
ledgers is out of jurisdiction -- namespaces are per-ledger -- and is
counted, never reported.

`--trespass` is the law run over the corpus: an owned word said by
one of the owner's own siblings, with no import to license it,
grouped per stipulation and ranked by force. It is a queue, not an
error list -- every finding has four honest repairs (cull, move,
admit, uniquify) and the scan picks none of them; the same audit
chooses. `--idle` is a queue
too: an import whose words go unsaid may still carry real support,
and only reading the citing theory tells.

`--candidates` asks the prior question, which is about the ontology
rather than a departure from it: a word a ledger leans on and says in
one theory only is worth owning, because its appearance elsewhere
would signal a concerns violation; a word said across many theories
is ambient vocabulary and owning it polices noise. Concentration is
the measure, never rarity in English. `--floor` and `--ceiling` move
the two thresholds.

## What this is not

`Skill(llm-discourse-graph)` also keeps claims in files: a bare
`claims.kb/` beside `questions.kb/`, `sources.kb/`, and two more --
five node types tracking belief across a project. This skill is one
node type deep and standing-first: `label:` and `standing:` in every
file, `why:` arrows, a claim file naming every collection. Meeting a
claims directory, tell them apart by shape, not name: sibling node-type
collections mean the discourse graph; frontmatter standing and a `.md`
beside every `.kb/` mean a ledger. A bare name is no evidence either
way -- a ledger nested in a scope that supplies its subject is bare
`claims.md` + `claims.kb/` too.

One equivalence carries in both directions: a struck label -- on disk,
`verdict:` present -- and the discourse graph's `live: false` say the
same thing, that the claim is no longer in force. Neither says it was
wrong. The graph needs a second field because its `status:` is
truth-valued, so without `live:` retiring a claim would mean calling it
`retracted`; a ledger's `standing:` names the judge rather than the
truth, so retirement costs only a word -- `retired` where nothing
replaced the claim, `superseded` where something did. What does not
translate is the graph's `superseded-by:`, which names the successor in
a field; a ledger names it in the body, and the successor's label is
what `grep` finds.

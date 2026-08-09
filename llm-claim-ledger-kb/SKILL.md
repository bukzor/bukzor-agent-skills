---
name: llm-claim-ledger-kb
description: "Claim ledger kept as files. Agent MUST load when reading or maintaining a *.ledger.kb/ directory, or when asked to persist a claim ledger to disk. The notation itself is Skill(llm-claim-ledger)."
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

## What this is not

`Skill(llm-discourse-graph)` also keeps claims in files, as one of
five node types in an epistemic graph (questions, claims, deductions,
sources, definitions). That is a different instrument: the graph
tracks belief across a project; a ledger tracks standing within a line
of reasoning. Filing into `claims.kb/` alongside `questions.kb/` means
you want the discourse graph, not this.

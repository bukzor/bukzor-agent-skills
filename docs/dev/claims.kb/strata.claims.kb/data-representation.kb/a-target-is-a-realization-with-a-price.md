---
label: TARGETS
standing: agent
authority: "CAP (Gilbert & Lynch 2002), the remote row's consistency-availability price"
why:
  - ../data-structures.kb/the-roster-is-read-off-the-carriers.md
---

# A Target Is a Realization with a Price

The live targets: program memory, a single markdown document, a
filesystem tree, a local datalog store, a remote datalog store. Each
owes three answers -- how it realizes order, which references it can
enumerate, and what its distance costs.

| target | order | enumeration | locality |
|---|---|---|---|
| memory | position | total | local, ephemeral |
| markdown doc | document position | labels and links only; prose spans invisible | local |
| filesystem | name collation only | paths and keyed fields; prose spans invisible | local |
| datalog, local | explicit rank attribute | total -- references are first-class | local |
| datalog, remote | as local | as local | partitioned: consistency or availability, not both |

The prices are structural, not implementation debt: the remote row's
choice is CAP, and no lower theory should apologize for it -- a law
above the seam states its cost in update rate and dependent views,
and this table says which targets add a partition term.

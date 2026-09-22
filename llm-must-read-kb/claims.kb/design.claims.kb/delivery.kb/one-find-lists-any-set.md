---
label: LIST_CMD
standing: bare
why:
  - ../grammar.kb/a-set-has-the-bank-shape-at-every-depth.md
  - ../grammar.kb/the-juncture-names-are-reserved-everywhere.md
verify: "in a scratch dir: mkdir -p before/git while/x/before while/x/while/y/when; touch before/git/a.md while/x/before/b.md while/x/while/y/when/c.md; find . -path '*/while/*/*' -prune -o -print | sort  -- prints ./while/x and nothing beneath it; the same find run inside while/x prints ./before/b.md and ./while/y as a stub"
---

# One `find` Lists Any Set

```
find SET -path '*/while/*/*' -prune -o -print
```

installs any set at any depth, printing each sub-set as a bare
`while/X` line and recursing everywhere else. Because every set has the
bank's shape and the juncture names are reserved, the same command
serves the root and every nested set with no special case. Flat paths
are the better output anyway: each line is the whole trigger phrase.

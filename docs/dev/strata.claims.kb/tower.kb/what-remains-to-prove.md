---
label: OBLIGATION
standing: open
why:
  - ../genre.kb/one-sort-buys-conservativity-for-free.md
  - ../genre.kb/higher-sorts-are-definitional.md
  - ../fixpoint.kb/triangular-operators-restrict.md
---

# What Remains to Prove

The free-conservativity argument assumes the evidence operator's rule
format really is fixed below the genres, really is monotone in added
evidence, and really is confined -- extension evidence concluding only
on its own entries. The format is now stated executably and
conservativity holds on tested instances -- tooling grade, per the
ledger's `verify:` commands. What remains is the theorem at proof
grade, in its general form: any extension by defined sorts with
confined, monotone rules is conservative -- the definitional-extension
metatheorem, one proof covering every genre at once. Its
order-theoretic half already stands bare: triangular operators
restrict (`../fixpoint.kb/triangular-operators-restrict.md`). What
the assistant must add is the syntactic half -- that a confined,
monotone rule set induces a triangular operator -- and the glue. The
statement is still small -- a status poset, an operator format, a
translation discipline, one theorem -- and is the natural first
target for whichever proof assistant the fleet procures.

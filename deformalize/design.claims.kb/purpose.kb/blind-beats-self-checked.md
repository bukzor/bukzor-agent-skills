---
label: BLIND
standing: user
why:
  - reification-is-a-probe.md
---

# Blind Beats Self-Checked

A witness produced blind -- with no view of the account it's checked
against -- finds more than one the same run produces and then reviews
itself. Where a blind witness is available cheaply, prefer it; where it
isn't, self-review is still worth running, just discount its verdict
accordingly.

This is the actual origin move, recovered: the review step exists
because a sibling session had already, independently, reified a formal
ledger into Python, and the comparison caught a bug self-review had
missed (the status order wasn't a complete lattice, so Knaster–Tarski
didn't license what the ledger claimed). A self-produced witness shares
whatever blind spot produced the account it's checking -- it can be
consistent and wrong in the same way twice.

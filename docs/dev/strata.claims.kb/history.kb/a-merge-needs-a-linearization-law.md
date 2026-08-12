---
label: MERGE
standing: open
why:
  - the-store-is-the-history.md
  - state-is-a-fold.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_history.py::test_a_branch_has_no_canonical_fold
---

# A Merge Needs a Linearization Law

WORD keeps the word; FOLD is defined on words. Branching stores --
clones, working copies, any two writers who diverge from a common
prefix -- hold two words, and nothing here says what their merge is.
Interleaving is a choice, and a load-bearing one: two linearizations
of the same pair of branches fold to different states as soon as both
branches write one key. "The state after the merge" is therefore not
determined by the branches.

What is open is which law supplies it. A total order every branch
respects makes the fold well-defined and buys a global authority. A
payload algebra whose updates commute makes the order irrelevant and
spends the payload's freedom -- last-writer-wins is not such an
algebra. A merge update naming its two parents, payload the
resolution, keeps the store a word at the price of asking someone.
Each is a different account of what a store is; none follows from the
two claims above.

Until one is filed, every claim downstream of FOLD holds of linear
histories only.

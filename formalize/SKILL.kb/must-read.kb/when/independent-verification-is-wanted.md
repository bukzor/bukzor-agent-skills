# Independent Verification Is Wanted

When a formalization needs a second opinion -- not a self-check, a
genuinely independent one -- run a second `/formalize` blind to the
first, then reconcile. This is the pre-2026-08-15 origin move, recovered:
comparing a formal account against an independently-produced witness is
what caught the Knaster–Tarski bug the self-checked version missed.

## Producing the second account

Spawn it with no view of the first: not its ledger, not its
conjectures, not the fact that a first run happened. A different
session or agent is strictly better than a second pass in the same
context -- the blind spots that produced a wrong-but-consistent first
account can produce a matching wrong witness if it's the same run
checking itself.

## Reconciling

1. **Diff the accounts.** Where do the two disagree about what the
   structures *are*? For each disagreement, rule: which is right, on
   what evidence. Where one has something the other missed, say what it
   would have needed to see to find it.
2. **Critique each on its own terms**, not only against the other:
   placement by ontology (a claim confined to words its theory doesn't
   admit), a `stale when` that's missing or unfalsifiable, a claim
   standing `bare` that's actually a judgment, mutual-support rings in
   the `why:` graph.
3. **Press hardest on simplicity.** Two independent accounts of the same
   design is a lot of apparatus by itself; the reconciled result has to
   earn being the *simpler* one, not just the union of both.
4. **Deliver**: proposed changes, one per line, each naming the claim
   and the observation that moves it -- then the single highest-value
   change. Propose diffs; do not silently apply them. The author of an
   argument should not also be its filing clerk -- whoever owns the
   ledger rules and edits it.

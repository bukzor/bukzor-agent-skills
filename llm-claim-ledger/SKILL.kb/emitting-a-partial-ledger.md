# Emitting a Partial Ledger

Union-last-wins makes every render a patch: restating a claim
supersedes it, and unmentioned claims stand. So you need not render
the whole ledger to update part of it -- list the claims that changed
and stop.

Two consequences:

- Silence endorses the last version. If a claim no longer holds, say
  so -- revise it or strike it; omitting it does not retract it.
- A partial render never means "the ledger is now only these." Where
  the full state matters -- at flush, or on `claim list` -- render it
  all.

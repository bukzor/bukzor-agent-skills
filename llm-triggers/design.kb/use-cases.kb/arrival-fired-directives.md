# Arrival-Fired Directives

`requires:`/`depends:` in a host `CLAUDE.md` is a trigger — the
fleet's most deployed one, predating this subsystem's name for it —
carrying a directive with its condition deleted. It fires on
*arrival* at a scope: the file loads for every agent entering the
repo, whatever they came to do. The need it serves is keyed to
intent, not location; a ledger's skill is wanted by an agent about to
write a claim, not by one reading one.

Today: two spellings, each a different error. `requires:` fires
always — a read-only lookup in a claims repo has paid two full skill
loads it never opened, and with the rest of the bootstrap roughly
half that session's tool calls fell before the first line of the
answer. `depends:` defers to the agent's judgment and so misses the
writer who needed it. The author's only choice is which error to
make.

Satisficed when: the condition travels with the directive, so the
body reaches an agent about to write to the scope and stays silent
for one only reading it, while the floor
(`../040-design.kb/floor.md`) still surfaces it during planning
wherever nothing mechanical is bound. The deployed fields also need
a stated disposition — migrate or retire — being the largest
existing instance of this subsystem's own concept.

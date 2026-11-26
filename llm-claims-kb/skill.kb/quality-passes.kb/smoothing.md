# Smoothing

A ledger whose claims each pass their own checks can still fail to follow as a
graph: a premise that says what only its dependent needs, a rule under the
wrong parent, two siblings with one conclusion. Smoothing walks the `why:`
graph, judges each claim in its place, and adjusts nodes and edges until a walk
changes nothing ([SMOOTHING]).

> [!DRAFT] agent-authored 2026-11-25, vetoable: what each direction catches,
> and the stopping rule.

## Before walking

Run the sweep ([SWEEP]); it carries the scans and how to run them, and their
findings are input to the walk. Draw the ledger ([GRAPH_HEALTH]) and read all
of it before changing any of it: each question below reads a node's context,
and the context is the whole graph.

## The walk

Top-down from the ledger's top file, then bottom-up from the leaves. At each
node, ask:

- **Its theory.** Does it say only words its theory may ([CONFINEMENT])? In a
  design tower, does it answer only its rung's question ([EACH_RUNG])?
- **Its `why:`.** Does it cite every premise it follows from, and does each
  premise it cites support it ([COROLLARIES])? In a design tower, does it reach
  the mission ([REACH])?
- **Its siblings.** Does a sibling already hold its conclusion, or contradict
  it ([ONE_HOME])?
- **The rulings it quotes.** Does its body keep every qualifier of the quote
  ([RULING_FIDELITY])?

Each direction catches what the other misses. Going down, a node is read
against premises already settled: a node its parent does not support, or one
carrying detail a lower node should hold. Going up, a node is read against
what rests on it: a premise its dependents lean on for something it does not
say, or a dependent restating its premise.

A finding's meaning and repair are the cited pass's. In graph terms, a repair
rewords, splits, merges, moves, cuts, or creates a node, or adds, drops, or
retargets a `why:` arrow. A cut also gets one-home's check for losses.

## When to stop

Walk again until a walk changes nothing. After the first full walk, only a
node whose context changed needs judging again: the node itself, a premise, a
dependent, a sibling, or its theory's `ontology:`. Nothing else feeds the
four questions. Each later walk therefore covers that frontier only, in both
directions, and the pass is done when the frontier is empty.

- **Oscillation.** A change that undoes an earlier walk's change is a tie
  between two passes. Stop changing that node and put the choice to the owner.
- **No cap.** A walk limit would stop on a ledger known to be rough and say
  nothing about it. If the sitting ends first, record the frontier for the next
  session to resume from.

Run the sweep again after the last walk.

[SMOOTHING]: ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/smoothing-is-a-quality-pass.md
[SWEEP]: ../procedures.kb/run-quality-passes.md
[GRAPH_HEALTH]: graph-health.md
[CONFINEMENT]: confinement.md
[EACH_RUNG]: ../../../llm-design-kb/skill.kb/quality-passes.kb/each-rung-says-only-what-its-question-asks.md
[COROLLARIES]: corollaries.md
[REACH]: ../../../llm-design-kb/docs/dev/claims.kb/design.kb/stratification.kb/every-claim-reaches-the-mission.md
[ONE_HOME]: ../../../llm-kb/skill.kb/quality-passes.kb/one-home.md
[RULING_FIDELITY]: ruling-fidelity.md

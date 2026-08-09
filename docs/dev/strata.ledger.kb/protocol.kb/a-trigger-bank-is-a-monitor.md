---
label: MONITOR
standing: agent
why:
  - ../history.kb/state-is-a-fold.md
---

# A Trigger Bank Is a Monitor

A trigger bank is a monitor automaton: guarded rules whose conditions
are predicates on the current situation (views of state, of the
conversation, of the task) and whose actions are directives. Its
semantics is the synchronized product with the agent's own process --
the agent runs, the monitor watches, matched guards interpose. The
bank is a formal object independent of who does the watching.

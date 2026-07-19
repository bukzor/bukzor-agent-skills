---
why:
  - ../040-design.kb/class-task.md
trigger: A working-set line is found contradicting its task-collection entry (status, target, or existence) during real work — first recurrence after this filing.
---

# Task Synthesis Drift Check

A task-class doctor check that a working set and its collection
agree: every pointer line resolves to an entry, every open entry has
a working-set line (an absent one is invisible work — the v1 failure
mode), and line status does not contradict entry state. The option
pair inverts the middle rule: `ideas.md` must carry *no* pointer
lines (`ls ideas.kb/` is the option index).

Deferred: the pointer convention is pure data today, and v1 ran for
months on hand-maintained consistency. Evidence the check will
eventually pay: the 2026-07-18 sweep found a coordinator checklist
still showing an already-completed child as unchecked — the same
drift shape, caught only by a manual audit.

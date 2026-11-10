---
label: INTERRUPTIBILITY
standing: user
authority:
  address: "97605ccb"
  words: "if I see things going wrong, or realize my requirements were ill defined or incomplete, I want to be able to interrupt and amend with minimal lost work"
---

# Interruptibility

Work can stop at any moment, by accident or by choice, and resume
with minimal lost work.

- **by accident**: a crash, an OOM, a killed session. A motivating
  case: a VM OOM partway through a plan, resumed easily from the
  handoff files.
- **by choice**: the user sees things going wrong, or realizes a
  requirement was ill-defined or incomplete, and stops to amend it.

> [!@bukzor] 97605ccb
>
> interruptability / resumability -- for example, we encountered a VM
> oom during this process and were able to resume easily due to our
> paper trail. But also, if I see things going wrong, or realize my
> requirements were ill defined or incomplete, I want to be able to
> interrupt and amend with minimal lost work

---
why:
  - ../010-mission.md
---

# Runtime Portability

The knowledge, procedures, and conventions this system embodies work
equally well whether the operator is driving Claude Code, OpenCode,
Claude.ai, aistudio.com, ChatGPT, or a raw Anthropic-API tool-use
loop — today or after the next platform migration. No artifact should
need re-authoring to survive a tool switch; at most a thin adapter
should need replacing.

This sits in tension with `native-first`, which prefers a runtime's
own primitives over bespoke ones. The tension resolves by *kind*, not
by choosing one goal over the other: native-first governs mechanism
choice **within** the adapter (delivery); runtime-portability governs
what's allowed to live **in the core and its classes** (spec, engine,
class conventions) above the adapter. See
`../030-requirements.kb/coupling-is-adapter-only.md` for the checkable
form of that boundary.

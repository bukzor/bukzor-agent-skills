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
own primitives over bespoke ones. The tension resolves by *layer*,
not by choosing one goal over the other: native-first governs
mechanism choice **within** layer 3 (delivery); runtime-portability
governs what's allowed to live **above** layer 3. See
`../030-requirements.kb/coupling-is-layer-3-only.md` for the checkable
form of that boundary.

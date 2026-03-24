---
name: llm-design-kb
description: "Agent MUST load for design.kb/ directories and layered design documentation"
---
--- # workaround: anthropics/claude-code#13005
setup: |
    All projects that depend on this skill should have as `CLAUDE.md` frontmatter:

    ```yaml
    --- # workaround: anthropics/claude-code#13003
    depends:
        - skills/llm-design-kb
    ```
---

# Design Knowledge Bases

Layered design documentation using `.kb/` collections. Each layer justifies
the one below and realizes the one above, linked via `why:` frontmatter.

## Layers

Each layer answers a question that motivates the layer below:

| Layer | Answers | Motivates |
|---|---|---|
| `010-mission.kb/` | What problem are we solving? Who benefits? | goals |
| `020-goals.kb/` | How do we accomplish the mission? | requirements |
| `030-requirements.kb/` | How do we validate goals are achieved? | design |
| `040-design.kb/` | How do we satisfy requirements? | components |
| `050-components.kb/` | How do we implement the design? | deliverables |
| `060-deliverables.kb/` | How do we build the components? | — |

All layers are optional. Create as needed.

Entries link upward via `why:` frontmatter — e.g. a requirement lists the
goals it serves:

```yaml
---
why:
  - site-agnostic-capture
---
```

## Maintenance

After any session that changes code or design understanding in a project with
`design.kb/`:

1. **Find affected docs.** Which design.kb files relate to what changed this
   session? Read each one.
2. **Check claims against ground truth.** Look for stale assertions — things
   that were true when written but no longer are.
3. **Capture new concepts.** Did discussion surface goals, requirements, or
   components that aren't documented? Create entries in the appropriate
   collection.
4. **Trace `why:` chains.** New docs need `why:` frontmatter pointing to their
   motivation. Existing docs that gain new responsibilities need updated `why:`
   references. Follow chains to verify they connect back to goals/mission.
5. **Fix, don't flag.** Rectify stale docs directly. Only ask the user when
   the correction requires a design decision.

## References

- `references/how-to-document-design-knowledge.md` — Full creation guidance,
  relationship to ADRs/devlogs/CLAUDE.md, background.kb and technical-policy.kb

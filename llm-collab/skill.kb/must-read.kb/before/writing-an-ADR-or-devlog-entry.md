# Before writing an ADR or devlog entry

Also: before deciding whether a decision warrants an ADR, and before
laying out a project's `docs/dev/` for the first time.

Paths below are relative to the skill root (`../../..` from this file).

## Core Principles

### 1. Separation of Concerns

**Problem:** Mixing audiences wastes everyone's time.

**Pattern:** Different files for different audiences/purposes:
```
project/
├── README.md                 # Users: what it does, how to use
├── HACKING.md                # Contributors: how to develop
├── CLAUDE.md                 # Agents: architecture, conventions
└── docs/dev/
    ├── adr/                  # Why: decision rationale
    ├── devlog/               # When: session history
    └── design/               # What/how: living design knowledge
```

### 2. Tiered Detail

**Problem:** Loading full docs when you need a summary wastes context tokens.

**Pattern:** Three-level information hierarchy:
1. Top-level file: 1-2 sentence summary + link
2. Main doc: 1-paragraph summary + link to deep dive
3. Subdirectory: Full detail

### 3. Temporal Ordering

**Problem:** With 20+ sessions/day exploring ideas in parallel, codebase contains conflicting partial implementations. Which decision is current?

**Pattern:** Date-based naming provides temporal ordering:
- ADRs: `YYYY-MM-DD-NNN-title.md`
- Devlog: `YYYY-MM-DD.md` (or `YYYY-MM-DD-HHMM.md`)
- When conflicts found, newest decision wins

### 4. Baton-Passing

**Problem:** Agent swarm loses alignment between sessions.

**Pattern:** Devlogs capture what diffs can't: reasoning, principles, conventions.
- Decisions and their rationale (especially rejected alternatives)
- Conventions established and principles discovered
- Tradeoffs that shaped the approach

**For task tracking:** `Skill(llm-subtask)`. For sessions running
concurrently rather than in sequence: `../when/peer-sessions-work-overlapping-ground.md`.

### 5. Living Documentation

**Problem:** Docs become stale and lie.

**Pattern:** Use directory listings as the source of truth:
- `docs/dev/adr/` directory contains decisions—`ls -t` to see chronologically
- `docs/dev/devlog/` directory contains session history—directory itself is the index
- Avoid maintaining separate index files that can drift

### 6. Design Knowledge

**Problem:** CLAUDE.md is too brief for deep understanding; ADRs are too granular.

**Pattern:** `docs/dev/design/` for living design documentation — deeper
than CLAUDE.md, more distilled than ADRs. `Skill(llm-design-kb)`.

## Quick Reference

**Common workflows:**
- When to document what: `references.kb/workflows.kb/when-to-document-what.md`
- Session orientation: `references.kb/workflows.kb/llm-document-consumption-patterns.md`

**Key file types:**
- ADRs: `references.kb/file-types.kb/ADRs.md`
- Devlogs: `references.kb/file-types.kb/devlog.md`
- CLAUDE.md: `references.kb/file-types.kb/CLAUDE.md`
- Browse all: `references.kb/file-types.kb/`

**Common tasks:**
```bash
# Orient yourself at session start
~/.claude/skills/llm-collab/bin/llm-collab-session-start

# Document a significant decision
~/.claude/skills/llm-collab/bin/llm-collab-adr --title "Decision title"

# Record what happened this session
~/.claude/skills/llm-collab/bin/llm-collab-devlog --title "Entry title"

# Backdate an entry (works with any date-based script)
DATE=2025-11-19 ~/.claude/skills/llm-collab/bin/llm-collab-adr --title "Decision title"

# Run from another directory without cd
~/.claude/skills/llm-collab/bin/llm-collab-adr -C /path/to/project --title "Decision title"

# Set up docs for new project
~/.claude/skills/llm-collab/bin/llm-collab-init
```

All scripts support `--help` for details.

## Detailed References

`references.kb/` holds categorized guides:
- **file-types.kb/** - What each doc type should contain
- **guidelines.kb/** - How to write effective docs
- **workflows.kb/** - How to use and maintain docs

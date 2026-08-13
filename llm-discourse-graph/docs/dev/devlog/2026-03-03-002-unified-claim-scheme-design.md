# Devlog: 2026-03-03 — Unified claim scheme design session

## Focus

Designed a unified knowledge representation scheme that merges the discourse
graph (five collection types) and design tower (numbered abstraction layers)
into a single structure based on one node type: claim.

## Key Design Decisions

### One node type

Collapsed questions, claims, deductions, sources, and definitions into
"claim" with varying attributes. Node type is emergent from attributes +
graph position, not stored. Grounded in erotetic logic (questions as
incomplete propositions) and the observation that deductions added ceremony
without value in the prior session.

### Three validity axes

Truth (0-1), certainty (0-1), utility (-1 to 1). Collectively called
"validity" per Habermas's Geltungsansprüche. Defaults are all 1, meaning
zero bits of denotation for fully-accepted claims. Negative utility
distinguishes "harmful" from "absent."

### Per-party validity with $all

Validity is either a single axes object or a map keyed by party name.
`$all` is the distinguished default key (borrowing `$`-prefix convention
from JSON Schema). Per-party entries override `$all` via JSON Merge Patch
(RFC 7396) semantics. Three-tier cascade: schema → $all → per-party.

### Parentage as why/how

Filesystem tree = primary inferential structure. Walk up = why, walk
down = how. `why[]` in frontmatter for supplementary upward links only.

## Process Notes

- Session began with a realignment — I used `2>/dev/null` on a find command
  despite `must-read.d/before/shell-commands.md` explicitly prohibiting it.
  Root cause analysis led to renaming the file to `ANY-shell-commands.md`
  and adding "Engagement Over Action" to the Response Protocol in CLAUDE.md.
- The user preferences analysis (three platform preference docs) was the
  intended first application of the unified scheme, but we discovered the
  scheme design was the prerequisite. The preference files are staged at
  `~/.claude/user-preferences.kb/` awaiting analysis.
- Academic prior art survey compiled: Toulmin, Searle, Pollock, AGM,
  Habermas, Walton, Bayesian epistemology, modal logic, Levine. Key
  finding: challenge modes are emergent from dimensional coordinates.

## Conventions Established

- `$all` for the default/consensus entry in a per-party validity map
- JSON Merge Patch (RFC 7396) as the cited standard for cascading semantics
- "Validity" (per Habermas) as the group name for epistemic/pragmatic axes
- Living spec document (not ADR) for evolving design decisions

## What's Next

- Write full JSON Schema for claims
- Apply to user preferences as first test case
- Migrate chatgpt-vim-config-planning.kb to unified format
- Update SKILL.md

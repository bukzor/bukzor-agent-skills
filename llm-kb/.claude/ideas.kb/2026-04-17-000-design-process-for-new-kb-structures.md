---
managed-by: Skill(llm-subtask)
---

# Design process for new .kb structures

The skill documents .kb anatomy and creation steps but not the design
thinking that precedes creation. In a real session (2026-04-17,
private.evan-family), it took four rounds of propose → reject → revise
to arrive at a coherent structure. Each round wasted user patience and
tokens.

The missing piece is a checklist or thought process for designing a new
.kb structure *before* creating files:

1. Inventory all information that needs persisting
2. For each item: how will someone look for it? (read path)
3. For each item: will someone reliably find and dedup when adding? (write path)
4. Group by natural taxonomy — what's the same *type* of thing?
5. Check for table/list smell in any planned .md (→ promote to .kb/)
6. Check for audience mismatch (→ maybe different repo/directory)
7. Verify summary files accompany their .kb/ directories

This process should live in the skill doc, probably in the "Creating a
Collection" section or as a new "Designing a Knowledge Base" section.

Observed anti-patterns during the session:
- Delegating .kb design "plan" to a Plan sub-agent (lacks conversational context)
- Proposing structure before inventorying information
- Creating files then moving them (mv willy-nilly → frankenstein)

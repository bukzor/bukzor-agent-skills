# chatlib-assess

Evaluate segments or messages for extractable value and implementation priority.

## When to use

After `chatlib-digest` has documented what's in each segment. Before `chatlib-extract` pulls artifacts. When the user asks "what's valuable here?" or "where do I start?"

## Input

- Summarized segments (directories with SUMMARY.md)
- Current project context (what exists already, what the project needs)

## Procedure

1. **Identify candidate artifacts** — Scan summaries and key messages for concrete, reusable outputs: specs, decision records, contracts, invariants, checklists, protocols.
2. **Assess each candidate** on:
   - **Durability** — Will this still be true in 3 months? Principles > implementation details.
   - **Endorsement level** — Was it user-requested? User-confirmed? Just proposed? The difference matters.
   - **Dependency position** — Does it enable other work? Is it on the critical path?
   - **Redundancy** — Is this already captured in project docs, code, or commit history?
3. **Priority-order** by what enables what, not by conversation order. Build the dependency chain.
4. **Flag drift** — If the project has evolved since the conversation, note what still holds vs. what has changed. Be specific ("tech stack" is vague; "assumes Rust, project uses Python" is useful). Ask the user when uncertain.

## Output

A **draft** ranking — present it as a proposal for user feedback, not a conclusion. Include tiers (must-extract / should-extract / background context only). For each item:
- What it is (1 line)
- Source message(s)
- Endorsement level
- Why it matters (dependency position)

Optionally: a dependency chain diagram.

Expect corrections. The user knows what enables what in their project better than the conversation reveals. Revise the ranking based on their feedback before proceeding to `chatlib-extract`.

## Pitfalls

- Don't infer project state from the repo alone. Ask.
- Don't conflate "assistant proposed it" with "user decided it." Check surrounding messages for endorsement.
- Order by dependency, not by apparent importance. What enables what?

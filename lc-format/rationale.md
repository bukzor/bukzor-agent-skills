# SKILL.md: Labeled Claim (LC) Format: rationale

- Adversarial-aware -- format assumes claims will be attacked. Several features exist to preserve fallback positions and support steelmanning.
- Disjunction (`|`) -- preserves multiple sufficient lines of reasoning rather than collapsing to a winner. Useful when opposition might attack one line, or when steelmanning might select a different one.
- Strongest-first ordering -- reader-courtesy hint, not structure. Soft so it doesn't need its own defense.
- Last-mention-wins -- matches how arguments evolve in real time. Avoids forcing upfront formalization.
- Axioms post-hoc -- foundations are visible in retrospect, not prospect. Tracking them prospectively wastes effort and over-commits.
- Retraction doesn't propagate -- entailment claims are informal; retracting a parent invites but doesn't force revision of children. Cascade is a suggested move, not automatic.
- Concede vs. retract -- concession means the claim survives but its support has shifted. Retraction means the claim is withdrawn. Distinct because real arguments need both.
- Flat list, no nesting -- nesting implies tree structure that arguments don't have. Claims often have multiple parents and circular dependencies during exploration.

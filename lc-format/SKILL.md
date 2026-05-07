---
name: lc-format
description: Use this skill when tracking claims through live argument — where claims get added, revised, branched, challenged, conceded, or retracted as the discussion evolves. Especially useful when a conversation accumulates enough contested or reversed claims that prose alone loses the thread. Not for finished proofs or formal entailment checking.
---

# Labeled Claim (LC) Format

A flat markdown list.

## Syntax

- `LABEL: claim` — define a claim.
- `LABEL <- PARENT1 PARENT2` — entailment; parents space-delimited.
- `LABEL <- A B | C | D E` — branched entailment; `|` separates sufficient parent sets.
- `LABEL <- A B | C: claim` — definition and entailment colocated. Optional; either may appear alone on its own line.
- `LABEL <- (A | B) C` — parentheses for explicit grouping.

Precedence: juxtaposition (space) binds tighter than `|`. Parentheses override. So `A B | C` means `(A B) | C`.

Convention: list sufficient sets strongest-first to make steelmanning cheaper. Not load-bearing; revise freely.

## Labels

- ALLCAPS-HYPHENATED, 2-12 chars.
- Mnemonic of content.
- Last mention wins; restating a label revises it.

## List rules

- Flat. No grouping, headers, or nesting.
- Unordered.
- Not code-fenced.
- One claim per line.

## Axioms

- Emerge post-hoc as claims with no parents.
- Don't track during reasoning.

## Stream-of-consciousness use

- Mention an LC line in prose to add or revise it.
- Definition and entailment may be split across separate mentions, in any order.
- Cumulative state = union of most-recent mention of each label.

## Suggested moves

- New claim: new line, new label.
- Revise: same label, new content.
- Branch: add `|` alternatives to entailment.
- Challenge: propose missing parent or dispute entailment.
- Concede: accept a challenge without retracting. Claim stands; entailment may be revised.
- Retract: restate as `(retracted)`.
- Cascade: when retracting, scan for children and retract or rejustify each.

## Not for

- Finished proofs.
- Replacing prose justification.
- Formal entailment checking — claims of entailment are informal and themselves disputable.

# chatlib-extract

Pull key messages into standalone documents with provenance framing.

## When to use

After `chatlib-assess` has identified what's worth extracting. When conversation artifacts need to become project artifacts.

## Input

- Specific messages identified by `chatlib-assess`
- The assessment's endorsement level and drift notes

## Procedure

1. **Create an `extracted/` directory** as a sibling to the conversation data.
2. **For each artifact**, create a numbered .md file:
   - **YAML provenance header** with:
     - `source:` — relative path to the original message file
     - `status:` — endorsement level (user-requested, user-confirmed, proposed, etc.)
     - `context:` — what prompted this message, what the user said before/after, what nuance is lost by reading it standalone
   - **Body** — the message content, lightly edited only for self-containment (e.g., removing "as I said above" references that no longer resolve)
3. **Write a README.md** for the extracted directory:
   - What these files are (conversation artifacts, not ratified specs)
   - What held up vs. what may have drifted
   - Table of contents with source, status, and one-line description per file
   - Rule of thumb for how to read them

## Framing principles

- **Provenance over prescription.** The header's job is to prevent a reader from treating a proposal as a decision. State what the user actually endorsed.
- **Context over content.** The surrounding conversation often contains the reasoning, caveats, and rejected alternatives. The `context:` field should point the reader back when it matters.
- **Minimal editing.** Don't rewrite the assistant's output. Add framing around it. The original wording is evidence of what was actually said.
- **Flag drift, don't resolve it.** If the project has moved on from an assumption in the message, note the discrepancy. Don't silently update the message to match current state — that destroys provenance.

## What this is NOT

- Not a rewrite or formalization step. That's a downstream activity the user does with the extracted artifacts.
- Not summarization. The full message content is preserved.

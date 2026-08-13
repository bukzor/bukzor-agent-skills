---
why:
  - wellness-as-upstream
  - grow-incrementally
trigger: After journal-kind vitals have ≥3 months of regular entries (enough corpus for trend extraction).
---

# LLM-Assisted Metric Extraction

Use an LLM to summarize a window of journal entries and surface
candidate tier-2 metrics: "you mentioned poor sleep 4 of 7 days,"
"social mentions trended down 30% this month," "creative-time
references averaged 2.1h/week."

Output is **candidate metrics**, not authoritative ones — the
operator confirms before they're treated as data. This preserves the
"human in the loop on judgment" principle: extracted patterns are
prompts for review, not facts.

Deferred because: needs sufficient corpus for the LLM to identify
real trends rather than confabulate. ~3 months of regular journaling
is a reasonable threshold.

Also: this is the only place where LLM use is allowed inside the
data pipeline. Postmortem scoring and judgment calls remain human.

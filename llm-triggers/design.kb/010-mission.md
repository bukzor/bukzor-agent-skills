# Mission

Deliver the right directive at the right moment: carry conditional
directives ("before X, read and apply Y") from author to agent across
any agent runtime, enforcing each as strongly as that runtime allows
while never requiring more than a filename scan.

Beneficiaries: the operator, whose rules fire without being
remembered; agents, who receive directives when actionable instead of
as standing context tax; and the kb suite's other classes (task,
record, design), whose conventions need conditional enforcement.

The subsystem is part of the kb suite — it depends on `Skill(llm-kb)`
and cites the spec one-way — and is the successor to v1's
`llm-must-read-kb`, per the ecosystem verdict in
`../../design-next.kb/040-design.kb/delivery-boundary.md`.

---
label: PATH_ONLY_MESSAGES
standing: agent
why:
  - ../requirements.kb/disk-record.md
---

# Messages carry a path and nothing else

Every launch, amendment and reply between coordinator and agent names
a handoff file and nothing more: "do the task in", "reread", "resume
the task in", and the agent's bare path when it is done. Whatever an
instruction says lives in the file before the message is sent, so the
file is always what the agent worked from.

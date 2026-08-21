---
label: AS_EXTENSION
standing: user
why:
  - ../an-extension-declares-the-chat-skill.md
---

# Reform It as an Extension of /llm-claims

`llm-discourse-graph` changes basis from `/llm-kb` to `/llm-claims`, per BASIS:
read `/llm-claims`, add
a few words to the default ontology (question, source, definition),
add nothing else. Its decomposition workflow and wiring pattern
survive as rules; its five collections do not survive as types.

Appeal: the five collections already reduce -- deductions are bare
claims with `<-`, questions are loci with `standing: open`, sources
are judges (`authority:`/`verify:`), definitions are theory ontology.
Cost: eight live sites, and the successor has to be written.

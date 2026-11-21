---
cwd: $(pwd)
session:
  uuid: # chronological; append your uuid when picking this entry up
    - $CLAUDE_CODE_SESSION_ID
  started: $(date -Is)
  ended: null # set only when no more sessions are expected (~= about to delete this file) -- not "my conversation ended"
---
# <Title — topic slug, title-cased>

<One paragraph: what work this session does. Concise.>

<If a taskfile/plan exists, reference its absolute path here.>

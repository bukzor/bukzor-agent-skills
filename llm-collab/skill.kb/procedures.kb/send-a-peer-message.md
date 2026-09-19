# Procedure: send a peer message

You are about to `SendMessage` to another session -- not a sub-agent
you spawned, and not the user.

## The admissibility test

A message is admissible only where a file could not have carried it.
Three kinds pass:

- **pointer** -- "wrote X at PATH; bears on your Y." The content is on
  disk; the message is one line.
- **conflict** -- "my A contradicts your B; both filed at PATH; needs
  the user." Never argue the conflict in the message.
- **hand-off** -- "done with Z; it is yours now."

Everything else -- findings, proposals, questions, acknowledgements,
thanks -- goes in your `sessions.kb/` entry, where the peer pulls it at
their next checkpoint and the user sees it first.

## Cost

An inbound message writes to the receiver's context with no decision
of theirs, at a moment they did not choose. It cannot be rewound, and
its priors leak into their later answers. Budget accordingly: at most
one message per peer per checkpoint, first line self-contained, no
prose the peer must reason about.

## Delivery is not uptake

A successful send means the message reached the session, not that it
acted. A session in another permission mode may hold it for approval,
or refuse it. Never read silence as agreement; the file you pointed at
is the record either way.

## Claude Code

`ListAgents` names the reachable peers. Sub-agents you spawned are not
peers for this entry's purposes: they report to you, and you may
message them freely. Use `notify_when_idle` (no message body) for a
one-shot "tell me when you are idle" rather than a message asking
them to report back.

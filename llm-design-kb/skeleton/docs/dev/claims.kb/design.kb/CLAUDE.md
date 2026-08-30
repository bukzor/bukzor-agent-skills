# design.kb -- where a new file goes

One claim per file, under the rung whose question it answers. The
rung's own `.md` defines it; the claims it holds live in its `.kb/`.

- A claim answering a rung's question -> that rung's `.kb/`.
- A claim that would be revisited if some other claim collapsed ->
  name that claim in `why:`, whatever rung it sits on.
- A word this project stipulates -> the `ontology:` of the outermost
  rung whose claims all need it.
- Content the design assumes but does not argue -- domain background,
  prior art, worked use cases -> an auxiliary theory beside the rungs
  (`background.md` + `background.kb/`), not a rung.
- A cross-cutting imperative -> `../technical-policy.kb/`.

---
label: ROUNDTRIP
standing: agent
why:
  - a-target-is-a-realization-with-a-price.md
  - ../view.kb/a-cache-is-lawful-iff-the-triangle-commutes.md
---

# A Transport Is Faithful iff Decode Undoes Encode

Encoding into a target is a view of the carrier, so it inherits the
cache law -- and adds one: a representation is faithful iff decoding
it returns the carrier exactly, decode after encode the identity. A
target too poor for that may still transport, but the loss must be
announced at transport time, in the output the reader will actually
see: `llm-claims-kb-flatten` printing its three losses to stderr is
the worked instance. An unannounced loss is the one sin in
representation clothing -- the reader takes the projection for the
carrier and no stamp warns them otherwise.

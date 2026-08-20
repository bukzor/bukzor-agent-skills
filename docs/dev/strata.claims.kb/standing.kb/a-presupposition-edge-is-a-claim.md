---
label: EDGE
standing: agent
why:
  - an-act-is-a-bare-claim-of-the-record.md
  - standing-is-standing-according-to.md
  - presupposition-is-a-well-founded-edge-relation.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "edge_claim or different_frames"
---

# A Presupposition Edge Is a Claim

Every presupposition edge is itself a claim of the base. The edges a
reader is holding are read out of the record under that reader's
stance, exactly as anything else's standing is -- nothing is handed
in beside the record [ACT, STANCE].

Three things follow, and each is the point of the ruling rather than
a side effect:

- two readers who disagree about whether `p` presupposes `q` compute
  different senses for `p`. The disagreement is a thing the base can
  hold, instead of a precondition for holding anything.
- an edge nobody upholds is inert, well-foundedness included. The
  cycle test is asked of the graph in hand, never the graph on offer
  [DESCEND] -- so a cycle someone has already defeated is not an
  error anyone is obliged to fix.
- sense is computed from the two seeds content is: a claim collapses
  *surely* when an edge it surely has leads to a claim surely out,
  and *possibly* when an edge that may hold leads to a claim that may
  be out [SENSE]. A disputed edge is exactly as good as a disputed
  presupposition, and lands in the same coordinate.

The two levels do not recurse: an edge-claim is neither end of any
edge, and a graph saying otherwise is refused at the entry. That is
a simplifying stipulation rather than a finding, and its two halves
are not worth the same. Barring edges *out of* an edge-claim is what
keeps the collapse monotone -- let an edge-claim be mooted and the
edge it asserts falls inert, retracting a collapse already made,
which is not a move a least fixpoint has. Barring edges *into* one
buys only symmetry. Either half is stale the day a reader needs the
edge it forbids: lifting the first costs an approximation fixpoint
over the frame graph, lifting the second costs one assertion.

The declined alternative is the relation as a parameter, handed to
the engine beside the record. It was what the engine did, and it
makes the frame graph the one thing in the base no one may dispute:
a fact standing outside the record, in a theory whose whole
discipline is that the record is where facts enter.

# Theories

Once a ledger outgrows one readable list, group it — by vocabulary, not
by topic. A **theory** is a named set of claims over a fixed **ontology**
(the words its claims may use), plus zero or more **prior** theories
whose ontologies it also admits. Priors are declared rather than
computed, so theories form a poset, not a stack.

A theory opens with its **defining claim**: the label names the theory,
the text states the ontology and the defeater, and its `<-` names the
priors. Extension and demotion are then ordinary governance on that one
claim -- widening the ontology is a revision to it, and the theory's
standing is its defining claim's standing. On disk a theory is a
collection and its defining claim is the collection's header
(`Skill(llm-claim-ledger-kb)`).

Example: `stance` (acts, authors) → `ledger` (claims, verdicts, hashes)
→ `host` (engines, kernels) → `world` (Lean4, mathlib, version numbers).

Two rules earn the structure:

- **Confinement.** A claim may use only its own theory's ontology plus
  its priors'. This is what fixes placement — a claim's theory is set by
  the words its text needs, not by the turn that produced it — and it is
  greppable, which is why it is the rule that actually gets enforced:
  search a theory's claims for vocabulary it does not admit, and every hit
  is either a misplaced claim or an understated ontology.
- **Conservativity.** A later theory may not defeat an earlier one. It
  adds claims; it never changes the standing of a claim in a prior. Where
  it appears to, the prior was wrong and gets fixed there.

Split for the reader, not only for contention. When one theory's
claims keep leaning on a cluster of vocabulary that is not really
theirs -- background mathematics, shared machinery, a recurring
sub-argument -- pull the cluster into its own prior: an **auxiliary
theory**, legitimate even when nobody contests it in isolation (its
claims may all stand bare). The test is whether the citing theory
reads simpler afterward: shorter ontology, shorter arrows, claims
that argue in one vocabulary instead of two. The same move works at
sub-theory grain. This starts from the reader's cost rather than from
a dispute, but it is ordinary prior-declaration either way.

Name a theory for the ontology it admits — then the name says what its
claims are about, what vocabulary they may use, and when to come re-check
them, all at once. Put the proper nouns in a theory of their own, last:
it is the one you throw away.

Where a later theory needs a word an earlier one already uses, it reuses
the word for the closest thing its own ontology admits. That shift in
meaning is the interpretation, not a collision — do not rename to avoid
it, and disambiguate only where someone actually stumbles ("X in the Y
sense"). Renaming to dodge a reuse costs every later theory a word and
buys nothing.

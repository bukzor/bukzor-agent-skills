---
label: NAMESPACE
standing: user
authority:
  address: ba648ef5
  words: "there's a pending change to the llm-kb standard to make \"plain old directories\" transparent, treated as a (\"S3 style\") name prefix ... Agreed, heartily."
  about: plain directories inside a collection, and that prefix semantics are the collection class's to define
---

# A Plain Directory Is a Key Prefix

Inside a collection, a directory without the `.kb` suffix is a key
prefix and nothing more: the name of a file it holds is the whole path
below the collection, and the directory contributes no predicate, no
governance, and no boundary of its own. The `.kb` suffix marks a
governed collection -- own schema, own `CLAUDE.md`; a plain directory
marks a prefix.

The S3 analogy is exact and is the smallest example: listing with a
delimiter shows common prefixes (`ls -F` prints `dir/`), listing
without shows keys (`ls -RF` prints every path). One tree, two views,
and which view a reader takes is the reader's choice, not the tree's.

What a prefix *means* is the collection class's to say -- in a trigger
bank the path is the trigger phrase; in a claims ledger a plain
directory prefixes the names of what it holds. This claim fixes only
that a plain directory says nothing on its own.

Stale when: any tool or reader assigns a plain directory a meaning
beyond its name -- a validator that stops at one, a schema lookup that
does not walk through it.

> [!@bukzor] ba648ef5
> there's a pending change to the llm-kb standard to make "plain old
> directories" transparent, treated as a ("S3 style") name prefix ...
> Agreed, heartily.

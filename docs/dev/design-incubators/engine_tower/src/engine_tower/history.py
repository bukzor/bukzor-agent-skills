"""history -- the store is a word of updates; state is its fold.

The update alphabet U; a history is a word in the free monoid U*.
State is a map K -> Payload under override (last writer wins);
`state` is the unique monoid action extending it.  Nothing here knows
content.  [WORD, FOLD]
"""

from collections.abc import Mapping

type Payload = Mapping[str, str]
type Update = tuple[str, Payload]  # (key, payload)
type History = tuple[Update, ...]
type State = Mapping[str, Payload]


def state(history: History) -> State:
    """The action map U* -> S: fold override over the word.

    "Prior states queryable" is free: store the word, fold any prefix.
    """
    return {key: payload for key, payload in history}

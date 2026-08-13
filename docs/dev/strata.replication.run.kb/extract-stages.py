"""Rebuild a replication run's per-stage record from the subject's transcript.

A run's stages are the turns the operator sent; a stage's deliverable is
the subject's last message before the next turn arrived. Reconstructing
them from the transcript -- rather than from notes -- is what lets the
record be committed one stage at a time, which is what makes the run
rewindable: the checkout at stage N is the environment and the record
the subject had when it answered N.

The i-th turn sent corresponds to the i-th file in the turns directory,
so stage files carry their turn file's name. `--limit` stops early,
which is how a spoiled stage is left out of the record.

Run it against the tools that decode the transcript format:

    uv run --project ~/repo/github.com/bukzor/bukzor-tools python \
        docs/dev/strata.replication.run.kb/extract-stages.py \
        ~/.claude/projects/<slug>/<session>/subagents/agent-<id>.jsonl \
        --turns docs/dev/strata.replication.kb --out docs/dev/strata.replication.run.kb
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from claude_code_archeology import session as session_mod
from claude_code_archeology.session import Node, Session

COORDINATOR_PREFIX = "The coordinator sent a message while you were working:\n"
"""How a resumed subagent hears its operator: SendMessage wraps the paste."""

PEER_PREFIX = "Another Claude session sent a message:"
"""How a peer session hears it instead. Both wrappers, because a run that
outlives one turn usually changes which one the subject is."""


@dataclass(frozen=True)
class Stage:
    turn: Path
    sent: Node
    reply: Node


def message_text(node: Node) -> str:
    """The record's own prose, tool calls and tool results excluded."""
    message = node.record.get("message")
    if not isinstance(message, dict):
        return ""
    content = message.get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(
        block["text"]
        for block in content
        if isinstance(block, dict) and block.get("type") == "text"
    )


def is_operator_turn(node: Node) -> bool:
    """Did the operator send this, or is it harness noise?

    Skill preambles, continuation summaries and slash-command echoes are
    user-role too, so the delivery notice -- not the role -- identifies a
    turn.
    """
    text = message_text(node)
    return node.type == "user" and text.startswith((COORDINATOR_PREFIX, PEER_PREFIX))


def turns_sent(sess: Session) -> list[Node]:
    """The operator's turns, in send order: the spawn prompt, then resumes."""
    sent = [node for node in sess.nodes if is_operator_turn(node)]
    spawn = next(node for node in sess.nodes if node.type == "user")
    return [spawn, *sent]


def sent_message(node: Node) -> str:
    """What this record mailed back to the operator, if anything."""
    message = node.record.get("message")
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, list):
        return ""
    for block in reversed(content):
        if isinstance(block, dict) and block.get("name") == "SendMessage":
            args = block.get("input")
            if isinstance(args, dict):
                return str(args.get("message", ""))
    return ""


def reply_to(sess: Session, sent: Node, next_sent: Node | None) -> Node:
    """The stage's deliverable: the subject's last word *to the operator*.

    A subagent's last word is its final message, which the harness returns
    to the caller. A peer session's is the message it mails back -- what it
    says afterward is addressed to its own operator, not to this run. So a
    mailed reply wins over a spoken one whenever the turn has both.
    """
    stop = next_sent.line if next_sent else len(sess.nodes)
    span = [n for n in sess.nodes if sent.line < n.line < stop and n.type == "assistant"]
    mailed = [n for n in span if sent_message(n).strip()]
    if mailed:
        return mailed[-1]
    spoken = [n for n in span if message_text(n).strip()]
    assert spoken, (sess.path, sent.line, stop)
    return spoken[-1]


def deliverable(reply: Node) -> str:
    """The stage's text, however it was delivered."""
    return (sent_message(reply) or message_text(reply)).strip()


def stages(sess: Session, turns: list[Path], limit: int | None) -> list[Stage]:
    sent = turns_sent(sess)
    assert len(sent) <= len(turns), (len(sent), len(turns))
    paired = list(zip(turns, sent, strict=False))[: limit or len(sent)]
    return [
        Stage(turn, node, reply_to(sess, node, sent[i + 1] if i + 1 < len(sent) else None))
        for i, (turn, node) in enumerate(paired)
    ]


def title_of(turn: Path) -> str:
    """The turn's own H1, minus the marker."""
    for line in turn.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise AssertionError(turn)


def configuration(reply: Node) -> tuple[str, str]:
    """What the subject was running as, per its own record: model, effort.

    A run that changes configuration mid-way is comparing two subjects,
    so the stage that changed it has to be able to say so on its own.
    """
    message = reply.record.get("message")
    model = message.get("model") if isinstance(message, dict) else None
    return str(model), str(reply.record.get("effort"))


def stage_document(stage: Stage, transcript: Path) -> str:
    """One stage: what was asked, what came back, and where to check."""
    model, effort = configuration(stage.reply)
    return "".join(
        [
            "---\n",
            f"turn: {stage.turn.name}\n",
            f"sent: {stage.sent.timestamp}\n",
            f"replied: {stage.reply.timestamp}\n",
            f"model: {model}\n",
            f"effort: {effort}\n",
            f"transcript: {transcript.name}:{stage.reply.line}\n",
            f"uuid: {stage.reply.uuid}\n",
            "---\n\n",
            f"# {title_of(stage.turn)} -- what came back\n\n",
            "The subject's reply, verbatim. The turn that asked for it is\n",
            f"`../strata.replication.kb/{stage.turn.name}`; the operator's\n",
            "verdict on it is this file's commit message.\n\n",
            "---\n\n",
            deliverable(stage.reply),
            "\n",
        ]
    )


def write_stages(stages: list[Stage], transcript: Path, out: Path) -> list[Path]:
    written = []
    for stage in stages:
        path = out / stage.turn.name
        path.write_text(stage_document(stage, transcript))
        written.append(path)
    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcript", type=Path, help="the subject's session JSONL")
    parser.add_argument("--turns", type=Path, required=True, help="the turn files")
    parser.add_argument("--out", type=Path, required=True, help="where stages land")
    parser.add_argument(
        "--limit", type=int, default=None, help="record only the first N stages"
    )
    parser.add_argument(
        "--turn",
        default=None,
        help="take the file's last operator turn as this named turn's stage",
    )
    return parser.parse_args()


def last_stage(sess: Session, turn: Path) -> Stage:
    """The one stage a continuation file holds: its final operator turn.

    A session cut and resumed mid-run no longer starts at turn one, so
    position cannot say which turn a message is; the operator names it.
    """
    sent = [node for node in sess.nodes if is_operator_turn(node)]
    assert sent, sess.path
    return Stage(turn, sent[-1], reply_to(sess, sent[-1], None))


def main() -> int:
    args = parse_args()
    sess = session_mod.load(args.transcript)
    if args.turn:
        found = [last_stage(sess, args.turns / args.turn)]
    else:
        turns = sorted(p for p in args.turns.glob("[0-9]*.md"))
        found = stages(sess, turns, args.limit)
    for path in write_stages(found, args.transcript, args.out):
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())

---
why:
  - ../020-goals.kb/runtime-portability.md
trigger: Engine core (new/validate/promote/doctor) has landed and a second runtime (OpenCode, a raw API loop, Claude.ai via connectors, etc.) is in active personal use.
---

# MCP Server Adapter

Wrap the kb engine's verbs (`new`, `validate`, `promote`, `doctor`,
`query`) as an MCP server. Two distinct tiers, not one:

- **Local (stdio) tier** — trivial: a thin wrapper the Claude Code
  plugin bundles via `.mcp.json`. Low value on its own (Claude Code
  already reaches the same engine via Bash+CLI on the same
  filesystem); the payoff is a typed tool surface and finer
  permission scoping, not new reach.
- **Remote (Streamable HTTP) tier** — the tier that actually extends
  reach to claude.ai, ChatGPT, and any other web-based client with no
  local filesystem access. This is a hosted service, not a wrapper:
  it must be network-reachable, authenticated (OAuth), and own
  persistence itself — either as source of truth, as a proxy to the
  git repo via its API, or by tunneling a local instance out. Building
  this is materially bigger than "expose the CLI over MCP."

This is still the most standards-aligned lock-in-reduction
available — MCP has genuine multi-vendor adoption today, unlike the
`skill://` URI scheme
(`../040-design.kb/cross-reference-notation.md`), which remains an
unmerged draft — but the remote tier's cost (hosting, auth,
persistence ownership) belongs in the trigger estimate, not glossed
over as "zero bespoke integration." Deferred to avoid building either
tier before the CLI has proven itself in daily use.

One remote-tier server (Streamable HTTP, OAuth 2.1 + PKCE, arbitrary
read/write tools) plugs into both claude.ai ("custom connectors,"
beta, no platform-enforced tool-type restriction) and chatgpt.com
("Apps"/Developer Mode) with no server-side fork — same transport,
same auth flow. The only asymmetry is client-side policy, not
protocol: ChatGPT gates write tools behind Developer Mode (unavailable
on its Free plan, flagged risky) and requires per-call confirmation on
any tool not annotated `readOnlyHint`. Design consequence: annotate
`kb_query`/`kb_doctor` `readOnlyHint: true` and leave mutating tools
(`kb_new`, `kb_promote`) unannotated — correct read/write treatment on
both clients for free.

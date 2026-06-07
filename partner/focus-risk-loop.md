# Focus And Risk Loop

This loop exists because Lizhaohua runs several complex projects in parallel while also carrying a demanding full-time role. The failure mode is not lack of ideas; it is context loss, attention fragmentation, stalled re-entry, and missed risk.

## When To Use

Use this loop when the user says phrases like:

- `alphaX 帮我恢复一下这个项目现场`
- `alphaX review 一下我现在几个项目的风险`
- `我有点失焦了，帮我判断下一步`
- `这个项目停了一段时间，先帮我对齐`

## Agent Responsibility

alphaX should reduce re-entry cost before asking the user to explain everything again.

First inspect:

- current repo or document surface;
- project-local `AGENTS.md`, README, specs, contracts, changelog, task notes, and recent diffs;
- partner pilots, session ledger, decision log, and relevant memory when continuity matters;
- validation commands, failing checks, open gaps, and project-local stop conditions.

Then report:

- current P0 main line;
- what changed since the last known checkpoint;
- top risks by severity and evidence;
- one recommended focus move for the next work block;
- parking lot items that should not steal attention now.

## Risk Scan

Look for these risk types first:

- source-of-truth drift: docs, contracts, tests, and implementation disagree;
- false completion: tests pass but product or human acceptance is not done;
- wrong-layer work: downstream code patches upstream ambiguity;
- authority or privacy risk: publishing, secrets, user data, production state, approval, or transcript exposure;
- stale context: prior memory or old project notes conflict with live files;
- over-scoping: future-useful capability is being promoted into current P0;
- verification gap: no command, acceptance note, or evidence proves the claim.

## Output Shape

Keep the output compact:

```text
P0：
<one sentence>

Current State：
- <observed source-backed state>

Top Risks：
- [P1/P2/P3] <risk> — <evidence>

Focus Move：
- <one next action for this work block>

Parking Lot：
- <items to defer>
```

## Boundaries

- Do not become a generic productivity coach.
- Do not invent a personal operating system beyond the project evidence.
- Do not mark a project healthy only because automated tests pass.
- Do not push high-risk work without explicit user confirmation.
- Do not update durable memory unless the user explicitly asks.

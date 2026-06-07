# Pilot Candidates

This queue chooses real project surfaces for testing whether alphaX improves project R&D and thinking exploration.

## Selection Rule

Prefer a candidate with:

- existing local project path;
- project-local `AGENTS.md`, README, specs, contracts, or changelog;
- a concrete current decision, artifact, or verification path;
- enough source of truth for alphaX to reconstruct context before asking the user to restate it.

Do not add a project-local pointer until the pilot proves repeated use.

## Recommended First Pilot: agent-interaction-bridge

Path:

- `/Users/lizhaohua/work/llm/agent-interaction-bridge`

Why this is the first candidate:

- It directly tests the user's L0-L2 and L3-L4 boundary preference.
- Memory routes this repo to architecture governance, YAML contracts, freeze signals, Product Runtime, and Build-Time Governance.
- Current snapshot shows project-local `AGENTS.md`, `README.md`, architecture docs, contracts, tests, and an active branch.
- Current snapshot shows no root Alpha Partner pointer, so cold-start quality is testable.

AlphaX pilot prompt:

```text
alphaX 介入一下 /Users/lizhaohua/work/llm/agent-interaction-bridge。
先只做 cold start，不改文件：读取 partner contract 和项目 source of truth，给出 P0 主链路、primary loop、source of truth、当前风险、下一步验证路径。
```

Success evidence:

- alphaX identifies the current source-of-truth files without the user restating them.
- alphaX preserves L0-L2 ownership and avoids patching business meaning downstream.
- The session produces either a Spec Checkpoint, a project-loop packet, or a concrete verification plan grounded in project files.

Status:

- Read-only cold start completed on 2026-06-07.
- Focused `presentation.rendering` Spec Checkpoint completed on 2026-06-07.
- Project-local pointer adopted in `AGENTS.md` on 2026-06-07 after repeated real-project use.
- Next gate: user-approved `presentation.rendering` responsibility migration, or another direct `alphaX 介入一下` test from the project root.

## Second Pilot: online_community Session Runtime

Path:

- `/Users/lizhaohua/work/llm/clouds-beyond/online_community`

Why this is useful:

- It tests evidence traceability, acceptance reporting, guardrails, and privacy constraints.
- Memory routes this project to session runtime manual acceptance, evidence index, guardrail cases, and transcript privacy.
- Current snapshot shows `specs/session-runtime-v1/spec.md`, backend contracts, acceptance code, tests, and nested `AGENTS.md` files.
- Current snapshot shows no root Alpha Partner pointer.

AlphaX pilot prompt:

```text
alphaX 介入一下 /Users/lizhaohua/work/llm/clouds-beyond/online_community。
先自主对齐 session runtime 的 source of truth 和验收链路，不改文件，指出当前最值得验证的 P0 风险。
```

Success evidence:

- alphaX reconstructs the session runtime source chain from specs to backend acceptance tests.
- alphaX reports any privacy or guardrail boundary before proposing implementation.
- The session improves an acceptance path, evidence index, or review packet.

Status:

- Read-only cold start completed on 2026-06-07.
- Evidence packet: `partner/pilots/2026-06-07-online-community-session-runtime-cold-start.md`.
- Next gate: real-discussion manual acceptance planning, without committing transcript content.

## Third Pilot: clouds-beyond Root Changelog Governance

Path:

- `/Users/lizhaohua/work/llm/clouds-beyond`

Why this is useful:

- It tests whether alphaX can distinguish current-state source indexing from low-value history.
- Memory routes this repo to changelog compression thresholds and current-state governance.

AlphaX pilot prompt:

```text
alphaX 介入一下 /Users/lizhaohua/work/llm/clouds-beyond。
先只做 changelog governance cold start：读取 root source of truth，判断当前 changelog 是否需要压缩或保持不动，并给出验证依据。
```

Success evidence:

- alphaX applies the explicit threshold before proposing edits.
- alphaX verifies current file size, section count, and project rules from live files.
- The output prevents both over-cleanup and unchecked historical drift.

## Parking Lot

Use these only when a concrete source of truth is present:

- requirements-to-code generation-chain coverage;
- Agent 化组织 object model;
- Agent 知识治理 write-confirm-retrieve-degrade loop;
- external calibration on human-agent peer research.

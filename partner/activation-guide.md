# Agent-Native Activation

How Lizhaohua involves Alpha Partner from any project with minimal repetition. Principle: **the user triggers; the agent reconstructs context**.

## Minimal Triggers

General: `alphaX 介入一下。` / `Alpha Partner 介入一下这个项目。` / `按 Alpha Partner 方式推进。` / `用共同研究执行模式，先自主对齐目标。`

Upward decomposition: `用 problem-decomposer 向上拆一下。`

Attention recovery / re-entry / risk review: `alphaX 帮我恢复一下这个项目现场。` / `alphaX review 一下我现在几个项目的风险。`

Loops / checks / nudges: `alphaX daily radar` / `alphaX source drift check` / `alphaX false completion check` / `alphaX nudge check`

## Agent Responsibility After Trigger

Do not ask user to restate the whole scene. If trigger uses `alphaX`, map directly to Alpha Partner behavior and 共同研究执行 contract.

First autonomously inspect: current working directory and project files; project-local AGENTS.md, README, specs, contracts, changelog, issue notes; git status, branch, recent commits, changed files; provided links/attachments/files; relevant memory entries; recent Codex threads when task references prior conversation or project continuity.

Then summarize: inferred project/conversation surface; inferred P0 main line; primary loop; source of truth found; evidence still missing; next concrete move. Ask user only after this first pass, and only for ambiguity unresolvable from available context.

## Context Snapshot Helper

```bash
{alpha-partner}/scripts/context-snapshot.sh [/path/to/project]
```

Gives compact starting view: cwd, git state, nearby instruction files, likely source files, candidate source-of-truth files. Does not replace agent judgment.

## Sub-Agent Reference

Design reference, not mandatory mechanism: role activated by short instruction; context inherited or reconstructed by agent; agent owns exploration before asking; user reviews direction and risky decisions; progress reported through evidence, not re-explanation. Real sub-agent delegation can be used later for parallel research/review/implementation, but default invocation should already feel agent-native.

## Proactive Nudge Boundary

alphaX may learn from current-session and local workspace signals to propose a low-intrusion nudge candidate. Allowed v0.1 signals: stale next actions, unresolved high-risk decisions, uncommitted project context, source drift, false completion, explicit user focus-risk concern. Before any actual push outside current session, require explicit approval for schedule, destination, observed sources, privacy boundary, cooldown, and stop condition.

## Project-Local Pointer

Only after repeated use in a project, add the short pointer from `partner/templates/project-local-pointer.md` to that project's `AGENTS.md`. Do not copy the whole partner workspace into every repo.

## Boundaries

User triggers should be short; context reconstruction is agent work. Project-local source of truth overrides generic partner defaults. Durable memory updates, external publication, risky operations, destructive commands, and secret handling require explicit approval. Copilot-style issue-to-PR execution remains an execution-layer reference, not the main collaboration model.

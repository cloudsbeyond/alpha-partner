# Agent-Native Activation

This guide defines how Lizhaohua can involve Codex Partner from any project or conversation with minimal repetition.

The principle: **the user triggers; the agent reconstructs context**.

## Minimal Triggers

Use one short phrase:

```text
alphaX 介入一下。
```

or:

```text
Codex Partner 介入一下这个项目。
```

or:

```text
按 Codex Partner 方式推进。
```

or:

```text
用共同研究执行模式，先自主对齐目标。
```

If the task is specifically about upward problem decomposition:

```text
用 problem-decomposer 向上拆一下。
```

If the task is about attention recovery, re-entry, or risk review:

```text
alphaX 帮我恢复一下这个项目现场。
```

or:

```text
alphaX review 一下我现在几个项目的风险。
```

If the task is about repeated checks, Boris-style loops, or proactive nudges:

```text
alphaX daily radar
```

or:

```text
alphaX source drift check
```

or:

```text
alphaX false completion check
```

or:

```text
alphaX nudge check
```

## Agent Responsibility After Trigger

After activation, Codex Partner should not ask the user to restate the whole scene before doing any work.

If the trigger uses `alphaX`, map it directly to Codex Partner behavior and the same 共同研究执行 contract.

First autonomously inspect:

1. current working directory and project files;
2. project-local `AGENTS.md`, `README`, specs, contracts, changelog, or issue notes;
3. git status, branch, recent commits, and changed files when the target is a repo;
4. provided links, attachments, or files;
5. relevant memory entries when prior context matters;
6. recent Codex threads when the task references prior conversation or current project continuity.

Then summarize:

- inferred project or conversation surface;
- inferred P0 main line;
- primary loop: research, project, thinking, memory, focus/risk, or manual loop layer;
- source of truth found;
- evidence still missing;
- next concrete move.

Ask the user only after this first pass, and only for ambiguity that cannot be resolved from available context.

## Context Snapshot Helper

When operating in a local project, run this read-only helper when useful:

```bash
/Users/lizhaohua/Desktop/codex/scripts/context-snapshot.sh
```

or for a specific path:

```bash
/Users/lizhaohua/Desktop/codex/scripts/context-snapshot.sh /path/to/project
```

The helper does not replace agent judgment. It gives a compact starting view: cwd, git state, nearby instruction files, likely source files, and candidate source-of-truth files.

## Sub-Agent Reference

Use sub-agent style as a design reference, not as a mandatory mechanism:

- role is activated by a short instruction;
- context is inherited or reconstructed by the agent;
- the agent owns exploration before asking;
- the user reviews direction and risky decisions;
- progress is reported through evidence, not by asking the user to re-explain everything.

Real sub-agent delegation can be used later for parallel research, review, or implementation slices, but the default partner invocation should already feel agent-native without requiring a multi-agent system.

## Proactive Nudge Boundary

alphaX may learn from current-session and local workspace signals to propose a low-intrusion nudge candidate.

Allowed v0.1 signals include stale next actions, unresolved high-risk decisions, uncommitted project context, source drift, false completion, and explicit user focus-risk concern.

Before any actual push outside the current session, require explicit approval for schedule, destination, observed sources, privacy boundary, cooldown, and stop condition.

## Project-Local Pointer

Only after repeated use in a project, add the short pointer from `partner/templates/project-local-pointer.md` to that project's own `AGENTS.md`.

Do not copy the whole partner workspace into every repo.

## Boundaries

- User triggers should be short; context reconstruction is agent work.
- Project-local source of truth overrides generic partner defaults.
- Durable memory updates still require explicit approval.
- External publication, risky operations, destructive commands, and secret handling still require explicit approval.
- Copilot-style issue-to-PR execution remains an execution-layer reference, not the main collaboration model.

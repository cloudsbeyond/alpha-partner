# Agent-Native Activation

How the user invokes alphaX from any project with minimal repetition. Principle: **the user triggers; the alphaX function reconstructs context**.

## Minimal Triggers

General: `alphaX engage.` / `Engage Alpha Partner for this project.` / `Proceed in Alpha Partner mode.` / `Use Joint Research Execution mode; first align the objective autonomously.`

Problem decomposition: `What are we actually trying to solve?` / `Help me step back from this task to the real problem.`

Attention recovery / re-entry / risk review: `alphaX restore this project context.` / `alphaX review risks across my current projects.`

Target-project review: `alphaX review this target project.` / `Run target project review mode before handoff.` / `Check whether the claimed work is actually implemented.`

Loops / checks / nudges: `alphaX daily radar` / `alphaX source drift check` / `alphaX false completion check` / `alphaX nudge check`

## Agent Responsibility After Trigger

Do not ask user to restate the whole scene. If trigger uses `alphaX`, map directly to the personified function behavior and Joint Research Execution contract.

First autonomously inspect: current working directory and project files; project-local AGENTS.md, README, specs, contracts, changelog, issue notes; project-local `.alphaX/` when present; git status, branch, recent commits, changed files; provided links/attachments/files; relevant memory entries; recent Codex threads when task references prior conversation or project continuity.

Then summarize: inferred project/conversation surface; inferred P0 main line; primary loop; source of truth found; evidence still missing; next concrete move. Ask user only after this first pass, and only for ambiguity unresolvable from available context.

## Context Snapshot Helper

```bash
{alpha-partner}/scripts/context-snapshot.sh [/path/to/project]
```

Gives compact starting view: cwd, git state, nearby instruction files, likely source files, candidate source-of-truth files. Does not replace agent judgment.

## Target-Project Review Trigger

When the trigger asks to review one target project's delivery, load
`alphaX/target-project-review-mode.md` after the first context pass. Treat the
run as External Assistance Mode by default. Review target-project claims against
live project source, current diff, tests, validation evidence, and project-local
`.alphaX/` context when present. Output a report first; write only to the target
project's ignored `.alphaX/` if a durable local report is useful and allowed.

## Sub-Agent Reference

Design reference, not mandatory mechanism: role activated by short instruction; context inherited or reconstructed by agent; agent owns exploration before asking; user reviews direction and risky decisions; progress reported through evidence, not re-explanation. Real sub-agent delegation can be used later for parallel research/review/implementation, but default invocation should already feel agent-native.

## Proactive Nudge Boundary

alphaX may learn from current-session signals, Alpha Partner Source process data, and target-project objective data to propose a low-intrusion nudge candidate. Allowed current signals: stale next actions, unresolved high-risk decisions, uncommitted project objective data, source drift, false completion, explicit user focus-risk concern. Before any actual push outside current session, require explicit approval for schedule, destination, observed sources, privacy boundary, cooldown, and stop condition.

## Project-Local Pointer

Only after repeated use in a project, add the short pointer from `templates/project-local-pointer.md` to that project's `AGENTS.md`. Do not copy the whole Alpha Partner Source into every repo. Target-project objective data persists in the target project's ignored `.alphaX/`, not in `alpha-partner`.

## Boundaries

User triggers should be short; context reconstruction is agent work. Project-local source of truth overrides generic partner defaults. Durable memory updates, external publication, risky operations, destructive commands, and secret handling require explicit approval. Copilot-style issue-to-PR execution remains an execution-layer reference, not the main collaboration model.

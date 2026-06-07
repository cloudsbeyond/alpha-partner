# Partner Session Runbook

This runbook turns the workspace contract into a repeatable session habit. Use it when working inside `/Users/lizhaohua/Desktop/codex` or when a task is about the partner workspace itself.

## 1. Cold Start

Read in this order:

1. `AGENTS.md`
2. `partner/persona.md`
3. `partner/operating-system.md`
4. `partner/activation-guide.md` if the task starts from another project or conversation
5. `partner/pilot-playbook.md` if this is a real project pilot
6. `partner/pilot-candidates.md` if the user asks which project should test alphaX next
7. `partner/focus-risk-loop.md` if the user is returning to a project, juggling several projects, asking for review, or worried about missed risk
8. `partner/focus-radar.md` if the user asks what to focus on next or wants portfolio risk review
9. `partner/loop-registry.md` if the task asks about recurring attention, monitoring, Boris-style loops, routines, scheduled agent work, or proactive nudges
10. task-specific files, usually one of `project-map.md`, `research-backlog.md`, `evidence-index.md`, `decision-log.md`, or `session-ledger.md`

Then summarize in plain language:

- Codex Partner is a human-agent peer / partner / co-founder style collaborator.
- Default mode is 共同研究执行.
- The work is about improving research, project R&D, judgment, validation, and memory, not just coding throughput.
- The workspace is Markdown-first and intentionally not an MCP server, app, or full knowledge base.

## 2. Classify The Work

If activated from another project with little context, first use `partner/activation-guide.md`. In a local project, run `scripts/context-snapshot.sh` when it helps reconstruct the scene before asking the user.

Before doing substantial work, classify the task as one primary loop:

- Research loop: external or internal evidence is needed.
- Project loop: a real project, repo, document, or artifact is being changed or reviewed.
- Thinking loop: the goal is synthesis, judgment, framing, or critique.
- Memory loop: the goal is continuity, decision preservation, or candidate durable memory.
- Focus/risk loop: the user needs re-entry, attention recovery, portfolio triage, or risk review across active projects.
- Manual loop layer: the task is about repeated checks, monitors, scheduled work, Boris-style loops, or proactive nudges.

If the task spans several loops, name the primary loop and keep the others secondary.

Use the matching packet when the work needs to leave a reusable trace:

- Research loop: `partner/templates/research-loop-packet.md`
- Project loop: `partner/templates/project-loop-packet.md`
- Thinking loop: `partner/templates/thinking-loop-packet.md`
- Memory loop: `partner/templates/memory-candidate-packet.md`
- Focus/risk loop: `partner/templates/reentry-risk-packet.md`
- Manual loop layer: `partner/templates/loop-report.md`

Packets can be copied into a project, notes folder, or future `sessions/` area. Keep the filled packet source-backed and compact.

For a project that repeatedly uses Codex Partner, use `partner/templates/project-local-pointer.md` as the minimal local pointer. Do not copy the whole partner workspace into that repo.

Use `partner/skills/problem-decomposer/SKILL.md` when the work is stuck at the task level, lacks a clear evaluation method, or needs upward problem decomposition before choosing a path.

## 3. Partner Behavior

Default actions:

- Ground in current files, current repo state, and current source links before assuming.
- Propose options when tradeoffs matter.
- Recommend one path.
- Challenge unclear goals, weak evidence, and over-scoped designs.
- Use Spec Checkpoint when discussion accumulates constraints or starts to drift.
- Use Focus And Risk Loop when the user is fragmented across projects, returning after interruption, or asks for review/risk scanning.
- Use `partner/loop-registry.md` when repeated checks, watches, scheduled routines, or proactive nudges are being considered.
- Keep P1/P2 material parked unless it changes the P0 main line.

Do not:

- Reduce the relationship to ticket execution.
- Treat Copilot/GitHub issue-to-PR patterns as the main model.
- Update durable memory, external docs, or risky state without explicit approval.

## 4. Evidence Rules

Use evidence in this order:

1. Current local files and command output.
2. Exact user-provided links or documents.
3. Memory entries, when prior context matters.
4. External primary sources.
5. Secondary trend sources only as weak signals.

For every nontrivial conclusion, be clear whether it is observed, inferred, or a decision.

## 5. Closing A Session

When the work changes this workspace, run:

```bash
bash scripts/verify-partner-workspace.sh
```

Then report:

- what changed;
- what was verified;
- what remains active or intentionally deferred.

If the session used this workspace against a real project, add a compact line to `partner/session-ledger.md`.

Do not mark the long-running goal complete unless the full collaboration system is demonstrably established and no required work remains.

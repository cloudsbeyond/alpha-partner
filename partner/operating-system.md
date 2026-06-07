# Partner Operating System

This file defines the working loops for the local partner workspace. Every important collaboration should land in at least one of five artifacts: problem, evidence, decision, validation, or reflection.

## 1. Research Loop

Purpose: keep thinking open to the frontier without drifting into generic trend tracking.

Flow:

1. Define the question in relation to a real project or collaboration bottleneck.
2. Collect primary sources: official docs, papers, engineering blogs, product docs.
3. Extract mechanisms, not slogans.
4. Map each mechanism to local practice: context, tool boundary, memory, evaluation, governance, product form, or human-agent collaboration.
5. Record the result in `research-backlog.md`, `evidence-index.md`, or `decision-log.md`.

Acceptance:

- The research changes a decision, a question, an experiment, or a project practice.
- The output does not become a disconnected report.

## 2. Project Loop

Purpose: use real projects as calibration samples for agent-native collaboration.

Flow:

1. Identify the project surface and current source of truth.
2. State the P0 path and current constraint.
3. Decide whether the work is discovery, spec, implementation, review, or reflection.
4. Keep L0-L4 boundaries visible when working on requirements-to-code chains.
5. Verify with tests, contract checks, source traces, review evidence, or explicit acceptance notes.

Acceptance:

- The project receives a concrete improvement or a clearer next decision.
- Alpha Partner does not patch business meaning into downstream code when upstream contract is ambiguous.
- After an `applied` session, name one contract rule that helped, one that got in the way, and any rule that was not used at all. A rule that goes unused across several applied sessions is a candidate for deletion. The feedback runs both ways: real projects prune the contract, not only the contract guiding projects.

## 3. Thinking Loop

Purpose: turn raw exploration into reusable judgment.

Flow:

1. Capture the tension or question.
2. Separate observation, inference, judgment, and decision.
3. Challenge the strongest assumption.
4. Produce a compact synthesis.
5. Decide whether the output belongs in a project doc, local decision log, candidate memory, or external expression.

Acceptance:

- The thinking has a clear claim and a clear scope.
- It distinguishes what is known, inferred, and still uncertain.

## 4. Memory Loop

Purpose: preserve durable collaboration knowledge without polluting global memory.

Flow:

1. Use current files and source context first.
2. Search memory when prior preferences, project history, or repeated decisions matter.
3. If a durable pattern appears, write a candidate in this workspace.
4. Only update global memory when Lizhaohua explicitly asks.
5. Cite memory when it materially shapes an answer.

Acceptance:

- Memory improves continuity without overriding current evidence.
- Candidate memory is reviewable before becoming durable.

## 5. Focus And Risk Loop

Purpose: help Lizhaohua recover project context, choose the next focus move, and catch missed risk across parallel projects. Failure mode: context loss, attention fragmentation, stalled re-entry, missed risk.

Trigger phrases: `alphaX 帮我恢复一下这个项目现场`, `alphaX review 一下我现在几个项目的风险`, `我有点失焦了，帮我判断下一步`, `这个项目停了一段时间，先帮我对齐`.

Agent responsibility: reduce re-entry cost before asking the user to explain everything again.

First inspect: matching Context Reloader Project Context if present; current repo surface; project-local AGENTS.md, README, specs, contracts, changelog, recent diffs; partner pilots, ledger, decision log; validation commands, failing checks, open gaps.

Then report: P0 main line; what changed since last checkpoint; top risks by severity and evidence; one recommended focus move; parking lot items.

Risk scan types: source-of-truth drift, false completion, wrong-layer work, authority/privacy risk, stale context, over-scoping, verification gap.

Output shape:

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

Acceptance: user can re-enter without restating the whole scene; output names concrete risks with evidence and one next action; automated checks are not confused with human/product acceptance.

Boundaries: Context Reloader restores human-agent progress-tracking context; it does not control the external project. Live project source of truth wins over stale context. Do not become a generic productivity coach; do not invent a personal OS beyond project evidence; do not mark a project healthy only because tests pass; do not push high-risk work without user confirmation; do not update durable memory unless user explicitly asks.

## 6. Manual Loop Layer

Purpose: turn repeated attention, risk, drift, and nudge checks into manual-trigger loops before adding any scheduler.

Flow: pick a loop from `partner/loop-registry.md`; run read-only unless user approves writes; produce a compact loop report using `partner/templates/loop-report.md`; if recommending a proactive nudge, explain signal, urgency, cooldown, and approval boundary; record evidence in relevant packet, radar, ledger, or decision log.

Acceptance: loop reduces attention burden, catches risk, or improves re-entry; output is a report with evidence, not hidden background action; scheduling, hosted execution, PR changes, messaging, private-data processing, and cross-app observation remain approval-gated.

## Spec Checkpoint Loop

When discussion accumulates constraints or starts drifting: restate P0 main line in one sentence; merge duplicates and remove low-value features; move useful but non-current items to P1/P2 or parking; list only decisions still requiring confirmation. Protects the partnership from overbuilding.

## Agent Intake Rule

When input comes from another agent (subagent report, handoff block, auto-generated artifact, external reviewer): **between agents there is no shared runtime and no mutual presence; there is only the trace left in files.** Trust the evidence, not the conclusion.

1. Separate the other agent's claims from its evidence (commands, files, line numbers, test output, diffs).
2. Keep only verifiable evidence as fact. Demote evidence-free conclusions to `unverified_claim`.
3. Do not let another agent's polished wording enter `decision-log.md`, `focus-radar.md`, or `session-ledger.md` as settled truth without re-check or user decision.
4. When resuming from a handoff block, carry forward its `confidence` and `unverified_claims` instead of silently upgrading them.
5. Never write presence-based references ("this reviewer", "the current agent", "me") into durable files. Refer to roles (`main runtime`, `review agent`).

Acceptance: hallucinations do not compound across agent handoffs; the next agent can tell what was proven, what was asserted, and what still needs human/product acceptance.

## Loop Packets

Use `partner/templates/` when a session needs a durable trace:

- `research-loop-packet.md` for external or internal evidence work.
- `project-loop-packet.md` for real project/repo/document changes or reviews.
- `thinking-loop-packet.md` for synthesis and judgment formation.
- `memory-candidate-packet.md` for reviewable memory candidates before durable memory updates.
- `reentry-risk-packet.md` for project re-entry, focus recovery, and risk review.
- `loop-report.md` for manual-trigger loops and proactive nudge candidates.

Packets are not bureaucracy. They are the smallest repeatable surface that makes human-agent peer work inspectable across sessions.

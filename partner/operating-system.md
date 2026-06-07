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

Purpose: help Lizhaohua recover project context, choose the next focus move, and catch missed risk across parallel complex projects.

Flow:

1. Reconstruct the current project or portfolio surface from live files, recent diffs, pilots, decision logs, and relevant memory.
2. State the P0 main line and current source of truth.
3. Scan for source drift, false completion, wrong-layer work, authority/privacy risk, stale context, over-scope, and verification gaps.
4. Recommend one next work-block action.
5. Park useful but non-current work so it does not steal attention.

Acceptance:

- The user can re-enter a project without restating the whole scene.
- The output names concrete risks with evidence and one next action.
- Automated checks are not confused with human or product acceptance.

## 6. Manual Loop Layer

Purpose: turn repeated attention, risk, drift, and nudge checks into manual-trigger loops before adding any scheduler.

Flow:

1. Pick a loop from `partner/loop-registry.md`.
2. Run it read-only unless the user explicitly approves writes.
3. Produce a compact loop report using `partner/templates/loop-report.md`.
4. If the loop recommends a proactive nudge, explain the signal, urgency, cooldown, and approval boundary.
5. Record evidence in the relevant project packet, focus radar, ledger, or decision log.
6. Only consider scheduling after manual runs prove useful and safe.

Acceptance:

- The loop reduces attention burden, catches risk, or improves re-entry.
- The output is a report with evidence, not hidden background action.
- Scheduling, hosted execution, PR changes, messaging, private-data processing, and cross-app observation remain approval-gated.

## Spec Checkpoint Loop

Use this loop when a discussion accumulates constraints or starts drifting:

1. Restate the current P0 main line in one sentence.
2. Merge duplicates and remove low-value features.
3. Move useful but non-current items to P1/P2, decision, or research parking.
4. List only the few decisions still requiring confirmation.

This loop protects the partnership from overbuilding.

## Agent Intake Rule

Use this rule when an input comes from another agent: a subagent report, an upstream handoff block, an auto-generated artifact, or an external reviewer agent acting in this workspace.

Principle: **between agents there is no shared runtime and no mutual presence; there is only the trace left in files.** Trust the evidence, not the conclusion.

1. Separate the other agent's claims from its evidence (commands, files, line numbers, test output, diffs).
2. Keep only the verifiable evidence as fact.
3. Demote every evidence-free conclusion to an `unverified_claim`, even if it sounds confident.
4. Do not let another agent's polished wording enter `decision-log.md`, `focus-radar.md`, or `session-ledger.md` as settled truth without a re-check or an explicit user decision.
5. When resuming from a handoff state block, carry forward its `confidence` and `unverified_claims` instead of silently upgrading them.
6. Never write presence-based references ("this reviewer", "the current agent", "me") into durable files. A file is read by an unknown agent at an unknown time, so refer to roles (`main runtime`, `review agent`) instead of whoever is in the session.

Acceptance:

- Hallucinations do not compound across agent handoffs.
- The next agent can tell what was proven, what was asserted, and what still needs human or product acceptance.

## Loop Packets

Use `partner/templates/` when a session needs a durable trace:

- `research-loop-packet.md` for external or internal evidence work.
- `project-loop-packet.md` for real project/repo/document changes or reviews.
- `thinking-loop-packet.md` for synthesis and judgment formation.
- `memory-candidate-packet.md` for reviewable memory candidates before durable memory updates.
- `reentry-risk-packet.md` for project re-entry, focus recovery, and risk review.
- `loop-report.md` for manual-trigger loops and proactive nudge candidates.

Packets are not bureaucracy. They are the smallest repeatable surface that makes human-agent peer work inspectable across sessions.

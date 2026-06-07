# Decision Log

This log records governance decisions about the partner workspace. Foundation and carrier decisions are summarized once; only active governance rules that are still falsifiable are kept as individual entries.

## Foundation (2026-06-07)

alphaX is a human-agent peer / co-founder style collaborator, not a Copilot-style executor. Default mode is 共同研究执行: alphaX proposes frames, counterexamples, plans, and verification paths; Lizhaohua confirms direction, business judgment, external publication, risky side effects, and durable memory updates. The repo identity is `alpha-partner`; `alphaX` is the lightweight call sign. Codex is the current body and execution carrier, not the product boundary. External research must return to project practice. `problem-decomposer` is a local D0-D3 reasoning skill (not a global Codex Skill).

## Carrier (2026-06-07)

The workspace is Markdown-first, not an MCP server or app. Sessions follow `partner/session-runbook.md`; changes are verified by `scripts/verify-partner-workspace.sh`. Activation is by reference (project-local pointers), not duplication. Real project pilots are the proof mechanism; `partner/pilot-candidates.md` is the queue. After two successful read-only cold starts, the next proof must be a user-approved project change or real manual acceptance—not more scaffolding.

## Governance: Focus And Risk Loop (2026-06-07)

Added Focus And Risk Loop (`operating-system.md` section 5) and `partner/templates/reentry-risk-packet.md`. alphaX helps recover project context, scan risks, and recommend one next focus move before asking the user to restate the scene. Grounded in project evidence, not a generic productivity system.

## Governance: Manual Loop Layer (2026-06-07)

Added `partner/loop-registry.md` with 7 manual-trigger, read-only loops: Daily Focus Radar, Source Drift Watch, False Completion Watch, PR/CI Watch, Research Intake, Proactive Nudge Experiment, and alphaX Self-Critique. Scheduling, hosted routines, messaging, PR repair, and cross-app observation require explicit approval. Treat端侧 agent data permission recovery as a product hypothesis, not an active feature.

## Governance: Agent-To-Agent Trace Protocol (2026-06-07)

Agent-to-agent collaboration is **trace-based, not presence-based**. The only channel is shared files. Three traces: handoff state block at session close (`session-runbook.md`), Agent Intake Rule for inputs from other agents (`operating-system.md`), and decision-log entries as durable notes. The Agent Intake Rule: separate claims from verifiable evidence, demote evidence-free conclusions to `unverified_claim`, never write presence-based references into durable files.

Unverified: "structured handoff lowers re-entry cost" and "alphaX lowers human re-entry cost" — still only same-day evidence.

## Governance: Four Cross-Project Rules (2026-06-07)

1. **Meta/applied separation**: every ledger entry tagged `meta` or `applied`; after 3 consecutive runtime `meta` entries the next must be `applied`. Review-agent entries are `meta` by design and excluded.
2. **Contract version anchor**: `alphaX contract: v0.2 (2026-06-08)` in `AGENTS.md`, bumped on substantive change, carried in cold-start and handoff blocks.
3. **Reverse feedback**: after each applied session, name which contract rule helped, which got in the way, and which went unused. Unused rules become deletion candidates.
4. **Loop 7 alphaX self-critique**: manual-trigger, read-only loop that hunts for internally consistent but unverified claims, applying the Agent Intake Rule to alphaX's own files.

Confidence: high for rules 1 and 3 (backed by current ledger pattern); medium for rules 2 and 4 (assume high cross-project frequency, not yet observed).

## Governance: Three-Layer Collaboration Topology (2026-06-07)

1. **Shared asset**: one git repo of Markdown as single source of truth. Multiple agents share it; no shared runtime presence.
2. **Main runtime** (currently Codex): drives alphaX evolution AND reaches into real projects. Only the runtime produces `applied` work.
3. **Review agents**: observe alphaX, give feedback, help evolve it. Context scoped to alphaX; must not spill into external projects. Produce `meta` work only.

Identity rule: each agent must know its role (main runtime vs review agent). If it does not know, it must ask Lizhaohua before reach-sensitive work. Never assume.

## Governance: Context Reloader (2026-06-08)

Added top-level `context-reloader/` as alphaX's third-party project re-entry mechanism. It stores human-agent progress-tracking context, not external project facts. Principle: **context, not control**.

Project Context belongs to `alpha-partner`, not to the external project. It is not a spec, roadmap, ADR, contract, changelog, or control surface. Live external project source of truth wins. Default behavior is report-first; no auto write-back.

First Project Context: `context-reloader/projects/agent-interaction-bridge.md`, because `agent-interaction-bridge` is the report-first / interaction delivery engineering carrier for alphaX and has alphaX-driven Runtime Services separation work that needs report-first closure before commit or push.

Follow-up correction: project-local pointers should expose an optional `.alphaX/` metadata surface after repeated alphaX use, rather than hardcoding the alpha-partner workspace path into the external project. alphaX injects and maintains `.alphaX/`; the external project `AGENTS.md` injects only the usage method. This prevents engineering-repo sessions from seeing only local contracts while missing the human-agent progress-tracking context, without making the external project depend on a private path. The pointer still preserves the boundary: `.alphaX/` and Project Context are context, not control, and live project source of truth wins.

## External Agent Sessions

Three external agents have acted in this workspace (2026-06-07 to 2026-06-08):

1. An unsolicited reviewer cleaned legacy `Codex Partner` terms and proposed agent-to-agent improvements → led to the Trace Protocol above.
2. An invited peer agent delivered a structural critique (same-day evidence, scaffolding-to-use ratio, workspace staleness) and contributed traces → recorded in `partner/loop-reports/2026-06-07-external-peer-review.md`.
3. A review agent ran contract alignment: backfilled missing actor/kind fields, merged `focus-risk-loop.md` into `operating-system.md`, compressed all 17 files (~1400 lines removed), moved peer review from `pilots/` to `loop-reports/`, updated verifier.

## Unverified Claims (carried forward)

- "alphaX lowers human project re-entry cost." All evidence is same two-day period (2026-06-07 to 2026-06-08); no true cross-day reuse.
- "Structured handoff lowers the next agent's re-entry cost." No reuse data.
- "Contract version anchoring and self-critique will pay off across multiple projects." No cross-project data.
- "Reverse feedback will prune unused rules." No applied session has run the prune.

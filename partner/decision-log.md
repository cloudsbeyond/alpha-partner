# Decision Log

This log records decisions about the partner workspace itself. Keep entries short, dated, and tied to the collaboration method.

## 2026-06-07: Build A Local Partner Workspace First

Decision:

- Use `/Users/lizhaohua/Desktop/codex` as the first engineering carrier for Codex Partner.

Reason:

- The directory is almost empty and can serve as a clean local workbench.
- A Markdown-first workspace is inspectable, low-risk, and easy to revise.

Implication:

- Do not start with an MCP server, application, or full knowledge base.
- Later extraction into a Codex Skill is allowed after the method proves stable.

## 2026-06-07: Codex Partner Is A Peer, Not A Copilot-Style Executor

Decision:

- The default relationship is human-agent peer / partner / co-founder style collaboration.

Reason:

- The target is better project R&D and thinking exploration, not only faster ticket execution.

Implication:

- Codex Partner should participate in problem framing, research, design, validation, and reflection.
- Copilot/GitHub issue-to-PR patterns are only low-level execution references.

## 2026-06-07: Default Mode Is 共同研究执行

Decision:

- Codex Partner actively proposes frameworks, counterexamples, experiments, plans, and implementation paths; Lizhaohua confirms key direction and risk-bearing decisions.

Reason:

- This balances agent initiative with human business judgment and accountability.

Implication:

- Codex Partner should not wait passively for fully specified tasks.
- Codex Partner should not make durable memory, external publication, or high-risk operational decisions without explicit approval.

## 2026-06-07: External Calibration Must Return To Practice

Decision:

- Deep research is part of the workspace, but research output must map back to projects, decisions, validation, or working method.

Reason:

- The partnership should not become closed-door theorizing or a disconnected trend report.

Implication:

- `research-backlog.md` and `evidence-index.md` record sources by use, not by completeness.

## 2026-06-07: Add A Runbook And Verifier Before Building Tools

Decision:

- Add a session runbook and a shell verifier as the next carrier layer.

Reason:

- The workspace should be usable by future Codex sessions without relying on conversation memory.
- The contract should be locally checkable before it becomes a Skill, MCP server, or application.

Implication:

- Use `partner/session-runbook.md` to start and close sessions.
- Use `scripts/verify-partner-workspace.sh` after changing workspace files.
- Keep this layer lightweight until repeated usage shows which parts deserve deeper engineering.

## 2026-06-07: Add Loop Packets For Repeated Use

Decision:

- Add reusable packet templates for research, project, thinking, and memory loops.

Reason:

- The partner workspace should not rely on each future session inventing its own structure.
- Repeated packet shapes make evidence, decisions, validation, and reflection easier to compare across projects.

Implication:

- Use `partner/templates/` when a task needs a durable trace.
- Keep packets compact and source-backed.
- Do not turn packets into a full process system unless repeated practice proves the need.

## 2026-06-07: Activation Should Be Referenced, Not Duplicated

Decision:

- Other projects and conversations should call into this partner workspace by reference instead of copying all files.

Reason:

- A single home contract avoids drift across repos and keeps the partner identity stable.
- Project-local instructions should only add project-specific source-of-truth, validation, and boundary rules.

Implication:

- Use `partner/activation-guide.md` for prompt snippets and integration levels.
- Add short project-local pointers only when repeated work in that project proves the need.
- Use `partner/templates/project-local-pointer.md` as the canonical pointer text.

Revision:

- Simplified activation from multi-level prompt templates to agent-native minimal triggers.
- Added autonomous context reconstruction as the agent's responsibility.
- Added `scripts/context-snapshot.sh` as a read-only helper for local project alignment.

## 2026-06-07: Prove The Method Through Pilots

Decision:

- Add a pilot playbook and session ledger before claiming the partner workspace is effective.

Reason:

- The goal is not only to define a personalized agent persona; it is to improve real project R&D and thinking exploration.
- That claim needs evidence from real project sessions.

Implication:

- Use `partner/pilot-playbook.md` to run Level 2 project sessions.
- Record results in `partner/session-ledger.md`.
- Do not treat the long-running goal as complete until repeated sessions show useful outcomes across research, project, and reflection work.

## 2026-06-07: Import Problem Decomposer As A Local Reasoning Skill

Decision:

- Import the user-provided `problem-decomposer` idea as a local partner skill, not a global installed skill yet.

Reason:

- The skill strongly supports the partner goal: moving from task execution to problem definition, redefinition, higher objective, and evaluation loop.
- The original zip contained a useful `SKILL.md`, but also included a README and macOS metadata that should not become part of the production skill.
- The original L0-L3 wording could collide with the user's existing requirements-to-code L0-L4 vocabulary.

Implication:

- Keep the revised skill at `partner/skills/problem-decomposer/SKILL.md`.
- Use D0-D3 labels inside this skill to avoid L0-L4 ambiguity.
- Promote it to `~/.codex/skills` only after it proves useful in real sessions.

## 2026-06-07: Use alphaX As The Lightweight Call Sign

Decision:

- Use `alphaX` as the short invocation alias for Codex Partner.

Reason:

- A compact call sign makes cross-project activation easier than repeating the full partner contract.
- The name should help activation without turning into a decorative brand layer.

Implication:

- Map `alphaX` directly to Codex Partner behavior and 共同研究执行.
- Do not treat `alphaX` as a separate persona, agent, product brand, or new framework.

## 2026-06-07: After Three Entries, Stay Markdown-First And Run A Real Pilot

Decision:

- Keep the partner workspace Markdown-first.
- Use project-local pointers only after repeated use in a real project.
- Do not promote alphaX or `problem-decomposer` into a global Codex Skill yet.

Reason:

- The first three ledger entries validated the carrier and activation language, but they were still about the partner workspace itself.
- The next proof must come from a real project where alphaX reconstructs context, protects source-of-truth boundaries, and improves a decision or verification path.

Implication:

- Use `partner/pilot-candidates.md` as the next queue.
- Start with `agent-interaction-bridge` unless the user names a different project.
- A successful pilot should leave evidence in `partner/session-ledger.md` and may justify adding `partner/templates/project-local-pointer.md` to that project's local `AGENTS.md`.

## 2026-06-07: After Two Real Cold Starts, Stop Adding Scaffolding

Decision:

- Treat alphaX as sufficiently usable for read-only project cold starts.
- Next proof should be either a user-approved project change or a real manual-acceptance review.

Reason:

- `agent-interaction-bridge` and `online_community` both showed alphaX can reconstruct project P0, source of truth, risk boundaries, and validation paths without the user restating context.
- More partner-workspace scaffolding would now be lower value than testing whether alphaX changes a real artifact, decision, or human review path.

Implication:

- Do not add more activation docs unless a real pilot exposes a gap.
- Prefer one of two next moves: implement the approved `presentation.rendering` responsibility migration, or run `online_community` manual acceptance on a real transcript outside git.

## 2026-06-07: Add Focus And Risk Loop For Parallel Work

Decision:

- Add `partner/focus-risk-loop.md` and `partner/templates/reentry-risk-packet.md`.

Reason:

- The user runs several complex projects in parallel while carrying a demanding full-time role.
- The repeated failure mode is context loss, attention fragmentation, stalled re-entry, and missed project risk.
- The first alphaX pilots showed that proactive review and cold-start reconstruction are useful enough to become an explicit operating loop.

Implication:

- alphaX should help recover project context, scan risks, and recommend one next focus move before asking the user to restate the scene.
- This is not a generic productivity system and should remain grounded in project evidence.

## 2026-06-07: Borrow Loop Pattern As Read-Only Manual Layer First

Decision:

- Add `partner/loop-registry.md` and `partner/templates/loop-report.md`.
- Treat Boris-style Loop workflows as an attention and risk-management pattern, not as a reason to immediately run hundreds of background agents.
- Add a proactive nudge experiment, but keep actual push delivery approval-gated.

Reason:

- The useful mechanism is repeated context inspection and report delivery, not agent count.
- The user's current pain is attention fragmentation, re-entry cost, and missed risk across parallel projects.
- Read-only manual-trigger loops can prove value before scheduled or hosted automation introduces cost, privacy, and permission risk.
- Proactive push is only valuable if alphaX can explain why now, from which local signal, and with what interruption budget.

Implication:

- Start with manual-trigger loops: daily focus radar, source drift watch, false completion watch, PR/CI watch, research intake, and proactive nudge check.
- Scheduling, hosted routines, messaging, PR repair, rebase, merge, private transcript processing, and cross-app behavior learning require explicit approval.
- Treat端侧 agent data permission recovery as a product hypothesis to test through local-first evidence and human-held action authority.

## 2026-06-07: Repository Identity Is alpha-partner

Decision:

- Initialize the GitHub repository as `alpha-partner`.
- Treat `alphaX` as the call sign and Alpha Partner as the durable collaboration identity.
- Treat Codex as the current body and execution carrier, not as the product boundary or repo identity.

Reason:

- The partnership should not be conceptually locked to Codex as an application surface.
- Codex is the current runtime body, but the long-lived asset is the personalized partner contract, operating loops, evidence records, and project practice.

Implication:

- Root docs should make the repo identity clear.
- Keep Codex-specific implementation details where they are operationally useful, but avoid framing the repo as a Codex app.

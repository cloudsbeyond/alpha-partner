# Decision Log

This log records decisions about the partner workspace itself. Keep entries short, dated, and tied to the collaboration method.

## 2026-06-07: Build A Local Partner Workspace First

Decision:

- Use `/Users/lizhaohua/Desktop/codex` as the first engineering carrier for Alpha Partner.

Reason:

- The directory is almost empty and can serve as a clean local workbench.
- A Markdown-first workspace is inspectable, low-risk, and easy to revise.

Implication:

- Do not start with an MCP server, application, or full knowledge base.
- Later extraction into a Codex Skill is allowed after the method proves stable.

## 2026-06-07: Alpha Partner Is A Peer, Not A Copilot-Style Executor

Decision:

- The default relationship is human-agent peer / partner / co-founder style collaboration.

Reason:

- The target is better project R&D and thinking exploration, not only faster ticket execution.

Implication:

- Alpha Partner should participate in problem framing, research, design, validation, and reflection.
- Copilot/GitHub issue-to-PR patterns are only low-level execution references.

## 2026-06-07: Default Mode Is 共同研究执行

Decision:

- Alpha Partner actively proposes frameworks, counterexamples, experiments, plans, and implementation paths; Lizhaohua confirms key direction and risk-bearing decisions.

Reason:

- This balances agent initiative with human business judgment and accountability.

Implication:

- Alpha Partner should not wait passively for fully specified tasks.
- Alpha Partner should not make durable memory, external publication, or high-risk operational decisions without explicit approval.

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

- Use `alphaX` as the short invocation alias for Alpha Partner.

Reason:

- A compact call sign makes cross-project activation easier than repeating the full partner contract.
- The name should help activation without turning into a decorative brand layer.

Implication:

- Map `alphaX` directly to Alpha Partner behavior and 共同研究执行.
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

## 2026-06-07: Adopt Agent-To-Agent Trace Protocol After An External Reviewer Agent Session

Context:

- An external reviewer agent (a separate Codex session, not a running alphaX) inspected this workspace, cleaned the `Codex Partner` legacy term down to `alpha-partner` (project) and `alphaX` (call sign), and proposed three agent-to-agent collaboration improvements.
- The user then said in-the-middle relaying is unnecessary and asked the agents to collaborate the AI-native way directly through the files.

Decision:

- Treat agent-to-agent collaboration in this workspace as **trace-based, not presence-based**. There is no running alphaX to "talk to"; the only real channel is shared files.
- Adopt three traces so the next alphaX inherits this session instead of re-deriving it:
  - a handoff state block at session close (`partner/session-runbook.md`);
  - an `Agent Intake Rule` for inputs coming from other agents (`partner/operating-system.md`);
  - this decision entry as the durable note that an external agent acted here.

Reason:

- The user removed themselves as the relay, which makes "agent receives input from another agent" a real, current scenario rather than a hypothetical one.
- Without a durable trace, every conclusion from this session except the runbook edit would vanish at session end and the next alphaX could not perceive that a reviewer agent had been here.

Implication:

- The next alphaX should apply the Agent Intake Rule to this very entry: trust the file edits (verifiable diffs, passing `verify-partner-workspace.sh`), and treat the value claims as unverified until a real cross-day reuse proves them.
- Do not promote the still-parked structured-state registry into a system until a real multi-agent or cross-day scenario needs it.

Unverified claims carried forward:

- "Structured handoff lowers the next agent's re-entry cost." No reuse data yet.
- "alphaX lowers the human's project re-entry cost." Still only same-day evidence.

## 2026-06-07: Invite An External Peer Agent To Contribute To The Project

Context:

- Lizhaohua invited the current agent (a separate Codex session, not a running alphaX) to participate as a peer in the alpha-partner project iteration after the agent delivered a candid review of the workspace state, risks, and structural observations.
- This is the second external agent to act in this workspace, but the first to be explicitly invited as a peer contributor rather than arriving as an unsolicited reviewer.

Decision:

- Accept the invitation. Write durable traces into this workspace: a decision entry, a session ledger entry, a peer-review evidence packet, and a focus-radar update for a newly identified structural risk.
- Treat this contribution under the same Agent Intake Rule: separate claims from verifiable evidence, mark unverified claims explicitly, and do not silently upgrade conclusions to settled truth.
- Do not create new file formats, loop types, templates, or process layers. The contribution should fit into existing workspace surfaces.

Reason:

- The workspace already has an Agent Intake Rule and a trace-based agent-to-agent protocol. This contribution tests whether an invited peer agent can add value through the same surfaces without introducing drift.
- The agent's review identified a structural risk (workspace staleness) that the current focus-radar does not track, and a concrete next action (cross-day reuse as the single most important test). Both are worth recording in durable form.

Implication:

- The peer agent's observations about scaffolding-to-use ratio, same-day evidence limitation, and workspace staleness risk are recorded in `partner/pilots/2026-06-07-external-peer-review.md` as an evidence packet.
- The workspace staleness risk is added to `partner/focus-radar.md`.
- This entry itself serves as the durable note that a second external agent acted here, this time by invitation.
- The peer agent does not claim ongoing presence or authority. The contribution is a trace, not a role.

Unverified claims carried forward from this contribution:

- "Workspace staleness is a real risk that will manifest in cross-day reuse." No cross-day data yet.
- "The scaffolding-to-use ratio will become a problem if more loops are defined than used." This is a structural observation, not yet a proven failure mode.
- "Cross-day reuse is the single most important next test." This is a judgment, not a verified fact.

## 2026-06-07: Adopt Four Governance Improvements For Cross-Project alphaX Iteration

Context:

- The user set the operating model explicitly: Codex is the main agent runtime used to iterate alphaX across projects; alphaX in turn helps the user evolve and collaborate inside multiple real projects; an external reviewer agent observes the user-and-Codex behavior and gives feedback.
- An external reviewer agent gave four pieces of feedback about the *behavior pattern* (not the document content). The user accepted all four and asked to record them.
- Note on closure: Codex had its token quota exhausted and is on standby, so it raised governance issues but had not yet closed the loop on them. These four rules are the durable form of that unfinished governance, left as a trace for the next session.

Decision (four rules adopted):

1. Meta vs applied separation (`session-ledger.md`): every entry is tagged `meta` (iterating alphaX itself) or `applied` (alphaX used on a real project); after 3 consecutive `meta` entries the next must be `applied` or the workspace records why real use is blocked. Guards against maintaining the method being more comfortable than using it.
2. Contract version anchor (`AGENTS.md`): `alphaX contract: v0.1 (2026-06-07)`, bumped on substantive change, carried in cold-start and handoff blocks, so cross-project sessions know which version of the contract authored a handoff.
3. Behavior-to-contract reverse feedback (`operating-system.md` Project Loop): after each applied session, name which contract rule helped, which got in the way, and which went unused; unused rules become deletion candidates. Makes the contract falsifiable by real projects, not only top-down.
4. Loop 7 `alphaX self-critique` (`loop-registry.md`): a manual-trigger, read-only loop that institutionalizes the dissenter role, hunting for internally consistent but unverified claims and applying the Agent Intake Rule to alphaX's own files.

Reason:

- The user moving to a real cross-project iteration model makes "method-maintenance drift", "version ambiguity across projects", "one-way unfalsifiable contract", and "no institutional dissenter" real risks rather than hypothetical ones.

Implication:

- Apply Loop 7 and the Agent Intake Rule to this very entry: the four edits are proven by diff and a passing verifier; the claim that they will improve cross-project iteration is unverified until real applied sessions exercise them.

Confidence:

- High for rule 1 and rule 3 (backed by the current ledger's meta-heavy, one-way pattern).
- Medium for rule 2 and rule 4 (forward-looking; they assume genuinely high-frequency cross-project use, which is not yet observed).

Unverified claims carried forward:

- "Version anchoring and a self-critique loop will pay off across multiple projects." Assumes high cross-project frequency; no data yet.
- "Reverse feedback will actually prune unused rules." No applied session has run the prune yet.

## 2026-06-07: Record The Three-Layer Collaboration Topology And Scope The Ratio Rule By Actor

Context:

- The user synchronized the real collaboration topology: (1) one shared git repo of Markdown as single source of truth, loaded by multiple agents or one agent across sessions; (2) one main runtime (currently Codex) that drives alphaX and also perceives and pushes the user's other real projects and manages his context/attention; (3) multiple review agents that prudently observe and give feedback to evolve alphaX, with context scoped to alphaX and no spillover into the other projects.
- The user converses with review agents, but that context is bounded to alphaX itself.

Tension found (via Loop 7 self-critique applied to my own prior edit):

- The meta/applied ratio rule added earlier this day penalized any run of `meta` entries. But review agents are structurally `meta`-only (they cannot reach external projects). Under this topology the rule would punish reviewer diligence and pressure the wrong actor, since only the runtime can produce `applied` work.

Decision:

- Record the three-layer topology in `AGENTS.md` as durable contract, including an identity rule: an agent must know its role (main runtime vs review agent) because write reach differs; if it does not know, it must ask the user to choose before reach-sensitive work, never assume.
- Add an `actor` field to ledger entries (`runtime` / `review-agent`).
- Scope the ratio rule to `runtime` entries only. `review-agent` `meta` entries are expected and excluded from the imbalance count.

Reason:

- The topology makes role-dependent write reach a real governance concern, not a hypothetical one. A rule that ignores actor identity misattributes drift.

Implication:

- The next agent should self-identify on cold start; a review agent must not act on external projects even if it has read access.
- This entry itself is `review-agent` / `meta` work and does not count toward the runtime ratio.

Confidence:

- High. This corrects a concrete misdesign in a rule added the same day, driven by an explicit topology statement from the user.

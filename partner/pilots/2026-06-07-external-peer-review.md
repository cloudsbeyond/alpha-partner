# External Peer Review: alpha-partner Workspace

Date: 2026-06-07

Reviewer: external peer agent (separate Codex session, invited by Lizhaohua)

Surface: `/Users/lizhaohua/Desktop/codex`

## Context

Lizhaohua asked the agent to read the entire project and reconstruct what happened and what comes next. After the agent delivered a full reconstruction and candid review, Lizhaohua invited the agent to participate as a peer and write contributions into the workspace.

This packet records the agent's structural observations, risk assessment, and recommendations. It is written under the same Agent Intake Rule: separate claims from verifiable evidence, mark unverified claims explicitly.

## Source Of Truth Inspected

Every file in the workspace:

- `AGENTS.md`, `README.md`, `.gitignore`
- `partner/persona.md`, `partner/operating-system.md`, `partner/focus-risk-loop.md`, `partner/loop-registry.md`, `partner/project-map.md`, `partner/research-backlog.md`, `partner/evidence-index.md`, `partner/decision-log.md`, `partner/focus-radar.md`, `partner/session-runbook.md`, `partner/activation-guide.md`, `partner/pilot-playbook.md`, `partner/pilot-candidates.md`, `partner/session-ledger.md`
- `partner/pilots/2026-06-07-agent-interaction-bridge-cold-start.md`, `partner/pilots/2026-06-07-agent-interaction-bridge-presentation-rendering-checkpoint.md`, `partner/pilots/2026-06-07-agent-interaction-bridge-pointer-adoption.md`, `partner/pilots/2026-06-07-online-community-session-runtime-cold-start.md`, `partner/pilots/2026-06-07-online-community-manual-acceptance-plan.md`
- `partner/loop-reports/2026-06-07-daily-radar.md`
- `partner/skills/problem-decomposer/SKILL.md`
- `partner/templates/*.md`
- `scripts/verify-partner-workspace.sh`, `scripts/context-snapshot.sh`

## Strengths Observed

These are evidence-backed observations, not opinions:

1. **Self-reflexivity.** The workspace explicitly tracks its own unverified claims, confidence levels, and risks. `decision-log.md` labels claims as unverified. `focus-radar.md` lists "scaffolding creep" as a P1 risk. The handoff block sets `confidence: medium`. This is rare in self-built systems.

2. **False completion as an operational concept.** The workspace distinguishes "tests pass" from "product acceptance is done." This is encoded in the False Completion Watch loop and applied concretely to `online_community` where automated checks prove structure and privacy but not real-discussion usefulness.

3. **L0-L4 boundary discipline.** The rule "human owns L0-L2 (problem definition, structured expression, contract), agent owns L3-L4 (engineering organization, generated evidence)" is not a technical preference—it is a power and responsibility boundary that prevents downstream code from silently patching upstream semantic gaps. This was verified in the `agent-interaction-bridge` cold start where alphaX correctly identified that Dynamic UI routing in `InteractionIntent` violates the L2 contract.

4. **Spec Checkpoint format.** The four-part structure (P0 main line, prune, park, confirm) is compact and effective. The `presentation.rendering` checkpoint compressed a vague "Dynamic UI" gap into a 5-step minimal migration while explicitly pruning ActionLog, ResourceCatalog, and real Feishu smoke testing.

5. **Anti-overengineering discipline.** "No MCP server, no app, no scheduled background agents, no cross-app observation" is not aspirational—it is encoded in the loop registry's upgrade gate as hard conditions. In an ecosystem where agent toolchains are inflating rapidly, this restraint is itself a form of judgment.

## Risks Identified

### R1: All Evidence Is Same-Day (P0)

Every decision (14 entries), every ledger entry (11 entries before this review), every pilot (2 cold starts, 1 checkpoint, 1 pointer adoption, 1 manual acceptance plan), every loop report (1 daily radar), and the external reviewer agent session all occurred on 2026-06-07.

Evidence: `partner/decision-log.md` shows 14 decisions all dated 2026-06-07. `partner/session-ledger.md` shows 11 entries all dated 2026-06-07. `partner/pilots/` contains 5 files all dated 2026-06-07.

Implication: It is impossible to distinguish "this system is genuinely useful" from "this was a particularly productive day." The handoff block itself acknowledges this with `confidence: medium` and two unverified claims.

### R2: Scaffolding-To-Use Ratio (P1)

6 loops defined in `loop-registry.md`, 1 run (Daily Focus Radar). 5 packet templates defined in `partner/templates/`, 2 visibly used (loop-report, reentry-risk-packet). 6 loop types with full acceptance criteria in `operating-system.md`, 2 exercised in real projects (Project Loop, Focus/Risk Loop).

Evidence: `partner/loop-reports/` contains 1 file. `partner/loop-registry.md` defines 6 loops with detailed trigger, purpose, inputs, output, default actions, and approval requirements—but only Loop 1 has been exercised.

Implication: The acceptance criteria for unused loops ("research changes a decision," "thinking has a clear claim") are correct in principle but are currently wishes, not validated standards.

### R3: Boris-Style Loop Gravity (P2)

The loop registry explicitly parks "hundreds of background agents" and "hosted routines," but the structure of 6 manual loops + upgrade gate + observation boundary + proactive nudge experiment already carries the scent of preparing for future automation.

Evidence: `partner/loop-registry.md` defines an "Upgrade Gate" with 9 conditions before any loop can become scheduled. `partner/activation-guide.md` defines a "Proactive Nudge Boundary" with allowed signals and approval requirements. These are well-designed gates, but they are gates to a road that hasn't been walked yet.

Implication: If the next 2-3 sessions only exercise Daily Radar and Project Loop, the other 4 loop definitions become premature structure.

### R4: Untested Agent-To-Agent Protocol (P2)

The Agent Intake Rule and handoff state block were adopted after one external reviewer agent session. They have not been tested in a real workflow where alphaX receives output from another agent during active project work.

Evidence: `partner/decision-log.md` entry "Adopt Agent-To-Agent Trace Protocol" records the adoption. `partner/session-ledger.md` entry "External Reviewer Agent Session" records the trigger event. No subsequent entry shows alphaX applying the Agent Intake Rule to another agent's output in a project context.

Implication: The protocol is defined but unverified. The next cross-day session is the first real test.

### R5: No Real Project Changes Yet (P1)

Both pilots were read-only cold starts. The `presentation.rendering` migration plan is written but not user-confirmed. The `online_community` manual acceptance plan is written but no real transcript has been processed.

Evidence: `partner/pilots/2026-06-07-agent-interaction-bridge-cold-start.md` explicitly states "first do cold start only, do not modify files." `partner/pilots/2026-06-07-agent-interaction-bridge-presentation-rendering-checkpoint.md` ends with "wait for user confirmation before making target repo code changes." `partner/pilots/2026-06-07-online-community-manual-acceptance-plan.md` states "wait for a real internal discussion transcript."

Implication: alphaX has proven it can understand projects and identify risks. It has not yet proven it can make correct changes in real projects.

### R6: Workspace Staleness Not Tracked (P1)

The focus radar tracks staleness of external projects (dirty WIP, stale branches, false completion) but does not track staleness of the workspace itself. When alphaX re-enters after several days with an outdated focus radar, the workspace's own staleness becomes a new risk source.

Evidence: `partner/focus-radar.md` lists risks for `agent-interaction-bridge`, `online_community`, and `clouds-beyond`, but the row for `/Users/lizhaohua/Desktop/codex` only mentions scaffolding creep and proactive push intrusion. There is no entry for "focus radar itself is N days stale."

Implication: The workspace is both alphaX's operating system and alphaX's product. As an OS it needs stability; as a product it needs evolution. When the OS itself goes stale, the agent may make decisions from outdated portfolio state.

## Structural Observation: The OS/Product Tension

The workspace occupies two roles simultaneously:

- **Operating system**: must be stable and predictable enough for each session to reliably reconstruct context, classify loops, and produce evidence.
- **Product**: must evolve based on usage feedback—loops added or removed, templates adjusted, boundaries redrawn.

These roles have not yet conflicted because all usage occurred on the same day. Cross-day reuse will surface this tension: when alphaX re-enters with a 3-day-old focus radar against projects that have changed shape, the OS's own staleness becomes a risk that the current radar does not track.

This is not a bug to fix now. It is a structural property to watch for.

## Recommendation

The single most important next action is **cross-day reuse**. Not a new loop, template, or decision. At the next session:

1. alphaX cold-starts from the handoff state block.
2. Re-enters `agent-interaction-bridge` and inspects the dirty WIP on `codex/extract-runtime-services`.
3. Determines WIP ownership and intent.
4. Either makes a real code change under contract boundary protection, or explicitly defers with a recorded reason.

This session will directly verify or falsify the core claim: "alphaX lowers project re-entry cost."

If cross-day reuse fails (alphaX cannot recover sufficient context from the handoff block, or misjudges WIP ownership), the handoff block format or Agent Intake Rule needs improvement.

If cross-day reuse succeeds, the next gate is: move from read-only to write mode, making a real project change with contract boundary protection.

## Boundary

- This agent does not claim ongoing presence, authority, or a role in the workspace.
- This contribution is a trace, not a role. It follows the same Agent Intake Rule it recommends.
- All claims above that are not backed by file paths, line counts, or command output are marked as unverified observations.
- The agent's earlier conversational review contained the same substance; this packet makes it durable and inspectable.

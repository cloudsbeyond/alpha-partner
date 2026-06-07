# Focus Radar

Updated: 2026-06-07

This radar is the current alphaX re-entry view for parallel project work. Keep it compact. Its job is to reduce context reload cost, expose missed risk, and recommend one next work block.

## Portfolio P0

alphaX should help Lizhaohua recover project context, detect risk, and choose the next focus move across parallel AI product and engineering explorations.

## Current Recommendation

Daily radar outcome: the main live risk is no longer partner-workspace scaffolding; it is stale context around dirty project WIP.

Choose one:

- Highest risk control: run a read-only `agent-interaction-bridge` WIP review before any implementation in that repo.
- Low re-entry cost: run the prepared `online_community` manual acceptance plan outside git.
- Automation experiment: run `alphaX nudge check` only inside the current session; do not schedule it yet.

## Project Radar

| Surface | P0 | Current State | Top Risk | Focus Move |
| --- | --- | --- | --- | --- |
| `/Users/lizhaohua/Desktop/codex` | Keep alphaX usable as a human-agent peer workspace. | Markdown-first workspace; first manual daily radar run recorded in `partner/loop-reports/2026-06-07-daily-radar.md`. | [P2] Scaffolding creep if loop reports multiply without driving real project decisions; [P1] proactive push can become intrusive without explicit source and cooldown boundaries. | Use the daily radar result to protect current project WIP; do not add scheduled automation yet. |
| `/Users/lizhaohua/work/llm/agent-interaction-bridge` | Build a bounded interaction agent with clean Product Runtime and Build-Time Governance boundaries. | Live branch `codex/extract-runtime-services`; dirty WIP includes `AGENTS.md`, `package.json`, `pnpm-lock.yaml`, `src/signal/delivery-support*.ts`, new `src/runtime/runtime-services-adapter*.ts`, and `src/signal/delivery-support-runtime-services.test.ts`. | [P1] Stale context: prior radar only described pointer drift; [P1] ownership risk if alphaX edits over user or other-agent WIP; [P1] test state not verified for current WIP. | Run read-only WIP review before any implementation, then decide whether alphaX should take over, preserve, or leave it. |
| `/Users/lizhaohua/work/llm/clouds-beyond/online_community` | Turn Work Buddy prototype into reusable Session Runtime with evidence refs, draft confirmation, routing, and manual acceptance. | Live branch `codex/session-runtime-acceptance-report`; working tree clean; manual acceptance plan prepared in `partner/pilots/2026-06-07-online-community-manual-acceptance-plan.md`; root partner pointer not present. | [P1] False completion: automated checks prove structure and privacy, not real discussion usefulness. | Use one real transcript outside git, run the prepared plan, and record only a non-sensitive summary. |
| `/Users/lizhaohua/work/llm/clouds-beyond` | Govern CloudsBeyond root as current-state source index and project boundary map. | Live branch `codex/changelog-may-compression`; working tree clean; root partner pointer not present. | [P3] Lower urgency unless root changelog, architecture convergence, or subproject boundary drift reappears. | Keep parked unless a root governance task blocks a subproject. |

## Cross-Project Risks

- [P1] False completion: passing tests can hide missing human acceptance.
- [P1] Wrong-layer work: downstream implementation may patch upstream semantic gaps.
- [P1] WIP ownership drift: a dirty repo can include user work, other-agent work, or old alphaX work; do not overwrite without review.
- [P2] Attention loss: uncommitted local instructions or branch-specific context can be forgotten when switching projects.
- [P2] Over-scope: future useful agent/product ideas can steal current P0 focus.
- [P3] Stale memory: prior pilot branch names may differ from live branch state.

## Parking Lot

- Promote alphaX or `problem-decomposer` into a global Codex Skill.
- Add project-local pointers to repos that have not repeated alphaX use.
- Expand portfolio tracking into a full app, MCP server, or dashboard.
- External research refresh unless it directly changes a current project decision.
- Schedule hosted routines before manual loop value is proven.
- Cross-app proactive observation before local permission boundaries are explicit.

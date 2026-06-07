# Focus Radar

Updated: 2026-06-08

Compact re-entry view for parallel project work. Reduces context reload cost, exposes missed risk, recommends one next work block.

## Portfolio P0

alphaX helps Lizhaohua recover project context, detect risk, and choose the next focus move across parallel AI product and engineering explorations.

## Current Recommendation

The single most important next test is **cross-day reuse**. All applied sessions are from 2026-06-07; the core claim "alphaX lowers project re-entry cost" is unverified.

- **Highest priority**: at next cross-day session, cold-start from handoff block, re-enter `agent-interaction-bridge`, inspect dirty WIP on `codex/extract-runtime-services`, determine ownership, make a real code change or explicitly defer.
- **Highest risk control (same-day)**: read-only `agent-interaction-bridge` WIP review before any implementation.
- **Low re-entry cost**: run prepared `online_community` manual acceptance plan outside git.
- **Do not**: add new loops, templates, or process layers until cross-day reuse proves or disproves the core claim.

## Project Radar

| Surface | P0 | Current State | Top Risk | Focus Move |
| --- | --- | --- | --- | --- |
| `/Users/lizhaohua/Desktop/codex` | Keep alphaX usable as a human-agent peer workspace. | Markdown-first workspace; daily radar and external peer review recorded in `partner/loop-reports/`. | [P1] Workspace staleness: focus radar itself goes stale across days, not tracked by any loop. [P2] Scaffolding creep if loop reports multiply without driving real decisions. | Cross-day reuse is the single most important next test. |
| `/Users/lizhaohua/work/llm/agent-interaction-bridge` | Build a bounded interaction agent with clean Product Runtime and Build-Time Governance boundaries. | Live branch `codex/extract-runtime-services`; dirty WIP includes `AGENTS.md`, `package.json`, `pnpm-lock.yaml`, `src/signal/delivery-support*.ts`, new `src/runtime/runtime-services-adapter*.ts`. | [P1] Stale context and ownership risk: dirty WIP may be user work, other-agent work, or old alphaX work. | Run read-only WIP review before any implementation. |
| `/Users/lizhaohua/work/llm/clouds-beyond/online_community` | Turn Work Buddy prototype into reusable Session Runtime. | Live branch `codex/session-runtime-acceptance-report`; working tree clean; manual acceptance plan prepared. | [P1] False completion: automated checks prove structure and privacy, not real discussion usefulness. | Run manual acceptance on one real transcript outside git. |
| `/Users/lizhaohua/work/llm/clouds-beyond` | Govern CloudsBeyond root as current-state source index. | Live branch `codex/changelog-may-compression`; working tree clean. | [P3] Lower urgency unless root governance blocks a subproject. | Keep parked. |

## Cross-Project Risks

- [P0] Same-day evidence: all applied sessions are from 2026-06-07; review-agent meta sessions extend to 2026-06-08 but no true cross-day reuse of applied work.
- [P1] False completion: passing tests can hide missing human acceptance.
- [P1] Wrong-layer work: downstream implementation may patch upstream semantic gaps.
- [P1] WIP ownership drift: dirty repos may include user, other-agent, or old alphaX work.
- [P1] Workspace staleness: focus radar itself goes stale across days; no tracking mechanism.
- [P2] Scaffolding-to-use ratio: 7 loops defined, 2 exercised; 7 packet templates, 3 visibly used.
- [P2] Attention loss: uncommitted local context can be forgotten when switching projects.
- [P2] Over-scope: future-useful agent/product ideas can steal current P0 focus.

## Parking Lot

- Promote alphaX or `problem-decomposer` into a global Codex Skill.
- Add project-local pointers to repos without repeated alphaX use.
- Expand portfolio tracking into a full app, MCP server, or dashboard.
- External research refresh unless it directly changes a current project decision.
- Schedule hosted routines before manual loop value is proven.
- Cross-app proactive observation before local permission boundaries are explicit.

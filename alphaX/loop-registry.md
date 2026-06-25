# Loop Registry

Adapts Boris-style Loop thinking to alphaX. Principle: **loops protect attention; they do not replace judgment**.

## Current Boundary

Current loops are manual-trigger and read-only by default. Do not schedule recurring tasks, create hosted routines, watch private systems, modify repos, post externally, or run destructive operations without explicit user approval.

## Source Inspiration

Claude Code `/loop` (local scheduled prompts), Claude Code Routines (hosted scheduled/API/GitHub automations), Boris-style workflow (background agents produce reports, human consumes summaries). alphaX: prefer loops over sub-agent fanout; prefer report-first before execution; keep project source of truth visible; upgrade from manual to scheduled only after proven useful and safe.

## Observation Boundary

alphaX may infer useful timing from local context during active session: project state, recent diffs, failing checks, stale ledger entries, unresolved decisions, repeated user interruptions, explicit user-provided work surfaces. Must not silently collect cross-app private data, scrape centralized super apps, process private chats, or create background watchers without approval.

## Loop 1: Daily Focus Radar

Trigger: `alphaX daily radar`. Purpose: refresh or produce a focus/risk view; identify best next work block; expose stale branch, uncommitted state, false completion, wrong-layer work. Inputs: optional local `.alphaX/process/focus-radar.md`, optional `.alphaX/process/session-ledger.md`, context-snapshot output for active projects, project-local AGENTS.md/README/specs/contracts, and project-local `.alphaX/` objective data when present. Output: compact focus/risk report. Default: read files, run read-only status commands, recommend one next focus move. Requires approval: writing project files, scheduling, publishing/messaging reports.

## Loop 2: Source Drift Watch

Trigger: `alphaX source drift check`. Purpose: lightweight entry for the shared
risk scan vocabulary in `alphaX/operating-system.md`, focused on
source-of-truth drift. Default: read-only report. If scoped to one target
project, use `alphaX/project-review/README.md`; if scoped to alphaX source
itself, use `alphaX/source-review/README.md`.

## Loop 3: False Completion Watch

Trigger: `alphaX false completion check`. Purpose: lightweight entry for the
shared risk scan vocabulary in `alphaX/operating-system.md`, focused on false
completion. Default: read-only report that separates proven claims, missing
evidence, and needed acceptance. If scoped to one project, use
`alphaX/project-review/README.md`; if scoped to alphaX source itself, use
`alphaX/source-review/README.md`.

## Loop 4: PR/CI Watch

Trigger: `alphaX PR CI watch`. Purpose: watch a specific repo or PR for failing CI, stale branch state, flaky tests, rebase needs. Inputs: explicit repo/PR URL, permission boundary, allowed actions. Default: read status only; summarize failures and probable owner boundary. Requires approval: pushing commits, rebasing, modifying CI, commenting on PRs.

## Loop 5: Research Intake

Trigger: `alphaX research intake`. Purpose: periodically map external alphaX collaboration, agent-native product, context, memory, tool harness, governance, and evaluation signals back to current projects. Default sources: official docs, papers, engineering blogs, primary product docs. Output: mechanism, local implication, project candidate, evidence link. Default: update `docs/research-backlog.md` or `docs/evidence-index.md` only after user asks for source write; otherwise produce candidate note.

## Loop 6: Proactive Nudge Experiment

Trigger: `alphaX nudge check`. Purpose: infer whether alphaX should proactively push a low-intrusion reminder, risk note, or focus suggestion. Allowed current signals: unresolved high-risk decisions in local process data, uncommitted or stale project-local objective data, prior local ledger next action with no follow-through, automated checks passed but manual acceptance missing, user explicitly says attention/focus/risk is degraded. Output: compact candidate nudge with evidence, reason, urgency, recommended channel. Default: produce inside current session; do not create recurring automation or push notification. Requires approval: Codex heartbeat/cron, Slack/Feishu/email/app notification, cross-app data access, private chat/meeting transcript processing.

## Loop 7: alphaX Self-Critique

Trigger: `alphaX self-critique`. Purpose: institutionalize the dissenter role so it is a mechanism, not an accident of whoever is in the conversation. Have an agent with clean context read alphaX itself and hunt for internally consistent but never-verified claims. Allowed signals: contract claims with no evidence trace; local process-data claims with no evidence trace; value claims still treated as proven without cross-day/cross-machine test; run of `meta` ledger entries with no `applied`; contract rules no `applied` session has reported using. Output: compact critique list—each item names suspect claim, why unverified, cheapest evidence to confirm/falsify. Explicitly separate "proven by diff" from "asserted", applying Agent Intake Rule to alphaX's own files. Default: read-only; produce critique inside current session; do not edit contract or delete rules without user approval.

## Upgrade Gate

Before any loop becomes scheduled, hosted, or proactively pushed outside current session: proven manual-trigger value; explicit scope and source list; read/write boundary; allowed observation signals; failure and stop condition; reporting destination; interruption budget and cooldown; cost and privacy review; human approval for the schedule.

## Parking Lot

Hundreds of background agents. Hosted routines. Slack/Feishu report posting. Automatic PR repair. Autonomous rebase/merge. Private transcript processing on a schedule. Cross-app behavior learning without explicit local permission boundary.

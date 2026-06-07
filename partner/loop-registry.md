# Loop Registry

This registry adapts Boris-style Loop thinking to alphaX.

The principle: **loops protect attention; they do not replace judgment**.

## v0.1 Boundary

Current loops are manual-trigger and read-only by default.

Do not schedule recurring tasks, create hosted routines, watch private systems, modify repos, post externally, or run destructive operations from this registry without explicit user approval.

## Source Inspiration

- Claude Code `/loop`: local scheduled prompts in an open session.
- Claude Code Routines: hosted scheduled, API, and GitHub-event automations.
- Boris-style workflow: many background agents produce reports while the human consumes summaries and makes key decisions.

alphaX adoption:

- prefer loops over sub-agent fanout for attention recovery;
- prefer report-first loops before execution loops;
- keep project source of truth and risk boundaries visible;
- upgrade from manual to scheduled only after a loop proves useful and safe.

## Observation Boundary

alphaX may infer useful timing from available local context during an active session: project state, recent diffs, failing checks, stale ledger entries, unresolved decisions, repeated user interruptions, and explicit user-provided work surfaces.

alphaX must not silently collect cross-app private data, scrape centralized super apps, process private chats, or create background watchers without approval.

For the long-term product question, treat端侧 agent data permission recovery as a research hypothesis: the user grants local context access, the agent explains the signal, and the human retains action authority.

## Loop 1: Daily Focus Radar

Trigger:

```text
alphaX daily radar
```

Purpose:

- refresh `partner/focus-radar.md`;
- identify the one best next work block;
- expose stale branch, uncommitted state, false completion, and wrong-layer work.

Inputs:

- `partner/focus-radar.md`;
- `partner/session-ledger.md`;
- live `scripts/context-snapshot.sh` output for active projects;
- relevant project-local `AGENTS.md`, README, specs, contracts, and changelog.

Output:

- update or produce a compact focus/risk report.

Default actions:

- read files;
- run read-only status commands;
- recommend one next focus move.

Requires approval:

- writing target project files;
- scheduling recurring execution;
- publishing or messaging reports.

## Loop 2: Source Drift Watch

Trigger:

```text
alphaX source drift check
```

Purpose:

- detect disagreement between spec, contract, implementation, tests, and evidence.

Candidate surfaces:

- `agent-interaction-bridge` architecture contracts and AI Contract Index;
- `online_community` Session Runtime spec, schema snapshot, backend tests, and guardrail cases.

Output:

- source-of-truth drift report with evidence and one recommended repair path.

Default actions:

- run project-local contract checks and test commands when safe;
- do not edit files unless the user explicitly asks for repair.

## Loop 3: False Completion Watch

Trigger:

```text
alphaX false completion check
```

Purpose:

- catch cases where tests pass but product acceptance, manual review, or human confirmation is incomplete.

Candidate surfaces:

- `online_community` manual acceptance;
- `agent-interaction-bridge` partial contract gaps;
- generated artifacts with harness evidence but missing human acceptance.

Output:

- list of claims that are proven, not proven, or blocked by missing acceptance.

Default actions:

- compare test results against acceptance criteria;
- mark missing evidence explicitly.

## Loop 4: PR/CI Watch

Trigger:

```text
alphaX PR CI watch
```

Purpose:

- watch a specific repo or PR for failing CI, stale branch state, flaky tests, or rebase needs.

Inputs needed:

- explicit repo or PR URL;
- permission boundary;
- allowed actions.

Default actions:

- read status only;
- summarize failures and probable owner boundary.

Requires approval:

- pushing commits;
- rebasing;
- modifying CI;
- commenting on PRs.

## Loop 5: Research Intake

Trigger:

```text
alphaX research intake
```

Purpose:

- periodically map external human-agent peer, agent-native product, context, memory, tool harness, governance, and evaluation signals back to current projects.

Default sources:

- official docs;
- papers;
- engineering blogs;
- primary product docs.

Output:

- mechanism, local implication, project candidate, and evidence link.

Default actions:

- update `research-backlog.md` or `evidence-index.md` only after user asks for local write;
- otherwise produce a candidate note.

## Loop 6: Proactive Nudge Experiment

Trigger:

```text
alphaX nudge check
```

Purpose:

- infer whether alphaX should proactively push a low-intrusion reminder, risk note, or focus suggestion.

Allowed signals in v0.1:

- a project has unresolved high-risk decisions in `focus-radar.md`;
- a branch has uncommitted or stale local context that can be forgotten;
- a prior ledger entry names a next action with no follow-through evidence;
- automated checks passed but manual acceptance is still missing;
- the user explicitly says attention, focus, or risk is degraded.

Output:

- a compact candidate nudge with evidence, reason, urgency, and recommended channel.

Default actions:

- produce the candidate nudge inside the current session;
- do not create a recurring automation or push notification.

Requires approval:

- Codex heartbeat or cron automation;
- Slack, Feishu, email, or app notification;
- cross-app data access;
- private chat or meeting transcript processing.

## Loop 7: alphaX Self-Critique

Trigger:

```text
alphaX self-critique
```

Purpose:

- institutionalize the dissenter role so it is a mechanism, not an accident of whoever happens to be in the conversation.
- have an agent with a clean context read alphaX itself and hunt for claims that are internally consistent but never verified.

Why it exists:

- both the user and the runtime tend to like this project; when both sides are satisfied, no one naturally pushes back.
- the value of a reviewer is in challenge, not acceptance; this loop supplies challenge on demand.

Allowed signals:

- decision-log or contract claims asserted with no evidence trace, command, file, or line number;
- value claims ("lowers re-entry cost", "Codex is only the body") still labeled or implicitly treated as proven without a real cross-day or cross-machine test;
- a run of `meta` ledger entries with no `applied` entry, signaling method-maintenance drift;
- contract rules that no `applied` session has ever reported using.

Output:

- a compact critique list: each item names the suspect claim, why it is unverified, and the cheapest evidence that would confirm or falsify it.
- explicitly separate "proven by diff" from "asserted", applying the Agent Intake Rule to alphaX's own files.

Default actions:

- read-only; produce the critique inside the current session;
- do not edit the contract or delete rules without explicit user approval.

Requires approval:

- any deletion of a contract rule the critique flags as unused;
- promotion to a scheduled or automated self-audit.

## Upgrade Gate

Before any loop becomes scheduled, hosted, or proactively pushed outside the current session, require:

- proven manual-trigger value;
- explicit scope and source list;
- read/write boundary;
- allowed observation signals;
- failure and stop condition;
- reporting destination;
- interruption budget and cooldown;
- cost and privacy review;
- human approval for the schedule.

## Parking Lot

- Hundreds of background agents.
- Hosted routines.
- Slack or Feishu report posting.
- Automatic PR repair.
- Autonomous rebase or merge.
- Private transcript processing on a schedule.
- Cross-app behavior learning without an explicit local permission boundary.

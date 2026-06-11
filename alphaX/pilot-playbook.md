# Pilot Playbook

Use this playbook to test whether alphaX improves real project R&D and thinking exploration.

## Pilot Purpose

A pilot is a real project session that uses Alpha Partner Source by reference, works from project source of truth, and leaves evidence of whether the collaboration mode helped.

The pilot is not a demo. It should test at least one of:

- sharper P0 problem definition;
- better product or architecture judgment;
- clearer L0-L4 boundary;
- stronger verification path;
- better external calibration;
- reusable reflection or memory candidate.

## Candidate Projects

Prefer projects with a clear source of truth, an active decision or artifact,
and enough validation surface to judge whether alphaX helped. If this checkout
has a local pilot queue, keep it under ignored `.alphaX/local/`.

## Pilot Start Prompt

Use this from the target project or conversation:

```text
Please use the Alpha Partner working mode for this project:
- Alpha Partner Source: `{alpha-partner}/AGENTS.md`
- Current project path/link: <project path or source link>
- Current source of truth: <specific docs, contracts, README, AGENTS, issue, or PR>
- Current goal: <one concrete project or thinking outcome>

First do a cold start: read the partner contract, then read the project source
of truth, and report the P0 main line, current loop classification, evidence to
inspect, and next execution path.
```

## Pilot Flow

1. Cold start from `AGENTS.md`, `alphaX/session-runbook.md`, and project-local instructions.
2. Classify the primary loop: research, project, thinking, or memory.
3. Fill or adapt one packet from `templates/` when the work needs a durable trace.
4. Do the real work against project source of truth.
5. Run project-level verification when the task changes files or claims completion.
6. Run `bash {alpha-partner}/scripts/verify-alpha-source.sh` only if Alpha Partner Source changed.
7. If this is a Source Evolution pilot and a local ledger exists, add one entry to this checkout's ignored `.alphaX/process/session-ledger.md` when the pilot ends.

## Success Evidence

A pilot counts as useful only if at least one is true:

- It changed a concrete project artifact.
- It clarified a decision with stronger evidence.
- It prevented over-scope or wrong-layer implementation.
- It produced a reusable packet, decision, or memory candidate.
- It improved verification or source traceability.

## Failure Evidence

Record the pilot as weak if:

- It only produced generic advice.
- It could not identify project source of truth.
- It acted like a ticket executor without peer-level framing.
- It added process without improving a project decision or artifact.
- It relied on memory or external trend claims without current evidence.

## Review Cadence

After three local pilot entries, review `.alphaX/process/session-ledger.md` and decide:

- keep Alpha Partner Source as Markdown;
- adjust persona or runbook;
- add project-local pointers;
- promote stable parts into a Codex Skill;
- defer deeper engineering.

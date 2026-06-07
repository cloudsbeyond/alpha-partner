# Pilot Playbook

Use this playbook to test whether Alpha Partner improves real project R&D and thinking exploration.

## Pilot Purpose

A pilot is a real Level 2 project session that uses the partner workspace by reference, works from project source of truth, and leaves evidence of whether the collaboration mode helped.

The pilot is not a demo. It should test at least one of:

- sharper P0 problem definition;
- better product or architecture judgment;
- clearer L0-L4 boundary;
- stronger verification path;
- better external calibration;
- reusable reflection or memory candidate.

## Candidate Projects

Prefer projects already represented in `project-map.md`:

- Agent 化组织;
- L0-L4 需求到交付链路;
- Agent 知识治理闭环;
- this partner workspace itself.

Use a different project only if it has a clear source of truth and a concrete current decision or artifact.

## Pilot Start Prompt

Use this from the target project or conversation:

```text
这个项目请启用 Alpha Partner 工作方式：
- partner workspace: `{alpha-partner}/AGENTS.md`
- 当前项目路径/链接：<project path or source link>
- 当前 source of truth：<specific docs, contracts, README, AGENTS, issue, or PR>
- 当前目标：<one concrete project or thinking outcome>

请先做 cold start：读取 partner contract，再读取项目内 source of truth，给出 P0 主链路、本轮 loop 分类、需要检查的证据和下一步推进方式。
```

## Pilot Flow

1. Cold start from `AGENTS.md`, `session-runbook.md`, and project-local instructions.
2. Classify the primary loop: research, project, thinking, or memory.
3. Fill or adapt one packet from `partner/templates/` when the work needs a durable trace.
4. Do the real work against project source of truth.
5. Run project-level verification when the task changes files or claims completion.
6. Run `bash {alpha-partner}/scripts/verify-partner-workspace.sh` only if the partner workspace changed.
7. Add one entry to `partner/session-ledger.md` when the pilot ends.

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

After three pilot entries, review `session-ledger.md` and decide:

- keep the workspace as Markdown;
- adjust persona or runbook;
- add project-local pointers;
- promote stable parts into a Codex Skill;
- defer deeper engineering.

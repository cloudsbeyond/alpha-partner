# Target Project Review Mode

Target Project Review Mode is the alphaX review surface for a concrete target
project. It is separate from the `{alpha-partner}` review-agent mechanism.

The `{alpha-partner}` review agent reviews alphaX source and local alphaX
process data. Target Project Review Mode reviews a target project's stated
goals, source of truth, changed files, validation evidence, and local
`.alphaX/` objective data when present.

## Role

Use this mode to check whether target-project work is supported by current
evidence before a handoff, merge, release, or claimed completion.

It may:

- read target-project instructions, source files, specs, tests, build output,
  issue notes, changelog entries, git status, commits, and diffs;
- read the target project's ignored `.alphaX/` objective data when present;
- compare claimed behavior with implementation and validation evidence;
- identify source drift, missing evidence, false completion, and risk;
- produce a report-first review for the user.

It must not:

- mutate `{alpha-partner}` source or this checkout's `.alphaX/process/` while
  reviewing an external target project;
- replace the target project's source of truth, spec, ADR, changelog, or
  approval flow;
- act as a hidden supervisor over multiple projects;
- implement fixes unless the user explicitly switches from review to execution;
- store secrets, private transcripts, raw hidden model chain-of-thought, or
  broad alphaX governance judgment inside the target project.

## Trigger Contract

Explicit triggers:

- `alphaX review this target project.`
- `Run target project review mode.`
- `Review whether the claimed work is actually implemented.`
- `Check this before handoff, merge, or release.`
- Chinese equivalents such as `启用目标项目 review mode`,
  `审一下这个项目交付是否真的完成`, or `合入前帮我做一次证据复查`.

Suggested triggers:

- after a nontrivial implementation before the final answer or handoff;
- after a context reload finds stale `.alphaX/` data, source drift, or missing
  validation evidence;
- before merging, publishing, or telling another agent that a project is ready;
- when two target-project files, schemas, specs, or claims disagree;
- when the user asks about false completion, missed risk, or whether stated
  functionality exists.

Non-triggers:

- alphaX source governance review stays in `alphaX/review-agent-mechanism.md`;
- portfolio or attention review stays in the Focus And Risk Loop unless it is
  narrowed to one concrete target project;
- vendor research, runtime design, and cross-project automation stay out of P0
  unless they directly affect the current review.

If the active working directory is `{alpha-partner}` and the user is asking
about an external project, classify the run as External Assistance Mode and ask
before writing to `{alpha-partner}`.

## Asset And Data Boundary

Shareable function assets live in `{alpha-partner}`:

- `alphaX/target-project-review-mode.md`;
- `templates/target-project-review-report.md`;
- generic trigger, boundary, and verifier rules.

Target-project data lives with the target project:

- versioned project source, specs, tests, and validation scripts;
- ignored target-project `.alphaX/project-context.md`;
- ignored target-project `.alphaX/reports/` review reports when a durable local
  report is useful;
- evidence pointers to commands, commits, files, or external artifacts.

Default output is the conversation report. If persistence is useful and allowed,
write only non-sensitive review summaries to the target project's ignored
`.alphaX/reports/` or refresh the target project's ignored
`.alphaX/project-context.md`. Do not write external project review data into
this checkout's `.alphaX/process/`.

Versioned target-project files may be edited only when the user asks to change
that target project. Target-project review alone is report-first.

## Review Procedure

1. Classify the run as External Assistance Mode unless the user is changing
   Alpha Partner Source itself.
2. Identify the target project root, branch, working tree status, and relevant
   instruction files.
3. Read target-project source of truth: `AGENTS.md`, README, specs, contracts,
   schemas, tests, changelog, issue notes, and current diff as applicable.
4. Read target-project `.alphaX/` objective data when present, treating it as
   context rather than source of truth.
5. List the claims being reviewed: requested behavior, claimed completion,
   handoff assertions, or release criteria.
6. Map each claim to evidence: files, tests, commands, build output, screenshots,
   logs, or explicit missing evidence.
7. Run the smallest safe validation commands needed to support the review.
8. Produce a target-project review report using
   `templates/target-project-review-report.md`.

## Expected Output

Use direct findings first:

1. verdict: ready, blocked, risky, or insufficient evidence;
2. findings ordered by severity with file, command, or artifact evidence;
3. drift markers between claims, source, tests, specs, and `.alphaX/` data;
4. missing evidence and `unverified_claims`;
5. next action: fix, validate, defer, or ask the user for a decision.

Keep the output scoped to the target project. Do not use target-project review
as a reason to change alphaX source unless the user explicitly starts Source
Evolution Mode.

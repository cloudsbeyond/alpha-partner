# Project Review

`project review` is the alphaX review scope for one concrete project. It is
separate from `source review`.

`source review` reviews Alpha Partner Source and local alphaX process data.
`project review` reviews a project's stated goals, source of truth, changed
files, validation evidence, and local
`.alphaX/` objective data when present.

## Role

Use this scope to check whether project work is supported by current
evidence before a handoff, merge, release, or claimed completion.

It may:

- read project instructions, source files, specs, tests, build output,
  issue notes, changelog entries, git status, commits, and diffs;
- read the project's ignored `.alphaX/` objective data when present;
- compare claimed behavior with implementation and validation evidence;
- review project lifecycle hygiene when the claim concerns PR/merge,
  handoff, freeze, release, publication, open-source readiness, or stale/noisy
  project `.alphaX/` evidence;
- identify risks using the shared risk scan vocabulary in
  `alphaX/operating-system.md`, including source-of-truth drift, false
  completion, and missing evidence;
- produce a report-first review for the user.

It must not:

- mutate `{alpha-partner}` tracked source while reviewing an external project;
- write to this checkout's `.alphaX/process/` except for a sanitized
  review-feedback note about alphaX mechanisms when the checkout is available;
- replace the project's source of truth, spec, ADR, changelog, or
  approval flow;
- act as a hidden supervisor over multiple projects;
- implement fixes unless the user explicitly switches from review to execution;
- store secrets, private transcripts, raw hidden model chain-of-thought, or
  broad alphaX governance judgment inside the project.

## Trigger Contract

Explicit triggers:

- `alphaX run project review.`
- `Run project review before handoff.`
- `Review whether the claimed work is actually implemented.`
- `Check this before handoff, merge, or release.`
- Chinese equivalents such as `启用 project review`,
  `审一下这个项目交付是否真的完成`, or `合入前帮我做一次证据复查`.

Suggested triggers:

- after a nontrivial implementation before the final answer or handoff;
- after a context reload finds stale `.alphaX/` data, source drift, or missing
  validation evidence;
- before merging, publishing, or telling another agent that a project is ready;
- when project `.alphaX/` has not been rewritten since a freeze/handoff/release
  signal, or its rough file size or line count makes current state hard to see;
- when two project files, schemas, specs, or claims disagree;
- when the user asks about false completion, missed risk, or whether stated
  functionality exists.

Non-triggers:

- alphaX source governance review stays in `alphaX/source-review/README.md`;
- portfolio or attention review stays in the Focus And Risk Loop unless it is
  narrowed to one concrete project;
- vendor research, runtime design, and cross-project automation stay out of P0
  unless they directly affect the current review.

If the active working directory is `{alpha-partner}` and the user is asking
about an external project, classify the run as `project review` and ask
before writing to `{alpha-partner}`.

## Asset And Data Boundary

Shareable function assets live in `{alpha-partner}`:

- `alphaX/project-review/README.md`;
- `templates/project-review/report.md`;
- generic trigger, boundary, and verifier rules.

Project data lives with the project:

- versioned project source, specs, tests, and validation scripts;
- ignored project `.alphaX/project-context.md`;
- ignored project `.alphaX/reports/` review reports when a durable local
  report is useful;
- evidence pointers to commands, commits, files, or external artifacts.

Default output is the conversation report. If persistence is useful and allowed,
write only non-sensitive review summaries to the project's ignored
`.alphaX/reports/` or refresh the project's ignored
`.alphaX/project-context.md`. Do not write external project review data into
this checkout's `.alphaX/process/`.

Versioned project files may be edited only when the user asks to change that
project. `project review` alone is report-first.

## Lifecycle Hygiene Checks

Run lifecycle hygiene automatically when the project claim is a PR/merge,
handoff, freeze, release, publication, or open-source readiness claim. Also run
it when project `.alphaX/` evidence affects the review and appears stale or noisy
by rewrite recency, rough file size, line count, repeated phase logs, or
conflicting current-state pointers. Include the smallest relevant subset of
these checks:

- tracked source state: branch, working tree, staged files, ignored local data,
  generated output, and private-path scan;
- evidence state: validation commands, test output, build output, screenshots,
  external artifact checks, or explicit acceptance notes;
- public/release state: remote URL, visibility, default branch, commit count or
  commit shape, tags when relevant, repository description/topics, README
  posture, license posture, and public metadata;
- history posture: whether local development history is intentionally preserved,
  squashed, tagged, archived, or not published;
- project `.alphaX/` posture: whether ignored local objective data is compact
  enough for re-entry, whether append-only logs should be rewritten after a
  freeze, whether unfrozen evidence and open decisions are preserved, and
  whether public source contains no target `.alphaX/` data.

For project `.alphaX` compaction, recommend an AOF-style rewrite, or
perform it only after explicit user approval: preserve the current baseline,
durable decisions, evidence pointers, unfrozen evidence, open decisions, and
next actions; archive or summarize step-by-step command transcripts unless a
concrete regression or audit requires retaining them. Compaction is not
source-of-truth migration: live project source still wins over stale
local `.alphaX` data.

## Completion State Vocabulary

Use these fields instead of a single broad "done" label:

- implementation_state: `<not-found|partial|implemented|not-reviewed>`;
- validation_state: `<not-run|failed|partial|passed|not-applicable>`;
- integration_state: `<local-only|branch-only|merged|released|not-reviewed>`;
- completion_call:
  `<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence>`.

Use the narrowest completion call supported by the reviewed evidence. When the
fields conflict, report the conflict instead of averaging it into a positive
status.

## Review Procedure

1. Classify the run as `project review` unless the user is changing Alpha
   Partner Source itself.
2. Identify the project root, branch, working tree status, and relevant
   instruction files.
3. Read project source of truth: `AGENTS.md`, README, specs, contracts,
   schemas, tests, changelog, issue notes, and current diff as applicable.
4. Read project `.alphaX/` objective data when present, treating it as
   context rather than source of truth.
5. List the claims being reviewed: requested behavior, claimed completion,
   handoff assertions, or release criteria.
6. Map each claim to evidence: files, tests, commands, build output, screenshots,
   logs, or explicit missing evidence.
7. Run the smallest safe validation commands needed to support the review.
8. Produce a project review report using
   `templates/project-review/report.md`.

If the review finds that project `.alphaX/` has become append-only noise,
recommend compaction rather than copying its contents into tracked source.

## Expected Output

Use direct findings first:

1. completion state: implementation, validation, integration, and completion
   call;
2. findings ordered by severity with file, command, or artifact evidence;
3. drift markers between claims, source, tests, specs, and `.alphaX/` data;
4. missing evidence and `unverified_claims`;
5. lifecycle hygiene gaps and compaction signals;
6. next action: fix, validate, compact, defer, or ask the user for a decision;
7. optional review-feedback backwrite for alphaX mechanism learning, using
   `templates/source-review/feedback-report.md`.

Keep the output scoped to the project. Do not use project review as a reason to
change alphaX source unless the user explicitly switches to `source work`.

If review feedback is written back to alpha-partner, keep it mechanism-level:
what helped, what got in the way, unused mechanisms and defensive reasons,
candidate source iteration, evidence pointers, confidence, and unverified
claims. Do not copy project facts, raw logs, private paths, secrets,
transcripts, or broad governance conclusions.

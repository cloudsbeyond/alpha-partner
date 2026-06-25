# Local alphaX Data Schema

This document defines the ignored `.alphaX/` data shape for a local checkout of
Alpha Partner Source.

The GitHub-tracked tree contains the reusable alphaX function source. The local
`.alphaX/` tree contains machine-local and person-local data. Different users
and machines will have different `.alphaX/` contents. That is expected.

Consistency comes from the schema, not from identical data.

## Required Shape

```text
.alphaX/
  manifest.yaml
  local/
    README.md
    agent-runtime-services.json
    project-paths.md
    project-meta-index.yaml
    pilot-candidates.md
    private-patterns.txt
  process/
    README.md
    decision-log.md
    focus-radar.md
    session-ledger.md
    source-review-backlog.md
    loop-reports/
    pilots/
    review-feedback/
    source-work-candidates/
```

Minimum shape required by `scripts/verify-local-alphaX.sh`: `manifest.yaml`,
`local/README.md`, `process/README.md`, `process/loop-reports/`, and
`process/pilots/`, `process/review-feedback/`, and
`process/source-work-candidates/`. The other files shown above are
recommended defaults created by `scripts/init-local-alphaX.sh`.

## Manifest

`.alphaX/manifest.yaml` is the local schema anchor.

```yaml
schema_version: 1
owner: local
kind: alphaX_local_data
created_by: scripts/init-local-alphaX.sh
source_contract: AGENTS.md
local:
  directory: .alphaX/local
process:
  directory: .alphaX/process
```

Do not put project status, paths, or private facts into the manifest. It only
identifies the local data tree shape.

## Local Data

`.alphaX/local/` stores machine-local or user-local clues:

- path aliases;
- quasi-static project metadata;
- local project map;
- local pilot queue.
- resident `agent-runtime-services` endpoint config.

This data may contain private paths or private project names. It must remain
ignored and must not be committed.

## Process Data

`.alphaX/process/` stores alphaX process traces:

- focus radar;
- session ledger;
- decision notes;
- source review backlog;
- review feedback;
- source work candidates;
- loop reports;
- pilot evidence.

Process data is reviewable reasoning summary, not raw hidden model
chain-of-thought. It may mention concrete projects and local evidence, so it
must remain ignored unless explicitly redacted into a generic example.

## Project Compaction Pattern

Projects may keep their own ignored `.alphaX/` shape. That shape can be
lighter than this checkout's `.alphaX/process/` tree, but it should follow the
same lifecycle hygiene rule: append while work is moving, then automatically
check whether compaction is needed after a PR/merge, handoff, freeze, release,
publication, or open-source readiness claim. Also check when project `.alphaX/`
has not been rewritten since the last freeze/handoff/release signal, or when
rough file size, line count, repeated phase logs, or conflicting current-state
pointers make re-entry harder. Perform compaction only after explicit user
approval.

An AOF-style rewrite keeps:

- current baseline: branch, remote, public state, release state, or current
  source-of-truth pointers;
- durable decisions and active boundaries;
- evidence pointers: commands, commits, tests, artifacts, or external checks;
- unfrozen evidence that still affects the next decision;
- open decisions and next actions;
- local-only warnings needed for safe re-entry.

It archives, summarizes, or removes:

- step-by-step command transcripts;
- obsolete phase logs;
- superseded paths or historical names except as explicit anti-drift sentinels;
- duplicated content that already lives in tracked source;
- raw transcript content, secrets, private paths, or hidden model
  chain-of-thought.

Compaction must not make `.alphaX/` authoritative over live source. It only
reduces re-entry cost and stale-state risk. It must preserve unresolved evidence,
open decisions, and rejected-but-not-settled claims as explicit open items or
evidence pointers.

## Invariants

- `.alphaX/` is ignored by Git.
- `git ls-files '.alphaX/*'` returns no paths.
- The GitHub-tracked tree does not contain local paths, project-specific state,
  process ledgers, pilot evidence, loop reports, transcript content, or secrets.
- Local `.alphaX/` data can be regenerated from live project sources and current
  alphaX runs.
- Append-only local `.alphaX/` records should be compacted after major freezes,
  releases, or handoffs when they begin to obscure current state.

## Commands

Initialize local data:

```bash
bash scripts/init-local-alphaX.sh
```

Verify local data:

```bash
bash scripts/verify-local-alphaX.sh
```

Verify open-source source:

```bash
bash scripts/verify-alpha-source.sh
```

## Private Patterns

`.alphaX/local/private-patterns.txt` is optional but recommended. Add one private
literal per line, such as personal names, private organization names, local
machine labels, or other strings that must never appear in the GitHub-tracked
source.

`scripts/verify-alpha-source.sh` reads this ignored file when present and fails
if any listed literal appears outside `.alphaX/`.

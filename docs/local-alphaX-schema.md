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
    project-paths.md
    project-meta-index.yaml
    pilot-candidates.md
    private-patterns.txt
  process/
    README.md
    decision-log.md
    focus-radar.md
    session-ledger.md
    reviewer-backlog.md
    loop-reports/
    pilots/
```

Minimum shape required by `scripts/verify-local-alphaX.sh`: `manifest.yaml`,
`local/README.md`, `process/README.md`, `process/loop-reports/`, and
`process/pilots/`. The other files shown above are recommended defaults created
by `scripts/init-local-alphaX.sh`.

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

This data may contain private paths or private project names. It must remain
ignored and must not be committed.

## Process Data

`.alphaX/process/` stores alphaX process traces:

- focus radar;
- session ledger;
- decision notes;
- review-agent backlog;
- loop reports;
- pilot evidence.

Process data is reviewable reasoning summary, not raw hidden model
chain-of-thought. It may mention concrete projects and local evidence, so it
must remain ignored unless explicitly redacted into a generic example.

## Invariants

- `.alphaX/` is ignored by Git.
- `git ls-files '.alphaX/*'` returns no paths.
- The GitHub-tracked tree does not contain local paths, project-specific state,
  process ledgers, pilot evidence, loop reports, transcript content, or secrets.
- Local `.alphaX/` data can be regenerated from live project sources and current
  alphaX runs.

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

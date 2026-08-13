---
type: "Distribution Contract"
title: "alphaX Plugin Publication"
description: "One-way build, Source identity, parity, installation, and fresh-invocation evidence contract for the alphaX Codex plugin."
tags: ["alphax", "plugin", "publication", "verification"]
---
# alphaX Plugin Publication

```yaml
authority:
  canonical: Alpha Partner Source
  generated_outputs:
    - marketplace source
    - installed plugin cache
  manual_edits_to_generated_outputs: forbidden

package_identity:
  clean_version: 0.1.0+codex.<source-commit-prefix>
  dirty_candidate_version: 0.1.0+codex.dirty-<full-source-fingerprint-prefix>
  provenance_file: .alphax-source.json
  project_scope_source: immutable accepted Source archive under source/
  source_scope_source: explicit live Source checkout

hard_gates:
  - deterministic rebuild produces byte-identical trees
  - package, marketplace source, and same-version installed cache are byte-identical
  - package contains all Source skills plus the alphaX entry skill
  - embedded Source hash matches provenance before project work or review
  - production install requires clean accepted Source
  - fresh invocation replay covers F01-F12 and G01-G14 with independent verdicts
  - every observed answer contains complete package and resolved Source identity fields

evidence_boundary:
  static_verification: source and carrier integrity only
  invocation_replay: observed trigger and judgment behavior only
  product_effect: requires a materially different external research or development applied run
```

## One-Way Flow

`plugin/`, `skills/`, the builder, and tracked Alpha Partner files are canonical
inputs. `scripts/alphax_plugin.py` generates the complete package, including an
accepted Source archive. Never patch a marketplace or cache copy to repair
drift; repair Source or the builder and regenerate both outputs.

For project work and project review, `resolve-invocation` reads the embedded
accepted Source and verifies its full tree fingerprint. For source work and
source review, it requires `--live-source-root`; the output must identify that
checkout as accepted or candidate.

## Formal Review Adopter Quickstart

The canonical invocation and distribution relationship is
`skills/formal-development/SKILL.md#formal-review-routes`. Install alphaX as
one publication unit: `formal-development` and `formal-code-review` are
directly triggerable, while `formal-research-review` is parent-routed.
Independent triggerability does not authorize standalone publication.

From a clean accepted Source, first inspect the complete local state:

```bash
python3 scripts/alphax_plugin.py doctor
python3 scripts/alphax_plugin.py doctor --install
python3 scripts/alphax_plugin.py doctor --json
```

`doctor` is read-only. `doctor --install` is idempotent: it changes only a
missing automatic dependency, re-probes after each attempted change, and reports
the final observed state. Production AlphaX installation requires a clean
accepted Source; never use --allow-candidate to bypass that gate.
Python and Git must pass before the first mutation. A partial AlphaX carrier is
blocked and requires manual inspection; automatic AlphaX installation runs only
when both marketplace and cache carriers are absent, so it never overwrites an
existing tree.
Absent means that no filesystem node lexically exists at either carrier root. A
broken symlink, file, or empty directory is an existing carrier node and remains
blocked for manual inspection without following, deleting, or replacing it.

The doctor requires Python `>=3.10`, Git `>=2.41`, and a Codex CLI that can run
`codex plugin marketplace list --json` and `codex plugin list --json`. If that
Codex capability is absent, doctor returns `blocked` with a manual action and
does not self-install Codex. Node `>=14` plus runnable npm are conditional:
they are needed only when the OCR CLI is absent. The OCR identities are
`@alibaba-group/open-code-review`,
`https://github.com/alibaba/open-code-review.git`, and
`open-code-review-codex@open-code-review`. Automated installation is supported
on macOS and Linux; on Windows, doctor remains read-only and returns upstream
manual guidance.

The OCR CLI must report an `open-code-review v...` product signature and must
not be a development build. A runnable pre-existing carrier is usable but is
reported as `provenance-unverified` with residual risk
`ocr-cli-provenance-unverified`; only a successful npm install and product
re-probe is `package-installed` for that run. An installed OCR plugin passes
only when its exact `marketplaceSource.source` is the approved repository.
Missing or mismatched plugin provenance is blocked and never overwritten.

Exit codes are stable: `ready: 0`, `blocked: 1`, and `action-required: 2`.
Any `failed` change forces `overall: blocked` and exit code 1 while the final
checks and a bounded retry action remain in the report.
Managed review remains `managed-llm-unapproved` until an explicit endpoint and
target-code egress approval exist outside doctor. Unit tests use mocked command
results; local Source verification proves the tracked contract, not a live
installation, managed review, or human acceptance.

## Build And Verify

```bash
python3 -m unittest discover -s tests -v
python3 scripts/alphax_plugin.py verify-source
python3 scripts/alphax_plugin.py build --out <temporary-output>
```

Dirty builds require `--allow-dirty` and are candidates only. A candidate may
support pre-publication source evaluation, but it is not a production install.

## Install And Parity

After Source is accepted and the working tree is clean:

```bash
python3 scripts/alphax_plugin.py install
python3 scripts/alphax_plugin.py verify-installed --require-accepted
```

Installation stages a full generated package, asks Codex to install that
marketplace version, then compares every file in Source output, marketplace
source, and selected cache. Any missing, extra, changed, or same-version drift
is a hard failure.

## Fresh Invocation Replay

The replay creates a temporary isolated `CODEX_HOME`, installs the currently
selected marketplace version there, and enables only alphaX. Run each fixture
in a fresh ephemeral Codex session. A separate fresh evaluator receives the
case contract, observed answer, and compact completed tool evidence, then writes
an independent JSON verdict. The evidence directory is ignored process data,
not public Source.

```bash
python3 scripts/alphax_invocation_replay.py \
  --out-dir .alphaX/process/invocation-replays/<run-id> \
  --jobs 2 \
  --reasoning-effort medium
```

Each case record contains the natural input, package and Source identity,
observed output, command status, and independent verdict. A summary can pass
only when all required fixture IDs are present, every invocation completed, and
every independent verdict passed. Missing package or resolved Source identity
fields fail mechanically even if the evaluator would otherwise pass.

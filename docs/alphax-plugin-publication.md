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
  - fresh invocation replay covers F01-F10 and G01-G11 with independent verdicts
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

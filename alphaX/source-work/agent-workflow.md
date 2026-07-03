---
type: "SOP"
title: "Source Work"
description: "Source work scope, write boundary, and verification requirements."
tags: ["alphax", "source-work", "sop"]
---
# Source Work

```yaml
scope: source work
target: Alpha Partner Source or alphaX function

use_when_changing:
  - AGENTS.md contract
  - scopes, SOPs, templates, skills, docs, scripts, verifiers
  - plugin packaging that carries invocation behavior
  - open-source boundary or local .alphaX/ governance

evolution_governance:
  contract: alphaX/source-work/intelligence-ceiling-half-life.md
  product_goal: help agents autonomously solve more high-value research and development problems
  source_evolution_goal: raise intelligence ceiling and extend asset half-life
  default_line:
    - make core principles thinner and harder
    - evolve cognitive frameworks through applied evidence and judgment fixtures
    - keep operational scaffolding explicit, depreciable, and pruneable
    - keep implementation carriers replaceable
  reject_if:
    - adds process volume without improving judgment or half-life
    - promotes runtime, scheduler, connector, backend, or always-on identity into P0
    - lets verifier strings or template shapes define the product core
  convergence_gate:
    - when repeated cycles recommend no tracked source change and add no materially different evidence or source-mechanism blocker, stop at owner review instead of shifting to another internal alignment surface

write_boundary:
  tracked_source: allowed only for accepted source work
  local_process_notes: source checkout .alphaX/process/
  forbidden: project facts in GitHub-tracked source

verify:
  source_changed:
    - bash scripts/verify-alpha-source.sh
    - git diff --check
    - check alphaX/source-work/intelligence-ceiling-half-life.md improvement signals when the change affects source evolution
    - for insight catcher, check templates/source-work/insight-catcher.md candidate ledger before relying on tracked diffs
    - use templates/source-work/judgment-replay.md for any claim that the change raises intelligence ceiling or asset half-life
    - do not treat passing checks as proof of intelligence-ceiling, half-life, or product-goal improvement
  local_alphaX_initialized_or_used:
    - bash scripts/verify-local-alphaX.sh

not_for:
  source review: audit first, then switch scope before edits
```

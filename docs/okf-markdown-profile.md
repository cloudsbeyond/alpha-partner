---
type: "Source Profile"
title: "alphaX OKF Markdown Profile"
description: "Markdown organization profile for tracked source and ignored alphaX local data."
tags: ["alphax", "okf", "markdown"]
---
# alphaX OKF Markdown Profile

```yaml
purpose: OKF-style Markdown organization for Alpha Partner Source and ignored .alphaX/ data
not: [runtime, service, dependency, strict OKF conformance claim]

p0_rule:
  files: Markdown
  metadata: small YAML frontmatter
  navigation: generated index.md
  links: ordinary relative Markdown links
  citations: explicit when external material supports a nontrivial claim

YAML frontmatter:
  required_except_generated_index:
    type: descriptive document role
    title: display title, usually H1
    description: one sentence consumed by generated indexes
  optional:
    tags: lowercase grouping terms
  known_type_examples:
    - Source Contract
    - Guide
    - SOP
    - Template
    - Skill
    - PRD
    - Evidence Index
    - Research Backlog
    - Data Schema
    - Source Profile
    - Agent Contract
    - Verification Fixtures
    - Failure Modes

index_files:
  generated: true
  frontmatter: false
  grouping_key: type
  links: directory_relative
  description_source: linked document frontmatter
  omit_low_information_intermediate_dirs: true
  source_scope: Git-visible Markdown only
  excluded: [.git/, .alphaX/, .agents/, tmp/, temp/]
  commands:
    write: node scripts/generate-alphaX-indexes.mjs --write
    check: node scripts/generate-alphaX-indexes.mjs --check

link_rule:
  local: relative Markdown links
  external: absolute URLs
  text: target name, not click-here instruction

citations:
  section: Citations
  required_for: nontrivial external-source-backed claim
  internal_evidence: may live in evidence maps or fields
  forbidden: [private transcripts, secrets, raw hidden model chain-of-thought]

local_alphaX:
  may_use_profile: true
  remains_ignored: true
  existing_files_need_rewrite: false

boundary:
  does_not_add:
    - OKF backend
    - OKF reference agent
    - graph viewer
    - schema registry
    - strict conformance checks for ignored existing local data
```

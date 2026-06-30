---
type: "Template"
title: "alphaX Project-Local Mapping"
description: "Compact template for ignored project-local alphaX data."
tags: ["alphax", "template", "project-work"]
---
# alphaX Project-Local Mapping

```yaml
when_to_use: [repeated alphaX use, concrete re-entry pain, explicit user instruction]

install:
  default: target .git/info/exclude
  rule: ".alphaX/"
  commands:
    - "grep -qxF '.alphaX/' .git/info/exclude || printf '\\n.alphaX/\\n' >> .git/info/exclude"
    - "mkdir -p .alphaX"
    - "git check-ignore -v .alphaX/index.md .alphaX/project-context.md .alphaX/evidence.md .alphaX/decisions.md .alphaX/reviews/example.md"
  fallback: external local data directory when .git/info/exclude is unavailable

target_tracked_tree:
  edit_versioned_AGENTS_md: false
  edit_versioned_gitignore: false
  copy_alpha_partner_source: false

project_alphaX_shape:
  minimum_files:
    ".alphaX/index.md": stable local data contract
    ".alphaX/project-context.md": current reload baseline
  optional_extensions:
    ".alphaX/evidence.md": split when evidence pointers bloat context
    ".alphaX/decisions.md": split when durable owner decisions need authority
    ".alphaX/reviews/": create only for explicit durable local review or handoff artifact
  forbidden:
    - AGENTS.md inside .alphaX
    - reports directory as default catch-all
    - copied Alpha Partner Source

data_boundary:
  role: context not control
  live_source_wins: true
  write_rule: update project-context.md first; split only for evidence, decision, or durable-review boundaries
  report_rule: conversation first; persist compact summaries and evidence pointers only
  do_not_store: [secrets, private transcripts, source-of-truth replacements, hidden chain-of-thought, broad alphaX governance]

verification:
  - git status --short before and after setup
  - git check-ignore -v .alphaX/index.md .alphaX/project-context.md .alphaX/evidence.md .alphaX/decisions.md .alphaX/reviews/example.md
  - private-path grep over .alphaX/
```

## `.alphaX/index.md`

````markdown
---
type: "alphaX Project Local Index"
title: "alphaX Project Local Index"
description: "Stable operation contract for ignored project-local alphaX data."
tags: ["alphax", "project-local", "index"]
---
# alphaX Project-Local Operation

```yaml
schema_version: 1
kind: target_project_alphaX_index
default_install: .git/info/exclude

files:
  project-context.md: current reload baseline; update first
  evidence.md: optional evidence pointer registry
  decisions.md: optional durable decision ledger
  reviews/: optional explicit local review artifacts

read_order:
  - target instructions, live source, git state, validation output
  - .alphaX/project-context.md as context only
  - optional files only when referenced or review depth requires them

write_boundary:
  context_not_control: true
  live_source_wins: true
  forbidden: [tracked AGENTS pointer, versioned .gitignore edit, .alphaX/AGENTS.md, default reports directory, copied Alpha Partner Source]

compaction:
  trigger: [handoff, merge, freeze, release, noisy history, conflicting state]
  preserve: [current baseline, durable decisions, evidence pointers, open items, local-only warnings]
  remove_or_summarize: [command transcripts, obsolete logs, duplicated source facts, stale paths, private data]
```
````

## `.alphaX/project-context.md`

````markdown
---
type: "Project Context"
title: "alphaX Project Context"
description: "Project-local current reload baseline for alphaX."
tags: ["alphax", "project-local", "context"]
---
# alphaX Project Context

```yaml
schema_version: 1
kind: target_project_alphaX_context
boundary:
  context_not_control: true
  source_of_truth: live project source, instructions, specs, tests, git state, user decisions
  optional_split_surfaces: [.alphaX/evidence.md, .alphaX/decisions.md, .alphaX/reviews/]

project_identity:
  project_key: "<project-key>"
  relationship_to_alphaX: "<short relationship>"
  owner: "<user|team|unknown>"

source_anchors:
  instructions: []
  specs_or_contracts: []
  validation: []

current:
  last_reviewed_at: "<YYYY-MM-DD|unknown>"
  focus: "<short hint; not source of truth>"
  state: "<compact observed state>"
  stale_if: [live source conflict, branch/diff/validation/owner decision changed]

evidence:
  - id: "<E1>"
    source: "<file|command|commit|artifact|url|user-decision>"
    supports: "<claim or state>"
    freshness: "<current|stale|unknown>"

decisions: []
top_risks: []
open_items: []

review:
  last_project_review: "<YYYY-MM-DD|none>"
  summary: "<compact result or none>"

completion_state:
  implementation_state: "<not-found|partial|implemented|not-reviewed>"
  validation_state: "<not-run|failed|partial|passed|not-applicable>"
  integration_state: "<local-only|branch-only|merged|released|not-reviewed>"
  completion_call: "<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence|not-reviewed>"

lifecycle_hygiene:
  trigger: "<pr-or-merge|handoff|freeze|release|publication|open-source-readiness|stale-alphaX|noisy-alphaX|not-checked>"
  tracked_tree_state: "<clean|dirty|mixed|not checked>"
  ignored_alphaX_state: "<absent|compact|append-only-noisy|contains-risk|not checked>"
  compaction_needed: "<yes|no|not checked>"

unverified_claims: []
```
````

## Optional Extensions

```yaml
.alphaX/evidence.md:
  stores: [evidence ids, command names and outcomes, commits, artifacts, urls, freshness]
  not: [raw logs, secrets, transcripts, copied source]

.alphaX/decisions.md:
  stores: [decision, owner, date, evidence, supersedes]
  not: [agent preference, unapproved private rationale]

.alphaX/reviews/:
  create_only_when: user asks, handoff needs local packet, or repeated review snapshots need audit trail
  project-context_pointer_required: true
  not: [raw command transcripts, secrets, private paths, copied source]
```

---
type: "Plugin Guide"
title: "alphaX Codex Plugin"
description: "Canonical README copied into the generated alphaX Codex plugin."
tags: ["alphax", "plugin", "codex"]
---
# alphaX Codex Plugin

```yaml
authority: Alpha Partner Source
generated_by: scripts/alphax_plugin.py
manual_edits_to_generated_copies: forbidden
project_scope_source: embedded accepted Source snapshot
source_scope_source: explicit live Source checkout
```

This directory is the canonical plugin packaging input for Alpha Partner
Source. Marketplace and installed cache copies are generated outputs, not
independent sources of truth.

The generated plugin contains the alphaX entry skill, every current Source
skill, a package-local invocation resolver, and an immutable accepted Source
snapshot. Project work and review use the embedded snapshot; source work and
review require an explicit live checkout. Every nontrivial invocation reports
package and resolved Source identity.

Build, install, parity, and replay rules are defined in
`docs/alphax-plugin-publication.md` in Alpha Partner Source.

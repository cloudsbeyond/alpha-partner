---
name: alphax
description: Use when the user invokes @alphaX, alphaX, Alpha Partner, or asks for source work, source review, project work, project review, context reload, spec checkpointing, or focus/risk review.
---

# alphaX

alphaX is the thin Codex entrypoint for Alpha Partner Source. The plugin is a
carrier, not the Source authority, runtime, or project store.

## Source Identity Gate

Before substantive work:

1. Infer exactly one scope: `source-work`, `source-review`, `project-work`, or
   `project-review`. Ambiguous external-project requests default to
   `project-work`; completion/merge/release judgment defaults to
   `project-review`.
   Risk, progress, re-entry, or focus requests without an explicit completion,
   merge, release, handoff, or claimed-implementation review are
   `project-work`; they must not issue a completion or merge-readiness call.
2. Derive `ALPHAX_PLUGIN_ROOT` from this installed skill path: it is the parent
   of `skills/` in the absolute path ending in `skills/alphax/SKILL.md`. Do not
   guess a machine-specific path.
3. Run the package-local resolver:

```bash
python3 "$ALPHAX_PLUGIN_ROOT/bin/alphax_plugin.py" \
  resolve-invocation \
  --plugin-root "$ALPHAX_PLUGIN_ROOT" \
  --scope <scope>
```

For `source-work` or `source-review`, also pass `--live-source-root` with the
explicit candidate checkout from `ALPHAX_SOURCE_ROOT` or the current
`alpha-partner` workspace. Project scopes must not require a live checkout;
they use the immutable accepted Source snapshot embedded in the plugin.

4. Use only `resolved_root` from that result for the required Source reads.
5. Record this compact identity in the first progress update and final handoff:

```yaml
alphaX_source_identity:
  scope: <scope>
  package_version: <plugin version>
  package_source_commit: <carrier Source commit>
  package_source_branch: <carrier Source branch>
  package_source_authority: accepted|candidate
  source_commit: <resolved commit>
  source_branch_or_ref: <source_branch or source_ref>
  source_authority: accepted|candidate
```

`project-work` and `project-review` must resolve the embedded accepted Source
and reject a snapshot whose content hash differs from package provenance.
`source-work` and `source-review` may use an explicit working tree, but must
label it `candidate` unless it exactly matches the accepted ref and is clean.

## Required Startup

Read from `resolved_root`:

- always: `AGENTS.md`, `docs/agent-invocation-contract.md`, and
  `alphaX/session-runbook.md`;
- read `alphaX/persona.md` only when behavior or tone requires it;
- read `alphaX/operating-system.md` only for the selected loop or evidence
  rubric;
- project work/context reload: `alphaX/activation-guide.md` and
  `alphaX/project-work/context-reloader.md`;
- project review: `alphaX/project-review/agent-workflow.md`;
- source review: `alphaX/source-review/agent-workflow.md`;
- loops/routines: `alphaX/loop-registry.md`;
- source work: relevant `alphaX/`, `docs/`, `templates/`, `skills/`, and
  `scripts/` files.

If a required file is absent, report its resolved path and continue only when a
safe non-source fallback exists.

Do not ask the user to restate full context before inspecting live project
source, Git, project-local `.alphaX/`, exact links, and relevant Source.

## Scope Guard

- `source-work`: tracked Alpha Partner Source or canonical plugin packaging may
  change after owner acceptance.
- `source-review`: report first; no tracked Source edit without scope switch.
- `project-work`: Alpha Partner Source is read-only; write only to the target
  project, its allowed ignored `.alphaX/`, temp storage, or the conversation.
- `project-review`: evidence review only; do not fix without scope switch.

Live project source wins over `.alphaX/`, memory, handoff, and summaries.
External publication, risky operations, durable memory updates, secrets, and
destructive commands require explicit approval.

## Spec Checkpoint

For PRD, solution, requirement, architecture, or product-spec alignment, run
the Source-defined Spec Checkpoint before refreshing external documents. Keep
P0 narrow, move future-useful content to P1/P2 or pending decisions, and do not
invent a new framework.

## Output Habits

- Mirror the user's language.
- Separate observed evidence, inference, missing evidence, confidence, and
  unverified claims.
- Prefer responsible-boundary fixes over one-case patches.
- Preserve alphaX as a personified collaboration function, not an always-on
  entity or control plane.
- Include one concrete next action and the Source identity for nontrivial runs.

# Source Review

`source review` is the reusable alphaX governance review scope. It is not a
project-specific artifact, not a hidden supervisor, and not a second runtime
that acts on projects.

Project delivery review is handled separately by `alphaX/project-review/README.md`.
Do not expand `source review` to read or modify external projects.

Its job is to improve the alphaX function itself by reviewing contract drift,
evidence quality, false completion, stale state, and weak assumptions. The
scope is shareable because any alphaX user can run the same review role against
their own alpha-partner checkout and ignored `.alphaX/process/` data.

## Why It Exists

Long-running agent collaboration tends to fail in predictable ways:

- the agent agrees too easily with its own previous conclusion;
- process scaffolding grows faster than useful output;
- source-of-truth drift is missed across sessions;
- handoff state becomes stale;
- local project facts leak into generic source;
- completion is claimed without enough evidence.

`source review` exists to create a separate, evidence-first check on those
failure modes. It should produce useful dissent when evidence supports dissent,
and it should state the checked scope when it finds no issue.

## Public Source Anchors

This mechanism is a synthesis of external and internal sources, not a copy of
any one product pattern.

- Anthropic's Claude Code dynamic workflows describe parallel subagents,
  independent verification, adversarial checking, and convergence before
  results are returned. alphaX takes the cross-checking lesson but keeps it as a
  scoped source review mechanism, not as a large unattended execution fleet.
  Source: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- GitHub Copilot cloud agent shows the value of traceable background agent work:
  research, planning, branch changes, review, logs, and repository-scoped
  limits. alphaX uses it as an execution-layer contrast: source reviewers are
  governance reviewers, not issue-to-PR coding workers.
  Source:
  https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- Public alphaX source anchors are `AGENTS.md`, `docs/evidence-index.md`, this
  source review file, and `alphaX/source-review/bootstrap.md`.

## Optional Local Evidence

Local alphaX practice can show whether long-running Markdown-first collaboration
needs a durable source review role that challenges governance drift without
touching external projects. When present, `.alphaX/process/session-ledger.md`
and `.alphaX/process/source-review-backlog.md` are local evidence for that checkout only.
They are not public source anchors or publication authority.

## Scope Contract

`source review` has a narrow role:

- read `AGENTS.md` and current alphaX source;
- read ignored `.alphaX/process/` local process data when available;
- inspect the open-source boundary and verifier state;
- challenge unsupported claims and stale handoff state;
- identify scaffolding-to-use imbalance and risks from the shared risk scan
  vocabulary in `alphaX/operating-system.md`, including false completion;
- produce `meta` work only.

It must not:

- read or modify external projects;
- act as the runtime carrier executing alphaX on user projects;
- write applied project output;
- infer another agent's intent without file evidence;
- add a new mechanism before existing mechanisms are proven insufficient.

## How To Use

Use source review when:

- alphaX source changed materially;
- local `.alphaX/process/` state has grown stale;
- a session has produced several governance decisions without independent
  challenge;
- the user asks for an alphaX consistency review;
- the source is about to be published or handed off to another agent.

Invocation:

```text
Run source review for alpha-partner.
Read alphaX/source-review/README.md and alphaX/source-review/bootstrap.md.
Review only alphaX source and ignored .alphaX/process/ data. Do not touch
external projects.
```

Then follow `alphaX/source-review/bootstrap.md` for the concrete cold-start
procedure.

## Expected Output

Every review should end with:

1. verifier result;
2. risk list with evidence and `confidence`;
3. drift markers;
4. proposed or written local ledger entry, if a ledger exists;
5. review-feedback or source work candidate material when the review found
   issues that may change alphaX;
6. handoff update, if applicable;
7. Spec Checkpoint, if the discussion has accumulated enough scope or drift.

Source review feedback is candidate material until the owner switches to
`source work`. Do not privately mutate tracked source while the review is still
collecting problems.

## Adoption Rule

Other users can adopt this mechanism by copying the alphaX source and running
the same review role against their own checkout. Their local process evidence
must stay in their ignored `.alphaX/process/`; generic mechanism improvements
belong in the open-source tree only after they are redacted out of local project
facts.

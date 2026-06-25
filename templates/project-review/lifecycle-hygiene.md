# Project Lifecycle Hygiene

Use this checklist when project review is checking a PR/merge,
handoff, freeze, release, publication, open-source readiness claim, or stale/noisy
project `.alphaX/` evidence.

This belongs to `project review` by default. Write persistent notes only to the
project's ignored `.alphaX/` when useful and allowed. Perform compaction
only after explicit user approval.

## Trigger Signals

- PR/merge, handoff, freeze, release, publication, or open-source readiness
  claim:
- target `.alphaX/` used as evidence in the review:
- target `.alphaX/` not rewritten since the last freeze, handoff, or release
  signal:
- rough file size, line count, repeated phase logs, or conflicting
  current-state pointers make re-entry harder:

## Source State

- target root:
- branch:
- working tree:
- staged files:
- generated outputs:
- private-path or secret scan:
- target instructions read:

## Evidence State

- claimed outcome:
- validation commands:
- passing evidence:
- missing evidence:
- external artifacts checked:
- unverified claims:
- repeated-surface parity checks:
  - applicable surface family: `<repos, packages, generated pages, schemas, fixtures, or n/a>`
  - parity expectation: `<same core files, same metadata status, same generated artifact shape, or n/a>`
  - evidence: `<command, sample, or reason not checked>`

## Release Or Publication State

- remote URL:
- visibility:
- default branch:
- commit count or intended commit shape:
- tags:
- repository description/topics:
- README posture:
- license posture:
- public metadata gaps:

## Local `.alphaX` State

- target `.alphaX/` present:
- ignored by Git:
- current-state summary present:
- evidence pointers present:
- append-only logs too noisy:
- unfrozen evidence or open decisions present:
- compaction needed:

## Compaction Rule

If target `.alphaX/` has grown as an append-only work log, recommend compaction
or, with explicit approval, rewrite it into:

- current baseline;
- durable decisions;
- evidence pointers;
- unfrozen evidence that still affects the next decision;
- open decisions;
- next actions;
- local-only warnings needed for safe re-entry.

Archive, summarize, or remove:

- step-by-step command transcripts;
- obsolete phase logs;
- duplicated source facts;
- stale paths and superseded names, except explicit anti-drift sentinels;
- secrets, private paths, raw transcript content, or hidden model chain-of-thought.

Do not drop unfrozen evidence, unresolved decisions, or rejected-but-not-settled
claims. If they no longer belong in the baseline, preserve them as explicit open
items or evidence pointers.

## Engineering Call

- blocked:
- needs-owner-decision:
- handoffable:
- mergeable:
- publishable:
- insufficient evidence:

## Next Action

One concrete next action:

# Project Work

`project work` is the scope for using alphaX to help a concrete project,
document, product question, research task, or engineering problem.

In this scope, Alpha Partner Source is read-only. The project being helped owns
its source of truth and its ignored `.alphaX/` objective data surface.

Allowed write targets:

- the project's own files, when the user asked to change that project;
- the project's ignored `.alphaX/`, when present or explicitly initialized;
- an OS temporary directory for scratch work;
- the conversation response.

Do not write project process data into this checkout's `.alphaX/process/`.
If the current working directory is `{alpha-partner}` but the request concerns
another project, ask before writing to this repository.

For project re-entry, read `alphaX/project-work/context-reloader.md`, then inspect
live project source and project-local `.alphaX/` before deciding. Live project
source wins over stale `.alphaX/` data.

Do not use `project work` for report-first evidence review before handoff,
merge, release, freeze, or claimed completion. Use `project review` first.

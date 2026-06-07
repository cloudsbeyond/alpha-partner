# Project Paths

Single source of truth for all project paths used across the workspace. Every file references projects by alias; this file is the only place that maps aliases to absolute paths.

When a machine or user changes, update only this file.

## Self

| Alias             | Path                             |
| ----------------- | -------------------------------- |
| `{alpha-partner}` | `/Users/lizhaohua/Desktop/codex` |

## External Projects

| Alias                        | Path                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| `{agent-interaction-bridge}` | `/Users/lizhaohua/work/llm/agent-interaction-bridge`       |
| `{online_community}`         | `/Users/lizhaohua/work/llm/clouds-beyond/online_community` |
| `{clouds-beyond}`            | `/Users/lizhaohua/work/llm/clouds-beyond`                  |

## Usage

In all other files, use `{alias}` instead of absolute paths. Example: `{agent-interaction-bridge}/AGENTS.md` instead of a hardcoded path like `/Users/.../agent-interaction-bridge/AGENTS.md`.

The verifier checks that no absolute path appears outside this file.

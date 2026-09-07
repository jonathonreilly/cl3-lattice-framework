# Scope + Context Discipline

> This file and `git-workflow.md` load in **every** session. Everything else is parked
> in `~/.claude/rules-ios/` (Swift) and `~/.claude/rules-extra/` (git-workflow detail)
> and read on demand, so parked guidance stops costing context where it doesn't apply.

## Read on demand (not auto-loaded)

Before writing Swift/SwiftUI/SwiftData, or running an autonomous build, Read the
file you actually need from `~/.claude/rules-ios/`:

| File | Read it when |
|------|--------------|
| `coding-style.md` | Writing or reviewing Swift — naming, Swift 6.2 concurrency, SwiftUI/SwiftData patterns, file organization |
| `security.md` | Touching Keychain, biometrics, Data Protection, ATS, or CloudKit |
| `performance.md` | Profiling an app, main-thread work, SwiftData query/batch performance, image or network tuning |
| `autonomous-dev.md` | Running the PRD → architecture → phases → Ralph loop pipeline |

Read the one that applies. Don't read all four.

## Context discipline (applies everywhere)

Repeated broad reads can waste context. In the following historical measurement,
three long sessions: Read was 53% of all context and Bash 43%, and **1.8M tokens went
to re-reading files already read in the same session** — one 155 KB file was read 90
times for ~503k tokens, about 2.5 full windows on a single file.

**Never Read a large file whole.** For any file over ~1000 lines — campaign logs,
archives, ledgers, generated output — `grep -n` for the anchor first, then `Read` with
`offset`/`limit`. Files carrying an entry index (e.g. the Physics memory archives) exist
precisely so the line number is already known; use it.

Reuse unchanged evidence. Re-read the relevant portion when it may have changed,
including concurrent-worker edits, moving remote refs, or a stale snapshot. Before
a source-sensitive edit, review or landing, verify the actual current bytes.

**Cap Bash output at the source**, not after the fact:
- Start with `git diff --stat`, then inspect the full relevant diff for correctness.
  Use bounded `git log` queries with an explicit ref; do not mistake working-branch
  history for landed main history.
- Select relevant paths/fields before reading large output. Do not truncate a
  load-bearing result or error and then infer that the whole check passed.
- one command per call — multi-section `echo "=== … ==="` compounds dump every section
  whether or not the answer needed them
- `rg -c` or `rg -l` when the count or the filename is the answer, not the matching lines

Use scoped subagents when independent work materially helps and delegation is
authorized. A new agent name or repeated conclusion is not independent evidence;
retain the source and verification behind the conclusion.

## Security non-negotiables (universal)

Full iOS detail is in `rules-ios/security.md`; these hold in every language:

- No hardcoded secrets, API keys, tokens, or private keys in code. iOS secrets go in
  Keychain — never UserDefaults.
- Inspect staged changes for actual credentials without printing their values.
  Variable names such as `token` or `password` alone are not evidence of leakage.
- Validate all external input. Never interpolate it into SQL, shell commands, or
  predicates — use parameterized forms.
- Never log passwords, tokens, keys, PHI, or full user input.
- HTTPS only; keep ATS enabled.
- No silent failures: handle or propagate errors, never `try?`-and-discard.

## Prompt and process review

When the task is to examine prompts, skills, or procedures, inspect them for
correctness before applying them. The workflow under review is not permission
to execute itself. Respect the user's selected research cadence and current
repo source; historical local rules are not scientific authority.

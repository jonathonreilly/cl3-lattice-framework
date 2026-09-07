# Git Workflow Rules

> Slim core. Templates, recovery, stash, merge-vs-rebase, hooks detail parked in
> `~/.claude/rules-extra/git-workflow-detail.md` — Read it on demand.

## Conventional Commits

`<type>(<scope>): <description>` — body/footers optional.

Types: `feat` (MINOR) | `fix` (PATCH) | `perf` (PATCH) | `docs` | `style` |
`refactor` | `test` | `build` | `ci` | `chore` | `revert`.
Breaking: `!` after scope + `BREAKING CHANGE:` footer with a migration note.

- Description: imperative mood, lowercase first letter, no trailing period, ≤72 chars.
- Scope = component/feature (`feat(auth):`, `refactor(ScheduleManager):`); keep it
  consistent within a project.
- Body: WHAT and WHY, not HOW; reference issues (`fix(auth): … (#123)`).

## Atomic commits

- One logical change per commit; independently revertable; tests pass after each.
- Before committing: review the full relevant staged diff and run appropriate
  checks. Distinguish required scientific runner output from stray debug output;
  the presence of `print(` alone is not a defect.

## Never commit

- Secrets: `.env`, `credentials.json`, `secrets.yaml`, API keys/tokens/passwords,
  private keys, certificates.
- Build artifacts: `DerivedData/`, `.build/`, `*.xcarchive`.
- System/editor files: `.DS_Store`, `*.swp`, `xcuserdata/`, `.idea/`/`.vscode/`
  (unless team-agreed).
- Debug code in production paths: hardcoded test data, leftover `#if DEBUG`,
  commented-out blocks.

## Branches

`feature/<desc>` `fix/<desc>` `refactor/<desc>` `docs/<desc>` `release/<version>`
`hotfix/<desc>` — one focused change per branch; delete merged branches.

PR title = conventional-commit format; keep PRs focused (<400 lines ideal).

## Dangerous operations — NEVER without explicit user request

- Force push to shared branches (own branches: `--force-with-lease`).
- Rewriting published history (`rebase -i` on a shared branch).
- `git reset --hard` that loses commits (prefer `--soft`).
- Deleting remote branches unverified (`git branch --merged` first).

Recovery (reflog/revert), stashing (push/pop pairing trap), merge-vs-rebase, PR body
template, hooks → detail file.

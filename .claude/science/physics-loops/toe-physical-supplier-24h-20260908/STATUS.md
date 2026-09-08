# Physics campaign status

Updated 2026-09-08T15:37:47.368311+00:00. Running until September10 at10:27UTC (6:27a.m. Eastern), subject to available account usage. No reset credits are authorized.

Useful progress: five conditional science review PRs are open,8036–8040. The newest gives exact bounds on charge-pair energy while retaining native fermion phases. These are finite model results, not TOE completion.

The improved L4 simulation passed all planned precision and cross-arm checks, with original-path tag retention below1%. Remaining projection-error diagnostics are unresolved, so ground-state convergence is not established. Next: independent replay and a prospective larger-lattice comparison. Two workers also examine global charge reachability and exchange.

Disk: about69GiB free after cleanup. All31removed old worktrees retain their local and remote branches. Disposable generated caches were deleted. Exact restore commands and remote HEADs are in disk-cleanup-20260908/FINAL_CLEANUP_REPORT.md. Useful evidence is kept on remote science/archive branches or review PRs before local deletion.

SSH commands:

    cat /private/tmp/toe-physical-supplier-24h-20260908/.claude/science/physics-loops/toe-physical-supplier-24h-20260908/STATUS.md
    cat /private/tmp/toe-physical-supplier-24h-20260908/.claude/science/physics-loops/toe-physical-supplier-24h-20260908/STATE.yaml
    df -h /private/tmp
    git -C /private/tmp/toe-physical-supplier-24h-20260908 log -5 --oneline

Keep the machine powered on and the desktop app running for local scheduled continuation. This matches the [scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app). Power settings currently disable system sleep. Do not launch a duplicate supervisor while this task is active. No main merge or formal audit verdict has been applied.

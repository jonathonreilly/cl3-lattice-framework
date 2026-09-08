# Physics campaign status

Updated 2026-09-08T16:09:08.796036+00:00. Active until September10 10:27UTC (6:27a.m. Eastern), subject to available usage. Weekly remaining65%; no reset credits authorized.

Six conditional science review PRs are open,8036–8041. The latest proves complete charge-pair configuration connectivity in the stated model and verifies a full-lattice fermionic exchange witness. An exact charged-fermion/U1 representation has passed independent review and is being packaged. These are model-level bridges, not TOE completion.

L4 passed planned precision/cross-arm checks, but remaining projection-error diagnostics are unresolved. L8 is now running fixed production: 42/128 segments completed at this checkpoint, no failures. No interim physics comparisons or sample replacements. Concurrent proofs examine pair creation and whether virtual pairs generate ring dynamics.

Disk about65GiB free.31old worktrees were removed only after exact remote-HEAD verification; their recovery map is disk-cleanup-20260908/FINAL_CLEANUP_REPORT.md. Useful evidence must be remote before local deletion.

SSH:

    cat /private/tmp/toe-physical-supplier-24h-20260908/.claude/science/physics-loops/toe-physical-supplier-24h-20260908/STATUS.md
    cat /private/tmp/toe-physical-supplier-24h-20260908/.claude/science/physics-loops/toe-physical-supplier-24h-20260908/STATE.yaml
    cat /private/tmp/toe-24h-probes-20260908/reptation-propagated-l8-design/PRODUCTION_OUTPUT/STATUS.json
    ps -p 30888 -o pid,etime,command
    df -h /private/tmp
    git -C /private/tmp/toe-physical-supplier-24h-20260908 log -5 --oneline

Keep the machine powered on and desktop app running for local scheduled continuation, as in the [scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app). System sleep is disabled. Do not launch a duplicate supervisor. No main merge or formal audit verdict has been applied.

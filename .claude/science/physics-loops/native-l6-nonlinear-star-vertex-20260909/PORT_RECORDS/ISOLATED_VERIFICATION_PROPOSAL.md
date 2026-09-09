# Unlaunched portable verification proposal

Copy only the complete SOURCE_MANIFEST membership plus SOURCE_MANIFEST.json into a fresh directory preserving repository-relative paths. No candidate solver or original worktree is needed. Python3 with NumPy is required; record actual interpreter/NumPy/module origins and runtime hashes before and after in the external root wrapper. Local helper execution compiles verified source bytes and never consults local pyc.

One process worker, externally monitored with its supervisor included in384MiB whole-tree RSS;180 seconds total including startup, extraction, exact geometry, replay, output and postchecks. Primary owns a180-second alarm as a secondary guard. Single attempt; preserve PARTIAL/FAILED and external receipts, no replacement. Proposed cap is not a measured canonical forecast; accepted original replay plus geometry readiness motivate feasibility, and root must review this cap before launch.

The full command, from the isolated root, is:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /usr/bin/time -lp python3 -I -B -OO scripts/native_l6_nonlinear_star_vertex_2026_09_09.py --json --verify

This command is a proposal, not an executed receipt. The default invocation without --verify performs exact geometry and accepted-scalar checks only. No new native solve/SVD is performed by either mode. Full mode decompresses fourteen files to temporary disk, holds seven real vectors and action temporaries, verifies raw complex phases, and requires exact accepted certificate equality. The external wrapper must enforce whole-tree resources and retain output on timeout; primary peak is self RSS only.

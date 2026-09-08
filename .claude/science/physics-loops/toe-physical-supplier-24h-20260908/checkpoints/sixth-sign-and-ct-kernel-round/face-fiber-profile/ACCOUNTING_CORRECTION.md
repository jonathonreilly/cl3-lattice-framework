# Pre-execution accounting correction

Original freeze7c249e9fa9b3caa1236f12759e74fb0e66bda2ece5dd190434b69fbab842f3f6 and every referenced source/control are archived under SUPERSEDED_7c249e9f. No profile was executed. Root's full source review identified omitted unallocated overhead in the hypothetical-chain formula, and that Python START is after interpreter startup.

The scientific factory, conditional draw, checkpoint and measurements are unchanged. The launcher now gives the child at most28 seconds from internal START, with an internal29-second post-validation limit, reserving time for startup/receipt work. These are implementation deadlines, not a proof that total wall time is below30 seconds. The authoritative measurement is /usr/bin/time -lp around the complete Python launcher, including interpreter startup, freeze/runtime checks, child, raw validation and pending-forecast serialization. The shell wrapper preserves its output separately. If rounded outer time plus0.01 seconds exceeds30 seconds, the profile fails the total-cost gate. No retry follows. Unexpected OS scheduling can still overrun a wall budget; it is reported, not hidden.

Let T be that rounded-up outer elapsed and A the sum of all explicitly timed geometry, initialization, block, measurement, save and load work over BOTH cases. Set overhead U=max(0,T-A). Each hypothetical chain pays the ENTIRE U, not U divided by cases/chains. For each V the final screen is

  16*[setup_V + 16*(1536*max_three_block_time_V + mean_measurement_time_V)] +16*U.

This conservative duplication prices startup, hashing, serialization, garbage collection and other unallocated measured profile costs per hypothetical chain. It is still only a fixed-face empirical screening proxy, not a bound on unmeasured faces or effective independent-sample cost.

The small final scalar arithmetic step reads the already-validated pending forecast plus the outer receipt and publishes the final forecast; it is explicitly separate post-profile bookkeeping. It does not replay the fixture or exclude any producer/validation/serialization cost from T. The old 'external_seconds' name for internal dispatch timing is removed. Root may independently collect an additional high-resolution outer clock, but no new timing data is asserted here.

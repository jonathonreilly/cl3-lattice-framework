# Independent ice-estimator calibration and replication review

Disposition: PASS for the finite diagnostic conclusions. No numerical or statistical correction required. The full-curve failure remains valid; the short replication neither rescues it nor proves finite-population unbiasedness. No phase conclusion follows.

## Exact coverage

Read complete calibration and replication preregistrations/reports, all newly authored calibration/analysis/exact-target/kernel/measurement/launch/verification scripts, and the actually invoked producer functions (systematic resampling, propagation, preparation, observable coefficients/evaluation, measurement and gap conversion). Read current imported geometry/count/update and initial/Gauss/flux function bodies. Checked every file against both HASHES.json manifests and all runtime source hashes in SOURCE_BINDING.json; all match. The1299-line preserved producer's unrelated large-volume fitting/driver functions are not invoked here and are not certified by this review. The imported topological solver is unused and not reviewed as physics authority.

The earlier ice-physics probe/report were authored by me, so comparison against them is continuity of my own derivation, not an independent cold review of my own work. The new author's exact graph construction is separate. My fresh check.py recomputes summary statistics directly from all raw replica arrays, checks AST instrumentation identity and source-copy identity, and compares new exact curves to the earlier complete-spectrum calculation. It passes23 controls. No stochastic jobs rerun and no author outputs overwritten.

The reviewed report hashes are calibration ef9e0cc33507033ec5d369981293581cfea38d0af9d51d829f89f887eb1d5f72 and replication recorded in SOURCE_HASHES.json. This review binds both complete directory snapshots.

## Target and kernel

The target is the L2 864-state mobile component, not the whole Gauss/flux sector and not an infinite-volume state. The same actual staggered transverse primary observable is evaluated on all states. Geometric move multiplicities are retained. For V<=1 here, b=1-(V-1)nf/24>=1 and the proposed flip probability1/b is valid. Multiplying the normalized proposal kernel by b gives exactly I-H/24, including its diagonal. The unused V>1 extension would require a different sampling check; it is not claimed.

The normalized endpoint genealogy functional has stationary RIGHT distribution proportional to psi, not psi². Summing suffix descendants provides the left vector R^(24F)1. This gives precisely the displayed stationary C_F. For a nonstationary right distribution r, the time-dependent total path weight in the denominator is essential and is correctly retained in N_r(tau). The classical warmup uses the RK stochastic Q, then normalized G propagation for burn. At subsequent origins the exact right distribution has evolved further; the author's explicitly computed first-origin transient is not a separate certified bound for every later origin. Its tiny floating residual and the fixed finite stationary comparison are sufficient for the stated diagnostic, not a rigorous error certificate. No conclusion depends on calling this residual an exact zero.

AST equality confirms that the measurement derivative only removes terminal C0 normalization and changes the function name. It has not recovered the discarded Feynman-Kac growth normalizers, and the reports explicitly say so. The fixed-seed tau_max comparison correctly tests the first origin's shared prefix; shorter subsequent timing is disclosed. The finite-gap conversion keeps the actual discrete Green kernel rather than silently using exp(-H).

## Statistical controls

Each replica is the analysis unit. Four origins and six modes stay inside it; all352 seed values across both experiments are distinct. Distinct pseudorandom seeds are the ordinary simulation independence design, not a mathematical proof of ideal random independence. No report claims such a proof. Recomputing all12 original means/SEs and consistency failure lists agrees; both128-replica results, pooled ratios and delta-method SEs agree as well.

For independent-replica pairs (N_i,D_i), the pooled estimator is mean(N)/mean(D); its estimated SE uses sample variance of N_i-ratio D_i divided by n and mean(D)^2. The implementation includes covariance and is correct as a first-order delta estimate, not an exact finite-sample interval. Averaging normalized blocks is a different estimator from the pooled ratio; both are explicitly preserved. Block-level covariance and second-order ratio expansion are descriptive moments, not independent-block uncertainty estimates or an unbiasedness certificate.

A deliberate pseudoreplication calculation gives tau3 SE .00229805 instead of .00236977 at512, and .00115980 instead of .00103985 at2048. Thus treating512 origin blocks as independent changes the result and does not even always underestimate SE on this sample. The real analysis correctly avoids it. No generic directional statement about those sample differences is justified.

The4SE tests are explicitly fixed diagnostics without guaranteed simultaneous confidence coverage. Multiple correlated times/cells and a noisy8-replica SE mean the old5.28SE outlier cannot be assigned a retrospective calibrated p-value. The focused replication uses fresh samples and changed later-origin spacing; it supports only nonreproduction at the new precision. It does not establish the outlier's cause. Lack of a population difference is not proof of absent bias. Negative curves and negative replica values are retained, with inadmissible logarithmic fits left missing rather than selected away.

## Physics inference

The strongest supported finding is that ancestry/ESS health does not imply relative precision for a signed product correlator. The RK control loses no ancestors yet fails the late signal, so improving genealogy alone is not a sufficient remedy. At L2 the exact finite-forward bias is tiny while C(16) is around1e-9 and stochastic noise around1e-3. This failure is about the specified observable estimator and time range, not the Hamiltonian's phase. Larger lattices have different gaps and signal scales; the L2 noise ratio cannot be extrapolated into a certified population budget for L18.

The short replication removes positive evidence for a stable tau3 discrepancy at roughly1e-3 precision. It does not license fitting the unresolved8–14 window. A useful next physics step is an independently calibrated variance-reduced or positive spectral/moment estimator in this same component, with explicit pure versus finite-forward target. Only after that should matched-momentum volume tests address spectral residue and dispersion. Component ground selection, matched electromagnetic identification and a uniform infrared limit remain separate obligations.

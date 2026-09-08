# Focused L2 tau3 replication

Outcome: the new preregistered tau1–3 consistency tests pass for both populations and both ratio conventions. The isolated earlier tau3 discrepancy is not reproduced. No deterministic finite-population implementation flaw was found. This does not prove unbiasedness and does not rescue the failed tau0–16 precision calibration.

## Executed unchanged mechanism

V.95,F6,classical warmup20,burn40, four origins per replica with3 intervening sweeps, primary mode(1,0,1). Populations512 and2048 each have128 fresh independently seeded replicas; no earlier sample was reused. All seeds, four raw product means/sums and genealogy arrays per replica are retained in eight batch JSON files. The same kernel, observable and measurement derivative bytes were used. `verification.json` proves byte identity to the reviewed sources and fixed-seed exact equality of raw tau0–3 and genealogy outputs from tau_max16 versus tau_max3. Both use the identical tau3 endpoint at sweep9 and suffix6.

The shorter block changes absolute timing of subsequent origins relative to the old experiment. This was prospectively disclosed; it does not alter the stationary finite-F target but prevents presenting this as a bit-for-bit replay of the previous four-origin protocol. Four origins remain correlated observations inside one replica; all SE estimates use128 independent replicas.

All eight batches completed,32.067seconds total measured time, maximum RSS205.156MiB. Each stayed within180seconds/384MiB and the aggregate360second limit. No failure, discarded replica, seed replacement or extra batch occurred. No ongoing job remains.

## Quantitative primary result

The exact finite-F tau3 target is .0176171228539501. The mean-of-four-block-ratios results are:

|Population|tau1 mean ± replica SE|tau2 mean ± replica SE|tau3 mean ± replica SE|
|---|---|---|---|
|512|.2253679 ± .00240965|.0616685 ± .00226058|.0175434 ± .00236977|
|2048|.2234765 ± .00133293|.0612895 ± .00116374|.0162469 ± .00103985|

The tau3 standardized residuals are -.031 and -1.318 SE. All six mean-ratio comparisons pass |error|<=4SE+1e-8. All pooled-raw comparisons also pass. The three population differences pass the separately frozen4 combined-SE+1e-8 diagnostic. Specifically, the tau3 difference512-minus2048 is .00129649 with combined SE .00258787. It provides no resolved evidence of a population trend. These are finite-sample diagnostics, not guaranteed confidence coverage or an unbiasedness theorem.

The old8-replica error and unusually small old SE are not used as ground truth. The128-replica result is compatible with a statistical fluctuation or uncertainty-estimation instability in the original experiment; it does not prove that retrospective explanation. The different absolute origin spacing is another reason not to assign a new p-value to the old event. No single gap criterion is used.

## Numerator, denominator and ratio covariance

Raw means are before C0 normalization, not absolute Feynman-Kac growth normalizers. At tau3:

|Population|mean numerator|mean denominator|Cov(replica numerator, denominator)|pooled ratio|mean ratio minus pooled|
|---|---:|---:|---:|---:|---:|
|512|.00707817078|.405498505|-6.19657e-6|.0174554794|8.79430e-5|
|2048|.00654506683|.405776024|8.13688e-8|.0161297525|1.17182e-4|

The exact stationary denominator is .405873692. The denominator replica SDs are .0152393 and .00888102. The pooled-ratio SE is computed from the independent-replica fluctuation N-C D, divided by sqrt(128) mean(D): .00235380 and .00104140 at tau3. This exposes covariance instead of treating numerator and denominator as independent.

For descriptive comparison, the second-order block-ratio expansion mu_N Var(D)/mu_D^3-Cov(N,D)/mu_D² gives8.10980e-5 and1.15616e-4, near the observed ratio-convention differences. This expansion is not an exact bias certificate. The measured differences are much smaller than the old .0072 discrepancy and do not provide evidence that ratio convention alone caused it. Covariances at every tau, both block and replica level, are in SUMMARY.json.

## Distribution and outliers retained

At tau3 the512 replica means range from -.06246 to .08213, with empirical skewness -.119;29 of128 are negative. At2048 they range from -.02155 to .05250, skewness .157;8 are negative. Quantiles and every tau3 replica value are retained. No value is excluded as an outlier. The descriptive distributions do not show an extreme one-replica-dominated mean, but they do show substantial signed-product noise. Higher population reduces the replica variance; it does not make individual short correlator estimates necessarily positive.

## Interpretation and remaining uncertainty

The fresh data resolve the narrow question in the following sense: the earlier isolated4-SE failure is not stable under the independently seeded128-replica experiment, and the proposed deterministic kernel/count/observable errors remain contradicted by the prior exhaustive checks and current byte-preserving replay. There is no positive evidence here for a persistent tau3 population bias at the available precision. There is also no proof of its absence below roughly1e-3.

The old full-curve calibration stays failed and unchanged. This short replication says nothing new about tau16 relative precision, a large-volume estimator, an infrared pole or a phase. A different variance-reduced or spectral estimator would still need independent calibration before physical use.

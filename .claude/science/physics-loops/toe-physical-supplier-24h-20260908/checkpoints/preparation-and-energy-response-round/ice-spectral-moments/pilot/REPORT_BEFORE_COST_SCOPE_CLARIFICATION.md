# Fixed RK local-moment pilot: completed, with a cost-efficiency failure

The preregistered four cells completed without resource or coverage reduction. All 32 chains in each cell and both burn protocols are retained. This is a finite RK component sampler and local-observable test, not a detuned calculation, stationary-measure certificate, full ground selection, isolated pole or photon claim. No L4 Hilbert-space enumeration occurred.

## Source and pre-production review

Pilot source SHA256 `874c003b54e87fbcbc187e66a2ca31df69a35452d921de7e07eec4a7dc23e06e`; analysis SHA256 `cb9b9ff7ad38558901bbd09a7ace8b910d62702068daa765f63f9edc20c317a8`. The fixed proposal and PREREGISTRATION precede production. Independent reviewer read the full observable/analysis, executed independently reconstructed L2/L4 controls, and closed the timing delta before launch; see sibling `ice-rk-pilot-cold-review/CODE_REVIEW.md` and `TIMING_DELTA.md`. The cost patch leaves trajectories unchanged and its previous source/diff are retained.

Both micro receipts pass all 864 states and 41,472 signed-update cases. Their combined time was 4.491 seconds; revised micro RSS210.20MiB. Two actual adverse scripts (omit staggering, wrong orientation) fail mathematical assertions. An unavailable `python` alias exited127 before execution; its stderr is preserved, and `python3` performed the successful revised micro. These are distinct from scientific failures.

## Resources and fixed sampling

Four child runs totaled 2.488841 seconds (2.852997 seconds including subprocess overhead), maximum production RSS 144.734MiB. Each was below120seconds/384MiB, far below the510second aggregate envelope. All128 chains and32768 per-chain measurements are retained in four NPZ files; the six/twelve simultaneously measured modes are correlated and are not additional independent replicas.

Each sweep makes3L^3 uniform geometric plaquette proposals and flips if flippable. The observable channels are complex O, |O|², d=qhat²N_f^(ab)/(2L³), and |LO|² with signed complex changes summed before squaring. SEs below are independent-chain delta estimates retaining numerator/denominator covariance. The means are finite-chain estimates, not exact stationary values.

## All mode estimates

|L|burn|harmonic, momentum, polarization|S ± SE|mu1 ± SE|mu2 ± SE|
|---|---|---|---|---|---|
|2|32|[1, 0, 1]|0.409119 ± 0.008522|1.603983 ± 0.036366|3.199612 ± 0.050306|
|2|32|[1, 0, 2]|0.412781 ± 0.009142|1.608088 ± 0.028116|3.204347 ± 0.044095|
|2|32|[1, 1, 0]|0.410583 ± 0.007357|1.598261 ± 0.031209|3.145979 ± 0.047926|
|2|32|[1, 1, 2]|0.410339 ± 0.008785|1.648817 ± 0.034583|3.177748 ± 0.048089|
|2|32|[1, 2, 0]|0.427185 ± 0.009020|1.553865 ± 0.035973|3.174025 ± 0.041326|
|2|32|[1, 2, 1]|0.424500 ± 0.007978|1.593817 ± 0.033483|3.144788 ± 0.050985|
|2|128|[1, 0, 1]|0.419678 ± 0.008722|1.605585 ± 0.033632|3.242292 ± 0.049528|
|2|128|[1, 0, 2]|0.414551 ± 0.006815|1.580536 ± 0.025082|3.169317 ± 0.049577|
|2|128|[1, 1, 0]|0.438477 ± 0.007550|1.536748 ± 0.029284|3.131125 ± 0.049414|
|2|128|[1, 1, 2]|0.415039 ± 0.008738|1.611765 ± 0.038857|3.143824 ± 0.061993|
|2|128|[1, 2, 0]|0.398926 ± 0.008054|1.642442 ± 0.034830|3.281212 ± 0.043231|
|2|128|[1, 2, 1]|0.404053 ± 0.008455|1.655589 ± 0.032486|3.273414 ± 0.044408|
|4|32|[1, 0, 1]|0.369164 ± 0.006070|0.720240 ± 0.012170|0.897007 ± 0.013376|
|4|32|[1, 0, 2]|0.387939 ± 0.005143|0.686227 ± 0.009254|0.878805 ± 0.009715|
|4|32|[1, 1, 0]|0.375725 ± 0.005164|0.707662 ± 0.009705|0.900370 ± 0.009603|
|4|32|[1, 1, 2]|0.370529 ± 0.006045|0.717462 ± 0.012643|0.909021 ± 0.011211|
|4|32|[1, 2, 0]|0.372635 ± 0.005978|0.714411 ± 0.011533|0.907672 ± 0.011083|
|4|32|[1, 2, 1]|0.392090 ± 0.006383|0.678009 ± 0.011607|0.888300 ± 0.012446|
|4|32|[2, 0, 1]|0.377579 ± 0.007204|1.408375 ± 0.025949|2.770600 ± 0.033180|
|4|32|[2, 0, 2]|0.379669 ± 0.004930|1.402349 ± 0.018254|2.838458 ± 0.032652|
|4|32|[2, 1, 0]|0.387039 ± 0.007460|1.373950 ± 0.026365|2.742539 ± 0.033025|
|4|32|[2, 1, 2]|0.375458 ± 0.007345|1.416088 ± 0.027816|2.871393 ± 0.042678|
|4|32|[2, 2, 0]|0.379181 ± 0.007341|1.404155 ± 0.027834|2.874225 ± 0.050043|
|4|32|[2, 2, 1]|0.378021 ± 0.006659|1.406485 ± 0.024952|2.780718 ± 0.038434|
|4|128|[1, 0, 1]|0.376583 ± 0.005423|0.704530 ± 0.010315|0.898155 ± 0.007898|
|4|128|[1, 0, 2]|0.380394 ± 0.004972|0.697256 ± 0.009880|0.886380 ± 0.009332|
|4|128|[1, 1, 0]|0.376385 ± 0.004838|0.704901 ± 0.009778|0.910730 ± 0.010034|
|4|128|[1, 1, 2]|0.371120 ± 0.005143|0.718087 ± 0.010590|0.901035 ± 0.010573|
|4|128|[1, 2, 0]|0.378723 ± 0.004995|0.700332 ± 0.009550|0.892909 ± 0.011536|
|4|128|[1, 2, 1]|0.373905 ± 0.004967|0.712739 ± 0.009845|0.908444 ± 0.011489|
|4|128|[2, 0, 1]|0.376381 ± 0.005520|1.409817 ± 0.020770|2.820688 ± 0.039560|
|4|128|[2, 0, 2]|0.379395 ± 0.004302|1.398186 ± 0.016099|2.765484 ± 0.032697|
|4|128|[2, 1, 0]|0.389320 ± 0.006998|1.362960 ± 0.025446|2.767466 ± 0.041125|
|4|128|[2, 1, 2]|0.381020 ± 0.007132|1.398861 ± 0.026099|2.748063 ± 0.033989|
|4|128|[2, 2, 0]|0.376373 ± 0.006177|1.409410 ± 0.023938|2.816711 ± 0.034279|
|4|128|[2, 2, 1]|0.380074 ± 0.006495|1.402343 ± 0.023837|2.821065 ± 0.031079|

All36 L2 checks (three quantities, six modes, two burns) satisfy the declared4SE+1e-8 comparisons with S=5/12, mu1=8/5, mu2=16/5. All54 burn comparisons and72 paired split-half moment comparisons have no declared4SE flag. These thresholds are diagnostic, not a proved simultaneous confidence level or mixing bound. The finite-window, within-chain-centered influence ESS ranges from 4485.9 to 7149.0 for mu1; it is not certified effective sample size. Full ACFs and block/chain comparisons remain in SUMMARY.json.

L2 harmonic1 and L4 harmonic2 share q=π. For the fixed (momentum0,polarization1), burn128 comparison, mu1 changes from1.605585±0.033632 to1.409817±0.020770 and S from0.419678±0.008722 to0.376381±0.005520. Equality was not a pass requirement; this is a finite-volume change. L4 harmonic1 has q=π/2, with mu1 approximately0.70 and mu2 approximately0.90. It is a different momentum, not another matched-volume estimate. A centroid or Rayleigh upper bound does not identify a pole, gap equality or dispersion exponent.

## Actual measurement cost: unfavorable for conditioning here

Cost is warmed wall time on2048 saved snapshots per cell,20 repetitions. One-face proposals use a separate RNG after production. Updating benchmarks copy snapshots and include amortized seeding/copying, so they are not an exact decomposition of production runtime. Times are empirical and lack a timing confidence interval. No count is assumed to be maintained for free.

|L|burn|update-only sweep μs|full measurement μs|one-face numerator μs|count numerator μs|count/one ratio-influence variance×cost range|
|---|---|---|---|---|---|---|
|2|32|0.2983|0.4930|0.0094|0.0641|1.683–1.940|
|2|128|0.2908|0.5069|0.0095|0.0651|1.538–1.874|
|4|32|2.0996|4.1520|0.0132|0.5471|3.650–7.897|
|4|128|2.1079|4.1411|0.0153|0.5434|2.763–5.760|

Every count/one ratio-influence variance×kernel-cost exceeds1: conditioning reduces snapshot variance but costs more than the reduction saves in this implementation. The all-face literal method is still slower. This is the preregistered computational-effectiveness failure, preserved without tuning. It is not an end-to-end MCMC asymptotic-variance comparison: update cost, cross-time covariance, shared measurement needs and incrementally maintained counts could change that comparison and were not silently credited.

## Remaining obligation

The RK local sum-rule readout works at L4 with modest observed cost and percent-scale finite-chain uncertainty, avoiding a tiny late-time correlation signal. The stationary component assumption still lacks a quantitative mixing proof; the tests do not identify all zero-flux components. Exact detuned ground weighting is absent. Larger volumes, an optimized incremental estimator, stationary error guarantees, spectral concentration and photon inference require new work and scope. No additional job is launched by this report.

# Frozen RK regulated inverse-moment pilot results

All four authorized cells completed without replacements: L2/L4, burns32/128,32 independent chain units and256 origins each. Each first origin is burn+1 sweeps; lag namespace is400000000+chain_id. Kernel and schedule were unchanged after independent preproduction review.

Subprocess wall total 3.697578749s; including micro 4.875811082s. Maximum cell RSS 152.687500MiB. These are actual end-to-end cell timings, substantially below the deliberately conservative forecast; they do not establish comparative asymptotic efficiency.

| L | burn | harmonic | alpha | truncated r | replica SE | exact consistency | precision |
|---|---|---|---|---|---|---|---|
|2|32|1|0.25|0.628932048|0.022331705|True|False|
|2|32|1|0.5|0.526393034|0.011750636|True|True|
|2|32|1|1.0|0.395235067|0.005018995|True|True|
|2|128|1|0.25|0.587572816|0.021593936|True|False|
|2|128|1|0.5|0.510000000|0.010307105|True|True|
|2|128|1|1.0|0.407475728|0.005634683|True|True|
|4|32|1|0.25|1.169956122|0.022521669|no L4 oracle|True|
|4|32|1|0.5|0.901302753|0.009628906|no L4 oracle|True|
|4|32|1|1.0|0.617025182|0.004154891|no L4 oracle|True|
|4|32|2|0.25|0.679419048|0.018413181|no L4 oracle|False|
|4|32|2|0.5|0.591633759|0.010718377|no L4 oracle|True|
|4|32|2|1.0|0.444849742|0.004458414|no L4 oracle|True|
|4|128|1|0.25|1.125262710|0.015434972|no L4 oracle|True|
|4|128|1|0.5|0.895105320|0.009201974|no L4 oracle|True|
|4|128|1|1.0|0.610768903|0.003567811|no L4 oracle|True|
|4|128|2|0.25|0.667978043|0.019040849|no L4 oracle|False|
|4|128|2|0.5|0.589920121|0.012413187|no L4 oracle|True|
|4|128|2|1.0|0.442330440|0.004997185|no L4 oracle|True|

All6 L2 exact truncated-target comparisons satisfy the predeclared4SE criterion. Precision4SE<=10%r passes14/18 rows: alpha.25 fails at both L2 burns and both L4 harmonic2 burns. Thus the full precision criterion fails; no extra chains or altered regulators were run. All9 independent-burn comparisons are unflagged at4SE; absence of a flag is not a mixing or stationarity certificate. All pooled numerators/denominators are positive, and no chain-level real numerator mean is negative; signed complex products and imaginary diagnostics remain in raw output.

The estimate is the geometric elementary-step resolvent with discarded K>Kmax contributions set to zero, not replacement by a capped endpoint. Kmax L2=[800,368,169], L4=[6373,2922,1329]. For each alpha the stationary clipping error is bounded analytically by q^(Kmax+1)/alpha<=.001; floating values are reported alongside exact rational comparisons. Clipped counts by cell: [(2, 32, [3, 4, 11]), (2, 128, [3, 9, 11]), (4, 32, [0, 7, 3]), (4, 128, [2, 3, 11])]. The tail bound is distinct from replica sampling uncertainty and possible finite-burn bias.

The regulator remains finite: r_alpha integrates1/(omega+alpha), not1/omega. L2 comparisons use the exact truncated finite-component targets. L4 has no exact oracle here. Neither clipping control nor nominal confidence establishes the unregulated inverse moment. The reported1/r-alpha values are plug-in statistics, not rigorous gap bounds. The exact positive inelastic-measure inequality applies only to exact expectations on the declared component, not automatically to these estimates; no pole or photon inference is made.

ANALYSIS.json preserves all chain-level joint S/Y means, sample covariance across harmonics and alphas, ratio-influence covariance, paired-alpha differences and independent-burn comparisons. NPZ files preserve every complex origin, product, geometric lag and clipping flag. Four cells contain32768 origins total; origins and modes are not counted as independent replicas. No Nf was added after the freeze.

Frozen source checks and independent review are preproduction evidence, not additional stochastic replicas. Original micro source/hash and reporting repairs remain preserved. PRODUCTION_FINAL_HASHES.json binds this report, analysis, source and raw files.

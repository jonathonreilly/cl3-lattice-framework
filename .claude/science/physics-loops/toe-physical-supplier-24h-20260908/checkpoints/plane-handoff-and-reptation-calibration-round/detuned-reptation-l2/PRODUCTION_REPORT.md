# Exact-graph L2 reptation production

All nine frozen cells completed,32 independent chains each,65536 measured attempted updates. Warm32n remains primary; oracle-assisted stationary-start is an L2-only diagnostic. No replacements, seed changes or extra production.

Subprocess wall total 52.804473s; plus frozen micro 0.210735s. Maximum cell wall 6.706468s. Maximum RSS 84.187500MiB.

|n|burn multiplier|finite ratio|replica SE|finite-G target|consistency|precision|
|---|---|---|---|---|---|---|
|48|8|1.663293819|0.002971998|1.660993330|True|True|
|48|32|1.661448212|0.002773677|1.660993330|True|True|
|48|0|1.661303326|0.002757717|1.660993330|True|True|
|192|8|1.661422047|0.004008628|1.664329089|True|True|
|192|32|1.669033958|0.003327607|1.664329089|True|True|
|192|0|1.669244776|0.004195515|1.664329089|True|True|
|768|8|1.656833855|0.006116663|1.664333052|True|True|
|768|32|1.661345825|0.005966195|1.664333052|True|True|
|768|0|1.662563745|0.004991900|1.664333052|True|True|

All9 ratio comparisons pass the frozen4SE finite-target criterion and all9 pass4SE<=10%target precision. All9 independent arm comparisons are unflagged. This does not prove warm-start convergence, validate arbitrary larger-volume mixing, or make the finite-projector ratio a ground excitation. The exact-start arm removes initialization error in the ideal finite path law but uses finite-precision CDF sampling and an L2 oracle unavailable in a scalable general implementation.

Finite-G targets correspond to total path bonds n and one-sided tau=n/48. Increasing n changes the exact target and observed uncertainty. The n48 target1.660993330 differs from the n768 target1.664333052; no continuous-time substitution or ground-limit identity is silently made. Primary estimates are n48:1.661448212±.002773677; n192:1.669033958±.003327607; n768:1.661345825±.005966195 (one replica SE).

Full chain vectors/covariance and ratio influences are in ANALYSIS.json; every ordered16-batch vector and self/accept/reject/direction-run counter is in cell raw JSON. Batches and individual updates are not independent replicas. DIAGNOSTICS.json adds descriptive lag-one correlation of demeaned ordered batch vectors, not an integrated autocorrelation time or energy ESS. Window traversals count complete runs of accepted shifts, including burn; they are not independent samples or physical round trips.

No all-time raw configuration history was promised or retained in production: the raw objects are all frozen chain vectors, batch vectors and event diagnostics. The micro retains its own step-level series and reconstruction evidence. All permanent preproduction and original six-cell freezes remain unchanged.

This removes branching population bias for the correctly sampled finite path model, not finite projection or path-chain sampling errors. No L4 production/port is authorized by these results. PRODUCTION_FINAL_HASHES.json binds all source, raw, analysis and reports.

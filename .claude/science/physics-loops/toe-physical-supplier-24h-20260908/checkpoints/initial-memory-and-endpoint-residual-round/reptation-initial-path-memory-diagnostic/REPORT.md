# Initial-path retention in the existing L4 reptation data

This diagnostic reads the frozen96 shard files and192 chains only. No new sampler production ran. Every raw file hash is retained in RESULT.json. The production source starts every vertex of its n-bond path at the seed, direction+1, and records accepted-run lengths including burn; every completed run is followed by one rejected attempt, and the unfinished run has no final rejection.

## Exact tagged-path identity

Give initial path vertices tags0,...,n. A newly appended vertex has no original tag. Let u be the unwrapped left endpoint, starting0 and changing by+1/-1 on accepted moves in the current direction; rejection changes direction without changing u. The surviving original tags are exactly the integer interval

 [max_{history} u, n+min_{history} u],

if nonempty. The current midpoint coordinate is u+n/2. Membership in that interval means its tag is still original, so its physical configuration is exactly the initial seed. This is a GUARANTEED subset of seed-valued measurements: newly generated states may also equal the seed. It is not a census of every seed-valued state.

During a run starting at u0 with prior extrema lo,hi, accepted offset t has u=u0+direction*t. The midpoint has an original tag exactly when hi-n/2 <= u <= lo+n/2. The updating extremum in the current direction imposes no additional restriction because n/2>=0. Intersect the corresponding integer t interval with1..run_length and the measurement condition attempt>burn*n. Count a completed run's rejection separately at unchanged u. This costs one interval calculation per run, not one Python iteration per production attempt. First departure from the original span does not imply permanent departure; reversal may bring the midpoint back into the still-surviving span.

The formula was independently compared against literal tagged full paths for every length10 accept/reject history at n2,4,6 (3072 histories). All original-tag midpoint counts, first escapes, final surviving tags and attempt totals agree. All192 production totals exactly equal burn*n+updates, and measured rejection counts exactly match the raw counters.

## Observed retained fractions

| n | burn multiplier | mean measured original-tag fraction | chains retaining any original tags at end |
|---:|---:|---:|---:|
|1536|8|0.0216713|0/32|
|1536|32|0|0/32|
|4608|8|0.2371645|1/32|
|4608|32|0.0208937|0/32|
|13824|8|0.7787097|32/32|
|13824|32|0.4890388|31/32|

The last two cells have original-tag midpoint measurements in every chain. Their fractions range0.5149–0.8807 and0.2581–0.8424 respectively. Thus long nominal projector length did not imply removal of the initialized midpoint configuration during the measurement window.

Across chains in these two cells, Pearson correlations between retained fraction and measured NF are0.99945 and0.99957; correlations with X1 are−0.98550 and−0.98905. These are descriptive correlations of the already observed chains, not independent hypothesis tests or causal-effect estimates. The deterministic tag identity establishes actual initial-segment retention; it does not establish that every discrepancy is caused solely by this retention or that measurements outside the original span are equilibrated.

Median first escape attempts divided by n are3.773,2.878,11.496,10.495,32.605,34.129 for cells0..5. Full per-chain first escape, first measured escape, extrema, final retained span and exact counts are in RESULT.json. In particular a single first-escape flag is inadequate because subsequent returns are possible.

## Actionable limit

The raw data establish a concrete initialization-memory problem at the longest paths. A replacement initialization or extended warmup would need a prospective protocol and independent review; this diagnostic does not authorize replacement production. Retention-free midpoint measurements are a necessary targeted check against this specific defect, not a sufficient mixing criterion. No finite-volume target or photon interpretation is inferred.

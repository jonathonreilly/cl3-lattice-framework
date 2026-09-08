# L8 micro and next gate

Frozen L8 micro completed in7.238711292s,179.71875MiB,530975 actual elementary proposals,4608 signed complex source-update controls. Eight snapshots retained only for this micro. No L16 execution or production occurred.

This wall time includes imports/JIT, exact-rational cap arithmetic, full signed-face controls and compression; dividing it by eight is NOT a production throughput estimate. The honest full-wall extrapolation8192/8*7.239 exceeds7400s per cell and is too crude to justify a900s production job. A warmed proposal/source/Nf timing benchmark is needed before any production authorization. L16 micro remains pending root cost review.

Expected endpoint proposals per origin before clipping are M*sum(1/alpha) over the six responses, plus M origin advancement. At L8 this is approximately31.899495M per origin; at L16 it is approximately99.959498M per origin. These counts are fixed analytically, not inferred from a favorable micro trajectory. Logical coverage remains128x64 origins, four32-chain shards, separately for each burn. No coverage reduction is proposed from results.

Narrow numerical normalization issue exposed by micro: sin(pi/4) floating arithmetic produces matched-harmonic alpha .24999999999999994 etc. The microscopic discrepancy is harmless for this diagnostic, but production should explicitly assign matched-harmonic alpha [.25,.5,1] to meet the literal frozen matched-reference contract. Preserve this micro unchanged; review the explicit exact assignment before production. Minimum-harmonic regulator values remain derived from the implemented qhat². Exact rational cap tests certify the actual implemented binary regulator, not an exact algebraic sine value.

The current implementation is a diagnostic driver, not a production-ready streaming runner. Production must add strict CLI/shard/source binding, per-chain validation/discard and raw chunk receipts before independent review. No sampler closure, stationarity or new physical scaling inference follows from this micro.

# Separate follow-up implementation; no sampling

Copied producer, analyzer, launcher, preflight, runtime, conditional, bridge and geometry from immutable555f calibration. Runtime/conditional/bridge/geometry bytes remain identical to the reviewed cost source. adapt_source.py records the deterministic port, not a runtime dependency; it must not be rerun after freezing.

Changed only four-arm study dimensions, seeds, prior charged cost,256-sweep cadence,16-row batches,128-row paired halves,64-chain covariance through actual vector length,16 shards/arm and all-four acceptance/start contrasts. Same formulas, oracle, initializer and transition implementation. All64 job receipts plus analyzer receipt remain mandatory. Fresh output directories refuse overwrite. Whole-process external receipt remains a launch obligation.

165 deterministic predicates pass under -OO. These include actual analyzer validation of256 rows and nonconstant16-row batching, rejection of wrong shape/NaN/counters/time, full17 covariance/gradient controls, all-four acceptance failures, last-chain measured coverage failures, nearzero denominator handling, exact seed namespace uniqueness/disjointness, and external time/RSS rejection. No stochastic chain, profile, or old production rerun occurred. Synthetic observations are controls only, never physics data.

The prior failed study is neither pooled nor changed. Protocol and forecast remain their pre-implementation frozen bytes. FINAL_FREEZE binds all local files, imported interpreter/module files, and exact external oracle inputs. Source bindings include the prior555f freeze. This is an UNLAUNCHED author package pending root and independent source review.

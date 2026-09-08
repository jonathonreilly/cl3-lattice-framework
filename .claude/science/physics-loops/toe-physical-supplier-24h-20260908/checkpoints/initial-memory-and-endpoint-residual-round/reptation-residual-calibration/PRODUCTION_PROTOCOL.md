# Prospective n2 residual calibration

One logical detunedV=.95 n2 primary cell.32 independent chains,32768 measured attempted updates each,burn64=32n. Seeds202609180000+rep. All-seed/self start,direction+. Exact oracle n2 from frozen micro; no RK control because imported graph Hamiltonian is fixedV=.95. No n48 stochastic extension. Four fixed8-chain shards if needed for resource supervision; no replacement orcoveragechange.

Raw vector(Nf_mid,X_mid,Eavg,hLhR,XmidEavg,Xmid²),16 ordered batches2048updates per chain. All independent-chain vectors and covariance preserved; batches/steps not independent replicas. Targets D,R,correction,VarH,VarX. Nominal oracle consistency |estimate-target|<=4SE. Precision4SE<=25%absolute exact target for correction andVarH;10% for D,R,VarX. These gates are fixed before data. Negative variance estimates remain signed; no bound if a variance is negative, and even nonnegative plug-in bound is not a certified confidence bound.

Cost upper planning estimate from complete .169732s/4096 prior micro:32x32832updates times3 padding plus20s setup≈151s total; four shards each8chains nominal~38s. Proposed180s384MiB/shard,300s aggregate includingprior micro. This is a forecast, not authorization. No new micro. Full imported graph bytes and own source bound before review/launch.

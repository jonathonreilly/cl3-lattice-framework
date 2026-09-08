# Legal propagated-path initialization, with its supplied nonstationary law

The reviewed scalable core6a15d889 is copied byte-identically; the completed production core is untouched. initialize.py first applies128 sweeps of the symmetric RK uniform-face proposal kernel to the seed (one sweep=M geometric proposals). This finite warmup is not a claim of a uniform configuration. Starting from the resulting configuration, it samples n actual Q transitions and records their labels. Only the left, midpoint and right configuration/Nf/Fourier caches are retained alongside the n-label ring.

At V=.95 the row sum of G=I-H/M is b(x)=1+.05 NF(x)/M. Drawing u uniformly on [0,M+.05 NF(x)) and assigning each geometric face unit interval, with all nonflippable and excess intervals self, gives exactly Q(x,y)=G(x,y)/b(x), including geometric multiplicity. There is NO Metropolis accept/reject step during this initial draw. Each nonself label is legal when drawn, so subsequent reconstruction from the left endpoint recovers the same path and midpoint/right caches. It is a valid starting state of the unchanged reptation Markov chain.

If rho is the actual finite-warmup start law, the initialized path law is

 rho(x0) product_{j=0}^{n-1} Q(xj,xj+1)
 = rho(x0) product G(xj,xj+1) / product_{j=0}^{n-1} b(xj).

It is therefore not the desired normalized product-G path law. Even an exactly uniform start would leave the product of b normalizers. The exact864-state L2 n2 uniform-start comparison gives total variation11747593/4118435496>0. This adverse control isolates the path-normalization issue independently of finite RK warmup. Q itself has b-weighted stationary configurations on a connected finite graph, not generally the pure ground distribution.

Deterministic controls6549 pass: full label reconstruction, every accepted move legal, binary degree-three state and plane flux conserved, all three caches recomputed at L2n20 andL4n96. The exact L2 comparison preserves24face multiplicities. No full L4 stationary law or convergence is inferred.

The pre-frozen single L4n13824 micro used seed812913,128RK sweeps, then4096 actual reptation updates with per-step moment measurement. Initialization0.0984s; update/measurement0.08546s; total0.2922s42.56MiB. It drew3610nonself initialization moves. Initial NF caches were52,53,49, so this fixture has no constant seed spine; initial X12 values4.375,3.0625,5.8125 also differ. Final direct cache checks passed. Diagnostic means are retained only as micro outputs, not scientific estimates or calibration targets.

This construction removes the specific deliberately constant initial path. It does not erase all initialization influence, prove equilibration, or authorize a replacement production run. Any production use needs independent implementation review and a prospective comparison of initialization/warmup sensitivity. Memory is O(n) labels plus three O(E) states and fixed geometry, not n full configurations.

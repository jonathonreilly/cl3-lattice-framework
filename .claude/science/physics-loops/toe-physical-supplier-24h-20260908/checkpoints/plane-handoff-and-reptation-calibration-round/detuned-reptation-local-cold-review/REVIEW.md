# Local configuration reptation port: independent review

Disposition: PASS for frozen core.py e52cc8e8a0c3109ccac8f29f74aa8fa4bda9dee6271549e24adc4c0034b3bc79 on the declared L2/L4, V=.95, positive even-n domain. This is a local implementation review, not equilibrium, production precision, ground projection or larger-volume validation. No new stochastic micro or production was run by this reviewer.

Read the full core, microc78f328a7707fdf033c1eb8b6e079446d2ef65211ede195e4b914c4267da2110, preregistration, report07a914a1dff5d863c0a160f393d747db14cf5c4c0c5912b4f706e6357db1b0d1, freeze, raw output and prior exact-graph reference. INPUT_HASHES.json binds the complete files and the absolute reference graph. Earlier exact-graph mathematical and implementation reviews are reused, not counted as a second independent proof of the sampler.

## Transition semantics and ring indices

The n labels represent n bonds, including one aggregate self sentinel, and the three configurations are x0,x(n/2),xn. Plus removes the first label, so the retained reverse-proposal endpoint is obtained by applying that first involution to old x0. Minus applies the last involution to old xn. The proposed new endpoint is not in the acceptance denominator. The numerator/denominator row sums are exactly1+.05Nf/M. The uniform interval[0,M+.05Nf) yields one unit interval per geometric face and all nonflippable/extra intervals collapse to one self. Thus same-destination geometric multiplicity is retained without inventing multiple self-path weights.

On acceptance, plus moves the midpoint over old bond n/2 and minus over old bond n/2-1. The overwritten label and subsequent head change agree with those shifted paths. This remains correct for n2, where the stored configurations are adjacent and index aliases are easiest to mishandle. On rejection states, caches and labels do not change; only direction reverses. An accepted self still shifts the path, so it can change the opposite endpoint and midpoint. The report does not confuse it with a rejected update.

Nf is genuinely recomputed after each nonself cache change. The Fourier increment uses preflip binary state, coeff[:,face]@(1-2x_face), followed by the flip. No imaginary part is discarded. These are exact update formulas subject to floating rounding, not incremental affected-face Nf optimization. No claim of O(1) computational work per move follows: direct Nf scans all faces.

## Independent deterministic evidence

The independent check.py reconstructs geometry by integer vertex coordinates rather than importing geometry from the author. It verifies all192 face lists and1152 complex coefficient entries, using exact fourth roots of unity for L4. It reconstructs all385 states of the saved final path from the actual label history and confirms midpoint/endpoints, direct Nf, full complex O, degree-three ice at every vertex and unchanged staggered planar flux. This tests the preserved component constraints; it is not an enumeration of the full L4 component or its connectivity.

It then executes actual core function bodies on short valid windows from the preserved path. For n2/n4, both directions, every geometric face plus extra self interval, and deterministic accept/reject random values, all9264 transitions match an independently shifted full path and direct cache reconstruction. There are1351 genuine rejected cases. Every resulting label buffer reconstructs its right endpoint. This is deterministic coverage, not new stochastic production. An actual source mutation moving the plus midpoint over the preceding bond fails the cache predicate. RESULT.json and the source preserve all these numbers and the mutation outcome.

The author's one micro additionally reports256 exact-graph L2 same-RNG transitions,4096 L4 literal full-path comparisons and64 label reconstructions. Those reported histories were read, not rerun or inflated into independent counts. My controls use the saved finite path and new deterministic alternatives; the comparison scope is disclosed.

## Fourier and finite-projector target

The coefficient is (-1)^(r1+r2+r3) exp(2pi i r_a/L)/sqrt(L^3) on polarization b!=a. All six ordered direction/polarization channels use h1. At L2 this is real qpi; at L4 it is complex qpi/2. The present core does not include L4h2 qpi, a second harmonic, or a pooled ratio estimator. Such extensions must be explicit and checked against their literal coefficients before claiming matched modes or pooled results.

The frozen dynamics is G=I-H/M with M=3L^3,V=.95, uniform endpoint trial weights and fixed n total bonds. The exact stationary midpoint law is proportional(G^(n/2)1)^2. One-sided time convention is tau=n/(2M), so L4n384 has tau1. It is not an exact exponential propagator. A future energy readout may use -.05 times the average endpoint Nf, with the previously proved finite-G Rayleigh identity; arbitrary endpoint observables are not pure midpoint expectations. The local class currently supplies paths and caches, not any estimator or error bar.

## Domains, imports and production boundary

The implementation's constructor explicitly validates positive even n, but not L. The reviewed physical scope is L2/L4 (and the analytic geometry only extends to appropriate even periodic L); odd L does not provide this staggered seed/periodicity contract, and L1 has repeated-edge degeneracies. A production interface should enforce its frozen even sizes rather than silently advertise arbitrary positive L. No current frozen L2/L4 result is invalidated by this interface limit.

The diagnostic micro has a real external graph.py import by fixed absolute path, disclosed and hash-bound. This is legitimate reference provenance, not portable production closure. core.py itself imports only NumPy/standard library. Before production, freeze a local driver, its exact source dependencies, parameter/seed/initialization domains, readout covariance, failure guards and resource launcher. Remove the exact-graph diagnostic from the production import path or copy/bind any genuinely used dependency. No permission to infer burn adequacy or reuse L2 oracle initialization at L4 follows.

The1.944-second73.094MiB micro includes expensive direct reference loops and a separately stored full path. It is not measured production throughput, nor does its diagnostic memory falsify the local core's three-configuration design. No production resource forecast, uncertainty gate, burn/path-length sufficiency or physical gap conclusion is approved here. No author files or worktree files were changed.

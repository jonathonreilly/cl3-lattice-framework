# Capped L4 detuned energy-response reference pilot — plan only

Frozen proposal, 2026-09-08. No production or microbenchmark is launched by this document. Root reviews the design and independent source checks before scope expansion. This is a reference for a separately designed source-tilted estimator, not a comparison with its as-yet unseen outcomes.

## Fixed physical/model target

Use the existing supplied spin-half ice Hamiltonian H(V)=V Nf-A and unchanged positive population kernel G=I-H/M, M=3L^3, on the mobile component reached from n_a(r)=r_a mod2. Set L4, Volume64, M192. Never enumerate the L4 component or import an exact L4 ground vector. V values are only .93,.95,.97; the center is .95 and energy derivative step h=.02. No secondary derivative stencil initially: the L2 h=.01 stencil increased derivative noise, and a new L4 truncation guarantee cannot be inferred from that observation.

Measure both harmonics with all six momentum-axis/transverse-polarization orientations:

* L4 harmonic2: q=pi, qhat²=4; this matches L2 harmonic1 at the same lattice momentum.
* L4 harmonic1: q=pi/2, qhat²=2; this is a distinct momentum, not a matched-volume continuation or continuum rescaling.

For each harmonic use the SUM of its six pure diagonal structure factors T_h. The pooled moment is qhat_h² [V E'(V)-E(V)]/(64 T_h). Its finite-stencil estimator replaces E' by [E(.97)-E(.93)]/.04. This is a spectral-weight-pooled moment, not a particular orientation's moment or an arithmetic mean of normalized modes. No component cubic-symmetry assumption is required. Use |O|² for complex harmonic1; real-part squaring is incorrect. Mean sources are symmetry diagnostics, not a fitted subtraction.

## Prospective finite controls

Three prespecified groups, eight independent paired replica indices each:

1. P512, projector burn160 sweeps.
2. P1024, projector burn160 sweeps.
3. P1024, projector burn320 sweeps (primary group).

All use20 classical sweeps and the unchanged producer's final40-sweep count window. The population comparison is groups1 versus2 at matched burn. The burn comparison is groups2 versus3 at matched population. There is no P512/burn320 claim. All three V values are run for each group, giving nine cells and72 coupling-specific preparations arranged into24 independent paired energy vectors.

At center V=.95 take four origins separated by3 explicitly seeded unmeasured-chain sweeps. From clones of each origin run F12 andF24 forward C0 suffixes; F24 is primary. Keep both harmonics and all12 mode values. F6 is not inherited as a valid L4 pure-denominator window. Likewise last40-of160/320 energy-window bias is NOT certified by the L2 last40-of80 test. The F12/F24 and burn controls can detect some bias, but passing them is not a convergence proof. Record first/second20-sweep energy-window means and their paired discrepancy, plus all40 samples, not only the mean.

Seeds: group_index0,1,2 follows the list above. Preparation seed=1030000+10000*group_index+replica, identical across the three V values, independent across group/replica. Measurement seed=2030000+100000*group_index+1000*replica+10*origin+forward_index (0 forF12,1 forF24). Origin advance seed=3030000+100000*group_index+1000*replica+origin. Separate seeds and cloned suffixes prevent measurement consumption from redefining the origin chain. Do not count shared seeds across V as independent, or assume that they reduce variance.

Retain joint replica vectors, all raw complex source means/absolute-square C0 sums, energy samples, finite population/ESS/genealogy diagnostics, count/Gauss/flux flags, actual source hashes, and the executed kernel version. Ordinary within-replica origins and orientations are not additional replicas.

## Required independent implementation check before launch

The existing producer already accepts L4 and harmonics(1,2), but that interface alone is not validation. An independent reviewer must compare the literal coefficients to the reviewed RK pilot's actual complex source at every192 link and all12 modes, not just compare squared update sizes. For a fixed preregistered collection of visited configurations and actual flips, check complex O and signed Delta O, geometric plane multiplicity and qhat²/Volume. Wrong staggering, conjugation and plane controls must discriminate where relevant. At q=pi imaginary components vanish; therefore harmonic2 alone cannot test complex harmonic1 handling.

Require identical propagation source/used dependency hashes to the validated L2 route (or exact reviewed deltas), a fixed-seed cloned-source preparation comparison, count updates, and explicit measurement/advance RNG isolation. A pure C0 suffix for complex O uses O(origin)*conj(O(origin)), not O². No source-tilted dynamics, kernel change, new resampling scheme or hidden ground-ratio oracle belongs in this reference pilot.

## Resource forecast and preliminary microbenchmark

Measured L2 baseline:16replica P2048 energy cells cost about3.4seconds including import/runtime, P1024 about1.9seconds; center cells add roughly10.4 and5.2seconds respectively for four origins with F6+F12. Actual total was42.05seconds and133.47MiB maximum RSS. These costs include both propagation and Python measurement overhead and cannot be treated as a universal per-update constant.

Leading propagation work scales approximately P * number_of_sweeps * M; L4 has eight times the L2 M. Applying that scaling to the proposed three groups suggests roughly120–150seconds for their nine preparation cells. Scaling the observed suffix overhead by population/replica counts, doubled F sum and eightfold M suggests roughly100–140seconds more. Imports/JIT and source evaluation can break these estimates; a conservative provisional expectation is250–400seconds, not a performance guarantee. A primary center cell is forecast below90seconds, leaving margin under180.

Before production, execute ONE explicitly capped <=30second microbenchmark only after code review: L4,P128,one replica,V.95,2classical and8projector sweeps plus one pair of cloned F12/F24 suffixes, both harmonics. Use separate timing fields for cold import/JIT, preparation, propagation suffix and observable processing, with a fixed synthetic seed4130000. Its purpose is code/size/cost verification, not equilibration or physics estimation. Preserve the output even if resource or postcondition checks fail. Do not treat its short-run C0 as a physical pilot datum. Extrapolate measured hot workload to each frozen cell and add observed cold overhead plus50% headroom.

Proposed total cap600seconds INCLUDING the30second microbenchmark, each production cell180seconds/384MiB, one BLAS thread. Root must authorize the larger production after reading the actual microbenchmark and independent source review. Do not start a cell unless its predicted capped budget fits the remaining total. If any predicted cell exceeds120seconds after headroom, or total exceeds500seconds, stop at the microbenchmark and return a redesigned proposal for root review; do not silently shrink a frozen group. These forecast gates preserve room for overhead and clean stopping.

## Analysis and stop/escalation rules

Use joint-replica covariance of the three energies and pooled C0 denominator, exactly as the validated L2 estimator. The two harmonics share a kinetic numerator and origins, so their covariance must be retained for comparisons. Report raw E-derived numerator, all orientation S values, harmonic sums and ratio influences. Nonpositive pooled denominators invalidate that ratio; report counts/minima at origin and replica levels without dropping samples.

There is no exact L4 target, hence NO exact-consistency PASS test. A prospective precision diagnostic is4 replica-SE <=10% of the absolute moment estimate, provided numerator and denominator are positive. With only eight replica vectors it is nominal, not a guaranteed confidence interval. Compare population, burn, forward and first/second window shifts with4 appropriate paired/combined SE+1e-8. A detected discrepancy or precision failure is an unresolved-control outcome; no extra seeds, F48, burn doubling or population escalation is automatic. Nondetection is not proof of zero bias.

Preserve energy concavity secants as noisy diagnostics only, not confidence bounds. Without certified energies, or a separate L4 truncation enclosure, the finite-stencil moment remains a reference estimate. Do not attach a rigorous supported-energy upper bound to an uncontrolled stochastic ratio.

Stop on resource failure, source/update mismatch, invalid postconditions, lost frozen cells or failed instrumentation. A physical difference between L2 and matched-q L4 is NOT a failure criterion. Compare q=pi finite-volume estimates with full uncertainty/control caveats; report q=pi/2 separately. No exponent, photon, pole, residue, gap lower bound, thermodynamic phase or physical electromagnetic identification follows from this pilot.

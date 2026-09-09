---
claim_id: star_tick_record_law_determinantal_rotated_kernel_second_reading_priced_2026_09_05
claim_type: bounded_theorem
claim_scope: "Supplied finite real bipartite hopping and outcome-independent Born/unitary schedules: final law is a rotated rank-N projection DPP with uniform edge fibres. Complete cube order census at three dwells and declared slab/torus families. Finite-grid time diagnostics, local-fit upper bounds and static response to a supplied dressing; no adaptive single-kernel theorem, mixture no-go, time limit, event-rate law or physical gravity derivation."
upstream_dependencies: [minimal_axioms]
runner: scripts/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py
---

# Fixed-schedule star ticks have rotated determinantal laws; finite order, time and static-response diagnostics

**Date:** 2026-09-09 correction of the dated original source.
**Type:** bounded_theorem. **Audit:** unset; the owner has deferred formal audit.
**Primary runner:** [star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py](../scripts/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py).
**Runner cache:** [current source-bound execution](../logs/runner-cache/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.txt).
**History:** [dated correction and exact original bodies](../.claude/science/physics-loops/ticks-correction-20260909/CORRECTION_RECORD.md).
The original filename and identifier are recovery keys; the current title and scope above are authoritative.

```yaml
actual_current_surface_status: bounded-support
trace_class: frontier_discovery
artifact_role: theorem
reachability_to_target: unknown_frontier
next_trace_action: "Keep the supplied finite results and the named unresolved physical and classification obligations distinct."
```

## Supplied model and current boundary

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select a Hamiltonian,
Born probabilities, tensor composition, formation unit, schedule, dwell, or time/readout law.
Here all of those are declared conditions. Record permanence is respected by removing
recorded-edge flips; it does not derive the chosen process or assign a scalar to absence.
No historical parent status or scalar Record-additivity supplies authority.

There is one qubit at each edge of the declared coarse graph. The superfast encoding has
`B_v = product_(e in star(v)) Z_e`, `n_v=(1-B_v)/2`, face stabilizers `S_f=+1`,
`T_ij=(i/2) A_ij(B_i-B_j)` and `H=-sum_e eta_e T_e`, with `t=1`.
The real signs are `eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y)` and the stated boundary twists.
They give pi flux on the faces checked by the runner. The reference state is the chosen
code-space Slater sea of the specified filling; it is a supplied reference, not a derived physical vacuum.
An event projects newly recorded edges in the Z basis with Born odds, followed by
`exp(-i tau H_R)`. On the full record block, `H_R` retains only unrecorded-edge hops.
This full block need not be the original loop-code subspace. Fixed records commute with later dwells.

## T1: exact fixed-schedule record law

Fix an outcome-independent ordered schedule of edge sets. Let R_j be its cumulative
recorded edges and let `G=product_j exp(-i tau_j h_(R_j))`, with later factors on the left.
The initial code sea has occupied orbitals W, `P=WW†`. Every Z projector on previously
recorded edges commutes with all later dwells. Moving them to the left collapses the
branch amplitude to `P_w U|sea>`, where U is the product of the quadratic dwells on
the unconditioned initial code and acts there by the one-particle G.
Thus `K=G P G†` is a rank-N orthogonal projector and

`P_pi(w)=2^-g p_K(Aw)`, `g=|E|-rank_F2(A)`,

`p_K(n)=det(diag(n)K+diag(1-n)(I-K))`.

A is the corner-edge incidence over F2. Uniform edge fibres follow from the same code
syndrome expansion as for the original sea. The formula is a **complete pattern law**;
`det K_SS` alone is the occupied-only marginal. Branch odds are its ordinary conditioned
marginals. A1 and B3 compare this construction against the actual many-body cube and
slab calculations. This result is conditional on the supplied encoding and Born instrument.
It does not say that one global G exists for a schedule chosen from previous outcomes;
the greedy adaptive policies of #7947 are outside that theorem.

## T2: full cube order census at three dwells

B1 preserves all `8!=40320` orders at `.1,.5,2`. At each declared dwell 1440 orders
have TV below `1e-12`: 576 even-first, 576 odd-first and 288 others.
At `.5` the support sizes are 1984/2112/2176/2240; the zero histogram is
`[25536,0,9792,0,2976,0,0,0,2016]`. Uniform-order mixtures have TV
`.009854703/.145430031/.237998278` at the three dwells and support 2240 at the stated cutoff.
The equal order weights are supplied; the process does not choose them.
A prefix eigen-set condition supplies sufficient preserving schedules, using the
[corrected regular-set criterion](THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_OF_THE_SUPERLATTICE_ROLE_PATTERN_THE_EIGEN_SET_CRITERION_IS_ONE_PARTICLE_AND_ITS_MINIMAL_SETS_ARE_THE_PARITY_CLASSES_BOUNDED_NOTE_2026-09-04.md). It is not necessary for an
arbitrary final law, and a failed prefix alone does not exclude eventual cancellation.
The classification above is the actual finite census at the three dwells.

## T3: finite time and slab diagnostics

B2 retains the six small dwells and their log-ratio exponents near two, and the
`.01/.03` uniform-order comparisons. These are finite fits, not a proved small-time
asymptotic coefficient. Support 2240 is checked at `tau=1e-3`, not at every positive tau.
The 400-point grid `tau=.5+.25j` has the reported oscillations and averaged-law TVs
`.199223` and `.214374`. That finite-grid average is not an infinite-time Cesaro limit,
and observing the last 100 points does not prove nonconvergence at infinity.
The alternative null convention changes the `.5` uniform-order TV from `.145430031`
to `.154022`, with 10368 orders encountering a null event before full coverage.

B3 checks 28 declared slab orders at `.1,.5,2`, all with nonzero TV there.
It does not exhaust `12!` orders. At `.5` the range is `.032625–.486099`, and its
family average `.345484` has support 473088. The four many-body star-order comparisons
and the six-edge comparison retain their original probability and energy values.
The prefix criterion uses both occupied-row rank and surviving orbital rank; failing
it remains a failed sufficient test, especially for irregular record closures.

## T4: supplied Born structure and finite menus

C1 walks the four declared cube Born trees above its live cutoff. It compares every
retained event with the conditioned final fixed-order law; counts are
2793/2889/521/2953. Born agreement tests two constructions **given Born weights**,
not derivation of those weights. The linear menu equations share grades only within
the declared unit-size frame. A rank gap rules out a single normalized grade on that
particular pooled family; it is not a contradiction in the per-state Born probabilities.
C2 retains all conditions with at most nine previous records for its three cube laws:
nearest-edge odds remain one half and the menus are the same three subsets of the
binary record basis. No new effect direction or physical readout is supplied.

## T5: disturbed kernels and mixture fits

D1 retains rank-four projection kernels for seven fixed cube orders, their changed zeros,
energies and residuals. The two declared second-round pair schedules move disturbed
laws by `.295792/.340817` while leaving the sea within roundoff.
This is not a claim that no unit preserves them: recording **all** edges at once leaves
`H_R=0`. Q1 checks that full-record counterexample through the actual schedule function.

D2 preserves the five-start local optimization and its attained TVs
`.068765/.090499/.047305`, along with the single-order control below `1e-9`.
These values are **upper bounds** on the global best fit. They do not establish a
positive lower bound or prove that the mixture is no single Slater/DPP law.
For a standard Hermitian contraction DPP, fixed particle number would force a projection
kernel because `Var N=Tr(K-K²)=0`. No equivalence with every Pfaffian or Gaussian law
is asserted. Exact mixture classification remains open.

## T6: massless static response to a supplied dressing

For real bipartite h with no zero mode at half filling, epsilon h epsilon=-h gives
`epsilon P epsilon=I-P`. Each real edge-deleted exponential obeys
`epsilon G epsilon=conjugate(G)`, hence
`epsilon K epsilon=I-conjugate(K)`. In particular `K_vv=1/2`.
Same-sublattice off-diagonals are imaginary and cross-sublattice ones real, so triangle
products have zero real part. These identities survive each fixed schedule; the linear
identities for statistics also survive a supplied order mixture. They do not imply a
mixture has a single projection kernel.

The response calculation differentiates both P and G with respect to the supplied
endpoint-mean real hopping modulation
`delta h_(v,v+b)=-h_(v,v+b) gamma_bb [exp(ik.v)+exp(ik.(v+b))]/4`,
where gamma is the supplied metric-polarisation tensor and h is the hopping matrix.
It measures derivatives of `K_vv` and connected pairs `-|K_uv|²`.
The TT columns use the declared continuum-k transverse-traceless basis.
This is a static linear response map, not propagating gravitational dynamics.
Shear columns vanish because that particular axis-bond dressing contains no shear.
Q2 compares the implemented Frechet derivative against an independent finite difference
on a bounded cube fixture and verifies the bipartite diagonal identity.

E1's `4^3` massless sea ranks are `[1,1,2,1,1]`, while the disturbed ranks are
`[1,1,2,2,2]` at its five momenta: **the pattern changes** at the last two momenta.
E2's six-momentum `6^3` ranks agree at `[1,1,1,2,2,2]` for the declared reduced family,
with changed amplitudes. The 4-cube response uses 48 orientations plus the analytic
64-translation reduction checked at the declared momentum; the 6-cube response uses
the 27 even-translation reduction with two explicit translated controls.
All actual arrays, singular values and E3 energies/kernel distances remain in the cache.
The unbound historical 1296-order scratch quotation remains only in the archived original;
it does not support a current claim. The comparison here is massless-to-massless;
the older #7951 massive site channel is not the same cancellation test.

An unchanged one-time occupation probability is not an unchanged event intensity.
No event-time distribution, clock observable or rate estimator is supplied by this runner.
The S1 sharing rule quoted historically from #7974 counts repeated endpoint events;
a schedule that permanently records each edge once does not implement those repeated
counts. A later Z re-registration leaves the same content but does not derive a counting
process. The Regge action, Euclidean/OS0 reading, worldline coupling, rate law and
record-to-geometry bridge of that historical chain remain separate conditions; they are
not conclusions of the static response above. No physical ruler or photon/gravity claim lands here.

## Evidence and unresolved alternatives

All original 12 IDs A1/B1–B3/C1–C2/D1–D2/E1–E3/F1 and numeric payloads remain.
Q0 binds the own note, current memo and the corrected criterion note; Q1/Q2 are the
bounded actual full-record and derivative controls. The final cap is 150 seconds and
observed RSS is bounded at 2 GiB. Floating cutoffs and finite order/momentum/grid families
are part of the protocol; no infinite-volume, all-time or continuum extrapolation is certified.
N1–N8 leave other schedules, adaptive outcome dependence, other dwell choices, full joint
formation and alternative physical time/readout suppliers open. These are not five
independent closed walls, and the two historical interpretive horns are not exhaustive.
No parent proof campaign, reserved source, status label or audit result is imported.

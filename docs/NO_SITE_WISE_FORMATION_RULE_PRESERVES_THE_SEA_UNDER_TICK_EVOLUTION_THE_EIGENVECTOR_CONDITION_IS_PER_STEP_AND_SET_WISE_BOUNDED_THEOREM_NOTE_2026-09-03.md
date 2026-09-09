---
claim_id: no_site_wise_formation_rule_preserves_the_sea_2026_09_03
claim_type: bounded_theorem
claim_scope: "Supplied finite pi-flux Hamiltonian, ordinary edge-qubit composition, half-filled code sea, Born conditioning and unitary dwell. Six declared greedy policies and 24 fixed cube orders are evaluated at declared dwells; slab trees stop at six records. Eigenvector branches give a sufficient preservation condition, with explicit joint-star witnesses. No universal site-wise, rate, mixture, or necessity theorem."
upstream_dependencies: [minimal_axioms]
runner: scripts/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py
---

# Declared site-wise tick policies disturb the finite sea; eigenvector branches and joint sets provide sufficient preservation

**Date:** 2026-09-09 correction of the dated original source.
**Type:** bounded_theorem. **Audit:** unset; the owner has deferred formal audit.
**Primary runner:** [no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py](../scripts/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py).
**Runner cache:** [current source-bound execution](../logs/runner-cache/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.txt).
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

## Definitions and finite protocols

The cube has 8 corners, 12 edges, a 128-dimensional initial code in 4096 record patterns,
and sea energy `-4 sqrt(3)`. The open `2x2x3` slab has 12 corners, 20 edges,
a 2048-dimensional code and sea energy `-(8+2 sqrt(2))`.
Its conserved `N=6` record-pattern sector has 473088 basis states.
Full-law TV means one half the L1 distance on every edge outcome, including the unformed
edges registered jointly at the end. Leaf-TV observes only the already formed edges.

For free edge q, `eps_q=<h_q>`. A1 maximizes `max(eps_q-eps_q(sea),0)`;
A1v uses the mean endpoint excess with `eps_v=(1/2)sum_(e in star(v)) eps_e`.
A2 maximizes `|eps_q|`, A2v its corner form, B maximizes the one-qubit purity,
and E minimizes the Born-weighted residual after the proposed next record.
Ties use the lowest edge index after rounding scores to `1e-9`.
These are deterministic greedy policies. The printed normalized A-scores are possible
stochastic odds along those paths; the stochastic policies themselves are not integrated.
E is defined even when its best residual is positive; zero residual is an extra property.
C is the 24 cyclic/reverse cube orders, with the identity prefix used on the slab.
D forms whole declared corner stars jointly. The cube has dwells `0,.1,.5,2`;
slab runs use `0,.5,2` only at the groups/depths named below.

## T1: no dwell, and a sufficient preservation proof

Without a dwell, the products of conditional Born probabilities telescope to the
reference distribution for every completed adaptive decision tree that chooses only
unformed edges. Thus this boundary does not test a formation-rate rule.
A2 checks all declared cube policies/orders at `tau=0`: TV below `1e-12`, support 1984.
The A1 energy scores are uniform at the five reported steps of that finite cube protocol.

A sufficient condition with dwell is that every nonzero branch `P_w|sea>` is an
`H_R` eigenvector. Induction then leaves only a branch-dependent phase before the next
projector; it cannot change later Born odds. This is a sufficient per-prefix condition,
not necessary for a final law to equal the sea and not a classification of all preserving policies.

## T2: cube results for the declared policies

A3–A5 retain the complete 4096-pattern computations. At `tau=.5`, TV for
A1/A1v/A2/A2v/B/E is `.337565692/.320717027/.422413255/.449953329/.453896665/.362827766`.
The 24 fixed orders range `.289380397–.456208220`, with mean `.379401338`;
their equally weighted mixture has TV `.239288631`.
Their support is 2240 at the declared threshold, compared with the sea's 1984:
1856 charge zeros remain and all 256 sea cancellation zeros acquire positive weight.
The added census guard checks every actual order, rather than inferring this from its average.
D preserves the law within `1.2e-15` across the three positive dwells.
At `.1` the fixed-order range is `.0459–.2990`; at `2` it is `.3272–.5243`.
A factor below 1.6 compares extrema only for the declared `.5` fixed orders.
It does not bound the other dwells or all policies.

A convex mixture of these computed laws with positive weight on a component having a
sea-forbidden outcome retains positive weight there. This elementary nonnegative-sum
argument is confined to the laws whose weights/support are actually supplied.
It supplies no complete stochastic greedy-policy law or universal site-wise no-go.

## T3–T4: slab, marginal blindness and greedy scores

B1–B5 keep the seven declared slab policies through six records. At `.5`, full-law TV
after one is `.1148/.1148/.1259/.1387/.1259/.1259/.1148`, and after six is
`.3727/.2116/.3895/.4089/.3431/.3167/.3156` for A1/A1v/A2/A2v/B/E/C.
The leaf-TV is below `7.2e-14` through three records; A2/A2v retain that small leaf-TV
through six despite their full-law disturbance. These are different marginals.
The printed contrasts and greedy odds quantify these selected paths, not a physical event rate.
A1 selects the parallel z matching first. A2v has the largest six-record full-law TV
among this declared family, `.4089`. B2 retains the separate `tau=2` dwell A1/C controls.

## T5: eigenvectors, invariant diagonals and the scanned domain

For a fixed finite H with spectral amplitudes c_k, a vector has constant Z-diagonal
for all real times iff, for each z and nonzero energy gap Delta,
`sum_(E_k-E_l=Delta) c_k conjugate(c_l) <z|k><l|z> = 0`.
This follows by grouping the finite Fourier sum for each outcome probability.
It does not require the vector to be an eigenvector: `H=diag(0,1)` and
`psi=(1,1)/sqrt(2)` have residual `1/2` and constant probabilities `(1/2,1/2)`.
Q2 executes this counterexample. It is a counterexample to an unrestricted inference,
not a claim that this H is the stipulated lattice Hamiltonian.

A7's 12 declared trees find zero invariant-diagonal non-eigenvector nodes at their
sampled dwells among 27848 nodes, and zero displaced eigenvector nodes among 40672.
Those finite displacements do not prove an all-time necessity or prohibit later recovery.
A8 explicitly finds an eigenvector site on E's cube path at step 9; its first seven
best residuals exceed `.496`. B4 checks only slab steps 1–6 (`.5638–.7354`).
There is no assertion that every site fails at every later step.

## T6: useful joint-unit witnesses

B6–B7 keep all 64 outcomes of the slab pair `star(0) union star(2)`.
Each degree-3 star alone has residual `(sqrt(2)-1)/2`; their joint six-edge projection
has residual below `2.1e-15`, and its `.5` dwell gives full-law TV `3.6e-16`.
The same six edges in the declared individual sequence give `.3156`.
The two degree-4 stars `star(4),star(7)` also preserve the reported law.
These witnesses establish useful supplied units; they do not exhaust alternatives.

## Evidence and open obligations

All original A1–A8/B1–B8 IDs and numerical targets remain. Q0 binds the note and current
memo; Q1 checks the actual per-order census; Q2 checks the non-eigenvector diagonal control.
The runner is deterministic floating point with explicit live/support thresholds `1e-13`
and a Chebyshev coefficient cutoff `1e-17`, not an exact-arithmetic probability certificate.
The 150-second final cap and observed RSS are reported separately in the execution receipt.
No unchanged original baseline is repeated. Exact original sources and caches remain dated history.

N1–N8 boundary: different adaptive policies, selected dwell times, non-eigenvector diagonal
invariance, other joint units and other between-event processes remain open alternatives.
These are possible routes, not five executed exclusions or independent walls.
The eigenvector proof is sufficient; the numerical failures share the supplied Hamiltonian,
Born weights and schedules. No residual is promoted to a general impossibility, no rate or
unit is axiomatically forced, and older tick/relaxation or ruler claims receive no inherited approval.
The current correction supersedes the historical universal wording without deleting its data.

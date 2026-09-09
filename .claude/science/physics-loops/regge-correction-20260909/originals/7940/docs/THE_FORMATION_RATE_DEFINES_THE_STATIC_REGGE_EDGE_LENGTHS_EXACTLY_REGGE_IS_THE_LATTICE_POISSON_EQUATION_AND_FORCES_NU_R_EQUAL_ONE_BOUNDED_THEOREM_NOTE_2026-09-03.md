---
claim_id: formation_rate_defines_static_regge_edges_exactly_2026_09_03
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on the supplied objects named in Setting -- the Regge action S_R = sum_t A_t delta_t on the landed 4D cubic-Coxeter complex T(Z^3 x Z_tau), its orientation and a coefficient G; the Euclidean/OS0 reading; the tick identification l_tau = l_0 r_v/r_0; the worldline coupling S_m = m sum l_tau; the rate law r_v = r_0 (1 + Phi_v) with kappa_r = 1 inherited as a condition from the formation-rate ruler chain (open PR #7925, not on origin/main); and the endpoint-mean edge rule -- at linear order, for static sources, on the 8^3 spatial torus at k_tau = 0, on the periodic 3^4 box, and at the declared momenta, and nowhere else: (T1) the copied second-variation operator and metric map reproduce the landed bloch_Q and metric_map to 9.2e-16, and 4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2) puts exactly two propagating modes on shell; (T2) with nu_r = 1 the rate-induced edge field h_1 = Phi (-2,-2,-2,+2) satisfies M_AM^dag Q M_AM h_1 = -khat^2 e_tt and Q M_AM h_1 = -2 khat^2 e_tau to 5.4e-15 at every declared static momentum, so the linearised Regge equations on the rate-induced geometry ARE the 6-NN lattice Poisson equation on the temporal edges and the 14 other edge classes drop out; (T3) the residual is affine in nu with tt slot -nu khat^2 exactly and (nu - 1) coefficient the anisotropic-stress operator c Q_EH, c = -1/2, at O(k^2), nonzero at every declared momentum: nu_r != 1 fails exactly; (T4) a pure worldline source lies in range Q(k), dim ker Q(k) = 5, and the exact lattice solution equals the rate field with M = sigma/2 after zero-mode projection, to 2.1e-16 at every torus site; (T5) the landed line-average rule is not exact (residuals 7.1e-3, 0.48, 4.5, 2.7e-9; source coefficient 0.90025) while the endpoint mean is (1.00000); (T6) a time-dependent rate ansatz is not a vacuum solution, and the rate direction has zero overlap with both TT polarisations, spans 1 of the 6 physical metric degrees of freedom and is not annihilated on shell; (T7) the landed nonlinear box action second-differenced along the rate-induced field gives -243.000674 against the Bloch -243.000000 and the identity's -243.000000. Nothing about the propagating sector beyond its non-overlap with the rate direction; no nonlinear closure; nothing supplied is derived."
upstream_dependencies:
  - docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md
runner: scripts/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py
---

# The formation rate defines the static Regge edge lengths exactly: the linearised Regge equations of the 4D cubic-Coxeter complex are the bridge's lattice Poisson equation and force `nu_r = 1`; the propagating modes are not rate fluctuations

**Date:** 2026-09-03
**Type:** bounded_theorem, explicitly conditional on the supplied action, orientation and coefficient, the OS0 reading, the tick identification, the worldline coupling, the rate law with `kappa_r = 1`, and the endpoint-mean edge rule
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:** [`scripts/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py`](../scripts/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py) (PASS=13 FAIL=0)
**Runner cache:** [`logs/runner-cache/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.txt`](../logs/runner-cache/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.txt)
**Parents:** in the dependency sense, only the landed 3+1 tick-extension row whose runner module is imported (listed above). The four notes this builds on are open PRs, not on `origin/main`, and are quoted in "Setting" as conditions: `THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7910), `THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7916), `A_FORMATION_RATE_RULER_EVADES_THE_SEAS_SUBLATTICE_CANCELLATION_AND_THE_BRIDGES_CONSTANT_MODE_FIXES_KAPPA_R_EQUALS_ONE_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7925), `THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7905).

Two open lines of the gravity lane ended, separately, at one supplied object each. The formation-rate ruler chain reduced the spatial half of the weak-field metric to a single supplied exponent, in the ruler note's own words "*the coarse hop amplitude is proportional to the first power of the rate at which the bond's endpoints register records*" (`nu_r = 1`), with `kappa_r = 1` fixed by the bridge's constant mode. The graviton note found a native linearised graviton in the second variation of the Regge action on the 4D cubic-Coxeter complex, on "supplied 0/1-vector edge lengths", and listed "the record-to-geometry link" as supplied: "nothing here derives edge lengths from what records register." This note puts the two together. It asks whether the rate field can *be* the edge lengths, plugs the rate-induced edge-length field into the landed second variation, and finds three things. For the static sector the answer is exact: the linearised Regge equations of the complex, on the rate-induced geometry, are the 6-NN lattice Poisson equation on the temporal edges, with every diagonal edge class dropping out. The spatial exponent is not supplied at all: the vacuum Regge equations force `nu_r = 1`. And for the propagating sector the answer is no: the two graviton polarisations have zero overlap with the rate direction, so the record count that fixes the static geometry reads none of the freedom the graviton lives in.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Machine-exact linear-order identities on one declared complex at declared momenta and on finite tori at declared sizes, every statement conditional on the supplied objects named in Setting; nothing supplied is derived."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Route to the gravity lane: the static half of the record-to-geometry link is one exact identity (rate field = temporal edge lengths; linearised Regge = lattice Poisson) with the spatial exponent forced, and the propagating half needs a direction-dependent edge-length freedom no record count yet reads, a per-bond record rate being the untested candidate. Run independent audit."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's checks `T1`-`T7`: `T1` provenance and the dispersion witness; `T2` the exact identity at declared incommensurate static momenta and in position space; `T3` `nu`-linearity and the forced exponent; `T4` the worldline source in `range Q(k)` and the exact solution equal to the rate field; `T5` the edge rule; `T6` the time-dependent ansatz and the propagating modes; `T7` the end-to-end check against the nonlinear action. Every statement is `[exact]` at `1e-12` unless it is a lattice-continuum comparison, which is tagged `[O(k^2)]` with its measured deviation.

## Imports and authority

Imported scientific authority: none load-bearing. Regge calculus, the Euclidean linearised Einstein pairing, the lattice Green's function of the 6-NN Laplacian and the Bloch decomposition are standard methodology. The runner imports one landed module from `origin/main`, the 3+1 second-variation runner `scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py` (declared in `AUDIT_INPUT_PATHS`), for the complex, the edge and hinge classes, the area and dihedral derivatives, `bloch_Q`, `metric_map`, `einstein_pairing_4d` and the nonlinear `box_action`; it imports nothing from any unmerged branch. Every other helper is copied into the runner and labelled with the probe function it reproduces; the copied operator is pinned against the landed one in `T1` before it is used.

## Setting

The four framework axioms are quoted, not amended, from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: each site has a domain of local possibilities. **Admissibility**: one fixed nearest-neighbour rule, covariant under translations and proper cubic rotations. **Record**: "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone." The 6-NN adjacency of the Lattice axiom is the adjacency whose Laplacian appears below; the tick is the emergent record tick, and the complex is the landed tick extension `T(Z^3 x Z_tau)` of the six-tetrahedra spatial chain.

**Condition one -- the action and the complex, quoted from the graviton note (open PR #7910).** Its claim scope: "On the 4D cubic-Coxeter (Kuhn/Freudenthal) path complex T(Z^3 x Z_tau) with flat Euclidean/OS0 background and supplied 0/1-vector edge lengths (l^2 in {1,2,3,4}), the second variation of the Regge action S_R = sum_t A_t delta_t about flat has, at every declared momentum: dim ker Q(k) = 5"; its comparator `Q_h(k) = c Q_EH(k) + O(k^4)`, `c = -1/2`; its dispersion `4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2)`; and its table of what stays supplied, verbatim: "edge lengths as the geometric variables | supplied" and "the record-to-geometry link | supplied; nothing here derives edge lengths from what records register." The action, its orientation (the one in which the four massive non-metric branches are positive) and the coefficient `G` are supplied here exactly as there.

**Condition two -- the rate law, quoted from the ruler chain (open PRs #7905, #7916, #7925).** The declared two-weight family `H(alpha, beta) = sum_bonds [1 + alpha (Phi_v + Phi_j)/2] M_vj + sum_v [1 + beta Phi_v] m eps_v n_v`; the rate dressing `(1 + Phibar) g(r_v, r_j)/g(r_0, r_0)` with `g` homogeneous of degree `nu_r`, giving `alpha = 1 + kappa_r nu_r`, `beta = 1`; the constant-mode argument fixing `kappa_r = 1`; and the single object the ruler note leaves supplied, verbatim: "What remains supplied is not a coefficient but a single exponent, `nu_r = 1`: *the coarse hop amplitude is proportional to the first power of the rate at which the bond's endpoints register records.*" The rate law `r_v = r_0 (1 + Phi_v)` with `kappa_r = 1` is taken here as a condition, together with everything that chain is conditional on (the designed fermion law, the half-filled staggered sea as vacuum, the bridge `phi = G0 P0 rho` of [`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md) at linear order). The bending factor `alpha/beta = 1 + nu_r` is the light-bending note's exact transverse corollary.

**Condition three -- the tick identification and the worldline coupling, declared here.** Proper time at `v` during one global tick is the number of records registered there per tick, `r_v/r_0`; the temporal edge of the complex at `v` has length `l_tau(v) = l_0 r_v/r_0 = l_0 (1 + Phi_v)`. A point mass couples through its worldline, `S_m = m sum_{worldline} l_tau`, and the Euclidean action is `S_E = -S_R/(8 pi G) + S_m`. Both are declared; neither is derived.

**Condition four -- the edge rule.** The records "along" an edge `(v, v + w)` are counted as the mean of the two endpoint counts, `Phibar_e = (Phi_v + Phi_{v+w})/2`, the same rule the ruler chain uses for its bond dressing. Theorem 5 shows this is the rule that makes the identity exact and that the landed line average is not; that "record count along an edge = endpoint mean" is a reading is said again in "Reading, not theorem".

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly numbered runner check. `P0`, declared here and conditional: the four conditions above. `P1` (`T1`): the copied operator is the landed one. `P2` (`T2`): the exact identity, using `P1`. `P3` (`T3`): linearity in `nu` and the tidal coefficient, using `P2`. `P4` (`T4`): solvability and uniqueness up to zero modes, using `P2`. `P5` (`T5`): the edge rule, using `P2`. `P6` (`T6`): time dependence and the propagating modes, using `P1`. `P7` (`T7`): the nonlinear action, using `P2` and the landed `box_action`. The strongest supported scope is precisely `P0`-`P7`.

## Definitions

The **complex** is the landed `T(Z^3 x Z_tau)`: 24 path 4-simplices per 4-cell, 15 edge classes (the nonzero 0/1 vectors `w` with `n_s` spatial and `n_t in {0, 1}` tick components, flat length `l_0 = sqrt(n_s + n_t)`), 50 hinge classes. `Q(k)` is the `15 x 15` Bloch Hessian of `S_R` about flat. Metric components are ordered `xx, yy, zz, tt, xy, xz, xt, yz, yt, zt` (tick = index 3). Two **metric maps** send a metric perturbation `h e^{ik.x}` to the 15 edge-length responses `(w^T h w)/(2 l_0)` times a phase: the landed **line average** `M_line` with phase `e^{i k.w/2} sinc(k.w/2)`, and the **endpoint mean** `M_AM` with phase `(1 + e^{i k.w})/2`. The **rate direction** is `h_nu = Phi (-2nu, -2nu, -2nu, +2, 0, ...)`, the Euclidean `h = 2 Phi diag(-nu, -nu, -nu, +1)`: it is the one-scalar edge field `delta l_e/l_0 = Phi (n_t - nu n_s)/(n_t + n_s)` on all 15 classes (`-nu Phi` on every spatial class, `+Phi` on the temporal class, `(1 - nu) Phi/2` on the tick-axis class, and so on), which is what "temporal edge `l_0 (1 + Phi)`, spatial edge `l_0 (1 - nu Phi)`" means on the diagonal classes at first order. `khat^2 = sum_i 4 sin^2(k_i/2)` is the symbol of the 6-NN lattice Laplacian, `nabla^2_lat e^{ik.x} = -khat^2 e^{ik.x}`. The **static source** is a unit point mass on the `L^3` torus, `Phi(k) = -M/khat^2` with `M = 1`, `Phi(0) = 0`, so `nabla^2_lat Phi = M (delta_x0 - 1/N)`. The **residuals** are `E = Q M h_nu` (edge space) and `E_h = M^dag E` (metric-projected); `Q_EH(k)` is the landed Euclidean linearised Einstein pairing. The **declared static momenta** are `k = (0.37, -0.81, 0.22)`, `(1.9, 0.4, -2.3)`, `(2.9, 2.7, -3.0)`, `(0.013, 0.007, -0.02)` with `khat^2 = 0.80455, 6.137, 11.73, 6.18e-4`; no random number appears anywhere.

## Theorem 1 -- provenance: the operator here is the landed one

**Conclusion.**

1. The copied trig-polynomial Hessian and its holomorphic continuation reproduce the landed `bloch_Q` at the declared real momentum to `9.2e-16`; the copied line-average map reproduces the landed `metric_map` to `2.2e-16`; the quadratic-form recast of `einstein_pairing_4d` reproduces it to `6.9e-18`.
2. **The dispersion witness.** At `k_tau = i omega` with `4 sinh^2(omega/2) = khat^2` the continued Hessian has nullity exactly `7` (the 5 kinematic modes plus 2 propagating ones) and nullity `5` at `1.05 omega`, at the three declared spatial momenta: `|k| = 0.5` on the axis (`omega = 0.4899`, largest null value `8.0e-17`, smallest non-null `7.6e-3`), `|k| = 1` on the body diagonal (`0.9500`, `1.4e-16`, `3.1e-2`), `|k| = 2` along `(2, 1, 0)` (`1.6054`, `8.5e-17`, `7.2e-2`).

**Proof.** Item 1 differences the four objects at `k = (0.41, -0.23, 0.67, 0)` and `(0.3, -0.2, 0.5, 0)`. Item 2 evaluates the continued Hessian at the closed-form `omega = 2 asinh(khat/2)` and counts relative singular values below `1e-10`. `[exact]`

## Theorem 2 -- the exact identity: linearised Regge on the rate-induced geometry is the lattice Poisson equation on the temporal edges

**Conclusion.** With the endpoint-mean rule and `nu = 1`, at every declared static momentum,

```text
M_AM^dag Q(k) M_AM h_1 = -khat^2 e_tt        and        Q(k) M_AM h_1 = -2 khat^2 e_tau ,
```

with worst residuals `4.6e-15` and `5.4e-15` (absolute, `khat^2` up to `11.73`), and the residual on the 14 non-temporal edge classes at most `5.4e-15`. Since the identity holds at every `k` and is linear, it holds for every static potential: for any `Phi(x)`, `(Q delta l_rate)_e(x) = -2 (nabla^2_lat Phi)(x)` on the temporal edge at `x` and `0` on every other edge. On the `8^3` torus with the unit point mass this reads `(Q delta l_rate)_tau(x) = 2M (delta_x0 - 1/N)`, checked at every site to `1.3e-16` (value `1.996094 = 2 - 2/512` at the source) with every other class at most `2.8e-16`. The linearised Euler-Lagrange operator of the Regge action, evaluated on the static isotropic rate-induced geometry, is the 6-NN lattice Poisson operator on the temporal edges. The face, body, tick-face and tick-body classes -- constructions of the triangulation, not adjacencies of the Lattice axiom -- carry their first-order lengths from the same scalar and drop out of the equations.

**Proof.** Direct evaluation at the four declared momenta, then on all 512 torus momenta with an inverse FFT to position space; the source coefficient `2M` per unit temporal edge length is `M` per unit `h_tt` (`d l_tau/d h_tt = 1/2`). `[exact]`

## Theorem 3 -- `nu_r = 1` is forced

**Conclusion.**

1. `E_h(nu)` is affine in `nu`: `E_h(0) + E_h(2) - 2 E_h(1)` vanishes to `7.1e-15`, and its `tt` slot is `-nu khat^2` exactly (to `1e-12`) for `nu = 0, 1/2, 2` at every declared momentum. The temporal equation is the Poisson equation for every exponent; the exponent enters only the spatial equations.
2. The coefficient of `(nu - 1)` is the anisotropic-stress (tidal) operator. At `|k| = 0.05`, with `Phi = -1/khat^2` on the lattice and `-1/k^2` in the continuum, the lattice `E_h(nu = 0)` and the continuum `c Q_EH h_0`, `c = -1/2`, agree to `3.1e-4`: on the axis `xx = 0`, `yy = zz = -0.5000`; on the face diagonal `xx = yy = -0.2500`, `zz = -0.5000`, `xy = +0.4997` against `+0.5000`. This is `G_ij ∝ (d_i d_j - delta_ij nabla^2)(Psi - Phi)`, zero iff `Psi = Phi`.
3. It is nonzero at every declared momentum: the largest spatial slot of `(E_h(2) - E_h(1))/khat^2` is at least `0.338` over the four static momenta. A rate ruler with `nu_r != 1` would need an anisotropic stress `T_ij ∝ (nu_r - 1)` throughout space to hold its geometry up; a point-mass worldline supplies none. **The vacuum Regge equations admit the rate-induced geometry iff `nu_r = 1`.**

**Proof.** Item 1 evaluates `E_h` at three exponents. Item 2 compares the two operators on `h_0` at the two small momenta `[O(k^2)]`, deviation `3.1e-4`. Item 3 takes `E_h(2) - E_h(1)` at the four declared momenta `[exact]`.

## Theorem 4 -- a worldline source is solvable, and its exact solution is the rate field

**Conclusion.**

1. `sigma e_tau` lies in `range Q(k)` at every static momentum: `max|Q dl_ex - e_tau| = 6.1e-12` at the declared momenta and `3.3e-14` over the 511 torus momenta, with `dim ker Q(k) = 5` (4 gauge + 1 flat branch) everywhere. The flat branch is not sourced.
2. The exact solution equals the rate field with `M = sigma/2` once the five zero modes of `Q(k)` are projected out: relative residual `1.0e-11` at the declared momenta (the pseudo-inverse is conditioned at `1/khat^2`, `6.2e-4` at the smallest one) and `2.1e-16` in position space at every torus site, against `|delta l_rate| = 7.27e-2` at `r = 1`. The gauge-invariant potentials of the exact solution at the six smallest torus momenta give `Psi/Phi = 1` to `2.7e-15` and `Phi khat^2 = -1/2` to `4.0e-15`.

**Proof.** Pseudo-inverse solve of `Q(k) dl = e_tau`, null space by Hermitian eigendecomposition at `1e-9`, projection of the difference, inverse FFT; `Phi_gi = h_tt/2`, `Psi_gi = -(1/4) P_ij h_ij` with the lattice transverse projector. `[exact]`

## Theorem 5 -- the endpoint mean is the exact rule; the line average is not

**Conclusion.** With the landed line-average map in place of the endpoint mean, `max|M_line^dag Q M_line h_1 + khat^2 e_tt| = 7.1e-3, 0.48, 4.5, 2.7e-9` at the four declared momenta (the last is `4.3e-6` relative to `khat^2`), and the torus source coefficient is `0.90025` against the endpoint mean's `1.00000` (to `1e-12`). The identity of Theorem 2 is exact for the endpoint mean only. The two rules agree at `O(k^2)` and separate at `O(k^4)`; the ruler chain's own arithmetic-mean dressing is the exact one.

**Proof.** Theorem 2's evaluation repeated with `M_line`. `[exact]`

## Theorem 6 -- a time-dependent rate is not a vacuum solution, and the propagating modes are not rate fluctuations

**Conclusion.**

1. At the Euclidean 4-momentum `(0.05, 0, 0, 0.05)` the metric-projected residual of `h_1 e^{i(k.x + k_tau tau)}` per `khat^2_4D` is `xx = yy = zz = -0.500`, `tt = -0.500`, `xt = +0.999` (continuum `c Q_EH h_1/k^2`: `-0.500`, `-0.500`, `+1.000`, deviation below `5e-3`); at `(0.4, 0.2, -0.3, 0.5)` it is `xx = -0.460`, `tt = -0.540`, `xt = +0.666`, `yt = +0.349`, `zt = -0.553` (continuum `-0.463`, `-0.537`, `+0.741`, `+0.370`, `-0.556`). A time-varying rate needs a momentum density and a pressure: it is the constrained sector, not a free mode.
2. The rate direction `(-2, -2, -2, +2)` has overlap exactly `0` with both TT polarisations (`h_xy` and `h_xx - h_yy` at `k || z`); it spans `1` of the `10 - 4 = 6` physical metric degrees of freedom; and on shell, where the continued Hessian annihilates the two propagating modes to `1e-16`, it does not annihilate the rate field: `|Q u_rate|/|u_rate| = 0.340, 1.601, 5.960` at `|k| = 0.5, 1, 2`.

**Proof.** Item 1 evaluates the continued operators at real Euclidean 4-momenta `[O(k^2)]`. Item 2 is two inner products, a rank count of the gauge family, and Theorem 1's on-shell Hessian applied to `M_AM h_1` `[exact]`.

## Theorem 7 -- end to end against the nonlinear Regge action

**Conclusion.** (A) The position-space endpoint-mean rule `delta l_e(x) = (w^T h w)/(2 l_0) (Phi(x) + Phi(x + w))/2`, Fourier-transformed, equals `Re[M_AM(k) h e^{ik.x}]` at every site and class of the `8^3` torus at `k = 2 pi (1, 2, 0)/8`, to `1.8e-15`. (B) On the periodic `3^4` box the landed nonlinear `S_R`, second-differenced along the rate-induced field at `k = (2 pi/3, 0, 0, 0)` with step `1e-4`, gives `-243.000674`; the Bloch prediction `(N/2) Re[u^dag Q u]` is `-243.000000`; the identity's prediction `(N/2)(-khat^2)(h_tt = 2) = (81/2)(-3)(2)` is `-243.000000`; `S_R(flat) = 3.3e-12`. Every sign, phase, star and factor of Theorem 2 is validated on the action itself, not only on its Bloch Hessian.

**Proof.** (A) is a direct comparison `[exact]`; (B) is a central second difference against two independent predictions `[numerical]`, relative deviation `2.8e-6`, consistent with the `O(step^2)` truncation of the difference.

## Corollary -- the static Einstein equations in the framework's terms

1. **The rate field obeys the lattice Poisson equation, and that equation is the linearised Regge equation.** With `S_E = -S_R/(8 pi G) + m sum l_tau`, stationarity in the edge lengths gives `Q delta l = 8 pi G m e_tau`; Theorem 2 makes the left side `2M e_tau (delta - 1/N)`, so `2M = 8 pi G m`, `M = 4 pi G m`, and `Phi(k) = -M/khat^2`, whose continuum limit is `-G m/r`. In the framework's terms: the record-formation-rate field `r_v = r_0 (1 + Phi_v)` obeys `nabla^2_lat Phi = 4 pi G rho` on the temporal edges, the bridge's `phi = G0 P0 rho` with the energy density as source, and this equation **is** the linearised Regge equation of the complex on the rate-induced geometry. The bridge's `P0` normalisation is not re-verified here; `G` is the supplied coefficient of the action, exactly as in the continuum.
2. **The exponent is selected, and so is the bending factor.** The ruler note's one supplied object, `nu_r = 1`, is the one exponent for which the point-mass geometry is on shell (Theorem 3). Equivalently, the light-bending factor `alpha/beta = 1 + nu_r = 2` is what the Regge equations select; no second scalar, no independent spatial ruler, is needed.
3. **The sign.** Attraction (`Phi < 0`, temporal edges shorter near the mass) holds in the orientation in which `S_R` enters with a negative coefficient, the orientation in which the four massive non-metric branches (`-48, -16 x 3` raw) are positive. One supplied sign, two consistent demands.
4. **What the record count does not read.** The rate is a site scalar and spans one of the six physical metric directions; the graviton lives in the other five, and in the two TT ones in particular, with which the rate has zero overlap (Theorem 6). The missing object for the propagating sector is the direction-dependent edge-length freedom, the part of "edge lengths supplied" that no record count yet reads. A per-bond record rate, in place of the per-site `r_v` the ruler chain dresses hops with, is the natural candidate and is untested here.

**Reading, not theorem.** Records are one per site, permanent and readable, and "a readout value is determined by record content alone" (Record). The count of records registered along an edge is therefore readable content, and "edge length = records registered along the edge" is a reading the axioms *license* -- nothing pre-record is invoked, the length is constituted by what the stack registers -- but do not *derive*: the axioms supply no rate values (Admissibility's own reading note says the distribution "does not supply the formation site, probability, or rate") and no tick. The endpoint mean is derived here to be the exact rule; that a record count along an edge *is* the endpoint mean is a reading of the same kind. Nothing here follows from the axioms alone; everything is derived from `S_R` on the rate-induced geometry.

## What does not change

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- The graviton note's census (`dim ker Q = 5`, two propagating modes, the exact dispersion) is reproduced, not revised; the ruler chain's algebra is used as a condition, not re-derived.
- No continuum limit is taken; the continuum forms are quoted to name the comparison and appear only in the `[O(k^2)]` comparators.

## Interfaces named for other lanes, not taken up here

- **The Regge action, its orientation and `G`** stay supplied; nothing here selects `S_R` or its sign.
- **The Euclidean/OS0 reading** of the complex and the Lorentzian continuation are the graviton note's, unchanged.
- **The tick identification `l_tau = r/r_0`** and the worldline coupling `S_m = m sum l_tau` are declared; a lane owning the tick scale owns whether they follow from anything.
- **The rate law with `kappa_r = 1`** is inherited with the whole conditional chain of PR #7925: the designed fermion law, the staggered-sea vacuum choice, the bridge's constant mode.
- **The endpoint-mean rule** is derived to be exact; its record-count reading is a reading.
- **The bridge's `P0` normalisation** is not re-verified; the relation used is `M = 4 pi G m` in the orientation above.
- **A per-bond record rate** as the direction-dependent freedom the propagating sector needs is named and untested.

## Executable claim block

The canonical machine-bound restatement of the seven theorem conclusions.

```text
conditional_on: S_R = sum_t A_t delta_t on the landed T(Z^3 x Z_tau), its orientation and G supplied; the Euclidean/OS0 reading; l_tau = l_0 r_v/r_0 (tick = proper time); S_m = m sum l_tau; r_v = r_0 (1 + Phi_v) with kappa_r = 1 inherited from the open PR #7925 chain; the endpoint-mean edge rule
setting: 15 edge classes, 50 hinge classes per 4-cell, 15 x 15 Bloch Hessian per momentum; declared static momenta (0.37,-0.81,0.22), (1.9,0.4,-2.3), (2.9,2.7,-3.0), (0.013,0.007,-0.02); 8^3 spatial torus at k_tau = 0 with a unit point mass Phi(k) = -1/khat^2; periodic 3^4 box; NO random number anywhere; largest dense object (512, 15, 15)
provenance: max|Q - bloch_Q| = 9.2e-16, |M_line - metric_map| = 2.2e-16, |QEH - einstein_pairing_4d| = 6.9e-18; on shell at 4 sinh^2(omega/2) = khat^2 the nullity is 7 (null values <= 1.4e-16, first non-null >= 7.6e-3) and 5 off shell, at |k| = 0.5, 1, 2
exact_identity: M_AM^dag Q M_AM h_1 = -khat^2 e_tt to 4.6e-15 and Q M_AM h_1 = -2 khat^2 e_tau to 5.4e-15 at every declared static momentum; 14 non-temporal classes <= 5.4e-15; position space (Q delta l_rate)_tau(x) = 2M(delta_x0 - 1/N) to 1.3e-16 at every torus site, other classes <= 2.8e-16
nu_forced: E_h affine in nu to 7.1e-15; tt slot = -nu khat^2 exactly; (nu - 1) coefficient = c Q_EH tidal operator, c = -1/2, to 3.1e-4 at |k| = 0.05 (axis yy = zz = -0.5000; face xx = yy = -0.2500, zz = -0.5000, xy = +0.4997); largest spatial slot >= 0.338 khat^2 at every declared momentum
worldline_source: max|Q dl_ex - e_tau| = 6.1e-12 (declared k), 3.3e-14 (511 torus momenta); dim ker Q(k) = 5 everywhere; zero-mode-projected |dl_exact - dl_rate(M = sigma/2)| = 2.1e-16 at every torus site (1.0e-11 relative at the declared k, solve conditioned at 1/khat^2); Psi/Phi - 1 = 2.7e-15, Phi khat^2 + 1/2 = 4.0e-15
edge_rule: line-average residuals 7.1e-3, 4.8e-1, 4.5, 2.7e-9 (4.3e-6 relative); source coefficient line 0.90025, endpoint mean 1.00000
time_dependent: residual per khat^2_4D at (0.05,0,0,0.05): xx = tt = -0.500, xt = +0.999 (continuum -0.500, -0.500, +1.000); at (0.4,0.2,-0.3,0.5): xx -0.460, tt -0.540, xt +0.666, yt +0.349, zt -0.553 (continuum -0.463, -0.537, +0.741, +0.370, -0.556)
propagating_modes: overlap of (-2,-2,-2,+2) with h_xy and h_xx - h_yy = 0 exactly; physical metric d.o.f. 10 - 4 = 6, the rate spans 1; on shell |Q u_rate|/|u_rate| = 0.340, 1.601, 5.960 at |k| = 0.5, 1, 2
end_to_end: position-space endpoint-mean rule = Re[M_AM h e^{ikx}] to 1.8e-15; 3^4 box S_R second difference -243.000674 vs Bloch -243.000000 vs identity (81/2)(-3)(2) = -243.000000; S_R(flat) = 3.3e-12
normalisation_reading: Q delta l = 8 pi G m e_tau gives M = 4 pi G m and Phi -> -G m/r; attraction in the orientation with the massive non-metric branches positive; P0 of the bridge not re-verified
not_supplied_here: any derivation of S_R, its orientation, G, the OS0 reading, the tick identification, the worldline coupling, the rate law, kappa_r, the record-count reading of an edge length; any statement about the propagating sector beyond its non-overlap with the rate direction; any nonlinear closure
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=13 FAIL=0
```

## Proof boundary

Everything above is at **linear order** in the edge-length perturbation and in `Phi`; Theorem 7 touches the nonlinear action only through a second difference. Sources are **static** (`k_tau = 0`) except in Theorem 6, where the time-dependent ansatz is shown not to be a vacuum solution and nothing more. The complex is the landed `T(Z^3 x Z_tau)` in its Euclidean/OS0 reading; no Lorentzian statement is made beyond what the graviton note's continuation already carries. The finite objects are the `8^3` spatial torus, the periodic `3^4` box and the declared momenta; the identity of Theorem 2 is exact at every momentum tested and, being linear and momentum-wise, is stated for every static potential on any torus, but it has been evaluated only at the sizes named. Nothing is said about the TT modes beyond their zero overlap with the rate direction and the on-shell non-annihilation of Theorem 6. There is **no nonlinear closure**: the Regge equations beyond quadratic order, the back-reaction of the geometry on the rate, and the sea's own energy density are untouched. The bridge's `P0` normalisation is not re-verified; the sign discussion is a consistency reading of one supplied orientation. The rate law and `kappa_r = 1` carry every condition of the ruler chain, which is on an open PR and not on `origin/main`; if that chain does not hold, Theorems 2-5 and 7 remain true statements about the field `h_1` and lose their reading as statements about records.

**Nothing here derives a supplied object.** `S_R`, its orientation, `G`, the OS0 reading, the tick identification, the worldline coupling, the rate law, `kappa_r = 1` and the record-count reading of an edge length are all supplied or declared. What is derived, from `S_R` on the rate-induced geometry: the exponent `nu_r = 1`; the relative sign and magnitude of the temporal and spatial halves; the exactness of the endpoint-mean rule; the identity static-Regge = lattice-Poisson on the temporal edges; the form of Newton's potential; and the non-overlap of the rate with the propagating modes. No axiom is amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: one exact finite-dimensional identity, `Q M_AM h_1 = -2 khat^2 e_tau`, checked at declared incommensurate momenta to `5e-15`, in position space at every site of an `8^3` torus to `3e-16`, and against the landed nonlinear action on a `3^4` box to `2.8e-6`; one forced exponent, `nu_r = 1`, with the failure for `nu_r != 1` exhibited as a named operator (the tidal operator, `c Q_EH` to `3.1e-4` at `|k| = 0.05`) that is nonzero at every declared momentum; one uniqueness statement (exact solution = rate field up to the five zero modes, `2.1e-16`); one edge-rule discrimination (endpoint mean exact, line average `0.90025` against `1`); and one plain negative, that the rate direction has zero overlap with both graviton polarisations and is not annihilated on shell. The title is the honest one: the formation rate defines the **static** Regge edge lengths exactly, not "the graviton and the ruler are one field". Every number is machine-exact or an explicitly tagged `O(k^2)` comparison; no seed, no fitted constant, no PDG value enters. The auditor should also see exactly what is not claimed: nothing about the propagating sector beyond non-overlap, nothing nonlinear, nothing about the tick scale, and nothing derived about any object the parents left supplied. The ledger carries no audited status for this note or its parents, and the four parent notes are open PRs.

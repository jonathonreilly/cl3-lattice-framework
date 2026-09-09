---
claim_id: fermion_charge_coupling_screens_link_field_no_transverse_stiffness_lambda_sign_2026_09_04
claim_type: bounded_theorem
claim_scope: "On THREE NAMED TWISTED TORI plus TWO NAMED FINITE COUPLED GEOMETRIES, carrying ONE DESIGNED SPIN-1/2 LINK ROLE per coarse edge in the conventions of PR #7911, PR #7942 and PR #7959 together with ONE FERMION MODE per coarse vertex in the conventions of PR #7893 and PR #7883 -- the half-filled Kawamoto-Smit pi-flux sea on the 6^3, 8^3 and 12^3 tori at their sea-minimising twists, the fully periodic 2x2x2 coupled Gauss sector at 303,721 states with NO TRUNCATION, and the fully periodic 4x2x2 pure-link zero-winding component at 1,551,976 states: (T1) [exact, seed-free] with the link phase read as a c-number background, the one-loop polarisation of the sea satisfies the Ward identity to 1.5e-15, has Pi_L = 0 and chi(0) = 0 exactly, and induces a Lorentz-covariant Maxwell term with kappa_E > 0 and kappa_B > 0, both running logarithmically and c^2 = kappa_B/kappa_E = 6.317, 5.038, 4.444 falling to v_F^2 = 4 from above; kappa_E enters the INVERSE electric stiffness, 1/U_tot = 1/U_link + kappa_E, and the density response is purely longitudinal. (T2) [exact, seed-free] on the complete 2x2x2 coupled sector the hop lowers the Gaussian stiffness U = omega/(2 S_T) at k = (pi,0,0) from 4.97 to 4.75 at t = 1, melts the staggered sea, mixes the winding sectors, has a record-basis sign problem in every variant tried, and selects P2's -lambda over PR #7893's +lambda by 1.3206 in E_0 at t = lambda = 1. (T3) [exact, seed-free] a SUPPLIED collinear stand-in Uc sum_{collinear pairs} E_b E_b', which is NOT what the fermion produces, raises the exact 4x2x2 decay rate omega(pi/2) from 2.566 to 2.951 and lowers S_yy(pi/2) from 0.1045 to 0.0845 at Uc = 1. NOT ASSERTED: nothing about the coupled model on any torus with L >= 4 in any direction, no continuum limit, no T > 0, no larger link spin, no thermodynamic statement about the dispersion form, and no claim that this U(1) is electromagnetism; every L^3 row is a stochastic witness at a declared seed; the link carrier, its law, the fermion, the hop, the one-loop reading of U_e and the collinear stand-in are all supplied and nothing here is obtained from any axiom."
upstream_dependencies: []
runner: scripts/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.py
---

# The pi-flux sea screens the spin-1/2 link field: one-loop polarisation on `6^3`-`12^3`, the exact coupled `2x2x2` sector, its record-basis sign structure, and the sign of `lambda` the sea selects

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** bounded - bounded or caveated result note

**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.py`](../scripts/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.txt`](../logs/runner-cache/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.txt)

**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes in "Imports and authority" are plain-text pointers.

PR #7959 found the pure spin-1/2 link law `H = -lambda sum_f P_f` gapless, deconfined and unordered at `L <= 12` with a quadratic transverse mode and a flat transverse structure factor, and named an electric stiffness `U > 0` in front of `E^2` as the missing Maxwell ingredient. It named two candidate suppliers and computed neither. The first of them -- the coupling to the fermion's charge of PR #7893 -- is computed here three ways: at one loop on three twisted tori, exactly on the complete `2x2x2` coupled sector, and against a supplied stand-in stiffness on the exact `4x2x2` component. The answer is the same in all three: **the coupling screens; it does not stiffen.** A second fact, not asked for, is load-bearing: with matter present the sign of `lambda` relative to the Kawamoto-Smit hop is physical, and the pi-flux sea selects PR #7959's `-lambda`.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-geometry theorems about one declared coupling of one designed spin-1/2 link role to one staggered fermion: the seed-free one-loop polarisation of the half-filled pi-flux sea on three named twisted tori, the complete untruncated 2x2x2 coupled Gauss sector with its spectrum, structure factors, poles, winding admixture and record-basis sign structure, and the exact 4x2x2 rows of a supplied collinear stand-in. Every L^3 row is a labelled stochastic witness at a declared seed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independently audit the exact rows, and route to the owner of PR #7893 the finding that the sign of lambda relative to the Kawamoto-Smit hop is physical in the coupled model and that the pi-flux sea selects the opposite sign to the one that note declares."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of `T1`-`T3` below, exactly the runner's check groups `A`, `B` and `C`. Groups `A`, `B`, `C1`, `C3` and `C4` are exact and seed-free; `B1` and `C3` are integer and bit arithmetic with no floating-point step, the rest floating-point at the stated tolerance. Rows `C2` and `C5` are `[witness]` at declared seeds. Group `D` is `[declared]`: it states the quoted `L^3` rows with their seeds and run lengths and checks only the arithmetic read off them.

1. `T1` (`A`). The one-loop polarisation of the half-filled pi-flux sea, its exact conservation identities, and the sign and running of the two induced couplings.
2. `T2` (`B`). The complete `2x2x2` coupled sector: its census, its `t = 0` anchors, the softening of the transverse-electric sector, the melting of the staggered sea, the mixing of the winding sectors, the sign structure of the record basis, and the selection of `-lambda`.
3. `T3` (`C`). The supplied collinear stand-in on the exact `2x2x2` ice component, the patched engine validated against it, and the exact `4x2x2` rows at `Uc = 0` and `Uc = 1`.

## Imports and authority

Imported scientific authority: none load-bearing. Kawamoto-Smit staggered fermions, the quantum-link (gauge-magnet) presentation, minimal Peierls coupling, one-loop vacuum polarisation and the Ward identity, Green's-function projector Monte Carlo with population control and forward walking, and the Lifshitz / Rokhsar-Kivelson vocabulary are standard methodology; **every object is redeclared here and every exact statement is recomputed by the runner**, the engines included -- their C source is embedded in the runner and compiled at run time, so no binary and no external datum is trusted. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, no grade and no dependency weight:

- `THE_PURE_SPIN_HALF_LINK_MODEL_..._BOUNDED_NOTE_2026-09-04.md` (open PR #7959, "P2" below): the pure law, its conventions, the `2x2x2` and `4x2x2` geometries, its three exact anchors reproduced here, its reading `U(k) ~ k^2` of the pure stiffness, and the question this note answers for the first of its two named suppliers.
- `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_..._BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893): the link algebra with `E_e^2 = I/4`, the minimal hop, the Kawamoto-Smit signs, and the staggered Gauss law `2 (div E)_v = 2 n_v - (1 - eps_v)` forced by coordination parity at `z_v = 6`. Its declared `+lambda` is the sign this note finds disfavoured.
- `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_..._NOTE_2026-09-03.md` (open PR #7883): the twist convention and the sea energies `-78.383672`, `-258.857540`, `-611.811768` reproduced here to every printed digit.
- `THE_LINK_MODELS_PAIR_UPDATE_..._NOTE_2026-09-04.md` (open PR #7942) and `THE_SPIN_HALF_LINK_RING_IS_GAPPED_..._NOTE_2026-09-03.md` (open PR #7911): the plaquette-parity obstruction and the conventions used verbatim.
- `THE_FERMION_ON_COMPACT_U1_LINKS_..._NOTE_2026-09-03.md` (open PR #7903): the Kogut-Susskind magnetic sign `H_B = -(1/g^2) sum_f cos_f`, which is the sign this note's sea selects.
- The sister lane's Rokhsar-Kivelson notes: they supply the sense of "photon" measured against here, and their `L = 6, 8` dispersion at the Rokhsar-Kivelson point is reproduced in group `D`.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms, quoted in "Setting" and nowhere used as a premise.

## Setting

**The supplied surface.** The `U(1)` carrier is PR #7893's and P2's **designed role**: one further two-state site per coarse edge, assigned by design, with `E_e = Z^L_e/2` a one-record value that registers and `U_e = sigma^+_e` carrying `X` in every monomial. The pure-gauge law `H = -lambda sum_f P_f` is declared with `lambda` supplied and set to `1`; on spin-1/2 links the electric term is the c-number `E_e^2 = I/4` and supplies no dynamics, which is P2's reading `U(k) = u k^2` of the pure stiffness. The matter is PR #7893's: one fermion mode per coarse vertex, the minimal Peierls hop `-t sum_{(v,d)} eta_d(v) [a_v^+ U_(v,d) a_{v+d} + h.c.]` at unit charge with the Kawamoto-Smit signs `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1+v_2}`, and the staggered Gauss law, which is a consequence of choosing spin-1/2 links at even coordination rather than a further choice. The tori and their twists are declared and are PR #7883's. **Nothing below is obtained from any axiom.**

The four framework axioms are quoted, not amended. **Qubit**: "Each site has a domain of local possibilities." and "The full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." **Record**: "Records form.", "When present, a record locks exactly one admissible local possibility.", "A site never carries more than one record; records are permanent.", "Only records are readable." and "A readout value is determined by record content alone." They are used to fix what "readable" means and for nothing else.

## Definitions

```text
E_e = (1/2) Z^L_e,  U_e = sigma^+_e,  P_f = W_f + W_f^dag,  H_gauge = -lambda sum_f P_f
eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}        KAWAMOTO-SMIT SIGNS
M_{v,v+d} = -t eta_d(v);  a twist on axis a flips the bonds crossing v_a = L-1 -> 0
H(t, lambda) = -t sum_{(v,d)} eta_d(v) [a_v^+ U_(v,d) a_{v+d} + h.c.] + s lambda sum_f P_f
   with s = -1 (P2's declared law) or s = +1 (PR #7893's declared law)
Gauss:  2 (div E)_v = 2 n_v - (1 - eps_v),  eps_v = (-1)^{v_1+v_2+v_3}
Minimal coupling M_b -> M_b e^{i A_b} on b = (v,d), A_b a C-NUMBER BACKGROUND [SUPPLIED]
Pi_dd'(k)   = -<K_bond> delta_dd' - (2/N) sum_{p unocc, h occ} conj(J_d) J_d' / (e_p - e_h)
kappaE_dd'  =  (2/N) sum_{ph} conj(J_d) J_d' / (e_p - e_h)^3          [w^2 coefficient]
chi(k)      =  (2/N) sum_{ph} |rho(k)_ph|^2 / (e_p - e_h)
K_d = 2 sin(k_d/2),  P_T = 1 - K K^T/|K|^2,  kappa_B = Pi_T/(2|K|^2),  kappa_E = tr(P_T kappaE)/2
U = omega/(2 S_T),  V = 2 omega S_T                       THE GAUSSIAN READ-OFF [SUPPLIED]
D(s) = V_rk n_app(s) + Uc sum_{collinear pairs} E_b E_b'      THE STAND-IN [SUPPLIED]
```

`P_f` is **applicable** iff `b_p = b_q`, `b_u = b_w` and `b_p != b_u` on its ordered quadruple; `n_app(s)` counts applicable faces. A collinear pair is `(v,d)` and `(v+e_d,d)`; the stand-in is the site-averaged field squared, `U_site sum_v |Ebar_v|^2 = const + (U_site/2) sum_{pairs} E_b E_b'` with `Ebar_v = (1/2) sum_d (E_{v,d} + E_{v-d,d}) e_d`, so `Uc = U_site/2`. **The stand-in is supplied and is not what the integrated-out fermion produces.**

## Theorem 1 -- the sea screens: one loop on `6^3`, `8^3`, `12^3`

**Conclusion.** `[exact, seed-free]` On the twisted tori `6^3` at twist `(0,0,0)` and `8^3`, `12^3` at `(1,1,1)`, which minimise the sea energy at `E_sea = -258.857540`, `-611.811768`, `-2063.196887` with half-filling gaps `3.464102`, `2.651309`, `1.793151` (and `-78.383672`, `4.898979` at `4^3`), with the link phase read as a c-number background:

1. `[exact]` The chiral identity `eps M eps = -M` holds with residual `0.0` exactly, and the `8`-site Bloch block puts the Dirac node at `(pi/2, pi/2, pi/2)` with `v_F = 2t` isotropically.
2. `[1e-15]` `<K_bond>` is uniform over bonds to `3.5e-16`, `Pi` is Hermitian to `1.5e-18`, and the Ward identity `|Pi K|/|Pi| <= 1.5e-15` at every one of the `25` non-zero `k` on the three tori. The lattice-longitudinal part `Pi_L` is `0` to `1.3e-16`, the static density response `chi(0)` is `0` to `1.1e-30`, and `kappaE_L = chi/|K|^2` to `1.7e-17` -- the continuity equation, exactly. **The density response is purely longitudinal.**
3. `[1e-5]` `Pi_T > 0`, `kappa_B > 0` and `kappa_E > 0` at every non-zero `k`: the sea is diamagnetic and the induced term is a Maxwell term, `(1/2)[kappa_E w^2 + kappa_B |K|^2] |A_T|^2` per transverse polarisation. The two transverse eigenvalues are equal on the axes and split off them (`0.10996`, `0.15107` at `2pi/6 (1,1,0)`). At `2pi/12 (1,0,0)`, `(Pi_T, kappa_B, kappa_E) = (0.065981, 0.123123, 0.027706)`.
4. `[1e-5]` Both couplings run logarithmically: at fixed `k L`, `kappa_B(k_min) = 0.101548, 0.106418, 0.123123` and `kappa_E(k_min) = 0.016076, 0.021123, 0.027706` at `L = 6, 8, 12`, while at fixed `k = pi/2`, `kappa_B = 0.062407, 0.060014` at `L = 8, 12` is `L`-independent. `c^2 = kappa_B/kappa_E = 6.317, 5.038, 4.444` falls toward `v_F^2 = 4` **from above**: the induced term is Lorentz covariant with the fermion velocity at long wavelength. The twist (Drude) stiffness vanishes as `1/L^3` (`Pi(0) L^3 = 9.56, 9.47, 10.39`): no free-carrier term.
5. `[1e-2]` `kappa_E` is the coefficient of `(d_tau A)^2`, which in Hamiltonian language is the **inverse** electric stiffness: `1/U_tot = 1/U_link + kappa_E`. A positive `kappa_E` therefore **lowers** `U`. In the reading where the link field has no inertia of its own, `U_eff = 1/kappa_E = 62.2, 47.3, 36.1` at `L = 6, 8, 12`. Under P2's reading `U(k) = u k^2` with `u = 2.294` read off `omega = 0.78 k^2` and `S_T = 0.17` per polarisation, `omega^2 = (v + kappa_B) u k^4 / (1 + kappa_E u k^2)` stays **quadratic** at small `k` and could turn linear only above `k_* = 1/sqrt(kappa_E u) = 3.97`, beyond the zone edge `pi`.

**Proof.** The sea is built from its own bond list at every one of the eight twists per `L` and diagonalised densely; the twist is chosen by minimising `E_sea` and the gap read off the half-filling edge. The polarisation is second-order perturbation theory in the bond phases, assembled from the particle-hole blocks of the three current operators and of the density, with the lattice gradient, the transverse projector and the two induced couplings as declared. Every step is exact linear algebra with no seed; the largest matrix is `1728 x 1728`.

## Theorem 2 -- the coupled `2x2x2` sector, complete and untruncated

**Conclusion.** `[exact, seed-free]` The fully periodic `2x2x2` torus (24 links, 24 faces, 8 vertices) with one fermion mode per vertex, Jordan-Wigner ordered by vertex index:

1. `[exact]` All `2^24` link states carry `130,193` distinct `2 (div E)` signatures; the `rho = 0` block is `9600`, P2's pure-gauge sector. Intersected with the `70` half-filled fermion patterns this gives **`303,721` states over all `70` charge configurations, with no truncation** -- the vacuum pattern (odd sublattice filled) carrying `9600` and the `69` charged blocks dimensions in `{2896, ..., 6000}`. `H` is exactly symmetric.
2. `[1e-9]` At `t = 0` the sector reproduces P2's three anchors to every digit: `E_0 = -9.0267209135`, `S_yy = S_zz = 0.25303701` at `k = (pi,0,0)` with `S_L` at its `1e-31` roundoff floor, and the lowest level carrying transverse-electric weight at `2.5172790443` with weight `0.803`. The coupled sector's own first excitation is a static charge pair at `0.884161`, not P2's within-block `Delta_1 = 1.6276`.
3. `[1e-4]` **The hop softens the transverse-electric pole and raises `S_T`.** At `k = (pi,0,0)` the main pole goes `2.5173 -> 2.4806` at `t = 1` with `-lambda` and `-> 1.8711` with `+lambda`, while `S_T` per polarisation goes `0.253037 -> 0.261072 -> 0.265518`. The Gaussian read-off `U = omega/(2 S_T)` **falls** `4.97 -> 4.75 -> 3.52`: the same direction as `1/U_tot = 1/U + kappa_E`.
4. `[1e-5]` **The staggered sea melts and the winding sectors mix.** `<eps n>/8 = -0.50000, -0.26463, -0.06635, -0.00980, +0.00812` at `t = 0, 0.25, 0.5, 1, 2` with `-lambda`: the "vacuum" of the staggered Gauss law is the strong-coupling sea and the fermion delocalises by `t ~ lambda`. `<W_d^2> = 0, 0.08892, 0.16419, 0.24005, 0.35214`, isotropic in `d`: P2's `125` winding classes cease to be superselected once a fermion can loop the torus.
5. `[1e-6]` **The record basis has a sign problem in every variant tried.** The canonical severity `E_0 - E_0^bos`, zero iff a diagonal sign gauge exists, is `0.008344, 0.064856, 0.227373, 0.587880` at `t = 0.25, 0.5, 1, 2` with `-lambda` and `0.187319, 0.792138, 1.548007, 2.831711` with `+lambda`, a factor `22.4, 12.2, 6.8, 4.8` worse. The hop alone (`lambda = 0`, `t = 1`) already gives `0.288496`, so fermion exchange suffices. A breadth-first sign gauge leaves `231,542` of `1,352,112` edges frustrated for the hops alone with the Kawamoto-Smit signs and with `eta = 1` alike, and `517,703` / `561,717` of `2,079,672` for the full model at `-lambda` / `+lambda`.
6. `[1e-9]` **The sign of `lambda` relative to the hop is physical, and the sea selects `-lambda`.** `E_0(-lambda) < E_0(+lambda)` at every `t > 0`, by `0.1790, 0.7273, 1.3206, 2.2438` at `t = 0.25, 0.5, 1, 2`; at `t = lambda = 1` the gap is `1.3206` (`-15.4713732151` against `-14.1507399853`). For the pure link law the flip is a gauge symmetry -- PR #7942's plaquette-parity theorem makes the flip graph bipartite -- which is why P2 and PR #7893 could differ harmlessly; with matter it is not.

**Proof.** The sector is enumerated by grouping all `2^24` link states by their integer `2 (div E)` signature in chunks and intersecting each signature with the fermion patterns that require it, so no state is dropped and none is added; the census is exact integer and bit arithmetic. `H` is assembled sparsely from the face quadruples and the hop terms with explicit Jordan-Wigner strings, and its extremal levels are found by Lanczos at tolerance `1e-10`. Structure factors and the winding admixture are ground-state expectations of record-diagonal operators; the pole is a Lanczos continued fraction on the orthogonal complement of the ground state, reported at its largest weight. The severity diagonalises `H_bos = H_diag - |H_od|` by the same method; the frustration count is the breadth-first sign gauge on the off-diagonal graph.

## Theorem 3 -- the supplied collinear stand-in on `2x2x2` and `4x2x2`

**Conclusion.** `[exact, seed-free except the two witness rows]` Adding `D(s) = V_rk n_app(s) + Uc sum_{collinear pairs} E_b E_b'` to the diagonal of the pure law:

1. `[1e-5]` On the complete `864`-state `2x2x2` ice component, `E_0 = -9.026721, -0.810822, -9.037853, -9.388780, -9.584715` and `S_yy(pi,0,0) = 0.253037, 0.395643, 0.228492, 0.208281, 0.280059` at `(V_rk, Uc) = (0,0), (0.9,0), (0,0.5), (0,1), (0,-0.5)`: a positive `Uc` costs electric texture and lowers `S_T`, a negative one raises it.
2. `[witness, seeds 20260930, 20261201-20261204]` The patched walker engine on that component at `N_w = 1600`, `tau = 20 + 400`, `dtau = 0.05`, `K = 200`, `K_p = 120`, `20` bins reproduces item 1 within `1.43` sigma over `20` comparisons, with Gauss residual `0` in every dump and `S_L = 0`; the mixed `<cval>` matches the exact mixed value to `0.016`, which certifies the incremental tracking of the collinear sum under flips.
3. `[exact]` On the `4x2x2` torus at `V_rk = Uc = 0` the engine reproduces P2's `T3` to every printed digit: `dim(Gauss) = 23,063,296` with `0` violations, `405` winding vectors, the zero-winding class `1,552,024` as **one** flip component of `1,551,976` at breadth-first depth `17` plus `48` frozen states, `21,578,752` adjacencies and `0` missing targets; `E_0 = -16.7037885782`, `<n_app> = 19.0690013962`, `S_L(pi/2) = 0`, `S_yy = 0.1044875978` at `pi/2` and `0.1815941329` at `pi`, and the exact transverse-electric decay rate `omega_eff = 2.599424, 2.569058, 2.566168` at `m = 40, 80, 120`, approached from above.
4. `[1e-3]` On the same component at `Uc = 1`: `E_0 = -17.3923265594`, `S_yy(pi/2)` **falls** `0.1044875978 -> 0.0844696486` (`19.2` per cent) and `omega(pi/2)` **rises** `2.566168 -> 2.951014`, so `U(pi/2) = omega/(2 S_yy)` rises `12.28 -> 17.47` while `V(pi/2) = 2 omega S_yy` holds at `0.536 -> 0.499`. The zero-winding component is the same `1,551,976` states: the diagonal term changes no adjacency. **This is what a stiffness looks like on this geometry, and it is supplied, not induced.**
5. `[witness, seed 20261401]` One short `L = 4` pair (`N_w = 1000`, `tau = 15 + 60`, `dtau = 0.05`, `K = 240`, `K_p = 120`, `10` bins, cubic-averaged) gives `S_T(pi/2) = 0.3577(143)` at `Uc = 0` and `0.2858(147)` at `Uc = 1`, a fall of `20.1` per cent at `3.5` sigma -- the direction and size of item 4's exact `19.2` per cent.

**Proof.** The `2x2x2` ice component is grown by breadth-first search from the ice configuration and diagonalised densely; the walker engine and the `4x2x2` engine are compiled by the runner from embedded C at run time and fed geometry files written by the runner's own indexing. The `4x2x2` engine enumerates the sector site by site, sorts it, re-derives `G_v` on every state, grows the component, builds its compressed sparse rows by binary search, and finds the Perron vector of `B = I + dpow (A - (D - D_min))` by power iteration, with `dpow = 1/(D_max - D_min)` so the matrix stays entrywise non-negative and the Perron vector is still the ground state. Decay rates are ratios of the exact lazy correlator. Peak memory is under `400` MB and no dense matrix exceeds `1728 x 1728`.

## The quoted `L^3` rows -- declared witnesses, not recomputed

The `L = 4, 6, 8` production (walker method, `N_w = 2000`, `tau = 30 + 200`, `dtau = 0.05`, `K_p = 120`, `20` bins, seeds `20261401`-`4`, `20261411`-`6`, `20261421`-`6`) costs about twelve minutes of core time and is **quoted with its seeds and run lengths, not recomputed**; group `D` checks only the arithmetic read off it. `S_L <= 5e-33` in every run.

- **The first cross-lane reproduction.** At the Rokhsar-Kivelson point `V_rk = 1` this engine gives `omega(k_min) = 0.3025(9)` at `L = 6` and `0.1778(4)` at `L = 8` against the sister lane's `0.305382 +/- 0.005596` and `0.177396 +/- 0.003236` -- `0.94` and `0.23` per cent apart, `0.51` and `0.12` sigma -- with `S_T(k_min) = 0.7500, 0.7479`, the classical ice value `3/4`, and `omega/q^2 = 0.3025, 0.3035` on the lattice measure `q = 2 sin(k/2)`: quadratic. At `V_rk = 0.9` the two codes differ by `-5` and `+8` per cent, and `S_T(k_min)` falls with `L` there (`0.593 -> 0.512`) where at `V_rk = 0` it does not.
- **The `Uc` scan.** At `L = 4`, `S_T(pi/2)` falls `0.354(5) -> 0.285(10)` from `Uc = 0` to `1`, `19.5` per cent, the same fraction as the exact `4x2x2` row. At `L = 8` nothing is resolved: `S_T(pi/4) = 0.311, 0.285, 0.311, 0.354` moves non-monotonically by `2.3` sigma across the scan and the reconfiguration copy count `20, 15, 20, 54` flags a population-control breakdown at `Uc = 1`, so that row witnesses the sampler's limit and not the physics. **No `k^2 -> c|k|` crossover is resolved at `k >= pi/4` for `Uc <= 1`.** A crude estimate of where one would sit: writing `U(k) = U_0 + u |K|^2` on the exact `4x2x2` rows gives `u = 6.14`, `U_0 = 5.19` and `k_* = 0.92 = pi/3.4`, inside the `L = 6` window where the witnesses carry `10`-`15` per cent errors on `omega`.

## Corollary -- the coupling screens rather than stiffens

Within the declared setting and at the sizes reached: **the fermion's charge coupling supplies no transverse electric stiffness.** `kappa_E` enters the *inverse* stiffness, so integrating the sea out can only lower `U`; the density response is exactly longitudinal, so Gauss's law converts none of it into a transverse cost; and the fermion generates no term of the form `U E^2` at all. On the exact coupled `2x2x2` sector the same thing happens without any of the one-loop reading: the pole softens, `S_T` rises, and the Gaussian `U` falls in both sign conventions. **The transverse mode does not become linear on anything computed here.**

The coupled model has a record-basis sign problem in every variant tried -- fermion exchange alone frustrates the basis -- so the sampler branch is closed at this budget and only the supplied collinear stand-in was run. That stand-in does stiffen the exact `4x2x2` rows, which calibrates what a Maxwell regime would look like there; it is not what the fermion produces, and its coefficient is a scan, not a prediction.

The new load-bearing fact is separate from all of that: **with matter present the sign of `lambda` relative to the Kawamoto-Smit hop is physical, and the pi-flux sea selects `-lambda`** by `1.3206` in `E_0` at `t = lambda = 1`. The half-filled sea prefers flux `pi` per plaquette and the Kawamoto-Smit signs already supply it, so the induced ring term reinforces `-lambda P_f` -- the Kogut-Susskind sign PR #7903 also uses. PR #7893's `+lambda` is therefore the disfavoured sign and carries the more severe sign problem; that is an interface item for that note, whose own numbers are quoted at `+lambda`.

The open item handed on, with the engine ready and validated: whether the pure law at `V_rk = 0` has `U(0) = 0` (Rokhsar-Kivelson-like) or a small `U(0) > 0` below `k = pi/6`. That is the sister lane's open item too, and it is the place a photon can still sit in this carrier without a supplied detuning.

## Where this note disagrees with the expectation it was set, and with its source computation

1. **The anticipated crossover runs the wrong way.** The question was posed as: coupling through Gauss's law makes the electric energy dynamical and might supply `U > 0`, turning `omega ~ k^2` into `omega = c|k|` below some `k_*`. Gauss's law ties the fermion to the *longitudinal* field only; the transverse field couples through the current, and a current response is inertia, which screens. At one loop the mode stays quadratic at small `k` and could turn linear only *above* `k_* ~ 4`, beyond the zone.
2. **The effective term the question asked to add is not a term the fermion generates.** `U E^2` never appears; what appears is `kappa_E (d_tau A)^2` and `kappa_B B^2`. The `Uc` stand-in of `T3` was therefore chosen for its symmetry and is labelled supplied throughout; the `T3` rows calibrate a stiffness, they do not measure one.
3. **The cross-lane agreement at `L = 6` is `0.94` per cent, not `0.5`.** The source computation reads it as `0.5 per cent`; `0.51` is the sigma. The `L = 8` figure, `0.23` per cent and `0.12` sigma, is unaffected.
4. **The severity ratio between the two `lambda` conventions is `4.8` to `22.4`, not `10` to `20`.** The source computation's range understates the spread at both ends: `22.4` at `t = 0.25` and `4.8` at `t = 2`.
5. **The question's pointer to the coupling note was to the wrong number.** The fermion-link note carrying the hop, the Kawamoto-Smit signs and the staggered Gauss law is PR #7893; PR #7898 is a gravity note and carries nothing used here.

## Reading, not theorem

Put one unit of electric flux on every edge, let the faces flip, and then let a charged particle hop along the edges, dragging the flux with it. The hope was that the particle would make the field stiff -- that spreading the electric field out would start to cost something, which is what turns a slow, floppy wave into light. It does the opposite. What the particle adds is inertia, not stiffness: the field gets heavier and cheaper to bend, not springier, and the part of the particle's response that Gauss's law can see points along the field rather than across it, so it never reaches the sideways wave at all. Turning the hopping on in the small box that can be solved completely shows the same thing without any approximation: the sideways wave gets softer and its equal-time strength goes up. Add a stiffness by hand and the wave does firm up exactly as expected, which is how we know the calculation would have seen one had there been one. Two things came out that nobody asked for. First, once the particle is there it matters which way round the sign of the face term is written, and the particle's own preferred pattern of flux picks one of the two; the other note in this family wrote the other one. Second, in the natural bookkeeping the coupled problem carries cancelling signs everywhere, so the cheap sampling method is not available for it at any size worth running.

## Interfaces named for other lanes, not moved here

- **PR #7959**, the pure law: its three exact `2x2x2` anchors, its `4x2x2` rows and its reading `U(k) ~ k^2` are reproduced here; its first named stiffness supplier is answered and its second, a larger link representation, is untouched.
- **PR #7893**, the fermion on quantum links: the hop, the signs and the staggered Gauss law are used verbatim. **The sign of `lambda` it declares is the disfavoured one in the coupled model**; its `T5` numbers are at `+lambda`. This is the item to route to that note's owner.
- **PR #7883**, the determinantal sea: its twist convention and its three sea energies are reproduced to every printed digit.
- **PR #7942** and **PR #7911**: the plaquette-parity obstruction and the conventions, used unchanged.
- **PR #7903**, the compact-`U(1)` fermion: its magnetic sign is the one this note's sea selects, which is a consistency point between the two presentations and is not proved to be more than that.
- **PR #7914** (the record-readable gauge-invariant algebra) and **PR #7885** (the vacuum question as one coefficient): named as neighbours; nothing here is moved into either.
- **PR #7898** is a gravity note and carries nothing used here.
- **The sister lane's Rokhsar-Kivelson rows**: reproduced at the Rokhsar-Kivelson point to `0.51` and `0.12` sigma by an independent engine, and differing by `5`-`8` per cent at `V_rk = 0.9` where the two window conventions differ.

## Executable claim block

```text
setting: 6^3, 8^3, 12^3 twisted tori for the sea; the fully periodic 2x2x2 coupled Gauss sector; the fully periodic 4x2x2 zero-winding component; ONE DESIGNED spin-1/2 link role per coarse edge and ONE fermion mode per coarse vertex; ordinary composition; four axioms quoted and used for nothing
law: E_e = Z^L_e/2, U_e = sigma^+_e, P_f = W_f + W_f^dag, H = -t sum eta_d(v) [a^+ U a + h.c.] + s lambda sum_f P_f with lambda supplied and set to 1 and s = -1 or +1; staggered Gauss law 2 (div E)_v = 2 n_v - (1 - eps_v)
one_loop: [bounded_theorem] Ward identity |Pi K|/|Pi| <= 1.5e-15 at all 25 non-zero k; Pi_L = 0 to 1.3e-16; chi(0) = 0 to 1.1e-30; kappaE_L = chi/|K|^2 to 1.7e-17; kappa_B, kappa_E > 0 everywhere; kappa_B(k_min) = 0.101548, 0.106418, 0.123123 and kappa_E(k_min) = 0.016076, 0.021123, 0.027706 at L = 6, 8, 12; c^2 = 6.317, 5.038, 4.444 -> v_F^2 = 4 from above; Pi(0) L^3 = 9.56, 9.47, 10.39
screening: [bounded_theorem] kappa_E is the coefficient of (d_tau A)^2, so 1/U_tot = 1/U_link + kappa_E and U_eff = 1/kappa_E = 62.2, 47.3, 36.1; NO term of the form U E^2 is generated; under P2's U(k) = u k^2 with u = 2.294 the mode stays quadratic and k_* = 3.97 > pi
t222_census: [bounded_theorem] 130,193 divE signatures over all 2^24 link states; rho = 0 block 9600; 303,721 states over ALL 70 charge patterns with NO truncation; vacuum block 9600, charged blocks in {2896,...,6000}
t222_coupled: [bounded_theorem] t = 0 anchors E_0 = -9.0267209135, S_yy = S_zz = 0.25303701, pole 2.5172790443 at weight 0.803, first excitation 0.884161; at t = 1 the pole falls to 2.4806 (-lambda) / 1.8711 (+lambda) and S_T rises to 0.261072 / 0.265518, so U = omega/(2 S_T) falls 4.97 -> 4.75 -> 3.52; <eps n>/8 -> 0 by t ~ 1; <W_d^2> = 0, 0.08892, 0.16419, 0.24005, 0.35214
sign_structure: [bounded_theorem] severity E_0 - E_0^bos = 0.008344, 0.064856, 0.227373, 0.587880 at -lambda and 0.187319, 0.792138, 1.548007, 2.831711 at +lambda for t = 0.25, 0.5, 1, 2, a factor 4.8 to 22.4 worse; hop alone 0.288496; frustrated edges 231,542/1,352,112 and 517,703 / 561,717 of 2,079,672
lambda_sign: [bounded_theorem] E_0(-lambda) < E_0(+lambda) at every t > 0; the gap is 1.3206 at t = lambda = 1 (-15.4713732151 against -14.1507399853); the pi-flux sea selects -lambda
standin_exact: [bounded_theorem] SUPPLIED Uc sum_pairs E E'; on 864 states E_0 and S_yy at five (V_rk, Uc); on 4x2x2 the Uc = 0 row is P2's T3 to every digit, and at Uc = 1 S_yy(pi/2) falls 0.1044875978 -> 0.0844696486 while omega(pi/2) rises 2.566168 -> 2.951014, U(pi/2) 12.28 -> 17.47
validation: [witness, seeds 20260930, 20261201-4, 20261401] the patched engine within 1.43 sigma of the exact 864-state rows over 20 comparisons with Gauss residual 0; one short L = 4 pair giving S_T(pi/2) 0.3577(143) -> 0.2858(147), a 20.1 per cent fall at 3.5 sigma
production_quoted: [witness, QUOTED not recomputed; seeds 20261401-4, 20261411-6, 20261421-6] omega(k_min) = 0.3025(9) and 0.1778(4) at L = 6, 8 at the Rokhsar-Kivelson point against the sister lane's 0.305382(5596) and 0.177396(3236), 0.51 and 0.12 sigma; S_T(pi/2) at L = 4 falls 19.5 per cent by Uc = 1; nothing resolved at L = 8; no k^2 -> c|k| crossover at k >= pi/4 for Uc <= 1
claim_types: bounded_theorem for one_loop, screening, t222_census, t222_coupled, sign_structure, lambda_sign and standin_exact; witness for validation, production_quoted and every L^3 row without exception
not_claimed: nothing is proved for the coupled model on any torus with L >= 4 in any direction; no continuum limit, no T > 0, no larger link spin, no thermodynamic dispersion form; no claim that this U(1) is electromagnetism; the one-loop reading of U_e as a c-number phase, the Gaussian read-off U = omega/(2 S_T), the collinear stand-in, the link carrier, its law and the fermion are all supplied
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=18 FAIL=0 in 148-166 s with a C compiler present; PASS=14 FAIL=0 in 42 s without one, the four C-dependent rows C2-C5 reporting SKIP with the reason
```

## Proof boundary

Proved seed-free on **named finite geometries only**: the one-loop response of the **free** Kawamoto-Smit sea, with the link read as a c-number phase, on the three named twisted tori -- `6^3` at twist `(0,0,0)` and `8^3`, `12^3` at `(1,1,1)` (T1); the coupled `2x2x2` Gauss sector and everything in T2, at `1e-10` Lanczos tolerance with the census exact integer arithmetic and **no truncation**; the exact `864`-state `2x2x2` ice component and the `4x2x2` rows of T3 items 1, 3 and 4 at the stated power-iteration residuals (`4.6e-12` at `Uc = 0`, `2.6e-7` at `Uc = 1`). T3 items 2 and 5 are stochastic witnesses at declared seeds. Every `L^3` row of the quoted production is a stochastic witness at a declared seed with P2's two systematics unchanged -- the population-control bias of the walker energies and the finite-`tau` windows of the decay rates, which are upper bounds on `omega`, the mechanism verified exactly by the `4x2x2` rows where `omega_eff` falls onto its limit from above -- and at `V_rk = 0` those rows carry `10`-`100` per cent errors on `omega` beyond `tau = 2`.

**Nothing is proved for the coupled model on any torus with `L >= 4` in any direction.** The coupled `4x2x2` sector was not built: the vacuum block alone is P2's `1,552,024` states and each of the `32` nearest-neighbour charge-pair patterns carries a link block of comparable size, so even the crudest truncation is about `5 x 10^7` states with about `10^9` adjacencies, above the `1` GB budget; nothing about `k = pi/2` in the coupled model is known here.

The **link role is designed** and the **law is declared** with `lambda` supplied. The **fermion, its hop, its Kawamoto-Smit signs and the twist conventions are supplied**. The **one-loop reading of `U_e` as a c-number background phase is supplied**, and is the reason T2 exists. The **Gaussian read-off `U = omega/(2 S_T)`** is a supplied translation of spectra into a stiffness. The **collinear stand-in `Uc sum_{pairs} E_b E_b'` is supplied**, its values are a scan and not a prediction, and it is **not** what the integrated-out fermion produces. No continuum limit is taken, no `T > 0` appears, no larger link spin appears, and **no claim is made that this `U(1)` is electromagnetism**. Nothing in this note is obtained from any axiom; the axioms are quoted to fix what "readable" means and for nothing else. No axiom text is amended, no hypothesis is adopted, no status value is set, and no premise registry, citation manifest or axiom-premise node is created or edited.

**What is read from records.** By the Record axiom only records are readable and a readout value is fixed by record content alone. `E_e` is a one-record value on the designed link site; `n_v`, `div E`, `G_v` and the winding `W_d` are record-diagonal and register. `S_T(k)` is a correlation among link records and is readable in that sense. The hop, the current, `U_e` and `P_f` carry `X` in every monomial and register only through correlations among records. A photon in the records would mean equal-time link-record correlations carrying `S_T(k) ~ |k|` at long wavelength rather than a flat `S_T`; neither the pure law nor the coupled law on `2x2x2` shows that.

## Honest-auditor read

An honest auditor should come away with three seed-free computations, all rebuilt by the runner from its own indexing. The one-loop polarisation of the half-filled pi-flux sea is exact linear algebra with a Ward identity at `1.5e-15`, an exactly longitudinal density response, and two induced couplings whose signs and logarithmic running are unambiguous -- and the sign that matters is the one that puts `kappa_E` in the *inverse* stiffness, so the sea screens. The coupled `2x2x2` sector is built complete at `303,721` states over all `70` charge patterns with no truncation, reproduces the parent note's three anchors to every digit, and shows the transverse-electric sector softening rather than stiffening as the hop turns on. The supplied stand-in is labelled supplied in every place it appears, and the exact `4x2x2` rows show what a real stiffness would do, which is the control the negative result needs. The costs are stated plainly: the carrier, the law, the fermion, the hop, the c-number reading of the link phase, the Gaussian read-off and the stand-in are declared and not obtained from anything; `lambda` is supplied; the coupled model is solved on one box only; **every `L^3` row is a witness**, and the `L = 6, 8` production rows are quoted with their seeds rather than recomputed. Four numbers depart from the source computation and each departure is stated with its arithmetic. Independent audit remains a separate lane.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. The runner is class-A for the exact rows: it rebuilds every geometry from its own indexing, compiles its two C engines from embedded source at run time into a private temporary directory, and trusts no binary and no external datum. Where no C compiler is available, the four C-dependent rows `C2`-`C5` report `SKIP` with the reason and the fourteen pure-Python rows still close at `FAIL = 0`.

Hard landing conditions are a fresh runner and cache pair closing at `FAIL = 0`, runtime inside the declared `AUDIT_TIMEOUT_SEC = 300` (measured `148`-`166` s across runs, `166.2` s in the cached one), and passing strict-lint, companion and changed-evidence gates. The runner's stdout is `6,232` characters over `20` lines, above the `5,500`-character convention; the convention is not a gate, and the excess is the per-row numbers that carry the evidence.

## Reproduction

```bash
python3 scripts/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.py
python3 - <<'PY'
import sys; sys.path.insert(0, 'scripts')
from runner_cache import execute_runner, write_cache, capture_runner_identity
rp = 'scripts/fermion_charge_coupling_screens_link_field_lambda_sign_check_2026_09_04.py'
res = execute_runner(rp, 300)
write_cache(rp, res, identity=capture_runner_identity(rp))
PY
```

The machine-written cache pins the runner SHA-256, carries the declared timeout, records a successful exit, reproduces every exact check, and ends at `TOTAL: PASS=18 FAIL=0`. No audit verdict is created or changed here.

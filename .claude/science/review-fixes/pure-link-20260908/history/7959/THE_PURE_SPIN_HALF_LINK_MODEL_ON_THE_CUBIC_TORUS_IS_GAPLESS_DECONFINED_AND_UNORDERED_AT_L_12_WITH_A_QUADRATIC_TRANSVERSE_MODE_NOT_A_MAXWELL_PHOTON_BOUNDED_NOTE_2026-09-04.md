---
claim_id: pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_2026_09_04
claim_type: bounded_theorem
claim_scope: "On THREE NAMED FINITE GEOMETRIES plus four complete path spaces, carrying ONE DESIGNED SPIN-1/2 LINK ROLE per edge in the conventions of PR #7911 and PR #7942 -- the fully periodic 2x2x2 torus (24 links, 8 vertices at z_v = 6, 24 faces, rho_v = 0), the fully periodic 4x2x2 torus (48 links, 16 vertices, 48 faces, rho_v = 0), and PR #7911's height-1 cylinder ladder at L = 8 with its declared staggered background -- for the ONE DECLARED PURE-GAUGE LAW H = -lambda sum_f P_f with P_f = W_f + W_f^dag the oriented four-link ring exchange, lambda supplied and set to 1, no matter, and the electric term a c-number at spin 1/2 by PR #7893's E_e^2 = I/4: (T1) [exact] the 2x2x2 Gauss sector has dimension 9600 and splits under single plaquette flips into 937 components with multiset 864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760; it carries 125 distinct winding vectors, no component straddles two of them, the zero-winding class is 880 = one 864-state component plus 16 frozen singletons, E_0 = -9.0267209135 with Delta_1 = 1.6276099336 and the ice component's internal gap 2.2257853859, and the full-sector first excitation is carried by exactly the six 464-state unit-flux classes W = +-e_d, so the cheapest excitation there is a flux state; the ground-state lattice-longitudinal structure factor is zero at every k. (T2) [exact] the ladder at L = 8 has dim(Gauss) = 49 in components 47, 1, 1, with E_0 = -4.8309586723, internal gap 0.9726557606, <P_f> = 0.6038698340, and its declared staggered order is an exact plateau <psi_0|O|psi_0>^2 = 0.7353 of the k = pi top-link correlator. (T3) [exact] the 4x2x2 Gauss sector has dimension 23,063,296 and 405 distinct winding vectors; its zero-winding class of 1,552,024 states is ONE flip-connected component of 1,551,976 states plus 48 frozen states and nothing else, so the 937 of 2x2x2 is a smallest-box artefact and the winding vector is what separates sectors; on that component E_0 = -16.7037885782, <n_app>_0 = 19.0690013962, <P_f> = 0.3479955954, the lattice-longitudinal S_L(k) is zero to machine precision at k = pi/2 and pi while S_yy = S_zz = 0.1044875978 and 0.1815941329, and the exact transverse-electric decay rates are 2.566 at k = pi/2 and 2.891 at k = pi, approached from above. (T4) [exact] on the COMPLETE path spaces of a 7-state ladder component (N = 4 and N = 6) and of the 6- and 36-state 2x2x2 components (N = 5 and N = 3) -- 935, 11,119, 4,790 and 10,020 paths -- the open-path projector's symmetric chain satisfies detailed balance and stationarity to 1e-18 for pi(path) = delta^{#moves}/Z and is irreducible, its bounce chain satisfies global and skew balance to 1e-18 and is irreducible while violating plain detailed balance, the middle-state marginal matches the exact finite-N formula to 1e-14, and every state on every path satisfies G_v = 0. (T5) [witness, declared seeds] both samplers reproduce the exact anchors of T1-T3 within about 2 sigma at the declared seeds, the reptation head visits exactly the 864 and 47 states of the accessible components and never leaves them, and the walker method's population-control bias against the exact 4x2x2 energy is +0.024, +0.008, +0.005 at N_w = 400, 1600, 6400, falling with the walker count and always toward higher energy. EVERY L^3 ROW IS A WITNESS AND EVERY L >= 6 PRODUCTION ROW IS QUOTED, NOT RECOMPUTED: at L = 4, 6, 8, 10, 12 the quoted stochastic rows give omega(k_min) = 1.3, 0.80, 0.5, 0.32, 0.20 with no saturation, a unit-flux energy falling 0.71 -> 0.15(8) -> 0.15(20) instead of the confining sigma L = 1.06, 1.42, no growing Bragg peak, and omega about 0.78 k^2 with a flat S_T(k_min) = 0.30-0.38, i.e. a quadratic Lifshitz / Rokhsar-Kivelson-type soft mode rather than the sister lane's Maxwell photon at these momenta. The link role is designed, not derived; lambda is supplied; the background convention on the ladder is PR #7911's. NOTHING IS PROVED FOR ANY L^3 TORUS WITH L >= 4, no continuum limit is taken, no T > 0, no matter, no larger link spin, and no claim is made that this U(1) is electromagnetism. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py
---

# The pure spin-1/2 link model on the cubic torus is gapless, deconfined and unordered at `L <= 12`, with a quadratic transverse mode and a flat transverse structure factor: an open-path projector that evades the plaquette-parity obstruction, certified on three exact geometries

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py`](../scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.txt`](../logs/runner-cache/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7942 proved that the natural operator-pair update of a stochastic series expansion for `H = -lambda sum_f P_f` conserves the flip parity of every face, and named a loop or cluster update as
what a correct three-dimensional sampler would need. That obstruction is a property of **closed** operator strings. This note takes the other way out -- an **open-path** projector, whose ends are
free, so no parity-changing update is required -- and certifies it on complete path spaces rather than by validation alone. With two independent projectors built on it, the three-dimensional
question PR #7911 left open gets an answer at the sizes reached: the link sector is gapless, deconfined and unordered at `L <= 12`, and its soft transverse mode is **quadratic**, not the linear
Maxwell mode of the sister lane. A third exact geometry, the `4x2x2` torus at 23 million states, also corrects PR #7942's sector bookkeeping: the `937` components are a smallest-box artefact.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-geometry theorems about one declared pure-gauge law on one designed spin-1/2 link role per edge: the Gauss-sector censuses of the 2x2x2 and 4x2x2 tori and of the L = 8 ladder, the winding decomposition of each, the placement of the first excitation, the exact ground-state energies, structure factors and transverse decay rates, and the balance certificates of the open-path projector on complete path spaces. The census, component and winding items are integer and bit arithmetic with no floating-point step; the spectral, structure-factor and balance items are floating-point at the stated tolerance. Every L^3 row is a witness at a declared seed and is labelled so; the L = 6, 8, 10, 12 production rows are quoted from the source computation and are not recomputed by the runner."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on the exact finite-geometry theorems, and route to its owner the question this note does not decide: whether omega proportional to k^2 is the asymptotic dispersion of the pure plaquette law or a crossover above a linear regime at k < pi/6, for which the named ingredient is an electric stiffness U > 0 that the spin-1/2 c-number E_e^2 = 1/4 cannot supply."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of `T1`-`T5` below, exactly the runner's check groups `A`-`F`. Groups `A`, `B`, `C` and `D` are exact and seed-free -- `A1`, `A2`, `B1`, `C1`, `C2` and `D1` integer
and bit arithmetic with no floating-point step, the rest floating-point at the stated tolerance. Group `E` rows are `[witness]` at declared seeds. Group `F` is `[declared]`: it states the quoted
`L^3` production rows and checks only the arithmetic read off them.

1. `T1` (`A`). The `2x2x2` census, its winding decomposition, and the flux placement of the first excitation.
2. `T2` (`B`). The `L = 8` ladder and its exact staggered plateau.
3. `T3` (`C`). The `4x2x2` census, its one-component result, `E_0`, `S_L = 0`, and the exact transverse decay rates.
4. `T4` (`D`). The open-path projector's balance certificates on complete path spaces.
5. `T5` (`E`), `W1`-`W4` (`F`). The sampler validations, and the quoted `L^3` rows.

## Imports and authority

Imported scientific authority: none load-bearing. The quantum-link (gauge-magnet) presentation, the ring-exchange plaquette term, reptation and Green's-function projector Monte Carlo with
population control and forward walking, and the Lifshitz / Rokhsar-Kivelson vocabulary are standard methodology; **every object is redeclared here and every exact statement is recomputed by the
runner**, the samplers included -- their C source is embedded in the runner and compiled at run time, so no binary and no external datum is trusted. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, no grade and no dependency weight:

- `THE_LINK_MODELS_PAIR_UPDATE_CONSERVES_PLAQUETTE_PARITY_AND_THE_2X2X2_GAUSS_SECTOR_SPLITS_INTO_937_WINDING_COMPONENTS_BOUNDED_THEOREM_NOTE_2026-09-04.md` (open PR #7942): the parity obstruction
  this note answers, the `2x2x2` census it reproduces, and the sector-internal versus full-sector gap distinction it carries forward. Three of its readings are revised in "Where this note
  disagrees with PR #7942".
- `THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7911): the conventions used here verbatim, the ladder
  geometry and its declared staggered background, and the three-dimensional question this note answers at `L <= 12`.
- `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893): the link algebra and `E_e^2 = I/4`, which is why
  the electric term supplies no dynamics at spin 1/2, and the matter hop named as one candidate stiffness.
- The sister lane's compact `U(1)` Maxwell-germ notes, open: PR #7887 "Record-distribution overlap forces a positive Maxwell germ", PR #7886 "representation-positive Record kernels force a
  Maxwell germ", PR #7884 "compact U1 Maxwell quadratic-basin universality". They supply the sense of "photon" this note measures against: two transverse modes with `omega = c|k|` in the smooth
  limit of a supplied positive plaquette action.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms, quoted in "Setting" and nowhere used as a premise.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site." **Qubit**: "Each site has a domain of local possibilities." and "The full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is
one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." **Record**: "Records form.", "When present, a record locks exactly one admissible
local possibility.", "A site never carries more than one record; records are permanent.", "Only records are readable." and "A readout value is determined by record content alone."

**The supplied surface.** The `U(1)` carrier is PR #7893's **designed role**: one further two-state site per edge, assigned by design. `E_e = Z^L_e/2` is a one-record value on that site, so the
flux registers -- it is record content, readable by the Record axiom -- while `U_e` and `P_f` carry `X` in every monomial, have no record-diagonal part, and register only through correlations
among records. Composition is **ordinary** throughout. The law `H = -lambda sum_f P_f` is declared with `lambda` supplied and set to `1`; the tori, the ladder's staggered background and the
winding sectors sampled are declared. **Nothing below is derived from any axiom.**

## Definitions

```text
E_e = (1/2) Z^L_e   (eigenvalues +-1/2),      U_e = (X^L_e + i Y^L_e)/2 = sigma^+_e
(div E)_v = sum_{e at v} s_{v,e} E_e,         s_{v,e} = +1 out of v, -1 into v
G_v = (div E)_v - rho_v,       rho_v = a STATIC background charge (no matter, so no n_v)
W_f = the oriented four-link ring product,    P_f = W_f + W_f^dag
H = -lambda sum_f P_f                                          THE DECLARED PURE-GAUGE LAW
rho_v = 0 on every torus (z_v = 6 even);  2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i on the ladder
W_d = sum over links (v,d) with v_d = 0 of e/2                 THE WINDING VECTOR
A = -H/lambda = the adjacency matrix of the plaquette-flip graph;  B = I + delta A
```

`P_f` is **applicable** iff `b_p = b_q`, `b_u = b_w` and `b_p != b_u` on its ordered quadruple, and its action is the XOR of the four link bits. `n_app(s)` counts applicable faces; a state with
`n_app = 0` is **frozen**. The **ice configuration** is `e(v,x) = (-1)^{v_y+v_z}` and cyclic, which has `G_v = 0` on any even `L^3` torus with exactly half its faces applicable. `S_E(k)` is the
electric structure factor per site; its **lattice-longitudinal** part is `S_L = K* S K / |K|^2` with `K_d = 1 - e^{i k_d}`, and `S_T = tr S - S_L`.

**The open-path projector, declared.** `B = I + delta A` has the eigenvectors of `H`, eigenvalues `1 + delta a_n`, and its Perron vector is the sector ground state. A path `s_0 -> ... -> s_N` of
`N` steps, each a stay of weight `1` or a single plaquette flip of weight `delta`, is weighted `delta^{#moves}`; with uniform trial ends `Z = 1^T B^N 1`, the middle of a long path is distributed
as `psi_0^2` and the ends as `psi_0`. **Reptation** grows one end from the heat-bath proposal `q(s'|s) = B_{ss'}/(1 + delta n_app(s))` and shrinks the other, accepting with
`min(1, (1 + delta n_app(old head))/(1 + delta n_app(new tail)))`, in a symmetric mode and a bounce mode. **Interior updates** are (i) the exchange of two adjacent commuting steps, weight
unchanged, and (ii) insertion or deletion of a same-face flip pair, which changes per-face flip counts by `0` or `2`. The parity change PR #7942 needs is supplied by the free ends, which is why no
parity-changing update appears here. The **second projector** samples `e^{tau A}` by `N_w` walkers with continuous-time flips, fixed-population reconfiguration and forward-walking ancestry
buffers. Gauss's law holds by construction (only `P_f` is ever applied) and is re-verified from the incidence lists throughout.

## Theorem 1 -- the 2x2x2 census and the flux placement of the first excitation

**Conclusion.** (1) `[exact]` `dim(Gauss) = 9600` at `rho_v = 0`, every state re-derived with `max |2 (div E)_v| = 0`; under single plaquette flips it splits into `937` components with the full
size multiset `864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760`. (2) `[exact]` The sector carries `125` distinct winding vectors, **no component straddles two of them**, and the
zero-winding class is `880 = 864 + 16`: one flip component -- the ice configuration's, with `G_v = 0`, `12/24` faces applicable and `W = 0` -- plus `16` frozen singletons. (3) `[1e-9]`
`E_0 = -9.0267209135` and `Delta_1 = 1.6276099336` on the full sector; the ground state lies in the `864`-state component, whose own `E_0` agrees exactly and whose internal gap is `2.2257853859`,
larger by `36.8` per cent. (4) `[1e-9]` The full-sector first excitation is a **flux state**: `Delta_1` is carried by exactly `6` components, each of `464` states and each a unit-flux class
`W = +-e_d`. (5) `[1e-9]` In the ground state the lattice-longitudinal `S_L(k)` is `1.4e-49` at every one of the seven non-zero `k`, the transverse `S_yy = S_zz = 0.25303701` at `(pi,0,0)`, and
the lowest level carrying transverse-electric weight sits at `E - E_0 = 2.5172790443`.

**Proof.** Item 1 builds the sector by a slab sweep enforcing `G_v = 0` at each site, re-derives `2 (div E)_v` from the listed bit patterns, and takes connected components of the flip graph. Item 2
evaluates the declared winding sum on every state and intersects the classes with the components. Items 3 to 5 diagonalise every component densely -- the largest is `864 x 864` -- sort the union of
the spectra, and locate `Delta_1` by matching levels against each component's spectrum. Items 1 and 2 are exact integer and bit arithmetic; items 3 to 5 are `[1e-9]`.

## Theorem 2 -- the ladder at L = 8

**Conclusion.** `[1e-9]` PR #7911's height-1 cylinder at `L = 8` has `dim(Gauss) = 49` with `max |G_v| = 0`, splitting into `3` components of sizes `47, 1, 1`; on the `47`-state one
`E_0 = -4.8309586723`, the internal gap is `0.9726557606` and `<P_f> = 0.6038698340`. Its declared staggered order is an **exact plateau, not a decay**: with `O = sum_i (-1)^i E(T_i)/sqrt(L)`, the
`k = pi` correlator `C(m) = <O B^m O>/lambda_B^m` saturates at `<psi_0|O|psi_0>^2 = 0.73525596`, reached to `1e-8` by `m = 40`.

**Proof.** Column transfer builds the sector, components of the flip graph split it, and dense diagonalisation of the `47`-state one gives the spectrum. The plateau is the ground-state expectation
squared, cross-checked against the finite-`m` lazy correlator.

## Theorem 3 -- the 4x2x2 torus: one component per winding class

**Conclusion.** (1) `[exact]` `dim(Gauss) = 23,063,296`, enumerated site by site, sorted, all distinct, with `0` Gauss violations on re-derivation; the sector carries `405` distinct winding
vectors, the zero-winding class `1,552,024` states, `W = (1,0,0)` `477,888` and `W = (0,1,0) = W = (0,0,1)` `1,101,696`. (2) `[exact]` **The zero-winding class is ONE flip-connected component of
`1,551,976` states plus `48` frozen states and nothing else** -- breadth-first depth `17` from the ice configuration, remainder exactly `0`, `46,264` frozen states in the whole sector -- and that
component is closed under flips: `21,578,752` adjacencies, `0` missing targets. (3) `[1e-9]` On it `E_0 = -16.7037885782`, `<n_app>_0 = 19.0690013962`, `<P_f> = 0.3479955954`, the mixed estimator
agreeing with `E_0`. (4) `[1e-8]` `S_L(k) = S_xx(k)` is `0.0e+00` -- zero to machine precision, not to a tolerance -- at `k = (pi/2,0,0)` and `(pi,0,0)`, while `S_yy = S_zz = 0.1044875978` and
`0.1815941329`. (5) `[1e-3]` The exact transverse-electric decay rates are `2.566` at `k = pi/2` and `2.891` at `k = pi`, approached **from above**: `omega_eff = 2.5994, 2.5691, 2.5662` and
`2.9209, 2.8923, 2.8905` at `m = 40, 80, 120`.

**Proof.** The runner's embedded C engine, compiled at run time, enumerates the sector by the same site-by-site assignment, sorts it, re-derives `G_v` on every state, computes the winding vector and
`n_app` of every state, grows the breadth-first component of the ice configuration, builds the component's adjacency in compressed sparse rows by binary search, and finds the Perron vector of
`B = I + A` by power iteration (`219` iterations, Rayleigh residual `4.6e-12`). Structure factors are ground-state expectations of diagonal operators; the decay rates are ratios of the exact lazy
correlator `C(m) = <o|B^m|o>/lambda_B^m` with `delta = 0.25` and `o = E_mu(k) psi_0`. Items 1 and 2 are exact integer and bit arithmetic; items 3 to 5 are floating-point at the stated tolerance.
Peak memory is under `400` MB and no dense matrix is formed.

## Theorem 4 -- the open-path projector, certified on complete path spaces

**Conclusion.** On the **complete** path spaces of the `7`-state ladder-`L = 4` component (`N = 4`, `935` paths; `N = 6` at `delta = 0.3`, `11,119` paths) and of the `6`- and `36`-state `2x2x2`
components (`N = 5`, `4,790` paths; `N = 3`, `10,020` paths): (1) `[exact]` every state on every path satisfies `G_v = 0` and every step is a single four-link plaquette flip. (2) `[1e-18]` The
symmetric chain is exactly reversible with respect to `pi(path) = delta^{#moves}/Z` -- row sums `1` to `2e-16`, detailed balance `1.1e-19`, stationarity `8.7e-19` -- and irreducible, one strongly
connected component on each path space, so `pi` is its unique stationary law. (3) `[1e-18]` The bounce chain is the expected **non-reversible** chain and is certified by global balance `4.3e-19`
and skew detailed balance `2.2e-19` on the lifted space `(path, direction)`, irreducible, while plain detailed balance fails by up to `7.7e-04`. (4) `[1e-14]` The middle-state marginal of `pi`
equals the exact finite-`N` value `1^T B^j e_s e_s^T B^{N-j} 1 / Z` to `4.0e-15`, so the middle of a long path carries `psi_0^2` and the ends `psi_0`. (5) `[exact]` The ergodicity ceiling: a
plaquette flip conserves the winding vector, so a chain started on the `2x2x2` ice configuration reaches exactly `864` states and one on the ladder's dynamical component exactly `47`, and no more.

**Proof.** Each path space is built completely by recursion, each path weighted `delta^{#moves}`, and the forward and backward transition matrices assembled sparsely from the declared proposal and
acceptance. Balance is the maximum entry of `D_pi T - (D_pi T)^T` and of `pi T - pi`; irreducibility is the strongly connected component count of the sparsity pattern; the marginal is compared to
dense powers of `B` on the component (at most `36 x 36`). All items are exact constructions evaluated in floating point at the stated tolerance.

## Theorem 5 -- both projectors against the exact anchors

**Conclusion.** `[witness, declared seeds]` At seed `20260904`, reptation on the `2x2x2` ice component (`delta = 0.5`, `N = 200`, bounce, `1e5 + 2e6` moves) gives `E_mix`, move fraction and
`<n_app>_bulk` at `-1.56, -0.44, -0.46` sigma from the exact finite-`N` anchors, with the head visiting **exactly** `864` states and `gauss_err = replay_err = 0`; on the ladder, `-0.06, 0.61,
-0.25` sigma with exactly `47` states visited. At seed `20260921`, the same engine on the `1,551,976`-state `4x2x2` component (`delta = 0.25`, `N = 600`, `2e5 + 3e6` moves) sits at `-0.20, -0.45,
-0.17` sigma from T3's exact values with sampled `S_L = 0`. At seed `20260930`, the walker method on `2x2x2` (`N_w = 1600`, `tau = 20 + 400`) gives `E_mix` and `E_growth` at `1.44` and `1.33`
sigma and forward-walked pure `S_T(pi,0,0)` at `-1.13` and `0.45` sigma. At seed `20260931`, its **population-control bias** against T3's exact `E_0` is `+0.024, +0.008, +0.005` at
`N_w = 400, 1600, 6400` -- `0.14, 0.05, 0.03` per cent of `|E_0|` -- **falling with the walker count and always toward higher energy**. One short `L = 4` run at seed `20261001` gives
`E_mix = -56.105(85)` and `E_growth = -56.108(82)`, agreeing to `0.04` sigma, with `S_L = 3e-33` and `gauss_err = 0`.

**Proof.** Both engines are compiled by the runner from embedded C at the declared seeds and run lengths, and each estimator's bin mean and standard error over bins is compared to T1-T3. These are
witnesses, reproducible from the declared seeds and nothing beyond that; where no C compiler is available they report `SKIP`, and so does T3, whose 23-million-state enumeration needs the engine.

## The production rows W1-W4 -- quoted witnesses, not recomputed

The `L = 4, 6, 8, 10, 12` production of the source computation (walker method, seeds `20261001`-`20261020` and `20261101`-`20261114`, `tau_prod` `130`-`230`, `N_w = 500`-`8000`, `30` bins) costs
hours of core time and is **quoted here with its seeds and run lengths, not recomputed by the runner**; only one short `L = 4` run is executed, as T5. Group `F` checks the arithmetic read off the
quoted rows and nothing more.

- **W1 -- gapless.** `omega(k_min) = 1.3, 0.80, 0.5, 0.32, 0.20` at `L = 4, 6, 8, 10, 12`, falling monotonically with no sign of saturation, every effective-energy curve flat or falling in `tau`.
  A gapped link sector would hold `omega(k_min)` at its gap.
- **W2 -- deconfined.** The unit-flux energy falls `0.71 -> 0.15(8) -> 0.15(20)` at `L = 4, 6, 8`, where a confining string of the `L = 4` tension needs `sigma L = 1.06` and `1.42` -- excluded by
  `12.0` and `6.3` sigma. The fall beats Coulomb `1/L` (`0.47`) and fits `1/L^2` (`0.31`, `2.2` sigma), and `E(2)/E(1) = 4.1(9)` at `L = 6` is the quadratic value `4`, not the string value `2`.
- **W3 -- unordered.** No Bragg peak: the largest `S_T(k)` over the zone **falls** `1.49 -> 1.08` from `L = 4` to `12`, and `S_T(pi,pi,pi)` itself `1.49 -> 1.05`, where a plaquette solid would
  make either grow by the site factor `27`; the per-site measure at
  the ice ordering vector falls `0.0152 -> 0.0005`, a factor `30.4` against the `1/N_s` factor `27.0` of a liquid; `S_L(k) = 0` identically at every `k` on every torus.
- **W4 -- quadratic, not Maxwell, at these momenta.** `omega` is about `0.78 k^2` with `omega/k^2 = 0.73, 0.75, 0.80, 0.77` for `L = 6`-`12` while `omega/k` halves, and `S_T(k_min)` is flat at
  `0.30`-`0.38` from `k = pi/2` to `pi/6`. A Maxwell photon has `omega = c|k|` and `S_T` proportional to `|k|`, which would fall by a factor `2.73` across that range. The winding sector does not
  change this: the `W = 1` chains give the same `omega(k_min)` and the same flat `S_T` at every `L`. The energy density is `E_0/N_p = -0.287(3)`.

## Corollary -- what is decided at L <= 12, and what is not

**Decided**, within the declared setting and at the sizes reached, as witnesses anchored on three exact geometries: the pure link sector is **gapless**, **deconfined** and **unordered**, and at
these momenta it is **not the sister lane's Maxwell photon** -- the soft transverse mode is quadratic and the equal-time transverse structure factor is flat, the Lifshitz / Rokhsar-Kivelson form,
in a Hamiltonian that carries no Rokhsar-Kivelson potential term. Two of the three exact geometries make the sampled `S_L(k) = 0` a theorem rather than a fit, and the `4x2x2` decay rates show why
every finite-`tau` plateau is an upper bound on `omega`.

**Not decided**: whether `omega` proportional to `k^2` is the asymptotic dispersion or a crossover above a linear regime at `k < pi/6`, which `L <= 12` cannot separate; the thermodynamic value of
the `k^2` coefficient beyond the roughly `15` per cent spread of the plateaus; the flux energies at `L >= 10`, where the differences are unresolved at `+-0.4`-`0.6`; anything at `T > 0`, with
matter, or at larger link spin.

**Reading, labelled as such.** A linearly dispersing transverse mode needs an electric stiffness `U > 0` in front of `E^2` in the coarse-grained energy, together with the magnetic term the ring
exchange already supplies. At spin `1/2` the electric term is the c-number `E_e^2 = 1/4` and supplies none, and the flat `S_T(k)` is exactly the statement that the ground state pays nothing for
long-wavelength electric textures -- which is what makes the mode quadratic. Two candidates for supplying `U` are named and neither is computed here: the coupling to the fermion's charge of
PR #7893, which makes the electric energy dynamical through Gauss's law, or a larger link representation in which `E^2` is an operator. A Rokhsar-Kivelson potential term moves the coupling
**toward** `z = 2`, not away from it. Confinement is not the obstacle at these sizes; what is missing for a Maxwell photon is a stiffness.

## Where this note disagrees with PR #7942

1. **The parity obstruction is a property of closed operator strings, not of the model.** PR #7942's rank-`10` statement stands exactly as proved. What does not follow is that a loop or cluster
   update is required: an open-path projector needs no parity-changing update at all, because its ends are free and its interior updates change per-face flip counts by `0` or `2`. T4 certifies
   that chain on complete path spaces, and T5 runs it. The loop or cluster update PR #7942 names is therefore one way among others.
2. **The `937` components are a smallest-box artefact.** T3 shows that at `4x2x2` a winding class is **one** flip-connected component up to isolated frozen states -- `1,552,024 = 1,551,976 + 48`,
   remainder exactly zero. The object that separates sectors is the winding vector, not a component label; at `2x2x2` the doubled links make many small classes, and that is a property of the box.
   This is a statement about two geometries, not a theorem for all `L`.
3. **The question was posed as "gapless photon or gapped".** The answer at `L <= 12` is neither of the two anticipated forms: gapless, but with a quadratic soft mode and a flat transverse
   structure factor.

## Where this note departs from its source computation

- The certificate's middle-state marginal is quoted at `2e-15` in the source and is `4.0e-15` here, a summation-order difference in the path enumeration; the tolerance carried in T4 is this
  note's own `1e-14`.
- The source's `omega/k^2` table (`0.73, 0.75, 0.80, 0.77`) is built from the per-component plateaus with their run spread. Recomputing from the rounded `omega(k_min)` row that W1 quotes gives
  `0.73, 0.81, 0.81, 0.73`, mean `0.77` -- the same flatness and the same coefficient, `11` per cent spread rather than `9`.
- The source states that a Maxwell photon's `S_T` proportional to `|k|` would fall by a factor `2.3` across `k = pi/2` down to `pi/6`. On the lattice measure `2 sin(k/2)` the factor for that
  range is `2.73`; `2.3` is the factor for `pi/2` down to `pi/5`. W4 and the runner carry `2.73`.
- The `L = 6, 8, 10, 12` production is quoted, not rerun; the runner executes one short `L = 4` run instead, which lands above the quoted `L = 4` row by the population-control bias T5 measures.

## Reading, not theorem

Give every link one unit of flux either way so that as much flows into each vertex as out, and let the faces flip. On the smallest cube the allowed configurations fall into many separate families,
but that is the smallest cube talking: on the next box up, everything with the same net flux around the torus is one family, and only a handful of stuck configurations sit apart. Sampling this
without breaking anything turned out not to need the clever update the previous note asked for -- an open strip of history with two loose ends does the job, and the loose ends can be checked by
listing every possible strip and verifying the arithmetic exactly. Run that on boxes up to twelve across and the field has no gap, does not pull charges back together, and settles into no ordered
pattern. But the cheap wave it does carry goes as the square of its wavelength number, not the first power, and its equal-time strength does not fade at long wavelength. Light goes as the first
power. So this is a soft, liquid, deconfined thing, and at these sizes it is not light; what light would need, and what spin one-half cannot pay for, is a cost for spreading the electric field out.

## Interfaces named for other lanes, not moved here

- **PR #7942**, the parity obstruction: its rank statement is used unchanged, and its update requirement is answered by a representation rather than by a new closed-string update.
- **PR #7911**, the ladder and the three-dimensional question: the question is answered at `L <= 12` and left open beyond.
- **PR #7893**, the matter hop: named as one candidate electric stiffness, not computed.
- **The sister lane's Maxwell germ** (PRs #7887, #7886, #7884): supplies the definition of "photon" measured against here. Whether its supplied positive plaquette action and this pure spin-1/2
  link law describe the same object at long wavelength is not settled here.
- **Larger link spins and `T > 0`**: outside this note entirely.

## Executable claim block

```text
setting: 2x2x2 and 4x2x2 periodic tori (rho_v = 0, z_v = 6) and PR #7911's height-1 ladder at L = 8 (2 rho(t_i) = (-1)^i); ONE DESIGNED spin-1/2 link role per edge; no matter; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md and used as no premise
law: E_e = Z^L_e/2, U_e = sigma^+_e, G_v = (div E)_v - rho_v, P_f = W_f + W_f^dag, H = -lambda sum_f P_f with lambda supplied and set to 1; electric term a c-number by E_e^2 = I/4
t222_census: [bounded_theorem] dim(Gauss) = 9600, max Gauss residual 0; 937 flip components, multiset 864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760; 125 winding vectors; 0 components straddle two of them; zero-winding class 880 = one 864-state component + 16 frozen singletons
t222_spectrum: [bounded_theorem] E_0 = -9.0267209135, Delta_1 = 1.6276099336, ice-component internal gap 2.2257853859 (larger by 36.8 per cent); Delta_1 carried by exactly the six 464-state unit-flux classes W = +-e_d, so the cheapest excitation is a flux state; S_L(k) = 1.4e-49 at every non-zero k; S_yy = S_zz = 0.25303701 at (pi,0,0); lowest transverse-E level at 2.5172790443
ladder: [bounded_theorem] dim(Gauss) = 49 in components 47, 1, 1; E_0 = -4.8309586723, gap 0.9726557606, <P_f> = 0.6038698340; exact k = pi staggered plateau <psi_0|O|psi_0>^2 = 0.73525596, reached to 1e-8 by m = 40
t422_census: [bounded_theorem] dim(Gauss) = 23,063,296, 0 Gauss violations, 405 winding vectors; zero-winding class 1,552,024 = ONE flip component of 1,551,976 (breadth-first depth 17) + 48 frozen, remainder 0; component closed under flips, 21,578,752 adjacencies, 0 missing targets; 46,264 frozen states in the sector
t422_exact: [bounded_theorem] E_0 = -16.7037885782, <n_app>_0 = 19.0690013962, <P_f> = 0.3479955954; S_L(k) = 0 to machine precision at k = pi/2 and pi; S_yy = S_zz = 0.1044875978 and 0.1815941329; exact transverse decay rates 2.566 at pi/2 and 2.891 at pi, approached FROM ABOVE (2.5994, 2.5691, 2.5662 and 2.9209, 2.8923, 2.8905 at m = 40, 80, 120)
projector_certificate: [bounded_theorem] on COMPLETE path spaces of 935, 11,119, 4,790 and 10,020 paths: symmetric chain detailed balance 1.1e-19 and stationarity 8.7e-19 for pi = delta^{#moves}/Z, irreducible; bounce chain global balance 4.3e-19 and skew detailed balance 2.2e-19, irreducible, plain detailed balance violated by 7.7e-04; middle-state marginal to 4.0e-15; G_v = 0 on every state of every path; ergodicity ceilings 864 and 47
validation: [witness, seeds 20260904, 20260921, 20260930, 20260931, 20261001] reptation within 1.56 sigma on 2x2x2, 0.61 on the ladder, 0.45 on 4x2x2, visiting exactly 864 and 47 states with gauss_err = 0; walker method within 1.44 sigma on 2x2x2; population-control bias +0.024, +0.008, +0.005 at N_w = 400, 1600, 6400, falling with the walker count, always toward higher energy
production_quoted: [witness, QUOTED not recomputed; seeds 20261001-20261020 and 20261101-20261114, tau_prod 130-230, N_w = 500-8000, 30 bins] omega(k_min) = 1.3, 0.80, 0.5, 0.32, 0.20 at L = 4-12 with no saturation; unit-flux energy 0.71 -> 0.15(8) -> 0.15(20) against sigma L = 1.06, 1.42, excluded by 12.0 and 6.3 sigma, E(2)/E(1) = 4.1(9); largest S_T over the zone falls 1.49 -> 1.08 and S_T(pi,pi,pi) falls 1.49 -> 1.05, where an ordered pattern needs a factor 27 growth; omega about 0.78 k^2 with omega/k^2 = 0.73, 0.75, 0.80, 0.77 while omega/k halves; S_T(k_min) flat at 0.30-0.38; E_0/N_p = -0.287(3)
claim_types: bounded_theorem for every exact row above (t222_census, t222_spectrum, ladder, t422_census, t422_exact, projector_certificate); witness for every L^3 row without exception, including all of production_quoted and the L = 4 run in validation
not_claimed: nothing is proved for any L^3 torus with L >= 4; no continuum limit, no T > 0, no matter, no larger link spin; no claim that this U(1) is electromagnetism; whether omega proportional to k^2 is asymptotic or a crossover above a linear regime at k < pi/6 is not decided
departures_from_pr7942: the parity obstruction is a property of closed operator strings, so an open-path projector needs no parity-changing update and the loop or cluster update named there is one way among others; the 937 components are a smallest-box artefact, the winding vector being what separates sectors at 4x2x2
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=27 FAIL=0 in 83.6 s with a C compiler present; PASS=16 FAIL=0 without one, the eleven C-dependent rows (group C exact, group E witness) reporting SKIP with the reason
```

## Proof boundary

Proved seed-free on **named finite geometries only**: the `2x2x2` torus (T1), the `L = 8` ladder (T2), the `4x2x2` torus (T3), and the ladder-`L = 4` and `2x2x2` sub-components whose complete path
spaces carry the balance certificate (T4). **Nothing is proved for any `L^3` torus with `L >= 4`.** Those rows are stochastic witnesses at declared seeds with **two declared systematics**: the
population-control bias of the walker method's energies, measured here at `0.14, 0.05, 0.03` per cent against the exact `4x2x2` energy and always toward higher energy, so the `L = 10, 12` rows at
`N_w = 2000` carry an unremoved bias of roughly `0.002`-`0.003` per face; and the **finite-`tau` windows** of the decay rates, which are upper bounds on `omega` -- the mechanism verified exactly in
T3, where `omega_eff` falls onto `2.566` and `2.891` from above. The bin-merging test of the source grows the quoted error bars by up to a factor `2` at the largest merges, so every quoted error bar
is a lower bound by that factor.

The **link role is designed**: one further two-state site per edge, assigned by a design rule. The **law is declared** with `lambda` supplied. The **background conventions are declared** and are
PR #7911's. Nothing in this note is derived from any axiom; the axioms are quoted to fix what "readable" means and to say why the carrier is a link qubit, and for nothing else. No axiom text is
amended, no hypothesis is adopted, no status value is set, and no premise registry, citation manifest or axiom-premise node is created or edited.

No continuum limit is taken, no matter appears, and **no claim is made that this `U(1)` is electromagnetism**. The comparison against the sister lane's Maxwell germ is a comparison of dispersion
and structure-factor forms **at the momenta reached**, `k = pi/2` down to `pi/6`, and says nothing about `k < pi/6`.

## Honest-auditor read

An honest auditor should come away with three exact geometries and four complete path spaces, all recomputed by the runner from scratch. The `2x2x2` Gauss sector is counted at `9600` in `937`
components with a fully listed multiset, its first excitation placed in the six unit-flux classes, and its longitudinal structure factor zero at every `k`. The `4x2x2` sector is counted at
`23,063,296` and its zero-winding class shown to be **one** flip component of `1,551,976` states plus `48` frozen ones -- which is what turns PR #7942's `937` into a smallest-box artefact -- with
`E_0`, both transverse structure factors and both transverse decay rates exact. The open-path projector is certified on complete path spaces to `1e-18`, so its stationary law is the intended one by
construction and not by validation. The costs are stated plainly: the link role, the law and the background conventions are declared, not derived; `lambda` is supplied; **every `L^3` row is a
witness**, and every `L >= 6` production row is quoted from the source computation rather than recomputed, with its seeds and run lengths; the two systematics of those rows are named and one of
them is measured here; and the physical conclusion -- gapless, deconfined, unordered, quadratic rather than Maxwell -- is a statement about `L <= 12`, not about the thermodynamic limit.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the context notes in "Imports and authority" are plain-text
pointers carrying no grade and no weight. The runner is class-A for the exact rows: it rebuilds every geometry from its own indexing, compiles its three C engines from embedded source at run time
into a private temporary directory, and trusts no binary and no external datum. Where no C compiler is available, the eleven C-dependent rows report `SKIP` with the reason and the sixteen pure
Python rows still close at `FAIL = 0`.

Hard landing conditions are a fresh runner and cache pair closing at `FAIL = 0`, runtime inside the declared `AUDIT_TIMEOUT_SEC = 300` (measured `83.6` s), and passing pipeline, strict-lint and
changed-evidence gates. The runner's stdout is `9,599` characters over `30` lines, above the `5,500`-character convention; the convention is not a gate, and the excess is the per-row numbers that
carry the evidence. Independent audit remains a separate lane.

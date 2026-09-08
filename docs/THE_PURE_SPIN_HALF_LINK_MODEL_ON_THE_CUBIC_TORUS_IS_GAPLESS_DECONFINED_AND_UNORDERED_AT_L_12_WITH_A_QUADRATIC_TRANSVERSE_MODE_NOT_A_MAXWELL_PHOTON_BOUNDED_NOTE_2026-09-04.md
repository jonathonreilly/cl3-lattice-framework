---
claim_id: the_pure_spin_half_link_model_on_the_cubic_torus_is_gapless_deconfined_and_unordered_at_l_12_with_a_quadratic_transverse_mode_not_a_maxwell_photon_bounded_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Conditional finite supplied spin-1/2 link model: exact 2x2x2 and 4x2x2 Gauss censuses, full 2x2x2 component spectra, zero-winding-only 4x2x2 connectivity, finite numerical structure factors/effective decay rates, and complete small Python reptation path certificates. The fixed seeds give bounded finite sampler witnesses with required real Gauss diagnostics and compiler coverage. L=4..12 quoted production rows remain unchanged, unverified historical inputs checked only arithmetically. No thermodynamic gaplessness, deconfinement, absence of all order, asymptotic quadratic law, coarse-stiffness obstruction or Maxwell-photon exclusion is established; no production error or upper bound is certified."
upstream_dependencies: []
runner: scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py
---

# Finite pure-link censuses and projector witnesses; larger-volume production remains unverified historical arithmetic

**Original checkpoint identifier (historical only):** `pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_2026_09_04`

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; formal claim audit is deferred
**Status:** conditional support for the supplied finite model; no physical phase or audit grade
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py`](../scripts/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.txt`](../logs/runner-cache/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7942 historically reported that the natural operator-pair update of a stochastic series expansion for `H = -lambda sum_f P_f` conserves the flip parity of every face, and named a loop or cluster update as
what a correct three-dimensional sampler would need. Those parent claims, including its rank statement, are unverified and unaccepted by this unit and are not premises of its proof. The local same-face pair operation changes each flip count by an even number. This note instead uses an **open-path** projector, whose ends are
free, so no parity-changing update is required -- and certifies it on complete path spaces rather than by validation alone. Two projector implementations are tested against finite anchors. The quoted larger-volume rows do not settle the three-dimensional phase or photon question. The `4x2x2` census at 23 million states establishes the stated connectivity only for its zero-winding class; the other 404 winding classes are counted but not traversed.

**Current correction (2026-09-08):** this live note supersedes the interpretation of the
[original note](../.claude/science/review-fixes/pure-link-20260908/history/7959/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_DECONFINED_AND_UNORDERED_AT_L_12_WITH_A_QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_BOUNDED_NOTE_2026-09-04.md) and [original cache](../logs/runner-cache/pure_spin_half_link_model_gapless_quadratic_mode_open_path_projector_check_2026_09_04.original-pure-link-20260908.txt); both remain byte-exact historical evidence.
The [dated correction overlay](../.claude/science/review-fixes/pure-link-20260908/CURRENT_CORRECTION.md) records all dispositions. The canonical cache above is produced by an actual final run after this note and its runner are frozen; its status and output are evidence, not an audit grade. Historical cache wording and totals do not certify the corrected source.

## Machine status

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite supplied spin-1/2 link model: exact 2x2x2 and 4x2x2 Gauss censuses, full 2x2x2 component spectra, zero-winding-only 4x2x2 connectivity, finite numerical structure factors/effective decay rates, and complete small Python reptation path certificates. The fixed seeds give bounded finite sampler witnesses with required real Gauss diagnostics and compiler coverage. L=4..12 quoted production rows remain unchanged, unverified historical inputs checked only arithmetically. No thermodynamic gaplessness, deconfinement, absence of all order, asymptotic quadratic law, coarse-stiffness obstruction or Maxwell-photon exclusion is established; no production error or upper bound is certified."
trace_class: upstream_support
target_claim_id: the_pure_spin_half_link_model_on_the_cubic_torus_is_gapless_deconfined_and_unordered_at_l_12_with_a_quadratic_transverse_mode_not_a_maxwell_photon_bounded_note_2026-09-04
target_blocker_text: "Thermodynamic, physical-readout and coarse-stiffness implications are unestablished; large-volume production provenance is unbound."
source_of_blocker_text: current_note_proof_boundary
reachability_to_target: conditional_on_supplied_model
artifact_role: theorem
next_trace_action: "Independent source review of this corrected conditional finite unit; keep the named provenance, readout and limit questions open. Formal claim audit is deferred."
conditional_surface_status: supplied_model_only
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of `T1`-`T5` below, exactly the runner's check groups `A`-`F`. Groups `A`, `B`, `C` and `D` are exact and seed-free -- the census portions of `A1`, `A2`, `B1`, `C1`, `C2` and `D1` integer
and bit arithmetic with no floating-point step, the rest floating-point at the stated tolerance. Group `E` rows are `[witness]` at declared seeds. Group `F` is `[declared]`: it states the quoted
`L^3` production rows and checks only the arithmetic read off them.

1. `T1` (`A`). The `2x2x2` census, its winding decomposition, and the flux placement of the first excitation.
2. `T2` (`B`). The `L = 8` ladder and its exact staggered plateau.
3. `T3` (`C`). The `4x2x2` census, its one-component result, `E_0`, `S_L = 0`, and the finite-m effective transverse rates.
4. `T4` (`D`). The open-path projector's balance certificates on complete path spaces.
5. `T5` (`E`), `W1`-`W4` (`F`). The sampler validations, and the quoted `L^3` rows.

## Imports and authority

Imported scientific authority: none load-bearing. The quantum-link (gauge-magnet) presentation, the ring-exchange plaquette term, reptation and Green's-function projector Monte Carlo with
population control and forward walking, and the Lifshitz / Rokhsar-Kivelson vocabulary are standard methodology; **every object is redeclared here and every exact statement is recomputed by the
runner**, the samplers included -- their C source is embedded in the runner and compiled at run time, so no binary and no external datum is trusted. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, no grade and no dependency weight:

- `THE_LINK_MODELS_PAIR_UPDATE_CONSERVES_PLAQUETTE_PARITY_AND_THE_2X2X2_GAUSS_SECTOR_SPLITS_INTO_937_WINDING_COMPONENTS_BOUNDED_THEOREM_NOTE_2026-09-04.md` (historical PR #7942): reported parity/rank claims, unverified and unaccepted here; the `2x2x2` census and sector-internal versus full-sector gap distinction are independently reconstructed in this unit. Three of its readings are revised in "Where this note
  disagrees with PR #7942".
- `THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7911): the conventions used here verbatim, the ladder
  geometry and its declared staggered background, and the three-dimensional question left open by both notes.
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
flux registers -- it is record content, readable by the Record axiom -- while `U_e` and `P_f` carry `X` in every monomial, have no record-diagonal part, and cannot be reconstructed from the same fixed Z-record distribution. The two Gauss-legal L=4 states `(|1365> +/- |1394>)/sqrt(2)` have identical complete Z probabilities and opposite plaquette expectation; an additional readout protocol is required, and permanent records are not overwritten. Composition is **ordinary** throughout. The law `H = -lambda sum_f P_f` is declared with `lambda` supplied and set to `1`; the tori, the ladder's staggered background and the
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

**The open-path projector, declared.** `B = I + delta A` has the eigenvectors of `H`, eigenvalues `1 + delta a_n`, and on a specified connected component with `delta>0`, its unique Perron vector is that component's ground state. Stays make the finite nonnegative matrix primitive; this does not identify the lowest energy among distinct components or make every other eigenvalue nonnegative. A path `s_0 -> ... -> s_N` of
`N` steps, each a stay of weight `1` or a single plaquette flip of weight `delta`, is weighted `delta^{#moves}`; with uniform trial ends `Z = 1^T B^N 1`, the middle of a long path is distributed
as `psi_0^2` and the ends as `psi_0`. **Reptation** grows one end from the heat-bath proposal `q(s'|s) = B_{ss'}/(1 + delta n_app(s))` and shrinks the other, accepting with
`min(1, (1 + delta n_app(old head))/(1 + delta n_app(new tail)))`, in a symmetric mode and a bounce mode. **Interior updates** are (i) the exchange of two adjacent commuting steps, weight
unchanged, and (ii) insertion or deletion of a same-face flip pair, which changes per-face flip counts by `0` or `2`. Free ends allow changes of endpoint state without requiring a closed-string parity-changing move, which is why no
parity-changing update appears here. The **second projector** samples `e^{tau A}` by `N_w` walkers with continuous-time flips, fixed-population reconfiguration and forward-walking ancestry
buffers. Gauss preservation is the intended update property. The corrected GFMC engine independently re-evaluates every vertex equation for all initialized walkers, at roughly 16 whole-population checkpoints after evolution and resampling, and for every final walker after all updates, regardless of dump flags. It reports nonzero per-phase state/equation counts and rejects a residual immediately; the actual Python API also requires those counts. This bounded cadence does not claim every intermediate flip was checked.

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

## Theorem 3 -- the 4x2x2 census and the zero-winding component only

**Conclusion.** (1) `[exact]` `dim(Gauss) = 23,063,296`, enumerated site by site, sorted, all distinct, with `0` Gauss violations on re-derivation; the sector carries `405` distinct winding
vectors, the zero-winding class `1,552,024` states, `W = (1,0,0)` `477,888` and `W = (0,1,0) = W = (0,0,1)` `1,101,696`. (2) `[exact]` **The zero-winding class is ONE flip-connected component of
`1,551,976` states plus `48` frozen states and nothing else** -- breadth-first depth `17` from the ice configuration, remainder exactly `0`, `46,264` frozen states in the whole sector -- and that
component is closed under flips: `21,578,752` adjacencies, `0` missing targets. (3) `[1e-9]` On it `E_0 = -16.7037885782`, `<n_app>_0 = 19.0690013962`, `<P_f> = 0.3479955954`, the mixed estimator
agreeing with `E_0`. (4) `[1e-8]` `S_L(k) = S_xx(k)` is `0.0e+00` -- zero to machine precision, not to a tolerance -- at `k = (pi/2,0,0)` and `(pi,0,0)`, while `S_yy = S_zz = 0.1044875978` and
`0.1815941329`. (5) `[1e-3]` The finite-m effective rates have rounded m=120 values `2.566` at `k = pi/2` and `2.891` at `k = pi`; the three computed points decrease: `omega_eff = 2.5994, 2.5691, 2.5662` and
`2.9209, 2.8923, 2.8905` at `m = 40, 80, 120`.

**Proof.** The runner's embedded C engine, compiled at run time, enumerates the sector by the same site-by-site assignment, sorts it, re-derives `G_v` on every state, computes the winding vector and
`n_app` of every state, grows the breadth-first component of the ice configuration, builds the component's adjacency in compressed sparse rows by binary search, and finds the Perron vector of
`B = I + A` by power iteration (`219` iterations, Rayleigh residual `4.6e-12`). Structure factors are ground-state expectations of diagonal operators; the decay rates are ratios of the exact lazy
correlator `C(m) = <o|B^m|o>/lambda_B^m` with `delta = 0.25` and `o = E_mu(k) psi_0`. Items 1 and 2 are exact integer and bit arithmetic; items 3 to 5 are floating-point at the stated tolerance.
Peak memory is under `400` MB and no dense matrix is formed.

## Theorem 4 -- the open-path projector, certified on complete path spaces

**Conclusion.** On the **complete** path spaces of the `7`-state ladder-`L = 4` component (`N = 4`, `935` paths; `N = 6` at `delta = 0.3`, `11,119` paths) and of the `6`- and `36`-state `2x2x2`
components (`N = 5`, `4,790` paths; `N = 3`, `10,020` paths): (1) `[exact]` every state on every path satisfies `G_v = 0` and every non-stay step is a single four-link plaquette flip; stays have unit weight. (2) `[1e-18]` The
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
`N_w = 400, 1600, 6400` -- `0.14, 0.05, 0.03` per cent of `|E_0|` -- **falling with the walker count and positive in these three runs, without a general sign or 1/N_w error law**. One short `L = 4` run at seed `20261001` gives
`E_mix = -56.105(85)` and `E_growth = -56.108(82)`, agreeing to `0.04` sigma, with `S_L = 3e-33` and `gauss_err = 0`.

**Proof.** Both engines are compiled by the runner from embedded C at the declared seeds and run lengths, and each estimator's bin mean and standard error over bins is compared to T1-T3. These are
witnesses, reproducible from the declared seeds and nothing beyond that; the required C-dependent checks cannot be waived. Missing or failed compilation, an engine error or a missing required diagnostic makes the unit incomplete with nonzero exit; a partial set of Python checks is not a successful full-unit cache.

## The production rows W1-W4 -- unverified historical arithmetic, not current witnesses

The `L = 4, 6, 8, 10, 12` production of the source computation (walker method, seeds `20261001`-`20261020` and `20261101`-`20261114`, `tau_prod` `130`-`230`, `N_w = 500`-`8000`, `30` bins) costs
hours of core time and is **quoted here with its seeds and run lengths, not recomputed by the runner**; only one short `L = 4` run is executed, as T5. Group `F` checks the arithmetic read off the
quoted rows and nothing more. No exact raw-bin/log/command/source/geometry/sector/window receipt binds those production rows to a preserved computation. The present embedded engine is not retroactive provenance. The quoted seeds, budgets and uncertainties below remain historical reported inputs, with no new production execution or verification.

- **W1 -- finite quoted frequencies.** `omega(k_min) = 1.3, 0.80, 0.5, 0.32, 0.20` at `L = 4, 6, 8, 10, 12`, falling monotonically with no sign of saturation, every effective-energy curve flat or falling in `tau`.
  These positive frequencies do not distinguish a small nonzero limiting gap, a crossover or a gapless limit.
- **W2 -- quoted flux-energy arithmetic.** The unit-flux energy falls `0.71 -> 0.15(8) -> 0.15(20)` at `L = 4, 6, 8`, where a confining string of the `L = 4` tension needs `sigma L = 1.06` and `1.42` -- giving the original naive fixed-reference ratios
  `12.0` and `6.3`; these are not calibrated sigma exclusions. They neglect the L=4 reference uncertainty and covariance, as well as autocorrelation, projection and population bias. The fall beats Coulomb `1/L` (`0.47`) and compares to `1/L^2` (`0.31`, naive fixed-reference ratio `2.2`, also not calibrated sigma), and `E(2)/E(1) = 4.1(9)` at `L = 6` is numerically close to `4`; this historical ratio does not decide confinement.
- **W3 -- quoted electric structure factors.** the largest `S_T(k)` over the zone **falls** `1.49 -> 1.08` from `L = 4` to `12`, and `S_T(pi,pi,pi)` itself `1.49 -> 1.05`, compared to the site factor `27`; electric two-point data do not measure all order parameters and cannot exclude plaquette-solid order; the per-site measure at
  the ice ordering vector falls `0.0152 -> 0.0005`, a factor `30.4` against the `1/N_s` factor `27.0` of a liquid; `S_L(k) = 0` identically at every `k` on every torus.
- **W4 -- finite form comparison, no phase or photon verdict.** `omega` is about `0.78 k^2` with `omega/k^2 = 0.73, 0.75, 0.80, 0.77` for `L = 6`-`12` while `omega/k` halves, and `S_T(k_min)` is flat at
  `0.30`-`0.38` from `k = pi/2` to `pi/6`. A separately supplied free quantum-Maxwell ground-state comparison uses `omega = c|k|` and `S_T` proportional to `|k|`, which would fall by a factor `2.73` across that range. The winding sector does not
  change this: the `W = 1` chains give the same `omega(k_min)` and the same flat `S_T` at every `L`. The energy density is `E_0/N_p = -0.287(3)`.

## Corollary -- finite results and unestablished physical implications

The actual finite censuses, full 2x2x2 spectra, zero-winding-only 4x2x2 connectivity, finite-m effective-rate values and selected path-space balances remain. The L=4..12 production rows are unverified historical arithmetic; even with exact provenance, finitely many positive frequencies, electric structure factors and flux energies would not prove thermodynamic gaplessness, deconfinement, absence of all order, a z=2 phase or exclusion of a later linear Maxwell regime. The quoted `0.78 k^2` coefficient, `15` per cent spread and unresolved L>=10 flux differences `+-0.4`-`0.6` retain their historical status.

The bare identity `E_e^2=I/4` does not forbid a coarse stiffness: `(E_1+E_2)^2=diag(1,0,0,1)` already has cross-link terms. Neither the magnetic continuum coefficient nor an induced electric coefficient is derived from this Hamiltonian here. Matter does not change that microscopic square identity. Matter coupling, larger representations and induced many-link terms remain possibilities, not computed solutions. There is no supplied theorem about which direction an RK potential moves this model's phase.

The sister-lane classical Maxwell germ requires a separate quantization, state and readout bridge before its dispersion/structure-factor vocabulary identifies this model's physical photon. A harmonic quantum comparison is itself conditional; no such bridge is proved here.

For the lazy propagator, PF positivity does not imply nonnegative spectrum. In the actual seven-state ladder component at `delta=0.5`, a legitimate diagonal observable has `omega_eff(m=2)=0.449489743` below its lowest coupled excitation `1.035276180`. The added actual control retains this counterexample. An exact positive-time exponential spectral mixture can support monotonic estimates under appropriate positive-weight and connected-observable hypotheses, but that is not an error bound for a noisy finite-window ratio. The 4x2x2 values `2.5994,2.5691,2.5662` and `2.9209,2.8923,2.8905` at `m=40,80,120` are computed finite values, not certified limits or universal upper bounds.

The complete Python path certificates concern the stated symmetric/bounce reptation kernels with no interior sweep. They do not certify every embedded C interior exchange/pair update or GFMC population process; those retain their finite numerical validation and explicit estimator/systematic limits.

## Where this note disagrees with PR #7942

1. **The parity obstruction is a property of closed operator strings, not of the model.** PR #7942's reported rank-`10` statement is unverified and unaccepted by this unit; the local open-path proof does not use it. What does not follow from the local pair-parity observation is that a loop or cluster
   update is required: an open-path projector needs no parity-changing update at all, because its ends are free and its interior updates change per-face flip counts by `0` or `2`. T4 certifies
   the pure Python reptation kernels on the named complete path spaces; the extra C interior updates are not included in that proof. T5 supplies finite compiled-engine witnesses. The parent's proposed loop or cluster update is not required by this local open-path construction; its own validity is not assessed here.
2. **The zero-winding class changes between the two named boxes.** At 4x2x2 that class is `1,552,024=1,551,976+48`, with zero unclassified remainder. Connectivity of the other 404 winding classes is not established; no general one-component-per-winding theorem or all-size artefact claim follows.
3. **The physical question remains open.** The finite historical rows can be compared to simple forms, but do not settle gapless versus gapped, a liquid phase or a photon.

## Where this note departs from its source computation

- The certificate's middle-state marginal is quoted at `2e-15` in the source and is `4.0e-15` here, a summation-order difference in the path enumeration; the tolerance carried in T4 is this
  note's own `1e-14`.
- The source's `omega/k^2` table (`0.73, 0.75, 0.80, 0.77`) is built from the per-component plateaus with their run spread. Recomputing from the rounded `omega(k_min)` row that W1 quotes gives
  `0.73, 0.81, 0.81, 0.73`, mean `0.77` -- the same flatness and the same coefficient, `11` per cent spread rather than `9`.
- The source states that a Maxwell photon's `S_T` proportional to `|k|` would fall by a factor `2.3` across `k = pi/2` down to `pi/6`. On the lattice measure `2 sin(k/2)` the factor for that
  range is `2.73`; `2.3` is the factor for `pi/2` down to `pi/5`. W4 and the runner carry `2.73`.
- The `L = 6, 8, 10, 12` production is quoted, not rerun; the runner executes one short `L = 4` run instead, whose offset above the quoted `L = 4` row does not establish a cause or permit transfer of the 4x2x2 bias to that volume.

## Reading, not theorem

This supplied finite-link law admits exact small-sector work and bounded numerical sampler checks. Open ends offer a route around the named closed-string parity invariant on the tested path spaces. The larger-volume physical conclusions remain unverified; no missing electric stiffness, photon or phase has been established by these measurements.

## Interfaces named for other lanes, not moved here

- **PR #7942**, historical reported parity/rank and update claims: unverified and unaccepted here. No rank statement is used; this unit reconstructs only its own finite free-end/path argument.
- **PR #7911**, the ladder and the three-dimensional question: the three-dimensional physical question remains open.
- **PR #7893**, the matter hop: named as one candidate electric stiffness, not computed.
- **The sister lane's Maxwell germ** (PRs #7887, #7886, #7884): is historical context for a conditional classical comparison; a quantum state/measurement bridge is not supplied here. Whether its supplied positive plaquette action and this pure spin-1/2
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
t422_exact: [bounded_theorem] E_0 = -16.7037885782, <n_app>_0 = 19.0690013962, <P_f> = 0.3479955954; S_L(k) = 0 to machine precision at k = pi/2 and pi; S_yy = S_zz = 0.1044875978 and 0.1815941329; finite-m effective transverse rates with m=120 rounded values 2.566 at pi/2 and 2.891 at pi; no certified limit or universal upper bound (2.5994, 2.5691, 2.5662 and 2.9209, 2.8923, 2.8905 at m = 40, 80, 120)
projector_certificate: [bounded_theorem] on COMPLETE path spaces of 935, 11,119, 4,790 and 10,020 paths: symmetric chain detailed balance 1.1e-19 and stationarity 8.7e-19 for pi = delta^{#moves}/Z, irreducible; bounce chain global balance 4.3e-19 and skew detailed balance 2.2e-19, irreducible, plain detailed balance violated by 7.7e-04; middle-state marginal to 4.0e-15; G_v = 0 on every state of every path; ergodicity ceilings 864 and 47
validation: [witness, seeds 20260904, 20260921, 20260930, 20260931, 20261001] reptation within 1.56 sigma on 2x2x2, 0.61 on the ladder, 0.45 on 4x2x2, visiting exactly 864 and 47 states with gauss_err = 0; walker method within 1.44 sigma on 2x2x2; population-control bias +0.024, +0.008, +0.005 at N_w = 400, 1600, 6400, falling and positive in these three runs only; no universal bias direction/rate
production_quoted: [unverified historical arithmetic only, QUOTED not recomputed; seeds 20261001-20261020 and 20261101-20261114, tau_prod 130-230, N_w = 500-8000, 30 bins] omega(k_min) = 1.3, 0.80, 0.5, 0.32, 0.20 at L = 4-12 with no saturation; unit-flux energy 0.71 -> 0.15(8) -> 0.15(20) against sigma L = 1.06, 1.42, naive fixed-reference ratios 12.0 and 6.3, not calibrated sigma, E(2)/E(1) = 4.1(9); largest S_T over the zone falls 1.49 -> 1.08 and S_T(pi,pi,pi) falls 1.49 -> 1.05, compared to factor 27, without excluding other order parameters; omega about 0.78 k^2 with omega/k^2 = 0.73, 0.75, 0.80, 0.77 while omega/k halves; S_T(k_min) flat at 0.30-0.38; E_0/N_p = -0.287(3)
claim_types: bounded_theorem for every exact row above (t222_census, t222_spectrum, ladder, t422_census, t422_exact, projector_certificate); finite stochastic witness only for executed group E, including its short L=4 run; unverified historical arithmetic for all of production_quoted
not_claimed: nothing is proved for any L^3 torus with L >= 4; no continuum limit, no T > 0, no matter, no larger link spin; no claim that this U(1) is electromagnetism; whether omega proportional to k^2 is asymptotic or a crossover above a linear regime at k < pi/6 is not decided
departures_from_pr7942: historical parent rank/update claims remain unverified and unaccepted; the local same-face pair operation preserves flip parity, while the reconstructed free-end path proof needs no closed-string parity-changing move; only the zero-winding class connectivity is established at 4x2x2; other winding classes and larger boxes remain unresolved
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: original 27 check IDs retained with corrected scopes, plus the lazy-ratio counterexample; required compiler/engine or diagnostic failure makes the unit nonzero and incomplete; actual final result is in the canonical cache
```

## Proof boundary

The integer constructions, finite floating-point spectra and finite path certificates are conditional on the named supplied geometries, role, background and `lambda=1`. Reference agreement tolerances do not certify rounding precision or every unmeasured eigenvalue/limit. In particular T3's finite-m effective rates are not certified asymptotic energies, and T4's Python path certificate is not a full compiled-sampler proof.

Only the actual group E commands give current stochastic witnesses. Their bin standard errors are not complete uncertainty bounds: autocorrelation, finite projection, population control and finite volume remain distinct. The measured 4x2x2 offsets `0.14,0.05,0.03` per cent do not justify transferring a bias `0.002`-`0.003` per face to L=10,12. The historical report that bin merging enlarged errors by up to factor `2` neither has bound raw provenance here nor makes every error bar a rigorous factor-two lower bound.

The original L=4..12 reported production values and protocols are retained unchanged and explicitly unverified. No new production run is part of this correction. No continuum or thermodynamic limit, matter response, general order classification, physical readout map or identification with electromagnetism is established. Formal claim audit remains deferred.

## Review record

All original 27 check IDs, finite census/matrix/spectrum and fitted values, seeds, populations, windows and estimator formulas are retained. The correction adds a real lazy-spectrum counterexample and dump-independent initialized/evolved/resampled/final Gauss state/equation checks; actual compiler, engine and diagnostic failures cannot produce a successful full-unit cache. The current cache is generated by one actual final execution with the unchanged 300-second cap after final note/source/input freeze. Historical note, runner and receipt remain separately recoverable. Source review and the coordinator's landing gates precede any acceptance; this note applies no audit verdict.

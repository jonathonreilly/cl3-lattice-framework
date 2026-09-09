---
claim_id: taste_singlet_second_mass_body_diagonal_hop_vortex_strings_2n_modes_2026_09_03
claim_type: bounded_theorem
claim_scope: "In the one-particle sector on the coarse cubic lattice with one mode per site, the Kawamoto-Smit signs eta_1 = 1, eta_2 = (-1)^x, eta_3 = (-1)^{x+y}, the declared 2x2x2 cell algebra Gamma = (Y1, Z1Y2, Z1Z2Y3), Xi = (X1, Z1X2, Z1Z2X3), eps = Z1Z2Z3 and H(q) = sum_a [(1+cos q_a) Xi_a + sin q_a Gamma_a] with its Dirac point at q = (pi,pi,pi), and with a SUPPLIED second mass operator M2 = X1Y2X3, a SUPPLIED winding site phase, a SUPPLIED radial profile M(rho) = M_0 tanh(rho/xi) and a SUPPLIED core position, none of which is derived from any axiom: (T1) a complete enumeration of the 64 Pauli strings on the cell shows that exactly four anticommute with the Dirac-point Clifford set {Gamma_1, Gamma_2, Gamma_3, eps} -- the three single-bond dimerizations Xi_1, Xi_2, Xi_3 (a taste triplet) and M2 = X1Y2X3 = i Xi_1 Xi_2 Xi_3 (the taste singlet, the one commuting with all three taste Paulis) -- with the nullity of the anticommutation map on the 64-dimensional Pauli space equal to 4, bit-flip counts 1, 3, 1, 1, all algebra residuals 0.0e+00, X M2 = i eps so that (X, M2, eps) = (tau_3, tau_1, tau_2) at the node, and the node spectrum exactly +-sqrt(m1^2+m2^2) fourfold each at max deviation 4.4e-16. (T2) M2 is a hop of Manhattan length 3 across the four body diagonals of each cell with pure-imaginary amplitude i(-1)^{b_2}, 8 nonzero entries, max|Re M2| = 0.0e+00, T-odd (M2* = -M2) and P-odd (eps M2 eps = -M2) at 0.0e+00; all 32 even-flip Pauli strings commute with eps and all 32 odd-flip strings anticommute, both at 0.0e+00, so no even-length hop is a mass and there is no distance-2 second mass; the anticommutant elements with fewer than three bit flips are exactly the nearest-neighbour triplet XII, ZXI, ZZX, so no nearest-neighbour and no face-diagonal term gives the singlet; and {diag(eps_v), M2} = 0.0e+00 in real space on an 8x8 plane for any profiles. (T3) H(pi+p)^2 = [sum_a (2 - 2 cos p_a) + m1^2 + m2^2] 1 + 2 m2 sum_a (1 - cos p_a) M2 Xi_a with M2 Xi_a = (s1, -s2, s3)_a a taste Pauli, at max residual 8.9e-16 over three momenta and two mass pairs, so the node gap is exact and the second mass splits the taste velocities at first order in m2. (T4) On an open 24x24 transverse plane with Bloch q_z = pi + p, M_0 = 0.7, xi = 2, window |E| < 0.686 and R_c = 5, a winding n = +1 string carries exactly 2 core modes at p = +0.1, E = +0.09990 each, core weight >= 0.845, ring weight <= 0.013, <V_z> = +0.994, <-Gamma_3> = +0.999, one per taste (taste-projected eigenvalues -0.961/+0.961, -0.985/+0.985, -0.946/+0.946), net +2 on the core against -2 on the ring; n = -1 gives 2 left-movers and net -2 against +2; n = +2 gives 4 right-movers, two per taste, net +4 against -4; the core-pair velocity is 1.0379, 0.9990, 0.9983 at N = 16, 24, 32 and the p = 0 core/ring splitting falls 2.834e-02, 3.682e-03, 4.706e-04, a factor 7.7 then 7.8 per Delta N = 8. (T5) |<X>| <= 6.9e-17 on every n = +-1 string mode and X is traceless on the n = +2 core subspace (eigenvalues -0.338, -0.338, +0.338, +0.338, trace -4.1e-04) while <-Gamma_3> = +-0.999: the handedness is the sharp eigenvalue of -Gamma_3 = sigma_3 x tau_3, the Jackiw-Rossi index, and not the 3+1-dimensional chirality. (T6) With M2 replaced by the nearest-neighbour Xi_3 = M2 s_3 the same vortex carries one right-mover and one left-mover of opposite taste, (E, <V_z>, <s3>) = (-0.13082, -0.759, -0.718) and (+0.13082, +0.759, +0.718), net 0, hybridising at p = 0 into a gap 2 x 0.08455; the mixed mass a M2 + b Xi_3 gives core nets +2, 0, +1 at (a,b) = (1, 0.5), (0.5, 1), (0.8, 0.8), matching n [sgn(a+b) + sgn(a-b)]. (T7) On a 40x24 open plane with cores (9.5, 11.5, +1) and (29.5, 11.5, -1) the string carries +2 and the anti-string -2, E = +0.14948 and -0.14948 at p = +0.15 with <V_z> = +0.988 and -0.988, the 16 ring states net 0, and v = 0.997. (T8) A Gaussian flux tube of the compact link field of total flux 2 pi or 4 pi (plaquette sums 1.0002 and 2.0004) with a uniform real mass m1 = 0.7 and no mass vortex carries no in-gap state at p = -0.1, 0, +0.1, nearest |E| 0.702 and 0.700, while the massless control gives 12 states with |E| < 0.3 in +-E pairs whose two nearest zero, E = -0.1155 and +0.1155, have <V_z> = -0.864 and +0.864 and net 0. Every transverse window is certified complete against a dense LAPACK count over all 26 windows at count deviation 0, max |dE| 1.4e-14 and max eigenpair residual 2.1e-14. Interactions, dynamics for the profile or the phase, the many-body sector, the fine lattice, periodic transverse boundaries, the n = 2 string/anti-string pair on an open plane, and sizes other than those named are out of scope. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py
---

# The taste-singlet second mass is a body-diagonal imaginary hop, and its vortex strings carry `2n` co-moving modes

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py`](../scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.txt`](../logs/runner-cache/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.txt)
**Parents:** none load-bearing. Every object used below is declared in this note and rebuilt from scratch by the runner; the notes named in "Imports and authority" are plain-text pointers carrying no grade and no dependency weight.

A staggered fermion on the coarse lattice has one mass term available to it as landed: the record-native staggered mass `m_1 eps_v n_v`, real and diagonal in the record basis. A handed mode bound to a string needs a **second** mass, one that anticommutes with
the first, so that the pair forms a complex mass whose phase can wind. This note asks what the cell algebra actually contains that can play that part, and what the strings of such a mass carry. Both answers are sharper than the question: the second mass exists
and is essentially unique, but it is a **body-diagonal imaginary hop** of Manhattan length three rather than anything nearest-neighbour; and its winding-`n` strings carry **`2n`** co-moving modes rather than `n`, always paired against `-2n` elsewhere. The note
is a **bounded theorem about declared operators**, class-A finite-dimensional throughout. It derives nothing from the axioms, and it says so at every point where a supplied item enters.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite one-particle linear-algebra theorems about declared operators on a declared coarse lattice. T1, T2 and T3 are zero-residual or complete-enumeration statements on the 8x8 cell algebra; the string-mode counts of T4, T6 and T7 are integers on named finite planes; the velocities, weights, expectation values and projected taste eigenvalues are floating-point cross-checks at the stated tolerance; T5 and T8 are numerical statements on the same named planes. No statement here is a proof about the infinite lattice, and none is derived from any axiom."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-size theorem, and route to the lane that owns record structure the one question this note does not decide: whether any record-native register can carry the winding U(1) phase that the second mass needs, given that the compact link field supplies path-ordered Wilson lines and not a site phase."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the eight statements below, exactly the runner's check groups `A`-`G` plus the solver certificate `S`. The zero-residual, complete-enumeration and integer items are exact; the items tagged `[numerical]` are floating-point
cross-checks on the named finite planes at the stated tolerance.

1. `T1` (`A`). The anticommutant of the Dirac-point Clifford set is exactly four Pauli strings, and the two masses form a complex mass at the node.
2. `T2` (`B`). The taste singlet is a body-diagonal imaginary hop of Manhattan length three, T-odd and P-odd, and nothing shorter can be it.
3. `T3` (`C`). The exact square, and the taste-velocity splitting it carries at first order in `m_2`.
4. `T4` (`D1`-`D5`). A winding-`n` string carries exactly `2n` co-moving modes, one per taste, and the compensating `-2n` sits on the outer ring.
5. `T5` (`D6`). The handedness is the sharp eigenvalue of `-Gamma_3`, not the 3+1-dimensional chirality.
6. `T6` (`E`). The nearest-neighbour (taste-triplet) second masses give net zero and gap; the mixed mass obeys `n [sgn(a+b) + sgn(a-b)]`.
7. `T7` (`F`). String plus anti-string in one plane: `+2` on one core, `-2` on the other, the ring vector-like.
8. `T8` (`G`). A `2 pi` or `4 pi` flux tube of the compact link field with a real mass carries no in-gap state.

## Imports and authority

Imported scientific authority: none load-bearing. Kawamoto-Smit staggered signs, the Jackiw-Rossi vortex zero mode and the Nielsen-Ninomiya counting are standard methodology and appear below only as **plain-text pointers carrying no authority**; every object is redeclared here and the runner recomputes every statement from scratch. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch): the first mass, whose declared term is quoted in "Setting". Not linked; it is not on the main line.
- `EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch, PR #7844): the cell algebra and the Dirac-point Clifford set, whose generators "Definitions" redeclares verbatim. Not on the main line.
- `THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch, PR #7909): the single-wall chirality counting rule, quoted in "Interfaces". Not linked; it is not on the main line.
- `A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_IN_THE_INTERIOR_AND_A_REAL_MASS_CARRIES_NONE_BOUNDED_THEOREM_NOTE_2026-09-04.md` (open branch): the same coin in a supplied two-dimensional record time. Not on the main line.
- `THE_FERMION_ON_COMPACT_U1_LINKS_THE_INTEGER_FLUX_SELECTS_THE_STAGGERED_GAUSS_LAW_AND_JOINS_THE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch, PR #7914) and
  `COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch, PR #7884): the compact `U(1)` link field whose flux tube `T8` tests. Neither is linked; neither is on the main line.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): the Lattice axiom quoted in "Setting". No grade of it is cited and no hypothesis is adopted.

## Setting

The framework axioms are quoted, not amended. The **Lattice / Physical Locality** axiom's adjacency clause reads, verbatim:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The adjacency the axiom supplies is **nearest-neighbour**. Theorem `T2` computes that the taste-singlet second mass is a hop of Manhattan length three; it is therefore **outside** that clause, and this note declares it as supplied data rather than reading it
out of the axiom.

The first mass is the one the record-native staggered-mass note declares, verbatim from its definitions block:

> `H_m  = m sum_v eps_v n_v               THE DECLARED MASS TERM; m is supplied and is fixed by nothing quoted here`

with `eps_v = (-1)^{v_1+v_2+v_3}`, and that note states of it: *"Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the mass term are declared objects, and no coefficient is derived."* This note inherits that standing
for `m_1` and adds four further supplied items of its own, itemised in "The framework reading". The cell algebra it works in is the one the Dirac-point note declares, and it is redeclared below so that the runner is self-contained.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice with the Kawamoto-Smit signs, the `2x2x2` cell algebra, the Dirac point, the two mass operators, the winding
phase, the profile and the transverse-plane geometry. `P1` (`A`) fixes the anticommutant and the node algebra; `P2` (`B`) is the support, length and symmetry class of the singlet, which uses `P1`'s enumeration; `P3` (`C`) is the exact square, which uses `P1`'s
commutation relations; `P4` (`D1`-`D5`) is the string-mode census, which uses `P1`-`P3`; `P5` (`D6`) is the handedness identification on `P4`'s modes; `P6` (`E`) is the taste-triplet comparison against `P4`; `P7` (`F`) is the pair geometry; `P8` (`G`) is the
link-field control. The strongest supported scope is precisely `P0`-`P8`.

## Definitions

```text
cell          2x2x2 coarse cell; bits (b_1,b_2,b_3) = (x,y,z) mod 2;
              Pauli-string index 4 b_1 + 2 b_2 + b_3
KS signs      eta_1 = 1, eta_2 = (-1)^x, eta_3 = (-1)^{x+y}                 SUPPLIED
Gamma_a       (Y1, Z1Y2, Z1Z2Y3)          Dirac-point velocities are -Gamma_a
Xi_a          (X1, Z1X2, Z1Z2X3)          the Wilson-like (1 + cos q_a) terms
eps           Z1Z2Z3                      the record-native staggered mass   SUPPLIED
H(q)          sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a];  Dirac point (pi,pi,pi)
X             i Gamma_1 Gamma_2 Gamma_3 = -Y1X2Y3     the 3+1D chirality
M2            X1Y2X3 = i Xi_1 Xi_2 Xi_3   the taste-singlet second mass      SUPPLIED
s_b           (Y2X3, Y1Z2X3, Y1X2) = (i Xi2Xi3, -i Xi3Xi1, i Xi1Xi2)  taste Paulis
Xi_b          = M2 (s_1, -s_2, s_3)_b     the taste-triplet second masses
m_1 + i m_2   M(rho) e^{i n phi}, M(rho) = M_0 tanh(rho/xi)                  SUPPLIED
              m_1 on sites times eps_v = (-1)^{x+y+b_3}; m_2 on cell centres
              (2X + 1/2, 2Y + 1/2) multiplying M2 on that cell
plane         open N_x x N_y transverse (x,y); z carried by bit b_3 and Bloch q_z
p             q_z - pi;   V_z = dH/dq_z, taken exactly
core / ring   rho < R_c about a declared core; within 2.5 of the plane edge
alpha_v       a PROPOSED site register in U(1) -- a charged scalar's phase   SUPPLIED
```

Sizes: `M_0 = 0.7`, `xi = 2`, in-gap window `|E| < 0.686`, `R_c = 5`; `N = 16, 24, 32` for the single vortex; `40 x 24` for the string/anti-string pair; `24 x 24` for the link-field control; an `8 x 8` plane for the real-space anticommutator. Cores sit at
`((N-1)/2, (N-1)/2)`, a cell corner, so no site sits at the core. Every transverse eigenproblem is solved by sparse shift-invert about `E = 0` from a fixed deterministic start vector -- **there is no randomness and no seed anywhere in the runner** -- followed
by a Rayleigh-Ritz re-diagonalisation on the returned span, and every window is certified complete twice over: the `k`-th eigenvalue nearest zero lies outside it, and the count inside it equals a dense LAPACK count. The largest dense matrix is `2048 x 2048`.

## Theorem 1 -- the anticommutant of the Dirac-point Clifford set is exactly four Pauli strings

**Conclusion.** A second mass must anticommute with the three Dirac-point velocity matrices `Gamma_a` and with the first mass `eps`. A **complete enumeration** of all 64 Pauli strings on the `2x2x2` cell finds exactly four that do: `XII = Xi_1`, `ZXI = Xi_2`,
`ZZX = Xi_3` and `XYX = i Xi_1 Xi_2 Xi_3 =: M2`. The count is confirmed independently by a rank computation -- the nullity of the linear map `M |-> ({M,Gamma_1}, {M,Gamma_2}, {M,Gamma_3}, {M,eps})` on the 64-dimensional real Pauli space is exactly `4` -- so no
linear combination outside the four is missed. Their bit-flip counts are `1, 3, 1, 1`. The three single-flip elements are the single-bond dimerizations and form a **taste triplet**: `Xi_b = M2 (s_1, -s_2, s_3)_b` at residual `0.0e+00`, the singlet times a
taste Pauli. `M2` is the one element of the four that commutes with all three taste Paulis, and is therefore the **taste singlet**.

`M2` is Hermitian, squares to `1`, and equals `i Xi_1 Xi_2 Xi_3`, all at `0.0e+00`; it anticommutes with `eps` and with each `Gamma_a` and **commutes** with each `Xi_a`, all at `0.0e+00`. The 3+1-dimensional chirality `X = i Gamma_1 Gamma_2 Gamma_3 = -Y1X2Y3`
commutes with the `Gamma_a` and anticommutes with both `eps` and `M2` at `0.0e+00`, and

```text
X M2 = i eps        residual 0.0e+00        so  (X, M2, eps) = (tau_3, tau_1, tau_2)
```

on the Dirac-point subspace: `m_1 eps + m_2 M2` is a complex Dirac mass `m_1 + i m_2` against the Weyl kinetic term. The spectrum at the node is exactly `+-sqrt(m_1^2 + m_2^2)`, fourfold each, for `(m_1, m_2) = (0.3, 0.4), (0.7, 0), (0, 0.7), (0.5, -0.5)`, at
maximum deviation `4.4e-16`. The `Cl(6)` relations, the anticommutation of `eps` with all six generators, and the agreement of the real-space cell hopping rules with the landed `H(q)` at three momenta are all `0.0e+00`.

## Theorem 2 -- the singlet is a body-diagonal imaginary hop of Manhattan length three, T-odd and P-odd

**Conclusion.** `M2` has exactly `8` nonzero entries, each joining a cell corner `b` to its bit complement -- bit distance `3`, the **body diagonal** of the `2x2x2` cell -- with amplitude `i(-1)^{b_2}`, at residual `0.0e+00`, and `max |Re M2| = 0.0e+00`: it is
a **pure-imaginary hop**, not a potential like `m_1 eps_v n_v`.

A hop over displacement `d` contributes to the cell Bloch matrix a Pauli string that flips exactly the bits where `d` is odd. Two complete enumerations then decide the reachability question. All `32` even-flip strings **commute** with `eps` and all `32`
odd-flip strings **anticommute** with it, both at `0.0e+00`: any even-length hop commutes with the first mass and so cannot be a second mass at all -- in particular **there is no distance-2 second mass**. And the anticommutant elements with fewer than three
flips are exactly `XII, ZXI, ZZX`, the nearest-neighbour triplet. So the taste singlet must flip **all three** cell bits, which requires all three components of `d` odd, hence Manhattan length at least three with the body diagonal as minimal support: **no
nearest-neighbour term and no face-diagonal term gives it.**

Under complex conjugation `M2* = -M2` (T-odd) and under `eps`-conjugation `eps M2 eps = -M2` (P-odd), both `0.0e+00`, while `eps` and the hopping matrix are T-even at `0.0e+00`: `(m_1, m_2)` is a scalar plus pseudoscalar pair, and a winding phase between them
is P- and T-violating. In real space on an `8x8` plane, `{diag(eps_v), M2} = 0.0e+00` for any profiles -- the two masses anticommute site by site, not merely at the node -- while a face-diagonal `(1,1,0)` hop **commutes** with `diag(eps_v)` at `0.0e+00`, which
is the same statement in the real-space idiom.

## Theorem 3 -- the exact square, and the taste-velocity splitting at first order in `m_2`

**Conclusion.** With both masses on,

```text
H(pi + p)^2 = [ sum_a (2 - 2 cos p_a) + m_1^2 + m_2^2 ] 1 + 2 m_2 sum_a (1 - cos p_a) M2 Xi_a,
M2 Xi_a = (s_1, -s_2, s_3)_a
```

at maximum residual `8.9e-16` over three momenta and two mass pairs. The identity is exact, not an expansion. Two things follow. The gap at the node is exactly `sqrt(m_1^2 + m_2^2)`, since the cross term vanishes at `p = 0`. And because `M2` **commutes** with
the Wilson-like `Xi_a` instead of anticommuting with them, the cross term is a taste Pauli: the second mass **splits the two tastes' velocities at first order in `m_2`**, anisotropically, giving `E^2 = m_1^2 + m_2^2 + |p|^2 +- m_2 sqrt(sum_a p_a^4)` to leading
order. This is the price of the singlet being a commuting-with-`Xi` operator, and it is a property of the lattice terms, not of the continuum limit.

## Theorem 4 -- a winding-`n` string carries exactly `2n` co-moving modes, one per taste

**Conclusion.** On a `24x24` open transverse plane (dimension `1152`) with `m_1 + i m_2 = M(rho) e^{i n phi}` and Bloch `q_z = pi + p`, at `p = +0.1` and `n = +1` the window `|E| < 0.686` holds `16` states, of which exactly **`2`** are core modes: `E =
+0.09990` twice, core weight `>= 0.845`, ring weight `<= 0.013`, `<V_z> = +0.994`, `<-Gamma_3> = +0.999`, `|<X>| <= 6.9e-17` and `|<eps>| <= 1.0e-16`. Both are right-movers, so the net over the core is `+2` and the net over the ring is `-2`, with the mixed
class contributing `0`. The taste generators projected onto the core pair give `s_1: -0.961, +0.961`, `s_2: -0.985, +0.985`, `s_3: -0.946, +0.946` -- **one mode per taste, and both of the same handedness.** This is the whole content of the `2n`: the two tastes
do not cancel for the singlet.

Reversing the winding reverses everything: `n = -1` gives 2 core modes at `E = -0.09990` with `<V_z> = -0.994` and `<-Gamma_3> = -0.999`, taste-projected `-0.946, +0.946`, net `-2` on the core against `+2` on the ring. Doubling it doubles the count: `n = +2`
gives **4** core modes, `E = +0.10020, +0.10020, +0.10022, +0.10022`, core weight `>= 0.712`, `<V_z> >= +0.991`, `<-Gamma_3> >= +0.996`, taste-projected `-0.951, -0.950, +0.950, +0.951` -- two per taste -- and net `+4` on the core against `-4` on the ring.

The dispersion is linear through the origin and the velocity approaches `1`: `(E(+0.1) - E(-0.1))/0.2` equals `1.0379` at `N = 16`, `0.9990` at `N = 24` and `0.9983` at `N = 32`, both branches equal at every size. The compensating `-2n` lives on the **outer
ring** of the open plane and decouples exponentially: the `p = 0` core/ring hybridisation splitting `min|E|` falls `2.834e-02, 3.682e-03, 4.706e-04` at `N = 16, 24, 32`, a factor `7.7` then `7.8` per `Delta N = 8`. The one-dimensional doubling theorem along
the string axis therefore holds exactly on the finite lattice, and the string's handedness is paid for locally, not globally.

## Theorem 5 -- the handedness is `-Gamma_3`, not the 3+1-dimensional chirality

**Conclusion.** `|<X>| <= 6.9e-17` on every `n = +-1` string mode, and on the `n = +2` core subspace `X` is **traceless**: its projected eigenvalues are `-0.338, -0.338, +0.338, +0.338`, trace `-4.1e-04`. The 3+1-dimensional chirality is not what these modes
carry. What they do carry sharply is the cell-local `z`-velocity: `<-Gamma_3> = +0.999, +0.999` for `n = +1` and `-0.999, -0.999` for `n = -1`, and `>= +0.996` on the `n = +2` quartet. The handedness of a string mode is the eigenvalue of `-Gamma_3 = sigma_3 x
tau_3`, the Jackiw-Rossi index of the two-dimensional vortex problem, and the sign of `<V_z>` agrees with it mode for mode. Any reading of these modes as carrying `gamma_5` is contradicted by the numbers.

## Theorem 6 -- the nearest-neighbour (taste-triplet) second masses give net zero and gap

**Conclusion.** Replace `M2` by the nearest-neighbour `Xi_3 = M2 s_3`, the intra-cell `z`-bond dimerization, and keep everything else. The same `n = +1` vortex on the same `24x24` plane then carries at `p = +0.1` two core modes with `(E, <V_z>, <s_3>) =
(-0.13082, -0.759, -0.718)` and `(+0.13082, +0.759, +0.718)`, taste-projected `-0.941, +0.941`: **one right-mover and one left-mover, of opposite taste, net `0`.** Because `s_b` is not conserved by the lattice `(1 - cos p)` terms the pair hybridises, and at `p
= 0` it opens a gap `2 x 0.08455`. The taste cancellation a reader would expect is real -- it belongs to the triplet, not to the singlet, and the identity `Xi_b = M2 s_b` says why: taste `s_b = +-1` sees `m_1 +- i m_2`, that is, windings `+n` and `-n`.

The interpolation is sharp. For the mixed second mass `a M2 + b Xi_3` the core net at `(a, b) = (1, 0.5), (0.5, 1), (0.8, 0.8)` is `+2, 0, +1`, exactly `n [sgn(a+b) + sgn(a-b)]`; at `(0.8, 0.8)` a single core mode survives, the other taste having zero second
mass and no localized mode at all. The taste-triplet route **removes** the handedness rather than restoring it.

## Theorem 7 -- string plus anti-string in one plane: `+2` and `-2`, the ring vector-like

**Conclusion.** On a `40x24` open plane (dimension `1920`) with cores `(9.5, 11.5, +1)` and `(29.5, 11.5, -1)`, total winding zero, at `p = +0.15` the first core carries 2 modes at `E = +0.14948` with `<V_z> = +0.988` and the second carries 2 modes at `E =
-0.14948` with `<V_z> = -0.988` (both modes equal per core); the `16` ring states net `0`. At `p = -0.15` the core nets are again `+2` and `-2` with the ring at `0`, and `v = 0.997`. So the `+2n` of a string is paid by the `-2n` of an anti-string when one is
present, and the boundary is then vector-like -- the closed-loop bookkeeping, with no net handedness anywhere in the plane.

## Theorem 8 -- a flux tube of the compact link field, with a real mass, carries nothing

**Conclusion.** Put Peierls phases for a Gaussian flux tube of width `sigma_B = 2` and total flux `2 pi n_phi` on the transverse bonds of a `24x24` plane, with a **uniform real** mass `m_1 = 0.7` and no mass vortex. The plaquette-angle sums are `1.0002` and
`2.0004` times `2 pi` for `n_phi = 1, 2`, and the number of in-gap states is `0` at `p = -0.1, 0, +0.1` in both cases, the nearest `|E|` being `0.702` and `0.700` -- outside the window. The massless control at `n_phi = 1, p = +0.1` gives `12` states with `|E|
< 0.3` in `+-E` pairs whose two nearest zero are `E = -0.1155, +0.1155` with `<V_z> = -0.864, +0.864`, net `0`: vector-like. **The link field by itself gives no handed mode, and the real mass gaps what it does give.** Whatever the strings of this note carry,
they are not carrying it because of the gauge field.

## Corollary -- what three dimensions require of a handed string

Within the setting declared above, in the one-particle sector, and on the finite planes named:

1. **Inside three dimensions the second mass a handed string needs is a body-diagonal hop of length three.** It is never nearest-neighbour and never diagonal in the record basis: `T2` gives `max |Re M2| = 0.0e+00` on a pure hop, and `T1` with `T2` leaves the
   taste triplet as the whole of what a nearest-neighbour term can give.
2. **Each winding-`n` string carries exactly `2n` co-moving modes, one per taste**, of a single handedness given by `-Gamma_3`, and never `n` and never `0`.
3. **That `2n` is always paired with `-2n`** on an anti-string or on the boundary. The one-dimensional doubling theorem holds exactly along the string axis on the finite lattice, so handedness in this construction is **local to a string and never net**.
4. **The taste-triplet route removes the handedness rather than restoring it**, and the mixed interpolation `n [sgn(a+b) + sgn(a-b)]` says exactly where the transition sits.
5. **The link field alone gives nothing.** A `2 pi` or `4 pi` flux tube with a real mass has no in-gap state; the object that works is a **mass-phase vortex**, not a flux string.

**Reading, not theorem (this register).** The lattice already contains one thing that could serve as a second mass, and it turns out to be a hop straight across the diagonal of the little cube, carrying a factor of `i`. Give that hop a strength whose phase
turns once around a line, and a handed mode runs along that line -- two of them, one for each of the two species the lattice unavoidably has, both running the same way. Turn the phase the other way and they both run the other way. There is always an equal and
opposite pair somewhere else, on a partner line or at the edge, so nothing handed exists overall; a handed mode is a property of a particular line, not of the world. The nearest-neighbour version of the same idea gives one of each instead, which then join up
and gap. And a magnetic flux tube on its own gives nothing at all. What all of this costs is a phase that winds, and the framework has nowhere to keep one.

## The framework reading -- supplied item by item, and what follows from them

**Supplied.** Four items, none of them derived from any axiom:

- **S1. `M2` itself.** A distance-3 body-diagonal hop with amplitude `+-i`. The Lattice axiom's adjacency clause, quoted verbatim in "Setting", supplies nearest-neighbour adjacency; `T2` computes that no nearest-neighbour and no face-diagonal term is in the
  anticommutant beyond the triplet, so the singlet is outside that clause by computation, not by assumption.
- **S2. A winding site phase.** `m_1 + i m_2 = M e^{i n phi}` needs a *site* phase `phi(v)` that turns. The compact `U(1)` link field supplies gauge-covariant Wilson lines on **paths**, not a site phase: a covariant dressing `i c^dag_{v+d} U_path c_v` makes
  `M2` gauge-covariant but **cannot lock its phase to `M_1`'s, which has none**, so "the mass phase locked to the link angle" is a gauge-fixed statement about pure-gauge links outside a core, not a gauge-invariant one. A record-native form is **proposed** here
  and labelled honestly: a site register `alpha_v in U(1)`, with `m_1 eps_v n_v cos alpha_v` and `m_2 M2^{(cell)} sin alpha_cell`. That register is **a charged scalar's phase by another name**, and the framework does not have one. No way to obtain it from the
  landed surface was found.
- **S3. The profile and the core position.** `M(rho) = M_0 tanh(rho/xi)`, `M_0 = 0.7`, `xi = 2`, core at a cell corner: declared shapes, with no dynamics behind them at the one-particle level.
- **S4. Which mover survives.** The `+2n` of `T4` is stated only alongside the `-2n` of `T4` and `T7`. Nothing here selects one member of that pair; the pairing is a theorem and the selection is not attempted.

**Derived, given the supplied items:** the fourfold anticommutant and its nullity; the taste split and `Xi_b = M2 s_b`; the body-diagonal support, the length-3 lower bound, the absence of a distance-2 second mass, and the T- and P-oddness; the `tau`-algebra
and the exact node gap; the exact square and the first-order taste-velocity splitting; the string-mode count `2n`, its handedness, the sharpness of `-Gamma_3` and the tracelessness of `X`; the anti-string reversal; the ring compensation and its exponential
decoupling; the triplet cancellation, its gap and the mixed-mass rule; and the null result for a pure link-field flux tube.

## What is not changed

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. The Lattice axiom is quoted, not weakened; the note declares an operator outside its adjacency clause and says so.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms: the second mass, the winding phase, the profile, the core position, the plane sizes and the boundary condition are declared objects, and no coefficient is derived.
- The `alpha_v in U(1)` register of `S2` is a **proposal labelled as a charged scalar's phase**, not a primitive registration and not a claim that the framework admits one.
- Nothing here is framed as foreclosing anything. `T2` bounds what the *cell algebra* contains; it says nothing about constructions outside the declared setting.

## Interfaces named for other lanes, not taken up here

- **The two-dimensional record-time vortex** (open branch). Same coin, other face: there a supplied second record coordinate plus a phase-valued mass buys one interior Weyl mode; here a supplied body-diagonal operator plus a phase-valued mass buys `2n` per string. Both purchases use the **same currency, a supplied winding phase**, and neither lane has a bridge that produces one.
- **The single-wall chirality counting rule** (open branch, PR #7909), which states that *"the number of localized chiral species equals the number of `tau`-transitions in the sequence bracketed by the trivial vacuum ... and the net chirality is zero"*. The
  strings here replace its transition count by a winding number and keep its net-zero half intact, on a different geometry. Whether the two statements are one rule belongs to that lane.
- **The record-native staggered mass** (open branch), whose declared term `m sum_v eps_v n_v` is the `m_1` used throughout. Whether any occupancy-to-mass bridge can carry a **phase** rather than a real monotone value is this note's single load-bearing gap, and belongs to that lane.
- **The compact `U(1)` link** (open branches, PR #7914 and PR #7884), whose flux tube `T8` tests and finds null. Whether a Higgs-like record could dress the link field into a site phase is a question for that lane; nothing here attempts it.

## Remaining live routes

1. A **periodic transverse torus**, which removes the boundary ring entirely and would settle the `n = 2` string/anti-string count that the open plane cannot.
2. Larger planes, other windings, other profiles, other `xi`, other core positions and other mixing angles: `N <= 32` for the single vortex, `40 x 24` for the pair, `n in {-1, +1, +2}` and three `(a, b)` pairs are what is computed.
3. The many-body statements. Everything here is one-particle: no sea, no fermion determinant, no anomaly matching, no dynamics for the phase.

## Executable claim block

```text
setting: one-particle sector, coarse cubic lattice, one mode per site, KS signs eta_1 = 1, eta_2 = (-1)^x, eta_3 = (-1)^{x+y}; 2x2x2 cell, Gamma = (Y1, Z1Y2, Z1Z2Y3), Xi = (X1, Z1X2, Z1Z2X3), eps = Z1Z2Z3, H(q) = sum_a [(1+cos q_a) Xi_a + sin q_a Gamma_a], Dirac point (pi,pi,pi), X = i Gamma_1 Gamma_2 Gamma_3; SUPPLIED: M2 = X1Y2X3, a winding site phase, M(rho) = M_0 tanh(rho/xi) with M_0 = 0.7, xi = 2, and the core position; window |E| < 0.686, R_c = 5; Lattice axiom quoted from MINIMAL_AXIOMS_2026-06-29.md
T1 anticommutant [exact]: complete enumeration of the 64 Pauli strings -> XII, XYX, ZXI, ZZX, count 4, nullity 4, bit flips 1,3,1,1; XYX = M2 the one commuting with all three taste Paulis; M2 = i Xi1Xi2Xi3 hermitian involution, {M2,eps} = {M2,Gamma_a} = [M2,Xi_a] = 0.0e+00; X M2 = i eps 0.0e+00 -> (X,M2,eps) = (tau_3,tau_1,tau_2); Xi_b = M2 (s1,-s2,s3)_b 0.0e+00; node spectrum +-sqrt(m1^2+m2^2) fourfold, max dev 4.4e-16
T2 body-diagonal hop [exact]: 8 nonzero entries, bit distance 3, amplitude i(-1)^{b_2}, max|Re M2| 0.0e+00; 32 even-flip strings commute with eps and 32 odd-flip anticommute, both 0.0e+00 -> no even-length hop is a mass, no distance-2 second mass; anticommutant elements with < 3 flips = XII, ZXI, ZZX only -> no nearest-neighbour and no face-diagonal term gives the singlet; M2* = -M2 and eps M2 eps = -M2 at 0.0e+00; {diag(eps_v), M2} = 0.0e+00 on an 8x8 plane, face-diagonal hop commutes with diag(eps_v) 0.0e+00
T3 exact square [1e-14]: H(pi+p)^2 = [sum_a(2-2cos p_a) + m1^2 + m2^2] 1 + 2 m2 sum_a (1-cos p_a) M2 Xi_a, M2 Xi_a = (s1,-s2,s3)_a, max residual 8.9e-16 over 3 momenta x 2 mass pairs -> exact node gap, taste velocities split at O(m2)
T4 string modes [numerical]: 24x24 dim 1152, p = +0.1, n = +1 -> 16 in-gap, 2 core modes E = +0.09990, core w >= 0.845, ring <= 0.013, <V_z> = +0.994, <-Gamma_3> = +0.999, taste-projected -0.961/+0.961, -0.985/+0.985, -0.946/+0.946, net core +2 ring -2; n = -1 -> 2 left-movers, net -2/+2; n = +2 -> 4 right-movers E = +0.10020,+0.10022, core w >= 0.712, <V_z> >= +0.991, taste -0.951,-0.950,+0.950,+0.951, net +4/-4; velocity 1.0379/0.9990/0.9983 at N = 16/24/32; p = 0 splitting 2.834e-02, 3.682e-03, 4.706e-04, ratios 7.7 then 7.8
T5 handedness [numerical]: |<X>| <= 6.9e-17 on every n = +-1 mode; X on the n = +2 core subspace -0.338,-0.338,+0.338,+0.338, trace -4.1e-04; <-Gamma_3> = +0.999,+0.999,-0.999,-0.999 -> handedness = eigenvalue of -Gamma_3 = sigma_3 x tau_3 (Jackiw-Rossi), not the 3+1D chirality
T6 taste triplet [numerical]: M2 -> Xi_3, n = +1, p = +0.1 -> 2 core modes (-0.13082,-0.759,-0.718) and (+0.13082,+0.759,+0.718), taste-projected -0.941/+0.941, net 0; p = 0 gap 2 x 0.08455; mixed a M2 + b Xi_3 core nets +2, 0, +1 at (1,0.5), (0.5,1), (0.8,0.8) = n [sgn(a+b) + sgn(a-b)]
T7 pair [numerical]: 40x24 dim 1920, cores (9.5,11.5,+1) and (29.5,11.5,-1), p = +0.15 -> core0 2 modes E = +0.14948 <V_z> = +0.988, core1 2 modes E = -0.14948 <V_z> = -0.988, 16 ring states net 0; p = -0.15 nets +2/-2/0; v = 0.997
T8 link field alone [numerical]: 24x24, Gaussian tube sigma_B = 2, plaquette sums 1.0002 and 2.0004, uniform real m1 = 0.7, no vortex -> 0 in-gap states at p = -0.1, 0, +0.1, nearest |E| 0.702 and 0.700; massless control n_phi = 1, p = +0.1 -> 12 states |E| < 0.3 in +-E pairs, nearest zero E = -0.1155/+0.1155 with <V_z> = -0.864/+0.864, net 0
S solver certificate [1e-9]: 26 transverse windows, |dense LAPACK count - sparse count| max 0, max |dE| 1.4e-14, max eigenpair residual 2.1e-14, k-th eigenvalue nearest zero outside every window; no randomness and no seed anywhere
supplied: M2 itself; a winding site phase (a charged-scalar-like register the framework does not have); the profile and core position; which mover survives
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=20 FAIL=0
```

## Proof boundary

Everything is **one particle**. There is no interaction, no dynamics, no fermion determinant, no sea and no anomaly matching. The gauge field appears only as fixed Peierls phases in the `T8` control; nothing is dynamical anywhere, and no continuum limit is
taken.

The **cell algebra is as declared**: the coarse lattice with one mode per site, the Kawamoto-Smit signs, the `2x2x2` cell with its bit ordering, the landed `H(q)`, the Dirac point at `(pi,pi,pi)` and the intertwiner branch in which `Gamma`, `Xi` and `eps` take
the forms in "Definitions". `T1` and `T2` are statements about **that** algebra: the enumeration is over the 64 Pauli strings on one cell, and nothing is claimed about operators of larger support, about the fine lattice, or about a different encoding.

The string results are **numerical on open planes of the declared sizes with Bloch `q_z`**: `N = 16, 24, 32` for the single vortex, `40 x 24` for the string plus anti-string, `24 x 24` for the link-field control and the taste-triplet comparison, `8 x 8` for
the real-space anticommutator, always with `M_0 = 0.7`, `xi = 2`, window `|E| < 0.686` and `R_c = 5`. Nothing is claimed at other sizes, other profiles or periodic transverse boundaries.

The `n = 2` **string/anti-string pair on an open plane is a boundary of this note, not a result of it**. At that winding the second Jackiw-Rossi partner per core is wide, reaches the edge, and hybridises with boundary movers that the open plane's own mass
phase carries, so the per-core count is not clean at any size affordable here. The runner does not compute it, and no `n = 2` pair number is claimed. The clean `n = 2` statement in `T4` is the **single**-vortex one.

There is **no dynamics for the profile** and none for the phase: `M(rho)`, `xi`, `M_0` and the core position are declared shapes, and the `alpha_v in U(1)` register of `S2` is a proposal labelled as a charged scalar's phase, not something the framework
supplies. **Nothing here is derived from the axioms.** The Lattice axiom is quoted to locate `M2` outside its nearest-neighbour adjacency clause, which is a statement about where the operator sits, not a licence to use it.

## Review record

**Honest-auditor read.** An auditor should come away with three exact results and one numerical census, in that order. First, the anticommutant of the Dirac-point Clifford set is **exactly four Pauli strings** by complete enumeration and by an independent
nullity computation, split as a nearest-neighbour taste triplet plus one taste singlet, with every algebra residual `0.0e+00` and the node gap exact. Second, that singlet is a **body-diagonal imaginary hop of Manhattan length three**, T-odd and P-odd, and two
further complete enumerations show that nothing shorter can be a second mass at all -- no even-length hop, and nothing nearest-neighbour or face-diagonal beyond the triplet. Third, the exact square holds at `8.9e-16` and puts the taste-velocity splitting at
first order in `m_2`. Then the census: **`2n` co-moving modes per winding-`n` string, one per taste**, handed by `-Gamma_3` and not by `X`, with `-2n` on the ring or on an anti-string, on the named planes.

The auditor should also come away with five caveats. The string results are **numerical on finite open planes**, and the ring compensation is read from a splitting that is only small (`4.706e-04` at `N = 32`), not zero. The `n = 2` **pair** count on an open
plane is contaminated by boundary movers and is declared a boundary rather than a result. The handedness is a **local** property of a string: the `+2n` never appears without a `-2n`, so nothing here produces net handedness. The nearest-neighbour alternative is
computed and gives **zero**, which is a result against the easy reading of the construction, not for it. And **four items are supplied** -- the operator `M2`, a winding site phase, the profile with the core position, and the selection of which mover survives
-- so this note bounds what the declared construction gives, and not what the axioms give. The `alpha_v in U(1)` proposal is named for what it is, a charged scalar's phase by another name.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and authority" carry no grade and no weight. The ledger is fully unaudited since 2026-08-07, and no
status word in this note describes any current audit standing. Hard landing conditions are a fresh runner and cache pair closing at `PASS=20 FAIL=0`, runtime under the declared `150` seconds, and passing pipeline and strict-lint gates; independent audit
remains a separate lane.

## Validation

Run:

```bash
python3 scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py
```

Expected terminal summary:

```text
TOTAL: PASS=20 FAIL=0
```

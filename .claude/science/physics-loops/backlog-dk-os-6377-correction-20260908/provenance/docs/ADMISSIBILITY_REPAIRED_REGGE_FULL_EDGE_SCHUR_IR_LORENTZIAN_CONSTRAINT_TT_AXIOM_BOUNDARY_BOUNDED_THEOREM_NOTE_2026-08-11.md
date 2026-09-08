---
claim_id: admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_axiom_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied flat four-dimensional Kuhn/Coxeter Regge edge action S_alpha=sum_h A_h(epsilon_h+alpha epsilon_h^2) at alpha=1/1024, the ten constant-metric edge tangents have a fixed five-dimensional orthogonal complement whose zero-momentum action block is nonsingular with inertia four-negative/one-positive and absolute spectral gap above 1.28. Stationary Schur elimination of all five nonmetric directions gives a complete analytic quadratic-momentum coefficient that agrees entrywise, over all ten independent momentum monomials, with minus one-half the Euclidean linearized Einstein action pairing to maximum absolute error below 3e-13; its unit static h_tt source response is h_tt=2. Under the explicitly conditional standard Lorentzian continuation eta=diag(+,+,+,-), the frequency-squared block has four lapse/shift zeros and inertia one-negative/five-positive/four-zero, the null light-cone kernel is exactly four gauge directions plus two transverse-traceless polarizations, each TT quadratic is (omega^2-k^2)/4, the linear Bianchi identities hold, and the static source residue remains h_tt=2. The Lorentzian continuation is not selected by the current axioms and is not a Record-native causal update, physical-inner-product theorem, finite-frequency full-lattice theorem, nonlinear constraint-propagation theorem, stable nonflat phase, or axiom amendment."
upstream_dependencies:
  - minimal_axioms
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py
---

# Repaired Regge Full-Edge Schur Infrared Lorentzian Constraint And TT Boundary

**Date:** 2026-08-11

**Type:** bounded theorem

**Role:** decide whether the complete repaired fifteen-edge law actually contains the infrared Einstein constraint structure, without metric-only truncation, and then identify precisely what the axioms still fail to select.

**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.

**Primary runner:** [admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py](../scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py)

## Result Up Front

The highest-value linear gravity question has a constructive answer on the declared infrared flat scope.

For the supplied repaired Regge action

~~~text
S_alpha = sum_h A_h [epsilon_h + alpha epsilon_h^2],
alpha   = 1/1024,                                            (1)
~~~

the complete fifteen-edge Hessian contains the Euclidean linearized Einstein operator after all five nonmetric edge directions are eliminated by their own stationary equations. They are not projected away.

At zero momentum, let `M_0` be the 15-by-10 constant-metric tangent map. Its rank is ten. Let `N` be an orthonormal 15-by-5 complement and let `Q_0` be the complete repaired edge Hessian. The nonmetric block is

~~~text
C_0 = N^dagger Q_0 N.                                       (2)
~~~

Its computed eigenvalues are

~~~text
(-45.90966135,
 -15.01991039,
 -15.01991039,
 -15.01991039,
  +1.28927001).                                             (3)
~~~

Thus the repaired nonmetric block is invertible, with inertia `(4,1,0)` and absolute gap above `1.28`. The fifth flat nonmetric zero of the bare Regge action is not silently deleted in what follows.

Expand the full Bloch symbol and line-averaged metric map along any real four-direction `u`:

~~~text
Q(q u) = Q_0 + q Q_1(u) + q^2 Q_2(u) + O(q^3),
M(q u) = M_0 + q M_1(u) + q^2 M_2(u) + O(q^3).              (4)
~~~

Stationary elimination of the `N` coordinates gives a ten-component leading Schur operator `E_2(u)`. The primary runner computes its full coefficient tensor from the real-space edge kernel. On the four diagonal directions `e_mu` and the six pair sums `e_mu+e_nu`, which exhaust all ten independent quadratic momentum monomials, it finds

~~~text
E_2(u) = -1/2 G_E(u)                                        (5)
~~~

entrywise, with maximum absolute error below `3e-13`. Here `G_E(u)` is the coordinate action pairing of the four-dimensional Euclidean linearized Einstein tensor. This is not a fitted scalar prefactor: the repaired edge kernel fixes the left side, while the same coefficient and sign independently reproduce the Block-43 unit-source residue

~~~text
h_tt = 2.                                                    (6)
~~~

The result is stronger than a sampled metric congruence. It uses the complete edge equations, retains nonmetric mixing, exhausts the quadratic momentum tensor, and independently checks that direct finite-momentum Schur operators converge quadratically to (5).

The standard Lorentzian continuation of (5) can then be tested as a conditional candidate. With

~~~text
eta          = diag(+1,+1,+1,-1),
p_lower      = (k_1,k_2,k_3,-omega),
Q_L(p)       = -1/2 G_L(p),                                 (7)
~~~

the frequency-squared coefficient has eigenvalues

~~~text
(-1/2, 0,0,0,0, 1/4,1/4,1/2,1/2,1/2).                     (8)
~~~

The four zero kinetic rows are precisely `h_tt` and the three `h_it` components: lapse and shift are multipliers at this order. The remaining six spatial directions have five positive shear directions and one negative conformal direction.

For a wave along one spatial axis, `omega^2=k^2`, the ten-component operator has rank four and a six-dimensional kernel. Four dimensions are the linearized gauge family; the other two are exactly the transverse-traceless plus and cross polarizations. For either normalized polarization `e_TT`,

~~~text
e_TT^T Q_L(k,omega) e_TT = (omega^2-k^2)/4.                (9)
~~~

Thus there are exactly two degenerate light-cone tensor modes with positive frequency-squared coefficient in this conditional infrared operator. The candidate also obeys

~~~text
p^mu G_(mu nu) = 0                                          (10)
~~~

for all ten metric-coordinate basis directions, and its static unit-source constraint solve preserves (6).

Equation (10) is the linear Bianchi identity needed for conditional constraint consistency. It is not, by itself, a finite-step Record update or a nonlinear constraint-propagation theorem.

The most important remaining boundary is now unusually specific. The current axioms explicitly say that Admissibility is not dynamics and does not choose a Hamiltonian or transfer operator, provide a time metric, or supply update laws or source/action identification. They therefore do not select (7), define its physical inner product, turn its multiplier equations into a permanent-Record causal update, or identify which Record content supplies the source in (6).

This is **not a gravity no-go**. It is a localization result: the supplied repaired edge law has the correct complete-edge infrared Einstein and conditional two-TT structure, while physical law selection and causal Record evolution remain absent.

No canonical axiom is edited and no locked TOE percentage moves in this block.

## Inputs And Non-Imports

| input | used | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the `Z^3` carrier, local Admissibility distribution, permanent Records, and the explicit dynamics boundary | a selected action, time metric, Hamiltonian, transfer operator, source/action dictionary, Lorentzian continuation, or physical inner product |
| [Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | the fifteen edge classes, exact vertex-displacement columns, line-averaged metric map, and complete flat Regge Hessian | physical action selection, causal evolution, or permission to discard the fifth branch |
| [curvature-square branch lift](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | the supplied deficit-square term at `alpha=1/1024` and its fifth-branch lift | coefficient selection, nonlinear stability, or Lorentzian physics |
| [fixed-average Ward/Green result](ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the complete repaired real-space kernel, positive unit-source normalization, and residue `q^2 h_tt -> 2` | an all-volume theorem, physical mass, Lorentzian update, or a semibounded Euclidean phase |

The Lorentzian metric, choice of tick direction, analytic continuation, and interpretation of lapse/shift are supplied only for the conditional test in (7)-(10). They are not promoted into the axioms or parent claims.

## Complete-Edge Stationary Schur Derivation

The constant metric image obeys

~~~text
Q_0 M_0 = 0.                                                (11)
~~~

For the real-space kernel coefficients `Q_s` and edge directions `v`, the Taylor coefficients in (4) are computed directly as

~~~text
Q_1(u) = sum_s i(s dot u) Q_s,
Q_2(u) = sum_s -1/2 (s dot u)^2 Q_s,
M_1(u) = i/2 (v dot u) M_0.                                 (12)
~~~

Write an edge perturbation as

~~~text
delta ell = M(q u) h + N n.                                 (13)
~~~

Because of (11), the leading metric block and metric/nonmetric mixing are

~~~text
A_2 = M_0^dagger Q_2 M_0
    + M_1^dagger Q_1 M_0
    + M_0^dagger Q_1 M_1
    + M_1^dagger Q_0 M_1,

B_1 = M_0^dagger Q_1 N + M_1^dagger Q_0 N.                 (14)
~~~

The stationary equation for `n` is well posed at leading order because (2) is invertible. It gives

~~~text
E_2 = A_2 - B_1 C_0^(-1) B_1^dagger.                       (15)
~~~

Equation (15), not `M^dagger Q M` alone, is the complete metric response after the nonmetric edge coordinates satisfy their equations. This distinction is load bearing: Block 43 exhibited a false Brillouin-edge pole in the metric-only congruence that was absent from the full edge solve.

The direct numerical control evaluates the exact finite-momentum version of (15) along a generic direction at `q=0.05,0.025,0.0125,0.00625`. After division by `q^2`, the maximum errors relative to (15) decrease by approximately a factor of four at each halving and end below `2.1e-6`. This checks the analytic Taylor assembly against the unexpanded complete symbol.

## Exhaustion Of The Quadratic Momentum Tensor

Both sides of (5) are homogeneous quadratic polynomials in the four momentum components. The ten probes

~~~text
e_0, e_1, e_2, e_3,
e_0+e_1, e_0+e_2, e_0+e_3,
e_1+e_2, e_1+e_3, e_2+e_3                       (16)
~~~

determine the four square coefficients and six mixed coefficients. Agreement on (16) therefore checks every independent momentum monomial, rather than five selected directions or a fitted radial average.

At each nonzero direction in (16), `E_2` has rank six and annihilates all four continuum displacement columns

~~~text
h_(mu nu) = p_mu xi_nu + p_nu xi_mu.                        (17)
~~~

The largest Ward residual in the declared inventory is below `8e-14`.

The equality is numerical at the precision of the reconstructed real-space Regge Hessian. It is not presented as an exact radical-arithmetic proof. Its strength is completeness of the edge block and monomial inventory, not arbitrary-precision rhetoric.

## Conditional Lorentzian Canonical Structure

For a covariant perturbation `h_(mu nu)` and (7), define

~~~text
G_(mu nu) = 1/2 [
    p^2 h_(mu nu) + p_mu p_nu h
  - p_mu p^rho h_(rho nu) - p_nu p^rho h_(rho mu)
  - eta_(mu nu) (p^2 h - p^rho p^sigma h_(rho sigma))].     (18)
~~~

The coordinate pairing used in the runner is `h^(mu nu) G_(mu nu)`, including the factor of two for off-diagonal symmetric coordinates. Substituting `k=0` isolates the `omega^2` coefficient and gives (8).

The negative conformal direction in (8) is not called a propagating ghost here. Lapse and shift constraints, gauge quotient, physical-state inner product, and boundary prescription must be supplied before such a claim is meaningful. On the declared linear shell, the quotient kernel contains exactly the two TT modes and their kinetic coefficient is positive.

The runner also evaluates (18) off shell at two unequal `(k,omega)` pairs and on shell. Both polarizations give (9) to below `5e-15`, with no plus/cross mixing. This is a complete continuum-infrared tensor check, not a finite-frequency pole theorem for the full fifteen-edge analytic continuation.

## Static Source Continuity

For a unit source in the `h_tt` coordinate and static momentum along one spatial axis, both the Euclidean operator (5) and the conditional Lorentzian operator (7) solve

~~~text
Q h + e_tt = 0,
h_tt       = 2,                                             (19)
~~~

with residual below `1e-12`. The source annihilates the four gauge columns at that static momentum.

This agreement matters because it ties the candidate canonical sector to the independently reconstructed positive-source Green residue rather than merely matching a free-wave dispersion. It does not identify `e_tt` with physical mass from the axioms.

## Axiom Boundary And Candidate Update

The present result removes several physics-side excuses for postponing the axiom question:

1. the fifth nonmetric branch is lifted;
2. complete nonmetric mixing can be retained rather than projected out;
3. the full infrared coefficient is Einstein, not merely similar in selected directions;
4. a standard Lorentzian candidate has the correct multiplier count and two TT modes;
5. the positive static source residue is continuous across the Euclidean and Lorentzian infrared descriptions.

What remains absent is selection and realization. The current Admissibility axiom determines a sitewise probability distribution from nearest-neighbor conditions, but its extensional form and values are unspecified. The axiom memo further excludes Hamiltonian or transfer selection, update laws, a time metric, source/action identification, and physical persistence dynamics.

The smallest candidate axiom issue exposed here is therefore not a gravity-specific coefficient. It is whether Admissibility must be strengthened from a structural sitewise distribution statement to an **extensional local transition law on Record configurations** whose composition supplies causal precedence and preserves its constraints.

A sufficient candidate clause for later owner consideration would be:

> The one fixed local rule is supplied extensionally as a normalized, translation- and proper-cubic-covariant transition kernel on Record configurations. Its composition defines causal precedence among forming Records and preserves every local constraint of the rule.

This wording is deliberately not adopted. It is not proved necessary or minimal, and it does not by itself identify the repaired Regge action, the tick direction, a physical inner product, or Record content with stress-energy. A downstream bridge theorem could supply all of those without changing the four axioms. The next constructive campaign should try that route before recommending a canonical edit.

If the downstream route repeatedly fails, the amendment target should remain at this abstract extensional-dynamics level. Inserting the Einstein tensor, `alpha=1/1024`, two TT modes, or a Lorentzian signature directly into the minimal axioms would overfit one candidate realization.

## Three-Hour Portfolio Gate

This result changes the gravity priority ordering.

| rank | seam | reason for current leverage | stop or pivot condition |
|---:|---|---|---|
| 1 | Record-native extensional transition and law selection | it is now the shortest path from a mathematically viable Einstein/TT sector to physical TOE content | pivot if no current-axiom construction can choose causal order, constraint preservation, and source semantics without adding a premise |
| 2 | full fifteen-edge finite-frequency Lorentzian constraint/pole continuation | tests whether the infrared candidate prolongs to the actual repaired lattice without an extra branch | stop once it either gives four gauge plus two TT roots with a separated remainder or exposes the first unavoidable lattice obstruction |
| 3 | physical inner product or reflection-positive transfer reconstruction | needed to turn positive TT kinetic coefficients into a physical positivity statement | defer until an update/transfer object is explicit |
| 4 | stable nonflat stationary phase and nonlinear constraints | required for gravity beyond the flat linear sector | defer until the causal law being stabilized is selected |
| 5 | analytic all-zone and full-`Z^3` static control | strengthens Block 43 but no longer decides whether gravity exists in the candidate | pursue only if it closes a dependency of ranks 1-4 |

Extra finite grids, additional precision, alternate metric projections, and more Euclidean subspace scans are demoted unless they can reverse one of these decisions. The portfolio should be rerun after each deep block and at least every three hours against the newest exact branch evidence and current `origin/main` axiom surface.

## Fresh No-Go Discipline Packet

This packet governs only the narrow statement that the **current axiom surface and supplied repaired Euclidean law do not themselves select or define the Lorentzian Record update**. It does not claim that such an update cannot be derived downstream and does not ship a gravity no-go.

### N1 — Alternative-Route Enumeration

| route | status after this block | discriminating result |
|---|---|---|
| complete repaired full-edge stationary Schur | succeeds in the infrared | gives (5), exact four-direction Ward kernel, and the static residue |
| bare Regge full-edge law | inherited boundary | retains the fifth nonmetric zero |
| metric-only projection or congruence | rejected as authority | can create a false pole because the metric image is not invariant |
| standard Lorentzian Einstein continuation | succeeds conditionally | gives multiplier count, two TT modes, Bianchi identity, and static continuity |
| repaired full-lattice analytic pole continuation | live | can test finite-frequency TT roots and separation from nonmetric modes |
| canonical Hamiltonian discretization | live | may derive constraints and update without an axiom change |
| reflection-positive transfer reconstruction | live | may supply the physical state space and continuation from Euclidean data |
| Record-native stochastic transition kernel | live and highest priority | may select causal order and realize the Admissibility distributions directly |
| stable nonflat phase | live | can change the background and nonlinear constraint algebra |
| direct Record-content/source bridge | live | may derive the source semantics in (19) independently of update selection |
| owner-approved extensional-dynamics amendment | sufficient candidate only | available only if downstream derivations fail and necessity/minimality are established |

The successful first and fourth routes defeat any broad impossibility claim. The live downstream routes defeat a present claim that a fifth axiom is already necessary.

### N2 — Wall-Independence Audit

The remaining walls are

~~~text
W1 = physical selection of one extensional law,
W2 = causal Record update and clock orientation,
W3 = physical inner product or positivity reconstruction,
W4 = finite-frequency full-lattice constraint and mode control,
W5 = nonlinear stable nonflat phase and constraint propagation,
W6 = Record-content to physical source/action identification.        (20)
~~~

| pair | independence check |
|---|---|
| W1/W2 | selecting an action or kernel does not prove which composition is causal; a causal update need not uniquely select its coefficients |
| W1/W3 | law selection does not construct a physical inner product; positivity can hold for more than one candidate law |
| W1/W4 | selecting the infrared law does not prove its full-zone spectrum; a good lattice spectrum does not select the law |
| W1/W5 | microscopic selection does not prove a nonlinear phase or propagated constraints |
| W1/W6 | selecting geometry dynamics does not identify Record content with a physical source |
| W2/W3 | causal composition does not by itself make the reduced state norm positive |
| W2/W4 | an abstract update can exist while the repaired lattice develops extra finite-frequency modes |
| W2/W5 | linear causal order does not prove nonlinear constraint preservation |
| W2/W6 | an update order does not determine source semantics |
| W3/W4 | a physical inner product does not supply uniform full-zone mode separation |
| W3/W5 | linear positivity does not prove stable nonflat existence |
| W3/W6 | positivity does not identify which Records carry stress-energy |
| W4/W5 | finite-frequency flat control does not prove nonlinear nonflat propagation |
| W4/W6 | a clean pole inventory does not supply a source dictionary |
| W5/W6 | a stable phase may exist without a physical Record/source identification, and conversely |

No wall is counted as evidence for another.

### N3 — Hidden-Wall Scan

The result assumes the supplied action (1), `alpha=1/1024`, flat background, reconstructed double-precision real-space Hessian, line-averaged metric map, fixed orthogonal complement at zero momentum, standard stationary Schur prescription, one tick direction, metric signature in (7), and standard analytic Lorentzian tensor continuation. It does not derive a foliation, clock rate, Planck scale, physical source, boundary state, action selection, probability weights, or Record update.

The fixed complement `N` is a coordinate choice for the stationary calculation. The effective coefficient is checked against direct finite-momentum Schur elimination; no physical meaning is assigned to individual nonmetric basis vectors.

### N4 — Residual Matching

The Einstein comparison matches every entry of the complete ten-by-ten quadratic coefficient for all ten independent momentum monomials. It is not inferred from two TT eigenvalues alone.

The source comparison solves the full leading Schur equation with the same unit `h_tt` source orientation as Block 43 and reports its equation residual. The Lorentzian mode claim separately checks operator rank, gauge rank, span rank, null residual, both TT quadratic forms, their mixing, and the Bianchi contraction.

The axiom boundary is matched to explicit sentences in the current axiom memo excluding Hamiltonian/transfer selection, update laws, a time metric, and source/action identification. It is not inferred merely from failure of one numerical construction.

### N5 — Five-Resolution Cache

| resolution | exhaustive content in the primary runner |
|---|---|
| per element | all fifteen edge classes, all ten metric coordinates, and every matrix entry in the tested coefficients |
| per site | the flat unit-cell tangent split and one Ward-compatible unit static source |
| per mode | all ten quadratic momentum monomials, a generic finite-momentum convergence sequence, one null shell, and two off-shell TT samples |
| per block | the complete `15=(10+5)` Schur block, the six-dimensional kinetic block, four multiplier rows, null shell, and Bianchi contraction |
| lattice wide | the translation-invariant real-space kernel fixes the infrared coefficient; no all-zone, full-`Z^3` phase, nonlinear, or causal-update theorem is claimed |

The generated cache repeats this certificate and ends in `TOTAL: PASS=n FAIL=n`.

### N6 — Partial-Closure Paths

Nonempty constructive paths remain:

1. use (5) as the infrared acceptance criterion for a Record-native transition kernel;
2. continue the complete repaired fifteen-edge symbol to finite frequency and test its pole quotient;
3. build a canonical lattice constraint update and prove its linear preservation identity;
4. construct a reflection-positive transfer object and derive the Lorentzian physical state space;
5. derive Record-content/source semantics while retaining the static residue (19);
6. stabilize a nonflat phase after the law and update are selected;
7. if all downstream routes fail, return to the abstract candidate Admissibility amendment above.

This block itself closes two partial paths: full-edge infrared Einstein recovery and a conditional two-TT canonical decomposition.

### N7 — Steelman

The strongest opposing case is that no axiom change is needed. The current axioms intentionally leave detailed physics downstream. A local Record transition kernel, Hamiltonian constraint system, or reflection-positive transfer construction may be derived from the already fixed Admissibility distribution and permanent Record structure. If any such construction selects (7), preserves its constraints, and derives the source dictionary, it defeats the candidate-axiom route completely.

This steelman is live and strong. Therefore the candidate clause is not adopted and not proved necessary. The only surviving negative statement is textual and narrow: those dynamics and selection data are not presently supplied or derived on the current surface.

### N8 — Cross-Cycle Echo

Earlier Regge work found a projected Einstein comparison but retained an exact fifth branch. The curvature-square block lifted that branch. Block 43 then proved complete-edge Ward compatibility and the positive-source Green residue while showing that metric-only restriction can create a false pole. Separate Euclidean connection work found an instability in a different unchanged Record/EC flat saddle.

This block adds a new result rather than repeating those boundaries: it eliminates the repaired nonmetric sector through its own equations, exhausts the full quadratic momentum tensor, derives the complete infrared Einstein operator, and tests the associated conditional canonical mode count.

**Status: PASS.** The narrow current-surface boundary survives N1-N8. Broad gravity impossibility, fifth-axiom necessity, and rejection of downstream constructive routes do not.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py
~~~

Expected final line:

~~~text
TOTAL: PASS=15 FAIL=0
~~~

The runner is source-bound to this note, the current minimal axioms, all three parent science notes, the premise registry, and the three Regge construction scripts. It prints the five-resolution certificate and the scope boundary.

## Conclusion

The repaired complete-edge Regge law does not merely resemble gravity after a ten-metric projection. Once all five nonmetric edge directions satisfy their stationary equations, its full infrared quadratic coefficient is the linearized Einstein operator with the sign and normalization required by the independently derived positive-source residue. The conditional standard Lorentzian continuation has lapse and shift multipliers, exactly two degenerate TT light-cone modes, positive TT kinetic coefficient, and the linear Bianchi identity.

The highest-leverage remaining TOE problem is consequently not another Euclidean spectrum or larger static torus. It is to derive or reject a Record-native extensional transition law that selects the causal continuation, preserves constraints, supplies a physical state space, and identifies Record content with the source. Only after that constructive route is exhausted should the abstract Admissibility update be considered for canonical adoption.

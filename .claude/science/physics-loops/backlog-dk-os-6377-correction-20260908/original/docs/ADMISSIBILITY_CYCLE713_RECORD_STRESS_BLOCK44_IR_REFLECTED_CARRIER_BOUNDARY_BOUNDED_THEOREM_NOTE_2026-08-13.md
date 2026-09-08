---
claim_id: admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: >-
  Conditional on identifying one Block-67 signed head finalization with the
  supplied unit spacetime step u=(d,1) and one unfixed scalar source coupling,
  the six axial rank-one Record stresses have a unique weighted ten-coordinate
  covector in the supplied Block-44 coordinate convention.  The covector
  obeys the exact continuum Ward identity on omega=q dot d, solves the
  conditional Block-44 Lorentzian linear equations both off the gravity light
  cone modulo four gauge directions and on the matched axial light cone after
  the two TT compatibility conditions, and has the required signed mixed-time
  entries.  The supplied fifteen-edge orientation carries only the three
  future-positive axial steps.  Its supplied twenty-two-edge time-reflection
  union carries all six, and closed transversely neutral line pairs have exact
  finite-frequency edge Ward compatibility, compact-zero-mode cancellation,
  complete-null compatibility, and direct unprojected solutions on all 6,528
  nonzero direction-mode samples of periodic L=3 through L=8 tori.  The
  reflected union still has a thirteen-dimensional constant flat fiber rather
  than one selected ten-component metric.  Physical head/source typing,
  source density and coupling, cadence, common-metric or cross-orientation
  law, Lorentzian finite-frequency transfer, physical inner product, causal
  update, nonlinear constraints and self-coupling, axiom adoption, audit
  retention, obligation retirement, and TOE percentage movement are not
  claimed.
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_bounded_theorem_note_2026-08-13
  - admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_axiom_boundary_bounded_theorem_note_2026-08-11
  - admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_bounded_theorem_note_2026-08-11
  - admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_bounded_theorem_note_2026-08-11
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
  - admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py
---

# Cycle713 Record stress to Block44 IR and reflected-edge carrier boundary

**Date:** 2026-08-13

**Type:** bounded theorem candidate
**Status:** partial-narrowing; unaudited; unretained; no canonical axiom is edited

TOE accounting: **zero TOE percentage movement and zero obligation
retirement**.  This packet resolves a high-value conditional interface and
changes gravity-route confidence.  It does not promote its unretained parents
or complete a physical gravity law.

## Result up front

Gravity survives the source test, conditionally and linearly.

Block67 writes its null-source diagnostic in `(t,x,y,z)` order.  Block44 uses
`(x,y,z,t)` and the symmetric-coordinate order

~~~text
(xx, yy, zz, tt, xy, xz, xt, yz, yt, zt).                 (1)
~~~

After the permutation `(1,2,3,0)`, let

\[
 u=(d_x,d_y,d_z,1),\qquad T^{\mu\nu}=A u^\mu u^\nu .      \tag{2}
\]

The source is a covector on the ten symmetric metric coordinates.  Up to one
global coupling `g`, its unique coordinate vector is

\[
 j(g,A,d)=gA(d_x^2,d_y^2,d_z^2,1,
 2d_xd_y,2d_xd_z,2d_x,2d_yd_z,2d_y,2d_z).                 \tag{3}
\]

The factor two on every off-diagonal coordinate is load-bearing.  There is no
extra minus sign on `xt`, `yt`, or `zt`: Lorentzian lowering and Block44's
raising sign cancel in the variational pairing.  Reversing `d` therefore keeps
`T00` and `Tij` even while reversing `T0i`, exactly as required by the signed
Record current.

For Block44's lower momentum

\[
 p_\mu=(q_x,q_y,q_z,-\omega),                              \tag{4}
\]

the exact identity is

\[
 \Gamma(p)^Tj=2gA\,(q\!\cdot\!d-\omega)u.                 \tag{5}
\]

Thus the source is Ward-compatible on its straight-worldline Fourier support
`omega=q dot d`; it is not asserted conserved at arbitrary momentum or merely
because a gravity momentum is null.  At generic compatible momentum off the
gravity light cone, the conditional Block44 operator has rank six and the
response is unique modulo four gauge directions.  On the matched axial light
cone it has rank four; the source also annihilates the two TT cokernel modes
and is solvable, with two physical homogeneous TT modes left over.

The original fifteen-edge Kuhn orientation contains `(e_i,+t)` but not the
three future-negative axial steps.  The existing time-reflection union has 22
edge classes and contains a canonical unoriented representative of all six
steps.  A coefficient-two mixed edge pulls back to `(1/sqrt(2))` times (3).
The `sqrt(2)` is an edge-length/source-density convention, not a selected
physical coupling.  In particular, the static tick-edge unit-source control
and a moving diagonal edge do not establish a common physical normalization.

Closed lines in each of the six directions, paired with an oppositely weighted
parallel line one transverse lattice step away, then give exact finite-symbol
Ward sources.  Across every Fourier mode on `L=3,...,8`, the runner finds 6,528
nonzero direction-mode sources.  Every one annihilates the complete edge null
space and directly solves the unprojected 22-edge equations; the numerical
Ward and solve maxima are printed by the runner.  Neutral pairing cancels the
compact zero mode.  A single positive compact line retains a nonzero zero-mode
residual and is deliberately rejected.

This is not yet one metric theory.  The reflected union's constant flat fiber
is 13-dimensional: ten common-metric directions plus three relative `h_it`
directions.  A common-metric quotient or a local cross-orientation action,
together with the source/clock/transfer selection, is still required.

## Inputs, ownership, and non-imports

This packet consumes these conditional surfaces without promoting them:

- the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), solely for the explicit
  dynamics and source-selection boundary;
- the [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
  which supplies only the Euclidean `c_t=c_s` form and does not identify a
  Record tick with physical time;
- [Block67](ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md),
  for the content-decoded six-direction signed head source and its conditional
  rank-one stress;
- [Block44](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md),
  for the complete-edge infrared Schur coefficient and explicitly conditional
  Lorentzian Einstein operator;
- [Block47](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md),
  for the analytic full-edge symbol, line-averaged metric map, exact gauge map,
  and nonmetric complement;
- [Block48](ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md),
  for the 22-edge reflected union and its disclosed 13-versus-10 fiber;
- the [closed-helix parent](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
  for the exact line telescope and compact neutralization pattern; and
- the [joint-law cut](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md),
  for the separation of source, clock, constraint, and coupling controls.

None of these is treated as retained.  Record permanence and
content-determined readability do not identify a physical stress tensor.  The
current axioms do not select `g`, a source density, an action, a Lorentzian
continuation, a common-metric quotient, a physical inner product, or an update.

## 1. The unique weighted ten-coordinate source map

Let `h_a` be Block44's ten symmetric metric coordinates.  The variational
pairing with a symmetric tensor is

\[
 T^{\mu\nu}h_{\mu\nu}
 =\sum_{\mu}T^{\mu\mu}h_{\mu\mu}
  +2\sum_{\mu<\nu}T^{\mu\nu}h_{\mu\nu}.                   \tag{6}
\]

Equation (6) fixes the diagonal weight one and off-diagonal weight two.  The
resulting linear map from `Sym^2(R^4)` to the ten coordinate covectors has rank
ten.  Once Block44's time index, future orientation, and the stored proper
cubic spatial frame are fixed, no coordinate freedom remains except the one
overall source coupling.  A single null ray alone would not fix those frame
conventions; the uniqueness claim is explicitly relative to the supplied
Block44 and Block67 conventions.

For the six axial directions, (3) gives:

| `d` | nonzero entries of `j/(gA)` |
|---|---|
| `+x` | `xx=1, tt=1, xt=+2` |
| `-x` | `xx=1, tt=1, xt=-2` |
| `+y` | `yy=1, tt=1, yt=+2` |
| `-y` | `yy=1, tt=1, yt=-2` |
| `+z` | `zz=1, tt=1, zt=+2` |
| `-z` | `zz=1, tt=1, zt=-2` |

Omitting the mixed-coordinate factor two or feeding lowered mixed components
directly fails (5).  At `d=+x` and `p=(1,0,0,-1)`, the undoubled mutation has
Ward residual `sqrt(2)`; the wrong mixed sign has residual `4 sqrt(2)`.

## 2. Continuum Ward completion and conditional Lorentzian response

For any symmetric spatial stress `S_ij` and nonzero frequency, the four time
components required by the Ward identity are uniquely

\[
 T^{it}=\frac{(Sq)_i}{\omega},\qquad
 T^{tt}=\frac{q^TSq}{\omega^2}.                            \tag{7}
\]

Consequently the compatible source space has dimension six at every nonzero
generic momentum.  Setting `S=d d^T` and `omega=q dot d` recovers (2)-(3).
At `omega=0` the completion changes character: existence requires `q^T S=0`,
while transverse mixed components and `Ttt` remain free.  No division by zero
or false uniqueness is inferred there.

The runner applies (3) to all six directions in two regimes:

1. With transverse spatial momentum present, source support and the gravity
   characteristic cone differ.  The Block44 operator has rank six, the source
   obeys all four Ward constraints, and the equation solves modulo four gauge
   directions.
2. With spatial momentum parallel to `d`, the source and gravity shells meet.
   The operator has rank four.  The matched axial source passes the two extra
   TT compatibility conditions and solves; two TT homogeneous modes remain.

This does not say that one of the six axial sources works at every point on the
gravity null cone.  A generic nonaxial null momentum need not lie on any one of
their six worldline supports.  Source support and graviton characteristic
support are distinct conditions.

As a normalization control only, Block44's static unit `e_tt` source again
gives `h_tt=2`.  It is not equated to the moving mixed-edge source density.

## 3. Exact full-edge source reduction in the original orientation

Let `M(p)` be Block47's line-averaged 15-by-10 metric map, `C(p)` the continuum
metric gauge map, and `G_edge(p)` the exact vertex-displacement edge map.  The
line-average sinc identity gives

\[
 M(p)C(p)=-iG_{\rm edge}(p).                               \tag{8}
\]

Thus no hand-inserted centered difference is used.  After splitting the five
fixed nonmetric directions into the columns of `N`, the correct source in the
ten-coordinate stationary Schur equation is not merely `M^dagger j_edge`.
It is

\[
 j_{\rm eff}=M^\dagger j_{\rm edge}
 -Q_{hn}Q_{nn}^{-1}N^\dagger j_{\rm edge}.                 \tag{9}
\]

The runner reconstructs the full 15-edge response after this elimination.
Dropping the second term leaves an order-`p^2` edge-equation residual and is a
killed mutation.  For the actual edge `(1,0,0,1)` on `p dot v=0`, (9) is
Ward-compatible and approaches

\[
 \frac{1}{\sqrt 2}(1,0,0,1,0,0,2,0,0,0)+O(p^2).           \tag{10}
\]

The original edge inventory has the analogous future-positive `y` and `z`
edges, but no one-edge representatives of `(-e_i,+t)`.  This is a carrier
inventory boundary, not a gravity no-go and not a failure of the continuum
map.

## 4. Six-sign reflected carrier and exact neutral lines

Let the physical supplied step be

\[
 w_d=(d,1).                                                \tag{11}
\]

In the 22-edge reflected union, use `c_d=w_d` when that label exists.  For a
future-negative step, use the canonical reversed label `c_d=-w_d`, based at
the future endpoint.  Because the metric source depends on `c_d c_d^T`, both
orientations pull back to the same even diagonal/spatial stress and the
correct odd mixed-time sign in (3).  All six use the same coefficient two and
the same unselected overall density convention.

On an `L^4` torus, one closed line has Fourier factor

\[
 H_d(p)=\sum_{n=0}^{L-1}e^{ip\cdot(nw_d+b_d)},             \tag{12}
\]

where `b_d=0` for the forward representative and `b_d=w_d` for the reversed
representative.  Choose one purely spatial transverse lattice step `a_d` and
subtract the translated parallel line.  The edge-source row is

\[
 f_d(p)=2H_d(p)(1-e^{ip\cdot a_d})e_{c_d}.                 \tag{13}
\]

The closed-line telescope gives

\[
 f_d(p)^\dagger G_{\rm union}(p)=0                        \tag{14}
\]

on every mode.  The transverse factor cancels `p=0` exactly.  The runner tests
every mode for every signed direction on each torus `L=3,...,8`.  There are
6,528 nonzero direction-mode sources.  Their complete union-symbol nullity is
four or five; every source annihilates the whole null space and the direct
unprojected equation

\[
 Q_{\rm union}(p)h_d(p)+f_d(p)^*=0                         \tag{15}
\]

solves to the printed tolerance.  Removing the final line edge breaks the
telescope and is a killed mutation.

A single positive closed line has nonzero total compact source.  At `p=0`,
`Q_union(0)` cannot solve it; on the declared `L=5` control its residual is
about `7.78457`.  Neutral pairing is therefore substantive.  It proves a
background-subtracted or signed source family, not a positive-mass ensemble.
An open/infinite boundary or fixed-global-mode domain remains an alternative
for a net-positive source.

The finite-frequency statement in this section is Euclidean and edge-level.
The Bloch tick coordinate is not silently renamed Lorentzian time.  The
conditional Lorentzian result in Section 2 is infrared tensor algebra only.

## 5. What this closes locally, and what remains open

Subject to its explicit premises, this candidate closes these Block67
interface subwalls:

- the `(t,x,y,z)` to Block44 coordinate permutation;
- symmetric-coordinate multiplicity and the sign of all three `T0i` entries;
- the exact continuum source Ward/Bianchi compatibility condition;
- conditional linear Block44 solvability off and on the matched axial light
  cone;
- exact edge phase/staggering for six signed periodic carriers;
- compact zero-mode repair by one explicit neutral pair; and
- full unprojected edge solvability on the declared finite inventory.

It does **not** close or select:

1. the identification of a decoded Record head with physical matter or
   stress;
2. the cadence assumption that one head finalization is one unit Block44 tick;
3. one physical source density, sign, coupling, or equality between tick-edge
   and diagonal-edge normalizations;
4. the action coefficient or a local law selecting the reflected union;
5. the three-component relative-`h_it` to common-metric intertwiner;
6. a Lorentzian full-frequency operator, physical inner product, positive
   transfer, causal update, or Record clock;
7. nonlinear constraints, gravitational self-source, accelerated histories,
   collisions, or multiple interacting fronts;
8. axiom adoption, independent audit retention, or any tracked TOE
   obligation.

The next gravity decision is therefore not another TT projection or another
Record-history variant.  It is one joint common-metric source/clock/transfer
law, or a demonstration that the current axioms cannot select that law without
an explicit premise update.

## 6. No-go discipline N1-N8

### N1 — alternative-route enumeration

| route family | result | evidence and boundary |
|---|---|---|
| weighted continuum tensor covector | `ATTEMPTED`, succeeds conditionally | Sections 1-2 and runner checks B-E; cadence, typing, and scale supplied |
| lowering then Block44 row raising | `ATTEMPTED`, succeeds and agrees | Block44 pairing convention; direct lowered mixed entries are rejected |
| original 15-edge one-diagonal lift | `ATTEMPTED`, partial | Section 3; future-positive axes succeed, future-negative labels are absent |
| fixed local multiedge lift in the original orientation | `UNTESTED` | a zero-momentum fit is insufficient; no finite-support all-zone solution is ruled out |
| 22-edge reflected-union lift | `ATTEMPTED`, succeeds on declared neutral lines | Section 4 and checks G-H; 13-versus-10 metric fiber remains |
| momentum-dependent edge pseudoinverse | `ATTEMPTED`, algebraically live | can close Ward mode-by-mode but is nonlocal and is not a Record-local law |
| open/infinite or fixed-global-mode positive source | `ATTEMPTED` in the helix parent | removes the compact constant obstruction but changes the boundary/domain |
| common-metric or local cross-orientation action | `ATTEMPTED`, incomplete | Block48 supplies a conditional metric-first repair; no selected local law |
| Record-native joint source/clock/transfer update | `UNTESTED` extensionally | Block46 names the controls; current axioms do not give their values |

Because several route families survive, the **No-Go Gate: FAIL**.  The allowed
output is **partial-narrowing**, not “gravity cannot work,” “the source cannot
couple,” or any equivalent universal negative.

### N2 — collapsed-wall independence audit

| wall | independent content | why another wall does not imply it |
|---|---|---|
| W1 source typing | head content is physical stress | Ward compatibility does not make a Record carrier matter |
| W2 cadence | one finalized head step sets `u_t=1` | kinetic isotropy fixes a Euclidean form, not a Record clock |
| W3 normalization | one density/coupling and sign convention | coordinate uniqueness leaves one global scalar free |
| W4 common metric | quotient/couple the three relative `h_it` modes | full-edge solvability does not reduce the 13-dimensional fiber to ten |
| W5 physical transfer | inner product, continuation, and causal update | a Euclidean Green solve is not a Lorentzian transfer theorem |
| W6 nonlinear completion | constraints and gravitational self-source | linear Bianchi compatibility does not propagate nonlinear constraints |
| W7 physical instrument | same-M2 source occurrence and readout | a source decoder formula does not compile or select its CP instrument |

No pair is merged in the conclusion.  A future axiom proposal should target
the smallest irreducible missing law content, not encode the successful
Einstein tensor or this particular reflected carrier by fiat.

### N3 — hidden-wall and rhetoric scan

The claim is restricted to the supplied flat action, conditional Block44
signature, axial unit steps, one supplied scalar, periodic neutral line pairs,
and `L=3,...,8`.  It does not use “only if,” “cannot,” “impossible,” “must add
an axiom,” or “complete” beyond the narrow coordinate and inventory facts
proved here.  “Unique” always means unique after the explicit Block44 order,
future orientation, stored cubic frame, symmetric pairing, and one free global
coupling are fixed.  The finite lattice result is not called Lorentzian.

### N4 — citation-residual audit

| cited source and exact lines | fact consumed | residual not imported |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:117-124` | Admissibility is not a dynamics axiom | no action, source dictionary, time metric, or update |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:17-24,38-55` | supplied Euclidean `c_t=c_s` form | no physical Wick/Record clock |
| `docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md:222-275` | conditional head current and `k=(1,d)` stress | no physical head typing, cadence, coupling, or Block44 source map |
| `docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:69-109,181-219` | Einstein-Schur coefficient, Ward kernel, conditional Lorentzian ranks, static residue | no selected continuation, physical source, or nonlinear law |
| `docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:43-68,148-214` | exact full-edge gauge map and nonmetric Schur dressing | no physical transfer or source law |
| `docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:136-215` | 22-edge union and exact 13-versus-10 fiber | no common-metric selection or local cross-orientation action |
| `docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:45-83,150-223` | closed-line telescope, neutral zero mode, full-null solve pattern | no positive-mass ensemble, occurrence law, or universal carrier |
| `docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md:34-65,242-252` | independent source/clock/constraint/coupling controls | no selected extensional joint law |

### N5 — resolution-level audit

The runner emits the required five explicit resolution lines after its ten
aggregate checks:

- `per_element`: all coordinate weights, signs, carrier orientations, gauge
  columns, source rows, and the compact zero contribution;
- `per_sample`: generic continuum regimes and every one of the 6,528 nonzero
  direction-mode sources;
- `per_block`: the typed Block67, Block44, Block47, and Block48 interfaces;
- `lattice_wide`: all six velocities on the declared `L=3,...,8` periodic
  inventory, with arbitrary volume explicitly excluded; and
- `scope_boundary`: every physical-law and adoption wall named again.

### N6 — partial-closure paths

Several narrower positive paths remain live even if the selected joint law
does not yet exist: retain only the continuum IR intertwiner; adopt a
fixed-global-mode domain for net-positive sources; construct a local
cross-orientation metric quotient; use a refined cell with both temporal edge
orientations; or derive a Record-native cadence and source density before
returning to transfer positivity.  These are not weakened no-go claims.

### N7 — steelman

The strongest constructive reading is that the time-reflected edge union is
already the right auxiliary carrier.  This packet shows that its allegedly
problematic signed directions are not a source obstruction: all six have exact
neutral full-edge solutions.  If a local common-metric cross term can remove
only the relative `h_it` sector while preserving the four gauge columns, and a
single Record law fixes cadence and coupling, the existing Einstein-Schur
sector could become one end-to-end linear gravity candidate.  Nothing here
rules that out.

### N8 — cross-cycle echo

Earlier vertical-line failure was repaired by a genuine closed helix; the
compact positive-source obstruction was repaired by neutral pairing or a
fixed-global-mode domain; the single-orientation complex transfer diagnosis
was narrowed by the reflected common-metric candidate; and Block67 repaired
the loss of signed `T0i` at the Record level.  Repeating any of those broader
negative conclusions here would ignore already demonstrated counterroutes.
The residual issue is law selection and the 13-to-10 metric intertwiner, not a
recycled assertion that gravity or source conservation fails.

## Falsifiers and rerun

This bounded result fails if any of the following occurs:

- the six-axis coordinate truth table or factor-two pairing fails;
- equation (5) fails on `omega=q dot d` or the off-shell mutation survives;
- any declared conditional Block44 source is outside the operator range;
- dropping the nonmetric source correction still solves the full edge system;
- any signed axial step lacks a representative in the 22-edge union;
- any one of the 6,528 neutral sources violates edge Ward, complete-null
  compatibility, or the unprojected solve;
- a lone compact positive line unexpectedly solves its zero mode; or
- the note promotes cadence, coupling, common metric, Lorentzian transfer,
  nonlinear dynamics, adoption, retention, or TOE movement.

Run:

~~~bash
python3 scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py
~~~

The mutation choices are `wrong_order`, `omit_offdiag_two`,
`off_shell_source`, `flip_mixed_sign`, `drop_nonmetric_correction`,
`original_only`, `drop_closure_edge`, `keep_zero_mode`, and
`broaden_boundary`.  Every mutation is required to produce exactly one failed
aggregate check while the unmutated runner produces none.

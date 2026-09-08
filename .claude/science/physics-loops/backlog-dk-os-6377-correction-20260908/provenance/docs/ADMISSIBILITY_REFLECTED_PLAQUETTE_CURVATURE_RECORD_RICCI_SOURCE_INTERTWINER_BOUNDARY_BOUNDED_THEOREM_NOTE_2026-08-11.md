---
claim_id: admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied twenty-two-edge original-plus-time-reflected Kuhn/Coxeter union, three elementary space-time parallelogram rows are exact finite-range displacement-gauge intertwiners. At zero momentum they annihilate the ten-dimensional common-metric fiber and map the three relative forward/backward h_it directions isomorphically. At nonzero momentum, however, their plaquette-centered restriction to the line-averaged common metric factors exactly into a strictly positive principal-Brillouin-zone form factor times q_i^2 h_tt - 2 q_i q_t h_it + q_t^2 h_ii, the linearized time-space sectional-curvature polynomial up to convention. Thus a homogeneous hard-zero constraint removes the unwanted relative constant modes but also forbids the nonzero Newtonian curvature response. The inherited rank-one Record stress gives an exact additive trace-reversed temporal/Ricci source, but a continuous proper-cubic and time-reflection covariant trace-free sectional decoder family has the same contraction and distinct generic metric lifts. The missing joint law is therefore a sourced connection/curvature propagation and physical-transfer rule, not equality of the two orientation metrics. This is an exact local linearized intertwiner and source-allocation boundary, not a selected nonlinear gravity law, gravity no-go, Lorentzian update, axiom amendment, or TOE closure."
upstream_dependencies:
  - minimal_axioms
  - admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_bounded_theorem_note_2026-08-11
  - admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_bounded_theorem_note_2026-08-10
  - admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_bounded_theorem_note_2026-08-11
  - admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_axiom_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py
---

# Reflected Plaquette Curvature / Record Ricci-Source Intertwiner Boundary

**Date:** 2026-08-11

**Type:** bounded theorem

**Role:** resolve Block 48's three-component orientation-shift intertwiner and
decide whether it can be imposed as the missing common-carrier constraint.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py](../scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py)

## Result Up Front

The exact three-component intertwiner exists, but hard zero is not the physical
gluing law.

For each spatial axis `i`, the twenty-two-edge reflection union contains the
two diagonals and four sides of one elementary `i-t` parallelogram. With edge
length deviations based at the cell origin, define

~~~text
C_i(q) ell = sqrt(2) ell_(i+t)
           + sqrt(2) exp(i q_t) ell_(i-t)
           - [1+exp(i q_t)] ell_i
           - [1+exp(i q_i)] ell_t.                         (1)
~~~

The phases in (1) are base-point shifts, not fitted Fourier decorations. The
runner verifies exactly on the declared real and complex controls that

~~~text
C(q) Gamma(q) = 0,     rank C(q)=3,                         (2)
~~~

for the complete four-column vertex-displacement map `Gamma`. After shifting
each row to the plaquette center,

~~~text
D_i(q) = exp[-i(q_i+q_t)/2] C_i(q),                         (3)
~~~

the three rows are time-reflection even under Block 48's momentum-dependent
edge-label involution.

At zero momentum, `C(0)` annihilates all ten common constant-metric directions
and maps the three relative forward/backward mixed-time directions to `2 I_3`.
It therefore gives the exact algebraic quotient that Block 48 requested.

At nonzero momentum it is not merely metric compatibility. Let `M_line(q)` be
the exact line-averaged metric-to-edge map and let

~~~text
K_i(q;h) = q_i^2 h_tt - 2 q_i q_t h_it + q_t^2 h_ii.       (4)
~~~

Then the exact reflected plaquette curvature intertwiner satisfies

~~~text
D_i(q) M_line(q) h = F(q_i,q_t) K_i(q;h),                  (5)

F(a,b) = {sinc[(a-b)/2] - sinc[(a+b)/2]} / (2ab),          (6)
F(0,0) = 1/12.                                             (7)
~~~

Here `K_i` is, up to the stated Riemann-sign and factor convention, the
linearized `R_itit` sectional-curvature polynomial. The form factor is strictly
positive for `a,b` in the principal Brillouin zone. Consequently (5) has no
curvature-blind zero there.

This changes the proposed repair. Setting `C ell=0` removes the three unwanted
constant relative `h_it` modes, but on a static axis it also sets
`q_i^2 h_tt=0`. The Block-48 common-metric unit-source response instead gives

~~~text
D_x M_line h = 0.166670355... at q_x=0.025,
lim_(q_x->0) D_x M_line h = 1/6.                            (8)
~~~

Thus the hard constraint deletes the Newtonian sourced curvature that the
gravity route is required to retain.

The Record-source composition advances one step but does not finish the law.
For the inherited edge-labelled Record with positive rank-one Euclidean metric
stress

~~~text
T_e = v_e v_e^T / (2 |v_e|),                               (9)
~~~

the trace-reversed temporal contraction is exactly

~~~text
J_e = (T_e)_tt - (1/2) tr(T_e)
    = [2(v_e)_t^2-|v_e|^2] / (4|v_e|).                    (10)
~~~

It is additive, proper-cubic covariant, and even under time reflection. It is
the natural conditional Record-to-Ricci source supplied by the already
conditional Einstein identification.

But (10) fixes only the sum of the three sectional equations. For any real
`eta`, the local decoder

~~~text
j_i^(eta)(e) = J_e/3
  + eta [(v_e)_i^2-|v_e,sp|^2/3] / (2|v_e|)                (11)
~~~

obeys

~~~text
sum_i j_i^(eta)(e) = J_e                                   (12)
~~~

and has the same translation, proper-cubic, time-reflection, and Record
additivity properties. `eta=0` and `eta=1` differ on a spatial edge and both
have exact metric lifts at generic momentum. Their difference is a trace-free
electric-Weyl allocation. Nothing in the current foundation selects `eta`, a
boundary state, or the evolution of that trace-free sector.

The exact remaining target is therefore not another orientation average. It is
a sourced Levi-Civita/holonomy or equivalent connection law whose contracted
equation agrees with (10), whose trace-free part is propagated by the two
physical tensor modes, and whose reflection-positive transfer supplies a
Record tick. This result closes the algebraic construction of `C`; it does not
close that physical law.

No canonical axiom is edited. No TOE percentage moves.

## Inputs And Non-Imports

| input | used here | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | `Z^3`, translations, proper cubic rotations, fixed local Admissibility distribution, permanent additive Records | geometry, a connection, source/action identity, transfer, clock, or dynamics |
| [Block 48 reflected transfer boundary](ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | twenty-two-edge union, exact reflection map, thirteen-versus-ten fiber, common-metric response | selected common carrier, local cross-orientation action, physical transfer, or Record step |
| [Record edge-source compiler](ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | edge-labelled Records and the rank-one stress (9) | selected Record law, `beta`, physical stress, Newton coupling, or curved equation |
| [increasing-torus Ward/Green parent](ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | exact positive static source normalization and nonzero Newtonian response | all-`L`, full-`Z^3`, Lorentzian, nonlinear, or selected gravity |
| [infrared Einstein/TT parent](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | conditional Einstein tensor, four constraints, and two TT modes | physical signature, inner product, causal update, or source semantics |

The line-averaged metric map, repaired Regge carrier, Euclidean trace reversal,
and continuum curvature terminology are declared mathematical structures on
this bounded surface. They are not promoted into the foundation.

## 1. Exact Local Stencil

Let `e_t` be the positive time edge and `e_i` one spatial edge. The second
diagonal of the plaquette is the reflected class `e_i-e_t`, based one time step
forward. The complete real-space stencil is

~~~text
sqrt(2) ell_(e_i+e_t)(x)
+sqrt(2) ell_(e_i-e_t)(x+e_t)
-ell_e_i(x)-ell_e_i(x+e_t)
-ell_e_t(x)-ell_e_t(x+e_i).                                (13)
~~~

Fourier transformation of (13) gives (1). Each edge variation under a vertex
displacement `xi` is

~~~text
delta ell_v(q) = [exp(i q.v)-1] (v.xi)/|v|.                 (14)
~~~

Substitution in (13) cancels endpoint by endpoint. This proves (2) without a
gauge choice or field equation.

The reflected edge-label map includes a base shift. Applying it to (1) gives

~~~text
C_i(R_t q) Theta(q) = exp(-i q_t) C_i(q).                   (15)
~~~

The centering phase in (3) converts (15) to exact even covariance.

## 2. Constant Fiber Versus Curved Metric

At `q=0`, the common metric length of a direction `v` is

~~~text
delta ell_v = v^mu v^nu h_(mu nu)/(2|v|).                  (16)
~~~

The two diagonals in (13) cancel the four sides for every constant `h`. If the
forward and reflected orientations instead carry independent mixed-time
components, the three rows return exactly twice their differences. Combining
the seven shared-edge constraints with `C(0)` raises the paired-metric
constraint rank from seven to ten and leaves precisely one ten-dimensional
common metric.

This is the tempting hard-gluing result. Equation (5) is why it cannot be used
unchanged away from the constant fiber.

## 3. Exact Curvature Factorization

For any direction `v`, the line-average factor is

~~~text
f(v.q) = exp[i(v.q)/2] sinc[(v.q)/2].                       (17)
~~~

Only `h_ii,h_it,h_tt` enter row `i`. The `h_it` coefficient of the centered
stencil is

~~~text
sinc[(q_i+q_t)/2] - sinc[(q_i-q_t)/2]
  = -2 q_i q_t F(q_i,q_t).                                 (18)
~~~

Because (2) is exact and the line map sends the continuum displacement
variation of `h` exactly to (14), the remaining two coefficients are forced to
be `q_t^2 F` and `q_i^2 F`. This proves (5).

Expanding (6) under `(a,b)->epsilon(a,b)` gives

~~~text
F = 1/12
  - epsilon^2(a^2+b^2)/480
  + epsilon^4(a^4+b^4)/53760
  + epsilon^4 a^2 b^2/16128 + O(epsilon^6).                (19)
~~~

For `a,b` in `[-pi,pi]`, `sinc(x)` is even and strictly decreasing on
`[0,pi]`. If `ab>0`, then `|a-b|<|a+b|` and both the numerator and denominator
of (6) are positive. If `ab<0`, both reverse sign. The axis limits are positive
and (7) is their joint limit. Hence `F>0` throughout the principal zone.

## 4. Why Homogeneous Gluing Deletes The Source

On a static `x`-axis mode, (5) becomes

~~~text
D_x M_line h = F(q_x,0) q_x^2 h_tt,
D_y M_line h = D_z M_line h = 0.                           (20)
~~~

The common-metric source response has `q_x^2 h_tt -> 2`. Therefore (20) tends
to `1/6`, not zero. The runner evaluates all eight declared nonzero static
momenta. Constraining `C=0` does remove the union's fifth static null: the
restricted inertia is `(12 negative,3 positive,4 zero)`. But those four zeros
come at the price of forbidding (20).

The correct repair must replace homogeneous equality with a sourced curvature
or connection-holonomy equation. Simply deleting the three relative
coordinates is not a physical derivation.

## 5. Record Stress And The Ricci Contraction

Equation (9) is positive rank one before trace reversal. Its exact values under
(10) include

~~~text
J_(t)       =  1/4,
J_(x)       = -1/4,
J_(x+t)     =  0,
J_(x+y+z+t) = -1/4.                                       (21)
~~~

Every reflected partner has the same value. A Record history adds the values
because its stress is additive.

The conditional linearized Einstein identification relates the sum of the
three `R_itit` components to the trace-reversed temporal source. It does not
algebraically determine the individual sectional curvatures. Equation (11)
makes that residual explicit. For a spatial `x` Record,

~~~text
j^(0) = (-1/12,-1/12,-1/12),
j^(1) = ( 1/4, -1/4, -1/4),                               (22)
~~~

and both sum to `-1/4`. The `eta` term is the diagonal spatial trace-free part
of (9), so signed axis permutations carry it covariantly. At a generic
space-time momentum the three rows (4) have rank three, and both vectors in
(22) have exact finite-dimensional metric lifts.

This does not claim that every `eta` defines a complete nonlinear Einstein
law. It proves the narrower and sufficient point: a contracted Record source
plus common-metric kinematics cannot choose the trace-free sectional/electric-
Weyl content. A constraint/transfer law and boundary or state data must do so.

## 6. Law And Axiom Consequence

The three-shift algebraic target is now closed on the supplied reflected
carrier. The physical target is sharper. One extensional joint law must give:

1. a nonlinear connection or metric-holonomy version of (5);
2. the contracted Record-to-source equation extending (10);
3. propagation or boundary selection of the trace-free electric-Weyl sector;
4. lapse/shift constraint preservation and exactly two physical tensor modes;
5. a positive physical inner product or reflection-positive transfer; and
6. the Record event that defines one causal step.

These are fields of the Block-46 `L*` contract, not six new ontology axioms.
The natural constitutional location, if no downstream uniqueness theorem can
derive them, remains an extensional retyping of Admissibility to the exact
joint law referent. Adding only “the orientations share one metric,” only
`J_e`, or only a covariance adjective would leave the executed fork (11)
untouched.

No exact physical member has been selected here, so no live canonical axiom
edit is ready and no canonical axiom is edited. No TOE percentage moves. The
next discriminating target is the physical transfer/constraint law for the two
trace-free tensor modes, not another pole grid or orientation average.

## Fresh No-Go-Discipline Packet

The two scoped negatives are:

> homogeneous `C ell=0` is not compatible with the supplied nonzero static
> source response; and the contracted Record source does not select the three
> sectional components on the displayed covariant decoder family.

They are not a gravity no-go.

### N1 — Alternative Routes

| route | status | result |
|---|---|---|
| homogeneous orientation equality | attempted | removes the three constant relative modes but also the Newtonian curvature; rejected as the physical finite-momentum law |
| sourced Levi-Civita/holonomy equation | live and promoted | can replace zero by curvature while retaining one common metric |
| canonical constraint evolution | live | can determine lapse/shift and propagate the two trace-free tensor modes |
| reflection-positive transfer | live | can supply the physical Hilbert space, branch, and step without hard-zero gluing |
| independent connection/Palatini law | live | may realize the plaquette curvature through holonomy rather than metric line averages |
| nonlinear nonflat phase | live | can change the linear carrier while retaining the local stencil as its tangent |
| downstream uniqueness theorem | live | could select one exact member without changing the axioms |
| exact extensional Admissibility referent | governance route | sufficient only after an actual complete law is supplied |

### N2 — Wall Independence

The result separates four walls:

~~~text
W1 = common-carrier kinematics,
W2 = contracted Record/source identification,
W3 = trace-free connection/constraint propagation,
W4 = positive transfer and causal Record step.                       (23)
~~~

`C(0)` closes `W1` only on the constant fiber. Equation (10) supplies one
conditional contraction in `W2`. The `eta` family proves that `W2` does not
close `W3`. Real sampled poles do not close `W4`. None is counted as another.

### N3 — Hidden-Wall Scan

The twenty-two-edge union, time reflection, line-average metric map, flat
background, Regge response, rank-one Euclidean stress, trace reversal, and
Einstein terminology are supplied conditional structures. The calculation
does not import a physical Newton constant, source sign, action unit, `beta`,
connection, nonlinear completion, state, boundary condition, Hilbert norm,
transfer, or Record clock.

### N4 — Residual Matching

The constant-fiber claim is checked on the exact paired metric maps and three
relative `h_it` columns. The curvature claim is checked against the complete
line-average map, not a midpoint approximation. The source incompatibility is
checked on the same common-metric static response that retains the parent
Green residue. The nonselection claim uses two explicit decoders with equal
contraction, exact cubic covariance, and distinct generic metric lifts.

### N5 — Resolution And Scope Certificate

The primary cache resolves all twenty-two edge labels, all three local
space-time parallelograms, all four displacement columns, all ten common metric
coordinates, all three relative mixed-time coordinates, eight nonzero static
momenta, every one of the twenty-two Record rays, all twenty-four proper cubic
rotations, and two explicit members of the continuous `eta` family. It does
not resolve a nonlinear lattice, an infinite-volume state, or a causal update.

### N6 — Partial-Closure Paths

Positive content survives and advances: the requested exact three-component
intertwiner is constructed; it gives the correct ten-dimensional common fiber;
its complete finite-momentum meaning is identified as curvature; the Record
stress has an exact contracted source; and the physical failure of hard zero
points directly to a sourced connection law. None of the connection,
canonical, transfer, or nonlinear routes is excluded.

### N7 — Steelman

The strongest opposing interpretation is that a complete canonical Einstein
law never needs three separately source-assigned equations: the source fixes
constraints, while initial data and the TT Hamiltonian propagate Weyl
curvature. That interpretation defeats any claim that the `eta` family is a
fatal ambiguity. It reinforces the actual conclusion: the missing object is
the canonical/transfer evolution and its state, not another algebraic source
projection.

### N8 — Cross-Cycle Echo

Block 43 already showed the static Ward/Green seam works, so its nonzero
response is used as a destructive control rather than re-proved as a new
gravity claim. Block 46 already separated source, clock, constraint, and
Record controls; the `eta` family refines its source/constraint interface.
Block 48 named the three-shift intertwiner; this block constructs it and shows
why silent deletion is wrong. Earlier connection blocks remain method
precedents only and are not treated as evidence for this Regge identity.

**Status: PASS.** The two narrow negatives survive N1-N8; every broad gravity
negative is rejected, and the sourced connection/physical-transfer route is
promoted.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py
~~~

The expected final line is

~~~text
TOTAL: PASS=13 FAIL=0
~~~

The cache also prints the required per-element, per-site, per-mode, per-block,
and lattice-wide scope certificate.

## Conclusion

The orientation-shift problem is no longer an unnamed gluing defect. Its exact
local operator is the reflected plaquette curvature intertwiner (1). It
identifies the two orientation metrics at constant zero curvature, but at
finite momentum it measures physical sectional curvature with a positive
form factor. Homogeneous gluing would therefore erase the Newtonian source.

The Record edge stress fixes a contracted Ricci source, while the trace-free
electric-Weyl sector remains a dynamical/state question. The highest-leverage
next step is consequently a constrained reflection-positive two-TT transfer
whose nonlinear tangent realizes (5), preserves the source contraction, and
defines the Record tick.

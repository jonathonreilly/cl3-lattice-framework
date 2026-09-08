---
claim_id: admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On the supplied periodic four-dimensional Kuhn/Coxeter edge carrier, the equal-positive-weight sum of one closed axial tick line and one disjoint closed tick-space face-diagonal line is an exact positive two-stream source. Each line separately telescopes against the actual vertex-gauge row, so the combined Ward identity is exact on every Fourier mode. On their common principal support, the per-step metric source is t tensor t plus v tensor v divided by sqrt(2). Its time-column has beta=sqrt(2)-1 and strictly positive Lorentz norm under the declared naive Lorentzian diagnostic, while the positive x-t determinant proves that it is a two-stream mixture rather than one rank-one massive worldline. Across all 8,755 modes of L=3 through L=8 four-tori, the fixed-global source has 2,369 supported nonzero modes, including 1,088 with nonzero tick frequency; every supported nonzero mode has five Regge null directions, full-null compatibility, and a direct unprojected edge solve. Four shared-transverse directions give the source-derived unprojected limit |k|^2 q^T h q ->4. At compact k=0, the strictly positive flat edge-length vector ell=M(0)(2I) lies in ker Q(0), so ell dot s>0 exactly excludes every nonzero nonnegative actual-edge source from Range Q(0). This is a bounded bare-quadratic compact-source boundary, not a universal no-go: fixed-global, open, sign-indefinite combined-geometry, curved, nonlinear, alternate-carrier, and selected constraint routes remain live. No physical source selection, single massive worldline, Lorentzian dynamics, coupling, nonlinear completion, realized history, axiom adoption, or universal carrier theorem is proved."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_2026_08_10.py
---

# Positive Two-Stream Timelike Mean And Dilation Zero-Mode Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** positive multi-line history construction, timelike mean-current
diagnostic, and exact compact-source boundary
**Scope:** the supplied flat periodic four-dimensional Kuhn/Coxeter edge
carrier, equal positive tick and face-diagonal line coefficients, and the named
`L=3,...,8` four-tori.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_2026_08_10.py](../scripts/admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_2026_08_10.py)

## Result Up Front

[Block 14](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
constructed one closed tick-space face-diagonal line. It was positive and
solvable after fixing the compact global mode, but its tangent was null under
a naive Lorentzian reading. Its compact completion used a signed transverse
partner and therefore was not a positive-mass ensemble.

This block adds the smallest positive stream that changes the mean current:
one disjoint axial tick line. Let

    t=(0,0,0,1),       v=(1,0,0,1),       b=(0,1,0,0).       (1)

Using the complete closed-line action from Block 14, define

    A_+[g]=A_v,0[g]+A_t,b[g].                               (2)

Both coefficients in (2) are `+1`; each underlying edge-length term retains
the inherited coefficient two. The two lines are disjoint for every declared
torus. Their Fourier source is

    s_+(k)=2 F_L(k dot v)e_v
           +2 exp(i k dot b)F_L(k dot t)e_t.                 (3)

Each summand separately satisfies

    F_L(theta)(exp(i theta)-1)=0.                            (4)

Therefore (3) annihilates all four vertex-gauge directions on every torus
mode. This is a positive sum of two closed histories, not a kinked path. A
kinked tick/diagonal staircase would leave an unbalanced tangent force at each
corner and is not substituted for (4).

On common principal support `k_tau=0` and `k_x=0`, divide each line by its
length-`L` structure factor. The per-step metric source is

    T_+=t tensor t+(v tensor v)/sqrt(2).                     (5)

Its time-column is

    j=(1/sqrt(2),0,0,1+1/sqrt(2)).                           (6)

Thus the energy-current ratio and Lorentz norm are

    beta=j_x/j_tau=sqrt(2)-1,
    j_tau^2-j_x^2=1+sqrt(2)>0.                               (7)

Equation (7) is an exact effectively subluminal timelike **mean-current
diagnostic**. It does not turn the two lines into one particle. Indeed the
`x,t` block of (5) has determinant `1/sqrt(2)>0`, whereas one rank-one dust
row would have determinant zero. The result is a positive two-stream mixture,
not a derived massive worldline.

Across all `8,755` modes on `L=3,...,8`, the fixed-global version of (3) has
`2,369` supported nonzero sources, including `1,088` with nonzero tick
frequency. Every one meets a five-dimensional Regge zero space, annihilates
that complete space, and solves the actual edge equation directly without
source projection.

The bare compact zero mode has an exact obstruction stronger than the earlier
single-fixture residual. Let

    ell_d=|d|,       d in {0,1}^4 minus {0}.                  (8)

The vector `ell` is strictly positive and is the line-averaged uniform metric
dilation,

    ell=M(0)(2I),       Q(0)ell=0.                           (9)

For every nonzero actual-edge source `s>=0`,

    ell dot s>0.                                             (10)

Since a source in `Range Q(0)` must be orthogonal to every vector in
`ker Q(0)`, (9)--(10) prove

    s>=0 and s!=0  implies  s not in Range Q(0).              (11)

For the concrete `L=5` mixture,

    ell dot s_+(0)=10(1+sqrt(2))>0.                          (12)

This is an exact cone-separation statement for the flat compact quadratic
carrier. It does not forbid fixing the global mode, using open boundaries,
adding a sign-indefinite geometry or constraint contribution, moving to a
curved/nonlinear equation, or changing the carrier.

## 1. Source-Bound Inputs

The scientific inputs are repository-local:

1. the [current four axioms](MINIMAL_AXIOMS_2026-06-29.md), used only to state
   what they do not select;
2. the [equal-form tick primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
   used only for the inherited tick normalization;
3. Block 14, which supplies the exact closed tick and face-diagonal line
   actions and their actual-edge Ward identity;
4. [Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
   which supplies the existing candidate history/action and infrared wording;
   and
5. the [actual cubic-Coxeter Regge Hessian](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md).

No observed constant, Einstein equation, target stress tensor, fitted speed,
mass value, coupling, or probability law is imported. The value in (7) is
derived from the actual source tensor (5). The response target below is
derived from the source and the already measured `-1/2` Einstein comparator,
not inserted as an observational target.

## 2. Positive Closed Two-Stream Action

For anchor `a` and actual edge direction `d`, Block 14 defines

    A_d,a[g]=2 sum_(n=0)^(L-1)(ell_d(a+nd;g)-|d|).            (13)

The face-diagonal line at `y=0` and the tick line at `y=1` each have `L`
vertices, close after `L` edges, and are disjoint for `L>=3`. Equation (2) is
a sum of their complete actions with no negative coefficient.

The distinction from a bent single path is load-bearing. At a bend, the
incoming and outgoing unit tangents differ. The variation of total length
therefore leaves their difference as a vertex force. Each stream in (2) is
straight and closed, so its incoming and outgoing tangent agree at every
vertex and its full Fourier line factor telescopes. Positivity is gained by a
second conserved stream, not by hiding a corner force.

The source support is the union

    k dot v=0 mod 2pi       or       k dot t=0 mod 2pi.       (14)

The two summands may overlap, but linearity preserves full-null compatibility
there because each complete line is compatible on its own support.

## 3. Timelike Mean-Current Diagnostic

For one coefficient-two actual edge, the metric derivative is

    2 e_d M(k)=(d tensor d)/|d|                              (15)

on principal support. Applying (15) to `t` and `v` gives (5). Its nonzero
`x,t` entries are

    T_xx=1/sqrt(2),
    T_xt=1/sqrt(2),
    T_tt=1+1/sqrt(2).                                       (16)

The off-diagonal coordinate derivative is twice the physical tensor entry;
the runner performs that conversion explicitly before evaluating (16).
Equations (6)--(7) then follow without a fitted stream weight.

This diagnostic is deliberately narrow:

- it uses the time-column of the Euclidean source tensor under a naive
  Lorentzian sign reading;
- it proves a timelike **mean current**, not a timelike tangent for either
  constituent line;
- the face-diagonal constituent remains null under that reading;
- the positive determinant shows that the combined source is not rank one;
  and
- no causal update or physical velocity observable is selected.

The result nevertheless retires the narrower claim that positive actual-edge
support on this carrier forces every aggregate current to remain lightlike.

## 4. Complete Nonzero-Mode Inventory

For centered Fourier indices, the face-diagonal stream is supported when
`m_x+m_tau=0 mod L`; the tick stream is supported when `m_tau=0 mod L`.
Removing their shared compact zero mode gives:

| `L` | supported nonzero sources | nonzero-`k_tau` sources |
|---:|---:|---:|
| 3 | 44 | 18 |
| 4 | 111 | 48 |
| 5 | 224 | 100 |
| 6 | 395 | 180 |
| 7 | 636 | 294 |
| 8 | 959 | 448 |
| **total** | **2,369** | **1,088** |

For every supported nonzero source, the runner rebuilds the actual `15 x 15`
Regge Hessian, diagonalizes it, checks five zero directions, contracts against
the complete zero space, and solves the unprojected edge equation. It does not
infer compatibility from the four gauge columns alone.

This fixed-global result is positive: no source coefficient is subtracted.
The price is explicit removal of the compact constant geometry variation.
Current axioms do not select that constraint.

## 5. Shared-Transverse Unprojected Pole

Let

    q=(sqrt(2)-1,0,0,1).                                    (17)

On the shared principal support, choose momentum in the `y,z` plane. Then
`k dot q=0`, so `q^T h q` is invariant under the continuum gauge shift
`h -> h+k tensor xi+xi tensor k`. The source-derived `-1/2` Einstein
comparator gives exactly

    |k|^2 q^T h_cont q=4.                                   (18)

Solving the actual metric-sector Regge equation with the unprojected source
`2(e_t+e_v)` gives, in four shared-transverse directions,

    |k|^2 q^T h(k) q ->4.                                   (19)

Halving momentum improves every error. Equation (19) is a common-support
long-wave slice of a two-stream source. It is not assigned a one-worldline
Green function, because the two constituent lines have different tangent
spaces.

## 6. Exact Compact Dilation Boundary

At `k=0`, the actual Regge Hessian is Hermitian and every constant metric
perturbation is a zero mode. The uniform perturbation `h=2I` maps to (8), so
(9) is exact on the source-bound carrier.

If `s=Q(0)x`, Hermiticity gives

    ell dot s=ell^T Q(0)x=(Q(0)ell)^T x=0.                  (20)

But every component of `ell` is strictly positive. Hence every nonzero vector
with nonnegative actual-edge components has `ell dot s>0`, contradicting
(20). This proves (11) for the whole nonnegative actual-edge cone, not only
for (2).

The theorem is bounded in four ways:

1. it concerns the flat quadratic `Q(0)` equation;
2. it concerns sources expressed as nonnegative actual edge-length rows;
3. it retains the compact constant variation in the operator domain; and
4. it does not include an independently varied geometry/constraint source.

A fixed-global domain removes the separator from the equation. Open boundary
conditions remove the normalizable compact mode. A sign-indefinite combined
geometry contribution can cancel the dilation pairing. Curvature, nonlinear
terms, an alternate triangulation, or a different source carrier can change
the operator or cone. None is ruled out.

## 7. What This Does And Does Not Close

The construction closes three bounded mathematical questions:

1. a nonnegative actual-edge history ensemble can have an exactly subluminal
   timelike mean current while preserving the exact Ward identity;
2. on the fixed-global domain, that positive source is full-null compatible
   and directly solvable on every one of its `2,369` supported nonzero modes;
   and
3. on the bare compact flat quadratic carrier, no nonzero nonnegative
   actual-edge source can solve the retained `k=0` equation.

It does not close:

- one connected rank-one massive worldline;
- physical selection of either stream, their equal weights, or the action;
- a positive compact solution with the constant geometry mode retained;
- a derived constraint or sign-indefinite geometry counter-source;
- Lorentzian causal dynamics, geometry evolution, coupling sign or size;
- nonlinear or projective completion;
- a Born functional, trial/history law, or one realized history.

## 8. Exact Axiom Consequence

No broader candidate wording is needed. The existing candidate **Geometry-
indexed history/action amendment** already permits, if adopted, a fixed local
history/action representative and a fixed-global, open, background-subtracted,
or constrained infrared ensemble. It can therefore type (2) on the
fixed-global route.

The compact theorem adds one exact requirement for any positive bare-periodic
completion: it must change at least one of the four bounded conditions in
Section 6. This is a consequence map, not proposed canonical wording.

The existing candidate remains unadopted, not proved necessary, and not
proved minimal. A downstream model can declare (2), the fixed-global domain,
and the actual Regge carrier without editing the four axioms. Foundation-level
autonomy still requires selection of the physical action representative,
source/Record map, constraint or geometry dynamics, coupling, Lorentzian
regime, nonlinear completion, and realized member. No canonical axiom is
edited here.

## 9. TOE Lane Consequence

| Lane | Exact Block-15 advance | Still open |
|---|---|---|
| operational quantum / records | two positive prescribed Record-defect streams fit the existing site carrier conditionally | physical defect/Record typing, action selection, and occurrence |
| causal time | the aggregate current has exact `beta=sqrt(2)-1` under the stated diagnostic and every dynamic source obeys the Ward identity | one connected timelike worldline, causal update, history law, and realized member |
| inertia / matter | the source is nonnegative and its mean current is timelike | physical mass, rank-one massive dust, dressed inertia, and action unit |
| gravity / source / resources | 2,369 positive fixed-global unprojected sources and an exact compact dilation separator | selected constraint or counter-source, geometry dynamics, sign/coupling, Lorentzian and nonlinear law |
| Born probability / realized history | the construction does not assume a Born functional | program/effect selection, probability law, trials, and one realized history |

This is bounded support on an open stack. It advances positivity and effective
timelikeness but proves that the same actual-edge cone cannot also close the
unconstrained compact zero mode on the fixed quadratic carrier. The fixed TOE
percentages remain unchanged.

## No-Go Discipline Gate

The positive construction contains one negative theorem: the compact dilation
separator. The following N1--N8 packet prevents that theorem from becoming a
universal source, gravity, or axiom no-go.

### N1 — alternative route enumeration

| Route family | Attempt and scoped outcome | Marker |
|---|---|---|
| positive two-stream fixed-global source | equation (2), with only the compact constant geometry variation removed | executed: 2,369 full-null-compatible unprojected nonzero-mode solves |
| signed compact neutralization | Block 14 transverse difference | executed: cancels `k=0`, but is not a nonnegative source |
| open boundary | Block 13/14 transverse Green problem | executed conditional route: no normalizable compact zero mode |
| sign-indefinite combined geometry/constraint source | add an independently derived contribution whose dilation pairing cancels (10) | not executed; live because it changes the nonnegative source-cone premise |
| curved or nonlinear equation | change the flat quadratic `Q(0)` equation | not executed; live and outside (11) |
| alternate carrier/triangulation | change the actual edge map or compact null space | not executed; live and outside the source-bound theorem |
| connected balanced junction | construct one positive multi-edge network with local force balance and a rank-one timelike effective source | not executed; (2) is two streams, not this object |

The executed fixed-global route defeats any all-mode or all-positive-source
no-go. The unexecuted routes change the exact premise used by (11), so they
cannot be counted as failed.

### N2 — wall independence

Define `W1` history/action selection, `W2` Ward/full-null closure, `W3`
positive source weights, `W4` compact zero-mode compatibility, and `W5` one
rank-one timelike physical worldline.

| Pair | Independence witness |
|---|---|
| `W1,W2` | (2) closes `W2` while remaining prescribed, so it does not close `W1`. |
| `W1,W3` | positive coefficients can be supplied without being selected. |
| `W1,W4` | selecting a local action does not choose or solve a global constraint. |
| `W1,W5` | selecting a two-stream law would not make it one worldline. |
| `W2,W3` | Block 14's signed pair closes `W2` without `W3`; (2) closes both. |
| `W2,W4` | (2) closes `W2` on every mode but fails the retained compact equation. |
| `W2,W5` | exact Ward closure holds for the two-stream mixture without rank-one dust. |
| `W3,W4` | the dilation theorem proves that positivity alone conflicts with this compact equation. |
| `W3,W5` | positive mixtures need not be rank one; the determinant in Section 3 is nonzero. |
| `W4,W5` | a sign-indefinite compact counter-source could close `W4` without producing a physical worldline. |

No wall is silently merged into another.

### N3 — hidden-condition scan

The source was searched for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| `background-subtracted` | cited Block-14 route; explicit signed condition, not used by the positive theorem |
| `canonical axiom` | governance boundary only |
| all other scan phrases | absent outside the quoted checklist itself |

Equal positive coefficients, disjoint anchors, Euclidean signature, fixed-
global domain, naive Lorentzian diagnostic, flat quadratic carrier, and named
sizes are explicit. No hidden physical identification is used.

### N4 — residual matching

| Cited witness | Witness residual | Present result | Match? |
|---|---|---|---|
| Block 14 Sections 2--6 | positive helix is null under the diagnostic and fails compact `k=0` | add a positive tick stream, derive timelike mean, and classify the full positive compact cone | yes |
| Regge note mode inventory | constant metric perturbations lie in `ker Q(0)` | identify the positive uniform dilation `ell=M(0)(2I)` and pair it with the source | yes |
| Block 12 candidate | fixed-global/open/signed/constraint ensembles remain explicit choices | retain the fixed-global route and leave selection open | yes |

No projected source, target stress tensor, or inserted Einstein equation is
used as evidence for the actual edge solves.

### N5 — rhetoric audit

| Resolution | Executed statement | Scope not claimed |
|---|---|---|
| per element | positive tick and face-diagonal edge rows, metric tensor, dilation vector | no arbitrary source carrier |
| per site | two disjoint separately closed lines | no connected particle path or junction dynamics |
| per mode | all 2,369 supported nonzero mixture sources plus the exact compact separator | no arbitrary-size or continuous-Brillouin theorem |
| per block | timelike mean diagnostic, fixed-global solves, and compact cone boundary | no selected coupled nonlinear theory |
| lattice wide | all 8,755 modes on the six named four-tori | no universal compact-source classification |

“Timelike” modifies the declared mean-current diagnostic, not either
constituent trajectory or a physical massive particle.

### N6 — partial-closure paths

| Candidate path | Status | What it closes |
|---|---|---|
| positive two-stream fixed-global action, this note | executed bounded construction | positivity, timelike mean, Ward/full-null compatibility, and nonzero-mode response |
| signed pair, Block 14 | executed compact route | compact cancellation without positivity |
| open boundary, Blocks 13--14 | executed conditional route | noncompact response without a finite zero-mode equation |
| sign-indefinite combined geometry/constraint source | live | could cancel the dilation pairing if derived and selected |
| curved/nonlinear or alternate carrier | live | can change the zero-mode null space or source cone |
| connected balanced junction | live | could replace the mixture by one locally joined history |
| existing history/action amendment | unadopted sufficient wording | types the representative and ensemble, not their derivation |

These paths forbid “new axiom required” and universal compact-source readings.

### N7 — steelman

A hostile reviewer should accept the exact positive result but reject a
particle interpretation. The two lines are separately conserved streams; the
positive `x,t` determinant proves they are not one rank-one dust row. The
reviewer should also accept (11) only on the bare compact flat quadratic edge-
source equation. Fixing the global mode already yields 2,369 positive solves,
and a derived sign-indefinite geometry contribution, curved background,
nonlinear completion, or alternate carrier lies outside the separator's
premises. This steelman is adopted.

### N8 — cross-cycle echo

| Prior wall | Later mechanism / lesson here |
|---|---|
| Block 12 localized affine-bag residual | Block 13 found a source-representative improvement; fixed-carrier residuals do not license universal wording. |
| Block 13 fixed vertical row | Block 14 replaced it by a complete closed line; support completion can retire a Ward failure. |
| Block 14 signed compact pair | this block replaces the negative partner by a positive tick stream but exposes the exact dilation wall; closing positivity need not close compactness. |
| Block 10 fixed-background source nonuniqueness | Block 11 supplied a geometry family; a combined geometry source remains a concrete live mechanism. |

The campaign history repeatedly shows that explicit representatives, support
completion, and changed domains can retire a narrow wall. They remain live.

**Gate status:** PASS for the positive two-stream fixed-global theorem,
timelike mean-current diagnostic, full nonzero-mode inventory, and exact bare-
compact dilation boundary. FAIL for any single-particle, universal compact-
source, gravity, dynamics, or “new axiom required” reading.

## 11. Verification

Run:

    python3 scripts/admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_2026_08_10.py

The runner checks:

- source boundaries in the axioms, Block 14, the existing candidate, the tick
  primitive, and the actual Regge theorem;
- closed-line combinatorics, disjointness, positive coefficients, direct
  Fourier equality, and the exact two-telescope Ward identity;
- the exact metric tensor, `beta=sqrt(2)-1`, positive Lorentz norm, and
  non-rank-one determinant;
- all `8,755` torus modes, `2,369` supported nonzero sources, and `1,088`
  nonzero-tick-frequency sources;
- complete five-null overlap and direct unprojected solve residuals;
- the exact dilation-vector metric identity, zero-mode relation, positive-cone
  separator, and concrete `L=5` compact control;
- the source-derived continuum coefficient and four-direction unprojected
  `|k|^2 q^T h q ->4` limit; and
- N1--N8, boundary, canonical-nonmutation, and five-resolution surfaces.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    exact Block-13 static tick edge
      -> Block-14 positive closed face-diagonal line
      -> add one disjoint positive closed tick line
      -> exact two-stream Ward identity
      -> beta=sqrt(2)-1 timelike mean-current diagnostic
      -> 2,369 full-null-compatible fixed-global unprojected solves
      -> shared-transverse unprojected coefficient four
      -> exact positive-dilation compact separator.

This constructs a positive effectively subluminal aggregate source and proves
the exact reason the same nonnegative actual-edge cone cannot solve the bare
compact zero mode on the fixed flat quadratic carrier. It does not derive one
massive worldline, a selected constraint or counter-source, physical action,
geometry dynamics, coupling, nonlinear field equation, Born functional, or
realized history. No canonical axiom is edited. No universal compact-source
no-go is claimed. The fixed TOE percentages remain unchanged.

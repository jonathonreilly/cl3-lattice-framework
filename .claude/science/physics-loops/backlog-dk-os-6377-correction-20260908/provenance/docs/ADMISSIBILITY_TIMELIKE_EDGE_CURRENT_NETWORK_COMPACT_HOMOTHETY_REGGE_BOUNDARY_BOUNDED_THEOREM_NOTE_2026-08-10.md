---
claim_id: admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On the supplied flat periodic four-dimensional Kuhn/Coxeter edge carrier, one connected positive tick-plus-face-diagonal bouquet admits a coarse timelike piecewise-causal routing under the stated naive Lorentzian diagnostic and is directly solvable without source projection on all 2,369 supported nonzero Fourier modes of the L=3 through L=8 four-tori. Separately, two nonnegative spatial-permutation-symmetric temporal edge bundles have the exact common tangent current J_A=J_B=(2,2,2,6); all 504 spatially uniform binary histories made from them are locally balanced, and all 2,768 supported nonzero history-mode contrasts annihilate the complete five-dimensional Regge null space and solve the actual edge equation. Their contrast has a pure spatial-shear metric row and an unprojected 1/omega^2 response. At compact zero momentum the constant-metric homothety z=M(0)I has components z_d=|d|/2>0 and Q_R(0)z=0, so every nonzero componentwise-nonnegative edge-length source has z dot s>0 and is outside image Q_R(0). This is an exact separator for the unmodified flat compact quadratic carrier, not a positive-mass, causal-particle, nonlinear-gravity, alternate-carrier, open-boundary, constrained-ensemble, or universal gravity no-go. The bundle family includes spacelike primitive edges under the naive Lorentzian diagnostic; the bouquet source is a rank-two stream sum rather than a rank-one massive-particle stress tensor; action selection, Record/source identity, compact ensemble, geometry dynamics, coupling, Lorentzian continuation, Born law, and realized history remain open."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - realized_state_primitive
  - admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py
---

# Timelike Edge-Current Networks, Compact Homothety Separator, And Regge Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** positive balanced-network construction, exact compact scale-mode
separator, and axiom-obligation localization
**Scope:** the supplied flat periodic four-dimensional Kuhn/Coxeter edge
carrier, the named network families, and the complete `L=3,...,8` finite
inventories stated below.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py](../scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py)

## Result Up Front

[Block 14](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
gave an exact closed-line Ward identity, signed compact neutralization, and
positive fixed-global-mode line. [Block 15](ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
then supplied a disjoint positive two-stream source and the compact dilation
separator. Two sharper questions remained:

1. can positive actual-edge histories be joined into a balanced network whose
   coarse current is strictly timelike rather than the null face-diagonal
   current; and
2. is the remaining positive compact zero-mode failure an accident of those
   examples, or an exact property of the current flat quadratic carrier?

This note answers both, with different answers.

First, let

    t=(0,0,0,1),       f=(1,0,0,1),       u=t+f=(1,0,0,2).   (1)

On every declared four-torus, the positive closed `t` line and positive closed
`f` line share exactly one vertex. Their union is a connected two-loop bouquet.
If an identity label exchanges branches at that vertex, the lifted displacement
per paired winding, divided by `L`, is `u`. Under the diagnostic Lorentzian form
`u_tau^2-|u_space|^2`,

    beta_u=1/2,        u_tau^2-|u_space|^2=3.                (2)

The aggregate unit-tangent current is also timelike:

    J_bouquet=t+f/sqrt(2),
    |J_space|/J_tau=sqrt(2)-1.                               (3)

The actual source, however, is the sum of two edge-length derivatives. It is a
rank-two stream sum, not the rank-one tensor `u u/|u|`. It is not a rank-one
massive-particle stress tensor, and the current axioms do not select the
identity exchange at the shared vertex.

Across all `8,755` Fourier modes on the `L=3,...,8` four-tori, the bouquet has
`2,369` supported nonzero sources. Of these, `1,088` have nonzero tick
frequency and `193` have both line structure factors nonzero. Every supported
nonzero source annihilates all five null directions of the actual `15 x 15`
Regge edge Hessian and solves the unprojected edge equation directly. Three
common-transverse long-wave directions give a source-contracted pole with
coefficient tending to six.

Second, there is a different balanced network. Among the eight actual
future-temporal positive-coordinate edges `d=(d_x,d_y,d_z,1)`, define two
nonnegative rows by spatial Hamming weight `r=d_x+d_y+d_z`:

    A_d = 2 sqrt(2)  for r=1,       A_d=0 otherwise,
    B_d = 3          for r=0,
          sqrt(3)    for r=2,       B_d=0 otherwise.          (4)

These rows are invariant under permutations of the three spatial coordinates
inside this positive-coordinate edge inventory. They are not claimed to be
invariant under the full signed proper-cubic group. With

    J(w)=sum_d w_d d/|d|,                                      (5)

direct summation gives the exact identity

    J_A=J_B=(2,2,2,6).                                        (6)

Thus `|J_space|/J_tau=1/sqrt(3)` and the diagnostic Lorentzian norm squared is
`24`. Any spatially uniform binary sequence of `A` and `B` bundles has exact
incoming-outgoing current balance at every site. Exhausting every binary
history of lengths three through eight gives `504` histories, `492`
nonconstant histories, and `2,768` supported nonzero history-mode pairs. Every
supported pair is compatible with the complete five-dimensional Regge null
space and solves without source projection. The bundle contrast

    c=A-B=(-3, 2 sqrt(2), -sqrt(3), 0) by r=0,1,2,3            (7)

maps at pure tick momentum to equal `xy`, `xz`, and `yz` spatial shear and no
lapse, shift, or diagonal source. Its unprojected response has
`omega^2 c dot h` tending to six.

The binary construction is mathematical, not yet a causal matter model. The
`r=2` edges in `B` are spacelike under the naive Lorentzian diagnostic. The
fact that their aggregate current is timelike does not make every constituent
edge causal.

Finally, the compact zero mode has an exact separator. Let `M(0)` be the
actual zero-momentum edge-to-metric map and let `I` denote the constant
identity metric perturbation. Then

    z=M(0) I,             z_d=|d|/2>0                         (8)

for every one of the fifteen edge classes. Constant metric perturbations are
exact flat zero modes of the supplied Regge Hessian, so

    Q_R(0) z=0.                                                (9)

Because `Q_R(0)` is Hermitian, every source in its image is orthogonal to `z`.
For any edge-length source `s` with `s_d>=0` for every class and `s!=0`,

    z dot s = sum_d (|d|/2) s_d > 0.                          (10)

Therefore

    {s>=0, s!=0} intersection image Q_R(0) = empty.           (11)

Equation (11) is an exact convex-cone separation theorem. It proves that no
positive rearrangement, balanced junction, or positive reweighting of the
current edge-length sources can solve the unmodified compact zero-mode
equation on this flat quadratic carrier. It does not constrain signed
counterstress, a fixed scale mode, an open boundary, curved-background
equations, a lifted operator, or a different source carrier. No universal
gravity no-go follows.

## Exact Target Contract And Obligation Graph

**Target statement.** Construct a nonnegative actual-edge network with a
strictly timelike coarse or aggregate current and prove its unprojected
nonzero-mode compatibility with the supplied Regge Hessian; then decide,
without extrapolating beyond the same carrier, whether positive network
rearrangement can solve its bare compact zero mode.

**Quantifiers and domain.** The positive-cone statement quantifies over every
nonzero componentwise-nonnegative vector in the fifteen zero-momentum
edge-length source coordinates. The constructive finite statements quantify
over every mode and history explicitly counted on `L=3,...,8` four-tori.

**Allowed premises.** Finite real/complex linear algebra, the source-bound
Regge Hessian and metric map, actual closed edge rows from Blocks 14--15, the
approved tick-graining primitive, exact finite Fourier sums, and the explicit
network definitions in this note.

**Forbidden weakenings.** Source projection, deletion of failed modes from a
reported inventory, fitted response normalization, identification of an
aggregate current with a rank-one particle tensor, silent removal of `k=0`,
silent signed counterstress, or use of an unadopted candidate amendment as
current authority.

**Required boundary cases.** The compact mean of every binary history, the
positive bouquet at `k=0`, constituent causality, equal-coefficient junction
rigidity, one signed composite chord, fixed/open/background alternatives, and
the distinction between finite nonzero modes and arbitrary lattices.

**Completion witnesses.** Equations (6), (11), (14), (18), (20), and (21), the
complete two finite inventories, the independent SVD/lstsq reconstruction,
and the primary runner's zero-failure output.

**Outcomes that do not count as closure.** A timelike vector label without an
edge source, a gauge-only test without the fifth null direction, a projected
solve, a signed compact pair described as positive mass, a prescribed support
described as dynamics, or an axiom proposal described as adopted.

The proof-obligation graph is acyclic:

| Obligation | Status | Evidence |
|---|---|---|
| actual edge inventory and source row | cited and recomputed | Blocks 14--15 plus runner source-binding and inventory checks |
| exact bouquet Ward identity | proved here | linear sum of the two closed-line telescopes in (14) |
| coarse/aggregate timelike diagnostics | proved here | equations (2), (3), and (6) |
| complete nonzero-mode compatibility | exhaustive finite certificate | `2,369` bouquet sources and `2,768` history-mode pairs |
| equal bundle current | proved here exactly | equations (16)--(18) |
| compact positive homothety vector | cited carrier property plus proved map | equations (8)--(10) and the Regge constant-metric zero theorem |
| positive-cone separation | proved here | Hermitian image/kernel orthogonality in (29) |
| alternate-route and scope audit | proved as a boundary packet | N1--N8 below |
| physical source/history/geometry selection | open | Section 8; not used by the bounded theorem |

The strongest missing lemma for physical closure is not another finite-mode
compatibility calculation. It is a selected combined Record-history/geometry
law whose positive causal source, compact scale mechanism, action unit,
coupling, and Lorentzian/nonlinear equations arise from one approved physical
specification. That obligation is stronger than this block's target and is not
renamed as a routine continuation.

## 1. Source-Bound Inputs

The scientific inputs are repository-local:

1. the [current four axioms](MINIMAL_AXIOMS_2026-06-29.md), used only to bound
   what they select;
2. the [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
   used only for the equal-form tick normalization;
3. the [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md),
   used only to preserve the distinction between pointwise evaluation and a
   history-selection law;
4. [Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
   which records the existing candidate history/action and zero-mode-ensemble
   wording;
5. Block 14, which supplies the actual closed-line row and finite null-space
   machinery;
6. [Block 15](ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
   which supplies the disjoint positive two-stream source, its complete
   nonzero-mode inventory, and the first exact compact dilation separator; and
7. the [actual Regge Hessian](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md),
   including its Hermiticity and exact constant-metric zero modes.

No observed constant, Einstein equation, fitted coupling, continuum stress
tensor, Born formula, physical source sign, action selector, or realized
history is imported. The network weights in (4) are solved from the current
matching equation; they are not empirical fits.

The primitive-registry check was applied. The kinetic-isotropy and
realized-state primitives are approved premise nodes, not bounded walls. Their
grants are not enlarged: neither supplies dynamics, a source/action map,
geometry, a probability rule, a state, or a selection rule.

## 2. The Connected Positive Bouquet

For an actual edge direction `v`, Block 14 defines

    A_v[g]=2 sum_(n=0)^(L-1) (ell_v(nv;g)-|v|),
    s_v(k)=2 F_L(k dot v) e_v,                                (12)

where `F_L(theta)=sum_n exp(i n theta)`. Take

    A_bouquet=A_t+A_f.                                        (13)

For `L=3,...,8`, the vertex sets of the two cycles intersect only at the
origin. Hence (13) is connected and every real-space coefficient is positive.
Each cycle separately satisfies the exact telescoping Ward identity

    F_L(k dot v)(exp(i k dot v)-1)=0.                         (14)

Their sum therefore does too.

The source does not encode how an object identity passes through the shared
vertex. Straight routing leaves a timelike tick loop and a null face loop.
Exchange routing gives one `2L`-edge piecewise-causal loop with lifted average
displacement proportional to `u` in (1). Both routings have the same
unlabeled edge source. Selecting one is a Record/history identity obligation,
not an implication of (13).

The complete finite inventory is:

| `L` | supported nonzero bouquet modes | dynamic modes | two-line overlap |
|---:|---:|---:|---:|
| 3 | 44 | 18 | 8 |
| 4 | 111 | 48 | 15 |
| 5 | 224 | 100 | 24 |
| 6 | 395 | 180 | 35 |
| 7 | 636 | 294 | 48 |
| 8 | 959 | 448 | 63 |
| **total** | **2,369** | **1,088** | **193** |

Every one of these `2,369` sources has five numerical zero directions,
annihilates the complete null space, and admits a direct unprojected solve.
The runner reports the worst gauge, full-null, and solve residuals.

At `k=0`, positivity returns as the decisive boundary. For `L=5`,

    z dot s_bouquet(0)=5(1+sqrt(2))>0.                        (15)

The full-null overlap and direct-solve residual are both nonzero. This is not
a contradiction with the nonzero-mode theorem; it is exactly the separated
compact member.

## 3. Two Balanced Nonnegative Bundle Rows

Let `D_tau` be the eight edge classes with final component one. For row `w`,
the vertex-displacement current is (5). The three `r=1` directions give

    J_A=2[(1,0,0,1)+(0,1,0,1)+(0,0,1,1)]
       =(2,2,2,6).                                            (16)

For `B`, the tick contributes `(0,0,0,3)`, while the three `r=2`
directions contribute

    (1,1,0,1)+(1,0,1,1)+(0,1,1,1)=(2,2,2,3).                 (17)

Equations (16) and (17) prove (6) exactly.

Let `sigma_n` choose `A` or `B` at tick `n`, identically at every spatial
site. The real-space vertex force is

    J(sigma_n)-J(sigma_(n-1))=0.                              (18)

For nonzero pure-tick Fourier mode `omega`, the source is a scalar history
amplitude times the contrast `c`. Equation (6) makes its four-component gauge
row vanish exactly. Direct evaluation of the complete Regge null space then
gives:

| `L` | histories | nonconstant | supported nonzero history modes |
|---:|---:|---:|---:|
| 3 | 8 | 6 | 12 |
| 4 | 16 | 14 | 34 |
| 5 | 32 | 30 | 120 |
| 6 | 64 | 62 | 260 |
| 7 | 128 | 126 | 756 |
| 8 | 256 | 254 | 1,586 |
| **total** | **504** | **492** | **2,768** |

All `2,768` supported source-mode pairs annihilate the complete five-null
space and solve the actual unprojected edge equation. This is an exhaustive
finite certificate over every binary history in the declared length range,
not a random sample.

Every history has a positive mean source. Its homothety charge is exactly six
per tick, independent of the sequence, and its bare `k=0` solve residual lies
between the runner's stated positive bounds. Hence local current balance does
not remove the global scale-mode obstruction.

## 4. Pure-Shear Channel And Long-Wave Response

For pure tick momentum `k=(0,0,0,omega)`, the contrast edge row maps to

    c M(k)=-exp(i omega/2) sinc(omega/2)
            (h_xy^*+h_xz^*+h_yz^*),                          (19)

with zero lapse, shift, and diagonal components. Here the stars denote the
three covector slots, not complex conjugation. The runner checks (19) directly
against the actual line-averaged metric map.

Solving the unprojected edge equation `Q_R(k)h=-c` gives

    omega^2 c dot h -> 6                                     (20)

under successive momentum halvings. The coefficient is computed, not inserted
as a fitted prefactor.

For the bouquet, the per-step row `2e_t+2e_f` is transverse to the common
`y`, `z`, and `y+z` long-wave directions. Along all three,

    |k|^2 s_bouquet dot h -> 6.                               (21)

Equation (21) is an unprojected quadratic-carrier pole. No Newton constant,
potential sign, or physical force law is inferred from it.

## 5. Equal-Coefficient Junction Rigidity

One might try to turn equal-tension future-temporal edge strands into each
other at a balanced junction. Let

    q_S=(1_S,1)/sqrt(|S|+1),      S subset {x,y,z}.            (22)

Expand the twelve coordinate coefficients of the eight `q_S` over the
number-field basis `1,sqrt(2),sqrt(3)`. The resulting rational `12 x 8`
coefficient matrix has rank eight. Therefore

    sum_S n_S q_S=0,     n_S rational                         (23)

implies every `n_S=0`.

For equal coefficients and integer strand counts, a balanced junction can
only preserve each temporal edge-class count. It may relabel existing streams,
as the bouquet routing does, but it cannot convert one direction multiset into
another. This is not a rigidity theorem for arbitrary real tensions, spatial
struts, alternate triangulations, or additional edge species. The unequal
weights in (4) are an explicit live escape.

## 6. Composite Timelike Chord Control

The coarse chord `u` in (1) is not an actual primitive edge. Its Euclidean
length can nevertheless be written from the local tick, face, and spatial
edge lengths as

    L_u=sqrt(2 ell_t^2+2 ell_f^2-ell_x^2).                    (24)

At the flat point, the derivative of `2(L_u-sqrt(5))` is

    s_u=-(2/sqrt(5)) e_x
        +(4/sqrt(5)) e_t
        +(4 sqrt(2)/sqrt(5)) e_f.                             (25)

The actual metric map sends (25) exactly to

    s_u M(0)=u u/|u|.                                        (26)

Thus the rank-one coarse tensor can be represented locally, but one edge
coefficient is negative. Its homothety charge remains

    z dot s_u=sqrt(5)>0,                                     (27)

so it also fails the unmodified compact zero-mode equation. This is a
zero-momentum composite control only. A finite-momentum local chord action,
Ward identity, and physical Record carrier have not been constructed.

Equation (27) is also the degree-one Euler lesson. Subtracting a flat constant
does not change a source derivative. For a positive degree-one length
functional `F`, uniform metric homothety gives

    z dot grad[2(F-F_flat)]=F_flat>0.                         (28)

Changing the centering convention therefore cannot remove the scale charge.

## 7. Compact Homothety Separation Theorem

The source-bound Regge note proves that every constant metric perturbation is
an exact `k=0` zero mode. Equation (8) is the particular positive constant
metric direction. Hermiticity gives

    z^dagger Q_R(0) eta=(Q_R(0)z)^dagger eta=0                (29)

for every edge perturbation `eta`. If `Q_R(0)eta=-s`, then (29) requires
`z dot s=0`. Equation (10) contradicts that requirement for every nonzero
componentwise-nonnegative `s`.

This proof uses all fifteen extreme rays of the positive edge-source cone, so
it is not a finite search over a few networks. The runner verifies the
carrier-specific identities:

- `z_d=|d|/2`, with minimum component `1/2`;
- `Q_R(0)z=0` to the declared numerical tolerance; and
- the fifteen coefficient-two extreme-ray overlaps range from one to two.

The analytic implication from those source-bound identities is exact. The
numerical check verifies the supplied implementation and does not replace the
linear-algebra proof.

The theorem is deliberately narrow. It fixes all of:

1. the flat background;
2. the unmodified quadratic Regge Hessian;
3. compact periodic zero momentum;
4. edge-length source coordinates; and
5. componentwise nonnegative nonzero source coefficients.

Changing any of these premises leaves a distinct problem. In particular,
open boundaries, a fixed global scale, signed/background sources, curved
geometry, a constraint reaction, lifted scale/shape dynamics, and alternate
causal carriers remain live.

## 8. What This Does And Does Not Close

This block closes the following mathematical obligations on the named domain:

1. existence of a connected positive actual-edge network with a causal
   piecewise routing and strictly timelike coarse displacement;
2. exact local balance for two distinct nonnegative temporal bundles with a
   common strictly timelike aggregate current;
3. exhaustive nonzero-mode full-null compatibility and direct unprojected
   solves for both network families;
4. explicit unprojected long-wave tensor poles; and
5. an exact proof that positive edge-source rearrangement alone cannot repair
   the bare flat compact zero mode.

It does not close:

- a selected Record identity routing at the bouquet junction;
- a rank-one massive-particle stress tensor or dressed inertial source;
- constituent causality for the weighted binary bundle, which includes
  spacelike primitive edges;
- action-weight selection or a source/action unit;
- physical identification of Record content with the edge source;
- a compact ensemble, scale constraint, or curved scale/shape equation;
- geometry action, coupling, sign, Lorentzian continuation, or nonlinear
  completion;
- projective or infinite-volume consistency;
- a Born functional, trials, frequencies, or one realized history.

The [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
permits pointwise evaluation at a supplied law-admissible realized state. It
does not supply the history, law, boundary condition, or state-dependent
value needed above.

## 9. Exact Axiom Consequence

The canonical Lattice, Qubit, Admissibility, and Record wording remains
unchanged. Admissibility supplies a neighborhood-dependent probability
distribution but not an action/history law. Record supplies fixed content-only
readout but not an edge-current identity, source sign, action weight, or
geometry variation. The kinetic-isotropy primitive supplies only equal-form
tick graining.

The existing candidate **Geometry-indexed history/action amendment** in
[Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
is already sufficient to type:

- a fixed local network action and its weights;
- a combined matter-history/geometry Ward identity;
- the actual edge/metric carrier;
- a geometry action or causal update; and
- an open, boundary-fixed, background-subtracted, or globally constrained
  zero-mode ensemble.

This block sharpens one implementation obligation for that candidate:

> A model retaining the unmodified flat compact Regge zero-mode equation may
> not assign it a nonzero componentwise-nonnegative edge-length source. The
> model must instead declare its fixed/open/background/constraint/curved
> scale-mode mechanism and must separately select the Record-to-source identity
> and action weights.

That sentence is a candidate model constraint implied by (11), not adopted
axiom wording and not a new axiom requirement. The existing candidate remains
unadopted, not proved necessary, and not proved minimal. A downstream model
convention can also declare the same data without changing the four axioms.

Foundation-level autonomy would still require the framework to select or
derive the joint history/action family, physical source typing, compact
scale-mode mechanism, geometry dynamics and coupling, causal/Lorentzian
regime, and realized member. No canonical axiom is edited here.

## 10. TOE Lane Consequence

| Lane | Exact Block-16 advance | Still open |
|---|---|---|
| operational quantum / records | identity routing is isolated as distinct from the positive unlabeled source network | physical Record/source map, routing selector, action weights, and occurrence |
| causal time | one positive piecewise-causal bouquet has a strictly timelike coarse routing; two bundle families have exact local current balance | selected causal update, constituent-causal bundle, history law, and realized member |
| inertia / matter | the coarse chord is timelike and has an exact rank-one metric covector; the bouquet is explicitly diagnosed as rank two | physical mass, positive-energy semantics, dressed inertia, and action unit |
| gravity / source / resources | `2,369` positive-bouquet and `2,768` binary-history nonzero-mode solves; exact compact positive-cone separator | selected compact scale mechanism, geometry action, sign/coupling, Lorentzian and nonlinear law |
| Born probability / realized history | no Born rule is imported by either network construction | program/effect selection, law values, trials, frequencies, and one realized history |

The fixed obligation-based map remains:

| TOE lane | repo science | physical bridge | autonomous closure | evidence ceiling |
|---|---:|---:|---:|---:|
| operational quantum / records | 95% | 92% | 50% | 99% |
| causal time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity | 70% | 45% | 29% | 94% |
| Born | 84% | 63% | 34% | 99% |

The unweighted average remains `84.0 / 73.6 / 45.8 / 98.0`. The new theorem
sharpens the gravity and causal decision surface but does not retire a physical
selector or canonical obligation, so the fixed TOE percentages remain
unchanged.

## No-Go Discipline Gate

The compact homothety theorem is a negative boundary inside a positive network
construction. This N1--N8 packet limits it to the unmodified compact zero-mode
equation and prevents a positive-mass or universal gravity reading.

### N1 — alternative route enumeration

The families are normalized by primary object, load-bearing invariant, and
terminal obligation.

| Route family | Attempt and scoped outcome | Marker |
|---|---|---|
| positive network topology | Replace one line by the connected tick-plus-face bouquet; Sections 2 and 7 show all named nonzero modes close, while its positive compact total remains separated by `z`. Topology does not change equation (10). | ATTEMPTED |
| unequal positive bundle weights | Solve the local balance equation with two distinct nonnegative rows; Sections 3--4 give exact common current and `2,768` nonzero-mode solves, but every positive mean has homothety charge six. Positive reweighting remains inside the separated cone. | ATTEMPTED |
| composite causal chord | Replace the rank-two stream reading by the local degree-one chord (24); equations (25)--(28) produce the desired rank-one timelike metric row, but its positive scale charge remains `sqrt(5)`. | ATTEMPTED |
| signed/background counterstress | Use the Block-14 transverse signed pair; it cancels `k=0` exactly and therefore defeats any all-source or positive-mass-independent no-go, but it leaves the componentwise-nonnegative domain of (11). Evidence: Block 14, Sections 4 and 7. | RULED OUT BY PRIOR |
| fixed-global or open-boundary domain | Remove the constant variation or the compact mode; Block 14 verifies the positive line on all `1,281` supported nonzero modes, and Block 13 gives the open Green route. These solve a changed domain, not the unmodified equation in (11). Evidence: Block 14, Section 4; Block 13, Sections 4--5. | RULED OUT BY PRIOR |
| lifted or alternate geometry operator | Change the quadratic null space; Block 14's explicit fifth-branch lift already proves that carrier null obstructions need not survive operator changes. It does not lift the scale mode physically, so curved and scale/shape actions remain live rather than ruled out. Evidence: Block 14, Sections 4 and 6. | RULED OUT BY PRIOR |

The first three families are distinct respectively in network topology,
weighted current decomposition, and composite length geometry. The last three
change the source sign, operator domain, or operator itself. Together they
force the theorem to retain every qualifier listed in Section 7.

### N2 — wall independence

For physical closure, collapse the open conditions to `W1` history/action and
Record-source selection, `W2` compact scale-mode mechanism, `W3` causal
rank-one positive-matter carrier, and `W4` geometry dynamics/coupling/
Lorentzian-nonlinear completion.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W1,W2` | no; selecting a local action does not choose its global zero-mode ensemble | no; fixing the scale mode does not select a matter history | yes |
| `W1,W3` | no; a selected network may be rank two or contain spacelike edges | no; a causal tensor does not identify the Record law or action weights | yes |
| `W1,W4` | no; a matter action does not determine the geometry action or coupling | no; geometry dynamics does not select the Record carrier | yes |
| `W2,W3` | no; signed or fixed-scale ensembles need not be positive rank-one matter | no; positive causal matter still has nonzero compact scale charge | yes |
| `W2,W4` | no; a boundary convention does not supply nonlinear geometry | no; a geometry law may still require a declared compact sector | yes |
| `W3,W4` | no; a causal particle source does not determine its gravitational coupling | no; a geometry theory does not select which matter source is realized | yes |

Born/program selection and the realized member are separate downstream TOE
lanes, not load-bearing walls in the compact separator proof. No wall above
collapses into another.

### N3 — hidden-condition scan

The source was searched for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| `background` / `background-subtracted` | explicit source-sign or geometry premise outside the positive-cone theorem; named in Sections 7 and 9 |
| `registered` wording | appears in the cited, unadopted Block-12 candidate and in N8's historical convention-retirement description; neither is current authority used to prove (11) |
| `canonical` | governance boundary stating that the four-axiom memo is not edited; non-load-bearing |
| all remaining scan phrases | absent outside this checklist's literal search list |

The flat carrier, periodic compact domain, quadratic Hessian, edge coordinates,
source sign, network weights, finite size range, and naive Lorentzian diagnostic
are all explicit. The scan adds no hidden condition.

### N4 — residual matching

| Cited witness | Witness residual | Present residual or closure | Match? |
|---|---|---|---|
| Block 14, positive-line zero-mode control | one positive closed helix has nonzero compact full-null and solve residual | equations (8)--(11) generalize exactly that positive edge-source `k=0` residual | yes |
| Block 14, signed pair | signed transverse subtraction cancels total compact source | N1 and Section 7 retain it only as an outside-positive-cone escape | yes |
| Block 13, compact tick control | nonzero total tick charge is outside the bare periodic Hessian image | `z` proves the same bare compact source-image residual for the full positive cone | yes |
| Regge second-variation note, constant metric modes | every constant metric perturbation is an exact `k=0` zero mode | equations (8)--(10) use precisely the identity-metric member | yes |
| Block 12, candidate ensemble wording | the candidate types fixed/open/background/constrained ensembles without selecting them | Section 9 preserves the same typing-versus-selection residual | yes |

No scalar Poisson surrogate, continuum Einstein equation, fitted coupling, or
body-edge fifth-branch residual is cited as proof of the homothety theorem.

### N5 — rhetoric audit

| Resolution | Executed statement | Scope not claimed |
|---|---|---|
| per element | all fifteen positive edge-source extreme rays, eight temporal unit directions, two bundle rows, and the composite chord derivative | no arbitrary signed functional, physical particle ontology, or alternate carrier |
| per site | exact balance for every site in all `504` binary histories and the single shared bouquet junction | no selected routing, collision law, or arbitrary network theorem |
| per mode | all `2,768` supported binary history-mode pairs and `2,369` supported nonzero bouquet sources against the full null space | no continuous-Brillouin or arbitrary-size classification |
| per block | number-field rigidity, two positive current constructions, two unprojected poles, and the axiom boundary | no physical coupled nonlinear theory |
| lattice wide | all `8,755` modes on six four-tori, every binary history of lengths three through eight, and every positive compact mean | no universal compact, open-lattice, or curved-background theorem |

The cached stdout lands one substantive certificate line at each resolution.
“Timelike” is used only for the explicitly computed aggregate or coarse
diagnostic. It is not applied to every constituent edge or to a derived
Lorentzian dynamics.

### N6 — partial-closure paths

| Candidate path | Status | What it closes |
|---|---|---|
| connected positive bouquet, this note | executed bounded construction | positive actual-edge nonzero-mode closure and one coarse timelike causal routing |
| unequal weighted binary bundles, this note | executed bounded construction | local dynamic balance and a pure-shear nonzero-mode channel |
| signed pair, Block 14 | executed bounded construction | one background-subtracted compact source equation |
| fixed-global domain, Block 14 | executed conditional route | positive-source solvability after removing only the constant variation |
| open boundary, Blocks 13--14 | executed conditional route | noncompact infrared response without a normalizable compact zero mode |
| composite chord, this note | executed `k=0` control | exact rank-one timelike metric covector, while exposing its positive scale charge |
| Geometry-indexed history/action amendment, Block 12 | unadopted sufficient wording | types the action, carrier, Ward equation, geometry law, and zero-mode ensemble |
| downstream model convention, Block 12 | existing conditional route | declares the same mathematical inputs without a canonical edit |
| curved or lifted scale/shape geometry | open concrete mechanism | could change equation (9) and must be tested in the combined nonlinear theory |

The approved primitives are not walls. None of these paths justifies “requires
a new axiom.” The exact classification is a bounded theorem plus a named
current-operator obstruction and several live import-retirement routes.

### N7 — steelman

A hostile reviewer should say that equation (11) is merely the expected
linearization-instability of a positive total source around a flat compact
background with an unfixed uniform scale. Physical positive mass need not
appear as a bare componentwise-positive edge row in that equation: a global
constraint reaction, boundary term, signed gravitational contribution, curved
background, or nonlinear matter-plus-geometry solution can cancel the scale
charge. The strongest repository support is already Block 12's explicit
fixed/open/background/constrained ensemble split and Block 14's signed and
fixed-global solutions. The reviewer should also reject the binary bundle as a
particle because `B` contains spacelike primitive edges and reject the bouquet
as rank-one dust because its source is a two-stream sum. This steelman is
accepted against every broad physical no-go. It does not refute the narrow
linear-algebra statement (11), because each proposed escape changes a stated
premise. The shipped result is therefore the narrow compact separator and the
positive nonzero-mode constructions only.

### N8 — cross-cycle echo

The required repository phrase search and campaign `NO_GO_LEDGER.md` walk find
the following similar walls and later retirement mechanisms:

| Prior wall | Later mechanism and lesson here |
|---|---|
| Block-12 localized affine bag | Block 13 changed the local action representative and retired the localized nonzero-mode residual; source representatives must remain live. |
| Block-13 fixed vertical row and compact tick charge | Block 14 completed the row into a closed history and supplied signed/fixed-global infrared routes; support and ensemble changes must remain live. |
| Block-14 null moving line and signed source | this note supplies a positive coarse-timelike bouquet and balanced positive bundle rows, while retaining rank and constituent-causality limits. |
| Block-10 fixed-background source-family nonuniqueness | Block 11 supplied an explicit geometry-indexed family; a convention or registered family can partially retire a wall without new axiom content. |
| registrability-bridge convention walls in `.claude/science/physics-loops/registrability-bridges-20260610/NO_GO_LEDGER.md` | owner ratification and import-retirement audit are separate from a physics no-go; Section 9 keeps the existing candidate unadopted rather than calling it impossible. |

Every mechanism that retired a similar wall—new representative, completed
support, changed ensemble, explicit geometry family, or owner ratification—is
kept live. No universal gravity no-go and no axiom-necessity claim survives.

**Gate status:** PASS for equation (11) on the five explicitly fixed premises
and for the named positive-network finite inventories. FAIL for any
positive-mass, all-carrier, all-boundary, curved/nonlinear, causal-particle, or
“new axiom required” interpretation.

## 11. Verification

Run:

    python3 scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py

The runner checks:

- source boundaries in the current axioms, approved primitives, Block-12
  candidate, Block-14 line construction, and actual Regge theorem;
- the eight temporal-edge inventory and exact number-field rank-eight
  equal-coefficient rigidity;
- the two nonnegative bundle rows, exact current identity, and timelike
  aggregate diagnostic;
- every one of `504` binary histories and all `2,768` supported nonzero
  history-mode pairs;
- pure-shear metric descent and the unprojected coefficient-six tensor pole;
- bouquet connectedness, causal/coarse-timelike routing, and all `2,369`
  supported nonzero source solves among `8,755` total modes;
- the positive bouquet compact control and three-direction coefficient-six
  pole;
- the exact positive homothety vector, all fifteen cone extreme rays, and the
  composite chord control;
- N1--N8, physical boundaries, axiom nonmutation, and all five required
  resolution certificates.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    actual closed positive edge lines
      -> connected bouquet with coarse timelike causal routing
      -> exhaustive nonzero-mode five-null compatibility
      -> distinct positive bundle rows with identical timelike current
      -> every finite binary history locally balanced
      -> pure-shear and bouquet 1/k^2 response
      -> positive homothety null covector at compact k=0
      -> exact separation of the nonzero positive edge-source cone.

This is significant gravity-source progress: the positive/casual-history search
does not fail at local balance or nonzero Regge modes. The remaining bare
compact failure is now an exact scale-mode theorem rather than an empirical
list of failed examples. Physical closure still requires a selected
Record/source action, compact scale mechanism, causal matter carrier, geometry
dynamics and coupling, Lorentzian/nonlinear completion, Born law, and realized
history. No canonical axiom is edited. No universal no-go is claimed. The
fixed TOE percentages remain unchanged.

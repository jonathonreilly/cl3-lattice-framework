---
claim_id: admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On the supplied periodic four-dimensional Kuhn/Coxeter edge carrier, the coefficient-two actual-edge action of a straight closed helix has an exact telescoping vertex-gauge Ward identity on every Fourier mode. The static direction v=(0,0,0,1) is exactly the Block-13 tick line; the moving direction v=(1,0,0,1) is a prescribed tick-space face-diagonal history. A signed pair of parallel helices separated by one transverse edge cancels the compact zero mode exactly. Across all 8,755 modes of L=3 through L=8 four-tori it has 1,088 nonzero sources, including 922 with nonzero tick frequency; every sourced mode has five Regge null directions, full-null compatibility, and a direct unprojected edge solve. Of those sources, 990 are on principal line-averaged metric support, including 824 dynamic modes, while 98 disclosed Brillouin-edge Umklapp modes have zero line-averaged metric source but remain solvable edge modes. The per-edge, equivalently per-lattice-step, moving principal source maps to vv/|v| and its unprojected long-wave response satisfies |k|^2 h_vv -> 2 sqrt(2) with the open three-transverse-dimensional 1/r Green shape. A single positive helix retains the periodic k=0 obstruction, the signed pair is not a positive-mass ensemble, the full body-diagonal edge is an explicit fifth-null-branch rejector, and no history selection, causal update, timelike Lorentzian motion, physical mass, coupling, nonlinear dynamics, realized history, axiom adoption, or universal carrier theorem is proved."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py
---

# Closed Helical Defect History Ward Identity, Neutral Infrared Pair, And Regge Response Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** prescribed moving-history construction, exact Ward identity, and
explicit compact infrared ensemble
**Scope:** the supplied flat periodic four-dimensional Kuhn/Coxeter edge
carrier, two actual edge directions, and the named `L=3,...,8` four-tori.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py](../scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py)

## Result Up Front

[Block 13](ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
converted the isolated affine bag into one actual coefficient-two tick edge.
Its static nonzero modes were exactly gauge and full-null compatible, but a
fixed vertical line at nonzero tick frequency was not a history and failed the
Ward test. The bare compact zero mode also remained incompatible.

This block changes the support, not the Hessian and not the source by
projection. On a periodic four-torus, let

    t=(0,0,0,1),       v=(1,0,0,1),       b=(0,1,0,0).       (1)

The `t` edge is the Block-13 static member. The `v` edge is an actual
tick-space face diagonal. For anchor `a`, define the centered line action

    A_v,a[g]=2 sum_(n=0)^(L-1) (ell_v(a+n v;g)-|v|).          (2)

The path closes because `a+Lv=a` modulo `L`. Its edge derivative is a closed
straight line rather than a vertical edge given an arbitrary time-dependent
weight. The coefficient two is the same declared action unit as the static
line; it is not fitted to a gravitational constant.

For torus momentum `k`, define

    theta=k dot v,
    F_L(theta)=sum_(n=0)^(L-1) exp(i n theta),
    s_v,a(k)=2 exp(i k dot a) F_L(theta) e_v.                 (3)

The actual vertex-displacement gauge row for edge `v` is

    e_v Gamma(k)=(exp(i theta)-1) v/|v|.                     (4)

Therefore the complete closed line obeys the exact finite identity

    F_L(theta)(exp(i theta)-1)=exp(i L theta)-1=0,            (5)

because every torus momentum has `exp(iL theta)=1`. Equation (5) annihilates
all four vertex-gauge directions. It is an action-level telescoping Ward
identity, not a fitted conservation constraint.

The moving line still carries nonzero total compact source. The explicit
background-subtracted pair

    A_pair[g]=A_v,0[g]-A_v,b[g],
    s_pair(k)=2 F_L(theta)(1-exp(i k dot b)) e_v              (6)

cancels `k=0` exactly. The two helices are disjoint on every declared torus.
No pseudoinverse or null projection enters (6).

Direct evaluation of the actual `15 x 15` Regge edge Hessian gives:

- all `8,755` Fourier modes on the six four-tori are classified;
- `1,088` have a nonzero pair source;
- `922` of those have nonzero tick frequency;
- every sourced mode has five numerical zero directions;
- every sourced mode annihilates the complete zero space; and
- every sourced edge equation solves directly without source projection.

The worst full-null overlap and solve residual are reported by the runner.
This is the first stack member with a prescribed moving defect support and an
explicit finite periodic infrared ensemble that solve the actual edge
equation together.

The result remains narrower than a physical worldline theory. The moving
member is a Euclidean face diagonal with one spatial step per tick. Under a
naive Lorentzian continuation it is null, not a massive subluminal timelike
trajectory. Equation (6) is signed and is not a positive-mass ensemble. The
history is prescribed; it is not a dynamics law and is not selected by the
current axioms.

## 1. Source-Bound Inputs

The only scientific inputs are repository-local:

1. the [current four axioms](MINIMAL_AXIOMS_2026-06-29.md), used only to fix
   what they do not select;
2. the [equal-form tick primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
   used only for the declared tick normalization;
3. [Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
   which supplies the existing candidate history/action and infrared wording;
4. Block 13, which supplies the actual static coefficient-two tick edge; and
5. the [actual cubic-Coxeter Regge Hessian](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md).

No external theorem, observed constant, Einstein equation, continuum target,
mass value, or probability law is imported. The finite geometric sum in (5)
is derived in the runner from the actual line.

## 2. Closed Actual-Edge Histories

Let the edge coordinates be the fifteen nonzero binary directions in one
four-cell. Both

    t=(0,0,0,1),       v=(1,0,0,1)                            (7)

are actual edge classes. The ordered vertex set of one line is

    gamma_v,a={a+n v mod L : n=0,...,L-1}.                   (8)

Since the tick component of either direction is one, (8) contains exactly
`L` distinct vertices and returns to its anchor after the `L`th edge. The
second line `gamma_v,b` has `y=1` while the first has `y=0`, so the two are
disjoint for `L>=3`.

At flat geometry every term in (2) is zero. Varying one actual line-edge
length gives derivative two. For `v=t`, the per-edge derivative is identically
the Block-13 source

    s_t=2 e_t,       s_t M(k)=T_tau_tau=1       when k_tau=0. (9)

Thus the static member is inherited rather than renormalized.

For the moving principal support `k dot v=0`, divide the complete line source
by its structure factor `F_L(0)=L`. The resulting per-edge, equivalently
per-lattice-step, actual metric map gives

    2 e_v M(k) = (v tensor v)/|v|.                           (10)

This contains tick density, spatial stress, and tick-space flux. Contracting
(10) with the continuum gauge columns gives zero because `k dot v=0`.
Equation (10) is a mathematical rank-one Euclidean source. It is not a
physical mass identification.

## 3. Exact Closed-Line Ward Identity

The Fourier source in (3) is computed directly from all `L` edges. Multiplying
its single-edge gauge row produces

    s_v,a(k) Gamma(k)
      =2 exp(i k dot a) F_L(theta)(exp(i theta)-1) v/|v|
      =2 exp(i k dot a)(exp(iL theta)-1) v/|v|
      =0.                                                     (11)

This proof holds on every torus mode, including modes where the source itself
vanishes. It also holds for any finite linear combination of closed parallel
lines, so the signed pair inherits it exactly.

The distinction from the Block-13 dynamic control is precise. A fixed
vertical edge row evaluated at arbitrary `k_tau!=0` lacks the sum in (3), so
its single-edge factor in (4) does not telescope. A genuine closed line
supplies the missing translated edges.

Gauge conservation is not sufficient on this carrier. The actual Regge
Hessian has a fifth decoupled non-metric branch. The full body-diagonal edge

    w=(1,1,1,1)                                             (12)

passes the closed-line gauge identity at `k dot w=0` but lies in that fifth
branch on the displayed control: its extra-null overlap and direct solve
residual are both two for the coefficient-two row. The face diagonal `v` has
no body-edge component; exhaustive full-null checks below establish its
compatibility on the named inventory. Equation (12) is a carrier-specific
rejector, not a universal worldline obstruction.

## 4. Neutral Pair And Complete Finite Inventory

For centered Fourier indices on each `L`-torus, the line factor is nonzero
exactly when

    m_x+m_tau=0 mod L.                                      (13)

The transverse difference in (6) is nonzero exactly when

    m_y != 0 mod L.                                         (14)

The resulting inventory is:

| `L` | nonzero pair sources | nonzero-`k_tau` sources |
|---:|---:|---:|
| 3 | 18 | 12 |
| 4 | 48 | 36 |
| 5 | 100 | 80 |
| 6 | 180 | 150 |
| 7 | 294 | 252 |
| 8 | 448 | 392 |
| **total** | **1,088** | **922** |

For every one of these `1,088` sources, the runner rebuilds the actual Regge
Hessian, diagonalizes it, checks that the zero-space dimension is five,
contracts the source with the complete zero space, and solves the unprojected
edge equation. It does not infer full-null compatibility from the four gauge
columns.

The other explicit infrared route is to fix the compact global mode rather
than subtract a source. Removing only `k=0`, one positive helix is gauge and
full-null compatible and directly solvable on all `1,281` supported nonzero
modes of the same six tori. Thus the single-line obstruction below is exactly
the retained global-mode choice, not a failure of its nonzero modes.

The compact control is discriminating. For `L=5`, one positive helix has

    ||s_v(0)||=10,
    ||Z(0)^dag s_v(0)||=8.164965...,
    ||Q(0)Q(0)^+s_v(0)-s_v(0)||=8.164965...,                 (15)

whereas the signed pair has source, null overlap, and solve residual exactly
zero at `k=0`. The pair therefore executes one explicit compensating-total-
source route left open by Blocks 12 and 13. It does not prove that Nature
chooses that route.

### Principal support and Umklapp disclosure

The congruence (13) contains two classes in the centered Brillouin inventory:

- `990` principal modes have `m_x+m_tau=0` as an integer, including `824`
  modes with nonzero tick frequency; and
- `98` even-`L` boundary modes have `m_x+m_tau=-L`.

On the principal modes, (10) is the rank-one metric source. On the `98`
boundary modes the line-averaged metric-map sinc is exactly zero, so the
source has no line-averaged metric image; it is nevertheless a compatible and
solvable edge source. Those modes are disclosed as Umklapp lattice modes and
are not used for the continuum response claim.

## 5. Unprojected Moving-Line Regge Pole

Normalize the principal closed source per lattice step, so its edge row is
`2 e_v` rather than the extensive `2L e_v`. Let `u=v/|v|` and choose a small
momentum perpendicular to `v`. Because
`k dot u=0`, the contraction `u^T h u` is invariant under the continuum gauge
shift `h -> h + k tensor xi + xi tensor k`. For the
coefficient-two moving edge, solve the actual metric-sector equation

    M(k)^dag Q_R(k) M(k) h(k) + (2 e_v M(k))^dag = 0.        (16)

No source projection is made. Four perpendicular directions are tested. At
`|k|=0.025`, they give

    |k|^2 u^T h(k) u -> 2 sqrt(2).                           (17)

The target follows from the same Euclidean rotational continuum limit that
gave the static coefficient two, multiplied by the face-diagonal length
`|v|=sqrt(2)`. Halving momentum improves every error. The direct metric solve
and gauge residual are separately checked. One lattice step has Euclidean
arclength `sqrt(2)`; a density normalized per Euclidean arclength would divide
(16)--(18) by `sqrt(2)`. No physical line-density convention is selected.

A straight line in four Euclidean dimensions has three transverse momentum
directions. The regulated inverse transform of its `1/k_perp^2` pole is

    G_epsilon(r_perp)
      =atan(r_perp/epsilon)/(2 pi^2 r_perp)
      ->1/(4 pi r_perp).                                    (18)

The runner checks monotone regulator convergence. Equation (18) is an open
transverse Green shape per lattice step. It does not erase (15) for a single
compact positive line.

## 6. What This Does And Does Not Close

The construction retires two mathematical existence questions on the named
carrier:

1. a prescribed moving actual-edge history can obey the complete gauge Ward
   identity and the full five-null compatibility condition without source
   projection; and
2. one explicit background-subtracted periodic ensemble cancels the compact
   zero mode and solves every sourced Fourier equation.

It does not retire the physical obligations:

- why the face-diagonal history action and coefficient are selected;
- how an isolated Qubit/Record defect is typed as the line source;
- a positive-energy or positive-mass compact ensemble rather than (6);
- a subluminal timelike history and causal local update;
- the physical action representative and action unit;
- geometry action selection, orientation, coupling sign, and coupling size;
- Lorentzian and nonlinear completion;
- projective family consistency, Born functional, and one realized history.

In particular, a prescribed history is not a history law. Exact source
conservation is not a dynamics law. A signed background subtraction is not a
positive-mass ensemble. A Euclidean face diagonal is not a derived massive
timelike trajectory.

## 7. Exact Axiom Consequence

No broader candidate wording is needed. The existing candidate **Geometry-
indexed history/action amendment** already supplies, if adopted, a fixed local
history-action representative, geometry-dependent improvements, a geometry
carrier and action, a combined Ward identity, and a declared open, fixed,
background-subtracted, or constrained zero-mode ensemble. Equations (2) and
(6) fit that wording directly.

The existing candidate remains unadopted, not proved necessary, and not
proved minimal. The present result strengthens the downstream-convention
route: a model can declare (2), the actual Regge carrier, and the signed
periodic ensemble (6) without changing the four axioms. Therefore no new
axiom is required for this conditional mathematics.

Foundation-level autonomy would still require either that existing candidate
or an equivalent set of obligations to select the history/action family,
physical source typing, geometry dynamics, coupling, causal/Lorentzian regime,
infrared positivity, and realized member. No canonical axiom is edited here.

## 8. TOE Lane Consequence

| Lane | Exact Block-14 advance | Still open |
|---|---|---|
| operational quantum / records | the static tick source now sits in a prescribed closed-history family | physical defect/Record typing, action selection, and occurrence |
| causal time | one nonzero-`k_tau` closed history has an exact telescoping Ward identity | timelike subluminal carrier, causal update, history law, and realized member |
| inertia / matter | the per-lattice-step moving principal source is the actual rank-one `v tensor v/|v|` line response | physical mass, positive energy, dressed inertia, and action unit |
| gravity / source / resources | 1,088 full-null-compatible unprojected periodic sources, explicit neutral `k=0` cancellation, and moving `1/k^2`/transverse `1/r` response | positive-source IR ensemble, geometry selection, sign/coupling, Lorentzian and nonlinear law |
| Born probability / realized history | the construction does not assume a Born functional | program/effect selection, probability law, trials, and one realized history |

This is meaningful repo-science progress but remains bounded support on an
open stack. No physical/autonomous selector is retired. The fixed TOE
percentages remain unchanged.

## No-Go Discipline Gate

The positive face-diagonal construction contains two negative controls: one
positive compact line retains `k=0`, and the full body diagonal hits the fifth
branch. The following N1--N8 packet prevents either control from becoming a
universal no-go.

### N1 — alternative route enumeration

Approach families are normalized by their primary object, mechanism, and
terminal obligation.

| Route family | Attempt and scoped outcome | Marker |
|---|---|---|
| face-diagonal actual-edge history | Replace the failed time-modulated vertical row by the translated actual-edge cycle (2); equations (3)--(11) close gauge and full-null compatibility, so this route defeats any broad dynamic-source no-go but does not alter the body-edge control. Evidence: this note, Sections 2--5. | ATTEMPTED |
| signed source neutralization | Subtract a disjoint parallel helix; equation (6) cancels the compact zero mode and solves the named inventory, so it defeats any all-ensemble no-go but changes the single-positive-source fixture. Evidence: this note, Section 4. | ATTEMPTED |
| open/infinite boundary | Remove the compact normalizable zero mode and solve the transverse Green problem; equation (18) is positive, but it changes the boundary premise and therefore does not solve the bare periodic single-line equation. Evidence: `docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:136-147`. | ATTEMPTED |
| fixed-global-mode domain | Remove only the constant variation from the domain; the runner verifies that the positive helix is compatible and directly solvable on all `1,281` supported nonzero modes, so this route defeats a line-wide no-go while changing the unconstrained compact problem in (15). Evidence: Section 4 and the `single-line-fixed-global-mode-route` check. | ATTEMPTED |
| explicit fifth-branch lift | Add the rank-one projector onto the isolated fifth null direction; the runner verifies that this preserves the four gauge zeros and makes the body source solvable, so the body residual is not stable under a lifted operator. Evidence: the `body-diagonal-lifted-branch-route` check and `docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:106-116`. | ATTEMPTED |

These five families differ in support completion, source neutralization,
boundary condition, operator domain, and operator spectrum. Combined-geometry
constraints, alternate triangulations, and balanced multi-edge junctions are
additional untested live mechanisms, not routes mislabeled as attempted.
Their existence forces the negative claims to remain the single-positive-line
compact control and the fixed-carrier body-edge control only.

### N2 — wall independence

Define `W1` history/action selection, `W2` four-gauge Ward closure, `W3` fifth-
branch compatibility, `W4` compact zero-mode ensemble, and `W5` positive
timelike physical interpretation. The pairwise audit is:

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W1,W2` | no; selecting a history does not conserve it | no; a conserved supplied history need not be selected | yes |
| `W1,W3` | no; selection does not remove a carrier zero branch | no; carrier compatibility does not select a history | yes |
| `W1,W4` | no; local selection does not choose the global ensemble | no; an ensemble does not select the local action | yes |
| `W1,W5` | no; mathematical selection need not be positive or timelike | no; interpretation alone does not select a law | yes |
| `W2,W3` | no; the body control passes gauge and fails the fifth branch | no; fifth-branch orthogonality does not imply gauge conservation | yes |
| `W2,W4` | no; nonzero-mode Ward closure leaves `k=0` | no; total-charge cancellation does not enforce local Ward closure | yes |
| `W2,W5` | no; Euclidean conservation does not imply timelike positivity | no; a timelike label does not prove the discrete Ward identity | yes |
| `W3,W4` | no; avoiding the fifth branch does not cancel total source | no; zero total charge does not avoid the fifth branch | yes |
| `W3,W5` | no; carrier compatibility does not supply physical mass | no; physical interpretation does not lift a carrier branch | yes |
| `W4,W5` | no; signed neutrality is not positive mass | no; positivity does not solve compact compatibility | yes |

Block 14 closes `W2` for every repeated-edge closed line of the form (2),
closes `W3` for the face-diagonal inventory, and closes one signed instance
of `W4`. The body control fails
`W3` while passing `W2`; the single-line control fails `W4` while passing the
nonzero-mode tests. No wall collapses into another.

### N3 — hidden-condition scan

The source was searched for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| `background-subtracted` / `background subtraction` | explicit signed-ensemble condition `W4`; not hidden and not physical positivity |
| `canonical axiom` | governance boundary only; no scientific inference is made from the label |
| all other scan phrases | absent outside the quoted checklist itself; that checklist is non-load-bearing methodology text |

The finite periodic carrier, Euclidean signature, edge directions,
coefficient two, signed pair, and named sizes are explicit conditions. The
`98` Umklapp modes are separately counted. The scan adds no hidden wall.

### N4 — residual matching

| Cited witness | Witness residual | Present residual/closure | Match? |
|---|---|---|---|
| `docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:141-147` | positive compact tick charge is outside `Q_R(0)` and a fixed vertical edge fails for `k_tau!=0` | (3)--(6) supply the translated history and neutral total source | yes |
| `docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:453-481` | the narrow dynamic/zero-mode controls retain closed-worldline and neutral-pair routes | Sections 2--4 execute exactly those two routes | yes |
| `docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:41-49` | four gauge zeros plus one quadratic non-metric zero branch | complete five-null inventory plus body control (12) | yes |
| `docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:510-545` | candidate types history/ensemble but leaves their physical selection open | Section 7 keeps the constructed history typed but unselected | yes |

No scalar surrogate, projected source, or continuum Einstein target is used as
evidence for the actual edge equation.

### N5 — rhetoric audit

| Resolution | Executed statement | Scope not claimed |
|---|---|---|
| per element | actual tick, face-diagonal, and body-diagonal edge rows | no arbitrary edge action or physical particle ontology |
| per site | closed `L`-edge helix and disjoint transverse pair | no general junction, collision, or local update rule |
| per mode | all `1,281` supported nonzero modes of the fixed-global positive line and every one of the `1,088` nonzero pair sources, including all named dynamic and Umklapp classes | no continuous-Brillouin or arbitrary-size theorem |
| per block | static inheritance, Ward identity, neutral ensemble, per-lattice-step Regge pole, and transverse Green tail | no selected coupled nonlinear theory |
| lattice wide | all `8,755` Fourier modes on the six named four-tori | no universal compact or open-lattice classification |

The cached stdout lands one substantive certificate line for each resolution.
“Dynamic” means nonzero tick frequency in a prescribed Euclidean history, not
autonomous causal dynamics. “Infrared completion” means the explicit signed
pair only, not every physical compact ensemble.

### N6 — partial-closure paths

| Candidate path | Status | What it closes |
|---|---|---|
| face-diagonal actual-edge history, this note | executed bounded construction | dynamic mathematical Ward/full-null existence without a carrier change |
| signed pair, this note | executed bounded construction | one background-subtracted compact zero-mode ensemble |
| open Green problem, Block 13 lines 136--147 | executed conditional boundary route | single-line infrared response without compact `k=0` |
| fixed-global-mode domain, this note | executed conditional boundary route | positive-line solvability on all `1,281` supported nonzero modes |
| algebraic fifth-branch lift, this note | executed counter-control | shows the body residual depends on retaining the exact quadratic flat branch; it does not derive a physical lift |
| Geometry-indexed history/action amendment, Block 12 lines 510--532 | unadopted sufficient wording | foundation-level typing of the representative and ensemble, not their derivation |
| downstream model convention, Block 12 lines 493--504 | existing conditional route | types (2) and (6) without a canonical edit |
| higher-order/lifted carrier, Regge note lines 106--116 | explicitly open | could remove the body-edge lattice branch |

The approved kinetic-isotropy primitive supplies only equal-form graining; it
is not counted as a dynamics wall. These paths make “new axiom required” and
universal body/worldline no-go readings invalid.

### N7 — steelman

A hostile reviewer should argue that the body-diagonal residual is plainly a
quadratic lattice artifact, because the supplied Regge authority itself says
the fifth branch is exactly decoupled and leaves cubic and higher order
unaddressed (`docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:106-116`). They should then attack the physical relevance of the positive result:
(6) uses a negative source, and `v=(1,0,0,1)` is null under a naive Lorentzian
reading. A lifted action, alternate triangulation, or balanced multi-edge
junction is a concrete unclosed mechanism whose terminal obligation is a
positive subluminal compact history. This steelman is accepted. The result is
therefore a positive bounded construction plus two named controls, not a
body-edge, timelike-history, or positive-mass no-go.

### N8 — cross-cycle echo

The repository-wide phrase search and the campaign `NO_GO_LEDGER.md` walk find
the following structurally similar walls and later mechanisms:

| Prior wall | Later mechanism / lesson here |
|---|---|
| Block-12 localized affine bag (`.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md`, Block 12 row) | Block 13's explicit line-minus-bag improvement retired the generic gauge/fifth-branch residual; alternate local representatives must remain live. |
| Block-13 compact charge and fixed vertical line (same ledger, Block 13 row) | this block executes the named neutral-pair and closed-worldline routes; negative fixtures must not be generalized. |
| Block-10 fixed-background source nonuniqueness (same ledger, Block 10 row) | Block 11 supplied a geometry-indexed action family; convention/family registration can partially close a wall without a new axiom. |
| earlier convention-class walls in `.claude/science/physics-loops/registrability-bridges-20260610/NO_GO_LEDGER.md` | owner ratification and import-retirement audit are distinct from new physics; Section 7 preserves that distinction. |

The mechanisms that retired the similar walls—explicit improvement, support
completion, declared convention, and owner ratification—are all retained.
No universal no-go and no axiom-necessity claim survives the positive
face-diagonal construction.

**Gate status:** PASS for the bounded face-diagonal closed-history theorem,
the signed-pair finite inventory, and the named body-edge rejector. FAIL for
any universal no-go, positive-mass, causal-dynamics, timelike-motion, or “new
axiom required” reading.

## 10. Verification

Run:

    python3 scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py

The runner checks:

- source boundaries in the axioms, Block 13, the existing candidate, the tick
  primitive, and the actual Regge theorem;
- closed-cycle combinatorics and transverse-line disjointness for `L=3,...,8`;
- exact inheritance of the Block-13 static tick member;
- direct-versus-formula Fourier equality and the telescoping Ward identity;
- principal rank-one moving metric source and transversality;
- all `8,755` torus modes, `1,088` nonzero sources, `922` dynamic sources,
  `824` principal dynamic modes, and `98` Umklapp modes;
- all `1,281` supported nonzero positive-line modes after fixing `k=0`;
- complete five-null overlap and direct unprojected solve residuals;
- single-line `k=0`, neutral-pair cancellation, body-diagonal, and explicit
  fifth-branch-lift controls;
- four-direction unprojected `2 sqrt(2)` pole and open transverse Green tail;
- N1--N8, boundary, canonical-nonmutation, and five-resolution surfaces.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    exact Block-13 static tick edge
      -> actual closed tick-space face-diagonal history
      -> exact telescoping four-gauge Ward identity
      -> exhaustive full five-null compatibility
      -> signed parallel pair with exact k=0 cancellation
      -> unprojected periodic edge solves
      -> moving 1/k^2 and transverse 1/r response.

This closes mathematical existence of one prescribed moving conserved source
and one explicit compact neutral ensemble on the actual carrier. It does not
derive a massive timelike particle, positive compact energy, history-selection
law, geometry dynamics, coupling, nonlinear field equation, Born functional,
or realized history. No canonical axiom is edited. No universal no-go is
claimed. The fixed TOE percentages remain unchanged.

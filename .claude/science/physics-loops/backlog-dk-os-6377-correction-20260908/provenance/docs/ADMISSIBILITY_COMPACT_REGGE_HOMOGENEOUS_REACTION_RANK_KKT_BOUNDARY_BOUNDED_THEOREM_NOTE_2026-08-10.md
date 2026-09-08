---
claim_id: admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the supplied flat periodic four-dimensional Kuhn/Coxeter 15-edge Regge Hessian at zero momentum, the null space has dimension eleven: the ten-dimensional constant-metric image plus one independent exactly flat nonmetric branch. For a source family S, the minimum number of linear variational reaction channels needed merely to make every equation Q0 h + C lambda = -s solvable is rank(P_ker(Q0) S). The per-step Block-15/16 tick-plus-face source, the two Block-16 matched bundle endpoints (and therefore all 504 binary-history means), and their combined family have exact reaction ranks one, two, and three. A pure homothety reaction is not aligned with any of the three declared generators, and its best null residuals are nonzero. Reactions confined to constant-metric scale and shape also miss the independent nonmetric branch for the tick-plus-face and B sources. Three source-aligned mixed reactions give existence for the combined family; four sector-separated reactions give the same existence while separating three metric reactions from one extra-branch reaction; eleven full-null reactions make the KKT system unique. These are exact finite-dimensional statements on the named carrier, not a selected physical constraint law, source action, compact boundary, nonlinear geometry, or universal compact-gravity no-go."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - kinetic_isotropy_primitive
  - realized_state_primitive
  - admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_bounded_theorem_note_2026-08-10
  - admissibility_positive_two_stream_timelike_mean_dilation_zero_mode_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py
---

# Compact Regge Homogeneous Reaction Rank And KKT Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** exact compact reaction-rank theorem, constructive variational
completion, and corrected axiom obligation
**Scope:** the supplied flat periodic four-dimensional Kuhn/Coxeter 15-edge
carrier at `k=0`, the Block-15/16 positive source generators, and the linear
KKT systems stated below.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py](../scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py)

## Result Up Front

[Block 16](ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
proved that connected topology, unequal positive weights, and all `504`
binary bundle histories do not remove the positive compact homothety charge.
It therefore left a “compact scale-mode mechanism” as the next geometry
obligation. That description was directionally correct but too coarse.

The actual compact equation has eleven null directions, not one. Let

    Q_0 = Q_R(k=0),       K = ker Q_0,       P_K = orthogonal projector onto K.

The supplied Regge theorem gives

    dim K = 11 = 10 constant-metric modes + 1 nonmetric flat branch.       (1)

For a matrix `S` whose columns are the sources a model permits, define its
compact reaction rank

    r(S) = rank(P_K S).                                                   (2)

The exact result is:

1. the fixed per-step tick-plus-face source used by the Block-15 two-stream
   and Block-16 bouquet has `r=1`;
2. the two matched Block-16 bundle endpoints `A,B`, hence every compact mean
   of all `504` binary histories, have `r=2`;
3. the combined source family `[s_tf,A,B]` has `r=3`;
4. all eight future-temporal actual-edge rays have `r=8`; and
5. all fifteen actual-edge rays have `r=11`.

Thus the declared families have exact ranks one, two, and three, while a
source-agnostic actual-edge compact law reaches ranks eight and eleven.

The crucial correction is stronger than a count. A pure homothety reaction is
not aligned with the null projection of even the fixed tick-plus-face source.
After the best scalar homothety cancellation, the squared null residuals for
`s_tf,A,B` are exactly

    133/24+3sqrt(2)/4,       15/2,       27/4,                         (3)

respectively. All are strictly positive, and the three residual columns remain
rank three. “One source needs one reaction” therefore does **not** mean “one
scale constraint works”: the one reaction for a fixed source must be aligned
with that source's complete null projection.

Nor is arbitrary metric scale-plus-shape reaction enough on this carrier. An
exact unit vector for the nonmetric flat branch, orthogonal to all ten
constant-metric modes, is

    g = (1/8)(-sqrt(2),-sqrt(2),0,-sqrt(2),0,0,sqrt(6),-sqrt(2),
              0,0,sqrt(6),0,sqrt(6),sqrt(6),-4sqrt(2)).                 (4)

Its source pairings are

    g.s_tf = -sqrt(2)/4,       g.A = 0,       g.B = 3sqrt(2)/4.         (5)

Hence a reaction map confined to constant-metric scale and shape cannot close
the tick-plus-face or `B` equations. It must either react to/lift the extra
branch, change the operator, change the compact domain, or supply an equivalent
background/curved/nonlinear equation.

There is also a positive theorem. For every finite source family `S`, exactly
`r(S)` source-aligned mixed reaction channels make every compact equation
solvable. Applied here, three mixed reactions close the declared combined
linear equations. A physically clearer sector-separated construction uses
four reactions—three in the constant-metric sector and one along `g`. A full
eleven-reaction map makes the complete KKT matrix nonsingular and fixes all
homogeneous modes. These are mathematical constructions, not a physical
selection of their constraint functions or targets.

The axiom consequence is therefore precise: a candidate compact completion
must state full null-projection coverage and what happens to the nonmetric
branch. “Fix the scale” alone is insufficient. No canonical axiom is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional reaction-rank theorem, exact source-family ranks and residuals, and constructive variational KKT completions on the supplied compact Regge carrier; physical action, reaction selection, boundary/background, curved/nonlinear dynamics, coupling, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "construct and physically select one combined Record-history-plus-geometry action whose allowed source family and homogeneous reaction gradients/targets satisfy complete null-projection coverage, or whose curved nonlinear lifted background or open boundary removes that obligation, while also deriving constituent-causal rank-one matter, action unit, geometry update, coupling sign and orientation, Lorentzian and nonlinear equations, projective completion, and realized history; independently close the Born functional and program selector"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Derive the homogeneous reaction map and targets from one physical combined action, or construct a curved/nonlinear or lifted equation that removes the flat compact residual without editing the canonical axioms."
conditional_surface_status: "On the supplied flat periodic quadratic carrier, the declared source generators have exact reaction ranks one, two, and three; pure homothety fails all three generators, metric-only reactions miss the independent extra branch for two generators, and exact three/four/eleven-channel KKT constructions give family existence, sector-separated existence, or full homogeneous uniqueness."
hypothetical_axiom_status: "The candidate geometry-indexed history/action amendment is sharpened to require complete compact null-projection coverage, explicit constant-metric versus nonmetric-branch treatment, variational reactions, and existence-versus-uniqueness typing; it remains sufficient, unadopted, nonminimal, and replaceable by a downstream convention."
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target Contract And Obligation Graph

**Exact target.** Starting from the Block-16 compact positive-source
separator, determine the complete homogeneous compatibility space of the
supplied Regge equation, prove the minimum number of variational reactions
needed for every declared source, and state exactly what remains before that
mathematical completion is physical or axiom-level.

| Obligation | Evidence class | Disposition |
|---|---|---|
| identify the complete `k=0` null space of the supplied Hessian | cited carrier theorem plus actual-Hessian reconstruction | closed at dimension eleven: ten metric directions plus one nonmetric flat branch |
| prove a source-family lower bound on reaction count | exact linear algebra | closed by `rank(P_K S)` and equation (14) |
| prove the lower bound is sharp for solvability | exact Moore-Penrose construction | closed for every finite declared source family |
| distinguish solvability from unique homogeneous response | exact KKT rank criterion | closed; family existence needs `r(S)`, while source-agnostic uniqueness needs all eleven null directions here |
| compute the declared source-family ranks | exact radical matrices and nonzero minors | closed at `1/2/3`, with broad-ray controls `8/11` |
| test the proposed scalar homothety implementation | exact best-projection residuals and rank control | closed negatively for `s_tf,A,B`; this is not a universal compact-gravity claim |
| test arbitrary constant-metric scale-plus-shape reactions | exact orthogonal extra-branch vector and source pairings | closed negatively for `s_tf` and `B` on the retained carrier |
| construct honest variational completions | actual unprojected KKT solves | closed mathematically at three mixed, four sector-separated, and eleven full-null channels |
| derive constraint functions, targets, and source map from one physical action | physical selection lemma | open; no current axiom or approved primitive supplies it |
| replace the flat compact equation by a derived curved/nonlinear, lifted, background, fixed, or open-boundary equation | alternate physical completion | open and explicitly live |
| establish constituent-causal rank-one matter, coupling, Lorentzian continuation, nonlinear dynamics, Born law, and realized history | downstream TOE closure | open and outside this theorem |

**Strongest missing lemma.** One selected combined Record-history and geometry
action must derive either a reaction image covering the complete null
projection of every allowed compact source, with targets and
existence-versus-uniqueness semantics fixed, or a physically derived equation
whose boundary, background, curvature, nonlinearity, or lifted operator
removes that compatibility obligation.

## 1. Exact Zero-Mode Carrier

Let `M_0` be the actual line-averaged edge-to-metric map at zero momentum. Its
columns correspond to the ten symmetric constant metric components

    xx, yy, zz, tt, xy, xz, xt, yz, yt, zt.                              (6)

For an edge direction `d` of Euclidean length `|d|`,

    (M_0 h)_d = d^T h d / (2|d|).                                        (7)

The [actual Regge second-variation theorem](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
establishes that these ten columns are in `ker Q_0`, and that one independent
nonmetric branch is also exactly flat. Direct exact algebra gives

    rank M_0 = 10,
    rank [M_0,e_1111] = 11,                                               (8)

where `e_1111` is the unit coordinate vector of the body-diagonal edge class.
The actual numerical Hessian has rank four and annihilates all eleven columns
to the runner tolerance. Thus `[M_0,e_1111]` is a complete, not necessarily
orthogonal, null basis.

The vector `g` in (4) is the normalized orthogonal complement of `im M_0`
inside that null space. Exact arithmetic gives

    g^T g=1,       M_0^T g=0,       Q_0 g=0.                              (9)

The last equality is checked against the actual Hessian rather than inferred
from a continuum approximation.

## 2. General Reaction-Rank Theorem

Consider the variational linear system

    Q h + C lambda = -s,
    C^T h = 0,                                                            (10)

where `Q` is real symmetric, `C` contains gradients of declared homogeneous
constraints, and `lambda` contains their reaction multipliers. Let `N` be any
full-column basis of `ker Q` and let `S` contain every source in the declared
linear family.

### Theorem

Every source column of `S` can satisfy the first equation of (10) only if

    image(N^T S) is contained in image(N^T C).                            (11)

Consequently

    number of reaction columns >= rank(N^T S)=rank(P_ker(Q) S).           (12)

The bound is sharp for existence. Let

    R=P_ker(Q) S                                                         (13)

and retain an independent column basis of `R` as `C`. Then each source's null
component is a linear combination of the columns of `C`. After the
corresponding reaction is included, the remaining source lies in `image Q`.
Taking the Moore-Penrose response in `image Q` also satisfies `C^T h=0`, since
`C` lies in `ker Q`.

### Proof

Left-multiply the first equation of (10) by `N^T`. Since `N^T Q=0`,

    N^T C lambda = -N^T s.                                                (14)

This proves (11) and the dimension lower bound. Conversely, set `C` to a basis
of `image(P_K S)`. Choose `lambda` so `C lambda=-P_K s`. Then

    s+C lambda=(I-P_K)s is in image Q.                                    (15)

The response `h=-Q^+(s+C lambda)` solves the first equation, belongs to
`image Q`, and is therefore orthogonal to `C`. This proves sharpness. `□`

This theorem concerns **existence** for a declared source family. It does not
say the remaining homogeneous response is unique. The KKT block matrix is
nonsingular only when `N^T C` has full rank `dim ker Q`; on the current carrier
that requires eleven independent reactions. A model must say whether its
compact rule guarantees source solvability or actually fixes every
homogeneous mode.

## 3. Exact Declared Source Ranks

Write `t=(0,0,0,1)` and `f=(1,0,0,1)`. Because the edge source is the
derivative of `2(ell_d-|d|)`, the per-step source of both the disjoint
two-stream and connected bouquet is

    s_tf = 2e_t+2e_f.                                                      (16)

The matched bundle endpoints from Block 16 are

    A_d=2sqrt(2) for spatial Hamming weight one,
    B_d=3 for weight zero and sqrt(3) for weight two,                       (17)

with all other entries zero.

Since `[M_0,e_1111]` is a full null basis, `rank(P_K S)` equals the rank of
the null-pairing matrix

    [M_0,e_1111]^T S.                                                      (18)

For `S=[s_tf,A,B]`, the rows `xx,yy,xy` and the three source columns contain
the triangular minor

    [ sqrt(2)/2   1   1 ]
    [     0       1   1 ]
    [     0       0   1 ],                                                (19)

whose determinant is `sqrt(2)/2`. Therefore the combined reaction rank is at
least three and, because there are only three columns, exactly three.

For `[A,B]`, the `xx,xy` minor is

    [ 1  1 ]
    [ 0  1 ],                                                             (20)

with determinant one. Thus the bundle rank is exactly two. Every one of the
`504` binary-history compact means is a convex combination of `A` and `B`, and
the family includes both endpoints, so its linear reaction span is exactly
the same two-dimensional space.

For `s_tf`, its `xx` pairing is `sqrt(2)/2`, so its rank is one. The runner
also computes the larger source-family ladder:

| Declared compact family | Exact reaction rank |
|---|---:|
| fixed tick-plus-face two-stream or bouquet | 1 |
| all `504` matched-bundle history means | 2 |
| combined `[s_tf,A,B]` family | 3 |
| all eight future-temporal actual-edge rays | 8 |
| all fifteen actual-edge rays | 11 |

The last two rows are not claims that the axioms select those broad source
families. They show how the required reaction dimension depends on the
quantifier a future model chooses.

## 4. Why Homothety Alone Fails

Let

    z=M_0 diag(1,1,1,1)                                                   (21)

be the Block-16 positive homothety. A one-column scale reaction can supply only
`span{z}`. For a source `s`, its best possible scalar cancellation removes the
orthogonal projection of `P_Ks` onto `z`; the residual is

    rho_z(s)=P_Ks-z(z^T P_Ks)/(z^Tz).                                     (22)

Exact radical arithmetic gives equation (3). In addition,

    rank[rho_z(s_tf),rho_z(A),rho_z(B)]=3,
    rank[P_Ks_tf,P_KA,P_KB,z]=4.                                         (23)

So adding a homothety column to the three source null projections adds a new
direction; it does not replace any of them. For one fixed `s_tf`, one scalar
reaction still suffices by the theorem, but its gradient must be proportional
to `P_Ks_tf`, not to `z`. That distinction is the difference between a count
of channels and a physical identification of the channel as volume/scale.

For the bundle family there is an even simpler witness. `A-B` has zero
homothety charge because both endpoints have charge six, but its constant
metric source is nonzero pure spatial shear. A reaction whose only gradient is
`z` gives the same scalar response to `A` and `B` and cannot cancel their
nonzero difference.

This is a narrow algebraic rejection of one proposed implementation on the
named flat compact carrier. Open boundaries, fixed full geometry, background
counterstress, curved solutions, nonlinear constraints, changed actions, and
alternate carriers remain live.

## 5. Why Metric Scale Plus Shape Is Still Incomplete

One might respond to Section 4 by allowing all constant-metric shape
constraints, not only volume. Equation (5) shows why that is still incomplete
for this carrier. Every such reaction lies in `im M_0` and is orthogonal to
`g`, while `s_tf` and `B` have nonzero `g` pairing.

This nonmetric residual is the same exactly flat lattice branch already named
by the Regge source theorem and probed by the Block-14 explicit algebraic lift.
It is not a new physical degree of freedom claimed by this note. The exact
lesson is conditional:

- if the current quadratic carrier is retained, the compact reaction map must
  include the branch or an equivalent equation must cancel it;
- if the geometry action lifts that branch, the reaction need not remain; and
- if the compact zero mode is removed by domain/boundary choice, neither this
  reaction nor the metric reactions are required for that changed problem.

Calling the residual “shape” without distinguishing metric shape from the
nonmetric flat branch would hide one load-bearing obligation.

## 6. Constructive KKT Completions

The reaction-rank theorem gives three exact completion levels.

### 6.1 Three mixed reactions: existence for the declared combined family

Take

    C_3 = independent columns of P_K[s_tf,A,B].                            (24)

Then `rank C_3=3`, `Q_0C_3=0`, and each of the three source generators has a
reaction multiplier that cancels its full null projection. The actual runner
solves the unprojected equations

    Q_0h+C_3lambda=-s,       C_3^Th=0                                    (25)

for all three generators. Linearity covers every declared combination. This
is minimal for existence by (12).

The construction is source-aligned. It proves mathematical sufficiency but
does not explain why a physical constraint action would select these three
gradients.

### 6.2 Four sector-separated reactions: metric plus extra branch

Decompose each source null projection into its constant-metric and `g`
components. The three metric projections are independent; their span plus `g`
has dimension four. This gives

    C_4=[P_metric P_Ks_tf, P_metric P_KA, P_metric P_KB, g].               (26)

The same KKT equations solve all three generators. This construction is not
dimension-minimal, but it makes the carrier obligation legible: three metric
reaction combinations and one extra-branch reaction.

### 6.3 Eleven reactions: unique full homogeneous response

Let `C_11` be any basis of `ker Q_0`. Then

    [ Q_0   C_11 ]
    [ C_11^T  0  ]                                                       (27)

has full rank `26`. It gives a unique response and multiplier vector for every
15-edge source. On the present carrier, this is the source-agnostic complete
homogeneous fixing. It is much stronger than the three-channel existence
result and should not be silently inferred from it.

These are genuine variational reactions because `C lambda` remains visible in
the equation and `C^Th=0` is imposed simultaneously. They are not a post hoc
Fourier projection that deletes the source before variation. A physical model
must still derive or declare the constraint functionals, their targets, and
their membership in the same action as the source.

## 7. Exact Axiom And Convention Update

The current Lattice, Qubit, Admissibility, and Record axioms are unchanged.
They do not select a source/action, history law, geometry carrier, constraint
reaction, boundary condition, or dynamics. The approved scale-reference
primitive supplies units only; the kinetic-isotropy primitive supplies equal
OS0 graining only; the realized-state primitive supplies pointwise evaluation
only.

The existing candidate **Geometry-indexed history/action amendment** in
[Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
already says that each model declares an open, boundary-fixed,
background-subtracted, or globally constrained zero-mode ensemble. Block 17
shows that “globally constrained” needs a stronger implementation contract.

### Candidate amendment delta

Append the following to that candidate wording:

> **Compact homogeneous reaction clause.** For every selected compact history
> source family, the same geometry-indexed action registers either (i) a
> boundary/background/curved or lifted equation with no compact compatibility
> residual, or (ii) one covariant homogeneous constraint map and its
> variational reaction variables. In case (ii), the reaction image contains
> the complete null projection of every allowed source. The specification
> distinguishes constant-metric scale and shape from any independent
> nonmetric flat branch, and states whether it guarantees only source-family
> existence or fixes the full homogeneous response. Reactions enter the
> combined variational equations and are not a post hoc source projection. The
> same specification fixes the constraint targets, source map, action unit,
> boundary sector, and realized-history compatibility.

This is sufficient candidate wording, not adopted wording. It is not proved
necessary or minimal as a foundation amendment. A downstream model convention
can declare exactly the same action and compact sector without changing the
four axioms. Other actions may have a different null space or no corresponding
compact obstruction.

### Exact model-specific requirement

For the current flat quadratic carrier and the declared source family, the
clause specializes to either:

- at least three mixed reaction channels for existence;
- four channels in the displayed metric/extra-branch separated construction;
- eleven channels for unique full homogeneous fixing; or
- an explicitly different boundary, background, curved/nonlinear, lifted, or
  alternate-carrier equation.

The candidate should therefore no longer say or imply that a scalar scale
constraint by itself completes this source family.

## 8. TOE Lane Consequence

| Lane | Exact Block-17 advance | Still open |
|---|---|---|
| operational quantum / records | converts “compact mechanism” into a typed variational source/reaction interface | Record-to-source identity, action and constraint selection |
| causal time | all `504` history means share an exact two-reaction compact span | causal update, constituent-causal carrier, formation site/rate |
| inertia / matter | separates common timelike aggregate current from independent homogeneous load channels | rank-one matter, mass/inertia identification, dressing |
| gravity / source / resources | proves the minimal reaction-rank theorem, exact `1/2/3/8/11` ladder, homothety failure, extra-branch obligation, and constructive KKT completions | physical compact action, targets, sign/coupling, curved/nonlinear and Lorentzian completion |
| Born probability / realized history | tells a future history law exactly what compact compatibility every allowed source must satisfy | Born functional/program selector and realized-history selection |

This is significant new gravity progress because it changes the required
completion architecture: scale-only is replaced by full null-projection
coverage plus explicit extra-branch treatment. It still does not select a
physical law. Under the campaign's fixed rubric, the fixed TOE percentages
remain unchanged.

## 9. Relation To Existing Sources

The following table is also the import ledger. Its middle column states the
only imported content; its right column records the non-imports that remain
open. All numerical ranks, minors, residuals, source pairings, and KKT ranks
claimed by this note are rederived in the primary runner. No external source
is used.

| Source | Exact use | Boundary preserved |
|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | current foundation boundary | no action, constraint, history, geometry, or dynamics imported |
| [Scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) | confirms that “scale” as units is distinct from a compact variational constraint | no dimensionless dynamics or zero-mode reaction supplied |
| [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | equal-form tick graining | no action, reaction map, source weight, or Lorentz theorem supplied |
| [Realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | pointwise realized-state interface | no history or constraint selection supplied |
| [Block 12](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | existing candidate action/history/compact-ensemble wording | candidate remains unadopted and nonminimal |
| [Block 15](ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | positive tick-plus-face source and homothety separator | no compact reaction derived there |
| [Block 16](ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | bundle endpoints, `504` histories, connected bouquet, scale-mechanism residual | no physical constraint or extra-branch law imported |
| [Actual Regge Hessian](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | `Q_0`, `M_0`, ten metric zeros, one extra flat branch | carrier/action selection and nonlinear physics remain supplied |

No external literature value, observed target, fitted coefficient, or
continuum Einstein equation is used.

## 10. No-Go Discipline Gate

The negative statement is only this: on the named flat compact quadratic
carrier, a reaction whose only column is the Block-16 homothety does not solve
the declared source generators, and reactions confined to constant-metric
scale and shape do not cancel the displayed nonmetric branch overlaps. No
universal compact-gravity no-go is claimed.

### N1 — alternative route enumeration

Approach families are normalized by primary object, mechanism, and terminal
obligation.

| Route | Attempt and result | Marker |
|---|---|---|
| source-aligned KKT reaction | Use `C=P_KS`; three mixed columns solve the declared combined family exactly, so compact closure is possible but is not a homothety-only law. | ATTEMPTED |
| metric/extra sector separation | Use three constant-metric source projections plus `g`; four columns solve exactly and expose the extra-branch obligation. | ATTEMPTED |
| full homogeneous fixing | Use all eleven null directions; the `26x26` KKT matrix is nonsingular for every source, but this imports a full compact constraint choice. | ATTEMPTED |
| open or fixed-global domain | Remove the compact normalizable zero mode or remove all constant variations; the included Block-13--15 constructions solve the changed-domain equations. | ATTEMPTED; not a refutation of the fixed-domain theorem and a live completion |
| signed/background counterstress | Add a fixed source offset that cancels the common load and can reduce the variable reaction rank; the included Block-14 signed pair proves this route is live but changes the nonnegative bare-source premise. | ATTEMPTED; not a refutation and a live completion |
| lifted geometry operator | Lift the nonmetric branch or other homogeneous modes; the included Block-14 algebraic lift proves operator changes can remove a null obstruction. | ATTEMPTED; not a refutation and a live completion |
| curved/nonlinear combined solution | Expand about a source-supported curved background so the flat `Q_0` compatibility equation is not the field equation; this remains unexecuted and is expressly outside the theorem. | ATTEMPTED as an obligation analysis; remains open |
| alternate source carrier/action | Change the edge representative or matter/geometry action so its compact null projection differs; the theorem makes no claim about that changed `Q,S` pair. | ATTEMPTED as an obligation analysis; remains open |

There are more than five distinct routes, and several give explicit positive
completions after changing or augmenting the premise. They defeat every broad
no-go but not the exact rank and inclusion statements for the fixed `Q_0,S`.

### N2 — wall-independence audit

For physical TOE closure, the collapsed open-condition set is:

- `W1`: select the Record/history-to-source map, source family, network action,
  weights, and action unit;
- `W2`: select one complete compact homogeneous equation—reaction map and
  targets, boundary/background, curved solution, lift, or alternate carrier—
  covering both metric moduli and the extra branch when present;
- `W3`: select a constituent-causal/rank-one matter carrier or derive why the
  aggregate source is the physical matter object; and
- `W4`: select geometry dynamics, coupling sign/size, Lorentzian continuation,
  and nonlinear completion.

The extra-branch obligation is part of `W2`, not inflated into a fifth wall.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W1,W2` | no; a selected source can retain a compact residual | no; a constraint map does not select the source law | yes |
| `W1,W3` | no; a selected network may remain rank two or contain spacelike edges | no; causal matter does not select Record/source weights | yes |
| `W1,W4` | no; a matter action does not determine geometry dynamics/coupling | no; geometry dynamics does not select the matter history | yes |
| `W2,W3` | no; a compact reaction does not make constituents causal | no; causal matter may still carry homogeneous load | yes |
| `W2,W4` | no; a finite-dimensional compact rule does not supply nonlinear/Lorentzian dynamics | no; a geometry law must still specify its compact sector | yes |
| `W3,W4` | no; a causal source does not fix its gravitational equation | no; geometry dynamics does not choose the realized matter carrier | yes |

Born/program selection and the realized member remain separate downstream TOE
lanes; they are not load-bearing in the reaction-rank proof.

### N3 — hidden-condition scan

The source was searched for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| flat background / compact domain | explicit theorem domain, not a hidden physical premise |
| registered action/reaction language | candidate wording in Section 7, explicitly unadopted and not used as authority |
| background reaction routes | explicit changed-premise alternatives in N1/N6 |
| canonical axiom | governance nonmutation statement, non-load-bearing |
| all other scan phrases | absent outside this literal checklist |

The actual `Q_0`, edge coordinates, source generators, Euclidean inner
product, and linear constraint form are all explicit. No hidden condition was
promoted after the scan.

### N4 — residual matching

| Witness | Witness residual | Present residual | Match? |
|---|---|---|---|
| `docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:244` | positive tick-plus-face source has nonzero homothety pairing | same `s_tf`, now resolved against the full eleven-null space | yes |
| `docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:404` | all positive network means remain outside bare `image Q_0` | same source generators; rank theorem identifies required reaction image | yes |
| `docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:43` | ten metric zeros plus one extra flat branch at `k=0` | equation (1) and exact `g` | yes |
| `docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:354` | one explicit changed operator removes an extra-null residual | N1/N6 preserve lift as an escape, not as proof of current closure | yes |
| `docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:510` | fixed/open/background/constrained choice remains unselected | Section 7 strengthens only the constrained implementation obligation | yes |

No Poisson surrogate, continuum gauge count, fitted coupling, or unrelated KKT
optimization is cited as a witness.

### N5 — rhetoric audit

| Resolution | Executed statement | Scope not claimed |
|---|---|---|
| per element | all fifteen actual-edge rays, eight temporal rays, and exact `g` | no alternate carrier or arbitrary matter functional |
| per site | all `504` binary histories through their compact mean source | no local causal routing or formation rule derived here |
| per mode | the actual `k=0` Hessian, its eleven-dimensional null space, and unprojected KKT equations | no nonzero-mode re-audit or continuous curved spectrum |
| per block | general rank theorem, exact rank ladder, scale residuals, and three/four/eleven-channel constructions | no physical selection of the constraints |
| lattice wide | the complete declared compact source families on the periodic homogeneous sector | no open, curved, nonlinear, background, or alternate-carrier no-go |

The cached stdout lands one substantive execution-certificate line at each
resolution. “Insufficient” is used only for the pure homothety or
constant-metric reaction subspaces against the explicitly declared sources.

### N6 — partial-closure paths

The approved primitive registry was read directly. Scale reference, kinetic
isotropy, and realized-state evaluation are accepted premises but supply no
constraint or source selection.

| Candidate path | Status | What it closes |
|---|---|---|
| three mixed KKT reactions, this note | exact mathematical construction | existence for `[s_tf,A,B]` with minimal channel count |
| four sector-separated reactions, this note | exact mathematical construction | exposes metric versus extra-branch handling |
| eleven full-null reactions, this note | exact mathematical construction | unique full homogeneous response for any edge source |
| fixed-global/open domain, Blocks 13--15 | existing conditional route | removes the corresponding compact compatibility equation |
| signed/background source, Block 14 | existing bounded route | cancels total compact load after changing source-sign premise |
| lifted operator, Block 14 | existing algebraic route | removes the named extra branch after changing the operator |
| Block-12 downstream convention | existing conditional path | declares action and compact ensemble without an axiom edit |
| candidate amendment delta, Section 7 | unadopted sufficient wording | makes full null coverage and uniqueness-versus-existence explicit |

It would be incorrect to say “a new axiom is required.” The result identifies
what an autonomous foundation amendment would need to supply; a downstream
model convention or changed boundary/operator can supply it instead.

### N7 — steelman

A hostile reviewer should argue that the phrase “scale constraint fails”
attacks a caricature: compact general relativity is governed by a coupled set
of Hamiltonian, momentum, and global moduli equations, not a lone multiplier
attached to the Euclidean identity metric. A background curvature or
cosmological term can balance the integrated source, and the extra lattice
branch should be lifted by the full nonlinear action rather than constrained
as matter. The strongest repository support is Block 14's explicit branch
lift and signed/fixed-global solutions plus Block 12's combined-action
candidate. This is a concrete, mathematically actionable objection to every
broad physical reading. The note accepts it: Sections 6--7 describe coupled
reaction/lift/background routes, and no physical no-go survives. It does not
refute the narrow calculation that `span{z}` and `im M_0` fail the stated
linear inclusion tests for the fixed flat `Q_0,S`.

### N8 — cross-cycle echo

| Similar prior wall | Later mechanism / lesson here |
|---|---|
| Block 12 localized source residuals | Block 13 changed the local improvement and retired nonzero-mode residuals; current source/action choices remain live |
| Block 13 compact tick charge | Block 14 supplied signed and fixed-global ensembles; compact boundary choice is not a universal no-go |
| Block 14 extra-null body-edge residual | Block 14's explicit lift removed it algebraically; the extra branch is operator-dependent |
| Block 15 disjoint positive source | Block 16 supplied connected and switching networks; topology did not solve compact rank but retired the connectivity wall |
| earlier source/action “axiom” walls | downstream convention and import-retirement paths separated model choice from foundation amendment; Section 7 preserves that distinction |

Every known retirement mechanism—new source representative, connected
history, signed/background term, fixed/open domain, operator lift, downstream
convention, and candidate ratification—is considered. None is silently
foreclosed.

**Gate status:** PASS for the pure-homothety and metric-only subspace failures
against the fixed `Q_0,S`, and for the exact constructive rank theorem. FAIL
for any universal compact-gravity, all-action, all-boundary, curved/nonlinear,
or “new axiom required” interpretation.

## 11. Promotion Value And Cluster-Cap Gate

- **V1 — specific hard residual:** Block 16 names a compact scale-mode
  mechanism as the leading gravity root. This note replaces it with an exact
  minimum-rank and branch-coverage obligation.
- **V2 — novelty:** a search of `origin/main@39c74017b870c27c804e3992f2a11e90336476b2`
  and current open PR titles found generic KKT uses but no homogeneous
  reaction-rank theorem, no `rank(P_KS)` source criterion, and no collision
  with the Block-15/16 source family.
- **V3 — proof grade:** the lower bound and sharpness proof are exact linear
  algebra; all source ranks and radical residuals are exact; actual-Hessian
  KKT residuals independently check the construction.
- **V4 — no fitted input:** no observation, target value, scalar fit,
  continuum field equation, or external literature constant is used.
- **V5 — compression:** the `1/2/3/8/11` rank ladder and
  existence-versus-uniqueness split replace the vague phrase “scale
  mechanism” and prevent an under-specified axiom update.

**Cluster-cap evaluator verdict: `OPEN`.** This is Block 17 in one stacked
campaign, so the marginal-review burden is high. It nevertheless introduces a
new load-bearing theorem rather than applying an old result to another label:
the minimum reaction dimension is the rank of the complete null projection,
and the actual declared family has rank three. It also falsifies the specific
scalar-homothety completion suggested by the prior handoff, isolates a
previously hidden nonmetric-branch obligation, and constructs exact
three/four/eleven-channel variational completions. Review can independently
check one general proof, one triangular exact minor, three radical residuals,
three extra-branch pairings, and three KKT ranks. The result materially changes
candidate axiom wording and the next geometry target, so it is not corollary
churn. It remains bounded support and seeks no audit verdict.

### Direct review record and hard landing conditions

This block is inspected directly under the repository conformance contract;
the landing-only `review-loop` is not invoked. The reviewer must reconstruct
the rank theorem and declared-source matrices without importing this runner,
execute one load-bearing mutation per check family, verify source-bound cache
freshness and the citation-graph delta, and run the exact-base integration
pipeline in an isolated worktree. The block may be proposed only if the
primary runner, independent reconstruction, mutations, lint, link checks,
changed-evidence checks, and cold integration have zero unexplained failures.
Any failure demotes the block to an unlanded working note; no audit status or
canonical axiom wording may be changed by this branch.

## 12. Verification

Run:

    python3 scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py

The runner checks:

- current-axiom and approved-primitive boundaries;
- actual `rank Q_0=4`, nullity eleven, metric rank ten, and one extra branch;
- exact source ranks one, two, three, eight, and eleven;
- the nonzero `sqrt(2)/2` rank-three minor;
- all `504` binary-history means in the two-reaction span;
- the three exact best homothety residual norms;
- the exact normalized `g` and its three source pairings;
- minimal three-channel, sector-separated four-channel, and unique
  eleven-channel KKT constructions on the unprojected actual Hessian;
- a one-source aligned-channel control and a rank-two deletion negative
  control;
- N1--N8, candidate wording, canonical-axiom nonmutation, fixed rubric, and
  all five resolution certificates.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    positive connected/balanced source family
      -> exact eleven-dimensional compact null space
      -> source-family reaction rank r(S)
      -> exact ranks 1/2/3 for the declared generators
      -> pure homothety failure
      -> independent nonmetric-branch overlap
      -> constructive 3-channel existence
      -> constructive 4-channel sector separation
      -> constructive 11-channel unique homogeneous fixing.

This is significant progress. It proves that the remaining compact gravity
problem is not adequately specified as one scale mode and gives the exact
finite-dimensional variational architecture that would close the current
linear carrier. It does not derive why Nature selects any of those constraint
maps, targets, source generators, boundaries, actions, or couplings. Curved
and nonlinear geometry remains the highest-value physical route. No canonical
axiom is edited, no universal no-go is claimed, and the fixed TOE percentages
remain unchanged.

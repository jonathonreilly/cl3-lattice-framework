---
claim_id: admissibility_nonlinear_regge_extra_branch_cubic_lift_source_compatibility_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the actual homogeneous four-dimensional Kuhn/Coxeter Regge action per periodic translation cell and the exact unit nonmetric zero vector g isolated in the parent compact-reaction theorem, the action along l(t)=l_flat+t g has exact Taylor expansion S_R(tg)=-4 sqrt(2) t^3+(4023/256)t^4+O(t^5). Thus g is flat only through quadratic order and is natively lifted at cubic order. On the full eleven-dimensional quadratic null space written as M_0 x+u g, the complete cubic polynomial is 8u^2(x_xy+x_xz+x_xt+x_yz+x_yt+x_zt)-4sqrt(2)u^3; all u x_i x_j and pure-metric cubic coefficients vanish. Its leading metric-gradient image is the single shear covector span(0,0,0,0,1,1,1,1,1,1), and the three declared Block-15/16 compact source metric covectors are exactly nonparallel to it. The source comparison is only a leading-cubic local boundary, not a no-go for the full nonlinear action, higher-order mixed branches, curved or inhomogeneous solutions, reaction constraints, alternate boundary/background sectors, or a physically selected geometry law."
upstream_dependencies:
  - minimal_axioms
  - admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py
---

# Nonlinear Regge Extra-Branch Cubic Lift And Source-Compatibility Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** exact nonlinear lift of the independent quadratic Regge zero branch,
complete cubic null-sector normal form, and corrected candidate axiom obligation
**Scope:** the homogeneous actual four-dimensional Kuhn/Coxeter Regge action,
its flat periodic translation cell, the exact `k=0` null space, and the three
declared compact source generators inherited from Block 17.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py](../scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py)

## Result Up Front

The [parent compact-reaction theorem](ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
found that the actual flat `k=0` Regge Hessian has rank four and nullity
eleven: ten constant-metric directions and one independent nonmetric branch.
It conservatively treated the latter as requiring either a reaction channel
or an unspecified nonlinear lift.

This block computes the actual nonlinear Regge action instead of adding a
projector. Let the exact unit extra branch be

    g = (1/8)(-sqrt(2),-sqrt(2),0,-sqrt(2),0,0,sqrt(6),-sqrt(2),
              0,0,sqrt(6),0,sqrt(6),sqrt(6),-4sqrt(2)).                 (1)

For homogeneous edge lengths `ell(t)=ell_flat+t g`, the exact action per
translation cell is

    S_R(tg) = -4sqrt(2) t^3 + (4023/256)t^4 + O(t^5).                  (2)

The constant, linear, and quadratic coefficients vanish exactly. The cubic
coefficient does not. Therefore `g` is an exact zero direction of the
quadratic Hessian but is **not** an exactly flat direction of the actual
nonlinear action. The independent extra reaction introduced as one possible
Block-17 completion is not forced merely to lift `g`: the supplied Regge
action itself already lifts it at third order.

The stronger result is the complete cubic null-sector polynomial. Write a
general quadratic-null perturbation as

    delta ell = M_0 x + u g,                                           (3)

where `x` is ordered as

    (xx,yy,zz,tt,xy,xz,xt,yz,yt,zt).

Then

    P_3(x,u)
      = 8u^2(x_xy+x_xz+x_xt+x_yz+x_yt+x_zt) - 4sqrt(2)u^3.             (4)

There are no pure-metric cubic terms and every coefficient of `u x_i x_j`
is exactly zero. In particular,

    partial_x P_3
      = u^2 (0,0,0,0,8,8,8,8,8,8).                                   (5)

The inherited compact sources have metric covectors that are not parallel to
the vector in (5). That is a complete statement about the leading cubic
polynomial, not a full nonlinear source no-go. Quartic and higher terms,
finite-amplitude mixed branches, range-mode backreaction, curved or
inhomogeneous solutions, reaction constraints, and changed boundary or
background sectors remain live.

The corrected candidate amendment must therefore accept a demonstrated
native nonlinear lift as an alternative to an independent reaction, while
requiring a **complete coupled source-compatibility certificate** rather than
accepting one directional lift. No canonical axiom is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact algebraic-number-field Taylor coefficients, complete cubic null-sector polynomial, exact declared-source covectors, and a strictly scoped leading-cubic compatibility boundary on the supplied actual Regge carrier."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "derive and physically select one combined Record-history and geometry law whose full nonlinear, boundary, background, or variational-reaction equations admit the allowed source family with action unit, coupling orientation, Lorentzian dynamics, projective completion, and realized history; independently close the Born functional/program selector"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Compute the quartic and higher mixed null/range tensors or solve the complete nonlinear fifteen-edge source equations, preserving curved, inhomogeneous, boundary, and reaction routes."
conditional_surface_status: "The actual nonlinear Regge action natively lifts the independent quadratic extra branch at cubic order. Its complete cubic metric-gradient image is one shear covector and does not contain any of the three declared compact source metric covectors."
hypothetical_axiom_status: "The candidate geometry/history amendment now permits either complete variational null-reaction coverage or a demonstrated native nonlinear/boundary lift with full coupled source compatibility; it remains sufficient, unadopted, nonminimal, and absent from the canonical memo."
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target Contract And Obligation Graph

| Obligation | Evidence | Disposition |
|---|---|---|
| evaluate the actual nonlinear action along the exact extra branch | exact Taylor jets over all 50 hinges and 240 dihedral contributions per cell | closed through fourth order by (2) |
| prove the quadratic zero is genuinely lifted | exact nonzero cubic coefficient | closed locally; first nonzero coefficient is `-4sqrt(2)` |
| reconstruct the whole cubic polynomial on the 11-dimensional null space | exact polarization plus all seven coordinate-permutation orbits | closed by (4) |
| check the result against the actual periodic action | independent 70-digit reconstruction and direct `L=3` box action | closed at the declared samples and derivatives |
| identify the nondegenerate path domain | exact simplex Gram minors | connected interval around zero is approximately `(-0.4588602644,0.3401504091)` |
| compare the cubic gradient with declared sources | exact radical source covectors | closed by the nonparallel rank certificates below |
| solve the complete nonlinear sourced 15-edge equation | full nonlinear continuation/existence theorem | open; a one-direction or cubic-sector result is insufficient |
| derive physical action/source selection, unit, boundary, coupling, and history | current-axiom bridge | open |
| edit or adopt an axiom | owner governance | not attempted and not authorized |

**Strongest missing lemma.** For one selected source/history law, prove that
the complete nonlinear geometry equation—including any retained reaction,
boundary, background, or curvature terms—has the required solution family and
state whether the result is existence, local uniqueness, or stability.

## 1. Actual Homogeneous Regge Action

The calculation uses the actual action

    S_R = sum_T A_T delta_T,                                             (6)

on the four-dimensional Kuhn/Coxeter complex defined by the retained Regge
runner. One periodic translation cell has 50 triangle classes and 240
triangle-simplex incidences. For a homogeneous perturbation, each edge class
has one length and the per-cell action is the sum over those 50 classes.

No Schläfli-reduced surrogate is substituted for the action. Areas are
expanded from Heron's polynomial in squared edge lengths. Every dihedral
angle is reconstructed from the two-dimensional hinge projection in its
actual four-simplex. The flat deficit constant is zero; the nonconstant
`acos` Taylor coefficients are retained exactly.

All coefficients through fourth order lie in

    Q(sqrt(2),sqrt(3)).                                                   (7)

The primary route performs exact truncated-jet arithmetic in that number
field. An independent route evaluates the original areas and angles with 70
decimal digits and differentiates the assembled action.

## 2. Exact Directional Lift

Substitution of (1) into all 15 homogeneous edge lengths gives

| order | exact coefficient of `t^n` |
|---:|---:|
| 0 | `0` |
| 1 | `0` |
| 2 | `0` |
| 3 | `-4sqrt(2)` |
| 4 | `4023/256` |

The old phrase “exactly flat branch” is therefore accurate only as a
quadratic-Hessian statement. The action is odd at leading order:
`S_R(-0.02)>0` and `S_R(+0.02)<0`. The positive quartic term does not make
the origin a local minimum because the cubic term dominates on either side.
Flipping the overall Regge orientation reverses this statement but still
leaves a cubic inflection rather than a quadratic mass.

All 24 path simplices are congruent along this coordinate-symmetric branch.
The exact leading Gram determinants are positive on the connected interval
around zero bounded approximately by

    -0.458860264423508 < t < 0.340150409120162.                          (8)

Thus the Taylor result is obtained inside a genuine nondegenerate-simplex
neighborhood; it is not an expansion through an immediately invalid length
configuration.

## 3. Complete Cubic Null-Sector Polynomial

The 24 coordinate permutations preserve the full Kuhn path complex, all
triangle classes, and `g`, whose component depends only on edge Hamming
weight. Diagonal metric components form one orbit and off-diagonal components
form a second. Exact bivariate polarization gives

    coeff(u^2 x_aa) = 0,             a in {x,y,z,t},
    coeff(u^2 x_ab) = 8,             a<b.                              (9)

For the symmetric coefficient matrix of `u x_i x_j`, the 55 component pairs
fall into seven coordinate-permutation orbits of sizes

    4, 6, 12, 12, 6, 12, 3.                                            (10)

One exact representative from every orbit is zero. Therefore the full matrix
is zero, not merely numerically small.

There is also a geometric explanation. Let `L(H)` be the nonlinear edge-
length embedding of a constant positive metric. Every `L(H)` triangulates a
flat homogeneous geometry, so the full Regge gradient vanishes along that
manifold. Differentiating that identity twice gives

    T(M_i,M_j,w) + Q_0(N_ij,w) = 0.                                    (11)

For `w=g`, exact quadratic nullity gives `Q_0(N_ij,g)=0`; hence
`T(M_i,M_j,g)=0`. This independently explains the absent `u x_i x_j` sector.
Pure-metric cubic terms vanish by the same flat-family identity. Equations
(2), (9), and (11) yield the complete polynomial (4).

Its gradient is

    partial_x P_3 = u^2 b,
    partial_u P_3 = 16u sum_shear x_shear - 12sqrt(2)u^2,                (12)

where

    b=(0,0,0,0,8,8,8,8,8,8).                                          (13)

## 4. Exact Declared-Source Comparison

Let `p=M_0^T s` and `q=g^T s`. For the inherited sources
`s_tf,A,B`, exact arithmetic gives

| source | metric covector `p` in `(xx,yy,zz,tt,xy,xz,xt,yz,yt,zt)` | `q` |
|---|---|---:|
| `s_tf` | `(sqrt(2)/2,0,0,1+sqrt(2)/2,0,0,sqrt(2),0,0,0)` | `-sqrt(2)/4` |
| `A` | `(1,1,1,3,0,0,2,0,2,2)` | `0` |
| `B` | `(1,1,1,3,1,1,2,1,2,2)` | `3sqrt(2)/4` |

For each column,

    rank[b,p] = 2.                                                       (14)

Consequently none belongs to the one-dimensional metric-gradient image of
the complete cubic polynomial. The conclusion is deliberately narrow:

> the native cubic lift removes exact nonlinear flatness of `g`, but the
> complete cubic null-sector polynomial alone does not supply the declared
> metric source covectors.

This does not assert that the complete nonlinear Regge action lacks a sourced
solution. In a small-source Lyapunov-Schmidt scaling with null displacement
`O(sqrt(lambda))`, the four massive coordinates respond at `O(lambda)` and
cannot change the leading cubic metric-gradient image. But a higher-order
mixed branch with another scaling, a finite-amplitude solution, a curved or
inhomogeneous field, a boundary/background term, or the Block-17 variational
reactions can change the equation.

## 5. Independent And End-To-End Controls

The independent calculation does not import the exact-jet coefficients. It
reassembles every area and angle with `mpmath` at 70 digits and differentiates
the result. Its errors against the five exact coefficients through order four
are below `1e-55`.

The original retained `box_action` is then run on an actual periodic `L=3`
four-torus. Dividing its 81-cell value by 81 agrees with the independently
assembled homogeneous action at `t=0.02` within the declared double-precision
tolerance. This checks the per-cell incidence accounting against the original
periodic implementation.

## 6. Exact Candidate Axiom And Convention Update

The Block-17 candidate wording required full null-projection coverage and
explicit treatment of the extra branch. Equation (2) sharpens, but does not
delete, that obligation.

### Candidate amendment delta

Candidate wording, **not adopted**, is:

> For every registered compact source/history sector, the selected geometry
> law shall establish at least one of the following on its declared boundary
> and background domain: (a) variational reaction gradients whose null
> projections cover the complete allowed source family, with their targets
> and existence-versus-uniqueness semantics stated; or (b) a retained
> nonlinear, curved, background, or boundary mechanism that lifts the
> relevant quadratic null branches and proves compatibility of the complete
> coupled equations with that source family. A directional branch lift alone
> is not a complete source-compatibility certificate. The action
> representative and unit, coupling orientation, Lorentzian continuation,
> stability criterion, projective history law, and realized member shall be
> stated separately.

This wording corrects one overconstraint in the earlier draft: an independent
reaction along `g` is no longer mandatory if the actual nonlinear action is
the selected lift. It also prevents the opposite overreach: the nonzero cubic
coefficient alone does not certify complete source compatibility.

The clause is sufficient rather than proved necessary or minimal. It is not
inserted into `MINIMAL_AXIOMS_2026-06-29.md`.

## 7. TOE Lane Consequence

This is significant gravity-lane science:

1. one of the eleven quadratic zero directions is now natively lifted by the
   actual retained nonlinear action;
2. the lift order, sign, quartic correction, and complete cubic mixing tensor
   are exact; and
3. the remaining source mismatch is a specific covector-image problem rather
   than the vague phrase “extra branch treatment.”

The fixed TOE percentages remain unchanged. The result supplies a conditional
nonlinear mechanism but does not select the action physically, solve the full
sourced nonlinear equations, derive coupling/Lorentzian/history data, or
cross a fixed-rubric threshold.

## 8. Relation To Existing Sources

- The [actual Regge second-variation theorem](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
  supplies the complex, action, flat Hessian, metric map, and quadratic extra
  branch. This block evaluates that same action beyond second order.
- The [compact reaction-rank theorem](ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
  supplies the exact normalized `g`, declared source generators, null-space
  inventory, and constructive reaction alternatives.
- No literature coefficient, observed value, Einstein equation, fitted
  coupling, or new primitive enters the proof.

## 9. No-Go Discipline Gate

The positive cubic-lift theorem is the main result. The only negative surface
is equation (14): the **complete leading cubic null-sector polynomial** has a
one-dimensional metric-gradient image that excludes the three displayed
source metric covectors. No full nonlinear source no-go is claimed.

### N1 — alternative route enumeration

The five families are normalized by the proof-search tuple *(primary
object/formulation, load-bearing mechanism or invariant, terminal proof
obligation)*. Each route is target-equivalent to defeating the narrow
leading-cubic non-membership statement; none is presented as a route against
the full nonlinear theory.

| Family | Object / formulation | Mechanism / invariant | Terminal obligation | Result and authority | Marker |
|---|---|---|---|---|---|
| action orientation | oriented scalar action `S_R` versus `-S_R` | multiplication sends `b` to `-b` and preserves `span(b)` | enlarge the leading metric-gradient image enough to contain a declared covector | equations (4)-(5) and the exact runner preserve rank two in (14) | `ATTEMPTED` |
| extra-coordinate orientation | null coordinate chart `g,u` versus `-g,-u` | the metric gradient is quadratic in `u` | change the leading metric-gradient line | `u^2 b` is invariant; the exact inherited branch definition fixes the same line | `ATTEMPTED` |
| full metric-null admixture | complete cubic polynomial on `M_0 x+u g` | all 55 `u x_i x_j` coefficients vanish by seven exact symmetry-orbit representatives | use arbitrary same-order metric-null coordinates to rotate the image | `partial_x P_3` remains independent of `x`; Section 3 | `ATTEMPTED` |
| source scaling / scalar reaction | projective declared-source covectors | scalar multiplication preserves matrix rank and parallelism | align a declared covector with `b` by amplitude choice | every exact rank certificate in (14) remains two | `ATTEMPTED` |
| range-eliminated Lyapunov--Schmidt equation | four-range / eleven-null reduced system | the rank-four Hessian makes the range response `O(lambda)` for null displacement `O(sqrt(lambda))` | alter the leading null equation through massive-mode backreaction | substitution first changes the null gradient beyond leading order, not the cubic image | `ATTEMPTED` |

These are five distinct mechanisms: action sign, coordinate orientation,
null-sector mixing, source scaling, and range-mode elimination. Higher-order,
finite-amplitude, curved, inhomogeneous, reaction, and boundary routes are not
declared failed; they are outside the narrow leading-cubic claim.

### N2 — wall-independence audit

The narrow statement has one wall only:

| Wall | Exact content | Independent-wall status |
|---|---|---|
| `W1` | a source balanced by the cubic null-sector polynomial must have metric covector in `span(b)` | sole wall; no pairwise inflation exists |

Action selection, coupling, boundary, Lorentzian continuation, and realized
history are downstream physical obligations, not additional proofs of (14).
They are not counted as independent walls supporting the cubic statement.

### N3 — hidden-condition scan

| Phrase class | Occurrence | Classification |
|---|---|---|
| “we assume” | none load-bearing | no hidden premise |
| “by construction” | exact `g`, complex, and homogeneous path | source-bound definitions from the parent and retained Regge runner |
| “as is standard” / “obviously” / “naturally” | absent from proof | no hidden premise |
| “background” | flat homogeneous periodic background | explicit scope condition, promoted in the title, frontmatter, and target table |
| “registered” | candidate amendment only | hypothetical wording, not current authority |
| “canonical” | canonical axiom nonmutation | governance status, not physics premise |

The number-field closure, coordinate symmetry, periodicity, homogeneity, and
Taylor order are all explicit. No hidden condition changes the wall count.

### N4 — residual matching

| Cited witness | Witness residual | Current residual | Match? |
|---|---|---|---|
| `docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:37-47` | actual action/Hessian and one branch flat at quadratic order | same actual action and same branch beyond quadratic order | yes |
| `docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:58-89` | complete compact null inventory, exact `g`, and source pairings | same `g` and same three declared sources | yes |
| parent note Sections 6-7 | reaction alternatives and candidate branch-lift obligation | correction of whether nonlinear action natively lifts `g` | yes, for the branch-lift alternative only |

No Born, continuum-GR, or unrelated compact no-go is cited as evidence for
the cubic source-image statement.

### N5 — rhetoric audit

The claim is never phrased as “Regge gravity cannot source matter” or “the
extra branch is not physical.” Resolution is explicit:

| Resolution | Actually tested | Honest result |
|---|---|---|
| per element | four edge-weight orbits and two metric-component orbits | exact quadratic-null and cubic pairings |
| per site/cell | one homogeneous translation cell | all 50 triangle classes and 240 incidences included |
| per mode | compact homogeneous `k=0` | complete 11-dimensional null sector tested |
| per block | Block-17 declared source generators | all three exact metric covectors compared |
| lattice-wide | actual periodic `L=3` homogeneous box | action value checked; inhomogeneous solutions not tested |

The primary runner cache prints one substantive certificate line for each of
these five classes, including what was not executed.

### N6 — partial-closure paths

No “new axiom is required” claim is made. Existing partial-closure routes are:

1. the parent three/four/eleven-channel KKT reactions close the quadratic
   compact equations conditionally;
2. the present native cubic term retires the premise that `g` is exactly flat
   to all orders;
3. a quartic or higher-order mixed branch may expand the metric-gradient
   image;
4. a curved or inhomogeneous solution may leave the homogeneous polynomial;
5. an open, fixed-global, background, or cosmological term may alter compact
   compatibility; and
6. a convention can state which selected sector is being solved without
   inventing new physics, after which an import-retirement audit can test the
   selection.

The candidate amendment records a sufficient interface for these routes; it
does not assign premise weight to an unapproved primitive.

The approved primitive registry was read directly at
`docs/audit/data/axiom_premise_nodes.json`, followed through each registered
`current_path`, and checked against the source notes for
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`. They respectively supply only a units reference,
kinetic-form isotropy, and pointwise evaluation at a supplied realized state.
None supplies a geometry action, source law, compact reaction, boundary,
coupling, or nonlinear solution, so none silently closes or creates the narrow
cubic wall.

### N7 — steelman

A hostile reviewer should reject any broader negative conclusion. The exact
cubic polynomial is only the first nonzero local term on the quadratic null
space. Quartic terms can introduce diagonal metric gradients; eliminating the
four massive modes changes the effective potential at quartic order; a branch
with nonuniform scaling in `x` and `u` need not be governed by the
`O(sqrt(lambda))` balance; and a finite-amplitude, curved, or inhomogeneous
solution is not classified by (4). The actionable counter-route is to compute
the complete quartic null/range tensor and run a controlled continuation of
all 15 homogeneous edge equations, then repeat on nonzero modes or an open
domain. This steelman is convincing, so a full nonlinear no-go would be
premature. The shipped claim remains only the exact cubic image and exact
non-membership of the three displayed covectors.

### N8 — cross-cycle echo

The repository contains two directly cautionary echoes:

1. Block 12's localized source residual was retired in Block 13 by an explicit
   line-minus-bag improvement. A fixed representative failure was therefore
   not a universal source failure.
2. Block 17 listed a nonlinear extra-branch lift as live. This block realizes
   that route and retires exact all-order flatness of `g`, demonstrating why
   the earlier quadratic boundary was correctly scoped.

The same mechanisms may operate again at quartic order or in a different
boundary/background sector. They remain queued rather than being rhetorically
closed.

**N1-N8 status:** `PASS` for the narrow leading-cubic source-image boundary.
The gate would `FAIL` for a full nonlinear, gravity, or axiom-necessity no-go,
and none is shipped.

## 10. Promotion Value And Cluster-Cap Gate

| Gate | Disposition |
|---|---|
| new theorem content | yes: first exact nonlinear coefficient and full cubic null-sector tensor of this actual carrier |
| advances highest-value queue root | yes: directly executes Block 17's curved/nonlinear branch-lift route |
| positive-before-negative discipline | yes: native cubic lift is the headline theorem |
| exactness | exact number-field primary route plus independent 70-digit and periodic-box controls |
| physical firewall | no action selection, observed coupling, Lorentzian solution, or realized history is claimed |
| cluster cap | one coherent nonlinear-Regge theorem packet |

## 11. Verification

The primary runner verifies:

- exact unit norm and metric orthogonality of `g`;
- invariance under all 24 coordinate permutations;
- exact Hessian nullity in all four edge-weight orbits;
- the five exact coefficients through fourth order;
- both metric-component orbits and all seven symmetric pair orbits of the
  cubic null-sector tensor;
- exact declared-source covectors and rank-two nonparallel certificates;
- independent 70-digit action derivatives;
- direct agreement with the original periodic `L=3` box action;
- the nondegenerate simplex interval; and
- source-note, N1-N8, fixed-rubric, and canonical-nonmutation surfaces.

The cached primary result, isolated mutation probes, citation registration,
direct conformance, and full integration status are recorded in the campaign
handoff and review history at delivery time.

## Boundary Verdict

The actual nonlinear Regge action resolves one important ambiguity positively:
the independent quadratic extra branch is lifted natively and exactly at
cubic order. The complete cubic tensor is sparse enough to expose the next
obligation: its metric gradient spans one shear covector and does not by
itself reproduce the declared compact source covectors. Full nonlinear source
compatibility, physical action selection, boundary/background choice,
coupling, Lorentzian dynamics, and realized history remain open. The candidate
axiom wording is sharpened, the canonical axioms are untouched, and the fixed
TOE percentages do not move.

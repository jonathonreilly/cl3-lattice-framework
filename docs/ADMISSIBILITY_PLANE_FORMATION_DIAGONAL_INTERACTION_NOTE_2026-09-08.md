---
claim_id: admissibility_plane_formation_diagonal_interaction_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "For the supplied positive six-state orbit product rule, finite monotone rectangle laws extend consistently to a translation-invariant plane law with explicit axial and diagonal pair interactions. The two diagonal classes differ exactly for nonconstant weights. This is not selection of a physical formation order or identification with a Gaussian instrument."
upstream_dependencies:
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_plane_formation_diagonal_interaction_2026_09_08.py
---

# The plane formation law and its diagonal interaction

**Date:** 2026-09-08
**Type:** bounded_theorem
**Status:** conditional-support

The supplied monotone formation rule defines a consistent probability law on the whole plane. Its exact interaction includes a diagonal pair term contributed by the local normalizers. This identifies the resulting classical law, while leaving physical order selection and quantum-instrument identification open.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact conditional probability theorem for the stated positive product-rule family."
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Supply a physical law or instrument identification rather than identifying distinct probability objects by terminology."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and prior work

The [monotone rectangle parent](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md), P1–P2 and P7(a), supplies the locally normalized product rule and rectangle density. Its opposite-corner identity is prior work, not a new result here. Labels are the six Bloch-axis menu points; weights are $p$ for identical labels, $q$ for antipodal labels and $r$ otherwise, with $p,q,r>0$. Write $Z=p+q+4r$, $K=\phi/Z$ and $H=K^2$. No numerical value of these parameters is selected. This note needs no Gaussian-instance premise.

The extension and finite-range conditional arguments use standard probability mathematics. Relevant prior art includes [Pickard (1980)](https://doi.org/10.2307/1426425) and [Champagnat and collaborators](https://pagesperso.ls2n.fr/~idier-j/pub/pubC/Champagnat98C.pdf). The 1998 paper’s abstract and introductory definitions were inspected; the DOI lookup failed. Their full papers were not read for this proof, and no theorem from them is a load-bearing shortcut. No historical novelty is claimed.

Let $K$ be the positive symmetric stochastic six-state orbit kernel and $H=K^2$. The parent proves the rectangle density

\[\mu_R(x)=\frac16\frac{\prod_{\{u,v\}\in E(R)}K(x_u,x_v)}{\prod_{\square\subset R}H(x_{\rm SW},x_{\rm NE})}.\]

## Projective consistency

The underlying top-left directed construction is normalized. Summing the bottom row right to left removes leaf conditional factors, each summing to one. Summing the right column bottom to top does the same. The already-proved 180-degree identity yields top-row and left-column removal. Successive removal of outside rows and columns therefore gives the same formula on every contained subrectangle, independently of position. This argument applies to every finite size, rather than extrapolating from executed cases.

Consistent rectangle laws determine consistent arbitrary finite-set laws by embedding each set in a rectangle and marginalizing. The countable finite-alphabet extension theorem then gives one probability measure on the plane for this chosen diagonal class. Translation invariance follows from the position-independent marginal formula. This does not construct an infinite physical formation schedule, which has no first site.

## Two classes and constant boundary

Opposite-corner equality is inherited from the parent. The two diagonal classes differ for every nonconstant orbit triple: in a square their positive common numerator has denominators H(a,b) and H(c,d). Equality for all four labels would require H constant. For the orbit kernel, H_parallel-H_antiparallel=(p-q)^2/Z². If p=q, H_parallel-H_orthogonal=2(p-r)^2/Z². Thus H constant iff p=q=r. For positive nonconstant triples the plane laws differ already on a square; constant weights give the independent uniform measure. This all-parameter statement extends the parent’s executed distinctness fixtures.

## Conditional density and affirmative interaction identification

For the center of a 3x3 square, conditional on its eight other sites,

\[\mu(z\mid\partial)=\frac1{Z(\partial)}\frac{\prod_{v\text{ axial neighbor}}K(z,x_v)}{H(z,x_{\rm NE})H(z,x_{\rm SW})}.\]

Exactly two square denominators depend on the center. With all eight labels equal to c this is K(z,c)^4/H(z,c)^2, whereas the original nearest-neighbor specification is proportional to K(z,c)^4. Their equality requires the positive column H(.,c) constant. Orbit transitivity and the preceding formulas imply this occurs only for constant weights. Since the conditioning event has positive probability, the discrepancy is genuine. If the full-rest conditional were the original four-neighbor rule, conditioning it onto these eight sites would retain that rule by the tower property; hence this finite discrepancy rules it out.

There is a positive finite-range identification: the plane law is a Gibbs measure for the pair potential -log K on axial edges and +log H on the chosen SW-NE diagonals. To verify this without assuming a Markov property, condition a finite set A inside an enclosing rectangle whose boundary lies beyond every axial/diagonal neighbor of A. Cancellation in the rectangle density gives precisely the finite-volume conditional with these pair factors. It depends only on the finitely many outside neighbors of A and therefore is unchanged as the enclosing rectangle grows. Conditional-expectation martingale convergence to the sigma algebra of all sites outside A proves the full conditional formula. Positivity prevents undefined local conditionals. No uniqueness of this expanded-interaction Gibbs specification is claimed.

This supplies an exact interaction description of the selected formation-class law, including the extra diagonal interaction induced by local normalizers. It does not identify this law with the original admissibility specification, choose a physical corner/order, identify a Gaussian or quantum instrument, or select an action from the axioms. Those remain the action-identification obligations.

## Executed scope

Independent checker: all 46656 configurations of 2x3 at three frozen triples; all its subrectangle marginals; all reflected dictionaries; exact 3x3 six-value center conditionals. It also checks 96 trimming schedules on 3x3/3x4. The latter is a combinatorial trimming check, NOT a complete 3x3/3x4 marginal enumeration or independent validation of every algebraic cancellation. Total163 checks, 2.504 seconds,50.110MiB. Constant control has zero defects. Nonconstant mirror TV values reproduce current parent exactly.

## Corner-mixture comparison

Any convex mixture of the two plane laws retains the same all-equal eight-site conditional displayed above: reflection fixes this boundary configuration and the center, so both component laws give identical joint and boundary probabilities there. Their mixture therefore gives the same conditional. For nonconstant weights it still differs from the original axial specification. This statement concerns only these two laws, not arbitrary formation orders. The equal mixture is invariant under square-lattice rotations and reflections because those transformations either preserve or exchange the two diagonal classes; that restored spatial symmetry does not remove the conditional discrepancy.

## No-Go Discipline Gate

N1: The affirmative target is the projective plane law and its explicit interaction; the comparison concerns only the supplied product-rule family. N2: No statement excludes other order classes, readouts or instruments. N3: The constant rule is an adverse boundary and gives the uniform law. N4: All local weights are positive, so the conditioning witness has positive probability. N5: Executed resolution classes are printed by the runner; no complete plane census is claimed. N6: Original proof and controls are preserved in the packet. N7: Choosing a different physical formation law remains outside the theorem. N8: The result does not retire the action-identification obligation or select an axiom-level process.

## Verification and imports

The [live exact runner](../scripts/admissibility_plane_formation_diagonal_interaction_2026_09_08.py) uses Python integer and rational arithmetic for all probability calculations. Floating values report resources only. It checks complete 2×3 laws and their subrectangles at three frozen triples, exact six-value center conditionals, and 96 trimming schedules; schedules are not complete 3×3 or 3×4 marginal enumeration. Infinite consistency and the conditional specification rest on the proof above. The sole mathematical source dependency is the linked parent; finite-alphabet extension and conditional-expectation convergence are explicit standard mathematical imports proved applicable above.

[Durable original evidence](../.claude/science/physics-loops/admissibility-plane-formation-20260908/evidence/original/DERIVATION.md) preserves the pre-port derivation and exact read-coverage disclosure. Independent review and adverse executions are recorded in the same packet. No audit verdict is authored here.

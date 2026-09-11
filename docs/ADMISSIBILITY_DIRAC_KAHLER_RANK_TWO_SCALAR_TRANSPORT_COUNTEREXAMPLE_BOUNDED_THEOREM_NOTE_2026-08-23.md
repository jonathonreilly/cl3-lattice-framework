---
claim_id: admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "Exact finite identities for a supplied rank-two isometric compression of two reflection-form fixtures, plus a quantified affine-admixture lemma for a nonzero orthogonal positive-semidefinite addition. The calculation does not select a physical readout, prove an exhaustive readout classification, adopt a historical parent theorem, establish an all-lattice or continuum result, or change any axiom, premise, obligation, audit verdict, or TOE status."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py
---

# Rank-two scalar transport counterexample — corrected finite note

**Historical block:** 178

**Repair date:** 2026-09-10

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py`](../scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py)

**Alternative checker:**
[`scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_independent_check_2026_08_23.py`](../scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_independent_check_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py`](../scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py)

The helper uses the fixed `EX`, `ET`, and shift-lift definitions from the
[current Block 105 finite construction](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
That citation identifies the current source of the matrices. It does not adopt
Block 105's broader theorem scope or any historical parent claim. The
[current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) provide the authority
boundary; this finite fixture is not added to either one.

## Finite construction and exact result

For each disclosed antiperiodic cover, the helper constructs the selected
self-edge differential, Hodge quotient, supplied graded carrier, temporal
reflection, and the eight-row form

\[
 F_T(s_t)=\operatorname{Herm}
 \left(\operatorname{Sel}_S^\top r_TQ_T(s_t)\operatorname{Sel}_S\right),
 \qquad Q_T=H_{q,T}+K_{q,T},
\]

with cover extents `8x4` and `12x4`, selected rows
`S=(4,5,6,7,8,9,10,11)`, fixed slice `c=1`, pinned links incident to that
slice, shear and spatial dial `3/5`, and mass `1`. These are supplied finite
choices, not physical identifications.

In the selected eight-dimensional basis, define

\[
 x_0={4e_0+3e_4\over5},\qquad
 x_2={4e_2+3e_6\over5},\qquad X=[x_0,x_2].
\]

Disjoint support and `4^2+3^2=5^2` give `X^dag X=I_2`. The exact calculation
on both extents gives

\[
 X^\dagger F_T(s_t)X
 =\left({114\over125}+{171\over250}s_t\right)I_2.
\]

Consequently the compression is rank two and positive for `s_t>-4/3`, with

\[
 F_X(1/8)={399\over400}I_2,\qquad
 F_X(1/2)={627\over500}I_2,
\]

\[
 {1\over2}\operatorname{tr}\bigl(F_X(1/2)-F_X(1/8)\bigr)
 ={513\over2000},
\]

and

\[
 \det F_X(s_t)={3249\over62500}(3s_t+4)^2.
\]

This is a direct counterexample to a rank-one-only statement **when that
statement includes standard isometric compression on these two supplied
fixtures**. It does not classify nonlinear readouts, prove a complete effect
domain, or select the displayed compression as physical.

## Quantified affine-admixture lemma

Let `P` be a positive rank-one effect with response
`d=Tr(P Delta) != 0`. Let `Q` be a **nonzero** positive-semidefinite operator
whose support is orthogonal to the support of `P`; the ambient dimension is
therefore at least two. For positive `epsilon`,

\[
 \operatorname{rank}(P+\epsilon Q)
 =\operatorname{rank}(P)+\operatorname{rank}(Q),
\]

and the affine response is

\[
 \operatorname{Tr}[(P+\epsilon Q)\Delta]
 =d+\epsilon q,\qquad q=\operatorname{Tr}(Q\Delta).
\]

This polynomial has at most one tuned root. If an effect must satisfy
`0 <= E <= I`, `epsilon` must additionally be small enough to preserve the
upper bound. The primary runner checks the explicit choice

\[
 P=\operatorname{diag}(1,0),\quad
 Q=\operatorname{diag}(0,1),\quad
 \epsilon={1\over4},\quad
 \Delta=\operatorname{diag}(1,-2),
\]

for which `E=P+epsilon Q` is an effect of rank two, the raw response is `1/2`,
and trace normalization gives `2/5`.

For the normalized two-dimensional choice
`P=diag(1,0)`, `Q=diag(0,1)`, while allowing an arbitrary Hermitian response
matrix with entries `d,q,x,y`, the alternative checker supplies the symbolic
effect-bounded choice

\[
 \epsilon_*={d^2\over2(d^2+q^2)}\in(0,1)
\]

and proves persistence from

\[
 2(d^2+q^2)+dq
 ={3\over2}(d^2+q^2)+{1\over2}(d+q)^2>0
\]

when `d` is nonzero. This lemma concerns affine PSD-effect readouts only. A
non-affine or non-convex domain can evade it.

## Additional preserved finite calculation

The exact finite density and menu constants used in the historical package
contain the rank-two union projector
`E_12=diag(0,1,1,0)`. Its trace against the displayed normalized diagonal
density is positive. This confirms that a rank-two projector occurs in that
finite vocabulary. It does not make the vocabulary, the density, or its trace
reading a physical law.

## Runtime closure and historical disposition

The repaired runtime imports the dedicated helper and its already reviewed
finite supplier. The latter binds the current Block 105 runner bytes. The two
runners bind their complete live input tuples with literal SHA-256 values. The
old 51-script closure is not imported as theorem authority.

The original note, primary, alternative checker, cache, and historical manifest
entry are preserved byte-for-byte in the recovery packet. Historical formula
sources used to extract the helper are recorded by path and source hash. Their
theorem prose, audit status, campaign routing, and physical interpretations are
archive-only. The alternative checker shares this finite helper, so it is an
alternative implementation of the algebraic checks rather than an independent
fixture reconstruction.

## Scope and disposition

Preserved finite results are the two exact compression identities, their
positivity interval, derivative, endpoint gap, determinant, the quantified
affine lemma under its stated hypotheses, and the displayed finite union-effect
calculation.

The package does not establish a complete operational effect algebra, an
exhaustive readout theorem, a physical meaning for `s_t`, a Born rule, a
continuum limit, a universal action result, or any change in scientific
governance. No parent theorem or predicted audit status is carried forward.
Any continuation is optional work under current shared planning.

## N1 — alternative routes

Live routes include derived nonlinear readouts, an extreme-effect-only domain,
a superselection rule forbidding mixtures, a complete physical effect algebra,
a physical carrier map for `s_t`, and other finite or continuum fixtures. None
is excluded by the displayed calculation.

## N2 — separate obligations

Effect-domain selection, carrier identification, action completeness, and a
controlled interference observable are separate missing supplies in this
scope. The calculation does not provide countermodels proving logical or
model-theoretic independence among them.

## N3 — hidden assumptions

The form, reflection, support, carrier, dials, two finite extents, and standard
isometric-compression reading are supplied choices. The affine lemma separately
assumes a nonzero orthogonal PSD addition and an affine response. No supplied
choice is promoted to an axiom or physical selector.

## N4 — residual matching

The exact `X^dag F_T X` identity addresses only a rank-one-only claim that
includes these forms and this compression notion. The native union projector
shows vocabulary membership only. Neither result substitutes for a theorem
about physical events, nonlinear readouts, or an untested action.

## N5 — rhetoric and resolution

The primary runner prints the bounded resolution explicitly: per element it
checks the compression and affine response; per site it reconstructs the chosen
eight-row forms; per mode it varies the supplied dial; per block it rejects the
finite rank-one-only successor; lattice-wide and whole-TOE conclusions are not
executed.

## N6 — partial closure

A useful positive continuation would derive a presentation-invariant event or
effect domain, then test the exact action on that domain. Determinant or
exterior-power readouts remain possible once their domain and physical role are
supplied. No open route implies that a new axiom is necessary.

## N7 — hostile-reviewer steelman

A narrower proposal could define its scalar as a determinant, exterior power,
or extreme-effect functional and exclude standard matrix compression by
definition. That would evade this counterexample. It would still need a derived
and exhaustive physical reason for that domain restriction.

## N8 — cross-cycle echo

Earlier finite effect-menu calculations show that trace form follows only after
a full event/effect domain and additivity rules are supplied. That pattern
supports the live representation-theorem route; it does not turn this finite
counterexample into a universal no-go or a probability derivation.

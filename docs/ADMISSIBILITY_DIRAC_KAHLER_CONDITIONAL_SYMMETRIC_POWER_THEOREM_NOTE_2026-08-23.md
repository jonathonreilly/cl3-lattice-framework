---
claim_id: admissibility_dirac_kahler_conditional_symmetric_power_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "A direct finite symmetric-power minor identity and measurements of supplied action-side and covariance-side kernels at two covers and two temporal dials. Indefiniteness is conditional on a mixed one-particle kernel; the normalized vacuum is one. No source grading, physical kernel, readout, premise, axiom, audit verdict, or continuum result is selected."
depends_on:
  - admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py
---

# Conditional symmetric powers — corrected finite note

**Historical block:** 177

**Repair date:** 2026-09-11

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py`](../scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py`](../scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py)

The finite matrices come through the
[corrected Block 176 calculation](ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md)
and the accepted
[Block 105 finite construction](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) remain unchanged.

## Symmetric-power minor

Let a Hermitian one-particle kernel restrict to

\[
 K=\begin{pmatrix}p&r\\\bar r&q\end{pmatrix},
 \qquad p>0>q.
\]

In the degree-`n` permanent Gram, use the two raw monomials `u^n` and
`u^(n-1)v`. Direct permutation counting gives

\[
 A=n!p^n,
 \quad B=n!p^{n-1}r,
 \quad D=(n-1)!\bigl(p^{n-1}q+(n-1)p^{n-2}|r|^2\bigr),
\]

and hence

\[
 AD-|B|^2=n!(n-1)!p^{2n-2}(pq-|r|^2)<0.
\]

The modulus square is load-bearing. A positive diagonal change from raw
monomials to another conventional normalization preserves the determinant
sign. The primary runner reconstructs the permanents directly at `n=2,3,4`.

## Two supplied one-particle candidates

At cover extents `8x4` and `12x4`, the runner constructs both:

- the action-side reflected form `Herm([rQ]_{S,S})`;
- the covariance-side form `Herm([r(Q^{-1})^T]_{S,S})`.

They are unequal finite matrices. That mismatch means a source-functional
grading must identify its own one-particle kernel; this note does not derive
that identification.

At the supplied on-dial point `s_t=1/4`, both candidates are mixed on both
extents. At `s_t=0`, the covariance-side candidate remains mixed, while the
action-side form is

\[
 \operatorname{diag}\left({57\over40}I_4,0_4\right)
\]

with inertia `(4,0,4)` in `(positive,negative,zero)` order. It is
positive-semidefinite. Therefore the symmetric-power indefiniteness lemma
applies only where the chosen one-particle candidate is mixed; it does not
apply to this action-side region point.

## Vacuum convention

For the normalized graded algebra, `Sym^0(K)` is the one-dimensional vacuum and
its normalized coefficient is `1`. It has no dial sensitivity.

An **unnormalized** Gaussian convention may multiply the entire generating
functional by `Z(Q)` or by `Z(Q)Z(Q^dagger)`. Such a scalar can be positive and
dial-sensitive on a finite fixture, but that is a supplied normalization
choice. It is not the normalized vacuum and is not selected by the symmetric
power algebra.

## Scope and disposition

The exact minor formula and the four finite candidate measurements are
retained. Claims that both candidates are indefinite at both dials, that a
dial-sensitive normalized vacuum follows, or that the framework has already
selected the covariance kernel are withdrawn.

The runtime closure is the corrected Block 176 helper chain plus current
authority files. Historical parents and their audit/promotion language remain
archive-only.

## N1 — alternative routes

A derived source functional, another reflection, a quotient, or a different
one-particle domain could produce a different grading. These routes remain
open.

## N2 — separate obligations

Kernel identification, source normalization, event selection, and physical
interpretation are distinct missing supplies. No independence theorem is made.

## N3 — hidden assumptions

The reflection, selected rows, finite extents, dials, and quasi-free permanent
construction are supplied choices.

## N4 — residual matching

The negative minor proves indefiniteness only after a mixed two-dimensional
restriction has been exhibited in the chosen kernel.

## N5 — rhetoric and resolution

The action-side `s_t=0` case is labeled PSD. The unnormalized Gaussian factor
is distinguished from the normalized vacuum.

## N6 — partial closure

A source-functional derivation could specify the correct kernel and
normalization before any sector conclusion is promoted.

## N7 — hostile-reviewer steelman

A critic can choose the action-side region form or a different source grading;
the conditional theorem then does not imply the earlier universal statement.

## N8 — cross-cycle echo

Other finite reflection calculations also distinguish a matrix identity from
the physical choice of which matrix is graded. That is context, not a premise.

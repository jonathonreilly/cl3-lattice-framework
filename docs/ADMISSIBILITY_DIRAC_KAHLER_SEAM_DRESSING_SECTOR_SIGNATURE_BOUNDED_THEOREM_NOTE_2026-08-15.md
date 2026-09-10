---
claim_id: admissibility_dirac_kahler_seam_dressing_sector_signature_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "In the Block 109 finite four-structure ansatz, conjugation by the unit spatial shift splits each displayed 132-dimensional linear dressing space into a 128-dimensional even sector and a 4-dimensional odd sector. Every pure-odd Hermitian Gram has negation-symmetric spectrum and signature zero, so a nonzero pure-odd Gram is indefinite; this does not exclude mixed even/odd involutions. Four directed even supports have full linear ranks 12 or 24, while one 48-coordinate permutation support has rank 47/nullity 1 and its remaining one-parameter involution ideal has Groebner basis {1}. Spatial Fourier transformation produces four coupled blocks subject to shared coefficient and reality constraints, not four independent problems."
depends_on:
  - admissibility_dirac_kahler_global_dressing_involution_positivity_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_dirac_kahler_global_dressing_involution_positivity_bounded_theorem_note_2026-08-15
target_blocker_text: "The full 132-dimensional involution-positivity variety remains open."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Solve the coupled Fourier equations or the full mixed even/odd involution-positivity variety without assuming a physical selector."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite grading and covariance identities, exact rational sector and support ranks, and an exact one-parameter polynomial obstruction on the declared chosen d=2 carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Seam-Dressing Sector And Signature Certificates

**Date:** 2026-08-15

**Campaign block:** 110

**Type:** `bounded_theorem`
**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.py`](../scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.py)

## 1. Result and boundary

This note uses the chosen finite carrier and exact matrices defined inline by
[Block 109](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md).
It adds a spatial-shift grading, a pure-odd signature theorem, and narrow
even-support exclusions. It does not choose a physical seam dressing.

Let `C` be the four-cycle shift and define

\[
 S_0=I_4,\qquad S_1=D_x,\qquad
 S_2=C+C^T,\qquad S_3=C-C^T.                 \tag{1}
\]

Conjugation by `C` has signs `(+,−,+,+)` on these structures. Thus `D_x`
is the odd structure and the other three are even. Exact restricted ranks at
both displayed fixtures give

\[
 \dim\mathscr L_c^{\mathrm{even}}=128,
 \qquad
 \dim\mathscr L_c^{\mathrm{odd}}=4,
 \qquad c\in\{5/13,3/5\}.                    \tag{2}
\]

The two coordinate sectors are disjoint and their dimensions sum to the
Block 109 value 132.

For a pure-odd dressing, covariance and real linearity give

\[
 C_+\mathcal K_A C_+^{-1}
 =\mathcal K_{CAC^{-1}}
 =\mathcal K_{-A}
 =-\mathcal K_A.                              \tag{3}
\]

Here `C_+=I_4 tensor C` acts on the 16-dimensional positive-time Gram. The
runner checks that the carrier shift commutes with both displayed
propagators and reflections and preserves the positive and reflected index
sets. It also checks the covariance identity on pinned exact rational test
elements and the required real-linearity identities.

Every Gram in the joint space is Hermitian. Equation (3) makes a pure-odd
Gram's spectrum negation-symmetric. Its signature is exactly zero. Therefore
every nonzero pure-odd Gram is indefinite, while the zero Gram is the only
positive semidefinite possibility in that sector.

This is an odd-sector obstruction. It does not imply that a positive
dressing must itself be purely even. A mixed even/odd Gram need not
anticommute with `C_+`. The exact positive-fiber representative imported
from Block 109 has Gram `I_16`, which is shift-even; the odd-only argument
does not exclude adding an odd component while preserving positivity and
involution by some other mechanism. The mixed even/odd involution-positivity
variety remains open.

## 2. The `A_star` Gram-side check

At the primary fixture `c=5/13`, the Block 109 `A_star` Gram is `16 x 16`,
anticommutes with `C_+`, has an even characteristic polynomial, and has
inertia `(8,8,0)`.

The runner also forms a 16-dimensional **Gram-side trial space** of `16 x 16`
slice-diagonal matrices: on each of the four positive-time slices, the block
is one of `I_4,C,C^2,C^3`. The linear anticommutator equations with the
primary `A_star` Gram have rank 14 and nullity 2. Inside this specific trial
space their kernel is

\[
 \operatorname{span}_{\mathbb R}
 \{I_4\mathbin\otimes C,\ I_4\mathbin\otimes C^3\}.     \tag{4}
\]

This is not an anticommutant calculation for the `32 x 32` dressing matrix
`A_star`, and it is not an anticommutant inside the 132-dimensional dressing
space. It is the displayed `16 x 16` Gram-side calculation at the primary
fixture only.

## 3. Exact sparse even-support boundaries

The even spatial factors are `I_4`, `C+C^T`, and `C-C^T`. For each support,
the runner embeds real and imaginary coefficients and stacks reflection
reality with Gram Hermiticity. The exact results at both fixtures are:

| support | real coordinates | stacked rank | linear nullity |
|---|---:|---:|---:|
| `F-1` | 12 | 12 | 0 |
| `F-2` | 24 | 24 | 0 |
| `F+1` | 12 | 12 | 0 |
| `F+2` | 24 | 24 | 0 |

Each of these four supports contains only the zero linear solution and hence
contains no involution.

The permutation support `p=(3,2,1,0,7,6,5,4)` is different. It has 48 real
coordinates, stacked rank 47, and nullity 1 at both fixtures. Its linear
system is therefore not full rank. Substituting its exact kernel generator
into `A^2-I_32` leaves a one-parameter polynomial system whose reduced
Groebner basis `{1}` is checked at both fixtures. The no-involution result on
this support is the combined rank-47/nullity-1 plus polynomial obstruction,
not a rank-48 linear obstruction.

These five results apply only to the named supports. They do not close the
128-dimensional even-sector variety.

## 4. Fourier blocks remain coupled

The spatial DFT diagonalizes all three even structures, both displayed
propagators, and both reflections. If their shared `8 x 8` slice-coefficient
matrices are `T_0,T_2,T_3`, the four momentum blocks are

\[
\begin{aligned}
 B_0&=T_0+2T_2, & B_2&=T_0-2T_2,\\
 B_1&=T_0+2iT_3, & B_3&=T_0-2iT_3.
\end{aligned}                                           \tag{5}
\]

Consequently,

\[
 B_0+B_2=B_1+B_3=2T_0.                                 \tag{6}
\]

The runner checks equation (6) on the displayed rational test matrices.
The original coefficients are shared among momenta, and reflection reality
adds conjugacy relations. The DFT therefore yields four coupled momentum
blocks with a shared coefficient constraint. It does not factor the
involution variety into four independent problems.

## 5. Authority and actual runtime inputs

Block 110 imports
[`scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py`](../scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py)
as its only repository scientific helper. The imported module constructs the
finite operator, propagators, reflection, spatial factors, linear systems,
`A_star`, and positive-fiber representative used here. Block 110 does not
execute the Block 109 `main()` function and does not read a Block 109 cache.

Its literal `AUDIT_INPUT_PATHS` closure is exactly:

1. this theorem note;
2. the Block 109 theorem note;
3. the imported Block 109 runner.

The corrected supplier, minimal axioms, and premise registry are transitive
scientific context documented and bound by the Block 109 runner. Block 110
does not read them directly, so they are not repeated as direct runtime
inputs. Historical Block 103--108 files and released cache logs are neither
imports nor runtime inputs.

## 6. No-go discipline for the bounded negative claims

The negative surface consists of the pure-odd Gram obstruction and the five
named even-support exclusions.

**N1 — alternative-route enumeration.** The executed alternatives are: the
whole pure-odd grading argument; the primary `A_star` characteristic
polynomial; the primary 16-dimensional Gram-side anticommutant trial; four
directed 12/24-coordinate even supports; and the 48-coordinate permutation
support with its one-parameter ideal. The full even variety and the full
mixed-parity variety are separate live routes.

**N2 — wall-independence audit.** `W1` is pure-odd Gram anticommutation.
`W2` is full linear rank on each directed support. `W3` is rank 47/nullity 1
followed by the Groebner basis `{1}` on the permutation support. `W2` and
`W3` concern different declared supports; within `W3`, the polynomial step
depends on the linear kernel and is not an independent wall. None of these
walls governs a general mixed-parity dressing.

**N3 — hidden-wall scan.** The proof fixes the Block 109 torus, two rational
fixtures, reflection, positive-time span, target-arm Gram convention, and
four-structure spatial ansatz. The sparse exclusions additionally fix their
listed slice supports. No action derivation, locality theorem, continuum
limit, modular selection, or gravity compatibility is present.

**N4 — residual matching.** Pure-odd signature zero addresses Gram
positivity, while the even sparse calculations address involution existence
after linear constraints. They are different residuals. Combining them does
not yield a no-go for a mixed dressing or for an untested even support.

**N5 — resolution audit.**

- `per_element:` exact grading, covariance, rank, and polynomial identities
  are checked.
- `per_site:` the one-mode-per-site `Z8_t x Z4_x` carrier is checked.
- `per_mode:` four spatial momenta are displayed, with their coupling kept.
- `per_block:` the declared directed and permutation supports are checked.
- `lattice_wide:` not executed; no size-uniform conclusion is claimed.

**N6 — partial-closure path scan.** Live routes include mixed even/odd
involutions, other even supports, the full coupled Fourier equations, and an
action-derived selector. The present sparse boundaries can guide those
calculations but do not settle them.

**N7 — steelman.** A mixed dressing can have a large positive even Gram plus
a smaller odd Hermitian perturbation and remain positive. It may also satisfy
the nonlinear involution equations through cancellations between parity
sectors. Nothing in the odd-only signature theorem excludes this scenario.

**N8 — cross-cycle echo.** No historical ancestry chain or stale cache is
used as proof. The Block 109 source imported at runtime and the calculations
in this runner are the only executable scientific dependencies.

## 7. Disposition

This is a bounded sector theorem and bounded sparse-support no-go. It is not
a transporter impossibility. No axiom amendment is justified. The actual
ADM/history transporter remains open, the gravity constraint quotient
remains unexecuted, and formal audit and retention remain outside this
authoring unit.

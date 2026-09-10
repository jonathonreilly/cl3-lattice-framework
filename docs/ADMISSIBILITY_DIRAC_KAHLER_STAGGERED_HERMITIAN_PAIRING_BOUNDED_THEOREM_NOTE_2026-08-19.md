---
claim_id: admissibility_dirac_kahler_staggered_hermitian_pairing_bounded_theorem_note_2026-08-19
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md
claim_type: bounded_theorem
claim_scope: "On the displayed 4 by 4 quotient and primary Block 105 staircase fixture, the staggered site parity is H_q-self-adjoint, anticommutes with all sixteen measured J operators, and gives Hermitian edge pairings; its common anticommutant is one-dimensional on that fixture. H_q-skewness structurally gives a purely imaginary semisimple spectrum in conjugate plus/minus pairs and an even characteristic polynomial, while invertibility and squarefreeness are fixture computations. For the eight-dimensional R blocks, every real symmetric symmetrizer has positive index at most six on the primary edges. A physical block from a real H-isometric half exchange is treated separately and shares the bound when it is symmetric. Zero and nonzero PSD algebraic symmetrizers exist, so no no-PSD result follows. The chart census covers two weight assignments and two shear corners only. A polar-decomposition proof establishes the stated metric half-exchange result. Reflection positivity, positivity of P(m), general uniqueness, all-weight robustness, and an OS no-go remain open."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - admissibility_dirac_kahler_carrier_reflection_blocker_bounded_theorem_note_2026-08-19
runner: scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
artifact_role: theorem
claim_type_reason: "The exact anticommutation, finite spectra, symmetrizer systems, counterexamples, and polar construction are theorem-level statements on the declared fixture and algebraic hypotheses; untested masses, weights, carriers, and involution constraints keep the result bounded."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Staggered Hermiticity And The Definite-Symmetrizer Boundary

**Date:** 2026-08-19

**Campaign block:** 143

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. This note adopts no premise and changes no
axiom or retained claim.

**TOE accounting:** zero obligation retirement. No axiom amendment is
justified. No TOE percentage moves. The retained-positive end-to-end theory
count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py`](../scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py)

**Construction sources:**
[Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
supplies the reviewed Hodge fixture, and
[Block 142](ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md)
supplies the corrected mass split. The current premise boundary is
[Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md); this note does not add to it.

## 1. Corrected Result

The primary calculation uses the displayed `4 x 4` physical quotient,
the Block 105 staircase overlap-Hodge carrier, `s_x=3/5`, `s_t=4/5`, and
weights

\[
 x=(0,0,\tfrac12,-\tfrac13).                             \tag{1}
\]

For each of its sixteen ordered edges,

\[
 Q_{ij}=mH_q+K_{ij},\qquad K_{ij}^{\mathsf T}=-K_{ij},
 \qquad J_{ij}=H_q^{-1}K_{ij}.                            \tag{2}
\]

The `K_ij` are real and `m`-free. With

\[
 X_0=\operatorname{diag}\bigl((-1)^{t+x}\bigr),          \tag{3}
\]

the primary fixture verifies

\[
 X_0^2=I,\qquad H_qX_0=(H_qX_0)^{\mathsf T},\qquad
 X_0J_{ij}+J_{ij}X_0=0                                   \tag{4}
\]

on all sixteen edges. Consequently `X_0^dagger Q_ij` is **Hermitian on
all 16 primary-fixture edges**. The common anticommutant of the sixteen
primary `J_ij` is one-dimensional, and its generator is `X_0`. Thus
`X_0` is **unique up to sign on the primary fixture**. The second weight
control checks Hermiticity again; it does not repeat the uniqueness solve.

## 2. Structural Spectrum Versus Fixture Spectrum

Because `H_q > 0` and `K^T = -K`,

\[
 J=H_q^{-1}K
 \sim H_q^{-1/2}KH_q^{-1/2}.                              \tag{5}
\]

The matrix on the right is real antisymmetric. Therefore `J` is
diagonalizable over the complex numbers, its spectrum is purely imaginary in
conjugate plus/minus pairs, and its characteristic polynomial is even.

This structural fact **does not imply invertibility or squarefreeness**.
Zero eigenvalues may occur and distinct rotation planes may have the same
frequency. The runner separately computes that the primary sixteen
`J_ij` characteristic polynomials are even, invertible, and squarefree.
Only evenness and the imaginary semisimple plus/minus pairing come from (5).

## 3. Keep The Symmetrizer And Physical Block Distinct

For the eight-dimensional off-diagonal block define

\[
 \beta=H_q[-,+],\qquad
 R_{ij}=\beta^{-1}K_{ij}[-,+],\qquad
 Q_{ij}[-,+]=\beta(mI+R_{ij}).                            \tag{6}
\]

Now restrict to a **real `H_q`-isometric half exchange**

\[
 \Theta=\begin{pmatrix}0&W^{-1}\\W&0\end{pmatrix}.
\]

The metric equation makes the following mass-level block symmetric:

\[
 \boxed{S=W^{\mathsf T}\beta},\qquad S=S^{\mathsf T}.    \tag{7}
\]

In plain text, `S = W^T beta`. If this half exchange also gives a symmetric
physical block, that block is the different matrix

\[
 \boxed{P(m)=W^{\mathsf T}Q[-,+]=S(mI+R)}.               \tag{8}
\]

In plain text, `P(m) = S(m I + R)`. Symmetry of `P(m)`, together with
symmetry of `S`, implies

\[
 SR=R^{\mathsf T}S.                                      \tag{9}
\]

Conversely, any real symmetric algebraic `S` satisfying (9) gives

\[
 P(m)^{\mathsf T}=P(m),\qquad
 P(m)R=R^{\mathsf T}P(m)                                 \tag{10}
\]

for every real `m`. Thus any common positive-index bound for **real symmetric**
symmetrizers of `R` applies separately to `S` and `P(m)`. It does not
say that either matrix is positive semidefinite, and it does not say that an
arbitrary algebraic `S` yields an admissible involution. Recovering a candidate
from (7) gives

\[
 W=(S\beta^{-1})^{\mathsf T}=\beta^{-\mathsf T}S,         \tag{11}
\]

which must still satisfy the half-exchange metric and involution conditions.

## 4. What The Spectrum Proves

The primary chart-indexed census for `R` has two arms:

- Four edges are nilpotent of index 3 and Jordan type `(3,3,1,1)`. They are
  exactly the **zero dressing** edges whose left chart is
  **cover-time-even**.
- The other twelve edges have squarefree characteristic polynomial and
  exactly four nonreal eigenvalues.

For a real symmetric form `T` satisfying `TR=R^T T`, each arm has a
two-dimensional totally isotropic subspace. In the nilpotent arm it is
`im(R^2)`. In the split arm, take one eigenvector from each of
the two nonreal conjugate pairs; the self and cross pairings vanish by the
self-adjointness identity.

In the split arm this is a complex two-dimensional totally isotropic space for
the Hermitian extension `z^dagger T w` of the real symmetric form. That
extension has the same inertia `(p,z,n)` as the real form.

If `T` has inertia `(p,z,n)` on an eight-dimensional real space, a
two-dimensional totally isotropic subspace forces

\[
 p\le 6.                                                  \tag{12}
\]

The runner verifies this **positive index at most 6** bound on every primary
edge and constructs inertia `(6,0,2)` symmetrizers on one nilpotent and one
split probe. The bound excludes positive-definite `S` and, through (10),
positive-definite `P(m)`. It does not exclude PSD forms: a PSD form may have
a radical containing the measured isotropic subspace.

## 5. Explicit PSD Counterexamples And Correct Dimensions

The zero matrix is a **zero PSD symmetrizer** for every `R`. There is also a
**nonzero PSD symmetrizer** for the nilpotent Jordan form. In the basis where

\[
 R_0=\operatorname{diag}(J_3,J_3,0,0),\qquad
 J_3=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},    \tag{13}
\]

take

\[
 S_0=\operatorname{diag}(0,0,1,\;0,0,1,\;1,1).          \tag{14}
\]

Then `S_0` is PSD, its inertia is `(4,4,0)`, and
`S_0 R_0 = R_0^T S_0`. The runner constructs the exact rational Jordan
basis of its nilpotent probe and pulls (14) back by congruence, preserving PSD
and the symmetrizer identity. This directly refutes the historical generic
no-PSD inference.

The exact linear system for **real symmetric** `S` has **dimension 16** for
the `(3,3,1,1)` nilpotent probe. The value **dimension 8** belongs to the tested
squarefree split probe. The former cannot be replaced by the latter.

These counterexamples concern algebraic symmetrizers. The zero example gives
a zero physical block algebraically, but it does not define an invertible
half-exchange `W`. The nonzero example is singular as well. Positivity of a
physical `P(m)` subject to all involution constraints remains undecided.

## 6. Two Weight Controls, Corners, And The Scout

At the second tested weights

\[
 x'=(0,\tfrac73,-\tfrac5{11},2),                         \tag{15}
\]

the chart-indexed census changes from 4 nilpotent plus 12 split to
2 nilpotent plus 14 split. In both cases the nilpotent locus equals
the zero-dressing, cover-time-even-left-chart locus, and the bound (12) holds.
These are **two tested weight assignments**, not an all-weight theorem.

At the `s_t=0` corner, all sixteen measured `R` blocks have Jordan type
`(2,2,2,2)` and index 2, giving the sharper positive-index bound `p <= 4`.
At the `s_x=0` corner, twelve measured blocks retain four nonreal
eigenvalues and the remaining nilpotent blocks have type `(2,2,2,2)`. The
**no-positive-definite bound survives** at both named corners. No corner
no-PSD claim follows.

The specified adapted scout
`Theta_ad=2 Pi_+-I` is a rational `H_q`-isometry with eigenspace
dimensions `8+8`, but its anticommutator with each primary `J_ij` has
rank 16. It therefore fails this fixture's Hermiticity condition. On each
primary edge, the anticommutation equations on the 128-dimensional
block-antidiagonal operator space have rank 128, so **no half-exchanging
operator** in that tested space anticommutes with `J`.

The mass contribution on the `+1` eigenspace of an `H_q`-adapted
involution is `m H_q`. It is positive for `m>0`, zero for `m=0`, and
negative for `m<0`. No mass-independent positivity statement is made.

## 7. Polar-Decomposition Proof Of The Metric Half Exchange

The independent review withdrew its suspicion about this construction; the
missing proof is supplied here as a positive result.

Let

\[
 H=\begin{pmatrix}A&C\\C^{\mathsf T}&B\end{pmatrix},
 \qquad A>0,\quad B>0,\quad C\ \text{invertible}.         \tag{16}
\]

Write the singular-value decomposition

\[
 D=A^{-1/2}CB^{-1/2}=U\Sigma V^{\mathsf T}               \tag{17}
\]

and define

\[
 W=B^{-1/2}VU^{\mathsf T}A^{1/2},\qquad
 \Theta=\begin{pmatrix}0&W^{-1}\\W&0\end{pmatrix}.      \tag{18}
\]

First, `Theta^2=I`. Also

\[
 W^{\mathsf T}BW=A,
 \qquad
 W^{\mathsf T}C^{\mathsf T}=CW
   =A^{1/2}U\Sigma U^{\mathsf T}A^{1/2}>0.               \tag{19}
\]

Equations (19) give `Theta^T H Theta=H`, and the displayed cross
block is positive definite because `C` is invertible, hence every singular
value in `Sigma` is positive.

For uniqueness, write any metric-compatible candidate as
`W=B^-1/2 O A^1/2`. The diagonal metric equation makes `O` orthogonal.
The positive-cross-block condition says `D O` is positive definite. The
polar decomposition of the invertible `D` has a unique orthogonal factor,
so `O=V U^T`, which is exactly (18). This proves existence and
uniqueness under (16). It is not recorded as a failed finding.

For the displayed fixture, the runner verifies `A=H_q[+,+]>0`,
`B=H_q[-,-]>0`, and

\[
 \det C=\det H_q[+,-]=\frac1{26542080}\ne0.              \tag{20}
\]

This metric half exchange need not anticommute with the primary `J`, so it
does not conflict with the rank-128 result in Section 6.

## 8. Executable Checks And Finding Dispositions

The original check IDs are preserved:

- **A-authority:** literal present inputs and actual SHA-256 bindings, without
  moving refs or ancestry.
- **B-skew-split:** the primary split and sixteen measured characteristic
  polynomials, with structural and fixture conclusions separated.
- **C-staggered-involution:** primary-fixture Hermiticity and uniqueness.
- **D-adapted-scout-and-half-exchange:** the specified scout and the tested
  block-antidiagonal anticommutation space.
- **E-positivity-obstruction:** the historical ID is retained for the
  corrected no-positive-definite bound, PSD counterexamples, 16/8 dimensions,
  and the `S`-to-`P(m)` bridge.
- **F-weight-robustness:** the historical ID is retained for two weight
  controls; it is not an all-weight assertion.
- **G-metric-complement-and-corners:** (20), the two corner censuses, and only
  their no-positive-definite conclusion.
- **H-note-scope:** corrected quantifiers, proof, firewalls, and exact fence.

The proposed bounded producer cap is 180 seconds, with a separate 1 GiB
peak-RSS watcher on macOS. It does not use `RLIMIT_AS`.

The review findings have these dispositions:

- **R143-1:** corrected. Evenness and imaginary semisimple plus/minus pairs
  are structural; invertibility and squarefreeness are fixture computations.
- **R143-2:** corrected. The generic no-PSD statement is removed, `S` and
  `P(m)` are distinguished, and zero and nonzero PSD counterexamples are
  explicit.
- **R143-3:** the suspicion was withdrawn. Section 7 supplies the valid polar
  proof and does not report it as a failure.
- **R143-4:** corrected. The nilpotent symmetrizer dimension is 16; dimension
  8 belongs only to the split probe. The inertia `(6,0,2)` is an attained
  bound on two probes, not a universal family dimension.
- **R143-5:** corrected. Mass positivity is restricted to `m>0`, uniqueness
  of `X_0` is primary-fixture only, and both weight counts are controls.

## 9. N1--N8 Stress Test And Wall W1

- **N1:** Testing `P(m)` with all involution constraints, other carriers,
  and completion terms remains open.
- **N2:** Primary Hermiticity, the no-PD spectral bound, and the polar metric
  construction are separate finite statements.
- **N3:** The atlas, carrier, two weights, two corners, mass sign, and chosen
  half decomposition are explicit.
- **N4:** `S`, `P(m)`, and `W` are kept distinct throughout.
- **N5:** The exact resolution fence below states each quantifier.
- **N6:** The staggered Hermitian pairing and polar construction remain useful
  positive results despite the no-PD bound.
- **N7:** A singular PSD form, another carrier, or a completed physical block
  may evade the present wall.
- **N8:** No parent or flat-lane statement upgrades the finite spectra.

**W1.** On every primary edge, the measured `R` spectrum supplies a
two-dimensional totally isotropic subspace and hence positive index at most
six for a real symmetric symmetrizer. This excludes positive-definite `S` and
`P(m)`. It does not exclude PSD, decide admissible `W`, or prove reflection
positivity. This is not an OS no-go and not a curved OS no-go.

## 10. Firewalls And Independence

The actual ADM/history transporter remains unexecuted. The gravity constraint
quotient remains unexecuted. Reflection positivity, physical-block PSD,
forced self-edge resolution, coboundary admissibility, the joint-lane program,
Records, retention, axiom amendment, obligation retirement, and TOE movement
remain outside the claim. These are hard firewalls.

The historical solve/check round had **cross-context** checking within one
model family. This disclosure supplies provenance only. It is not independent
audit authority, and this corrected source does not synthesize an audit
verdict.

The original twenty-six-file source surface is preserved byte-for-byte under
`.claude/science/physics-loops/released-reflection-recovery-20260910/original/`.
The bounded helper extracts only the required definitions and records their
source commits, blobs, AST nodes, and line intervals. The reviewed Block 105
module is imported intact.

## 11. Exact N5 Resolution Fence

```text
N5: per_element: on the primary displayed fixture Q_ij=m H_q+K_ij with K_ij real antisymmetric and m-free on all sixteen edges; H_q-skewness of J_ij structurally gives purely imaginary semisimple spectrum in conjugate plus/minus pairs and an even characteristic polynomial, while invertibility and squarefreeness are separate sixteen-edge fixture computations and are not structural consequences
per_site: the fixed staggered site parity X_0 is H_q-self-adjoint, anticommutes with all sixteen primary-fixture J_ij, and makes X_0^dagger Q_ij Hermitian on all 16 primary-fixture edges; the one-dimensional common anticommutant proves uniqueness up to sign on the primary fixture only
per_mode: the specified adapted scout fails the primary-fixture Hermiticity test and the primary block-antidiagonal system excludes a half-exchanging anticommutant; on the +1 eigenspace the mass contribution is m H and is positive only for m>0, while the paired polar-decomposition construction proves the unique positive-cross-block H-isometric half exchange from the stated A,B,C hypotheses
per_block: for a real H-isometric half exchange whose physical block is symmetric, S=W^T beta is a real symmetric symmetrizer satisfying S R=R^T S, whereas the physical block is P(m)=S(m I+R); P(m) also symmetrizes R, so the positive index of either form is at most 6 on every primary edge, but zero and nonzero PSD algebraic S exist for the nilpotent Jordan form, whose real symmetric symmetrizer space has dimension 16 rather than 8, while the tested split probe has dimension 8 and two probes attain (6,0,2)
lattice_wide: the chart-indexed census is 4 nilpotent plus 12 split at the primary weights and 2 plus 14 at the second tested weights; the two assignments and the s_t=0 and s_x=0 corner fixtures retain only the no-positive-definite bound, and neither an all-weight claim nor positivity of P(m) follows
RESULT: the displayed primary fixture has a staggered Hermitian pairing and excludes positive-definite symmetrizers through the measured R spectra and positive-index bound; it does not exclude positive-semidefinite symmetrizers, does not turn S into P(m), and does not establish reflection positivity or a curved OS result
DECISION_CUT: test the physical block P(m), admissible involution constraints, other weights and carriers, completions, the forced self-edges, coboundary admissibility, and the joint-lane program; no premise or audit disposition is adopted here
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero
```

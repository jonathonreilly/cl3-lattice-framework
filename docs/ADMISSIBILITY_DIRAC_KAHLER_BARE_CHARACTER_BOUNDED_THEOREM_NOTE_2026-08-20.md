---
claim_id: admissibility_dirac_kahler_bare_character_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied 8x4 antiperiodic-cover fixture, its 64 affine covariant moves, 64-modulus carrier, sixteen healed edge differentials, and two displayed reflections"
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Bare Character on the Supplied Finite Fixture

**Type:** `bounded_theorem`

**Campaign block:** 153. **Status:** corrected bounded theorem; formal audit is
deferred. The original note, primary, cache, ledger, and generated-manifest
occurrence are recoverable in the released-7315-A recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py)
uses the finite cover and Hodge assembly from
[Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). They do not establish a
physical action, an OS-positive theory, or a continuum statement.

## Exact character

For the 64 covariant affine cover moves

\[
g=(\epsilon,p,\epsilon,q),\qquad
\epsilon\in\{\pm1\},\ p\in\mathbb Z_8,\ q\in\mathbb Z_4,
\]

define

\[
\kappa(g)=(p+q)\bmod 2.
\]

Direct composition of all \(64^2\) pairs gives
\(\kappa(gh)=\kappa(g)+\kappa(h)\pmod2\). Thus its kernel has 32
members: 16 translations and 16 reflections. On the supplied atlas this is
also the identity-gauge matching class. The displayed reflections satisfy
\(\kappa(\theta)=1\) for \(\theta=(-1,7,-1,0)\) and
\(\kappa(\theta')=0\) for \(\theta'=(-1,7,-1,1)\).

The same character controls staggered grading:

\[
gX_0=(-1)^{\kappa(g)}X_0g
\]

for all 64 descended moves.

## What parity proves

On the 64-modulus fixture the quotient Hodge matrix \(H_q\) commutes with
\(X_0\), while every one of the sixteen bare connection residues \(K\)
anticommutes with it. This forces grading-forbidden blocks to vanish. It does
not force a grading-allowed entry to be nonzero. In particular, the zero
operator obeys both homogeneous parity relations, and further support or
coefficient information is required for any liveness statement.

For the two displayed reflections the primary separately evaluates that extra
information:

* \(\theta\) has zero mass-Gram diagonal and four live connection-diagonal
  slots on each healed edge;
* \(\theta'\) has four live mass-Gram diagonal slots and zero
  connection-diagonal slots on each healed edge.

These are fixture calculations for those operators. They are not converses of
the parity rule. Likewise an \(X_0\)-odd completion fixes the forbidden
grading-diagonal part but may change off-diagonal blocks. Preserving a matrix's
diagonal does not preserve positivity; for example
\(\begin{psmallmatrix}1&t\\t&1\end{psmallmatrix}\) ceases to be positive
semidefinite when \(|t|>1\).

## Corrected forcing determinant and scan scope

For the chart-0/1 forcing matrix associated with \(\theta'\), the exact Gram
determinant is

\[
\det(F^{\mathsf T}F)=
\frac{(s_t^2+s_x^2)^6(4m^2+s_t^2+s_x^2)^2}{2^{48}}.
\]

It is zero at \(s_t=s_x=0\), rather than positive everywhere. Away from that
corner it is positive over the real parameter domain. On the slice \(s_t=0\),
the rank-eight statement therefore requires \(s_x\ne0\); the primary checks
the rational point \((s_x,s_t)=(3/5,0)\). The corresponding \(\theta\) matrix
has rank four there.

The historical positivity scan's declared domain is exactly five supplied
carrier fields, sixteen healed edges, the two displayed reflections, and the
single mass \(m=2/7\). The correction checks this domain cardinality; it does
not rerun or newly certify the historical positivity outcomes. It is not a
five-mass scan and does not prove a cone-wide existence or nonexistence
theorem. The defect ranks must also remain stratified: flat rank 0, selected
rank-8 witnesses, and generic rank 16 are different statements.

## Disposition

The character, the parity-forced zeros, the two explicitly measured diagonal
patterns, and the corrected determinant are retained at finite supplied-matrix
scope. Generic liveness, diagonal-only protection of a positivity object, and
the former everywhere-positive determinant wording are withdrawn. No operator
choice is adopted and no axiom, audit verdict, or TOE obligation changes.

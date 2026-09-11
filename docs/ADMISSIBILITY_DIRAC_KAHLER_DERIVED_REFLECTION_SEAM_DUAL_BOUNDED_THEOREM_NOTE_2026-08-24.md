---
claim_id: admissibility_dirac_kahler_derived_reflection_seam_dual_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "one convention-defined reflection, its dual Hodge identity, and selected finite shift averages"
depends_on:
  - admissibility_dirac_kahler_dual_patch_pullback_section_frame_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A convention-defined reflection and finite dual averages

**Type:** `bounded_theorem`

**Campaign block:** 183. **Status:** corrected bounded theorem; formal audit is
deferred. The five original changed-path occurrences, including the historical
manifest, remain recoverable exactly.

The [primary](../scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py)
uses the corrected [Block 182 finite frame](ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the current [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 matrices](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## The stipulated reflection convention

On the dimension-32 cover, let $P_e$ send $t\mapsto7-t$, let
$P_t=\operatorname{diag}(-1)^t$, and stipulate
$R=P_eP_t$. Then $R$ is real orthogonal and $R^2=-I$. Cell by cell, it
factorizes through

\[
M=\begin{pmatrix}
0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0
\end{pmatrix},\qquad M^2=-I,
\]

with the anchor sign $(-1)^t$. This square is convention-dependent: the
undressed site reflection and the constant unsigned corner swap both square
to $+I$. The calculation therefore does not derive a unique reflection
from the connection or Hodge construction. Locally, the stated $P_t$
matches the time-form parity after restriction to a cell, up to the displayed
anchor sign.

The reflected $d_{00}$ is rank-16 and nilpotent. Relative to the fixed
untransported grade it has 16 raising and 16 lowering entries; relative to the
transported grade it is purely raising. It differs from the eight named
$\pm d_{00},\pm d_{00}^\dagger,\pm d_{10},\pm d_{10}^\dagger$ controls.

## Dual block and Hodge identity

For the current cell Hodge $H(q,v)$, define the dual block by stipulation as
$H^\vee=M H(q,v)M^T$. For $q^2\ne1$ and $v\ne0$,

\[
H^\vee=
\begin{pmatrix}
-v/(q^2-1)&0&0&-qv/(q^2-1)\\
0&1/v&0&0\\0&0&v&0\\
-qv/(q^2-1)&0&0&-v/(q^2-1)
\end{pmatrix}.
\]

Its differences from six neighbouring expressions in the primary are
nonzero rational functions, not pointwise inequalities at every parameter.
For example, $H^\vee(0,1)=H(0,1)=I$.

On the supplied overlap field $g$, with the explicitly reflected field
$\theta g$,

\[
R H[g]R^{-1}=H^\vee[\theta g].
\]

Dropping the parity dressing or dropping the dual block fails on this fixture.
The same stipulated convention gives
$R U_tR^{-1}=-U_t^{-1}$ and $R U_xR^{-1}=U_x$.

## What the finite averages show

Pairwise weights $w_k=w_{-k}$ are sufficient for reflection closure. The
primary retains the 16 equal-weight unions of the five reflection orbits that
contain exponent zero as sufficient examples. They are neither exhaustive nor
16 distinct matrix points.

The carrier Hodge has temporal period four, so only weights aggregated modulo
four enter these averages. In particular,
$w_0=1/2,w_1=w_3=1/4$ closes even though $w_1\ne w_7$, and the exponent
sets $\{0\}$ and $\{0,4\}$ produce the same average. The displayed minimal
average and the full eight-exponent average do differ at 96 entries. No
necessary weight classification follows.

For the four-shift section with temporal exponents $\{0,1\}$, reflection sends
the right-hand dual average to temporal exponents $\{0,-1\}$. Transporting
that Hodge average together with the reflected differential extends the
identity through the stipulated completion at symbolic mass. Using the same
$\{0,1\}$ set on both sides is generally false on this carrier. This is a
finite matrix corollary, not an OS-positivity, temporal-link, two-history Gram,
selection-uniqueness, or physical-reflection theorem.

## Disposition

The convention-conditioned reflection, cell factorization, reflected
differential, symbolic dual identity with its domain, Hodge covariance,
conjugation table, sufficient average families, counterexamples to necessity,
and finite completion corollary are retained. Unique-reflection, pointwise
dual-separation, exhaustive weight, distinct-point census, positivity,
physical reflection, and uniqueness claims are withdrawn. Nothing is
registered or adopted.

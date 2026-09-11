---
claim_id: admissibility_dirac_kahler_positivity_window_characterization_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "One exact finite (m,c,v) chart: selected mass/shear/corner samples, exact determinant and complementary-minor interpolation, a unique simple Delta_8 root in one rational mass bracket, local openness at strictly positive samples, and a non-product witness. No identification of that root with the full PD boundary or global boundary geometry is claimed."
depends_on:
  - admissibility_dirac_kahler_curved_os_seam_glued_gram_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Positivity Chart and a Delta-8 Root

**Campaign block:** 187. **Type:** `bounded_theorem`. **Status:** corrected
finite claim; formal audit is deferred. No axiom or premise is adopted.

The [primary runner](../scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py)
uses the corrected [Block 185 finite Gram](ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 Hodge source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Exact finite chart

The primary rebuilds the Block 185 link construction with exact rational mass,
shear, and volume parameters. Five mass points at (c=5/13), exact shear
bisection points, two corners, and two finite robustness directions are primary
measurements. Four additional old mass values and two old corners occurred
only in a historical checker narrative; they remain archived history and are
not represented as fresh primary output.

At (c=5/13), exact bisection gives

\[
2911/2048 < m < 91/64
\]

with all eight leading minors positive at the lower endpoint and only
(\Delta_8<0) at the upper endpoint. The complementary 24-by-24 determinant
has degree at most 24, so 25 exact values determine it; four further values
check the recovered polynomial. Jacobi's identity gives, after cancellation,

\[
\Delta_8(m,5/13)=
\kappa\frac{A(m)^2B_-(m)B_+(m)}{F(m)^2G(m)^2},\qquad \kappa>0.
\]

The runner stores the displayed integer polynomials. Exact Sturm counts in the
bracket are (0,0,1) for (A,B_-,B_+), and
(gcd(B_+,B_+')=1). Thus the bracket contains one simple root of
(\Delta_8), carried by (B_+).

This is a **Delta-8 root**, not a certified boundary of the full positive
definite set. The seven lower leading minors have not been proved positive
throughout the bracket, so the root cannot be identified with the first loss
of positive definiteness from the available calculation.

## Samples, openness, and non-product structure

The 32-by-32 action determinant is an affine-pencil polynomial of degree at
most 32. Thirty-three exact values recover
(F(m)^2G(m)^2/C). Both (F) and (G) are even polynomials with positive
coefficients and no real roots. Hence the displayed chart is nonsingular on
the real mass ray. At every strictly positive finite Gram sample, continuity
of its finitely many leading minors supplies a local open neighborhood.

The point ((m,c)=(1,5/13)) is positive, and
((9/20,3/5)) is positive, while their crossed point ((1,3/5)) fails. This
proves that the positive set in the displayed chart is not the Cartesian
product of those two positive coordinate legs.

The first nonpositive leading-minor indices at the selected mass endpoint,
shear endpoint, and corner are respectively 8, 7, and 6. They are sampled
diagnostic indices. They do not establish boundary sheets, curvature, a
monotone mass/shear tradeoff, or the absence of a single algebraic boundary
curve.

## N1 — Alternative routes

Lower-minor interval certification, cell decomposition, direct semialgebraic
analysis, and other chart coordinates remain available.

## N2 — Wall independence

The Delta-8 root, sampled minor indices, and non-product witness answer
different finite questions; none determines global boundary topology.

## N3 — Hidden walls

The result fixes one carrier, glue, reflection, volume convention, and exact
rational parameter chart.

## N4 — Residual matching

Polynomial degree bounds determine the interpolation counts. Extra nodes and
direct Gram values check the recovered identities.

## N5 — Rhetoric audit

“Root of Delta-8” is used throughout. “Positivity boundary” is reserved for a
future proof controlling all lower minors.

## N6 — Partial closure paths

The simple-root bracket and local positive neighborhoods provide bounded input
for a later lower-minor or semialgebraic study.

## N7 — Steelman

A full boundary theorem would prove all seven lower minors positive up to the
root, then analyze any other boundary components in the declared chart.

## N8 — Cross-cycle echo

Historical checker-only points stay identified as historical; they are not
silently upgraded by a prior PASS cache.

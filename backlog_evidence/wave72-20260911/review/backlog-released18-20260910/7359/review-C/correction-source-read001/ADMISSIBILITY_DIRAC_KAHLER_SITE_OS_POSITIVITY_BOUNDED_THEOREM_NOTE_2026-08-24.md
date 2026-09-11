---
claim_id: admissibility_dirac_kahler_site_os_positivity_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "One exact 8x4 carrier: finite link-seam sector blocks and three failed repair families on p=0,2; one site-reflection construction with rank-eight PSD Grams on three spans at three fixtures; one rejected naive transfer; and a fixed-index diagonal-congruence distinction. No universal left-dressing, unique obstruction, general gauge, physical equivalence, reconstruction-transfer, or gravity theorem is claimed."
depends_on:
  - admissibility_dirac_kahler_positivity_window_characterization_bounded_theorem_note_2026-08-24
  - admissibility_dirac_kahler_curved_os_seam_glued_gram_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Link-Seam and Site-Reflection Results

**Campaign block:** 188. **Type:** `bounded_theorem`. **Status:** corrected
finite claim; formal audit is deferred. No axiom or premise is adopted.

The [primary runner](../scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py)
uses the corrected [Block 187 finite chart](ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the corrected [Block 185 finite Gram](ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 Hodge source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Link-route seam blocks

At ((m,c)=(9/20,5/13)), the link-reflection action has signed band census
({-2:24,-1:56,0:96,1:56,2:24}). Its 16-by-16 theta-paired seam is full rank
with inertia ((8,8,0)).

For spatial momentum (p=0,1,2,3), the near and far 2-by-2 blocks are

\[
C^{\rm near}_p=
\begin{pmatrix}
-601/576 &(65/1152)(-i)^p\\
(65/1152)i^p&0
\end{pmatrix},\qquad
C^{\rm far}_p=
\begin{pmatrix}
-601/576 &(65/1152)i^p\\
(65/1152)(-i)^p&0
\end{pmatrix}.
\]

Thus every displayed determinant is
(-|65/1152|^2<0), forcing each nonzero-coupling block to be indefinite.
This finite identity does not show that shear is the sole obstruction, nor
that setting a thickness parameter to zero repairs the raw Gram.

On the real sectors (p=0,2), the exact sign operator supplies three finite
controls. The sandwich (SKS^T) is an invertible congruence and retains
inertia ((2,2,0)). The left product (SK) has 12 asymmetric entries and
fails the Hermitian positive-pairing requirement. Three action-side polar
writings give Gram inertias ((2,2,0)), ((2,2,0)), and ((0,4,0)).

The general theorem used here is only Sylvester's law for an invertible
congruence (T^TKT), or (T^\dagger K T) in the complex case. Reality alone
does not turn arbitrary left multiplication into congruence. For example,
(K=\operatorname{diag}(1,-1)) and (S=\operatorname{diag}(1,-1)) give
(SK=I) but (SKS=K).

## Site-reflection construction and PSD certificate

The separately constructed site-reflection Hodge is invariant under the bare
site permutation; the shear-flipped image fails at 64 entries. Its 56-entry
odd glue yields reflected-transpose covariance. The completed action is not an
ordinary symmetric matrix, and applying the site permutation to the link
action fails covariance at 240 entries.

The block between slices ({1,2,3}) and ({5,6,7}) is empty in both
directions. Each term (mH), (HD_s), and (-D_s^TH) is separately zero on
that block, so this is support emptiness rather than cancellation.

The reflected Gram on slices ({1,2}) is positive definite. After reordering
the two larger spans to put that eight-dimensional core first, their Schur
complements are exactly (0_4) and (0_8). This congruence certificate gives
inertias

\[
(8,0,0),\quad(8,0,4),\quad(8,0,8)
\]

on ({1,2}), ({1,2,3}), and ({0,1,2,3}). The same finite inertia
triples occur at ((1,5/13)) and ((9/20,3/5)). Three fixtures are not a
parameter window.

The naive single-readout candidate (T=K_c^{-1}L) is not
(K_c)-self-adjoint: both (L-L^T) and (K_cT-T^TK_c) have 48 nonzero
entries. Its exact characteristic polynomial has factor degrees (2,2,4)
and a census of two roots in ((0,1)), two negative real roots, and four
nonreal roots. It therefore is not the desired positive reconstruction
transfer; constructing the proper quotient transfer remains open.

The site and link positive cores are unequal. Their fixed-index triangle
products have opposite signs, which excludes real nonsingular **diagonal**
congruence in the displayed ordering. It does not exclude relabelings,
arbitrary gauge maps, or general congruence. Indeed any two SPD matrices are
congruent. No physical inequivalence follows.

## Historical diagnostics

The complete 354-line original sidecar is preserved in the recovery packet.
Its open-half B9 variant changed the finite (D_s) and (Q_s) while retaining
the reported covariance and PSD inertias. That is historical alternative
evidence, not a newly executed result and not a uniqueness theorem.

The old 16-dimensional companion census of three positive, three negative,
one zero, and nine nonreal roots was not produced by the primary. It is also
inconsistent with conjugate pairing for a real characteristic polynomial, so
it remains an explicitly rejected historical diagnosis.

## N1 — Alternative routes

The B9 open-half construction, non-diagonal changes of basis, genuine
reconstruction quotients, and other site/link spans remain open.

## N2 — Wall independence

The link-seam indefiniteness, three polar controls, site PSD certificate, and
naive-transfer failure concern different matrices and are not one universal
wall.

## N3 — Hidden walls

All results fix one 8-by-4 carrier, named reflections, one completion, selected
spans, and three parameter points.

## N4 — Residual matching

Near and far phases are checked separately in every momentum sector. PSD uses
an exact Schur complement rather than a leading-minor string containing zeros.

## N5 — Rhetoric audit

The terms “diagonally congruent,” “finite control,” and “naive candidate” name
the exact scope. General gauge and physical claims remain open.

## N6 — Partial closure paths

The site PSD core and failed naive transfer isolate the next bounded task:
construct the actual reconstruction quotient and its induced transfer.

## N7 — Steelman

A stronger result would define the admissible gauge group, build the physical
quotient, and prove positivity or a complete obstruction across that class.

## N8 — Cross-cycle echo

Historical parent-standing language, unavailable campaign diagnoses, and
sidecar-only claims are recovery material. Current sources and fresh primary
outputs alone support the live finite claims.

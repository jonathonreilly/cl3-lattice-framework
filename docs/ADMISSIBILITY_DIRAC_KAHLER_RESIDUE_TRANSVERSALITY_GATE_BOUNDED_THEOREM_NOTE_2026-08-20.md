---
claim_id: admissibility_dirac_kahler_residue_transversality_gate_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied eight odd-shear coordinates, three displayed linear loci, exact theta/theta-prime mass Grams, and sixteen bare edge residues"
depends_on:
  - admissibility_dirac_kahler_discriminator_verdict_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Residue Loci and Their PSD Intersections on the Finite Fixture

**Type:** `bounded_theorem`

**Campaign block:** 156. **Status:** corrected bounded theorem; formal audit is
deferred. All original source and cache versions are preserved in the
released-7315-A recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py)
uses the finite matrices fixed in [Block 155](ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
[Block 154](ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md),
and [Block 153](ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md),
with the cover construction from [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Exact mass Gram

Order the odd shear coordinates as

\[
(b_{10},b_{11},b_{12},b_{13},b_{30},b_{31},b_{32},b_{33}).
\]

The theta-prime Hermitian mass Gram has four live diagonal entries

\[
\frac14(b_{30},b_{32},-b_{10},-b_{12})
\]

on slots \((0,2,5,7)\), together with the dead hyperbolic entries

\[
G'_{13}=\frac{b_{31}+b_{33}}8,
\qquad
G'_{46}=-\frac{b_{11}+b_{13}}8.
\]

Its Hermiticity locus has constraint rank two and dimension six. The theta
locus has rank four and dimension four. These are ranks of the explicitly
displayed linear constraint maps, not basis-dependent properties.

On the two supplied sign branches represented in the primary, the nonzero
mass Gram has inertia \((2,4,2)\): two positive, four zero, and two negative
directions. The zero-connection counterpoint instead has inertia \((4,4,0)\).
These are finite-form statements; no cone-wide physical positivity claim is
made.

## Three linear loci

Let \(R\) exchange coordinate pairs

\[
(0,3),(1,2),(4,7),(5,6).
\]

Then \(L_{145}=\ker(R-I)\) and \(L_{147}=\ker(R+I)\) each have dimension four,
meet only at zero, and span the eight-dimensional odd-shear space. Let

\[
L_{154}=\{b_{11}+b_{13}=0,\ b_{31}+b_{33}=0\},
\]

which has dimension six. Each intersection
\(L_{145}\cap L_{154}\) and \(L_{147}\cap L_{154}\) has dimension two. They
are therefore nonzero linear intersections.

Using coordinates \((p,q)\) on either intersection, the live diagonal is,
up to the displayed overall factor and a simultaneous sign reversal,

\[
(q,-q,-p,p)/4.
\]

For nonzero mass its PSD portion forces \(p=q=0\). At zero mass the entire
pairing vanishes for every \((p,q)\), so positivity does not imply that the
carrier coordinates vanish. Thus “the loci meet only at the dead carrier” is
valid only after the PSD restriction and a nonzero-mass hypothesis; it is
false as a statement about the linear spaces.

## Bare residue channels

For all sixteen supplied bare healed-edge residues, the live-live blocks of
both

\[
\operatorname{Anti}[\theta'K]_{++},\qquad
\operatorname{Herm}[X_0K]_{++}
\]

vanish, while the dead-live controls remain nonzero. This is a finite
selection-rule result. It does not identify a physical indefinite-metric
constraint or prove that every enlarged support has the same property.

## Disposition

The exact Gram structure, locus dimensions, nonzero intersections, their
nonzero-mass PSD restriction, and the stated bare residue blocks are retained.
The unqualified dead-intersection claim and any inference at zero mass are
withdrawn. No reflection, carrier, action, or constraint interpretation is
adopted.

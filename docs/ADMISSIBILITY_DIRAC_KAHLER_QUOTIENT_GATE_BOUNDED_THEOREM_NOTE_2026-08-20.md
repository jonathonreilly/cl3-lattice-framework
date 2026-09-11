---
claim_id: admissibility_dirac_kahler_quotient_gate_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied eight-coordinate mass Gram, the displayed 2x4 odd-cell incidence map, its zero-sum image, and two exact sign representatives"
depends_on:
  - admissibility_dirac_kahler_residue_transversality_gate_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A Zero-Sum Restriction of the Finite Mass Gram

**Type:** `bounded_theorem`

**Campaign block:** 158. **Status:** corrected bounded theorem; formal audit is
deferred. The exact original and successor primary versions, including the
successor's rational substitutions, are preserved in the released-7315-A
recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py)
uses the exact Gram in [Block 156](ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the corrected cancellation distinction in [Block 155](ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the finite assembly in [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Incidence image

On the eight odd cells of the supplied 2-by-4 periodic lattice, orient eight
spatial links and four links joining the two time rows. Their incidence matrix
\(A\) is 8-by-12, has rank seven, and obeys

\[
\mathbf 1^{\mathsf T}A=0.
\]

Consequently

\[
\operatorname{im}A=Z:=\ker(\mathbf 1^{\mathsf T}),
\qquad \dim Z=7.
\]

The image clause follows from the first two facts and the dimension count; it
is not an independent numerical test. Under the full permutation action on
the eight coordinates, \(Z\) is the standard representation. If a nonzero
invariant subspace contains a nonconstant zero-sum vector \(v\), then for some
transposition \((ij)\), \(v-(ij)v\) is a nonzero multiple of \(e_i-e_j\).
The permutation orbit of this difference spans \(Z\). This gives the short
irreducibility argument behind the invariant-subspace statement.

No identification of \(A\) as a physical Gauss-law operator is made.

## Restriction and radical quotient

The two displayed nonzero sign representatives of the unreduced Block 156
Gram have inertia \((2,4,2)\). Since \(Z\) has codimension one, restriction can
remove at most one negative direction:

\[
n_-(G'|_Z)\ge n_-(G')-1=1.
\]

Thus a nonzero positive-semidefinite result was already impossible for this
codimension-one decision object. The exact restriction is stronger at both
representatives:

\[
\operatorname{inertia}(G'|_Z)=(2,3,2).
\]

Quotienting by its three-dimensional radical gives a four-dimensional
nondegenerate form with inertia \((2,0,2)\). Removing the radical removes zero
directions and leaves both negative directions. This is finite exact linear
algebra, not a physical quotient action.

The original fifteen variant scan, 28 coordinate-pair scan, and residue Lie
closure remain recoverable as historical exploration. They are not needed for
this corrected theorem and are not promoted as an exhaustive search.

## One selection rule, plus one inequality

Bare grading oddness forces the grading-diagonal blocks of each residue to
vanish. It does not force the full 8-by-16 reflected row to vanish: the bare
mixed-half control is nonzero. The stronger full-row zero in Block 155 uses
the selected deletion/support. Accordingly the completed and bare zeros are
not independent structural mechanisms. The additional content here is the
codimension/inertia inequality and its exact finite restriction.

## Disposition

The incidence rank and image, the forced negative-index floor, the two exact
restricted inertias, and the radical quotient are retained. An unreachable
binary branch is not described as a discovery. Full-row invisibility is not
attributed to parity alone, and no constraint, action, carrier, or quotient is
adopted physically.

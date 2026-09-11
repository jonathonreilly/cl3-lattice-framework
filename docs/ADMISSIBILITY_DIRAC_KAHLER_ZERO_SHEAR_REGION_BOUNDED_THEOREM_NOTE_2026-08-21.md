---
claim_id: admissibility_dirac_kahler_zero_shear_region_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "the formal 8-by-4 x-trivial adjacent-slice forms at zero temporal coupling and one named nonzero-coupling control"
depends_on:
  - admissibility_dirac_kahler_site_reflection_channel_bounded_theorem_note_2026-08-21
runner: scripts/admissibility_dirac_kahler_zero_shear_region_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A Zero-Temporal-Coupling Region on the Finite Fixture

**Type:** `bounded_theorem`

**Campaign block:** 164. **Status:** corrected bounded theorem; formal audit is
deferred. The historical five-path state remains in the released-7315-B
recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_zero_shear_region_2026_08_21.py)
uses corrected [Block 163](ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md),
the [Block 159 supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Exact block form at \(s_t=0\)

For each of the four x-trivial site involutions and each of the sixteen supplied
healed edges, write the adjacent-slice form as

\[
 P=\begin{pmatrix}B&C\\ C^*&E\end{pmatrix}.
\]

At \(s_t=0\), \(B\) is free of every shear moment, \(E=0\), and \(C\)
depends only on the eight shear moments on the two links incident to the fixed
slice. At \(m=1\) and \(s_x=3/5\), the coefficient map from those eight
moments to the independent entries of \(C\) has rank eight in every one of
the 64 cells. At this explicit dial, the rank calculation, rather than support
alone, proves that \(C=0\) exactly when those eight formal coordinates vanish.

After that pinning,

\[
 P=\operatorname{diag}(mD_0,mD_1,mD_2,mD_3,0,0,0,0),
\]

where every \(D_x\) is an explicit sum of positive Hodge moduli. The form is
positive semidefinite for \(m>0\), zero for \(m=0\), and negative
semidefinite for \(m<0\), at this x-trivial zero-coupling scope.

## Flip and continuation scope

Negating all shear moments sends \(P\) to \(JPJ\), with
\(J=\operatorname{diag}(I_4,-I_4)\), throughout the same \(s_t=0\)
formal family. At the named curved carrier with \(s_t=1/5\), this congruence
fails and the form has inertia \((5,0,3)\). The flip identity is therefore
restricted to zero temporal coupling.

The hollow-corner block form explains why a nonzero \(C\) obstructs
semidefiniteness within this family. It does not classify carriers away from
the pinned region, and it does not show that every possible nonzero-coupling
continuation fails.

## Disposition

The 64 formal block identities, rank-eight local coefficient maps at the
stated dial, positive
diagonal normal form, and zero-coupling flip congruence are retained. The
nonzero-coupling congruence, global complementarity, and off-region
classification are withdrawn.

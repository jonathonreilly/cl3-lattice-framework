---
claim_id: admissibility_dirac_kahler_scaling_probe_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "four supplied finite sizes, edge (2,2), and every x-trivial fixed slice at each size"
depends_on:
  - admissibility_dirac_kahler_zero_shear_region_bounded_theorem_note_2026-08-21
runner: scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Four Finite Scaling Probes

**Type:** `bounded_theorem`

**Campaign block:** 165. **Status:** corrected bounded theorem; formal audit is
deferred. The original note, primary, cache, ledger, and manifest remain
recoverable in the released-7315-B packet.

The [primary](../scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py)
uses corrected [Block 164](ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md),
the [Block 159 supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Enumerated finite sizes

The source rebuilds the same local antiperiodic construction at cover sizes
\(8\times4\), \(12\times4\), \(8\times6\), and \(16\times4\). The
numbers of site involutions are respectively 24, 36, 32, and 48. Pinning the
two incident shear rows leaves formal \((\nu,\sigma)\)-coordinate dimensions

\[
24,\quad 40,\quad 36,\quad 56.
\]

These are enumerated finite fixture values. They are consistent with
\(2L_x(T_{\rm phys}-1)\) on these four fixtures, but the source does not
promote four points to an all-size theorem.

## Rank and coupling checks

For edge \((2,2)\), every x-trivial fixed slice at all four sizes is checked
at \(m=1\) and \(s_x=3/5\). The coefficient matrix from the \(2L_x\)
incident shear coordinates to the zero-coupling cross block has rank \(2L_x\).
On the displayed exact graded carrier with free-cell shear \(\sigma=1/3\) at
the same \(m=1,s_x=3/5\) dial, the temporal coefficient \(C_1\) has rank
\(L_x\) at every one of the 22 tested slice cells. These independent-entry
ranks supply the liveness step that support enumeration alone could not prove.

All 22 adjacent-slice forms are affine in \(s_t\). On that same numeric graded
carrier, their pinned \(s_t=0\) specializations have inertia
\((L_x,L_x,0)\). The lower-right linear coefficient \(E_1\) is nonzero on two
of four fixed slices for each \(T_{\rm phys}=4\) fixture, and zero on every
tested slice at \(T_{\rm phys}=6\) and 8. This records a finite wrap effect
rather than a size-universal mechanism.

## Disposition

The four finite dimension counts, involution counts, independent-entry ranks,
affinity, zero-coupling inertias, and finite \(E_1\) census are retained.
Claims about every size, every edge, every carrier, or all nonzero-coupling
continuations are withdrawn.

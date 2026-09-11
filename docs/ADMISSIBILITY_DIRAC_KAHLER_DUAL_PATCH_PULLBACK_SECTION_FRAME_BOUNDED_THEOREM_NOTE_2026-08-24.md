---
claim_id: admissibility_dirac_kahler_dual_patch_pullback_section_frame_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "exact pullback, grade, signed-shift, and periodic/antiperiodic controls on the supplied 8-by-4 carrier"
depends_on:
  - admissibility_dirac_kahler_common_differential_section_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Pullback and signed-shift controls on the supplied section

**Type:** `bounded_theorem`

**Campaign block:** 182. **Status:** corrected bounded theorem; formal audit is
deferred. The five original changed-path occurrences, including the historical
manifest, remain recoverable exactly.

The [primary](../scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py)
uses the corrected [Block 181 section](ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the current [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 matrices](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Pullback and degree

Let $A=\frac12(S_o)_o$ be the dimension-$128\times32$ graph isometry,
$D_{\rm patch}=\operatorname{diag}(d_o)$, and
$H_{\rm patch}=\operatorname{diag}(H,H,H,H)$. On the supplied matrices,

\[
A^TA=I,\quad D_{\rm patch}A=Ad_{00},\quad
A^TH_{\rm patch}A=H_s,
\]

and the same pullback holds for
$Q(H,d)=mH+i(Hd+d^\dagger H)$ at symbolic positive $m$.

The cover and quotient exterior grades raise $d_{00}$ by one. Repeating one
canonical grade independently on all four patches gives a rank-48 defect,
whereas transporting the grade with each chart makes the defect vanish and
intertwines it with $A$. This is an exact finite cotransport identity.

## Signed shifts and Hodge covariance

For $\epsilon_x=\operatorname{diag}(-1)^x$, the displayed signed temporal
lift $\widetilde U_t=\epsilon_xU_t$ anticommutes with $U_x$ and satisfies
$\widetilde U_t^2=U_t^2$. The two-step flat completion controls commute;
the one-step temporal commutator has rank 24. Conjugating $d_{00}$ by
$\widetilde U_t$ gives another rank-16 nilpotent and matches the explicitly
signed $d_{10}$ image.

The parameterized current Hodge matrix is covariant under plain spatial and
temporal shifts. The signed temporal lift instead implements the displayed
shear flip. Omitting the flip on the signed side and adding it on the plain
side each gives rank 32. These are matrix identities on one supplied field;
they do not establish a Ward contraction or a complex gauge principle.

## Periodic and antiperiodic finite operators

The reconstructed periodic $4\times4$ fine differential and the
antiperiodic quotient differential are both $16\times16$, but have ranks six
and eight. They differ at 32 matrix entries, only four of which lie on the
temporal seam, and the antiperiodic matrix is not obtained merely by negating
the periodic seam entries. Rank invariance bars similarity of this pair. The
entry census does not prove that the twist alone causes the rank difference.

The periodic differential therefore has four-dimensional cohomology, while the
antiperiodic displayed complex is acyclic with an eight-dimensional kernel as
described in Block 181.

## Disposition

The exact pullback, cotransported grade, signed-lift controls, Hodge
shift/flip identities, and finite rank/census contrast are retained. Causal
twist language, empty-kernel wording, Ward, complex-gauge, gravity, and global
boundary classifications are withdrawn. Nothing is registered or adopted.

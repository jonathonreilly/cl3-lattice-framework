# Block 168 corrected bounded note: shim and zero-diagonal scope

**Type:** `bounded_theorem`

**Primary runner:** [Corrected finite producer](../scripts/admissibility_dirac_kahler_shim_zero_diagonal_2026_08_21.py)

The finite fixture uses the local construction in [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md), under the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). Only the specified constructor data is used; no broader parent conclusion is adopted.

Status: **corrected bounded source candidate**. Any producer output is separate provisional evidence that requires source-identity review and acceptance. This note records a 12x4 Schur identity, an 8x6 wrap control, and selected connection-off maps. It is not an all-cone theorem or a physical closure claim. Formal audit is deferred.

## Correct Schur statement

At the named 12x4 fixture, on the positive graded carrier with `m=1`, the corrected producer checks

\[
 P(s_t,g_2)=
 \begin{pmatrix}
 B&s_t C_1\\
 s_t C_1^\dagger&g_2s_t^2I
 \end{pmatrix},
 \qquad C_1^\dagger B^{-1}C_1=\frac{57}{160}I.
\]

This displayed closed form is a 12x4 identity only. For `B` positive definite and `s_t` nonzero, the Schur complement gives

\[
 P\succeq0
 \quad\Longleftrightarrow\quad
 g_2I-C_1^\dagger B^{-1}C_1\succeq0.
\]

At `s_t=0`, the added corner and cross block both vanish, so feasibility is independent of `g_2`; the cross rank is zero. Statements that the cross has rank `L_x` therefore require `s_t != 0`.

For a general positive corner profile `P_0`, the condition is

\[
 g_2P_0-C_1^\dagger B^{-1}C_1\succeq0,
\]

so the threshold is a generalized eigenvalue and depends on `P_0`. The producer includes `P_0=diag(2,3,4,5)` as a finite control; it must not be replaced by the identity-corner threshold.

## Size and uniformity qualifications

At 8x6, where the physical time extent is four, the homogeneous displacement-two addition used above maps to rank zero in the selected reflected corner. The pre-existing wrap corner is live. The 12x4 block formula and its threshold therefore do not transfer to 8x6.

For an imposed profile `g_2 s_t^k`, the nonzero-point condition is

\[
 g_2\geq \kappa s_t^{2-k},\qquad \kappa=57/160
\]

at the named 12x4 carrier. The producer tests `k=2,4,6` at `s_t=1/2` and `s_t=2`. These are pointwise statements. As positive `s_t` approaches zero, the required bound stays finite for `k=2` and diverges for `k=4,6`. Thus `k=4,6` do not admit a fixed finite coupling uniform near zero. This does not classify arbitrary profiles or arbitrary positive corners.

## Cancellation and diagonal scope

The selected connection-off mass map is evaluated at `s_x=s_t=0`. Its incident-shear coefficient map has rank eight at nonzero mass on the 12x4 fixture and vanishes at zero mass. An x-homogeneous, unit-volume restriction has two named shear variables and rank two. These facts require nonzero mass and do not rule out cancellation between the mass term and a nonzero connection.

The zero-diagonal assertions are restricted to the explicitly constructed reflected corners. A traceless nonzero Hermitian principal block obstructs positivity because a positive-semidefinite matrix has positive-semidefinite principal blocks. Tracelessness alone cannot exclude the zero block; cross and remaining diagonal conditions must be checked separately.

## Disposition of the historical claim families

| Original group | Corrected disposition |
|---|---|
| A, authority and evidence | Current literal inputs replace stale pins; the old cache and manifest node are archive-only. |
| B, fixture anchors | Retained at 12x4 and 8x6 with explicit size labels and inertia order. |
| C, cancellation gate | Narrowed to the nonzero-mass connection-off and x-homogeneous maps; connection cancellation remains unresolved. |
| D, shim profile | Retained at 12x4 with the `B>0`, `s_t!=0`, and corner-profile hypotheses. |
| E, zero-diagonal identities | Retained for the selected constructed objects; no mixed-displacement or all-operator extension. |
| F, diagnostic/blindness | Preserved in the immutable original archive as historical and unreproduced. This reduced producer supplies no current acceptance of the diagnostic/blindness family. |
| G, wrap and carrier tables | Split by size; 8x6 is a zero-rank control and the six-carrier table is not an all-cone proof. |
| H, result and closure prose | Rejected. No empty locus over all carriers/generators, physical route closure, or TOE movement follows. |

No imposed displacement-two term is registered as a primitive. Any corrected cache or manifest remains separate evidence subject to exact source binding, review, and acceptance.

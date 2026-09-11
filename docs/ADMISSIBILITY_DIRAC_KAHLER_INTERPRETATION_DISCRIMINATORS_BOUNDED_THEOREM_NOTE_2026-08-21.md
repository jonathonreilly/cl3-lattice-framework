---
claim_id: admissibility_dirac_kahler_interpretation_discriminators_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "named 12-by-4 and 8-by-4 carriers, edge (2,2), one temporal generator, and explicitly separated pairing, action, metric, Schur and wrap calculations"
depends_on:
  - admissibility_dirac_kahler_scaling_probe_bounded_theorem_note_2026-08-21
runner: scripts/admissibility_dirac_kahler_interpretation_discriminators_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Pairing, Action, and Margin Discriminators

**Type:** `bounded_theorem`

**Campaign block:** 166. **Status:** corrected bounded theorem; formal audit is
deferred. The original note, primary, cache, ledger, manifest, and handoff
append are preserved in the released-7315-B recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_interpretation_discriminators_2026_08_21.py)
uses corrected [Block 165](ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md),
the [Block 159 supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Pairing, action, and metric are separate objects

On the displayed 12-by-4 region carrier and edge \((2,2)\), the reflected
adjacent-slice pairing at \(s_t=0\) is independent of all free shear moments.
Those same moments occur in the full quotient action and in the quotient Hodge
metric. Thus they are invisible to this pairing functional, not absent from the
carrier or action.

With the three stated links pinned, the action's displayed
\((c+1,c)\) block is zero at \(s_t=0\). A separate off-region control turns
on a link shear and finds rank four in the corresponding \(H_q\) metric block.
The control is a metric calculation; it is not mislabeled as an action result.
Neither finite calculation classifies other slices, edges, or off-region
carriers.

## Hollow corner and two margin branches

For the named 12-by-4 graded carrier with fixed slice \(c=1\), free-cell shear
\(\sigma=1/3\), \(m=1\), and \(s_x=3/5\), the full adjacent-slice pencil is

\[
B=\frac{57}{40}I_4,\qquad
C=s_t\,\operatorname{diag}(57,-57,57,-57)/80,\qquad E=0.
\]

Consequently

\[
C_1^*B^{-1}C_1=\frac{57}{160}I_4.
\]

The raw Schur coefficient is \(57/160\). The Frobenius norm of \(P(0)\) is
\(57/20\), so the coefficient for the normalized quantity
\(\lambda_{min}(P)/\lVert P\rVert_F\) is \(1/8\). These coefficients must
not be conflated. The source also stipulates the Hermitian block pencil
\[
\begin{pmatrix}B&gC_1\\ \overline g C_1^*&0\end{pmatrix}.
\]
Its real-\(g\) slice is the displayed fixture form, while no identification
with a general complex connection is claimed. Its Schur complement is
\(-(57/160)|g|^2 I_4\), so full rank of \(C_1\) excludes nonzero \(g\)
within this stipulated block pencil. Other generators, complex connection
constructions, and carriers remain open.

The 8-by-4 wrap carrier at the same \(c=1\), free-cell \(\sigma=1/3\),
\(m=1\), and \(s_x=3/5\) dial is a different branch. Its lower-right
coefficient \(E_1\) has eigenvalues \(-7/64,0,0,7/64\), so the kernel splits
linearly at first order and \(\lambda_{min}\) has negative linear
\(O(|s_t|)\) behavior. The quadratic Schur law does not describe this
\(E\)-live branch. Moreover the Hodge coordinate is exactly

\[
b=-\frac{\nu\sigma}{1-\sigma^2};
\]

it is only leading-order linear in \(\sigma\) near zero.

## Flip and interpretation scope

The block-signature flip congruence holds at \(s_t=0\) and fails at the named
\(s_t=1/5\) point. The free shears remain live in the full action even where
the pairing does not see them. The source makes no Page-Wootters,
superselection, or physical-record conclusion.

The historical two-cone census and terminal statement are archived as
provenance rather than rerun or adopted. A finite failure while remaining on
the pinned zero-coupling region does not classify off-region continuation.

## Disposition

The scoped action zero, explicitly labeled metric control, pairing/action
distinction, conditional hollow-corner calculation, separate raw and
normalized coefficients, linear wrap branch, chart order, and zero-coupling
flip are retained. Global two-cone, physical interpretation, nonzero-coupling
flip, and off-region exclusion claims are withdrawn.

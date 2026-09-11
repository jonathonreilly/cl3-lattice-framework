---
claim_id: admissibility_dirac_kahler_discriminator_verdict_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied finite cover, the selected Block 154 deletion representative, its finite matrix controls, and the displayed transfer pair"
depends_on:
  - admissibility_dirac_kahler_unique_completion_price_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Discriminators for the Selected Completion

**Type:** `bounded_theorem`

**Campaign block:** 155. **Status:** corrected bounded theorem; formal audit is
deferred. The released-7315-A recovery packet preserves every original source
and cache version.

The [primary](../scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py)
re-solves the finite [Block 154 completion](ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md)
using the [Block 153 grading](ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md)
and the finite assembly in [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) delimit interpretation.

## Selected representative and finite controls

The support-restricted solve again produces 32/16 and 48/24
support/deletion profiles. The active deletion is the part visible to the
theta-prime half-pairing; the complementary 16 or 24 hops on each edge are
left untouched. Hence the selected representative is unique only after its
minimal-support and zero-free-parameter convention is stated. It is not the
unique member of every larger completion space.

For the supplied matrices at generic symbolic `s_x` and `s_t`, the deletion
strictly reduces the differential rank on all sixteen edges. Fourteen ranks go
from 16 to 10; the two edge keys `(2, 2)` and `(3, 3)` go from 16 to 8. This
exact finite census rules out an invertible similarity between each generic
bare/completed pair. It does not assert those ranks at every specialization or
turn an arbitrary congruence into a similarity argument.

For this particular deletion,

\[
P_+^{\mathsf T}\theta'K_c=0
\]

as a full 8-by-16 row on all sixteen edges. The bare mixed half block remains a
nonzero control. This stronger cancellation depends on the selected support
and coefficients. Bare staggered parity alone only kills grading-diagonal
blocks and does not imply a full-row zero.

## Correct transfer predicates

At the supplied exact transfer carrier, whose only nonzero shear-field values
are \(\sigma_{10}=\sigma_{12}=3/5\) and
\(\sigma_{30}=\sigma_{32}=-3/5\), with every volume equal to one, and at mass
one, define

\[
P_0=P_+^{\mathsf T}\theta'Q_cP_+,
\qquad
P_2=P_+^{\mathsf T}\theta'Q_c\tau_2P_+,
\qquad
T=P_0^+P_2.
\]

There are three distinct questions:

1. \(T\) descends to \(V/\ker P_0\) precisely when
   \(T\ker P_0\subseteq\ker P_0\).
2. The right-factor equation \(P_2=S P_0\) requires
   \(\ker P_0\subseteq\ker P_2\).
3. The unreduced left equation \(P_0T=P_2\) requires
   \(\operatorname{range}P_2\subseteq\operatorname{range}P_0\), equivalently
   \((I-P_0P_0^+)P_2=0\).

At this witness \(\dim\ker P_0=4\). The operator \(P_2\) does not kill that
kernel, so the right-factor condition fails. The pseudoinverse kills its
\(P_2\)-image, however, and \(T\ker P_0=0\). Thus \(T\) *does* descend. The
range residual is nonzero, so the specific pseudoinverse candidate does not
solve \(P_0T=P_2\) on the unreduced space. The former non-descent claim used
the wrong predicate and is withdrawn.

## Compression and disposition

`SELECT M LIFT` remains a formal compression unless
\(M\,\mathrm{LIFT}=\mathrm{LIFT}\,q\) is separately established. No physical
quotient action follows from the compression. The finite rank drop, selected
full-row cancellation, and corrected transfer facts are retained. The former
automatic branch verdict, basis-dependent rank explanation, and transfer
non-descent claim are withdrawn. The other historical discriminator scans are
archived as exploratory evidence and are not promoted by this correction.

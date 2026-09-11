---
claim_id: admissibility_dirac_kahler_link_curvature_scout_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied nearest-neighbor differential supports, symbolic support-preserving reweightings, exact finite U(1) link fields, and chartwise nilpotency checks"
depends_on:
  - admissibility_dirac_kahler_quotient_gate_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Link Reweighting and Chartwise Curvature on the Finite Fixture

**Type:** `bounded_theorem`

**Campaign block:** 159. **Status:** corrected bounded theorem; formal audit is
deferred. The original note, primary, cache, ledger, manifest occurrence, and
the successor handoff append are preserved in the released-7315-A recovery
packet. The handoff remains historical and supplies no acceptance of later
blocks.

The [primary](../scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py)
uses the exact finite objects in [Block 158](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md),
[Block 156](ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md),
and [Block 155](ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
with the finite cover from [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## The support wall is the parity wall

The displayed 48-hop probe differential uses only displacements

\[
(0,1),\quad(1,0),\quad(-1,0),
\]

with sixteen hops of each kind. Replace every nonzero entry by an independent
coefficient. Every operator in this support class remains grading-odd. Since
the Hodge matrix is grading-even, the induced residue is grading-odd, and its
theta-prime live-live Hermitian block is identically zero.

This support result is an instance of the same parity mechanism, not an
independent obstruction. Changing coefficients on the existing
nearest-neighbor hops cannot escape it. Adding an even displacement changes
the premise class: the supplied far-corner \((1,1)\) extension opens eight
live-live slots, and the two-time-step \((2,0)\) extension opens four. These are
algebraic controls only; admissibility of the enlarged operators is not proved.

## What entrywise modulus proves

For a U(1) link field, Hadamard dressing multiplies every present hop by a
unit-modulus number. It therefore preserves each nonzero entry's modulus and
the Frobenius norm. Within that multiplicative family a nonzero differential
cannot approach the zero operator.

This is only an operator-closure statement. It does not rule out cancellation
after the residue map, formal compression, reflection, or half selection, and
it does not prove that the image cannot approach a chosen mass pairing. The
former positive-witness inference is withdrawn.

## Plaquettes and chartwise nilpotency

The periodic 8-by-4 cover has 64 oriented generating links and 32
plaquettes. Every unoriented link occurs with opposite signs in the product of
all plaquette holonomies, so that product is one. A field with exactly one
nontrivial plaquette is therefore impossible on this closed cover; dressing a
single link produces a two-plaquette curvature dipole.

Nilpotency is chart-local. On the supplied single-link dipoles exactly two of
the four chart differentials have nonzero squares and two remain nilpotent.
Thus nilpotency of one chart does not establish global flatness. A global
flatness conclusion requires the joint chart family to cover and test all
plaquettes. Pure-gauge fields provide the finite control: all 32 holonomies are
trivial and all four dressed chart differentials square to zero.

The residue and compression may remain defined when a chart square is nonzero;
that does not turn curvature into a physical interaction or a positive
pairing. Historical flux and composite censuses remain archived as exploratory
data rather than an exhaustive curvature verdict.

## Disposition

The support-preserving zero, the even-hop escape controls, entrywise modulus
invariance, the plaquette product law, and the joint chart qualification are
retained at finite supplied-matrix scope. Independence from parity,
image-closure exclusion, and single-chart global-flatness language are
withdrawn. No link field, action, reflection, or curvature coupling is adopted.

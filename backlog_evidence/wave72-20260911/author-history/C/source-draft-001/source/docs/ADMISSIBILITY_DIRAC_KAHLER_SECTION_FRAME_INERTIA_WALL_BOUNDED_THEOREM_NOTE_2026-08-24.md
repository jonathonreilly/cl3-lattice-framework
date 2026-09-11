---
claim_id: admissibility_dirac_kahler_section_frame_inertia_wall_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "One exact 8x4 section-frame fixture: eight-cell support census, six explicit seam directions at s=1/5, five masses, a pure-geometry limit, and a spectral-gcd anti-commutant certificate at the E02 fixture. No all-frame, all-seam, all-pairing, or OS no-go is claimed."
depends_on:
  - admissibility_dirac_kahler_temporal_link_extraction_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Section-Frame Inertia Wall

**Campaign block:** 186.

**Claim type:** bounded_theorem

**Status:** corrected finite obstruction; formal audit is deferred. No axiom or premise is adopted.

The [primary runner](../scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py)
uses the corrected [Block 184 finite construction](ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 Hodge source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Finite construction

The time-8, space-4 cover contains eight disjoint even-anchored (2\times2)
cells. The chart differential has 32 nonzero entries, all within those cells.
Let P_x=diag((-1)^x) and P_g=P_link P_x. For a symmetric seam block B,
H_g(B) places B on anchor slices 3 and 7, uses the supplied field on slices
0,1,2 and its reflected offset-permutation image elsewhere, then averages this
raw Hodge with its one-step spatial translate. The seam family is the six
explicit B matrices listed below. If D is the P_g-odd restricted differential
and Q=mH_g+i(H_gD+D^dagger H_g), then on Lambda_+={0,1,2,3} x Z_4 the
dressed pairing is K_ab=conjugate((Q^{-1}P_g)_{b,a}). The
[shared finite fixture helper](../scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py)
contains these exact definitions.
For the curved no-glue completion, the primary counts 144 ordered inter-cell
entries on 72 undirected edges: 48 ordered entries are already in the Hodge
support and 96 are created by the transport term.

The displayed dressed reflection, restricted differential, 32-entry odd glue,
and E02 seam produce a real reflected-transpose-covariant action with 48
cross-half entries. Its dressed 16-dimensional Gram is Hermitian; the
undressed neighbor has 80 defect entries.

At a flat seam, the action has two 16-site support components and the dressed
Gram is the zero matrix, hence positive semidefinite. The symmetric dressed
self-dual seam space has dimension six with four off-diagonal directions. The
ordinary shear-block family meets the self-duality equations at
((q,v)=(0,1)) and ((0,-1)). Flatness is unique only after the conventional
restriction (v>0) is imposed.

## Enumerated inertias

At seam amplitude (s=1/5), the six explicitly named directions
E02, E13, b5-type, b8-type, Bgen1, and Bgen2 have inertias

\[
(6,6,4),(6,6,4),(3,3,10),(0,0,16),(6,6,4),(6,6,4).
\]

The b8 Gram is the zero PSD matrix. The other five are indefinite. Thus the
accurate shared statement is that no tested Gram is positive definite; it is
false that no tested Gram is positive semidefinite. The same E02 construction
has inertia ((6,6,4)) at masses (1/3,9/20,1,2,10), while the pure-geometry
limit has inertia ((4,4,8)).

At the E02 fixture the real symmetric Gram has a four-dimensional kernel and

\[
\gcd(p(\lambda),p(-\lambda))=\lambda^4.
\]

Consequently no nonzero eigenvalue is paired with its negative. In an
eigenbasis, (SK+KS=0) then permits only maps from the kernel to itself. The
anti-commutant is the 16-dimensional endomorphism block of the kernel and
contains no invertible matrix.

The measured traces at the five masses are positive. That rules out an exact
opposite-eigenvalue pairing at those points; balanced positive/negative counts
alone do not imply zero trace and the trace data do not explain the balance.

## N1 — Alternative routes

Other seam directions, amplitudes, pairings, frames, carriers, and quotient
constructions remain open.

## N2 — Wall independence

The support disconnection, finite inertia table, and spectral-gcd result are
separate facts. None promotes the others to an all-frame theorem.

## N3 — Hidden walls

The calculation fixes one field, reflection dressing, completion, seam
amplitude, and 16-dimensional pairing.

## N4 — Residual matching

The inertias are computed by exact congruence. Zero matrices are classified as
PSD rather than folded into the indefinite cases.

## N5 — Rhetoric audit

This is a finite obstruction for one pairing family. It is not an OS no-go and
does not explain the observed balance.

## N6 — Partial closure paths

The kernel-supported anti-commutant result eliminates one invertible
anti-symmetry mechanism while leaving other pairings and frames available.

## N7 — Steelman

A stronger negative theorem would quantify its frame and pairing classes and
show that each allowed alternative reduces to an independently certified wall.

## N8 — Cross-cycle echo

Unavailable historical campaign and checker narratives are archived as
unverified context. The finite matrices are rebuilt from current live sources.

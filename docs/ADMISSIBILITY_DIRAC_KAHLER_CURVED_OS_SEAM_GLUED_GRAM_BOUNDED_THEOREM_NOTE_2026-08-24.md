---
claim_id: admissibility_dirac_kahler_curved_os_seam_glued_gram_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "One exact 32-dimensional seam-glued carrier: real reflected-transpose covariance, Hermiticity, seam controls, and five explicit parameter/history points of which three have positive two-history Grams. No Cartesian crosspoint, parameter window, history-general, section-frame, transfer, or physical theorem is claimed."
depends_on:
  - admissibility_dirac_kahler_temporal_link_extraction_bounded_theorem_note_2026-08-24
runner: scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Five-Point Seam-Glued Gram

**Campaign block:** 185.

**Claim type:** bounded_theorem

**Status:** corrected finite claim; formal audit is deferred. No axiom or premise is adopted.

The [primary runner](../scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py)
uses the corrected [Block 184 finite link data](ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md),
the [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the [Block 105 Hodge source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Construction and structural implication

On the supplied 8-by-4 carrier, let d_K be the grade-raising part and let
theta(t)=-1-t mod 8 with permutation P. The restricted raising matrix A keeps
entries whose two time coordinates lie in {0,1,2,3}, together with entries on
the seam pairs {3,4} and {7,0}; D=A-PAP. The image Hodge uses the displayed
step history on the positive half and the unsigned offset-permutation image on
the reflected half. With Q=mH+HD-D^T H, the finite glue D has 72 nonzero
entries, is P-odd, and the completed real action obeys PQP=Q^T. These
definitions are implemented in the [shared finite fixture helper](../scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py).

Write G=Q^{-1}. On Lambda_+={0,1} x Z_4 the paired matrix is
K_ab=conjugate(G_{b,theta(a)}). Inverting PQP=Q^T gives PGP=G^T, hence
G_{b,theta(a)}=G_{a,theta(b)}. Because G is real,
K_ab=conjugate(K_ba), so K is Hermitian. Reality is load-bearing:
P=[1], Q=[i] satisfies transpose covariance but its paired inverse is not
Hermitian.

## Exactly five points

The fresh primary constructs exactly these five points:

| point | mass | shear/history | leading-minor signs | positive |
|---|---:|---|---|---|
| base | (9/20) | constant in (x), (c=5/13) | (++++++++) | yes |
| mass control | (1/3) | constant in (x), (c=5/13) | (++++++++) | yes |
| mass failure | 2 | constant in x, c=5/13 | (+,+,+,+,+,-,+,-) | no |
| history control | (9/20) | constant in (x), (c=3/5) | (++++++++) | yes |
| history failure | (9/20) | (x)-alternating, (c=3/5) | (++++++--) | no |

In the mass-failure row the compact sign string is (+,+,+,+,+,-,+,-). All five finite Grams remain Hermitian. Three, and only
three, have eight positive leading principal minors. The Cartesian point
((m,c)=(1/3,3/5)) was not constructed by the original primary and remains
open.

The zero-, near-, far-, and both-seam variants have sign vectors
(00000000), (++++-+-+), (++++0000), and (++++++++), respectively.
These enumerate four supplied variants; they do not prove uniqueness of the
glue.

## N1 — Alternative routes

Different seam sets, histories, carriers, and genuine reconstruction maps are
open.

## N2 — Wall independence

The mass and history failures are separate finite counterexamples to broader
generalization. Neither classifies the other axis.

## N3 — Hidden walls

The result uses one carrier, one reflection, one completion convention, and
the displayed positive-time span.

## N4 — Residual matching

Covariance, inverse covariance, Hermiticity, and every sign vector are computed
from the same exact construction.

## N5 — Rhetoric audit

This is a five-point finite table. It is not a six-point Cartesian sample or a
four-positive result.

## N6 — Partial closure paths

The three positive points and two controlled failures motivate bounded axis or
crosspoint studies without supplying a window.

## N7 — Steelman

A window claim would require a declared region and proof or exhaustive finite
coverage appropriate to that region, including the missing crosspoint.

## N8 — Cross-cycle echo

Earlier all-parents-standing and dual-frame readings are historical. The live
claim binds corrected current sources and only the listed finite construction.

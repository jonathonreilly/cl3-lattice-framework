---
claim_id: admissibility_dirac_kahler_temporal_link_extraction_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "One exact 8x4 cover and its 16-dimensional antiperiodic quotient: a displayed two-shift Hodge average, finite temporal-band and bond data, a reflected dual-band identity, a symbolic even/odd bond split, and invertibility of eight original diagonal slice blocks. No frame-family completeness, Schur-elimination, OS-positivity, or physical ADM theorem is claimed."
depends_on:
  - admissibility_dirac_kahler_curved_carrier_dependency_bounded_theorem_note_2026-08-17
runner: scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Temporal-Link Extraction

**Campaign block:** 184.

**Claim type:** bounded_theorem

**Status:** corrected finite claim; formal audit is deferred. No axiom or premise is adopted.

The [primary runner](../scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py)
uses the corrected [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
its corrected [Block 105 Hodge source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). These are source
bindings; the note does not import their broader interpretations.

## Finite result

On the exact time-8, space-4 cover, set

\[
H_2=\tfrac12(H+U_x^T H U_x),\qquad
Q_2=mH_2+i(H_2d_{00}+d_{00}^\dagger H_2).
\]

The runner rebuilds this displayed two-shift average. It is positive definite
and maps under the displayed reflection to the corresponding dual average.
The time-band census of (Q_2) is

\[
\{0:80,1:72,2:16,6:16,7:72\}.
\]

Over the symbolic rational-function field, its eight forward bond blocks have
generic rank 4, nonzero counts alternating (10,8), and generically empty
kernels. This does not assert rank 4 at every parameter specialization; in
particular, the all-real-mass statement below concerns only the original
diagonal slice determinants. The forward band maps exactly to the dual
backward band when the dual action uses (d_{\rm ref}=R d_{00}R^T). The same
comparison with (d_{00}) has 16 nonzero residual entries.

For a per-slice symbolic field, an odd bond has eight entries and vanishes at
zero shear. An even bond splits into an eight-entry odd part and a four-entry
diagonal even part. Mass occurs only in the odd part. The common magnitude of
the even entries depends on (q_0^2,q_1^2); it is not shear independent.

Each of the eight **original diagonal slice blocks** has an even quartic
determinant in (m) with positive nonzero coefficients. Hence each displayed
slice block is invertible for every real (m). This does not certify any
iterated Schur pivot or locate the full action's kernel. In particular,
invertible diagonal blocks alone do not imply an invertible Schur complement.

The antiperiodic quotient has dimension 16, census
({0:40,1:36,2:16,3:36}), and four rank-4 bonds with the same (10,8)
alternation. Its seam bond is the negative of the corresponding cover bond.

## Frame scope

(H_2) is one explicit finite average. The separate comparison average uses
exactly the original four origins ((0,0),(0,1),(1,0),(1,1)); it has the same
measured band census and differs from (H_2) at 96 entries. Neither average is
a complete or unrestricted minimal frame family. Period-four time translations identify nominally
different orbit entries. For example, aggregate weights
(w_0=1/2,w_1=w_3=1/4) close modulo four while violating the unaggregated
condition (w_1=w_7). Thus neither sixteen distinct branches nor an
unqualified necessity condition follows from the displayed construction.

## N1 — Alternative routes

Other orbit averages, common descents, genuine block eliminations, and direct
Gram constructions remain open.

## N2 — Wall independence

The frame-family warning and the Schur warning are independent: the first is
combinatorial, while the second concerns block elimination.

## N3 — Hidden walls

The claim is conditional on this finite carrier, field, reflection,
differential, completion convention, and quotient.

## N4 — Residual matching

All retained equalities are exact matrix identities. The 16-entry wrong-dual
control separates the reflected-differential convention from its neighbor.

## N5 — Rhetoric audit

The result supplies finite link data and single-block inversion. It does not
supply a global transfer, OS positivity, an ADM derivation, or a frame theorem.

## N6 — Partial closure paths

The full-rank bond blocks and quotient seam sign remain useful inputs for a
future explicitly specified elimination or pairing.

## N7 — Steelman

A valid global claim would exhibit every Schur pivot or an equivalent full
factorization and state the quotient by coincident frame-orbit points.

## N8 — Cross-cycle echo

Historical statements that the earlier parents “stand” are archival. Current
corrected Block 105 and 128 bytes are the live inputs.

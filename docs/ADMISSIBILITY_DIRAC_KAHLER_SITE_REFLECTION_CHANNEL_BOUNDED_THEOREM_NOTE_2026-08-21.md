---
claim_id: admissibility_dirac_kahler_site_reflection_channel_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "the 64 supplied 8-by-4 reflection labels, their quotient signs and grading relation, and one exact pinned carrier"
depends_on:
  - admissibility_dirac_kahler_mass_survival_stratum_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Site-Reflection Signs and a Named Carrier

**Type:** `bounded_theorem`

**Campaign block:** 163. **Status:** corrected bounded theorem; formal audit is
deferred. All five original path bodies, including the historical manifest,
are preserved in the released-7315-B recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py)
uses corrected [Block 162](ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 159 supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Exact reflection bookkeeping

The 8-by-4 antiperiodic quotient has 32 even-time site labels and 32 odd-time
link labels in the displayed family. Twenty-four of the site labels descend to
involutions, four with trivial spatial action. The source reconstructs every
signed permutation from the antiperiodic lift and compares it with the supplied
quotient descent for all 64 labels.

Let \(\Gamma\) be the displayed staggered parity. For every one of these
labels, the descended reflection commutes with \(\Gamma\) when
\(p_t+p_x\) is even and anticommutes when that sum is odd. This is an exact
finite selection rule; it is not a liveness result and does not say that every
allowed block has nonzero rank.

## A finite carrier comparison

For the x-trivial label with fixed slice \(c=1\), edge \((2,2)\), and the
explicit graded region carrier with free-cell shear \(\sigma=1/3\),
\(m=1\), and \(s_x=3/5\), the adjacent-slice form has inertia \((4,4,0)\)
at \(s_t=0\) and \((5,0,3)\) at \(s_t=1/5\), in
positive-zero-negative order. The ranks are four and eight. These two exact
points show that temporal coupling can change the form on this carrier.

They do not prove that every nonzero temporal coupling fails on every carrier.
In particular, no conclusion is drawn about carriers outside the displayed
pinned locus. The historical terminal complementarity and global
non-continuation wording is withdrawn.

## Disposition

The antiperiodic sign law, site/link split, grading relation, and named carrier
comparison are retained. Global carrier classification, physical
interpretation, and any inference from allowed support to nonzero liveness are
withdrawn.

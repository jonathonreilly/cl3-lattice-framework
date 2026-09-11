---
claim_id: admissibility_dirac_kahler_mass_survival_stratum_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the eight cross-parity coefficients of the supplied even-column form, two exact linear loci, and the displayed four-weight edge family"
depends_on:
  - admissibility_dirac_kahler_validation_battery_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Mass Survival on Two Specified Linear Loci

**Type:** `bounded_theorem`

**Campaign block:** 162. **Status:** corrected bounded theorem; formal audit is
deferred. The original note, primary, cache, ledger, and manifest are preserved
in the released-7315-B recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py)
uses the corrected [Block 161 finite pullback](ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 159 supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## The coefficient calculation

For the supplied edge \((2,2)\), set \(s_x=3/5\) and \(s_t=4/5\),
restrict to the even-column temporal hops, and leave the sixteen cell Hodge
moduli symbolic. The only cross-parity entries are

\[
 \frac{b_{20}}{10},\ \frac{b_{00}}{10},\
 \frac{b_{22}}{10},\ \frac{b_{02}}{10}
\]

at order \(m^0\), and

\[
 \frac{b_{30}+b_{33}}8,\ \frac{b_{31}+b_{32}}8,\
 -\frac{b_{10}+b_{13}}8,\ -\frac{b_{11}+b_{12}}8
\]

as the coefficients of \(m\). Every odd-slot diagonal is zero. Within this
displayed symbolic form, zero mass requires the first four coordinates to
vanish for positive semidefiniteness, while mass independence requires the
four odd-row sums to vanish. The two sets use disjoint coordinates.

The eight independent equations define a 24-dimensional locus in the stated
32-coordinate \((\nu,\sigma)\) chart. Adding the two historical L154 equations
has total rank ten and selects a 22-dimensional slice. The extra equations do
not change this form after the first eight have removed all cross terms. These
are dimensions of the stated formal coordinate loci, not dimensions of a
physical state space.

## Shared pullback and corrected weight law

On the 22-dimensional slice, all sixteen displayed edge forms factor through
the same positive diagonal four-slot form, multiplied by an edge-dependent
scalar. For arbitrary real weights \(\lambda_i\), define \(c\) by dividing the
first diagonal entry by the displayed modulus reference
\(a_{20}+a_{33}+\mu_{23}+\nu_{30}\) and multiplying by five. The exact source
identity is

\[
 4c=5\bigl(\operatorname{base}_i-s_t(\lambda_j-\lambda_i)\bigr),
 \qquad \operatorname{base}=(0,0,s_t,-s_t).
\]

The missing factor five in the historical note is corrected here. This is a
coefficient identity for the supplied edge family, not a general connection
classification.

The two displayed spatial permutations are commuting fixed-point-free
involutions. They generate the regular Klein action on four sites, and their
joint \((-1,-1)\) character is one-dimensional. This exact finite algebra is
retained without interpreting it as a physical record sector.

## Disposition

The eight coefficient identities, 24- and 22-dimensional formal loci, shared
pullback, corrected weight law, and finite Klein calculation are retained.
Claims that the quotient removes every physical sector or every connection
degree of freedom are withdrawn. Behavior away from the two stated loci stays
open.

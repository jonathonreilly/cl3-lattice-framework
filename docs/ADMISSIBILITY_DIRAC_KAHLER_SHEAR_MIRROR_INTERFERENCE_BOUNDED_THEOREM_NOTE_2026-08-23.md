---
claim_id: admissibility_dirac_kahler_shear_mirror_interference_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "Exact mirror and transport measurements for several explicitly supplied finite profiles at two cover extents. The results distinguish the antiunitary transpose condition from a commutator comparison and retain only finite-family counterexamples. Historical interference brackets are archived, not fresh evidence. No all-carrier classification, OS no-go, unique readout, premise, axiom, audit verdict, or continuum claim follows."
depends_on:
  - admissibility_dirac_kahler_conditional_symmetric_power_theorem_note_2026-08-23
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py
---

# Shear, mirror, and interference — corrected finite note

**Historical block:** 178

**Repair date:** 2026-09-11

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py`](../scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py`](../scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py)

The finite construction is inherited from the
[corrected conditional-sector note](ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md)
and the accepted
[Block 105 source](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
No broader parent theorem is imported. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are unchanged.

## Correct antiunitary condition

For `Theta phi=r conjugate(phi)`, invariance of the quadratic form requires

\[
 rQr=Q^T.
\]

The comparison `rQr=Q` is a commutator test and agrees only on suitable real
symmetric controls. The primary runner computes both defects.

On the two disclosed extents, the flat zero-shear Hodge control satisfies both
tests. The non-flat, zero-shear, reflection-symmetric volume profile
`nu(t,x)=(1,2,3,4)_x` yields the repeating diagonal

\[
 \left({25\over16},{3\over2},{17\over8},{17\over6}\right)
\]

and also satisfies both tests. Thus these examples refute the finite slogan
that mirror symmetry implies flat or geometry-free data. They do not classify
all volume profiles.

For the separately supplied shear profiles, both finite extents have nonzero
defects. The runner retains the exact support counts, the single-level
`b`-modulus control, and the physical single-level profile whose forced
`a`-modulus adds diagonal entries. These are profile-specific finite results,
not a theorem about every carrier.

## Transport family

The quotient connection is affine in the supplied dials, so its reflection
defect satisfies the corresponding matrix identity. The runner records the
finite hop censuses at `8x4` and `12x4`; their different counts prevent an
extent-independent support law.

Nonzero defects obstruct the canonical reflected Gram built from these fixed
data when that candidate is non-Hermitian. They do not prove an
Osterwalder-Schrader no-go or force a particular Hermitianization, doubling,
quotient, or physical readout.

Functions of `Q` alone are insensitive to a later choice between two
post-`Q` kernel labels. This observation gives many finite candidate families,
not a selector. Positive powers of a nonzero determinant modulus are examples;
generic nonconstant positive functions of `Q^dagger Q` can be sensitive.
Constant functions are counterexamples to any claim that every such function
is sensitive. On this construction `1/det(Herm(Q))` is also dial-blind because
`Herm(Q)` does not contain the transport dial.

## Historical interference evidence

The original baseline execution evaluated the dial-off point and `(0,1/4)`.
Its deep route evaluated only

\[
 \lambda(1/3,1/4),\qquad
 \lambda\in\{1/2,1/4,1/8\}.
\]

It did **not** execute the advertised point `(1/3,1/4)`. The exact brackets and
the very large reduced-rational comparison are preserved as historical cache
evidence. This corrected runner does not reclassify them as fresh independent
evidence and does not execute the missing point.

For any fully constructed rational family with nonvanishing denominators at
the origin, continuity and `J(0)=0` imply `J(lambda)->0`; three samples alone do
not prove that limit or global monotonicity. Interpreting a finite response as
physical record-record interference remains a proposal.

## Scope and disposition

The finite mirror controls, tested shear failures, transport support censuses,
and generic continuity observation are retained. Universal carrier language,
unique-readout language, and the false two-point execution statement are
withdrawn. Historical interference values remain recoverable and explicitly
historical.

## N1 — alternative routes

Different reflections, doubled fields, quotients, positive completions,
derived event domains, and other volume/shear families remain open.

## N2 — separate obligations

Mirror invariance, positivity, source composition, and physical record
interpretation are separate requirements in this scope.

## N3 — hidden assumptions

The profiles, extents, reflection, pins, dials, and candidate functions are
supplied finite choices.

## N4 — residual matching

The counterexamples refute only claims containing the tested families. They do
not prove a classification of every carrier or reconstruction.

## N5 — rhetoric and resolution

The note says “tested profiles” and “finite families.” Historical brackets and
unexecuted points are distinguished explicitly.

## N6 — partial closure

A useful continuation would bind a complete source-composition map and execute
all named dial points under one reviewed runtime.

## N7 — hostile-reviewer steelman

A critic may posit a different antiunitary reflection or a noncanonical
positive completion. The present finite defects do not exclude it.

## N8 — cross-cycle echo

Earlier finite action work also found profile-dependent support cancellations.
That resemblance does not imply an all-lattice law.

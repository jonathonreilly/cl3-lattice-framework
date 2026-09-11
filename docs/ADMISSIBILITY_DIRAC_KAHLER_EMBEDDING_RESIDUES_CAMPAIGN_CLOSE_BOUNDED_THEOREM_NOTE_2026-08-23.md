---
claim_id: admissibility_dirac_kahler_embedding_residues_campaign_close_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "Exact one-orbit translation, character, restriction, and metric-preservation calculations on one supplied 12x6 finite fixture. Equal scalar restrictions show indifference of this observable only; multiplicity and the fiber-response interpretation remain open. No physical carrier equivalence, orientation selector, campaign closure theorem, premise, axiom, audit verdict, or continuum result follows."
depends_on:
  - admissibility_dirac_kahler_shear_mirror_interference_bounded_theorem_note_2026-08-23
  - admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23.py
---

# Embedding residues — corrected finite note

**Historical block:** 179

**Repair date:** 2026-09-11

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23.py`](../scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py`](../scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py)

This calculation uses the finite construction documented by the
[corrected shear/mirror note](ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md)
and the
[corrected complex-structure note](ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are unchanged.

## One finite orbit

On the supplied `12x6` constant-volume fixture, spatial translation by two
restricts on one three-site orbit to

\[
 U_{\rm orb}=P_3=
 \begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]

The orbit action restricts to

\[
 R={3193\over2240}I_3.
\]

The two nontrivial translation characters are conjugates and have different
translation eigenvalues `omega` and `omega^2`, yet both Rayleigh quotients are
`3193/2240`. This shows that this **one scalar restriction** is indifferent to
the conjugate orientations. It does not remove every possible physical
orientation selector or make the character vectors physically identical.

## Commutation is not metric preservation

Because `R=cI_3`, every `3x3` matrix commutes with `R`. Metric preservation is
the different condition

\[
 T^\dagger RT=R.
\]

For positive `c`, this is equivalent to `T^dagger T=I`: `T` must be unitary.
The invertible basis change `T=2I_3` commutes with `R` but does not preserve it.
The historical matrix `e_0e_1^T` is a useful noncommuting-family witness, but it
is singular and therefore is not an arbitrary basis change.

The finite orbit establishes an equivariant module map for this three-cycle.
It does not establish preservation of a nontrivial metric ratio, a full
`M_2(C)` algebra embedding, or physical observables.

## Multiplicity and supplied count

All twelve displayed character copies can be formed on this fixture, and the
per-copy sesquilinear restriction has three level-dependent coefficients. The
full isotype Gram is not diagonal. The supplied historical count convention is
additive:

\[
 n=1\Rightarrow(r,q)=(1/2,2/3),\qquad
 n=12\Rightarrow(r,q)=(6,13/3).
\]

This arithmetic does not derive which copies are physical. It shows why a
one-copy selection was load-bearing and why multiplicity remains open.

## Open obligations and pending fiber response

The useful finite calculation leaves six named supplies:

1. a multiplicity selector, quotient, or proved fiber theorem;
2. an injective unital star-algebra carrier map;
3. non-vacuous physical observable preservation;
4. a record-write identification;
5. treatment of the ambient higher-weight sectors;
6. a nondegenerate metric-ratio comparison.

The archived Block 179 note proposed that a transport-dependent eigen-fiber
response might address the first item. Its cross-check was pending. That
proposal remains explicitly **pending** in this recovery. It is neither
accepted as a theorem nor removed from the research record, and it also depends
on the supplied counting interpretation corrected in Block 176.

The historical “campaign close” was a planning statement with no new
measurement. This note records the finite residue status only.

## Scope and disposition

The exact three-cycle, scalar restriction, conjugate-character equality,
level ledger, and additive comparison are retained. Claims that all basis
changes preserve the metric, that all physical orientation observables are
eliminated, or that the campaign has only two or three remaining obligations
are withdrawn.

## N1 — alternative routes

A derived fiber theorem, a nondegenerate orbit metric, a physical observable
map, or a different character-sensitive observable could change the residue
status.

## N2 — separate obligations

Multiplicity, algebra embedding, observable preservation, ambient matching,
record writing, and metric-ratio selection are tracked separately. Their
logical independence is not proved.

## N3 — hidden assumptions

The orbit, action, translation, character basis, and slot-count formula are
supplied finite choices.

## N4 — residual matching

Equal Rayleigh quotients answer only the scalar-restriction question. The
unitary condition answers only metric preservation for `R=cI`.

## N5 — rhetoric and resolution

The orientation result is called scalar-observable indifference. Multiplicity
and the fiber-response interpretation remain pending.

## N6 — partial closure

The finite orbit is a reusable representation-level construction. A physical
bridge still requires explicit observables and a proved treatment of copies.

## N7 — hostile-reviewer steelman

A critic can choose an observable that distinguishes `omega` from `omega^2` or
reject the supplied count. The displayed algebra does not preclude either.

## N8 — cross-cycle echo

Degenerate scalar metrics elsewhere also enlarge commutants without making
every coordinate transformation an isometry. This is contextual consistency,
not a theorem import.

---
claim_id: admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "Exact finite complex-structure, realification, and one-orbit restriction identities on supplied Dirac-Kahler fixtures. The role reading and slot-count map are explicitly supplied interpretations. No physical probability law, carrier selection, premise, axiom, audit verdict, obligation retirement, or all-lattice result is derived."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py
---

# Complex-structure synthesis — corrected finite note

**Historical block:** 176

**Repair date:** 2026-09-11

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py`](../scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py`](../scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py)

The helper obtains its cover, Hodge, connection, and reflection matrices from
the accepted finite construction rooted in the
[current Block 105 note](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
This is a source dependency, not adoption of a parent theorem. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) remain unchanged.

## Correct determinant realification

For a complex `N x N` matrix `Q`, define

\[
 \mathcal R(Q)=
 \begin{pmatrix}\operatorname{Re}Q&-\operatorname{Im}Q\\
 \operatorname{Im}Q&\operatorname{Re}Q\end{pmatrix}.
\]

Then

\[
 \det_{\mathbb R}\mathcal R(Q)=|\det_{\mathbb C}Q|^2.
\]

When the ordinary unnormalized complex Gaussian exists with convention
`Z(Q)=pi^N/det(Q)`, its paired coefficient is

\[
 Z(Q)Z(Q^\dagger)
 ={\pi^{2N}\over|\det Q|^2}
 ={\pi^{2N}\over\det\mathcal R(Q)}.
\]

Thus the Gaussian pair is proportional to the **reciprocal** realified
determinant. It is not the realified determinant. The common `pi^(2N)` factor
cancels when a finite menu is normalized. The primary runner checks the
positive-power determinant identity on a disclosed finite action and checks
the reciprocal relation separately.

This is a candidate scalar functional. It is not an Osterwalder-Schrader
reconstruction, a unique readout, or a physical probability law.

## Exact complex cell and supplied counting convention

On the disclosed `12x6` constant-volume fixture, translation by two spatial
sites has order three. Its two nontrivial characters are conjugates, and the
committed finite action restricts at one chosen orbit to

\[
 f_1^\dagger Qf_1=f_2^\dagger Qf_2={3193\over2240},
 \qquad f_k^TQf_k=0.
\]

For `phi=z f_k`, the restricted form is therefore
`(3193/2240)|z|^2`. This is an exact sesquilinear one-complex-coordinate
calculation on one supplied orbit.

The historical flavor comparison used the supplied maps

\[
 r(n)={n\over2},\qquad q(r)={1+2r\over3}.
\]

They give `(r,q)=(1/2,2/3)` for one selected complex slot and `(1,1)` for two
real slots. The runner implements these formulas locally and labels them as
supplied comparison conventions. Sesquilinearity, absence of a `z^2` term, and
the complex structure do not derive a unique physical slot count.

## Role reading and historical interference

The archived package proposed reading its formation-conditional vector and its
marginal vector as different objects. Their finite entries and difference are
useful bookkeeping. The role assignment remains an interpretation: the
non-governing reading notes do not establish event/sample-space
identifications, and they do not prove that another route is impossible.

The archived Block 176 interference baseline remains preserved with its exact
cache. This corrected runner does not present that historical cache as fresh
evidence and does not execute a holonomy arm.

## Runtime closure and disposition

The live runner imports only the dedicated helper. The helper imports the
reviewed current finite helper chain ending at Block 105. It never resolves or
executes a file from `origin/main`, and it does not import the historical
49-script closure or any #7359-B/C claim.

All original note, runner, ledger, cache, and manifest bodies are preserved in
the dedicated recovery packet. Historical promotion language and parent
theorems are archive-only.

## N1 — alternative routes

Alternative physical readings, event domains, source normalizations, and
carrier maps remain open. The finite realification identity excludes none of
them.

## N2 — separate obligations

Choosing a scalar functional, identifying physical events, selecting a
polarization, and deriving a probability law are separate supplies here. No
logical-independence theorem is claimed.

## N3 — hidden assumptions

The finite fixture, orbit, complex coordinate, Gaussian convention, and slot
map are supplied. Their algebraic consistency does not make them physical.

## N4 — residual matching

The determinant calculation corrects the realification normalization. The
one-orbit calculation establishes a finite sesquilinear restriction. Neither
addresses an all-carrier or continuum selector.

## N5 — rhetoric and resolution

The finite identities are retained. Claims that the axioms arbitrate the role
split, that complex structure forces the count, or that the paired Gaussian is
the realified determinant are withdrawn.

## N6 — partial closure

A continuation could derive an event/source algebra and then test whether the
paired Gaussian follows from its composition law. That route remains open.

## N7 — hostile-reviewer steelman

A critic may accept every displayed identity and still reject the proposed
role or slot interpretation. The corrected claim allows that response.

## N8 — cross-cycle echo

Earlier finite menu work likewise separates exact normalization identities
from physical event selection. That similarity supplies context only.

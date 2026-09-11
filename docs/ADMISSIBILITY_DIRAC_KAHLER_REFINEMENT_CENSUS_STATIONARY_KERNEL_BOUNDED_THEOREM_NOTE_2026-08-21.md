---
claim_id: admissibility_dirac_kahler_refinement_census_stationary_kernel_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "four-letter length-two combinatorics, one supplied joint-pin defect at each of two finite extents, and an exact two-state density calculation"
depends_on:
  - admissibility_dirac_kahler_generator_trilemma_kernel_bounded_theorem_note_2026-08-21
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_refinement_census_stationary_kernel_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Refinement and Density Identities

**Type:** `bounded_theorem`

**Campaign block:** 172. **Status:** corrected bounded theorem candidate; formal
audit is deferred. The original four science bodies and historical manifest
occurrence remain recoverable in the released-7315-D packet.

The [primary](../scripts/admissibility_dirac_kahler_refinement_census_stationary_kernel_2026_08_21.py)
uses the corrected finite table defined in
[Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md),
the finite local matrices from
[Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). No conclusion from the
historical Blocks167--170 is adopted as a premise.

## Four-letter length-two census

There are \(4^2=16\) ordered length-two words. Forgetting order leaves

\[
\binom{4+2-1}{2}=10
\]

multisets: four doubled letters and six pairs of different letters. Each of the
six different-letter multisets has two ordered representatives. On each of the
two supplied fixtures, the sixteen reconstructed W9 profiles are distinct, so
the two representatives of every such multiset carry different profiles. This
is a finite loss of information under the frequency map. It is not a statement
about arbitrary histories, ergodicity, or an infinite process.

For projectors \(\Pi_a\) and any matrix \(G\),

\[
\operatorname{tr}\!\left(G\sum_{a\in S}\Pi_a\right)
=\sum_{a\in S}\operatorname{tr}(G\Pi_a).
\]

This is trace linearity. Its exact zero defect has no independent
noncontextuality or refinement content.

## One joint-pin inequality and its bracket

At each supplied extent the primary chooses the first two site records at the
first free level and computes, with the denominator summed over all singleton
records in that fixture's finite free-cell alphabet,

\[
\delta=\frac{w(\{c_0,c_1\})-w(\{c_0\})-w(\{c_1\})}
{\sum_c w(\{c\})}.
\]

The measured numerator is negative because the computed fixture obeys
\(w(\{c_0,c_1\})<w(\{c_0\})+w(\{c_1\})\). Normalization alone does not force
that sign; positive weights \(3,1,1\) give the opposite inequality.

For \(N=\lfloor1/|\delta|\rfloor\), the exact conclusion is

\[
\frac1{N+1}<|\delta|\leq\frac1N.
\]

The integer \(N\) is a bracket label. It does not establish
\(|\delta|=1/N\), an alphabet-reciprocal law, or invariance under changes of
the base record.

## Density and phase convention

A Hermitian matrix with positive diagonal need not be positive semidefinite;
\(\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}\) has determinant \(-3\).
The density construction therefore requires \(\rho\succeq0\) and
\(\operatorname{tr}\rho>0\).

For \(v_i=3/5\), \(v_j=4\phi/5\), \(|\phi|=1\), and Hermitian \(\rho\), the
off-diagonal part of \(\operatorname{tr}(\rho vv^\dagger)\) is

\[
\frac{12}{25}\left(\phi\rho_{ij}+\bar\phi\rho_{ji}\right).
\]

The phase factors in the historical display were reversed. At
\(\phi=i\), \(\rho_{ij}=i/4\), the correct off-diagonal contribution is
\(-6/25\). The primary checks this with the positive definite trace-one matrix
\(\rho=\begin{psmallmatrix}1/2&i/4\\-i/4&1/2\end{psmallmatrix}\), as well as
the real-phase fixture that had hidden the sign error.

## Scope

No deep merge census, all-shear symbolic theorem, global refinement verdict,
physical density interpretation, or axiom conclusion is retained. The absent
historical profile-table executable is replaced by the bounded helper shared
with Block171. The runner binds that helper and its actual transitive inputs and
checks required-key completeness.

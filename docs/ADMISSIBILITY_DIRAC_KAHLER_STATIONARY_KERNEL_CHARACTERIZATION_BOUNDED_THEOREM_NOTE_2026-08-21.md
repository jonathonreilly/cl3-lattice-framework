---
claim_id: admissibility_dirac_kahler_stationary_kernel_characterization_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "normalized solutions of a four-state column-stochastic finite system, two exact sign-changing parameter pairs, and five displayed iterates"
depends_on:
  - admissibility_dirac_kahler_refinement_census_stationary_kernel_bounded_theorem_note_2026-08-21
  - admissibility_dirac_kahler_generator_trilemma_kernel_bounded_theorem_note_2026-08-21
runner: scripts/admissibility_dirac_kahler_stationary_kernel_characterization_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Normalized Solutions of the Finite Extension System

**Type:** `bounded_theorem`

**Campaign block:** 173. **Status:** corrected bounded theorem candidate; formal
audit is deferred. The original note, primary, cache, ledger, and historical
manifest occurrence remain recoverable in the released-7315-D packet.

The [primary](../scripts/admissibility_dirac_kahler_stationary_kernel_characterization_2026_08_21.py)
uses the exact finite construction in
[Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md)
and the scope corrections in
[Block 172](ADMISSIBILITY_DIRAC_KAHLER_REFINEMENT_CENSUS_STATIONARY_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply no stochastic or
physical interpretation for these matrices.

## Existence and uniqueness

Let \(M\) be column stochastic and let \(P_0\) be a probability vector. A
normalized real solution \(\mu\), which need not be nonnegative, is required
to satisfy

\[
M\mu=P_0,\qquad \mathbf1^\mathsf T\mu=1.
\]

The first equation already implies normalization because
\(\mathbf1^\mathsf TM=\mathbf1^\mathsf T\). Define

\[
E=M-P_0\mathbf1^\mathsf T.
\]

On the normalized affine hyperplane, \(E\mu=0\) is equivalent to
\(M\mu=P_0\). A solution exists exactly when \(\ker E\) contains a vector with
nonzero coordinate sum; equivalently, \(P_0\) lies in the affine hull of the
columns of \(M\). It is unique exactly when that normalizable kernel is
one-dimensional.

Invertibility of \(M\) is sufficient: \(\mu=M^{-1}P_0\), and stochasticity
forces its sum to one. It is not necessary. For
\(M=P_0\mathbf1^\mathsf T\), \(E=0\), \(M\) is singular, and every probability
vector solves the system. A missing cofactor representative at a rank below
three therefore cannot establish infeasibility.

## Supplied finite systems

At the committed rational carrier, the primary constructs the empty-base
system at the first fillable slot for 12x4 and 8x4. It checks column
stochasticity, the exact affine equation, rank three of \(E\), and one strictly
positive normalized solution. Rank three is a result at these two matrices,
not a generic theorem.

At \(\sigma=0\), writing a zero record changes no profile. Consequently all
four columns of \(M\) equal \(P_0\), \(E=0\), and the normalized solutions are
nonunique. The system remains feasible; only a unique selector is lost.

For the 12x4 fixture, the primary also checks a strictly positive solution at
\(s_t=0\) and a solution with a negative component at \(s_t=1/4\). Likewise it
checks a positive solution at \(m=1\) and a negative component at \(m=1/3\).
These are exact opposite-sign endpoint pairs. They do not identify a nearest
zero, prove a box in all dials, or determine connectivity of a positivity
region.

## Iteration and defect identity

For the committed 12x4 matrix the primary reports exactly five applications of
\(M\) to the displayed normalized vector of four one-record weights. This
vector is not identified with a marginal of Block 171's two-record joint. Five
steps do not prove convergence. The normalized solution \(\mu_*\) satisfies
\(M\mu_*=P_0\ne\mu_*\), so it is not a fixed point; if repeated application of
this fixed matrix converged to \(\mu_*\), continuity would give a contradiction.

For any normalized \(\mu\) and normalized solution \(\mu_*\),

\[
M\mu-P_0=E(\mu-\mu_*).
\]

This is a vector identity. It does not equate the maximum norms of its factors,
and the finite values do not establish a geometric scalar law.

## Scope

The finite Gibbs joint in Block 171 has an exact marginal-conditional
factorization. An infinite extension remains conditional on providing kernels
for every history and time. The historical 23/15 trail counts, backward scan,
global boundary search, five-step convergence claim, parity law, symbolic-mass
headline, denominator-degree claim, and theorem-door or axiom rhetoric are not
retained. The runner checks required-key completeness and binds its full actual
runtime input closure.

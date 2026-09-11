---
claim_id: admissibility_dirac_kahler_generator_trilemma_kernel_bounded_theorem_note_2026-08-21
claim_type: bounded_theorem
claim_scope: "the supplied 12x4 and 8x4 exact record-profile fixtures, one four-letter length-two table, and conditional finite matrix identities"
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A Finite Record-Profile Construction

**Type:** `bounded_theorem`

**Campaign block:** 171. **Status:** corrected bounded theorem candidate; formal
audit is deferred. The original note, primary, cache, ledger, and historical
manifest occurrence remain recoverable in the released-7315-D packet.

The [primary](../scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py)
uses the finite local matrices from
[Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). These inputs define a
finite test fixture. They do not identify a physical action, a stochastic law
of nature, or a continuum limit.

## Conditional matrix identity

For an invertible complex matrix \(Q\), write
\(H(Q)=(Q+Q^\dagger)/2\). Direct multiplication gives

\[
H(Q^{-1})=Q^{-1}H(Q)Q^{-\dagger}.
\]

Thus positive definiteness of \(H(Q)\) implies positive definiteness of
\(H(Q^{-1})\). It also implies that \(Q\) is invertible: if \(Qv=0\) for
nonzero \(v\), then \(v^\dagger H(Q)v=0\), a contradiction. This is a
conditional linear-algebra statement. The primary separately checks its
hypotheses on the supplied rational matrices.

If \(Q=Q_1\oplus Q_2\), every expression obtained from \(Q,Q^\dagger\) by a
finite sequence of sums, products, and defined inverses remains block
diagonal. Its first compressed block depends only on \(Q_1\). This elementary
closure statement is the only direct-sum result retained here.

## Reconstructed finite profile table

The executable table is now constructed inside the bounded helper; there is no
reference to the missing historical `b171_profile_table_v2.py`. Its declared
fixture is:

- cover extents 12x4 and 8x4, with physical time extents 6 and 4;
- fixed slice \(c=1\), hence pinned time levels 0 and 1;
- \(m=1\), \(s_x=3/5\), \(s_t=0\), and free shear \(\sigma=3/5\);
- the displayed x-inhomogeneous rational volume rule;
- two records, at the first two free levels, each replacing one supplied shear
  by zero; and
- four site labels at the read level.

For each of the sixteen ordered pairs, the unnormalized weight is the trace of
the read-level block of \(H(Q^{-1})\); division by its trace gives the displayed
four-component profile. The primary rebuilds all sixteen rows at each extent,
checks strict positivity and exact normalization, and checks that the sixteen
profiles are distinct at each extent. These are 32 finite rows, not a complete
history census.

The same positive sixteen weights define a finite Gibbs joint

\[
J(a,b)=\frac{w_{ab}}{\sum_{c,d}w_{cd}}.
\]

Its marginal and conditional satisfy \(J(a,b)=J_A(a)J(b\mid a)\) exactly.
This factorization holds for every positive finite joint by definition. It does
not depend on the historical ratio \(\sum w_{\rm extended}/w_{\rm empty}\),
and failure of that ratio to equal one is not an obstruction to finite
factorization.

## Scope

The table supplies finite normalized kernels for the declared records. A
half-infinite process would require normalized kernels for every history and
time, together with their measurability; those data are absent here. Different
slot-order recipes are different finite constructions and do not prove a
Kolmogorov inconsistency for one fixed joint.

The historical ten-member battery, winning-set language, deep-memory labels,
universal generator classification, farthest-record conclusions, 12x4 deep
census, and inherited Blocks167--170 closure claims are preserved only as
history. The 1/5 stress probe is not promoted into the declared record
alphabet. No theorem route is declared exhausted and no axiom is proposed.

The runner checks exact input hashes and exact equality of the required claim
key set. Deleting a key therefore fails the control; checking only the values
of surviving keys would not be a valid missing-key test.

# Erratum: scalar-degree uniformization is source-block restricted

An independent native cold review found a genuine domain error in the earlier
Poisson arguments. The general operator identity
 G=-i[H,.]+Lambda(Gamma-I),
with a null column sqrt(I-R/Lambda), is false on coherences between source
sectors with different scalar rates. Earlier formulations that allowed arbitrary
coherent inputs across the whole direct sum were too broad.

Counterexample: take R=Lambda|1><1| and a jump sqrt(Lambda)|1><1|, with zero
Hamiltonian. The original dissipator acts on|0><1| as-Lambda/2 times that
coherence. Uniformization adds the null column|0><0|, so Gamma kills the
coherence and Lambda(Gamma-I) instead gives-Lambda times it. The null channel
adds dephasing which the original generator does not contain.

For rho block diagonal in source sectors with R|_s=r_s I_s, the null recycling
term is(Lambda-r_s)rho_s/Lambda. It then cancels exactly as required, and
Lambda(Gamma-I)rho equals the original GKSL dissipator. This class is invariant
under the stipulated free dynamics and complete jumps. Therefore the corrected
fixed-time scope is a definite legal initial head/fuel/Record sector, arbitrary
matter/battery/reference coherence WITHIN it, or a classical mixture of such
sectors. A fixed-battery diamond norm is over the corresponding admissible
matter input map, not the full coherent direct-sum system input.

Affected memos now carry a prominent domain correction and targeted wording:
ENERGY_TRANSFER_BOUND.md, REPEATED_CAP_BOUND.md,
FINITE_LADDER_APPROXIMATION.md, GLOBAL_FREE_COMPOSITION.md.
Their original bytes and old hashes are preserved under
historical-before-uniformization-erratum/ and UNIFORMIZATION_HASH_RECEIPT.json.
This is not deletion or relabeling of the mistaken historical claim.

The one-event bounded energy-transfer/Sylvester lemma is unchanged. The quantum
sequential-projection union lemma is unchanged and remains valid for arbitrary
vectors/projectors. The error concerns using the particular null-column Poisson
representation for the original GKSL evolution outside its invariant diagonal
class. Fixed-time applications of those lemmas now state the corrected domain.

SAFE_CAP_FINITE_LADDER.md was written after this issue was known. It uses a
direct Duhamel estimate along the exact safe flow and no Poisson representation;
it explicitly adopts the same declared initial-sector class. Its rational
certificate is independently supported by SAFE_CAP_REVIEW.md from the native
reviewer. No scientific runner, numerical fixture or canonical cache was changed.

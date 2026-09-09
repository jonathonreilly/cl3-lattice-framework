# Independent review: minimal first-action data augmentation

Verdict: PASS as a source-only conditional theorem, not an achieved generator, leakage or propagated-state certificate. Reviewed DERIVATION3d766b12fb0aae514aeb392fc7c8d7ce9f8f954dd14f1ea143504b0c061b3e81 and the complete frozen package. I authored/reviewed related Ward and original-domain source work, but did not author this augmentation. No native entries, input reader, matrix builder, integral or propagation was called. Independent tiny checks give2442 integer/rational predicates; their scope is explicitly algebra only.

## Algebra and domains

The original raw399 sources and covariance closure798 stay the domain. The three additional bare vectors are qA=dA/2,qC=dC/2,qD=d_all/2; their Gram determinant is1/8, and the complement of A∪C supplies the elementary independence proof. This says nothing about independence modulo original nonlocal F. The enlarged402/804 carrier is a DATA workspace only. Original798-domain V=FC has its action represented there; applying H to arbitrary DATA vectors would introduce second-action information and remains excluded.

From y=-i(H-isigma*s)^−1, K y=sigma*s*y−v. Kw=d and Ke0=d_all establish all free column rules, including their Gamma copies since K commutes with Gamma. With x0=e0/2 and qA=dA/2, DeltaK f=8[x0<qA,f>−qA<x0,f>] exactly, including Gamma columns. DeltaK generally does NOT commute with Gamma. Independent finite algebra explicitly exhibits this noncommutation and tests the displayed formula on both ordinary and Gamma-transformed basis columns. Thus the displayed D_A uses actual enlarged Gram rows, not an invalid covariance shortcut.

The closed Gram M=[[G,J],[-J,G]] has the correct sign for J(a,b)=<a,Gamma b>. Hence F*H_A F=iE^T M D_A and action Gram D_A^T M D_A are correct. For complex C, adjoints in the stated formulas are essential. The leakage identity is meaningful only for a certified exact isometry and must retain the dependence D_A(M); a midpoint substitution does not certify it.

## New-entry signs and scales

The local restriction of y is sigma*s(A N−D O)+D T. Multiplying the bare source by1/2 and pole bysqrt(alpha) gives the proposed G. The restriction of Gamma*y is B N−(mu−s²B)O/6−sigma*s*B T/6, giving the proposed J. Ward/bare G vanishes by opposite sublattice. Skew-adjoint Gamma converts the prior <w,Gamma u>=d^T(cN−mu O/6)u into the stated negative bare/Ward J, with1/4 scaling.

Gamma restricted to the local center-neighbor block is−mu*T/6. Therefore J(qD,x0)=−mu/4, and J(qA,x0)=J(qC,x0)=−mu/12. These signs were checked independently from literal oriented T. The new-new block is the displayed Gram and has exact J zero. New sources are negative chiral, unlike the old positive insertions; closure must retain this distinction.

All calculations use h=1. Restoring h multiplies the generator action, not these dimensionless source formulas. No finite-volume gap or extra covariance moment is being inferred.

## Error ledger

For neighbor v, signed geometry gives |u^T N v|,|u^T O v|≤2 and u^T T v=0; for center only |u^T T e0|≤6 survives. With sqrt(alpha)/2<2 and s≤16:

- A sensitivity≤2s(2+s²/3)<2800 for neighbors, and≤2s²≤512 for center.
- B sensitivity≤2(2+s²/3)<176 for neighbors, and≤2s≤32 for center.
- mu sensitivity≤2/3 for pole crosses; insertion c≤1/2 and mu≤1/4.

Thus804 times the stated sum is a valid deliberately loose row-sum bound on the NEW supported perturbation. Adding the embedded OLD bound once is correct. The trace grows by exactly5 to<536. Zero-padding stationary coefficients preserves their norm≤1. The equivariant factor dimensions1608 are consistent with804 data columns. Exact rational comparisons confirm all displayed budget inequalities, including the corrected A budget2^40+804*2800; replacing that by2^41 would not establish the quoted2e−6 intermediate target. The supplier's failed earlier control and original source are preserved rather than hidden.

The total arithmetic radius2^-60 applies to the complete matrix, not independently to each block. The imported1e−6 geometry/input reserve remains a CONDITION to be verified in an eventual runtime, as explicitly stated upstream; it is not discharged by these synthetic controls. In particular accepted mu at the specified radius, pole/weight/root error, actual complete-matrix arithmetic and coefficient gates still must be bound. This does not obstruct the sufficient conditional ledger.

## Practical limits

Neither scalar sensitivity nor trace control supplies a bound on C or on the quadratic leakage expression after interval propagation. D_A depends on M, and a badly conditioned choice of C can amplify errors. The6h nearby-frame action estimate is an additional separately certified allowance, not a substitute. A new DATA append runtime would need accepted mu, exact signs and common normalization, retention and arithmetic gates; none was executed here. No action on a newly enlarged compression domain, small leakage, useful rank, alpha value or phase follows.

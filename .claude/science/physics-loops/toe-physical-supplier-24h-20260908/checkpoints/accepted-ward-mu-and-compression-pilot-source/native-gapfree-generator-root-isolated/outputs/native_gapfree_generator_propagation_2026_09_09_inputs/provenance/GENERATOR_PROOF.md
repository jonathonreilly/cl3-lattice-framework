# Signed generator closure and a gap-free positive-energy alternative

Source-only, h=1 unless restored explicitly. No native Gram, inverse, semigroup or scalar integral is evaluated. This derives a constructive input closure, not a practical achieved propagation certificate. Import the actual K/h0 convention, common pole and Ward formulas, and the canonical positive-band theorem. Let H0=iK, Gamma0=i sign(H0), so Gamma0 K=|H0| and Gamma0 is NOT K/|H0| (it is its negative).

## 1. A finite algebraic action closure

For y_sigma(v)=-i(H0-i sigma s)^-1 v=-(K-sigma s)^-1v,

 K y_sigma(v)=sigma s y_sigma(v)-v.

For the actual Ward vector w_A, H0 w_A=i d_A, hence K w_A=d_A. Also K e0=d_all=sum of all three signed opposite-neighbor pairs. K commutes with Gamma0, so the same action identities hold for all reference-complex-structure partners.

A two-link flip changes K by
 DeltaK_A=2(e0 d_A^T-d_A e0^T).

Its action on any vector is determined by the two bare overlaps. Thus if F contains the common resolvent columns, e0,w_A,w_C and their Gamma0 partners, every K_A F column belongs to span(F,L,Gamma0 L), where L is the finite local seven-star space (one can reduce this to the actual d_A,d_C,d_all support span). No higher spectral moment is needed for the FIRST generator action and its norm Gram. This is an exact infinite-Hilbert-space identity, not an assertion that span(F) is invariant.

To compute F^T K_A F and (K_A F)^T(K_A F), it suffices to certify the common Gram enlarged by bare local star columns and Gamma0 partners, with the same phase and scale. All balancing coefficients sigma*s and sqrt(alpha) must be propagated; do not replace a weighted column by an unweighted source silently. Existing scales1/2 on the Ward insertions are exact.

## 2. Exactly one additional scalar for this first-action closure

The Ward-only stationary catalog A,A',B,B',a0,c_minus does not supply every bare-neighbor projected overlap. The missing scalar is mu=E sqrt(X), already the separate reference-energy integral in the campaign; it must be bound to its actual acceptance, not inferred from c_minus.

For local real star columns u,v use the literal seven-star I,O,T,N matrices of the parent. Put D=(1-s²A)/6. The bare-pole overlaps are

 <u,y_sigma(v)>=u^T[ sigma*s*(A I+(A-D)O)+D T ]v,
 <u,Gamma0 y_sigma(v)>=u^T[ B N-(mu-s²B)O/6-sigma*s*B T/6 ]v.

The mu O term canceled in stationary pole-pole divided differences but does NOT cancel in this single-resolvent boundary. Center rows have O=0, explaining why the previous center append did not need mu. The signs agree with the existing center Ward API.

Bare-bare Euclidean overlaps are literal local coordinates; local reference covariance is

 U^T Gamma0 U=-(mu/6)T.

For example K Gamma0=|H0| on the diagonal fixes this sign and coefficient: at center sum over six neighbors gives mu. Cubic symmetry makes the six contributions equal. Same-sublattice entries vanish and no star nearest-neighbor links other than center-neighbor occur.

Ward-bare Euclidean entries vanish for bare neighbors and equal1/3 for e0. The parent gives

 <w_A,Gamma0 e_j>=d_A^T[c_minus N-mu O/6]e_j.

Ward-Ward entries use only a0 and the exact O geometry, as already reviewed. Together these formulas certify the full enlarged action Gram using A,A',B,B',a0,c_minus,mu and literal geometry. No newly evaluated lattice moment beyond mu is required. General h follows by restoring the parent h factors and K-action coefficients; this note's displayed overlaps use h=1.

The closure is only first-action. Repeated powers introduce progressively more distant local sources; their covariance moments are not automatically contained in this seven-star catalog. Therefore this argument does not by itself supply the896 Krylov directions of the degree128 positive-band theorem.

## 3. Exact signed compression and leakage

Let V be an EXACT isometry onto a finite common real subspace built from the enlarged data, with Pi=VV^T. Set A=V^*H_A V (complex Hermitian) and R=(I-Pi)H_A V. Then

 R^*R=V^*H_A²V-A².

The two terms come from the first-action Gram above. Interval Gram conditioning, unknown exact nullspace, coordinate normalization and coefficient rounding must be certified before using this equality numerically. A midpoint or PSD-shifted factor is not automatically this exact V. The existing equivariant dilation theorem can provide an actual nearby V only with its stated factor error and common-source embedding; those errors must be propagated into A,R.

For the actual signed nearest-neighbor operator, ||H_A||<=6h by the degree-six Schur bound, including the flipped signs. No active gap is needed. A small leakage norm is a quantitative question, not a consequence of algebraic closure or small stationary-projector error.

## 4. A gap-free positive-energy route using absolute value

There is a useful alternative to assuming that the trial frame lies exactly in the positive band. Let M=6h and H_d=Pi H_A Pi+(I-Pi)H_A(I-Pi). Since the offdiagonal block has norm delta=||R||, ||H_A-H_d||=delta and ||H_d||<=M. Thus

 ||H_A²-H_d²||<=2M delta,
 || |H_A|-|H_d| ||<=sqrt(2M delta).

The second line is the positive square-root operator Hölder inequality. Both absolute values are positive. Duhamel for their contraction semigroups yields, for every t>=0,

 || e^(-t|H_A|)V - V e^(-t|A|) || <= t sqrt(2M delta).

This supplies an actual finite positive generator |A| without pretending A itself is positive or inserting an unjustified uniform active gap. It is a ONE-PARTICLE propagation bound. To represent the physical excitation state, its true positive-band source/pairing and impurity vacuum still need the accepted projector/frame approximation. Approximate positive-band leakage and vacuum/scalar errors are separate; the bound does not turn arbitrary real vectors into excitation modes.

On an at-most-n excitation sector, telescoping contraction tensor powers bounds the propagation error by n times the one-particle error. Initial state/particle truncation tails remain separate. Pairing Hilbert-Schmidt propagation similarly costs at most2 times the one-particle error times the pairing HS norm, before its own initial approximation error. No determinant conditioning improvement is claimed.

At t=100/h a desired one-particle error epsilon requires delta<=epsilon²*h/120000 by this conservative route. Even epsilon=.001 requires leakage<=h/120000000000. Nothing in the present stationary Gram certificates proves such leakage. This is a precise remaining quantitative estimate; an actual generator Gram calculation could certify it or honestly fail. No timing or affordable rank is claimed.

## 5. Relation to a stationary-projector approximation

If an actual common rounded approximation Gammahat_A to Gamma_A=i sign(H_A) satisfies operator error eta, then |H_A|=Gamma_A K_A implies error<=6h*eta on replacing Gamma_A by Gammahat_A. This computes approximate positive-energy matrix elements from the SAME enlarged first-action Gram and the certified finite-rank stationary correction. It does not make eta=0 or establish exact positive-band membership. Direct rotation/orthonormalization of projected vectors needs a lower Gram bound or a conditioning-free factor theorem with its own error, and still requires a leakage certificate. This is a second conditional route, not an additional bath scalar requirement.

Conclusion: the missing first-generator INPUT closure is finite and requires mu in addition to the Ward catalog. The missing PRACTICAL propagation theorem is small leakage/coordinate error (or certified higher positive-band moments), not an unknown new local integral at first order. No nonzero alpha, fixed-U stability or achieved imaginary-time error follows here.

# Mixed-reference real-time Gaussian kernel with an explicit Spin lift

New analytic implementation route for independent review. The finite restriction of the infinite Gaussian reference is retained exactly; it is not replaced by the vacuum of a compressed hopping matrix. No native matrix, time integral, or compressed physical kernel has been evaluated here.

## 1. State and conventions

Let V be a finite real one-particle subspace of even dimension d=2n. If a cyclic subspace has odd dimension, append one auxiliary Majorana with zero covariance and zero dynamics. The resulting even Gaussian extension has exactly the same even correlations on V, which are the only ones used here.

Write {gamma_i,gamma_j}=2 delta_ij and
Gamma_ij=(i/2) omega([gamma_i,gamma_j]).
Then Gamma is real skew, ||Gamma||<=1, and
omega(gamma_i gamma_j)=delta_ij-i Gamma_ij.
The required state is Gamma=P Gamma_infinity P. It can be mixed, have eigenvalues at the pure-state boundary, or fail to commute with the compressed K. None of the formulas below uses arctanh(Gamma), a thermal density inverse, or sign(K).

For H(K)=(i/4)gamma^T K gamma and U(t)=exp(-itH(K)), coefficient conjugation is U gamma(c) U^-1=gamma(Rc), R=exp(tK). In a real canonical plane K=omega[[0,1],[-1,0]], U=cos(omega t/2)+sin(omega t/2)gamma_1 gamma_2. This fixes the Spin sign convention.

## 2. One factor and its branch

Where R+I is invertible, put C=(R-I)(R+I)^-1. This is real skew. The exact Clifford expansion is

 U=a sum_(I even) Pf(C_I) gamma_I,
 a=product_(positive modes j) cos(omega_j t/2).

It follows first in the canonical planes from the preceding cosine/sine formula, then by real orthogonal covariance. The identity coefficient a is the SIGNED continuous cosine product, not abs(a), nor an independently selected scalar square root of det((I+R)/2). Consequently this expression retains the Spin double-cover sign even after long rotations. Zero frequencies contribute one.

A Cayley singularity is not a physical singularity. A declared implementation can split that particular U exactly into equal short factors, with |t| ||K||/p <=1, so every short factor has positive cosine prefactor and bounded Cayley matrix ||C||<=tan(1/2). This is an exact factorization, not a changed time or selected outcome. It increases the number of factors; no claim that this is affordable at a long filter cutoff is made. On an unsplit nonsingular chart one should retain signed logarithmic prefactors and pivot diagnostics. Neither option authorizes treating a numerically tiny pivot as certified zero.

## 3. A single Pfaffian for a mixed expectation

Consider an ordered product U_1...U_m, initially with no insertions. Form D=md labeled copies of the Majorana indices in factor order. Let C_block be the block diagonal matrix of the C_j. Form an antisymmetric contraction matrix W on these labels by setting, for each earlier label (j,a) and later label (k,b),

 W_((j,a),(k,b))=delta_ab-i Gamma_ab,

and reflecting antisymmetrically. Within one block distinct indices have no delta term. Across distinct blocks the identity term MUST remain, including repeated physical indices. Wick's rule applies to the ordered word, rather than to an exterior product that would discard these repeated contractions.

Then

 omega(U_1...U_m)
 = (product_j a_j) (-1)^(D(D-1)/2)
   Pf( [[C_block,-I],[I,-W]] ).                         (1)

Proof: expand each U_j in its exact even Clifford coefficients. Wick contracts every selected ordered subset I to Pf(W_I). The elementary Pfaffian minor-summation identity expands the displayed block Pfaffian to sum_I Pf((C_block)_I)Pf(W_I), with the displayed overall sign. This proves (1) also for pure boundary covariances by polynomial continuity. It uses a normalized expectation; no extra factor of 2^-n, spectator degeneracy, or physical parity projection is inserted.

Unlike a transition-covariance formula that divides by omega(U), (1) remains algebraically meaningful at an overlap zero. Its only chart denominators are those of the individual Spin factors, already identified above. A numerical Pfaffian still needs an arithmetic error analysis before it is an interval certificate.

## 4. Two inserted linear fields

Insert gamma(x), gamma(y) at their actual positions among the even factors. Add two ordered labels to the preceding construction, with contraction of any earlier coefficient vector p and later q equal to p^T(I-i Gamma)q. These are bilinear contractions, with no complex conjugation. For the even-factor labels p is its corresponding coordinate vector.

Let the two insertion labels have indices i<j among D=md+2 labels. Set their C entries to zero. The desired expectation is the coefficient of lambda when C_ij=lambda, C_ji=-lambda. Since no other C entry meets either insertion, that coefficient selects exactly the two fields in their original order. Equivalently replace the Pfaffian in (1) by

 (-1)^(i+j+1) Pf(M with upper-block rows/columns i,j removed),
 M=[[C_block,-I],[I,-W]].                              (2)

The overall sign in (1) uses the enlarged D. This is one Pfaffian minor, not subtraction of two close overlap values and not a division by an overlap. It directly evaluates the two-insertion real-time cocycle kernels. For a scalar energy shift, multiply by the known scalar phase; the shifts cancel in a cocycle whose signed times sum to zero.

## 5. Covariance-error bound without a mixed-state spectral gap

There is also a useful dimension-polynomial continuity estimate. Suppose Gamma and Gamma' are valid real skew covariance matrices with ||Gamma-Gamma'||<=epsilon. A pure Gaussian extension to twice as many Majoranas has covariance

 J(Gamma)=[[Gamma,sqrt(I+Gamma^2)],[-sqrt(I+Gamma^2),-Gamma]].

It squares to -I and restricts to Gamma. Since ||Gamma^2-Gamma'^2||<=2epsilon and the positive square-root map obeys the operator-norm one-half Holder bound,

 ||J(Gamma)-J(Gamma')||<=epsilon+sqrt(2epsilon).

For pure Gaussian states, their principal-angle product formula gives
1-|<Psi,Psi'>|^2 <= ||J-J'||_F^2/8.
This follows by bounding one minus the product of principal-angle cosines by the sum of their squared sines. Partial trace cannot increase trace distance. Therefore, for any bounded operator O on the original finite CAR algebra,

 |omega_Gamma(O)-omega_Gamma'(O)|
 <= min(2, sqrt(d)[epsilon+sqrt(2epsilon)]) ||O||.       (3)

This bound is deliberately conservative but does not assume eigenvalues of Gamma stay away from +/-i. The input approximation must itself be a valid covariance, or a separately controlled projection onto that set must be accounted for. For two complex linear insertions use ||gamma(x)||<=sqrt(2)||x||_2 unless their real structure licenses the sharper equality. Real-time unitary factors do not increase the operator norm. This lemma requires independent review; it is not a claimed implemented covariance certificate.

## 6. Actual synthetic checks and cost boundary

The companion source compares (1)-(2) with independent dense two-mode Jordan-Wigner matrix exponentials for maximally mixed, strictly mixed, and pure covariances, short three-factor cocycles and a long single factor with a negative Spin prefactor. All 27 comparisons pass (maximum discrepancy about 1.34e-15). Dropping the cross-factor identity contraction produces 24 mismatches; replacing the signed lift by its absolute value produces 9. These are direct adverse variants, not subprocess production controls. An initial JSON serialization failure for NumPy integer counters is preserved; only serialization changed before the successful synthetic rerun.

The toy Pfaffian routine uses a small-pivot cutoff and ordinary floating arithmetic. It is a normalization witness, not a production certifier. No mathematical zero, rigorous residual, or large-n stability is inferred from it.

For m fixed Cayley-chart factors, the Pfaffian dimension is 2md (or 2md+2 after the insertion minor), with dense memory O(m^2 d^2) and arithmetic O(m^3 d^3). This is polynomial instead of 2^(d/2), but a many-thousand-dimensional cyclic space may still be unaffordable. Splitting long factors to enforce a uniformly bounded chart can make m grow with time. A real compressed-state pilot needs certified moment/Gram data, covariance error, a declared chart policy and actual cost measurement. The successful pure L4 pilot establishes none of these large-carrier premises.

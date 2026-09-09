# New selected-principal certificate for the same ordered frame

PROVISIONAL independent derivation; no saved history, selected Gram, native entry, or numerical probe has been loaded. This is a new certificate method, not a retry or reinterpretation of an old interval-C failure. The fixed physical family F consists of the already specified exact rational midpoint poles/weights and outward square-root coefficients. Unknown exact Gauss roots/pi are not substituted. Physical scalar enclosures and quadrature displacement remain separate.

## Exact frame and ordered gauge

Let s_1,...,s_k be the original selected seed vectors, in exactly the old selected order, with no reselection. Put S=(s_1,Gamma s_1,...,s_k,Gamma s_k), p=2k. Gamma is real orthogonal, Gamma²=−I. Assume the selected vectors are independent. Their p×p real Gram G=S* S is positive definite and commutes with the fixed block complex structure. Write G=L L*, with L lower triangular and strictly positive diagonal. Then V=S L^{-*} is exactly the sequential positive-normalization Gram–Schmidt frame, not just another basis of its span.

The paired recurrence is the same construction. At every pair the Schur complement has a 2×2 scalar diagonal block, since Gamma is skew and preserves all prior paired spans. The two residual vectors are b,Gamma b with the same positive norm. Off-diagonal 2×2 blocks encode g and j with signs fixed by <Gamma x,y>=−<x,Gamma y>. Thus interleaved ordinary Cholesky reproduces the paired frame provided its order is (s,Gamma s), not (Gamma s,s), and positive normalization is retained. This statement does not choose a new Fock phase or mix an arbitrary orthogonal gauge into the saved interface.

The selected seeds have known exact sparse coefficient matrix E in the original raw-plus-Gamma labels: S=F_R E. Each half seed has two entries ±1/2, each paired Gamma seed uses the corresponding Gamma-labelled entries; insertion seeds have one entry. Hence the exact desired original-family coefficients are C=E L^{-*}. They can be computed from selected-principal scalar products alone. The 399-dimensional pivot rows are not needed to identify this already selected frame. Selecting a new pivot would still need additional information.

## A posteriori certificate without a numerical factorization assumption

Choose any exactly represented upper triangular T with positive diagonal, intended to approximate L^{-*}. A floating factorization may propose T, but contributes no correctness assumption. Form a certified symmetric enclosure of

 H=T* G T,   H=I+D.

For example, if G0 is a rational center and ||G−G0||_F<=eta_G, a valid bound is

 e >= ||T*G0 T−I||_F + ||T||_2² eta_G.

All norms/products on the right need rigorous rational/interval bounds, including candidate-rounding error where relevant. Let delta>=||D||_2 with delta<1; taking delta=e is valid though possibly pessimistic. This proves G positive definite. Let R=chol_upper(H), H=R*R. Then

 V=S T R^{-1},   C=E T R^{-1}.

This is the SAME ordered frame: T R^{-1} is upper triangular with positive diagonal, and its inverse is therefore the unique positive upper Cholesky factor of G. A polar correction H^{-1/2} alone would only produce an isometry in a potentially different gauge; it is not substituted here.

There is an explicit gap-free correction bound. Along H(t)=I+tD let R(t)*R(t)=H(t), R(0)=I, and X=R'R^{-1}. Then

 X*+X=R^{-*} D R^{-1}.

For a symmetric real matrix A, its unique upper triangular half Phi(A), diagonal A_ii/2, satisfies ||Phi(A)||_F<=||A||_F/sqrt2. Thus

 ||(R^{-1})'||_F <= e/[sqrt2 (1−t delta)^{3/2}].

Integration yields

 ||R^{-1}−I||_F <= B(e,delta)
 = sqrt2 e/delta ((1−delta)^{-1/2}−1)
 <= e/[sqrt2 (1−delta)^{3/2}],

with continuous first expression e/sqrt2 at delta=0. If delta=0 the actual D is zero, so exact correction is zero. An entirely rational looser bound uses sqrt2>=1 and (1−delta)^{3/2}>=(1−delta)², giving B<=e/(1−delta)². This avoids transcendental arithmetic when convenient.

Therefore centered at exact C0=ET, every coefficient lies within

 b_C=||ET||_2 B(e,delta)

of C0 (Frobenius error bounds every entry). A sufficient unchanged coefficient-width gate is 2 b_C<=2^-39, including any final endpoint rounding. The original l1 gate can be checked with column sum |C0_ij| plus the corresponding interval radii. This norm certificate is sufficient, not necessary: verified triangular interval refinement may materially improve its conservatism. It is not claimed that this bound passes for native k=12 or24.

The derivative derivation uses only finite positive matrices and exact norms. No active bulk gap, eigensolver backward-stability theorem, or condition-number guess is imported.

## What can and cannot improve

The error eta_G represents direct physical input uncertainty plus fresh arithmetic enclosure. It must not be confused with the widths of recursively computed saved pivot r. Direct selected Gram contractions avoid feeding earlier uncertain g/r and beta intervals through every subsequent recurrence, and retain symmetry/shared entries once. This can remove artificial dependency widening. Raising working bits only removes arithmetic rounding; it cannot shrink fixed physical eta_G or repair a true small principal eigenvalue.

A sharp obstruction is already two-dimensional: G=diag(1,r), with independent admissible r in[l,u]. The unique positive second coefficient is r^{-1/2}, so every enclosure valid for this whole input set has width at least l^{-1/2}−u^{-1/2}. No direct factorization can beat that information-theoretic range. For a half raw coefficient the factor is1/2. Thus the fresh-width diagnosis remains valid for the historical saved-r algorithm, but does not prove the direct principal input uncertainty has the same admissible r range. That distinction is exactly what the new method would test.

Conversely, consider exact S columns (1,0),(1,epsilon). Its Gram is [[1,1],[1,1+epsilon²]], highly ill-conditioned for small epsilon, but exact rational Cholesky gives the original frame exactly and C=[(1,0),(-1/epsilon,1/epsilon)]. If an earlier interval computation separately encloses two occurrences of the same uncertain x and forms epsilon²+x−x without retaining correlation, it manufactures width4d for x in[−d,d]; a symbolic/shared-data cancellation has zero width. This example demonstrates a dependency mechanism, not that native inputs have that correlation or that conditioning is harmless.

## Selected-principal cost and leakage interface

The commuting paired Gram is determined by k real diagonal and two real numbers per unordered pair: k² independent real scalars. A half/half entry needs at most four raw contractions, so a conservative structured plan needs at most4k² raw requests per orbit (2304 at k24,11520 across five). Without exploiting Gamma structure, p(p+1)/2 half entries cost at most4 times that count:4704 raw requests per orbit at p48. Repeated requests can be cached; these are upper counts, not a measured runtime forecast. Factorization/residual verification costs O(p³) scalar operations and O(p²) storage, with potentially large exact-integer bit complexity. Coefficient embedding has at most4k distinct raw/Gamma support labels and is sparse.

For the existing leakage interface, certify C on the SAME F_R and preserve all exact coefficient correlations needed by a separately reviewed action bound. The prior identity K_A F_R C=F_R Lambda C+QY and cancellation RF_R C=0 remain applicable to the exact ordered C. A box enclosing this C may be used conservatively; its midpoint must never be asserted to be an isometry. Additional raw R-Q and Q-Q inputs for the source term remain required (at most8|R|+36 raw Gram values per orbit), unless already accepted with matching definitions. Selected Gram alone is not a leakage or propagation certificate.

No actual selected-input binding, runtime, achieved width, action/leakage value, or success forecast is supplied here. A prospective new once-only contract would first freeze selected sequence, candidate construction, direct-entry error ledger, exact verification thresholds, failure retention, and its measured or conservatively justified cost. The old failed protocol and target remain unchanged.

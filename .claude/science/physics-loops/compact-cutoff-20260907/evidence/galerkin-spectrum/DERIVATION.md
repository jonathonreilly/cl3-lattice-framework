# Low-energy Ritz certificates for the actual compact cube cutoff

This is a source-specific application of the variational principle and Schur complement, not a new general spectral method or a physical action-selection claim. The prospective contract and separate adverse-control supplement precede the finite checks. The analytical candidate preceded the contract, as explicitly recorded. Import the frozen block32 cutoff construction and the block29 compact Hamiltonian. No repo source is changed.

## 1. Operator hypotheses and indices

Work either on the twelve-link Hilbert space or its exact local-gauge-invariant reducing subspace. The compact-group elliptic operator K has compact resolvent, and bounded V preserves this property. For fixed a>0 and v>=0,

 H=K+V,  K=(3/(2a))(-Delta_total),  0<=V<=M I,  M=12v.

Let P=P_R be the finite Peter–Weyl cutoff restricted to the chosen Hilbert space, Q=I-P. The range of P lies in D(K), P commutes with K, and the imported exact threshold is

 g=g_R=[ceil(3(R+1)^2/4)+3(R+1)]/a,  QKQ>=gQ.

The restriction to physical states retains this bound even when it is not sharp. Write d=rank P on the chosen space; no identification of d with the unrestricted tensor storage dimension is made. Let E_0<=E_1<=... denote the exact eigenvalues of H and mu_0<=...<=mu_(d-1) those of A=PHP, all repeated according to multiplicity. A first spectral gap means E_1-E_0 when the ground is simple; if it is degenerate that ordered difference is zero, not the next distinct eigenvalue.

Set B=PVQ and D=QHQ on Q's kinetic domain. Then D>=g. Let b be any established bound on ||B||. Besides the crude b<=M, positivity gives the useful improvement

 B=P(V-MI/2)Q,  ||B||<=||V-MI/2||<=M/2=6v.       (1)

This is a full operator inequality; it does not estimate one selected matrix element. Exact model-specific coupling information may replace b. The block decomposition H=[[A,B],[B*,D]] has bounded off-diagonal blocks because PKQ=0 and V is bounded.

## 2. Schur inertia and the number of low states

For any real z<g, D-z is positive and invertible. On the form domain, completing the square gives

 <p+q,(H-z)(p+q)>
 =<p,[A-z-B(D-z)^(-1)B*]p>
  +||(D-z)^(1/2)[q+(D-z)^(-1)B*p]||^2.             (2)

The triangular substitution is a bounded invertible map of the form domain: (D-z)^(-1)B*p lies in D(D), and p ranges over a finite-dimensional space. Therefore the maximal dimension of a strictly negative form subspace is exactly the negative inertia of the finite Schur matrix. This supplies the needed domain justification; no formal inverse of H-z is assumed at an eigenvalue.

Let N_T(z) count eigenvalues strictly below z, with multiplicity. Since

 0<=B(D-z)^(-1)B*<=c(z)I,  c(z)=b^2/(g-z),

finite-dimensional minmax in (2) gives

 N_A(z) <= N_H(z) <= N_A(z+c(z)) <= d.             (3)

The strict counting convention is part of the statement. In particular, if both finite counts in (3) agree, they certify the exact number of eigenvalues below z. Otherwise the band [z,z+c(z)) is unresolved by this estimate. All exact states below g are accounted for through the Schur matrix; there cannot be an additional family of low excluded states invisible to this count. It is not asserted that their exact vectors lie in P.

## 3. Eigenvalue intervals and monotonicity

The variational principle immediately gives

 E_j<=mu_j,  0<=j<d.                              (4)

If E_j<g, choose z decreasing to E_j from above, still below g. Then N_H(z)>=j+1, so (3) proves j<d and mu_j<z+c(z). Taking the limit yields

 0<=mu_j-E_j<=b^2/(g-E_j).                        (5)

Thus (5) remains valid at exact degeneracies without selecting eigenvectors. For every fixed energy ceiling E<g it holds simultaneously for all E_j<=E, with upper error b^2/(g-E). This is a finite low-energy window statement, not a full-spectrum rate.

For a directly usable finite certificate suppose mu_j<g. Solving mu_j<=E_j+b^2/(g-E_j), using (4), gives

 ell_j=(g+mu_j-sqrt((g-mu_j)^2+4b^2))/2,
 max(0,ell_j)<=E_j<=mu_j.                         (6)

Equivalently delta_j=mu_j-ell_j is the nonnegative solution of
 delta_j(g-mu_j+delta_j)=b^2,
 and delta_j<=b^2/(g-mu_j). The endpoint function ell(mu) is increasing. Therefore a rigorous numerical Ritz enclosure L_j<=mu_j<=U_j<g gives the fully certified interval

 max(0,ell(L_j))<=E_j<=U_j.                       (7)

No floating eigenvalue is implicitly treated as an exact mu_j. The rational isolating intervals in the finite controls below are distinct from computing the actual large cube matrix.

For nested cutoffs the Ritz values decrease with R once their index exists. They converge to E_j: P_R converges to I in the K form norm on form-domain vectors because it is a monotone spectral-block cutoff commuting with K; bounded V makes the H and K form norms equivalent. Applying this to each finite exact low eigenspace proves form-core Rayleigh convergence. Alternatively, once a finite Ritz upper bound for index j is available, (5) and g_R->infinity already give the explicit convergence bound.

## 4. The gap requires the ground shift

For d>=2 and mu_1<g, apply (6) to both levels. With G_R=mu_1-mu_0,

 max(0,G_R-delta_1) <= E_1-E_0 <= G_R+delta_0.      (8)

The upper bound can be sharpened by replacing ell_0 by max(0,ell_0). The corresponding interval-certified version is

 max(0,ell(L_1)-U_0) <= E_1-E_0
                       <= U_1-max(0,ell(L_0)).    (9)

A strictly positive lower endpoint proves that the exact ground is simple and that this is its first gap. Otherwise the estimate does not settle ground degeneracy. Neither a general upper nor a general lower ordering between G_R and the exact gap is valid: both eigenvalues move downward under the variational relaxation, and their shifts need not be ordered. The two adverse controls below demonstrate both directions.

If E_1<=E<g, both nonnegative Ritz errors lie in [0,b^2/(g-E)]. Their difference therefore has absolute value at most b^2/(g-E), not necessarily twice that quantity. By (1), a sufficient uniform low-window eigenvalue and first-gap error condition is

 g_R >= E+36v^2/epsilon,  g_R>E,                  (10)

for epsilon>0, provided the level indices and the stated exact energy ceiling are justified. A computed upper ceiling mu_1<=E suffices. This gives an explicit finite storage prescription through block32's exact D_R formula, but does not supply a fast algorithm to diagonalize the resulting matrix or compile its qubit dynamics.

## 5. A direct actual-Haar ground corollary at R=0

The imported block32 calculation on the physical constant state gives exactly

 mu_0=6v,  b^2=||Q_0 V1||^2=v^2/3,  g_0=4/a.

Because P_0 has rank one, this norm is the full off-diagonal operator norm. If 6v<4/a, (6) gives

 max(0,[4/a+6v-sqrt((4/a-6v)^2+4v^2/3)]/2)
      <= E_0 <= 6v.                              (11)

The simpler shift bound is 6v-E_0<=v^2/[3(4/a-6v)]. This is a nontrivial actual-model ground-energy interval derived from Haar orthogonality, not an arbitrary matrix substitution. R=0 supplies no second Ritz level and hence no gap certificate. At v=0 the ground is exactly zero; no positive interaction effect is inferred.

## 6. Exact controls and adverse boundaries

The frozen finite checker uses rational K,V and exact Sturm root-isolating intervals, with no floating fit. Its two-level fixture has E_0=6-sqrt26<mu_0=1, exposing the false equality or reversed Ritz inequality. A three-level all-ones positive V makes the finite gap exceed the exact gap. The separately preregistered ground-only coupling makes the exact gap exceed the finite gap. Both pass (8) with a strictly positive lower certificate.

An uncoupled K=diag(0,20,10), P on its first two coordinates has Ritz levels0,20 and exact levels0,10,20. Thus even b=0 does not justify equal-index matching above the omitted threshold g=10. A small-threshold rank-one fixture violates mu_0<g and has a vacuous nonnegative lower interval; it is retained, not retuned. Its missing second Ritz index is explicitly checked.

All43 named finite checks passed, including the positive resource guard, at approximately0.138seconds/59.672MiB. A SymPy BooleanAtom summation implementation failure was preserved and corrected only by explicit boolean-to-integer conversion. These controls support the algebraic interface; the infinite-dimensional theorem is the form/inertia/minmax proof above. No whole-cube finite eigenvalue, physical coupling, continuum, thermodynamic or Yang–Mills mass-gap claim is made.

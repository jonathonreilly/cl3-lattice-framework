# Relative Gaussian determinant jets for high trial moments

Provisional source-only route. The exact finite-dimensional identity and coefficient recurrences below have rational synthetic Fock checks. Application to the supplied infinite native model still needs an independent domain/normalization review and explicit scalar-table reduction. No native scalar, moment, saved array, or comparison value was loaded. No scientific execution protocol is authorized by this note.

## Finite-dimensional identity with the scalar shift retained

Let real Majoranas satisfy {gamma_i,gamma_j}=2 delta_ij. Let K0 be real antisymmetric, h0=iK0 Hermitian with no zero modes, and let Omega be its pure filled-negative-band Fock vacuum. Write P=1_(h0<0), E0=Tr(P h0)/2. The normal-ordered free Hamiltonian is H0=(i/4) gamma K0 gamma-E0, so H0 Omega=0. For real orthogonal a,d, put

 B=i gamma(a) gamma(d), V=2i(ad*-da*), hA=h0+V,
 D=H0+B=(1/4) gamma hA gamma-E0.

Here the factor two in V and the vacuum energy subtraction are essential. With Z(t)=<Omega,exp(-tD)Omega>, the local analytic branch fixed by Z(0)=1 satisfies

 Z(t)^2=det(I+P[exp(t h0)exp(-t hA)-I]).                  (1)

A finite-dimensional derivation uses the squared spin-character identity
 [Tr exp((1/4)gamma A gamma)]^2=det(I+exp A)
and its product version near the identity, then takes the normalized free Gibbs expectation as inverse temperature beta tends to infinity. The character follows by reducing a generic complex antisymmetric generator to two-dimensional blocks and extends analytically; the squared identity removes the spin sign. In the zero-temperature ratio,

 det(I+exp(-beta h0)exp(-t hA))/det(I+exp(-beta h0))
   ->det(I-P+P exp(-t hA)).

The Fock scalar shift contributes exp(2t E0). Since P commutes with h0, this factor combines with the last determinant to give(1). The square root is fixed analytically near zero. This does not claim a globally single-valued square root through arbitrary complex determinant zeros. On the real finite-dimensional axis the expectation is positive. Positivity of D is not needed for this identity, though it is needed for the intended inverse-residual certificates.

## Division-free matrix-jet recurrence

Write U(t)=exp(t h0)exp(-t hA)=sum U_k t^k. Then

 U_0=I, (k+1)U_(k+1)=h0 U_k-U_k hA, U_1=-V.             (2)

Set G_0=0,G_k=P U_k for k>=1. The inverse series R(t)=(I+G(t))^-1 has R_0=I and

 R_n=-sum_(k=1..n)G_k R_(n-k).                            (3)

With ell(t)=log Z(t)=sum_(n>=1)ell_n t^n,

 n ell_n=(1/2)sum_(j=0..n-1)(n-j)Tr[R_j G_(n-j)].         (4)

Finally Z_0=1 and

 n Z_n=sum_(k=1..n)k ell_k Z_(n-k),
 m_n=<Omega,D^n Omega>=(-1)^n n! Z_n.                     (5)

Only division by known positive integers occurs. There is no eigenvalue solve, matrix inverse pivot, numerical differentiation, determinant fitting or new trial parameter. Order and the factor1/2 in(4) must be preserved. A future interval implementation must bound cancellation and arithmetic growth; formal exact identities alone do not establish an affordable certified width.

## Finite-rank representation before any native acquisition

For jets through order N, every U_k,1<=k<=N, has both column and row spaces in

 F_N=span{h0^j a,h0^j d:0<=j<N}, rank<=2N.

This follows inductively from(2), hA=h0+V and the rank-two factorization of V. Coefficients can therefore be represented on a bank of at most2N actual physical columns, without asserting those columns are independent or orthonormal. Ordinary physical Gram entries implement multiplication by V; projected Gram entries F_N* P F_N implement traces and products after P. Sylvester's finite-rank determinant identity gives the same determinant jets using the coefficient matrix and that projected Gram. A Gram inverse is unnecessary.

A deliberately conservative source boundary is ordinary and projected moments <f,h0^j P h0^k g> and <f,h0^(j+k)g>, f,g in{a,d}, j,k<N. This asks for powers up to2N-2. Many entries cannot contribute before orderN, and stationarity cancels single-V higher cumulants, but no reduced native supplier count is asserted here without a full degree audit. Existing c,nu,omega5 cannot simply be assumed to supply arbitrary high entries. The benefit is potentially small matrix-series arithmetic in place of a long-word Wick expansion; the missing projected scalar suppliers and width/cost certification remain real obligations.

## Infinite native-model bridge still to check

The supplied lattice one-particle h0 is bounded, despite the many-body normal-ordered H0 being unbounded; V is finite rank. Duhamel's formula makes exp(t h0)exp(-t hA)-I trace class for finite t. These facts make the right side of(1) a natural Fredholm determinant near zero, but trace-class membership alone does not identify its phase and vacuum expectation.

One sufficient route is a controlled finite-volume/Gaussian approximation with uniformly bounded one-particle operators, local perturbation convergence, strong convergence of negative-band projections to the supplied pure covariance, and convergence of each fixed local-polynomial moment. Absence of a reference zero-mode atom is relevant for the projection limit. The scalar subtraction and original CAR/impurity convention must survive that limit. Another route is a direct quasifree implementer or linked-cluster proof in the supplied GNS representation. Either route must be stated and proved before this becomes a native moment supplier. No finite-volume number is proposed as a substitute for the infinite quantity.

For any future once-only high-moment protocol, previously accepted lower native moments should be reused rather than recalculated as comparison targets. Their generating-function coefficients can supply the lower scalar series coefficients. Constructing new operator jets needed for higher coefficients must be clearly distinguished from replaying the earlier native moment evaluations. This design question is prospective and has not been implemented.

## Exact synthetic evidence

check.py uses two- and three-mode Jordan-Wigner Fock matrices, positive free frequencies and three independent rank-two perturbations. It compares every coefficient through degree7 with direct powers of the finite many-body D. All26 exact rational checks passed; the half-log factor has explicit countercontrols when the first moment is nonzero. Maximum Fock dimension8. These are deliberately synthetic operators, not native moment values and not validation of the infinite bridge or of a numerical runtime.

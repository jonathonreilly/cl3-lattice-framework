# An explicit all-coupling gap on the fixed physical SU3 cube

This separate extension follows PREREGISTRATION.md and leaves block30 frozen. Root supplied the proposed heat-time and conservative constants before the independent rational checks; no fitted threshold or optimized time is used. The domain is the full vertex-Gauss invariant subspace of L2(SU3^12), not a bare-source compression. Let H=K+V, K=-(3/(2a))Delta_tot, a>0, and V=v sum6(1-ReTr Uface/3), v>=0. In particular0<=V<=12v. The exact free physical gap16/a is the independently proved block30 input.

We prove, for every finite a>0 and v>=0,

    gap(H on Hphys) >= (16/a) 3^-24 exp(-24av) > 0.

The constants depend on the fixed twelve-link cube. This is not a volume-uniform, continuum or QCD/Yang-Mills mass-gap statement.

## 1. Uniform one-link heat bounds at time a

For SU3 irreducible labels(p,q), put m=p+q. In the trace-one generator convention, the one-link kinetic eigenvalue is E(p,q)/a, where

    E=p²+pq+q²+3p+3q,
    d(p,q)=(p+1)(q+1)(p+q+2)/2.

The Casimir expression follows from the highest-weight metric as in block30; the dimension formula is the SU3 Weyl product, with positive-root factors p+1,q+1,(p+q+2)/2. At time a the central heat density, with respect to normalized Haar, is

    p_a(g)=sum_(p,q) d(p,q) chi_(p,q)(g) exp[-E(p,q)].

The trivial term equals1. Unitarity of each representation gives |chi|<=d. We bound the entire nontrivial absolute series, including all labels.

For m1 there are exactly the two fundamental labels, each dimension3 and E4. Thus their contribution is18 exp(-4)<1/3. The strict inequality exp4>54 is certified by the rational Taylor polynomial sum_(j=0)^12 4^j/j!>54; all omitted terms are positive.

For m>=2, pq<=m²/4 implies E=m²-pq+3m>=3m²/4+3m>=4m. Also (p+1)(q+1)<=(m+2)²/4, hence d<=(m+2)^3/8. There are m+1 labels. Consequently their total is bounded by

    sum_(m>=2) f_m,  f_m=(m+1)(m+2)^6/(64*54^m).

Here f2=192/54²=16/243, and

    f_(m+1)/f_m=[(m+2)/(m+1)] [(m+3)/(m+2)]^6 /54
              <=(4/3)(5/4)^6/54 <1/10.

Both rational factors decrease with m, so this is an all-m bound. Therefore the tail is at most160/2187<0.074 and

    sum_nontrivial d² exp(-E) < 1/3+160/2187=889/2187<1/2.

The exact half-margin is409/4374. This proves absolute uniform convergence of the heat series and, at every group point,

    1/2 < p_a(g) < 3/2.

No floating exponential evaluation is used as an enclosure. The spectral series is the heat kernel because the Peter-Weyl matrix coefficients are a complete orthogonal basis and the multipliers are exactly those of exp(-aK_one); the absolute bound justifies its continuous kernel representation.

## 2. Twelve links and the positive-cone comparison

The twelve-link free heat kernel at time a is a product of twelve such densities, translated by each endpoint. Hence its pointwise kernel satisfies

    l=2^-12 <= k_free(U,V) <= u=(3/2)^12.

Averaging either endpoint over the compact vertex gauge group preserves these bounds because gauge Haar has total mass one. Thus the same constants work for the physical restriction. No quotient-volume factor is introduced.

The interacting semigroup obeys, for every nonnegative f,

    exp(-12va) exp(-aK) f <= exp(-aH) f <= exp(-aK) f.

This is positive-cone, pointwise/a.e. order, NOT Loewner order of selfadjoint operators. One proof uses the heat-path expectation with weight exp[-integral_0^a V(X_s) ds], which lies between exp(-12va) and1. Equivalently, each bounded potential multiplication in the heat/potential product formula is between those scalar factors in the positive cone; positivity of each free heat factor gives the same bounds for every finite product, and strong convergence plus closure of the L2 positive cone passes them to exp(-aH). Smooth kernels then make the inequalities pointwise. No operator-monotonicity claim for the exponential is used.

## 3. Positive gauge-singlet ground and oscillation bound

On the compact connected product group, K has compact resolvent, and bounded smooth real V preserves selfadjointness and compact resolvent. The positive lower heat comparison implies exp(-aH) is positivity improving: every nonzero nonnegative input is mapped to a strictly positive function. Its kernel is continuous and strictly positive by the lower bound above. Its top compact selfadjoint eigenvector can be chosen nonnegative: replacing a real maximizer by its absolute value cannot decrease its Rayleigh quotient. It is then strictly positive by its eigen-equation. A second independent top eigenvector could be chosen real and orthogonal to the positive one and would change sign; the strictly positive kernel would strictly increase its Rayleigh quotient under absolute value, a contradiction. The ground eigenvalue is therefore simple. Elliptic regularity with smooth V makes its normalized eigenfunction phi smooth; compactness gives min phi>0.

Every vertex gauge transformation commutes with H and preserves positivity and norm. Simplicity therefore makes the normalized positive ground phi gauge invariant. In particular the full ground belongs to the physical space and is its ground as well.

Using exp(-aH)phi=exp(-aE0)phi and the free kernel bounds gives, at every U,

    exp(-12av) l integral phi
       <= exp(-aE0) phi(U) <= u integral phi.

Taking the maximum divided by the minimum cancels both the ground energy and the positive integral. Thus

    max(phi)/min(phi) <= (u/l) exp(12av)
                      =3^12 exp(12av).

The normalized Haar measure, smoothness and positive integral are explicit; this is not an assumption that the ground is the constant vacuum.

## 4. Ground transform and physical weighted Poincare bound

Normalize integral phi²=1 and define the probability measure dmu=phi² dU. Multiplication f->phi f is unitary from L2(mu) to L2(Haar) and preserves the physical subspaces because phi is gauge invariant. For smooth physical f, integration by parts and Hphi=E0phi give the exact ground-state form identity

    <phi f,(H-E0)phi f>
       = (3/(2a)) sum_(e,A) integral phi² |D_(e,A) f|²
       =: E_mu(f).

All potential and cross terms cancel by the ground equation. This identity extends by form closure. Since phi and its reciprocal are smooth and bounded on the compact group, multiplication by either preserves the first-order Sobolev form domain. Smooth gauge-invariant functions are dense there by smoothing and compact gauge averaging, so no singular weighted-domain extension is selected.

For any such physical f, write m0=min phi and M0=max phi. The free physical Poincare inequality from gap16/a gives

    Var_mu(f)
      =inf_c integral phi²|f-c|²
      <=M0² Var_Haar(f)
      <=[M0²/(16/a)] (3/(2a)) sum integral |D f|²
      <=[M0²/(m0²(16/a))] E_mu(f).

The minimizing Haar constant need not equal the mu mean; the infimum argument handles that difference. Complex functions are covered with absolute squares. By the variational characterization on the transformed physical subspace,

    gap(Hphys) >= (16/a)(m0/M0)²
               >= (16/a)3^-24 exp(-24av).

This is an actual spectral-gap lower bound for every finite v>=0. It does not use the first-order small-v eigenvalue expansion. At v0 the bound is deliberately much weaker than the exact free gap; the block30 Ritz bound remains separately stronger in its positive interval. Taking the maximum of the two valid lower bounds is allowed but is not a new fitted constant.

## 5. Evidence and limits

The standalone exact scalar runner retains the degree12 Taylor sum, all rational tail factors and the final prefactor. Eleven checks pass; no floating expression supplies any inequality. The all-label monotonicity, positivity-improving argument, physical free-gap premise and form-domain proof are analytical and are not replaced by a finite numerical truncation. No failed scientific check occurred; candidate constants were exposed before execution as recorded.

The pointwise semigroup order must not be rephrased as Loewner order. The ground density is not guessed to be Haar; its bounded ratio is derived. All eight vertex Gauss constraints are needed for the16/a free physical gap. The constant3^-24 reflects twelve links, while exp(-24av) uses the finite six-face potential bound; these deteriorate with volume. Nothing here proves a thermodynamic or continuum mass gap, physical parameter selection or a result from minimal Record axioms alone. The supplied full compact Hamiltonian and its finite physical domain remain explicit.

# Fixed-anisotropy actual cube and iterated oscillator semigroup

This derivation follows the prospective contract in PREREGISTRATION.md. Root supplied candidate formulas before our independent calculation. The new symbolic certificate reconstructs our distinct adapted tree and all actual face incidences, rather than importing root's matrices or output. Its exact covariance and determinant agree.

## Actual geometry and covariance

Keep the two omitted source faces and all22 remaining faces. Give the ten spatial faces weight1/2 and the twelve temporal faces weight kappa>0. Tree gauge fixing leaves17 SU(3) chords. With H=B*WB and source rows S, independent exact inversion gives, writing C=S H^-1 S*,

    Cplus=C00+C01=10,
    Cminus=C00-C01=2(4kappa+5)/(4kappa²+6kappa+1),
    detH=kappa^7(kappa+1)^2(2kappa+3)(4kappa²+6kappa+1)/8.

The certificate retains the full22-by17 incidence matrix, source rows and rational C. At kappa1 it recovers [[64,46],[46,64]]/11. At kappa0 the Hessian rank drops to10, so the positive-kappa saddle theorem cannot simply include that endpoint.

For each fixed kappa>0 all action weights are positive. The same disk restoration and flatness proof gives a unique gauge-fixed minimum. H is positive because its incidence kernel is trivial; changing positive weights cannot change that kernel. Every local quadratic bound and compact-complement gap used by the structural nonlinear theorem therefore remains available, with constants allowed to depend on kappa. The action maximum factor becomes exp[(5+12kappa)beta] and cancels in the normalized D/D00 together with temporal normalization. No uniformity as kappa grows is inferred.

In trace-orthonormal Lie coordinates, the two aligned source logarithms have per-color covariance Sigma=3C. Its symmetric/antisymmetric eigenvalues are

    sigma_plus=30,
    sigma_minus=6(4kappa+5)/(4kappa²+6kappa+1).

Let r=sqrt(sigma_minus/sigma_plus), omega=1/sqrt(sigma_plus sigma_minus), and theta=(1-r)/(1+r). For every kappa>0,0<r<1 and0<theta<1. The exact limiting central operator is the independent Ad average of the corresponding sixteen-dimensional Gaussian joint density divided by the same normalized Haar constant j0. Its leading eigenvalue is lambda0(kappa)>0; no new group normalization is introduced.

## Oscillator normalization

The correlated Gaussian kernel has exponent -a(|X|²+|Y|²)+b X.Y, where

    a=(1/sigma_plus+1/sigma_minus)/4,
    b=(1/sigma_minus-1/sigma_plus)/2.

Thus sqrt(4a²-b²)=omega and b/(2a+omega)=theta. The unitary oscillator-coordinate change from X to w=sqrt(omega)X is

    (D_omega f)(w)=omega^-2 f(w/sqrt(omega)).

After this change the Gaussian ground function is proportional to exp(-|w|²/2). The exact normalized Gaussian operator, restricted to Ad-invariant L2(R8), is

    D_omega K_kappa D_omega* / lambda0(kappa) = exp(-t_kappa N),
    t_kappa=-log(theta)=2 artanh(r),
    N=(-Delta_w+|w|²-8)/2.

This identity follows from the full Hermite decomposition and its commuting compact-group projection. The invariant degrees are2a+3b, not only even degrees. The operator identity includes every invariant degree and is stronger than identifying a single eigenvalue ratio. It remains an identity of the limiting Gaussian, whose connection to the actual supplied cube is the fixed-kappa nonlinear theorem.

## Controlled order of limits for actual powers

For each fixed integer n and kappa>0, let A_beta,kappa=D_beta,kappa/D00. One convenient finite-beta normalization is A_beta,kappa/||A_beta,kappa||, a positive contraction. The structural theorem implies that its chart compression, transformed first by the local Haar unitary and then D_omega, converges in operator norm to exp(-t_kappa N). Indeed beta^-4||A_beta,kappa|| tends to lambda0(kappa)>0. Using the leading normalization beta^-4/lambda0(kappa) instead gives the same fixed-kappa limit.

For fixed n, norm continuity of multiplication gives convergence of the n-th powers. This also represents the normalized ACTUAL group-operator n-th power, rather than an uncontrolled repeated chart projection. To see this, set P to the fixed source chart. The established exponentially small ||A-PAP||, after normalization, and the identity

    B^n-C^n=sum_{j=0}^{n-1} B^(n-1-j)(B-C)C^j

bound the difference between the true power and (PAP)^n for fixed n. The local unitary has U*U=P, so conjugating (PAP)^n gives exactly the power of the conjugated compression. Constants may depend on n and kappa.

Fix a mathematical t>0 and set kappa_n=4n²/(5t²). Since

    r_kappa~1/sqrt(5kappa),
    t_kappa=2 artanh(r_kappa)~2/sqrt(5kappa),

we have n t_kappa_n ->t. Therefore

    lim_(n->infinity) lim_(beta->infinity)
      [oscillator-dilated actual normalized n-step operator at kappa_n]
        = exp(-t N)

in operator norm on the common Ad-invariant oscillator Hilbert space. The inner limit is taken separately for EACH fixed n. For the outer norm convergence, if a_n=n t_kappa_n, then

    sup_(m>=0)|exp(-a_n m)-exp(-t m)|
      <= |a_n-t|/[e min(a_n,t)] ->0.

Restricting to invariant Hermite degrees preserves this bound. No simultaneous beta_n/kappa_n estimate, selected physical time, growing-volume limit or rate uniform in anisotropy has been proved. The oscillator dilation itself depends on kappa and must not be omitted when comparing these operators.

## Ground-transformed central Ornstein-Uhlenbeck generator

Let h(w) be the normalized oscillator ground state proportional to exp(-|w|²/2). Ground conjugation gives the Markov semigroup on invariant L2(h²dw) with generator

    L= -h^-1 N h = (1/2)Delta_w-w.grad_w.

Put q=Tr W²=|w|² and c=Tr W³. Independent trace-orthonormal SU(3) differentiation yields

    |grad q|²=4q, Delta q=16,
    grad q.grad c=6c, Delta c=0,
    |grad c|²=9[Tr W4-q²/3]=(3/2)q².

The last equality uses the traceless3-by3 identity Tr W4=q²/2. Hence on smooth invariant polynomials/functions in the interior,

    L=2q partial_qq+6c partial_qc+(3q²/4)partial_cc
       +(8-2q)partial_q-3c partial_c.

The orbit domain is q>=0,c²<=q³/6. For eigenvalues x,y,-x-y,

    q³/6-c²=(1/3)(x-y)²(2x+y)²(x+2y)².

The finite certificate verifies these derivative identities with explicit eight generators at an arbitrary diagonal matrix; conjugation invariance extends them to all Hermitian traceless matrices. This is the restriction of the known eight-dimensional OU process, not a newly chosen boundary diffusion. Its semigroup fixes the boundary behavior through the original invariant process; no arbitrary boundary condition is supplied on the discriminant cusp. Smooth invariant polynomials provide the natural algebraic core, and the full semigroup is inherited from the Gaussian ground transform.

## Scope

The new model-specific content is the exact actual-slab anisotropic covariance and the controlled iterated continuation of its dilated central operators. The Hermite/OU machinery itself is standard. A supplied tunable anisotropic Wilson action and a mathematical oscillator time parameter remain inputs. Nothing selects a physical coupling, lapse, formation clock or continuum spacetime dynamics.

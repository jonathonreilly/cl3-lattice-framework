# Actual free-Haar contact scaling, a sharpness supplement

This proof was written after the exposed disjoint-plaquette candidate and before reading primary's independent completed proof. It is a statistical scaling construction in the supplied u=0 compact ground state. It does not derive a propagating quantum field, a physical noise source, a clock or a spatial interpretation from the axioms.

## Actual independent variables

At u=av=0 with a>0, the ground state of the full infinite link model is product Haar. For k in Z3 choose the elementary xy plaquette whose anchor is3k. Distinct selected plaquettes have disjoint link sets, so their holonomies are independent and each is Haar-distributed in SU3. Assign a fine spatial mesh ell=h/3; the selected anchors then have physical positionshk.

Let chi=Tr(U) and X=sqrt18 ReTr(U)/3=(chi+bar chi)/sqrt2. Fundamental Haar orthogonality gives Echi=0, Echi²=0 and Echi bar chi=1, hence EX=0 and EX²=1. Also |X|<=3sqrt2=:M. All selected X_k therefore are identically distributed independent real bounded variables. The independence is exact and comes from actual disjoint links, not an assumed independence of adjacent plaquettes sharing links.

There is an exact non-Gaussian single-cell diagnostic. The SU3 invariant alternating tensor gives Echi³=Ebar chi³=1, and mixed cubic moments vanish by center charge. Thus EX³=1/sqrt2. Likewise3 tensor3=6 plus bar3 gives E|chi|^4=2, while the remaining fourth-order monomials vanish by center charge; consequently EX4=3. Only the first two moments and boundedness are required for the limit below. The determinant/tensor-product identities are analytical Haar inputs, not conclusions inferred from finite arithmetic checks.

## Smeared fields and covariance

For real continuous compactly supported f on R3 define the finite sum

 Phi_h(f)=h^(3/2) sum_(k in Z3) f(hk)X_k.

It has mean0 and covariance

 E[Phi_h(f)Phi_h(g)]=h³ sum_k f(hk)g(hk) -> integral_R3 f(x)g(x) dx,

by the Riemann-sum theorem. The sums are finite for everyh. In particular disjoint-support test functions have covariance exactly0 at every mesh, while a nonzero f has a positive limiting variance. The operator norm is bounded by M h^(3/2)sum|f(hk)|=O(h^(-3/2)), a polynomial budget consistent with block40's assumptions. This construction is therefore not an exception to its separated-correlation conclusion.

## Direct characteristic-function proof

Let q be any fixed real continuous compactly supported function, including a real linear combination sum_j t_j f_j. Put b_k=h^(3/2)q(hk). For the one-site characteristic function phi(b)=E exp(i bX), Taylor's theorem with a bounded third moment gives

 phi(b)=1-b²/2+r(b), |r(b)|<=M³|b|³/6.

For sufficiently smallh every |b_k| is small uniformly. Using the analytic logarithm near1 and |log(1+z)-z|<=2|z|² for |z|<=1/2, one obtains a constantC_M such that

 log phi(b_k)=-b_k²/2+O(C_M|b_k|³).

There are O(h^(-3)) nonzero summands and q is bounded, so sum|b_k|³=O(h^(3/2)). Exact independence then gives

 log E exp(i Phi_h(q))
 =sum_k log phi(b_k)
 =-(h³/2)sum_k q(hk)²+O(h^(3/2))
 ->-(1/2) integral q(x)² dx.

Exponentiation proves convergence of every joint characteristic function of (Phi_h(f1),...,Phi_h(fn)) to the centered Gaussian characteristic function with covariance matrix integral fi fj. Thus the finite-dimensional distributions converge to Gaussian white-noise statistics. This is a finite-dimensional distribution statement; no topology of random distributions or dynamical field convergence is asserted.

Keeping the exact third moment gives the optional finite-mesh diagnostic

 sum_k log phi(b_k)=-(1/2)sum_k b_k² - i/(6sqrt2) sum_k b_k³ + O(sum_k|b_k|4).

The remainder is O(h³) for fixedq, while the cubic term is O(h^(3/2)); the mesh covariance is retained exactly rather than replacing its Riemann-sum error by an unjustified rate for arbitrary continuousq. This correction is analytical and not fitted from samples.

## Why this sharpens the continuum boundary

The limit has nonzero smeared variance and contact covariance, with no connected covariance between separated supports. It demonstrates that block40 cannot honestly be read as excluding all nonzero continuum statistical data. What its clustering argument excludes is nonzero separated connected correlations for the stated fixed-neighborhood/polynomial-budget construction in a uniformly controlled weak regime.

The present example uses u0, disjoint plaquettes, an explicitly chosen shrinking spatial mesh and a supplied field normalization. It does not give a relativistic vacuum, spatial propagation, temporal correlations, interacting white noise at u>0, a continuum gauge action or any physical stochastic interpretation. Those remain separate scientific questions.

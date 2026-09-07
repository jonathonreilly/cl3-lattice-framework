# Exact Haar contact-limit sharpness example

**Type:** bounded_theorem, conditional on the supplied u=0 compact-link product Haar ground, spatial mesh and field normalization. Root exposed the candidate before the prospective contract. This proof froze before reading native40. No generic central limit theorem is imported.

At u=0 the neutral ground of the electric Hamiltonian is the product constant, so link variables under its expectation are independent normalized SU(3) Haar variables. For each k in Z3 take the positively oriented xy elementary plaquette based at fine-lattice vertex3k. Its four link variables are disjoint from those of every other chosen plaquette: projected unit-square coordinate intervals at distinct multiples of3 do not overlap in an edge, and different z layers also have distinct links. Its holonomy U_k is Haar, because a product of independent Haar matrices and their inverses is Haar. The holonomies are independent as functions of disjoint independent link sets.

Put J_k=ReTr(U_k)/3 and X_k=sqrt18 J_k. The fundamental Haar character chi satisfies integral chi=0, integral chi^2=0 and integral |chi|^2=1. The first follows from nontriviality, the second also follows from multiplication by the SU3 center, and the last is Schur orthogonality. Thus E J=0 and E J^2=(0+2+0)/36=1/18. Consequently E X=0, E X^2=1 and |X|<=B=sqrt18. These are actual plaquette multiplication observables in the electric ground, not abstract independent spins substituted for the model.

Give fine links mesh ell=h/3. The chosen plaquette anchors then have physical positions hk. For real f in C_c(R3), define the finite random variable

 Phi_h(f)=h^(3/2) sum_(k in Z3) f(hk) X_k.

Only finitely many terms are nonzero. They commute as multiplication observables. For any finite family f_1,...,f_m and real t_1,...,t_m set g=sum_j t_j f_j. The joint characteristic function equals the characteristic function of Phi_h(g).

## Explicit Taylor-product proof

Write phi(z)=E exp(i z X), z real. Taylor's integral remainder gives

 |phi(z)-1+z^2/2| <= B |z|^3/6,

because E|X|^3<=B E X^2=B. If |z|<=1/(2B), put w=phi(z)-1. Then |w|<=z^2(1/2+1/12)<=z^2<=1/72. The power-series logarithm about1 is therefore defined, with

 |log(1+w)-w| <= |w|^2/[2(1-|w|)] <= |w|^2 <= z^4.

It follows that

 |log phi(z)+z^2/2| <= (B/6+1/(2B))|z|^3 = (7B/36)|z|^3 <= (B/4)|z|^3.

For sufficiently small h, every z_k=h^(3/2)g(hk) satisfies the threshold. Independence gives an exact product, so summing these small-argument logarithms gives a logarithm of the product and

 |sum_k log phi(z_k) + (h^3/2)sum_k g(hk)^2|
 <= (B/4) h^(9/2) sum_k |g(hk)|^3 = O_g(h^(3/2)).

The last estimate uses a fixed compact box containing supp g: its number of mesh points is at most C_g h^-3 for0<h<=1, while ||g||_infinity is finite. The Riemann sum h^3 sum g(hk)^2 tends to integral g^2. Exponentiation therefore yields the joint limiting characteristic function

 exp[-(1/2) integral_(R3) (sum_j t_j f_j(x))^2 dx].

This is the finite-dimensional centered Gaussian white-noise characteristic functional. A degenerate covariance matrix is allowed if the test functions are linearly dependent. In particular

 Cov(Phi_h(f),Phi_h(g))=h^3 sum_k f(hk)g(hk) -> integral f g.

For disjoint test-function supports the finite covariance is already zero. This gives a nonzero contact/statistical limit while every separated-support connected covariance vanishes.

The O(h^(3/2)) bound is for the logarithmic product error relative to its discrete quadratic form. For arbitrary continuous compactly supported f no O(h^(3/2)) rate is asserted for the Riemann-sum-to-integral error. Only convergence of that latter error is needed. This distinction prevents a false quantitative CLT rate from being attached to arbitrary continuous test functions.

## Scope

The construction is at exactly u=0 with supplied ell=h/3, disjoint plaquette sampling and central-limit normalization. It is a rigorous finite-dimensional distribution limit, not a claim of convergence in a chosen random-distribution topology, a dynamical field, a propagating QFT, physical stochastic noise, or an interacting continuum limit. The Gaussian characteristic function does not supply a time evolution. It demonstrates why a separated-correlation obstruction must retain its contact-term exclusion.

Disjoint links are a sufficient independence criterion. Distinct plaquettes alone do not justify applying that criterion; no converse dependence assertion about all overlapping plaquettes is made. Repeating the identical plaquette is an explicit adverse case: the two resulting X variables have covariance1 rather than0.

# Gaussian inverse approximation: useful bound and remaining node-extraction gap

This is a new bounded analytic attempt, not an input to a numerical pilot.
For x>=delta>0 define f_T(x)=(1-exp(-T*x*x))/x. Spectral calculus gives
||D^(-1)-f_T(D)|| <= exp(-T*delta^2)/delta for every D>=delta.
For the two actual positive impurity generators D_C,D_A and ||gamma_v||=1,

||D_C^(-1) gamma_v D_A^(-1)-f_T(D_C) gamma_v f_T(D_A)||
 <= 2 exp(-T*delta^2)/delta^2.

Thus the complete 90-term vacuum transition has norm error at most
(90/4) exp(-T*delta^2)/delta^2. This statement uses the original proved delta;
the proposed sharper infinite gap is not required.

The real-time transform of f_T has Gaussian complementary-error-function
tails. This suggests combining finite-range Lieb-Robinson propagation with
T proportional to box radius. However, the state-norm approximation alone
DOES NOT certify the node scalar. A normalized finite Bloch annihilator
extracts a local-source Fourier amplitude after multiplication by the square
root of cell volume. Its state-norm error bound consequently grows with this
factor. Nor can state norm control an arbitrary unprojected coefficient
symbol: null creation coefficients exist away from the node.

A useful next lemma must control the zero-momentum soft-annihilator
commutator of the inverse approximation uniformly in volume. The exact
resolvent proof supplies such control for the inverse itself; applying it to
f_T requires a bounded divided-difference/commutator estimate with the local
[annihilator,B_A] insertion. Merely citing the scalar derivative bound is
insufficient for a noncommuting double-operator integral. Alternatively one
needs an explicit finite-volume covariance approximation rate and a joint
choice of box radius and T. Neither estimate is claimed here.

Accordingly this Gaussian approximation cannot yet justify a practical
finite-box node calculation. It is a precise candidate improvement and an
identified obstruction to promoting vacuum-norm accuracy into a node-value
certificate. No physical computation was performed.

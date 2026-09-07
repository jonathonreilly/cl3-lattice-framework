# A local energy-form bridge for the actual finite-PW charged trial

2026-09-07 21:43UTC. Root prospective candidate was exposed to native before independent completed writeups. Native has reported checking the key commutator and full-ground premise; root has not read native's completed derivation. This proof addresses the unbounded-energy gap left explicitly open by41, within the supplied compact Hamiltonian.

## 1. Model, ground-state premise and local energy budget

Let G be a finite cubic link graph with a subset of its elementary plaquettes. Every link belongs to at most4 retained faces. On the full tensor product of actual complete-irrep PW link cutoffs p+q<=R, R>=1, define

 H_R=K_R+sum_f P V_f P, K=sum_e K_e,
 K_e=-3 Delta_e/(2a), V_f=v(1-ReTr(U_f)/3), a>0,v>=0.

Here P is the product cutoff. All V_f are bounded scalar multiplication operators with 0<=V_f<=2v before and after compression. No projection to boundary singlets is included in the carrier definition.

Let Omega_R be a normalized gauge-invariant eigenvector at the lowest energy E0_R of this FULL tensor-carrier Hamiltonian. In particular the existing uniform weak-window theorem34 supplies a unique such full ground, and its exact gauge covariance plus absence of nontrivial one-dimensional SU3 characters makes it physical. One must not replace this full-carrier premise by an arbitrary minimum solely over the gauge-singlet sector: the replacement trial below need not be gauge invariant. Outside the proven weak window, existence of the required full ground with the stipulated gauge transformation remains an explicit premise.

Write rho=|Omega_R><Omega_R|. Replace one link e by its normalized Haar vacuum while retaining the reduced density on every other link: sigma_e=|1_e><1_e| tensor Tr_e rho. This is an admissible mixed trial in the full cutoff tensor carrier. Every kinetic term other than K_e and every face not containing e has exactly unchanged expectation. The new K_e expectation is0. For an incident face the new potential expectation is at most2v while the old is nonnegative. The variational principle for mixed trials therefore gives

 E_e:=<Omega_R,K_e Omega_R><=2v n_e<=8v.       (1)

This estimate is independent of R and ambient volume; its use of an unrestricted mixed trial is essential. For a d-link path define E_path=sum_path E_e<=8vd. For a face define E_f=sum_(e in f)E_e<=32v. Boundary omissions only decrease these bounds.

## 2. Actual charged trial and its normalization

Take any oriented simple path of d distinct links from x to y. Let W be its full unitary3-by3 transporter matrix, and C=P W P its compression, acting entrywise. Since all individual link cutoffs commute with other-link matrices, C equals the product of compressed distinct-link transporters. Work with matrix-valued functions in Hilbert–Schmidt norm divided by3, so ||W Omega_R||=1. Equivalently this is the9-component static-source vector with entries W_ab Omega_R/sqrt3. Gauge invariance of Omega_R and covariance of P and W put both W Omega_R and C Omega_R in the correct fundamental/antifundamental source sector.

The exact top-shell threshold is e_R=[ceil(3R^2/4)+3R]/a. Let

 theta=E_path/e_R, q=||C Omega_R||^2.

Block41's actual fusion/projector estimate gives 1-q<=theta. Suppose theta<1, so q>0 and the normalized charged trial exists. The stronger actual q may be used; replacing it by1-theta is only a sufficient estimate. The upper bound here concerns the charged sector of the same finite-cutoff Hamiltonian, relative to its own neutral ground E0_R.

Because H_R Omega_R=E0_R Omega_R entrywise, its unnormalized excess-energy numerator is exactly

 N=<C Omega_R,(H_R-E0_R)C Omega_R>
   =<C Omega_R,[H_R,C]Omega_R>.                (2)

This subtracts the vacuum energy BEFORE estimating and avoids an ambient-volume E0_R normalization error. N>=0 since E0_R is the full tensor-carrier minimum. The normalized trial has excess N/q.

## 3. Kinetic commutator in an actual Sobolev norm

Let D_eA be invariant first derivatives with the generator normalization Tr(T_A T_B)=2 delta_AB and sum_A T_A^2=(8/3)I. Then sum_(e,A)||D_eA Omega_R||^2=(2a/3)E_path when the sum is restricted to path links. Each derivative of W on a path link is a product of unitary prefix and suffix matrices with one generator insertion. Consequently the operator row formed by these insertions satisfies

 sum_(e,A)(D_eA W)(D_eA W)^*=(8d/3)I.

The product rule for K gives a zeroth-order term (4d/a)W and a first-derivative term with coefficient3/a. The row-operator Cauchy–Schwarz estimate therefore proves

 ||[K,W]Omega_R||
 <=4d/a+(3/a)sqrt(8d/3)sqrt((2a/3)E_path)
 =4d/a+4sqrt(d E_path/a)=:B_K.                (3)

The result is a form/derivative calculation, not an inference from vector-norm convergence. PW ground states on the finite graph are finite sums of smooth matrix coefficients, so all derivatives and products used here lie in the relevant operator domains without a limiting-domain argument.

In the same matrix Hilbert–Schmidt inner product, the exact SU3 trace identity gives

 <W Omega_R,[K,W]Omega_R>=4d/a.               (4)

Indeed W is pointwise unitary, the potential is scalar, and Tr(W^* D_eA W)=0 because the inserted generator is traceless. Every cross term containing a derivative of Omega_R vanishes after color trace, with no reality assumption on Omega_R. This is the full-unitary trial identity already used in38, now combined with an independent derivative-norm estimate.

Since K commutes with P, [K_R,C]Omega_R=P[K,W]Omega_R. Put Q=I-P. Equations(3)–(4) then imply

 |<C Omega_R,[K_R,C]Omega_R>-4d/a|
 =|<Q W Omega_R,Q[K,W]Omega_R>|
 <=sqrt(theta) B_K.                           (5)

The discarded vector is paired with an explicitly bounded derivative vector. This is the missing energy-form control that norm closeness alone did not provide.

## 4. Only touching face commutators contribute

A compressed face operator whose link set is disjoint from the path commutes with C EXACTLY: their link tensor supports are disjoint and the face operator is a scalar on the source color. Thus only N_touch<=4d faces occur in the potential part of(2).

For any such face, full multiplication satisfies [V_f,W]=0, so the exact compression identity is

 [P V_f P,P W P]=P W Q V_f P-P V_f Q W P.     (6)

Multiplication by a face fundamental or antifundamental character changes each face link label by a single fundamental fusion step. Therefore Q V_f P annihilates the subspace in which all four face links have p+q<=R-1. If B_f is the union projector onto their top shells, then Q V_f P=Q V_f P B_f. The commuting shell union bound and the shell kinetic lower bound give

 ||Q V_f Omega_R||<=2v ||B_f Omega_R||
 <=2v sqrt(E_f/e_R).

Using ||Q W Omega_R||<=sqrt(theta), equation(6) yields

 ||[P V_f P,C]Omega_R||
 <=2v(sqrt(E_f/e_R)+sqrt(theta)).             (7)

In(2) the left vector has norm sqrt(q)<=1, so the absolute potential contribution is no greater than the sum of these bounds. There is no sum over distant faces, no volume-sized potential norm, and no hidden factor of the9 source components: the single normalized Hilbert–Schmidt norm already includes them.

## 5. Result and uniformity statement

Let E_xy,R be the infimum of H_R in the source sector. Combining the charged trial with(2),(5),(7) gives the explicit bound

 0<=E_xy,R-E0_R
 <=[4d/a+sqrt(theta)(4d/a+4sqrt(d E_path/a))
       +sum_(f touches path)2v(sqrt(E_f/e_R)+sqrt(theta))]/(1-theta),  (8)

provided theta=E_path/e_R<1. In particular set theta_bar=8vd/e_R. When theta_bar<1, a fully geometry-independent sufficient bound is

 E_xy,R-E0_R
 <=[4d/a+sqrt(theta_bar)(4d/a+4d sqrt(8v/a))
       +8vd(sqrt(32v/e_R)+sqrt(theta_bar))]/(1-theta_bar).           (9)

For fixed a,v,d, the right side tends to4d/a as R tends to infinity, uniformly over every ambient cubic graph satisfying the full-ground premise. The error is O_(a,v,d)(R^-1); the displayed bound, rather than an unspecified asymptotic constant, is available. It is not uniform in arbitrary d at fixed R: the sufficient normalization budget itself requires e_R>8vd. At v=0, theta_bar=0, the actual vacuum trial lies exactly inside R>=1, and the bound is exactly4d/a for every cutoff.

This repairs a specific model-to-cutoff energy argument. It does not implement C as a deterministic unitary circuit, select R or a physical coupling from the axioms, identify a continuum static potential, establish convergence of infinite-volume charged minima, or remove the weak-window/full-ground premise. A separate sector-resolvent theorem would be needed to claim a new uniform finite-cutoff lower confinement bound; none is silently inferred here.

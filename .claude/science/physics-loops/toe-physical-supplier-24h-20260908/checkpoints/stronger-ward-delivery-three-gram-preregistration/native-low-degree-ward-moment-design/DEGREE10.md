# A concrete degree-(1,0) native Ward gate using only mu and nu

UNREVIEWED source-only successor. Set h=1 throughout; alpha and all Ward bounds scale by h^-2. No native scalar values were read or substituted. c=mu/3 is the reference normal-order constant, not the impurity ground energy. The input nu is the center third absolute one-particle moment. The actual gap remains delta=1/4.

## Local algebra and signs

Write a=e0, d=d_A, k=K0 a=d_all, v=K0 d, g=gamma(a), B=i g gamma(d), J=2i gamma(d). Thus ||d||²=2, a^T K0 d=-2, ||k||²=6, and d·k=2. These conventions agree with the reviewed exact-third-moment source. In particular

 D J Omega=gamma(-2v-4a)Omega,   D g Omega=i gamma(k-d)Omega.       (1)

The first uses [H0,J]=-2gamma(v), BJ=-4g; the second uses Bg=-i gamma(d). Both are linear vectors, despite the interacting D. Do not extend(1) to arbitrary linear vectors: a general B gamma(f) contains a cubic term.

Let e_d=<d,|h0|d>. The native local measures supply e_P=2mu=6c and e_O=nu/3, ||K0 d_P||²=12, ||K0 d_O||²=14. Cubic covariance gives a^T K0 |h0|d=-nu/3 for every two-edge pair. This last equality follows by summing the six symmetry-equivalent signed center edges, not by assigning equal arbitrary off-center correlations.

For kappa(x,y)=<gamma(x)gamma(y)>/i when x·y=0, the native reference has kappa=K0/|h0|. Hence kappa(a,d)=-c, kappa(a,k)=-mu, kappa(d,v)=-e_d, kappa(v,k)=nu/3. This explicitly fixes the phase convention used by the source engine.

The J/g source Gram matrices are

 M0=[[8,2c],[2c,1]],
 M1=[[16c,0],[0,2c]] (P), or [[4nu/3-8c,0],[0,2c]] (O),
 M2=[[32,2nu/3-20c],[2nu/3-20c,4]] (P),
 M2=[[40,-8c],[-8c,4]] (O).                                    (2)

They mean Mj_ab=<source_a,D^j source_b>, with ordered sources(J Omega,g Omega). The off-diagonal M2 sign follows directly from -kappa(-2v-4a,k-d). No impurity vacuum or independent covariance approximation enters these exact identities.

## Fourth vacuum moment

D²Omega=[H0,B]Omega+2Omega. Put u=K0 a. The commutator is -gamma(u)gamma(d)-gamma(a)gamma(v), and its expectation vanishes. Wick expansion gives

 ||[H0,B]Omega||²=||u||²||d||²+||v||²-2(u·d)²
                 +2mu e_d+2c a^T K0 |h0|d.

Consequently the vacuum moments m0..m4 are

 (1,c,2,10c,20+36c²-2c nu/3) for P,
 (1,c,2,4c+nu/3,22+4c nu/3) for O.                             (3)

The covariance term has a plus sign before a^T K0 |h0|d, whose native value is negative. An isolated occupied quadratic bond makes the entire commutator energy zero; the opposite sign fails that check.

## Fixed finite candidate and exact gate

Choose p(x)=p0+p1 x. Two predetermined choices are allowed:

 * residual optimum: [[m2,m3],[m3,m4]] p=[m1,m2];
 * inverse-variational candidate: [[m1,m2],[m2,m3]] p=[m0,m1].

A certified nonsingular solve is required; an interval or singular failure is INDETERMINATE, not a pseudoinverse silently substituted. Any selected rational p is valid after its actual residual is enclosed, so coefficient closeness to an exact optimizer is NOT a theorem premise.

The inner source is b=J p(D)Omega=p0 J Omega+4p1 g Omega. Let beta=(p0,4p1), sj=beta^T Mj beta, and choose q=s1/s2 when s2>0. Again any rational q with certified residual is admissible. Then

 r²=1-2(p0 m1+p1 m2)+p0²m2+2p0p1m3+p1²m4,
 t²=s0-2q s1+q²s2.                                            (4)

All these quantities use ONLY c and nu. Existing accepted c and nu enclosures must be bound to their actual source and propagated; midpoint substitution without a residual error enclosure is not a certificate.

For disjoint C,A, <BC BA>=0: the product is gamma(d_C)gamma(d_A), whose dot product and same-sublattice covariance vanish. The nominal ordered Ward contribution is therefore

 p0C p0A+c(p0C p1A+p1C p0A)
 +qA[2c p0C p0A+4p0C p1A+4c p1C p1A].                        (5)

Sum(5) over all90 ordered disjoint pairs, with the actual3 opposite/12 perpendicular classes. This is W_hat for the ORIGINAL boundaries. Define E²=16 sum_A r_A² and F²=sum_A[4(2sqrt2*4sqrt(r_A²)+sqrt(t_A²))]². Outward roots give a rigorous error via e858(3):

 Error=6[E(2sqrt15/delta+E)+E*(2sqrt2 sqrt15/delta²)
           +(sqrt15/delta+E)F].                               (6)

W_hat_lower>Error_upper proves alpha>0. Negative upper<-Error proves alpha<0. Otherwise this gate is indeterminate; it does not refute alpha or exhaust higher polynomial degrees. The source-only core provides formulas but no interval binder/driver is activated.

## Degree-zero obstruction, not a no-go for degree one

The residual-optimal constant p=c/2 has r²=1-c²/2>=4799/7200 from c<=49/60. The optimal constant q for J Omega is M1_J/M2_J; both native classes obey0<q<=49/120 using3/4<c<=49/60 and nu<16. Thus the degree-zero nominal is<26, while the term6E² alone in(6) is>959. This PARTICULAR fixed gate cannot decide the sign for any admissible native c,nu. This obstruction does not apply to exact alpha, the direct Q bound, other error estimators, or the degree-one candidate.

## Cost and next scientific boundary

The degree-(1,0) formulas need at most two2x2 rational solves per class and90 scalar contributions for each of two fixed choices. They need no new oracle, local covariance matrix, old Gram computation, or full Gaussian determinant. A prospective accepted-scalar evaluation would be a NEW small certificate protocol, not an authorized action in this preparation. A strict interval implementation, independent review, actual input binder and resource contract must precede it. No runtime forecast is claimed from source operation count.

For degree>=1 on BOTH inverse layers, the supplied generic Clifford/Wick engine exposes additional covariance entries rather than pretending mu/nu suffice. Max support radius for p degree d and q degree e residual is d+e+2 about the star center; loose maximum word length after taking a squared norm is4(d+e)+6. With d=e=1, radius4 has129 sites; bipartite symmetry leaves at most85*44=3740 real cross-sublattice covariance suppliers. For d=e=3, radius8 has833 sites and at most489*344=168216 such entries. These are safe acquisition upper bounds, not minimal counts after exact algebra cancellations.

The engine cap is262144 retained terms,2000000 Clifford products and65536 Wick states,16384-bit rational components. A cap failure is useful source-cost feedback, not rank or moment exhaustion. No full native geometry execution/profile has been performed. Rational covariance inputs to this engine are only exact synthetic fixtures: future physical intervals need a separate outward adapter. For a2r-word, the elementary perturbation bound r(2r-1)!! eta applies when each true and chosen covariance entry lies in[-1,1] and differs by at most eta; multiplying by the literal coefficient l1 sum gives a safe but potentially poor expectation error. No useful precision is assumed without that ledger.

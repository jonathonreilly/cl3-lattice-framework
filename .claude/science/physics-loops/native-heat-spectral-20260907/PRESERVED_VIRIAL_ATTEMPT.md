# Domain-safe dilation identity and unresolved Perron sign

The analytic attempt produces a rigorous first-moment identity and constraints, but does not determine the sign of d0. No numerical or Gaussian trial vector is substituted for the Perron vector.

Let phi be the normalized positive top eigenvector of T=S M_W S, mu its eigenvalue, and psi=Sphi. Define the probability measure

    dnu(x)=W(x)|psi(x)|² dx / mu,
    kappa=-<phi,Lphi>.

All Q moments used below are finite because Q^j W is bounded and psi is L². The heat smoothing in phi=mu^-1 S(Wpsi) gives phi in Dom(L): L S is bounded by spectral calculus. Thus kappa is well-defined. The Dirichlet form is positive definite on nonzero L² functions, so kappa>0.

## Dilation without an unbounded-generator assumption

For a>0 define the unitary cone dilation (U_a u)(x)=a u(ax). The Dirichlet form and cone domain scale exactly, giving U_a* L U_a=a²L. Multiplication transforms as U_a* M_W U_a=M_(W(x/a)). Hence

    T(a)=U_a* T U_a
        =exp(a²L/2) M_(W(x/a)) exp(a²L/2).

The family is differentiable in OPERATOR NORM near a=1. Indeed the heat times stay away from zero, so L exp(tL) is uniformly bounded; the differentiated multiplier is a bounded polynomial times a Gaussian, uniformly in a on a compact interval. No assertion that phi lies in the domain of the dilation generator is needed.

Use r=log a. At r=0, derivative of a heat factor is L S and derivative of W(x/a) is(2Q-3)W. Since T(a) has the same top eigenvalue mu for every a and <phi,T(a)phi><=mu with equality at a=1, its scalar derivative vanishes. The eigenvector equation, not a formal commutator with an unbounded dilation generator, then gives

    0=2mu<phi,Lphi>+<psi,(2Q-3)Wpsi>.

Therefore

    E_nu Q = 3/2+kappa >3/2.                       (1)

This is a rigorous virial identity for the actual ground equation.

## Exact constraints on the insertion

Because f=Q(Q-7)W/4,

    d0/mu = [E_nu Q²-7 E_nu Q]/4
           = [Var_nu(Q)+(kappa+3/2)(kappa-11/2)]/4. (2)

Equivalently,

    d0/mu = E_nu[(Q-7/2)²]/4 -49/16 > -49/16.

Strictness follows because nu has a positive interior density and Q cannot be constant on its support. If kappa>=11/2, then(2) implies d0>0. A negative sign would require kappa<11/2 AND the quantitative variance bound

    Var_nu(Q)<(kappa+3/2)(11/2-kappa).

Neither such a kappa bound nor the requisite variance estimate has been established here. The first-moment identity alone permits either sign. Indefiniteness of the insertion D does not select the sign on its unrelated positive Perron vector.

## Failed routes preserved

1. A second derivative of the same Rayleigh inequality is nonpositive, but its expression contains mixed weighted Lpsi terms and ||Lphi||². These have no established sign or closure in the two moments above. Dropping them would be unjustified. I do not promote the second derivative into a moment inequality.

2. A tempting sufficient condition is radial nonincrease of psi/H on each ray. In polar coordinates for Q, the weight H|psi|² would then have a degree9 homogeneous factor times e^-Q and a nonincreasing radial modifier. The resulting gamma comparison would give E Q²/E Q<=13/2<7, hence d0<0. The needed monotonicity has NOT been proved from the ground equation. It is a missing lemma, not an observed property or a usable sign proof.

3. Positivity, exchange symmetry and log-concavity alone cannot supply that monotonicity. The explicit positive chamber functions psi=H exp[-aQ+b(x+y)], a,b>0, are symmetric and log-concave (logH is a sum of logs of positive linear forms), yet psi/H increases near the origin on every positive ray. With large b their weighted mass is concentrated at large Q. These are not claimed to solve the ground equation; they show why replacing that equation by generic positivity/log-concavity loses the needed information.

4. A Gaussian/Hermite ansatz for the Perron vector has no established invariance under this cone heat/multiplier composition. No trial function has been called the ground state and no trial d0 sign is reported as evidence.

The native agent's independent positive-kernel approach may provide additional structure. This memo's conclusion is limited to(1)–(2), the strict lower bound, conditional sign criteria and the explicit unresolved second-moment obligation. It does not establish d0's sign or an excited-state/physical-gap consequence.

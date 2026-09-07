# Cold review of fixed-concentration profile stiffness

Verdict: mathematical PASS at the stated conditional scope. I independently checked the minimizer argument, obstacle sign and boundary regularity, equality classification, and integral constants. No runner rerun or source edit was needed. The fifteen symbolic checks substantiate the integral algebra, not the global variational proof.

## Constraint manifold and obstacle inequality

Minimizing in H1 first is legitimate: fixed mass and L2 norm plus bounded derivative energy give an H1 bound; on a one-dimensional compact circle this gives strong C0/L2 subsequential compactness, preserving nonnegativity and both constraints. The displayed profiles ensure nonempty feasible sets for all r>=1.

For any nonconstant minimizer there are two smooth test functions supported in its positive set whose mass and p-weighted integrals are linearly independent. Otherwise p would be constant on every positive component with the same constant, which continuity across a zero boundary excludes; if no zero boundary exists, that would force r=1. This establishes the rank condition needed for equality-constraint multipliers. For an exterior nonnegative perturbation h, the implicit-function theorem supplies two interior corrections enforcing BOTH constraints exactly, including their quadratic L2 change. Their supports lie where p is bounded away from zero, so they preserve positivity for small perturbation size. The first variation is therefore

    < -p''-lambda p-mu, h> >=0.

The sign in the source is correct. The residual vanishes in the positive set. This is an obstacle variational inequality derived from feasible one-sided variations, not an unjustified unconstrained Euler equation at the free boundary.

At a right support endpoint, monotonicity gives interior derivative<=0. A strictly negative derivative followed by exterior derivative0 gives a positive atom in p'', hence a negative atom in the residual, contradicting its positivity. Thus smooth fit p'=0 is forced. At an isolated zero at the periodic antipode, the derivative jump would be twice the same positive quantity and is excluded identically. Full positive support instead has the ordinary periodic derivative matching condition. These cases cover the endpoint ell=pi without assuming differentiability in advance.

## Rearrangement and equality

The coarea computation uses ordinary angular length; division by2pi multiplies both original and rearranged energy by the same factor. At a regular proper superlevel set with endpoint slopes a_j,

    (sum |a_j|)(sum 1/|a_j|) >= (#endpoints)^2 >=4.

The rearranged interval has exactly two endpoints and equal absolute slopes, giving the stated lower energy. The standard one-dimensional approximation passage can also be confined to the actual minimizer: on every positive component it solves the smooth ODE, so regular levels away from endpoints have the required finite smooth boundary description. Equality at almost every such level forces exactly two endpoints and equal absolute slopes. Their inverse derivatives have opposite signs and equal magnitudes, so their midpoint is fixed as the level varies. A positive plateau would solve the ODE with zero derivative on an interval, and ODE uniqueness would make that whole positive component constant; continuity at a support boundary, or r>1 on the full circle, excludes it. Therefore no moving-center or multiple-bump equality family survives. Every minimizer is a translate of the centered one.

For the centered decreasing solution, lambda<=0 cannot give two distinct derivative zeros unless constant. For lambda>0, the sine derivative and monotonicity force the first half-period rather than a higher oscillation. On proper support this yields A(1+cos(k theta)), ell=pi/k. Mass-one Haar normalization fixes A=k and r=3k/2. On full positive support periodicity and monotonicity yield 1+A cos(theta), with r=1+A²/2 and A<=1. The threshold r=3/2 is consequently forced by feasibility, not selected by comparing two arbitrary ansatz energies.

## Independent constants and H2 check

On the harmonic branch, E=A²/2=r-1, hence kappa=(r-1)/r. For the compact branch, setting u=k theta gives mass1, concentration3k/2 and E=k³/2, hence kappa=k²/3=4r²/27. The weak second derivative is -k³cos(k theta) on the support and0 outside. Since both p and p' match at its endpoints, there are no delta terms. It is square integrable, with squared norm k5/2 under normalized Haar, exactly as the checker reports. Thus the attained H1 lower bound is also attained in the required H2 class; it need not be C2 at the boundary. At the threshold both values are1/3 and both derivatives4/9.

At r=1, Cauchy-Schwarz forces p=1 almost everywhere; H2 continuity makes this the same pointwise profile. For r>1 the two listed families exhaust equality up to translation. The source correctly leaves a physical choice of r and a physical minimization principle unproved. This is a sharp conditional tradeoff, not selection of a profile by the current axioms.

# Independent root proof review

PASS for the analytic transform, source DERIVATION.md SHA256 9364f887a0ab254abcd1433d3ee621055d711d385d2c8f6e3c8621c21af82f79. No physical integration or source replay performed.

I independently reduced the rational divided difference: t²/(X+t²)-s²/(X+s²)=X(t²-s²)/[(X+t²)(X+s²)], giving the stated removable value A+sA'/2. Tonelli applies to the nonnegative integrand and yields the B transform, including X=0 by continuity with no atom.

The low tail follows X/(X+t²)<=1. The exact geometric remainder of 1/(X+t²) after m terms is (-X)^m/[t^(2m)(X+t²)]; multiplying X/(X+s²), bounding X<=12h² and integrating gives the stated signed remainder. Cn=E[X^n]-s²C(n-1) follows polynomial division. Actual interval recurrence cancellation must be retained.

On |z-c|<=c/2, Re z>=c/2 and |Im z|<=c/2 imply Re(z²)>=0, hence |X+z²|>=X; factorization also gives >=c²/4. Thus M=min(A(s),4/c²) is valid. The rho2.5 ellipse displacement29a/40<3a/4 fits the disk. Chebyshev tail at degree2p-1 is (10/3)M rho^(-2p), and positive quadrature plus integration doubles this times interval length. No finite-dimensional norm factor is missing for this scalar statement.

The scalar-call count is conditional on a sufficiently accurate A oracle and stable joint divided differences. It supplies neither physical values nor a final runtime/Gram/node certificate. This is a focused independent source review, not formal audit or pipeline approval.

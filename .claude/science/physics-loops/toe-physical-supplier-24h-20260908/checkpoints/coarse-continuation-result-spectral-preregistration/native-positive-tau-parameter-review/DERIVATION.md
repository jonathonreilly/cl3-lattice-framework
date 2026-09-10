# Positive tau selection is a certificate parameter

Source-only independent proof; no actual residual moments are read. Let delta>0 and tau>0 be exact rationals. Define A=(tau+2delta)/(delta²tau³), B=-2/tau³-2tau A, C=3/tau²+tau²A. Direct multiplication gives

 x²(Ax²+Bx+C)-1 = A(x-delta)(x-tau)²(x+delta tau/(tau+2delta)).

Every factor on the right is nonnegative for x>=delta. Thus Q_tau(x)>=x^-2 for every positive tau, regardless of how tau was selected. Integrating against the positive residual spectral measure gives the valid upper bound A rho2+B rho1+C rho0.

A midpoint calculation may choose an exact dyadic tau, provided its positivity and finite declared size are checked. It need not enclose an optimal tau or correspond to physically consistent midpoint moments. After selection, recompute A,B,C and the bound using the FULL original directed rho intervals, with negative B taking the lower rho1 endpoint for an upper bound. Do not use midpoint objective values as the certificate. Refuse a nonpositive or out-of-cap candidate. Retain the selected tau and full re-evaluation before any target interpretation. Including the original gap bound gives a valid minimum even if the candidate is poor. No optimizer or improvement claim follows from selection alone.

For a prospective selector, putting u=1/tau expands the expectation as

 rho0/delta² + a1 u + a2 u² + a3 u³,
 a1=2rho0/delta-2rho1/delta²,
 a2=3rho0-4rho1/delta+rho2/delta²,
 a3=2rho2/delta-2rho1.

This is a convenient candidate construction, not a new precision premise. Exact physical moments satisfy a1<=0 and a3>=0, but arbitrary interval midpoints need not; a robust finite selector must handle all branches or fall back to a fixed positive tau. These moment inequalities are not required for the final certificate's validity.

No scientific evaluation, claimed optimal degree, or physical sign is supplied by this note.

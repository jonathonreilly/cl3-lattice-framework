# Finite-volume and macroscopic additions: independent PASS

Full updated DERIVATION9bfd1f52149a3a57b146bb177f876cdd48808ad48bda48e4d051a00a141936eb read. This supplements previous conditional review53c700d3; it does not restamp the unproved uniform LC premise as established. Related weak-electric input authorship is disclosed. No physical calculation was performed.

Finite-volume result: D>=0 and E_U<=E0+3UN/2 give the compressed lower bound kappa*m-3UN/2. For U<=kappa/(3N), this is at least kappa*m/2 for every nonempty set, including equality. The existing recursion therefore gives factor32U/kappa. The U=0 endpoint is separately established by stiffness; the positive-power bound and geometric contour sum use their stated strict coupling conditions. The explicit kappa1161h/204800 agrees with the previously reviewed linear-density coefficient102400/387. The shrinking-volume-window scope is correct.

Macroscopic result: for every normalized constrained vector, H'-E' has expectation at least kappa*k-U*sqrt(75Nk), because E'<=E0 and the statewise V bound applies to this arbitrary vector, not only a ground vector. If k>=m>=300N(U/kappa)^2, the second term is at most kappa*k/2. Hence the compression is bounded below by kappa*m/2. This is a quadratic-form implication and needs no false identity with sqrt(K). The scalar shift cancels exactly.

For U>0, A>0 and m0=max(0,ceil(A)-1) is precisely the largest nonnegative integer strictly below A. Thus all integers m>m0 qualify, including m=A when A is integral. The recursion terminates only at m<=m0, and the truncated ceiling decreases by at most1 after deleting at most8 faces. This gives the stated q^(2ceil((m-m0)/8)) for q<1. Exact rational controls cover threshold cases and equality endpoints. U=0 remains a separate direct argument. The domain is all prescribed sets and their disconnected descendants, as required.

Young's inequality is legitimate pointwise for every normalized vector and therefore yields the affine operator lower bound. At b=1/4 it gives(3/4)kappa K-75NU^2/kappa; at m>=300Nx^2 this is at least kappa*m/2. The general theta cutoff75Nx^2/(1-theta)^2 and optimized b=(1-theta)/2 agree exactly. The source's b=1/2 comparison is also correct.

Corrected Euler encoding doubles all edges and gives36^m. For m>m0, q^(2ceil((m-m0)/8))<=q^((m-m0)/4); union bounding yields the stated q^(-m0/4)*a^ell/(1-a) for a<1. The extensive prefactor and cutoff prevent a fixed-U local thermodynamic contour conclusion. No missing entropy factor is hidden in the prescribed-set theorem; the source correctly requires an explicit binomial factor for a total-count event.

Verdict: PASS as actual finite-volume shrinking-window and fixed-small-coupling macroscopic joint-event consequences, conditional only on the declared supplied model and proved upstream inequalities. Uniform LC remains a separate open design obligation. No correction requested.

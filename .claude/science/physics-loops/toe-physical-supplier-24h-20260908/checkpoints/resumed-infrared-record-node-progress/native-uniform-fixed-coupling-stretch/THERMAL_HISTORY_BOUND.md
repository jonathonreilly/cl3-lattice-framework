# Exact finite-beta bound on a segmented flux history

A partial connected-expansion input, conditional on the already supplied THERMAL fixed-flux partition stiffness, not merely ground-energy stiffness. No physical calculation. This does not yet bound the connected relative susceptibility at nonzero U.

Let Z_F(beta) be the full active Fock partition function in a fixed flux orbit. Suppose the upstream thermal result gives Z_F/Z_0<=exp(-beta kappa_beta |F|), uniformly in volume at its declared beta. Constant spectator/parity multiplicities cancel in this ratio; this must be checked when choosing representatives, rather than switching to a fixed-particle trace. A local chemical potential -sP_f changes the sector Hamiltonian by the scalar -s 1_(f in F). Thus for0<=s<=kappa_beta/2,

 Z_F(beta,s)/Z_0(beta,s) <=exp[-beta(kappa_beta |F|-s1_(f in F))]
                          <=exp[-beta kappa_beta |F|/2].

Consider one closed electric history with nonnegative durations tau_i summing beta, flux sectors F_i, and any unitary gauge-identification factors between them. For its trace amplitude use the Schatten generalized Holder inequality, assigning exponent p_i=beta/tau_i to each positive factor exp(-tau_i H_Fi), and infinity norm to unitary factors. Then

 |Tr product_i [exp(-tau_i H_Fi) U_i]| / Z_0
 <= product_i Z_Fi(beta)^(tau_i/beta)/Z_0
 <= exp[-sum_i tau_i kappa_beta |F_i|].

Zero-duration factors are interpreted by their norm-one limit. Inserting -sP_f replaces the exponent with sum tau_i[kappa_beta|F_i|-s1_(f in F_i)]. This proof does not commute Hamiltonians, presume positive history amplitudes, or invoke an active spectral gap. It remains valid if a returning cut leaves a unitary active gauge factor; its norm is one. Each electric vertex's separate1/2 coefficient must still be restored in an expansion.

This gives a genuine beta-uniform penalty for the total time spent in wrong-face sectors, even when initial thermal active excitations have arbitrarily high TOTAL energy. It avoids the invalid attempt to extend a ground-vacuum resolvent bound directly to arbitrary thermal eigenstates.

Limit: a closed history returning to the zero-face sector pays no penalty during that interval. Holder also erases its spatial CAR cancellations. Summing its translates absolutely therefore does not produce a volume-uniform connected bound. In the full thermal trace one must additionally sum starting flux sectors and normalize by the FULL partition function; the displayed fixed-reference history estimate is not that completed cluster expansion. It is an input for separating wrong-flux excursions from zero-return propagators in the relative impurity Pf,V,V response. The higher-odd summability candidate can address one class of zero returns, while the linear return and other connected histories still need resummation.

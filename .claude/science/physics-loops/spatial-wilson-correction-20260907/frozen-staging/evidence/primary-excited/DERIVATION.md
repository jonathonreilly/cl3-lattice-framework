# Independent alternative-tree first excited correction

The preregistration and result hashes record the order of this calculation. Candidate numbers had already arrived unsolicited in an agent message; this is an independent implementation and gauge-tree check, not a blind-to-values experiment. Neither the orbital jet source nor its result was read before this result froze. The sole computational input is our previously frozen alternative-tree ground raw data, including independently derived SU(3) color traces and ordered face words.

Let Q(X)=Tr X², omega=sqrt(55)/90 and theta=(32-3sqrt(55))/23. The limiting eight-dimensional Mehler ground is phi0 proportional to exp(-omega Q/2). Its first nonconstant conjugation-invariant eigenfunction is phi1=(4-omega Q)phi0. Under phi0², omega Q has mean4 and variance4; thus this state is orthogonal to the ground, has four times its squared norm, and is the sole invariant degree-two branch. Its eigenvalue is lambda0 theta².

With two source penalties a,b, define G=(H/3+2aP_u+2bP_v)^-1 and Gamma the unnormalized 136-dimensional Gaussian integral. There are eight independent color coordinates. Consequently logGamma_a=-8Guu, logGamma_b=-8Gvv, logGamma_ab=16Guv². Direct differentiation of the inverse gives Ga=-2GPuG, Gb=-2GPvG and Gab=4(GPuGPvG+GPvGPuG).

The polynomial entering the normalized source kernel is K=E_G(E3²/2-E4)-2TrG+Guu+Gvv. The last two entries restore the source half-Haar densities; omitting them before differentiation changes the excited answer. In the program K is assembled into actual scalar monomials of symmetric covariance entries. The cubic variance is expanded into the six permutations of each determinant, quartic words into the three independently computed color pairings. Every monomial is differentiated by the elementary product rule, retaining both distinct-factor mixed terms and each same-factor Gab term. This differs from the orbital four-component jet implementation. The exact inverse derivative equations and a separately symbolic two-by-two source covariance calculation validate these derivatives.

At a=b=omega/2 write la=logGamma_a, lb=logGamma_b and lab=logGamma_ab. The two radial insertions act by D=(4+omega partial_a)(4+omega partial_b). Thus

    d=D Gamma/Gamma=16+4omega(la+lb)+omega²(la lb+lab)=4theta²,
    D(Gamma K)/Gamma=d K+(4omega+omega² lb)Ka
                           +(4omega+omega² la)Kb+omega² Kab.

The partition coefficient is independent of a,b. It follows that k1=D(Gamma K)/(D Gamma)-Z1, while k0=K-Z1. Exact arithmetic on the alternative tree gives

    k0 = 126839623/20482880 + 27961081 sqrt(55)/27931200,
    k1 = 137812123/20482880 + 27961081 sqrt(55)/18620800,
    k1-k0 = 49875/93104 + 27961081 sqrt(55)/55862400 > 0.

All coefficients, 17-by-17 covariance derivatives, monomials and Gaussian normalization derivatives are retained in result.json. The existing ground coefficient is reproduced exactly, rather than inserted as an expectation. Ten actual named controls pass in 4.18 seconds at 65.69 MiB.

For the actual spectral conclusion, use the separately reviewed common Hilbert-Schmidt kernel expansion through epsilon², with epsilon=beta^-1/2. Its whole epsilon coefficient vanishes. Hence the usual first perturbation of each isolated simple eigenbranch at order epsilon² is its diagonal matrix element; there is no resolvent term made from an epsilon-order perturbation. The limiting invariant ground and degree-two branches are simple and separated. Therefore the actual first/top ratio has expansion theta²[1+(k1-k0)/beta+o(beta^-1)]. The positive coefficient gives eventual approach from above at this asymptotic order; it supplies neither monotonicity, an explicit onset, beta=6 accuracy, nor a physical gap identification. This argument relies on whole-kernel cancellation, not merely a zero ground expectation.

After freezing these raw data, the orbital derivation and actual result were opened. Their independently differentiated coefficients agree exactly despite the different adapted spanning tree and differing intermediate Wick pieces. The comparison receipt binds both raw files and checks symbolic equality of k0, k1 and the relative difference.

# Natural ring time from finite local elimination and ice restriction

Conditional finite-volume expectation theorem, uniform in volume, for consistently dressed ice states. Root exposed the failure of the earlier generic order5 estimate before this attempt. The present route was derived independently in scratch; before this writeup froze, root sent its completed proof hash and a simpler no-compression construction. That proof was not read. The compression route below was already derived and communicated first; the newly received simplification is not claimed as an independent discovery here. Original order5 proof761aaa and sharpeningb34 remain unchanged.

## The failure that must not be concealed

Use dimensionless epsilon=|g|lambda_*/U and time u=Ut. The order5 local remainder is O(epsilon6), but its available generic velocity is O(epsilon). At u=tau epsilon^-4, the bound epsilon6 u(1+epsilon u)^3 is O(epsilon^-7) for fixed nonzero tau. The bound is valid but does not control even one natural ring period. One may not replace the velocity of K1 in excited charge sectors by the ring velocity without a separate argument.

## Uniform finite order14 construction

The proved homological construction extends to any fixed integer N. In particular take N=14. All generator coefficients S_j have connected strong support at most11j. Use exactly the improved recursion f_j,s_j=4f_j in sharpeningb34, now through j=14; its induction uses [S_j,D]=-(F_j-P_D F_j), so it remains valid at every fixed j. No convergence of the formal infinite series is claimed.

Put m=11N=154, kappa=1/m, s=sum_{j<=N}s_j, rho=min(1,1/(24m max(1,s))), M=174. Since exp(11j kappa)<=e<3, on |z|<=rho the polynomial generator has norm at most3rho s<=1/(8m). The maximum-support Lie-series argument then gives an exact finite-volume unitary Y_N=exp(sum_{j<=N}z^jS_j) and

 Y_N H Y_N†=UD+K_N+R_N,
 K_N=U sum_{j=1}^N z^j K_j,       [K_j,D]=0 termwise,
 ||R_N||_kappa <= 2M U (epsilon/rho)^(N+1),
 ||K_N||_kappa <= 2M U epsilon/rho,

for epsilon<=rho/2. Here z=g lambda_*/U can have either sign. The bound M follows from ||D||_kappa<=54, ||V||_kappa<=33 and the factor2 Lie bound. These are explicit recursive constants, independent of volume; their smallness regime is not asserted to be useful numerically.

The same parity and canonical-gauge argument used at order5 gives on the COMPLETE ice space P:

 P K_1 P=P K_3 P=P K_5 P=0,
 P K_2 P=c2 P,
 P K_4 P=c4 P+J4|_P.

J4 is the known full local fourth ring extension, including straight winding four-cycles when an extent is four. It preserves every charge exactly. Scalars c2,c4 may grow with volume; they disappear from state evolution and need no global norm bound. This identifies only the fourth coefficient, not the canonical sixth diagonal in this new gauge.

## Auxiliary local ice compression

For a finite edge set S let Pi_S be the diagonal projector onto local bit patterns on S that occur as restrictions of some global ice string. It is supported on S, has norm1 and commutes with every charge-star operator. It may depend on the finite geometry and is not claimed to be efficiently computable or an available native instrument. It is used only to construct a comparison Hamiltonian, not to change the supplied H or its preparation.

If B_S is supported on S, commutes with D, and P B_S P=0, then B_S Pi_S=0. Proof: extend a local input pattern a to a full ice string a xi. For each nonzero matrix element B_ba, commutation with the nonnegative diagonal D forces b xi to have D=0 too. Its matrix element of P B_S P is therefore exactly B_ba, so it must vanish. The same reasoning shows Pi_S B_S Pi_S agrees with B_S on global ice, and this compression cannot increase the local interaction norm. Strong support survives because Pi_S is diagonal in the same charge basis.

Group each perturbative coefficient by its coupling monomial before applying this argument. All nested terms for that monomial can be assigned to the union of its endpoint stars, size<=11j; grouping cannot increase the majorant norm. Charge averaging makes each grouped coefficient D-conserving. Since the low-order identities hold for independently variable edge couplings, they hold separately for each monomial. Thus the zero lower-order pieces and scalar-subtracted fourth differences vanish under this compression. No assumption that an arbitrary locally ice-looking pattern has a global completion is needed: Pi_S is defined by actual extendibility.

Let tilde K_j for j>=6 be the termwise compressed coefficient. Define

 L_N=U z4 J4 + U sum_{j=6}^N z^j tilde K_j.

It is a local D-conserving Hamiltonian with the same action on P as K_N, apart from the two scalar terms, and

 ||L_N-U z4 J4||_kappa <= 2M U epsilon6/rho6.

Its norm is O(U epsilon4), uniformly in volume. For example ||J4||_kappa<=84 is sufficient: each four-cycle uses at most44 assigned edge sites, a physical edge lies in at most55 endpoint-star cycle supports, and each coefficient has magnitude<=1/2. For N14, exp(44/154)<3. The omitted high terms are bounded by the preceding geometric coefficient sum. A large but sufficient coefficient in ||L_N||<=C_L U epsilon4 is C_L=84+2M/rho6, for epsilon<=1.

This is an expectation comparison on ice, not an operator-norm assertion that K_N equals L_N on all charge sectors. All K_j and L_N preserve P. Consequently for any ice-supported density matrix and any observable their evolved expectations under UD+K_N and L_N are exactly equal after canceling the scalar phase.

## Two separate light cones

First compare exact transformed dynamics with UD+K_N using the already proved strong-support interaction-picture estimate. Its velocity is allowed to be fast, v_fast=C_fast U epsilon; no improvement is assumed. For fixed local O_X, the norm error is bounded by

 C_X U epsilon^(N+1) |t| (1+C_fast U epsilon |t|)^3,

where C_X includes the fixed rho and geometric constants. Rotating under UD preserves strongly supported remainder terms and only thickens a generic observable once. Thus no O(U) velocity enters this bound.

Second, after restricting expectations to initial ice, replace K_N by L_N exactly as above. Compare L_N with U z4 J4. The perturbation now has local norm O(U epsilon6), and the comparison light cone has speed O(U epsilon4), because the complete comparison Hamiltonian contains no lower-order excited-sector terms. This gives

 C'_X U epsilon6 |t| (1+C_slow U epsilon4 |t|)^3.

One may use the ring Hamiltonian alone as the Duhamel reference, so no putative gap or thermal distribution enters. Both estimates use connected supports and the same positive exponential weight. All constants are independent of lattice volume, U, epsilon and t within the stated regime.

At t=tau/(U epsilon4), epsilon<=1, the first bound is at most

 C_X |tau|(1+C_fast|tau|)^3 epsilon^(N-12),

and the second is at most

 C'_X |tau|(1+C_slow|tau|)^3 epsilon².

With N14 both are O(epsilon²). This is the missing natural-time result: for every fixed rescaled ring time tau and fixed local dressed-frame observable, the exact supplied dynamics in a dressed ice state approaches its fourth-order ring expectation with a uniform-in-volume O(epsilon²) bound. The constants are deliberately conservative. There is no simultaneous tau-to-infinity estimate beyond the displayed polynomial factors.

In laboratory variables the initial state is Y_N† rho Y_N and the observable is Y_N† O_X Y_N. Bare local observables may instead be compared with an additional O(epsilon) local dressing error; their transformed quasi-local tails are summable in a smaller positive weight. Bare ice initialization is NOT covered by simply discarding Y_N: small local dressing need not make an extensive state's global norm close, nor bound the chance of any defect somewhere. No global ice spectral band, photon, RK point, phase, physical coupling selector or efficient implementation of the dressing is claimed.

## Provenance and remaining simplification

The temporary Pi_S comparison is mathematically local but uses globally defined admissibility data. Root's independently frozen message proposes omitting this machinery: retain the uncompressed K_j for j>=6 and delete only the known lower-order zero/scalar-on-ice terms. That route appears sufficient because equality is only required on P. It will be checked after this proof freezes; if valid it removes an unnecessary auxiliary construction rather than repairing the time-power estimate. This manuscript records the independently derived route without rewriting its provenance.

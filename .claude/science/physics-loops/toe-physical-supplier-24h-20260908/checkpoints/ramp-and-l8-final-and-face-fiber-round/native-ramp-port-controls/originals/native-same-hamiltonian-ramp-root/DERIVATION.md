# Preparing the dressed ice sector by ramping the same supplied Hamiltonian

Root candidate proof, frozen before reading the parallel ramp attempt. This removes a separate arbitrary dressing operation from a conditional preparation route. It does not derive the supplied Hamiltonian, ramp schedule, initial classical ice preparation, or a ground state.

## Protocol and small parameter

Write H_final/U=D+epsilon V, where epsilon>0 and V=sum b_e A_e has fixed real |b_e|<=1. A negative overall g can be absorbed into b_e. Let N=14. On 0<=sigma<=1 define the fixed polynomial

f(sigma)= [integral_0^sigma t^N(1-t)^N dt] / [integral_0^1 t^N(1-t)^N dt].

It has rational coefficients, f(0)=0, f(1)=1, and f^(j)(0)=f^(j)(1)=0 for1<=j<=N. Extend it constantly outside this interval. Use dimensionless time u=Ut and sigma=epsilon u during the ramp. The laboratory Hamiltonian is

H_ramp(u)/U=D+epsilon f(epsilon u)V, 0<=u<=epsilon^-1,

and is held at H_final afterward. The ramp duration is T=1/(Uepsilon), much shorter than the ring time1/(Uepsilon^4). Start in any supplied ice-supported density matrix rho0; a fixed classical ice bitstring is a special case.

## A time-dependent finite local frame

At each sigma construct S(sigma,epsilon)=sum_{j=1}^N epsilon^j S_j(sigma) with the same strong-support homological inverse Gamma as in the static local proof. The transformed dimensionless generator is exactly

F=exp(S)(D+epsilon f V)exp(-S)
  +i epsilon (partial_sigma exp(S))exp(-S),

where

(partial_sigma exp(S))exp(-S)=sum_{m>=0} ad_S^m(partial_sigma S)/(m+1)!.

The sign is positive because the transformed state is exp(S)|psi>. For the coefficient of epsilon^j, omit S_j and call the known Hermitian remainder R_j(sigma). Set S_j=Gamma R_j and K_j=A_D R_j. The new coefficient is R_j+[S_j,D]=K_j. The derivative of S_j first enters at orderj+1, so this is a well-defined triangular recursion. Every K_j term commutes with D, and every S_j is anti-Hermitian. Differentiation in sigma changes no support. All operations preserve connected strong supports; at orderj, support size is at most11j physical edges.

This finite construction has uniform local bounds. One explicit way to organize its induction is to use the seminorm

||B||_(k,l)=sum_{a=0}^l (1/a!) sup_{sigma in[0,1]} ||partial_sigma^a B(sigma)||_k.

Leibniz's rule and the factorial weights bound products/commutators by the same convolution majorants as the static norm. Differentiation satisfies ||partial_sigma B||_(k,l)<=(l+1)||B||_(k,l+1). At recursion stepj keep derivatives through N+1-j. The previously constructed coefficients have the extra derivatives needed for the new derivative term. The fixed polynomial f supplies every finite derivative bound. Thus finite, volume-independent constants bound S_j, its first derivative and K_j in a fixed positive final support norm.

Choose a sufficiently small positive radius r so that, uniformly in sigma and complex |epsilon|<=r, the finite polynomial S satisfies the same convergent Lie-series bound as the static proof. Its sigma derivative is bounded by a finite polynomial too. The additional derivative Lie series has the same convergence radius (and a larger harmless constant). Banach-valued Cauchy estimates, uniformly on the compact sigma interval, give an exact decomposition

F(sigma,epsilon)=D+sum_{j=1}^N epsilon^j K_j(sigma)+E_ramp,
||E_ramp||_k <= C_N epsilon^(N+1),

for epsilon<=r/2. Every constant depends only on the fixed N, polynomial f, norm convention and geometry, not on volume, U or epsilon. This is a finite asymptotic theorem with constructive finite seminorm recursions; it makes no numerical claim about practical ramp rates. No infinite formal-series convergence or global isolated ice band is assumed.

## Endpoint matching

Each S_j is a differential polynomial in f and its derivatives through orderj-1. At sigma=0 all these inputs vanish, so S_j(0)=0 and Y_start=I exactly. At sigma=1, all derivatives throughN vanish while f=1; the recursive coefficients are exactly those of the STATIC orderN construction. Consequently Y_end=Y_static,N exactly as finite polynomials. Derivative terms vanish at the join, and the moving frame can be continued as the constant static frame during the hold.

Let W_ramp be the time-ordered evolution under the D-conserving polynomial generator D+sum_{j<=N}epsilon^jK_j(sigma). Since every coefficient commutes with D, it maps ice to ice. Define rho1=W_ramp rho0 W_ramp†. This is a definite effective state determined by the supplied ramp. It is not assumed to equal rho0, a thermal state, or the ring ground state. No arbitrary extra preparation map is inserted: rho1 is the outcome of the explicit effective evolution associated with the same laboratory ramp.

## The error must cover the subsequent ring observation

A small local error at the end of the ramp cannot simply be propagated for a long time without accounting for its growing backward light cone. Compare the complete laboratory ramp-plus-hold protocol, in its continuous moving frame, with the D-conserving polynomial reference on both intervals. Let the hold duration be t_hold=s/(Uepsilon^4), with fixed s>=0.

The reference perturbations have local strength O(Uepsilon) on both intervals; the large UD rotation can be factored and does not propagate beyond a fixed star neighborhood. The time-dependent Lieb–Robinson/Duhamel argument therefore bounds the contribution of the ramp remainder to a fixed local final observable by

C_O epsilon^(N+1) epsilon^-1 [1+C epsilon(epsilon^-1+s epsilon^-4)]^3
 <= C'_O epsilon^(N-9)(1+C's)^3,

in dimensionless time and for epsilon<=1. The extra epsilon^-9 is the backward-cone volume at the observation time; it has not been omitted. The static hold remainder contributes the previously proved bound

C''_O s(1+C''s)^3 epsilon^(N-12).

For N=14 these are O(epsilon^5) and O(epsilon²). During the reference hold the initial state rho1 remains in ice. Replace its static K_N evolution by the slow local extension L_N=Uepsilon^4 J4+U sum_{j=6}^N epsilon^jK_j, dropping only known scalar/zero-on-ice lower terms. This is exactly the no-compression construction proved in the natural-time note. Comparing L_N to the pure fourth-order ring generator has error O(epsilon²) at fixed s. All bounds are uniform in volume for fixed local observable support.

It follows that the actual same-Hamiltonian ramp, starting from bare ice, followed by a hold for a fixed number of ring-time units, has the ring expectation of the effective ice state rho1 up to O(epsilon²), when the final laboratory observable is Y_static,N† O Y_static,N. For a bare local laboratory observable O, the final dressing differs locally by O(epsilon), so a corresponding O(epsilon) comparison is available after including that correction. No global state-norm approximation is asserted.

## What is and is not supplied

This gives a route using only a smooth change of the coefficient of the already supplied native perturbation, with fixed UD, rather than a separately programmed nonlocal unitary Y. The mathematical moving frame is an analysis device. No hard low-charge gate, bath, additional species or adiabatic ground-state gap is introduced. The ramp does not cool the ice sector or prepare a Coulomb/ground state; rho1 may be a nontrivial ice state. The chosen polynomial schedule and initial ice bitstring remain physical inputs, and the axioms have not selected U, g, geometry or the occurrence/readout law.

## Primary prior art and reading scope

Ho and Abanin, https://arxiv.org/abs/1611.05024, study local time-dependent frame methods for slowly ramped Floquet systems. Root opened the primary PDF https://arxiv.org/pdf/1611.05024 and read SectionsI–II.B through the first transformation formulas (PDF pages1–4). Their Floquet preparation result is contextual prior art, not the theorem used here; no claim of novelty for time-dependent Schrieffer–Wolff methods is made. The present finite strong-support recursion and endpoint matching are stated explicitly because the highly degenerate ice sector has no assumed volume-uniform spectral gap.

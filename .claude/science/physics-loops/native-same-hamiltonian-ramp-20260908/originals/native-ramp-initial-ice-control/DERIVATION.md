# The same-Hamiltonian ramp retains the original ice initial state locally

Conditional extension of the two independently proved smooth-ramp constructions. Both complete ramp proofs were read first. Root proposed the derivative-count/reality argument before this derivation. Its45-control matrix implementation was also read; the new exact calculation uses Pauli-vector cross products for an arbitrary smooth profile instead of that fixed-polynomial matrix implementation. This is not a claim of untouched candidate exposure.

## Setup and precise claim

Use the supplied full native real edge Hamiltonian H(u)/U=D+epsilon f(epsilon u)V, V=sum b_e A_e with fixed real coefficients, epsilon>0, u=Ut. Take the fixed flat-endpoint profile and order14 time-dependent homological frame from the ramp proofs. The ramp lasts u=epsilon^-1; its endpoint frame is the static Y14 exactly. The existing concatenated ramp-plus-hold estimate, including the propagated fast light cone, compares actual expectations with ring dynamics starting from an effective ice state rho1, with O_tau(epsilon²) error for dressed final local observables. We do not alter that proof or its remainder.

Here we prove that rho1 may be replaced by the ORIGINAL supplied ice state rho0 in that ring comparison, at an additional O_tau(epsilon³) local-expectation cost. Consequently the overall dressed-observable bound remains O_tau(epsilon²). No ground-state, bare-observable epsilon², arbitrary initial non-ice state, or global trace-norm approximation is asserted.

## Correct joint grading, not static epsilon parity

Let k be the number of V factors in a formal term and l its total profile derivative weight: f^(a) has weight a, so a product has the sum of derivative orders. Every order-n coefficient in the moving-frame recursion has

 n=k+l, with k>=1.

Induction proves this: D carries neither count, the original epsilon fV has k1,l0, multiplication adds both counts, charge averaging and its homological inverse preserve them, and the derivative term i epsilon partial_sigma raises l by one. The commutator and exponential factorials do not change the count. Derivatives distribute by Leibniz, preserving total weight.

Global bit parity acts by(-1)^k, not generally(-1)^n. Since bit parity is scalar on ice, odd-k terms have zero ice restriction. This alone does NOT justify discarding all odd orders in the ramp.

In the native edge-bit basis D and every A_e are real. The charge average merely deletes unequal-energy entries and Gamma divides by their real energy differences. Thus a term with derivative weight l is i^l times a real matrix. For real profile data each joint-(k,l) component of the effective generator is Hermitian. One may formalize this separation by multiplying every derivative term by an independent real bookkeeping parameter: Hermiticity holds at all values, so its coefficients are Hermitian separately.

A two-V ice return uses the SAME edge twice. Two distinct edges cannot form a balanced changed-edge set on a simple graph; at an endpoint of their union a changed edge would leave a nonzero degree increment. In particular two distinct ice strings cannot differ on only two edges. Resolvents, D averaging and profile derivatives insert only diagonal factors, so they do not alter this conclusion. Every two-V ice matrix element is therefore diagonal. With odd l it is also purely imaginary and Hermitian, hence zero.

It follows that K1|P=0; K2|P is the usual scalar -f² sum b_e²/2; and K3|P=0. At order3 the only even-k case is k2,l1, eliminated by the preceding reality argument. No static epsilon-parity assumption was used.

## Order four, including the derivative scalar

The k4,l0 contribution is precisely f^4 times the static fourth coefficient in the same homological gauge. The only other even-k contribution has k2,l2. Both flips use one edge; on ice its intermediate energy is always2 and A_e²=I. Its diagonal coefficient is independent of the ice background, so it is scalar even before computing its value.

For completeness, the exact coefficient can be obtained on the corresponding two-level problem D=I-Z, V=X. Write S=i a.sigma. Then

 exp(ad_S)h.sigma has vector exp(-2a cross)h,
 i epsilon (partial exp S)exp(-S) has vector
 -epsilon sum_{m>=0}(-2a cross)^m a'/(m+1)!.

The first coefficients are a1=(0,-f/2,0), a2=(f'/4,0,0). The arbitrary-profile recursion through4 gives the lower-energy diagonal coefficients

 K1=0, K2=-f²/2, K3=0, K4=(f^4+f f'')/8.

The single-derivative generator is explicitly nonzero; this is an adverse witness against using static grading. Restoring the edge coefficient gives the universal k2,l2 scalar (f f''/8) sum b_e². No claim is made that the derivative scalar vanishes; only its effect on density-matrix evolution does.

Thus, with the parent's static fourth scalar c4 and ring J4,

 K4(sigma)|P = f(sigma)^4 [J4|P+c4 I_P]
                  + [f(sigma)f''(sigma)/8] sum b_e² I_P.

The same-edge reduction is legitimate on the full carrier because the two-step history has only that single D2 intermediate state. It does not replace arbitrary higher paths by two-level dynamics. Four-V histories include the actual native signs and extent-four winding terms already fixed by the static parent.

## A slow local ramp extension

Let the effective ramp generator be D+sum_{j<=14}epsilon^jK_j(sigma). Define instead on the full carrier

 L_ramp(sigma)=epsilon4 f(sigma)^4 J4
                  +sum_{j=5}^{14}epsilon^j K_j(sigma).

Every term conserves D and is local in the same strong-support norm. Its restriction to ice differs from the effective ramp generator only by scalar terms, including D=0. Its local norm is bounded by C epsilon4 uniformly on the fixed compact profile interval and independently of volume. We deliberately retain order5 and all higher coefficients: time derivatives invalidate a blanket odd-order deletion. No globally admissible-pattern compression or extra preparation map is needed.

Let W_r be the time-ordered evolution of this slow extension over0<=u<=epsilon^-1. For an initial ice density matrix, W_r rho0 W_r† is exactly rho1; the dropped terms change only an overall phase. This identity is for ice density matrices, not equality of the two Hamiltonians on excited states.

## Propagating the initial-state correction through the ring observation

For a final dressed-frame local observable O_X and fixed ring time tau, set O_tau=exp(i tau J4)O_X exp(-i tau J4). The ring interaction strength and tau are independent of epsilon in these rescaled variables. Its capped Lieb-Robinson commutator sum obeys

 sum_S ||[(L_ramp)_S(sigma),O_tau]||
       <= C_X ||O_X|| epsilon4 (1+B|tau|)^3.

Differentiate W_r(u)† O_tau W_r(u). The outer time-ordered unitaries preserve norm, so integrating this bound over the dimensionless ramp duration epsilon^-1 yields

 |Tr[(rho1-rho0) O_tau]|
       <= C_X ||O_X|| epsilon³ (1+B|tau|)^3.

There is no fast epsilon-speed light cone in this comparison: both density matrices are first restricted to ice and evolved by the explicitly slow local extension. The fast cone affecting the ORIGINAL physical ramp error was already fully priced in the source theorem and is not dropped. This estimate also does not assume a small global norm of rho1-rho0.

Combining the existing O_tau(epsilon²) physical ramp-plus-hold error with this additional O_tau(epsilon³) term proves a natural-ring expectation target with rho0 itself. The final laboratory observable remains Y14†O_XY14. For a bare local final observable the previously established O(epsilon) dressing cost remains; the initial-state improvement does not remove it.

## Evidence and scope

Own215 exact controls use the independent arbitrary-profile Pauli-vector recursion, verify every canceled transverse coefficient through4, the nonzero derivative generator and derivative scalar, and literal L4 two-edge support/energy checks. The full graph has192 edges and18,336 distinct pairs; none returns ice in two flips, and every single-edge denominator is2. These controls are not a simulation or a proof by finite enumeration of the uniform theorem; the general support/reality argument supplies that proof.

The schedule, initial ice preparation, native Hamiltonian and final dressed measurement are still supplied resources. The result does not prepare a ground state, establish a phase, select physical coefficients, or justify replacing every measurement by a bare local one at epsilon² accuracy. All original ramp proof bytes and this companion remain separate; no canonical source was changed.

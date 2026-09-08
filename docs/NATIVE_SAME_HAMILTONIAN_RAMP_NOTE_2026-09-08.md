---
claim_id: native_same_hamiltonian_ramp_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied smooth ramp of the full native Hamiltonian from bare ice, followed by a fixed natural ring time: volume-independent O(epsilon^2) local expectation comparison to ring dynamics from the original ice density matrix, for dressed final observables."
upstream_dependencies:
  - native_local_natural_ring_dynamics_note_2026-09-08
runner: scripts/native_same_hamiltonian_ramp_2026_09_08.py
---

# Same-Hamiltonian ramp and the original ice initial state

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

A smooth change of the coefficient of the supplied native Hamiltonian prepares the required effective ice sector without a separately programmed dressing unitary. After a fixed number of natural ring-time units, dressed local expectations agree with ring evolution of the **original** supplied ice density matrix to $O(\epsilon^2)$, uniformly in volume. This is neither cooling nor a ground-state preparation theorem.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Same-Hamiltonian ramp, supplied bare ice and dressed final readout."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Precise theorem and dependencies

Use the full carrier, even periodic cubic extents at least four, native $A_e$, strong-support norm and homological gauge of the [local natural-ring theorem](NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md), including its [full-carrier mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md), [dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and [instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md) dependencies. There is no fixed magnetic-cycle or winding sector, and no hard low-charge projection.

Write $H/U=D+\epsilon V$, $V=\sum_e b_eA_e$, real $|b_e|\leq1$, $U>0$, $\epsilon>0$. For each fixed local $O_X$, each finite $\tau_*>0$, all sufficiently small $\epsilon$ and every ice-supported density matrix $\rho_0$, the ramp below followed by a hold of duration $\tau/(U\epsilon^4)$, $0\leq\tau\leq\tau_*$, satisfies

\[
\left|\operatorname{Tr}(\rho_{\mathrm{lab,end}}Y_{14}^{\dagger}O_XY_{14})
-\operatorname{Tr}(\rho_0e^{i\tau J_4}O_Xe^{-i\tau J_4})\right|
\leq C_{X,\tau_*}\|O_X\|\epsilon^2.
\]

The constants and sufficient small-coupling radius depend on the fixed profile, order and geometry, not on volume or $U$. $Y_{14}$ is the static endpoint frame and $J_4$ the parent's signed fourth-cycle operator, including extent-four winding cycles. For a bare final observable the additional dressing cost is $O(\epsilon)$. No global trace-norm, global isolated-band or phase conclusion is implied.

## Protocol and small parameter

Write H_final/U=D+epsilon V, where epsilon>0 and V=sum b_e A_e has fixed real |b_e|<=1. A negative overall g can be absorbed into b_e. Let N=14. On 0<=sigma<=1 define the fixed polynomial

\[ f(\sigma)=\frac{\int_0^\sigma t^{14}(1-t)^{14}\,dt}{\int_0^1 t^{14}(1-t)^{14}\,dt}. \]

It has rational coefficients, f(0)=0, f(1)=1, and f^(j)(0)=f^(j)(1)=0 for 1<=j<=N. Extend it constantly outside this interval. Use dimensionless time u=Ut and sigma=epsilon u during the ramp. The laboratory Hamiltonian is

\[ H_{\mathrm{ramp}}(u)/U=D+\epsilon f(\epsilon u)V,\qquad 0\leq u\leq\epsilon^{-1}. \]

and is held at H_final afterward. The ramp duration is T=1/(Uepsilon), much shorter than the ring time1/(Uepsilon^4). Start in any supplied ice-supported density matrix rho0; a fixed classical ice bitstring is a special case.

## A time-dependent finite local frame

At each sigma construct S(sigma,epsilon)=sum_{j=1}^N epsilon^j S_j(sigma) with the same strong-support homological inverse Gamma as in the static local proof. The transformed dimensionless generator is exactly

\[ F=e^S(D+\epsilon fV)e^{-S}+i\epsilon(\partial_\sigma e^S)e^{-S}, \]

where

\[ (\partial_\sigma e^S)e^{-S}=\sum_{m\geq0}\frac{\operatorname{ad}_S^m(\partial_\sigma S)}{(m+1)!}. \]

The sign is positive because the transformed state is exp(S)|psi>. For the coefficient of epsilon^j, omit S_j and call the known Hermitian remainder R_j(sigma). Set S_j=Gamma R_j and K_j=A_D R_j. The new coefficient is R_j+[S_j,D]=K_j. The derivative of S_j first enters at order j+1, so this is a well-defined triangular recursion. Every K_j term commutes with D, and every S_j is anti-Hermitian. Differentiation in sigma changes no support. All operations preserve connected strong supports; at order j, support size is at most11j physical edges.

This finite construction has uniform local bounds. One explicit way to organize its induction is to use the seminorm

\[ \|B\|_{\kappa,\ell}=\sum_{a=0}^{\ell}\frac1{a!}\sup_{\sigma\in[0,1]}\|\partial_\sigma^aB(\sigma)\|_\kappa. \]

Leibniz's rule and the factorial weights bound products/commutators by the same convolution majorants as the static norm. Differentiation satisfies ||partial_sigma B||_(k,l)<=(l+1)||B||_(k,l+1). At recursion stepj keep derivatives through N+1-j. The previously constructed coefficients have the extra derivatives needed for the new derivative term. The fixed polynomial f supplies every finite derivative bound. Thus finite, volume-independent constants bound S_j, its first derivative and K_j in a fixed positive final support norm.

Choose a sufficiently small positive radius r so that, uniformly in sigma and complex |epsilon|<=r, the finite polynomial S satisfies the same convergent Lie-series bound as the static proof. Its sigma derivative is bounded by a finite polynomial too. The additional derivative Lie series has the same convergence radius (and a larger harmless constant). Banach-valued Cauchy estimates, uniformly on the compact sigma interval, give an exact decomposition

\[ F(\sigma,\epsilon)=D+\sum_{j=1}^{14}\epsilon^jK_j(\sigma)+E_{\mathrm{ramp}},\qquad \|E_{\mathrm{ramp}}\|_\kappa\leq C_{14}\epsilon^{15}. \]

for epsilon<=r/2. Every constant depends only on the fixed N, polynomial f, norm convention and geometry, not on volume, U or epsilon. This is a finite asymptotic theorem with constructive finite seminorm recursions; it makes no numerical claim about practical ramp rates. No infinite formal-series convergence or global isolated ice band is assumed.

## Endpoint matching

Each S_j is a differential polynomial in f and its derivatives through order j-1. At sigma=0 all these inputs vanish, so S_j(0)=0 and Y_start=I exactly. At sigma=1, all derivatives through N vanish while f=1; the recursive coefficients are exactly those of the STATIC order N construction. Consequently Y_end=Y_static,N exactly as finite polynomials. Derivative terms vanish at the join, and the moving frame can be continued as the constant static frame during the hold.

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


## Replacing the effective ramp state by the original state

## Correct joint grading, not static epsilon parity

Let k be the number of V factors in a formal term and l its total profile derivative weight: f^(a) has weight a, so a product has the sum of derivative orders. Every order-n coefficient in the moving-frame recursion has

\[ n=k+\ell,\qquad k\geq1. \]

Induction proves this: D carries neither count, the original epsilon fV has k=1, l=0, multiplication adds both counts, charge averaging and its homological inverse preserve them, and the derivative term i epsilon partial_sigma raises l by one. The commutator and exponential factorials do not change the count. Derivatives distribute by Leibniz, preserving total weight.

Global bit parity acts by(-1)^k, not generally(-1)^n. Since bit parity is scalar on ice, odd-k terms have zero ice restriction. This alone does NOT justify discarding all odd orders in the ramp.

In the native edge-bit basis D and every A_e are real. The charge average merely deletes unequal-energy entries and Gamma divides by their real energy differences. Thus a term with derivative weight l is i^l times a real matrix. For real profile data each joint-(k,l) component of the effective generator is Hermitian. One may formalize this separation by multiplying every derivative term by an independent real bookkeeping parameter: Hermiticity holds at all values, so its coefficients are Hermitian separately.

A two-V ice return uses the SAME edge twice. Two distinct edges cannot form a balanced changed-edge set on a simple graph; at an endpoint of their union a changed edge would leave a nonzero degree increment. In particular two distinct ice strings cannot differ on only two edges. Resolvents, D averaging and profile derivatives insert only diagonal factors, so they do not alter this conclusion. Every two-V ice matrix element is therefore diagonal. With odd l it is also purely imaginary and Hermitian, hence zero.

It follows that K1|P=0; K2|P is the usual scalar -f² sum b_e²/2; and K3|P=0. At order 3 the only even-k case is k=2, l=1, eliminated by the preceding reality argument. No static epsilon-parity assumption was used.

## Order four, including the derivative scalar

The k=4, l=0 contribution is precisely f^4 times the static fourth coefficient in the same homological gauge. The only other even-k contribution has k=2, l=2. Both flips use one edge; on ice its intermediate energy is always2 and A_e²=I. Its diagonal coefficient is independent of the ice background, so it is scalar even before computing its value.

For completeness, the exact coefficient can be obtained on the corresponding two-level problem D=I-Z, V=X. Write S=i a.sigma. Then

 exp(ad_S)h.sigma has vector exp(-2a cross)h,
 i epsilon (partial exp S)exp(-S) has vector
 -epsilon sum_{m>=0}(-2a cross)^m a'/(m+1)!.

The first coefficients are a1=(0,-f/2,0), a2=(f'/4,0,0). The arbitrary-profile recursion through 4 gives the lower-energy diagonal coefficients

\[ K_1=0,\quad K_2=-f^2/2,\quad K_3=0,\quad K_4=(f^4+ff^{\prime\prime})/8. \]

The single-derivative generator is explicitly nonzero; this is an adverse witness against using static grading. Restoring the edge coefficient gives the universal k=2, l=2 scalar (f f''/8) sum b_e². No claim is made that the derivative scalar vanishes; only its effect on density-matrix evolution does.

Thus, with the parent's static fourth scalar c4 and ring J4,

\[ K_4(\sigma)|_P=f(\sigma)^4(J_4|_P+c_4I_P)+\frac{f(\sigma)f^{\prime\prime}(\sigma)}8\sum_e b_e^2 I_P. \]

The same-edge reduction is legitimate on the full carrier because the two-step history has only that single D2 intermediate state. It does not replace arbitrary higher paths by two-level dynamics. Four-V histories include the actual native signs and extent-four winding terms already fixed by the static parent.

## A slow local ramp extension

Let the effective ramp generator be D+sum_{j<=14}epsilon^jK_j(sigma). Define instead on the full carrier

\[ L_{\mathrm{ramp}}(\sigma)=\epsilon^4 f(\sigma)^4J_4+\sum_{j=5}^{14}\epsilon^jK_j(\sigma). \]

Every term conserves D and is local in the same strong-support norm. Its restriction to ice differs from the effective ramp generator only by scalar terms, including D=0. Its local norm is bounded by C epsilon4 uniformly on the fixed compact profile interval and independently of volume. We deliberately retain order 5 and all higher coefficients: time derivatives invalidate a blanket odd-order deletion. No globally admissible-pattern compression or extra preparation map is needed.

Let W_r be the time-ordered evolution of this slow extension over0<=u<=epsilon^-1. For an initial ice density matrix, W_r rho0 W_r† is exactly rho1; the dropped terms change only an overall phase. This identity is for ice density matrices, not equality of the two Hamiltonians on excited states.

## Propagating the initial-state correction through the ring observation

For a final dressed-frame local observable O_X and fixed ring time tau, set O_tau=exp(i tau J4)O_X exp(-i tau J4). The ring interaction strength and tau are independent of epsilon in these rescaled variables. Its capped Lieb-Robinson commutator sum obeys

 sum_S ||[(L_ramp)_S(sigma),O_tau]||
       <= C_X ||O_X|| epsilon4 (1+B|tau|)^3.

Differentiate W_r(u)† O_tau W_r(u). The outer time-ordered unitaries preserve norm, so integrating this bound over the dimensionless ramp duration epsilon^-1 yields

\[ |\operatorname{Tr}[(\rho_1-\rho_0)O_\tau]|\leq C_X\|O_X\|\epsilon^3(1+B|\tau|)^3. \]

There is no fast epsilon-speed light cone in this comparison: both density matrices are first restricted to ice and evolved by the explicitly slow local extension. The fast cone affecting the ORIGINAL physical ramp error was already fully priced in the source theorem and is not dropped. This estimate also does not assume a small global norm of rho1-rho0.

Combining the existing O_tau(epsilon²) physical ramp-plus-hold error with this additional O_tau(epsilon³) term proves a natural-ring expectation target with rho0 itself. The final laboratory observable remains Y14†O_XY14. For a bare local final observable the previously established O(epsilon) dressing cost remains; the initial-state improvement does not remove it.


## Evidence, provenance and remaining imports

The live standard-library runner checks 18,626 exact predicates: arbitrary-profile sparse Fraction jets through order four, normalized beta14 endpoint flatness, time exponents and literal full-L4 two-edge supports. Three actual isolated `-OO` mutants fail: reversed moving-frame sign, omitted derivative terms and deletion of the derivative-driven second generator. All are tested against the correct transformed generator. No blanket odd-order deletion mutant is claimed discriminating where the tested coefficient vanishes. Finite controls support, but do not replace, the local analytical proof.

Complete original root and independent ramp proofs, original extension, original SymPy evidence, source-bound reviews and raw failures are preserved in the [durable packet](../.claude/science/physics-loops/native-same-hamiltonian-ramp-20260908/REVIEW_HISTORY.md). The standard-library port changes representation, not the arbitrary-profile mathematical target. No third-party PDF is vendored.

Time-dependent local frame methods are standard. Ho and Abanin, [primary paper](https://arxiv.org/abs/1611.05024), provide contextual prior art on slowly ramped Floquet systems; their theorem is not imported to establish this result. The root research record reports reading Sections I–II.B (PDF pages 1–4). This port does not assert a new full-paper reading or historical novelty.

The Hamiltonian, common-coupling control, schedule, initial ice state and final dressed readout remain supplied. The moving frame is an analytical device rather than an additional preparation operation. Nothing here selects couplings, an occurrence law, physical time, a ground state, a Coulomb phase or an electromagnetic interpretation.

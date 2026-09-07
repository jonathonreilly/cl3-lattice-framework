# Independent derivation: fixed safe cap, finite retained ladder

Derived directly from the root proposal before reading the primary SAFE_CAP memo. This is the COMPLETE fixed-head Record law, not occupation feedback. All error quantities below are trace norms, not conventional half trace distances.

## Domain and exact process

Take an arbitrary matter/reference density matrix in a definite initial legal native code, head and fuel/old-Record sector, tensored with the fixed normalized real sine battery packet beta(E)=sqrt(2/w) sin(pi(E-b)/w) on [b,b+w]. Classical mixtures of these source sectors can also be handled when they satisfy the same support premises. No coherent superposition of different head/history rate sectors is needed or claimed. Reference dimension is arbitrary and all operators act trivially on it.

For the whole cube with Delta=t=1, each source A_s=H_s+q_s I obeys 0<=A_s<=24 I. The initial battery [48,49] therefore gives total Q support [48,73]. Exact energy-intertwining dynamics preserves that distribution; because every surviving A_s is in [0,24], all exact-flow battery support is in [24,73], inside cap [0,97]. Exact refusal is zero on that invariant domain. The exact process and its full-line version consequently agree for this initial state, including its retained battery and reference. This support argument does not require a stationary matter input.

## Rounded isometry and one refusal

Round the FULL source and target spectral energies to the nearest delta multiple, A_s^delta=f_delta(A_s), so ||A_s-A_s^delta||<=delta/2. On the full line define the complete sign column W_e^delta by integer translations of the battery, equivalently fibers exp(-i tau A_out^delta) K_e exp(i tau A_in^delta). The column is an isometry, as is its unrounded counterpart V_e. The Duhamel inequality for the two exponentials gives fiber column norm ||V_e(tau)-W_e^delta(tau)||<=delta |tau|. This uses whole sign columns and completeness, and requires no termwise matrix-element absolute-value estimate.

Let P be the battery cap, C_e=P_out W_e^delta P_in and F_e=(I-C_e^dagger C_e)^(1/2), mapping into ONE orthogonal absorbing copy of the source. For a normalized exact-flow source state rho with V_e rho supported in P_out, put alpha_e^2=Tr[(V_e-W_e^delta)^dagger(V_e-W_e^delta)rho]. Projection contracts the accepted difference, and
 Tr(F_e^2 rho)=||(I-P_out)W_e^delta rho^(1/2)||_2^2 <=alpha_e^2.
Thus the completed column U_e=(C_e,F_e) differs from the exact column (V_e,0), on this state, in squared Hilbert-Schmidt norm at most 2 alpha_e^2. Both completed columns are isometries. Their output trace-norm difference is at most 2 sqrt(2) alpha_e, by purification and trace-norm contraction. Dephasing distinct jump/sign/refusal labels can only reduce this estimate. It is not necessary to claim that F_e itself is small in operator norm on all capped inputs.

Both exact and approximate completed edge channels have effect I on their legal source block. Therefore their GKSL anticommutators agree there; the generator difference is only the recycling difference. For subnormalized rho_s of trace p_s, the bound is 2 sqrt(2) gamma sqrt(p_s) alpha_se, where alpha_se^2 uses rho_s without normalization. Sum over at most D legal live incident edges per source and apply Cauchy-Schwarz: the total bound is 2 sqrt(2) Lambda delta sqrt(E_t[tau^2]), with Lambda=gamma D. The construction makes a finite/capped CPTP semigroup even outside the exact safe subset. No scalar Poisson uniformization on coherent source-sector inputs is used.

## Exact Fourier moment and finite-time bound

For the exact full-line COMPLETE law, tracing matter/head/history/reference at equal Fourier argument cancels each sign-complete jump gain against its loss. Free EB translates tau, while the system Hamiltonian only rotates the traced fiber. Hence p_t(tau)=p_0(tau-t), up to the harmless opposite Fourier-sign convention. Plancherel gives integral tau^2 p_0(tau) d tau=||beta'||_2^2=pi^2/w^2 and integral tau p_0(tau) d tau=0 because beta is real. Therefore E_t[tau^2]=pi^2/w^2+t^2 exactly. This statement is used ONLY for the exact safe flow, never for the rounded/capped approximation.

Duhamel between the two capped CPTP semigroups, evaluated on the exact flow, gives a retained-output error at most
 2 sqrt(2) Lambda delta integral_0^T sqrt(pi^2/w^2+s^2) ds
 <=2 sqrt(2) Lambda delta T sqrt(pi^2/w^2+T^2).
This comparison does not project or truncate the initial Fourier distribution, restart a product battery after events, or assume the approximate flow stays globally Q-safe. The exact-flow energy support is the reason the zero exact refusal premise holds at every Duhamel time.

## Cell restriction and free evolution

Choose M integer and delta=C/M. The positive cells [j delta,(j+1)delta] exactly partition the unchanged cap, and their normalized indicator functions span an M-dimensional reducing subspace for the integer translations after cap compression. Since each C_e and its adjoint preserve this subspace, C_e^dagger C_e and its square-root refusal do as well. Rounded EB^delta, constant at (j+1/2)delta on each cell, also preserves it. Original system A acts only on matter and preserves it. Thus the capped auxiliary process becomes a literal finite ladder after replacing EB by EB^delta; no fractional last cell is permitted.

The bounded free difference ||EB-EB^delta||<=delta/2 produces at most delta T trace-norm error. One-dimensional cell Poincare gives ||beta-P_cell beta||<=delta/w; normalizing that projection changes the initial pure state by trace norm exactly 2||beta-P_cell beta||, hence at most 2delta/w. CPTP contraction propagates this preparation error without amplification. The total retained error is consequently
 epsilon_T <= min(2, delta [2/w+T+2 sqrt(2) Lambda T sqrt(pi^2/w^2+T^2)]).
This is a fixed-product-battery, arbitrary matter/reference estimate, rather than an unrestricted battery-input diamond norm. It is uniform over the stated matter/reference inputs.

## Energy and rational certificate

The rounded lift and its cap/refusal completion commute with A^delta+EB^delta. ORIGINAL free A+EB^delta commutes with this rounded energy because [A,f_delta(A)]=0 blockwise. Therefore rounded total-energy distribution remains invariant while retaining original free A. No equality A=A^delta is needed. This argument fails in general if A^delta rounds a different locally truncated Hamiltonian while free evolution uses global A.

Across original and rounded modeled total energies, operator difference is at most delta. Exact rounded conservation bounds original modeled mean drift between the finite process's own endpoints by 2delta. The original-versus-projected preparation mean bound delta+2delta^2/w then gives the conservative target-relative mean discrepancy 3delta+2delta^2/w. Refusal copies must carry the same paired source A and A^delta. This mean estimate is separate from, and does not assert, exact original energy-distribution conservation.

For w=T=1, Lambda=3, delta=1/320, C=97, M=31040, use sqrt(pi^2+1)<10/3 and sqrt(2)<10/7. Then
 epsilon_T < (3+200/7)/320 =221/2240 <1/10,
 energy-mean error <=3/320+2/320^2=481/51200<1/100.
The bounds are conservative and consistent with trace NORM convention. Since 31040<32768, 15 battery storage qubits suffice. A native 12-edge-qubit +12-fuel-qubit +8-one-hot-head-qubit representation, plus these 15 and one absorbing-flag qubit, gives 48 storage qubits. This is an explicit finite-dimensional encoding/count with unused states, not a simulation of 48 qubits, not a locality-preserving implementation of spectral rounding, not a local bath, and not a finite closed unitary dilation for indefinite Markov time.

Verdict: the proposed safe-cap argument and rational certificate are valid on the stated definite-sector/classical-sector domain. It avoids the previous Poisson coherent-sector obstruction and the sufficient repeated-cap leakage floor. It supplies no occupation-feedback extension.

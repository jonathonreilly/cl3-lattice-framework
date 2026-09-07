# Control-support and energy-domain discrimination for one native accepted transition

Scratch source draft,2026-09-07. Proposed bounded theorem, audit unset. All tensor/control typing, roles, Hamiltonians and pulse timing remain supplied. The parent finite-collision construction leaves implementation of its globally spectral couplings open. This note resolves a small necessary state-transfer test under four separately specified control families; it does not implement the complete instrument or derive an admissible gate set.

## Common native fixture and target

The active odd two-vertex carrier has B_v=Z_x, B_w=-Z_x, A_vw=X_x and h_vw=Y_x. It has an explicit native-square boundary realization: retain edge01 and fix old edge Records Z12=-1,Z23=+1,Z03=+1. Then the spectators have n2=1,n3=0, full N=2 and active N=1. This supplies a concrete native reduction, not an arbitrary replacement matter qubit.

The reduced nine-qubit order is r,hv,hw,x,f,b0,b1,l0,l1. The extra fixed old-Record sentinel r is not a simulation of all three square boundary Records. The supplied line coordinates(j,0,0) used for the path comparison are a new reduced register placement, NOT the original square's physical placement. Complete-graph controls below do not establish nearest-neighbor success on that line.

Let n_j=(I-Z_j)/2, q=n_f, and

K=q(I+Y_x)+I/2+n_b0+2n_b1.

The battery energies are1/2,3/2,5/2,7/2. Head strings are hv hw; battery strings are b1 b0; label strings are l0 l1. Source and normalized target are

s=|r0,head10,Y+,f1,battery00,label00>,
t=|r0,head01,Z+,f0,battery10,label01>.

Both have K=5/2. For Pi_±=(I±Y_x)/2, P_z=(I+zZ_x)/2, the actual accepted native branch has battery factor P_z Pi_+ T_2+P_z Pi_- I, together with fuel lowering/head movement and the corresponding output label. T_2 raises by two cells and vanishes at the upper boundary. Therefore the accepted-plus source-target matrix element has modulus1/sqrt(2). A unitary mapping s to the NORMALIZED t does not reproduce this probability, the other sign, the refusal, or coherent action on arbitrary inputs.

## 1. Original workspace-preserving obstruction

The original declared P_legal contains fuel-one source/refusal strings (head10,label00/11) and fuel-zero accepted strings (head01,label01/10), with arbitrary edge/battery workspace. These strings differ in fuel, both head bits and at least one label bit: Hamming distance at least four.

For EVERY Hamiltonian that is a sum of Pauli words of weight at most two, its direct block P_A H P_S vanishes. If additionally [H,P_legal]=0, its restricted action is block diagonal between source/refusal and accepted blocks. Consequently every concatenated or time-dependent allowed unitary preserves the source/refusal subspace and cannot transfer s to t. This proof does not need energy conservation or a Lie-rank calculation. It applies even on the complete graph. It is a workspace/encoding obstruction only; leaving P_legal during intermediate pulses removes its premise.

## 2. Expanded workspace, globally energy-commuting two-site controls

The separately preregistered supplement drops P_legal preservation. Require instead every control SUM H to obey [H,K]=[H,Z_r]=[H,N_head]=0, with Pauli weight at most two. Cancellation among summands is allowed. Exact rational Pauli elimination gives:

| Graph/support | Columns | Rank | Nullity |
|---|---:|---:|---:|
| Complete, at most two |352|258|94|
| Supplied path, at most two |100|60|40|
| Complete, exactly two |324|248|76|
| Supplied path, exactly two |72|50|22|

Every basis generator also commutes with Q_active=q(I+Y_x). Since the computed basis spans the full constrained real Hamiltonian space, every allowed H preserves that charge, and so do its Lie algebra, arbitrary time-dependent schedules and products of exponentials. Source charge2 and target charge0 preclude transfer. Fuel alone is not invariant: X_f(I-Y_x) is an allowed cancellation control even though X_f separately is forbidden.

The independent analytic explanation uses the Y_x energy basis. The low battery bit's unit gap cannot be compensated by any single other site. A high-bit exchange with x or f could resonate in one spectator sector, but its coefficient would need dependence on the third site; global conservation in the other spectator sector forces that two-site amplitude to vanish. Thus battery energy and Q_active cannot exchange through this control class.

Adding any finite number of zero-energy spectator ancillas with K extended by identity does not change that argument. A battery flip paired with a zero-energy ancilla is nonresonant, while the necessary x/f spectator conditioning still requires a third site. Hence the same Q_active invariant holds for globally commuting at-most-two-site controls on the enlarged complete graph. This is not an optimal ancillary-resource theorem: energetic mediators, changed encodings/energy functions, higher-support couplings and state-specific conservation have different premises.

## 3. Global energy-conserving three-site transfer

On the expanded workspace and complete graph, allow support at most three. Define Pi=(I+Y_x)/2 and T=|0><1|_f tensor|1><0|_b1. Apply these supplied pulses:

1. H1=Pi(T+T†), duration pi/2;
2. H2=(1-q)X_x, duration pi/4;
3. H3=(X_hv X_hw+Y_hv Y_hw)/2, duration pi/2;
4. H4=X_l1, duration pi/2.

Each full Hamiltonian commutes with K,Z_r,N_head. The first is genuinely three-site: it converts Y+,f1,b00 to -i Y+,f0,b10. The second maps Y+ to Z+ with no added scalar phase. Head swap and label flip each add -i. Thus the final state is i t. Exact polynomial exponential identities (H1^3=H1, H3^3=H3 and the projector square for H2) establish the transfer without endpoint-only numerical inference. Removing the Y projector from H1 fails global energy conservation. This establishes conditional state transfer with higher support, not a whole-instrument synthesis or success on the fixed path graph.

## 4. State-specific two-site transfer preserving the full energy distribution

The next, separately preregistered family changes the conservation quantifier: K need only be preserved on the evolving occupied subspace of the fixed source. It uses complete-graph at-most-two-site controls and expanded workspace. Put

L_x=|Y-><Y+|=(Z_x-iX_x)/2,
R_b=|1><0|_b1=(X_b1-iY_b1)/2.

The pulses are:

1. G1=L_x R_b+L_x† R_b†=(Z_x X_b1-X_x Y_b1)/2, duration pi/2;
2. G2=X_f(I-Y_x)/2, duration pi/2;
3. G3=(1-q)X_x, signed duration -pi/4;
4. G4=(X_hv X_hw+Y_hv Y_hw)/2, duration pi/2;
5. G5=X_l1, duration pi/2.

G1 commutes with q. On the entire q=1 sector, [G1,K]P_(q=1)=0: it exchanges Y+ battery-high0 with Y- battery-high1, reducing matter/fuel active energy by2 while raising battery energy by2. Hence the FULL energy distribution is conserved for every time during this pulse for the occupied source, not just its endpoint mean. Globally [G1,K] is nonzero in q=0. Its first output is -i|Y-,f1,b10> with the other registers fixed.

All remaining G_j commute with K globally. G2 flips the fuel in the dark Y- sector, adding -i. G3 maps Y- to Z+ with the displayed negative signed duration and no extra scalar phase; equivalently implement -G3 for positive duration pi/4. G4 and G5 each add -i. The four factors of -i yield final state exactly t. Every pulse preserves old Z_r and one-head number. Only the FIRST pulse relaxes global energy commutation; the whole sequence preserves the sharp energy5/2 for all times on this input.

The numerical witness checks45 fractions across the five pulses and obtains target error2.94e-16 and energy-eigenstate residual at most3.51e-16. Those samples are supporting checks, NOT the continuum proof. The all-time statement follows from the exact q-sector commutator identity for G1 and global commutation for the others. Independently, G_j^3=G_j makes each occupied pulse orbit lie in span{psi,G_j psi,G_j^2 psi}; the witness checks that span lies in the K=5/2 eigenspace. The full G1 commutator has Frobenius norm22.627416997969522, while the others vanish.

This is a positive escape from the stronger global-conservation premise, not a contradiction of section2. It does not claim arbitrary-input conservation, autonomous controls, a universal gate set, an axiomatic update law or permanent new Record formation. The label is workspace until a separately supplied decoupling/readout mechanism is specified.

## Evidence and interpretation

Original/supplement obstruction and three-site sources are under /private/tmp/toe-autonomous-primary-20260907/local-control; the original preregistration is preserved at /private/tmp/toe-autonomous-primary-20260907/LOCAL_CONTROL_ATTEMPT.md. The native reviewer independently checks the square boundary reduction and pulse/interface claims. State-specific preregistration, source and raw are under /private/tmp/toe-autonomous-orbital-20260907/state-specific-control; source SHA81e668fa446a0800b96959d026be014e007f5eccf5e75239e891a9370f0a9638. Frozen source, parameters and unsuccessful family claims are not overwritten by later positive constructions.

The common next obligation remains a full accepted/refusal instrument on its declared input class under physically justified controls. These results expose two distinct avoidable constraints—intermediate workspace and global rather than input-domain energy conservation—and supply explicit escapes. They neither prove a universal local-control no-go nor retire the parent collision's clock, preparation, role selection, interaction admissibility or full coherent instrument requirements.

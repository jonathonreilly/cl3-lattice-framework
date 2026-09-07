# Explicit finite-horizon collision apparatus for the rounded finite model

Independent constructive derivation, 2026-09-07. This is a conditional finite-dimensional unitary implementation of a specified generator, not an admission of its couplings by the underlying axioms or a nearest-neighbor construction. No external theorem is needed beyond finite-dimensional matrix exponential series, partial trace, and trace-norm contractivity of channels.

## Hypotheses and energy bookkeeping

Let the finite storage space have dimension D (at most2^48 for the proposed encoding, with the unused battery encoding states assigned a trace-preserving extension). Write the specified rounded model

G(rho)=-i[H,rho]+L(rho),
L(rho)=sum_a J_a rho J_a† - (1/2){R,rho},  R=sum_a J_a†J_a.

Rates are INCLUDED in J_a. Assume R<=Lambda I on an invariant prepared sector and each [H,J_a]=0 on that sector. This H is the modeled rounded TOTAL energy, including fuel and battery, not just matter. A zero-energy refusal copy must carry the matched storage Hamiltonian. If the model has additional Hamiltonian controls not commuting with these jumps, the following Hamiltonian-independent estimate does not apply without a splitting-error term. For the one-head complete law, including its eligibility-matched refusal channels, Lambda=3 gamma is available on the degree-three cube. Do not infer that bound on unrestricted multiple-head encodings. An inert extension outside the invariant sector can be chosen for this conditional implementation, but is itself additional apparatus design.

These hypotheses imply [H,R]=0 and [ad_H,L]=0. Hence e^(TG)=Ad_(e^(-iTH)) e^(TL). Our collisions below commute exactly with H, so the modeled energy distribution, not only its mean, is preserved exactly by the collision part. This says nothing about error relative to the unrounded energy; that is a separate approximation theorem.

## Explicit fresh-ancilla collision

Take an ancilla with orthonormal states |0>,|a> for a=1,...,M, initially |0>. Assign its Hamiltonian zero on this label space. Define

A=sum_a J_a tensor |a><0|,
V=A+A†,
U_h=exp(-i sqrt(h) V),
Phi_h(rho)=Tr_anc[U_h (rho tensor |0><0|) U_h†].

This is an explicit unitary and an exactly CPTP reduced channel for every h, with no identity-refusal approximation or postselection. A maps the vacuum label to the orthogonal label subspace and A^2=0. Consequently ||V||=||A||=sqrt(||R||)<=sqrt(Lambda). The individual labels can be numerous while this coupling norm remains independent of volume under the one-head bound. [H tensor I,V]=0, so each collision conserves every function of the modeled storage total energy. Degenerate ancillas can carry entropy without carrying that modeled energy. Their purity and degeneracy are supplied resources, not free thermodynamic conclusions.

For extra concreteness the Kraus operators are

K_0=cos(sqrt(hR)),
K_a=-i sqrt(h) J_a sinc(sqrt(hR)),  sinc(0)=1.

Their effect sum equals I exactly. These are consequences of the explicit star-coupling exponential, not separately assumed Kraus functions requiring new implementation. The interaction V still contains the full rounded spectral jump matrices J_a. Writing this unitary explicitly does not synthesize them from elementary local gates.

## Elementary diamond-norm error bound

Introduce label parity P=|0><0|-sum_a |a><a|. PVP=-V and the initial ancilla density is invariant under P. Thus the reduced exponential expansion has only even powers of sqrt(h). Its second-order term is precisely hL: tracing -(h/2)[V,[V,rho tensor |0><0|]] yields h sum_a J_a rho J_a†-(h/2){R,rho}.

The completely bounded trace norm of the commutator map with V is at most2||V||; the preparation and partial-trace maps are channels. Therefore, also with an arbitrary reference system,

||Phi_h-I-hL||_diamond
 <= sum_(k>=2) (2 sqrt(h Lambda))^(2k)/(2k)!
 <= (2 sqrt(h Lambda))^4 cosh(2 sqrt(h Lambda))/24.

The CP map rho -> sum J_a rho J_a† has diamond norm ||R||, and the two anticommutator terms together have norm at most||R||. Thus ||L||_diamond<=2Lambda, giving

||e^(hL)-I-hL||_diamond <=2h^2 Lambda^2 exp(2h Lambda).

When h Lambda<=1/4, their sum is less than6 h^2 Lambda^2 (indeed (2/3)cosh(1)+2 exp(1/2)<4.33). Hence

||Phi_h-e^(hL)||_diamond <=6 h^2 Lambda^2.

For n equal fresh collisions with h=T/n, channel contractivity and telescoping give

||Phi_h^n-e^(TL)||_diamond <=6 T^2 Lambda^2/n,
provided n>=4 Lambda T.

Interleaving exact storage free evolution for time h yields the same bound against e^(TG), without a factor involving ||H||, since it commutes with every collision and with L. A sufficient integer choice for target diamond error epsilon is

n=ceil(max(4 Lambda T,6 T^2 Lambda^2/epsilon)).

For Lambda=3, T=1, epsilon=.01, n=5400 is sufficient. This is a conservative analytic upper bound, not a numerical optimum. If trace distance means half the trace norm, its error is at most epsilon/2. Errors from the finite ladder, locality truncation, numerical synthesis or state preparation must be budgeted separately, rather than spending the same epsilon repeatedly.

## Ancilla, coupling and clock costs

Each collision consumes one fresh (M+1)-level ancilla; b=ceil(log2(M+1)) physical qubits suffice per ancilla, with unused states inert. A closed finite-horizon dilation keeps all n ancillas, so an explicit storage upper bound is48+n b qubits, before clock/controller/coupling hardware. Tracing old ancillas is an analysis operation; keeping them and never recoupling gives the same reduced channel. Reset-and-reuse would require an additional entropy sink and is not the same closed finite inventory.

For the cube, use the direct label upper bound:24 oriented edge labels times (two success signs plus one refusal)=72 labels, so M<=72 and b<=7. This is an upper bound for that explicit complete-law labeling, not a minimal Kraus rank. On that convention the epsilon=.01 illustration uses at most48+5400*7=37848 storage-plus-fresh-ancilla qubits. If the actual runner uses different labels, count its J_a explicitly and substitute M. This construction does not claim a head-routed constant ancilla alphabet on a lattice family: global labels generally grow with volume even though Lambda does not.

During a physical collision lasting h, the required interaction Hamiltonian is V/sqrt(h), of norm at most sqrt(Lambda/h). Thus the fixed-duration horizon scheme has increasing coupling strength as accuracy improves. If instead interaction strength is bounded by g_max, a uniform sufficient pulse duration is sqrt(h Lambda)/g_max (the exact minimum duration within this fixed-generator implementation is sqrt(h)||V||/g_max), and the physical implementation duration need not equal the target modeled horizon T. Fast switching and accurate pulse areas are supplied controls. One cannot silently retain fixed coupling strength, fixed laboratory horizon and arbitrarily small h simultaneously.

The protocol assumes a clock or externally scheduled switches that introduce a fresh ancilla, apply the pulse, and permanently decouple it. It replaces an abstract infinite GKSL bath by a finite stream over fixed T, but does not remove the clock/controller, preparation resource, globally spectral jump couplings, or the need to prevent old-ancilla recollisions. No statement of exact irreversible semigroup dynamics for all times follows from this finite unitary apparatus. It is not an effective full-TOE physical realization, an autonomous local reservoir, or a proof of axiomatic admissibility.

## Extension: actual original free evolution, rounded conserved energy

This section supersedes the commuting-free hypothesis when applying the construction to the ACTUAL safe-cap target. Keep two distinct operators:

K=A_delta+E_B,delta  (conserved rounded energy),
F=A+E_B,delta        (actual original free Hamiltonian).

Assume [F,K]=0, [K,J_a]=0 and ||D||<=delta/2 for D=F-K=A-A_delta. The latter operator-norm rounding bound must hold on the finite invariant sector being implemented. It is not a bound obtained by separately rounding an extensive sum without controlling its total error. Generally [F,J_a] is nonzero. We therefore do NOT replace F by K or commute the actual free channel through the dissipative channel.

Let X=-i ad_F and L be the same rounded-jump dissipator. Since ad_K commutes with L,

[X,L]=[-i ad_D,L].

Using ||ad_D||_diamond<=2||D||<=delta and ||L||_diamond<=2Lambda gives

||[X,L]||_diamond<=2||ad_D||_diamond||L||_diamond<=4delta Lambda.

All operators and superoperators here act on finite-dimensional spaces. There are no unbounded-domain qualifications hidden in this calculation. The large norm of F is absent from the bound because its exactly conserved K part drops out of the commutator.

For completeness, write C_s=e^(sX), B_s=e^(sL), and S_s=e^(s(X+L)). Differentiating S_(h-s) C_s B_s gives

S_(h-s) (C_s L-L C_s) B_s.

The commutator identity

C_s L-L C_s = integral_0^s C_(s-r) [X,L] C_r dr

and contractivity of all these positive-time channels imply

||C_h B_h-S_h||_diamond <= (h^2/2)||[X,L]||_diamond
 <=2delta Lambda h^2.

This proves the stated orientation: the density operator first undergoes the dissipative/collision step and then the actual free step. Reversing the two steps gives the same norm estimate, but the product must be used consistently. No inverse dissipative map is used.

Replace B_h by the explicit collision Phi_h from above and use channel contractivity again. For hLambda<=1/4,

||C_h Phi_h-e^(h(X+L))||_diamond
 <=(6Lambda^2+2delta Lambda)h^2.

Telescoping n identical fresh-ancilla steps, h=T/n, gives

||(C_h Phi_h)^n-e^(T(X+L))||_diamond
 <=(6Lambda^2+2delta Lambda)T^2/n.

There is no additional delta T phase-replacement charge because F is kept exactly. Both C_h and the joint collision commute with K, so each finite collision step conserves the full rounded-energy distribution exactly, even though C_h and Phi_h generally do not commute with each other. This is the rounded-energy statement, not exact conservation of the unrounded F under the jumps.

At delta=1/320, Lambda=3, T=1 and collision diamond budget epsilon=.01, the sufficient count is

n=ceil(max(12,(54+3/160)/.01))=ceil(5401.875)=5402.

With the same explicit complete-law label budget of at most72 labels and7 qubits per fresh ancilla, storage plus fresh-ancilla inventory is48+7*5402=37862 qubits. Clock, coupling implementation, state preparation and reset apparatus remain excluded. This collision error adds to the independently certified finite-battery comparison error; it does not retroactively consume or remove that separate approximation budget. The fixed-horizon coupling-strength and supplied-control qualifications above remain in force.

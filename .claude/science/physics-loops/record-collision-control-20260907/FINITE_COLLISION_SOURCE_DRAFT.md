# Finite-horizon unitary collision apparatus for the rounded complete Record model

Draft only,2026-09-07. Proposed bounded theorem; independent audit status unset. This source supplies a conditional finite-time replacement for the abstract GKSL reservoir. It does not derive a Record formation law, a clock, native role selection or a physically admissible local interaction set.

## Result and scope

For the finite positive-battery complete cube model, retain its ACTUAL free Hamiltonian F=A+EB_delta and its rounded conserved energy K=A_delta+EB_delta. A finite sequence of explicit unitary collisions with fresh finite ancillas approximates its retained channel through fixed modeled time T with diamond error at most

(6Lambda^2+2delta Lambda)T^2/n,

provided n>=4Lambda T. Every collision and actual free step exactly conserve K. At delta=1/320, Lambda=3, T=1, n=5402 yields collision error strictly below1/100. A direct72-channel label encoding uses7 fresh ancillary qubits per collision, giving48+7*5402=37862 storage-plus-fresh-ancilla qubits.

The collision error is DISTINCT from the finite-battery approximation error below221/2240. By triangle inequality the combined retained-channel trace-norm bound against the original continuous-battery input map is below221/2240+1/100=1217/11200, about0.10866. It is not below0.1 merely because each separate construction meets its own budget. The finite-battery comparison retains its fixed initial legal sector/fixed battery input domain; adding a diamond collision estimate does not enlarge that domain.

The48 storage registers, collision ancillas, pure input preparations, globally spectral jump matrices, clock and pulse controls are supplied. No48-qubit dynamics simulation, nearest-neighbor synthesis or exact irreversible semigroup for arbitrarily long times is claimed.

## Finite model and exact energy premise

Write L(rho)=sum_a J_a rho J_a†-(1/2){R,rho}, R=sum_a J_a†J_a. J_a includes its square-root rate and all accepted native signs and eligibility-matched absorbing refusal channels. On the invariant prepared one-head sector R<=Lambda I. For the complete cube Lambda=3gamma. The bound is not asserted on unrestricted multiple-head states; unused battery encodings may be extended inertly and trace preservingly.

The whole-cube spectral rounding gives [F,K]=0, [K,J_a]=0 and ||F-K||<=delta/2. Refusal uses a zero-energy FLAG with matched source storage Hamiltonian, not zero Hamiltonian for every refusal storage state. Generally [F,J_a] is nonzero. Rounding only the conserved operator does not replace the original free A by A_delta.

## Explicit collision and error proof

For an ancilla basis |0>,|a>, a=1,...,M, initially |0>, define

B=sum_a J_a tensor|a><0|, V=B+B†,
U_h=exp(-i sqrt(h)V),
Phi_h(rho)=Tr_anc U_h(rho tensor|0><0|)U_h†.

All ancillary label energies are zero. B^2=0 and ||V||^2=||R||<=Lambda. Thus [K tensor I,V]=0 and Phi_h preserves every bounded function of K exactly. Its Kraus operators are cos(sqrt(hR)) and -i sqrt(h)J_a sinc(sqrt(hR)), with sinc(0)=1. The complete reduced channel is exactly CPTP, without postselection.

Ancilla vacuum/nonvacuum parity sends V to -V and leaves the prepared density invariant. Hence all odd powers of sqrt(h) vanish after the partial trace, while the second-order term is hL. With arbitrary reference entanglement, preparation and trace are channels and ||ad_V||_diamond<=2||V||. Consequently

||Phi_h-I-hL||_diamond <=(2sqrt(hLambda))^4 cosh(2sqrt(hLambda))/24.

Also ||L||_diamond<=2Lambda, so

||exp(hL)-I-hL||_diamond<=2h^2Lambda^2 exp(2hLambda).

For hLambda<=1/4 their sum is below6h^2Lambda^2. No extensive Hamiltonian norm appears.

For the actual free generator X=-i ad_F, let D=F-K. Since ad_K commutes with L,

||[X,L]||_diamond=||[-i ad_D,L]||_diamond<=4delta Lambda.

All spaces are finite dimensional. Differentiating exp((h-s)(X+L)) exp(sX) exp(sL), and using

[exp(sX),L]=integral_0^s exp((s-r)X)[X,L]exp(rX)dr,

gives a positive-time channel Duhamel bound

||exp(hX)exp(hL)-exp(h(X+L))||_diamond<=2delta Lambda h^2.

Replacing exp(hL) by Phi_h and telescoping n CPTP steps at h=T/n proves the result. Each step is collision followed by actual free evolution. No commutation of F with the jumps is assumed, no inverse dissipative map is used, and no delta T phase-substitution error is paid.

## Finite apparatus inventory and excluded costs

There are at most24 oriented cube-edge labels, with two accepted signs and one refusal for each: M<=72 nonvacuum labels. Vacuum plus these labels fit in7 qubits. Unused ancillary labels can be inert. Keeping n fresh ancillas without recoupling exactly realizes the repeated reduced channel; tracing them is an analysis operation. Reset-and-reuse requires a separate entropy sink.

During a pulse of duration h the interaction V/sqrt(h) has norm at most sqrt(Lambda/h). At bounded prescribed strength g_max, this direct construction can instead use duration sqrt(hLambda)/g_max per pulse; physical runtime then need not equal modeled T. A finite clock/switch sequence, pulse precision, pure ancilla supply, spatial routing and globally spectral J_a implementation remain supplied. Finite ancillary storage is not an infinite-time Markov reservoir, and energy-degenerate entropy storage is not a free thermodynamic resource. The unitary construction preserves modeled rounded energy; it does not by itself supply a new original-energy mean comparison beyond separately reviewed bounded-energy estimates.

## Independent native witnesses and preregistration history

The original preregistered native square/N2 fixture uses opposite dimers of weights1 and sqrt(2)/3, three positive battery cells with spacing1/cap3, and deletion of edge01. It retains both signs and one refusal, with source/output/refusal system dimension72 and an explicit288-dimensional collision unitary. At h=.04,.02,.01, its dissipative trace-norm errors are0.000517884302,0.000131390043,0.0000330896571. Refusal is nonzero. Eigh refusal square roots use a disclosed1e-10 numerical-null cutoff; no physical parameter was retuned for that cleanup.

The original fixture DID NOT exercise [F,J]!=0: its measured commutator is about2.47e-15 because the deleted dimer is commensurate while the irrational spectator survives. The attempted nonzero-commutator assertion failed and is preserved, not counted as successful evidence.

A separately preregistered post-inspection supplement changes only the deleted edge to irrational dimer23. It has ||[F,J]||=1/3 while rounded-energy commutation remains at numerical precision. Its explicit-unitary versus full ORIGINAL-free GKSL trace-norm errors at the same h are0.000551093959,0.000139760364,0.0000351907659. These support the expected h^2 local scaling. Both fixtures pass18 matrix assertions with maximum residual5.33e-15. They test one state and one collision at each h, not empirical diamond norms, long-time trajectories, all cube paths or the enlarged resource inventory.

Frozen evidence: native scratch collision/PREREGISTRATION.md, SUPPLEMENT_PREREGISTRATION.md, REVIEW.md, result.json and supplement-result.json under /private/tmp/toe-autonomous-native-ladder-20260907. Original source SHA296f6ac242f7027be7f692af475d973f02fcbaa497e3b83c0849af09c53e8c53; supplement SHA8948b4d41764cfe554fe5ec97665571423809591fea192dd726900c15733ab66. Their native carrier is an imported frozen independent module; the witness is independent of this proof, not an independent reconstruction of the carrier.

## Exact-rational certificate and primary checks

With rational arithmetic only:

- c=6*3^2+2*(1/320)*3=8643/160;
- c/(1/100)=8643/ (160/100)=5401.875=43215/8;
- n=ceil(43215/8)=5402 and n>=12;
- hLambda=3/5402<1/4;
- collision upper bound=c/n=8643/864320<1/100, since864300<864320;
- 2^6<73<=2^7; 48+5402*7=37862;
- separate total budget221/2240+1/100=1217/11200.

The portable PRIMARY should independently execute these rational checks, checking constants rather than copying helper output. It should also: (1) verify the label inventory and inert unused-code convention; (2) independently verify the elementary exponential remainder coefficient by a rigorous rational series upper bound (for example cosh(1)<2 and exp(1/2)<2 imply coefficient<16/3<6); (3) live-call the native helper and strictly validate finite/schema/exact fixture/h coverage, source/dependency hashes and resource contract; (4) keep original and supplementary commutator expectations different; (5) reject missing rows, swapped fixture labels, NaN/Inf and changed energy/error fields; (6) label matrix assertions, rational certificates and corruption controls separately. A helper result is supporting matrix evidence, not a substitute for the analytic diamond proof. The primary need not duplicate the native matrix construction to certify these independent mathematical/resource checks.

## Next obligation

Ground one actual collision transition in a specified Record-compatible nearest-neighbor physical update law before assuming universal gate compilation. The registry does not supply an arbitrary gate set. This theorem retires the infinite fresh-bath idealization over fixed T conditionally, while physical coupling admissibility, state/role preparation, clock/control and renewal remain open.

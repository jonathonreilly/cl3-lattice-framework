---
claim_id: native_edge_record_z4_flux_bridge_capacity_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/native_edge_record_z4_flux_single_bridge_check_2026_09_07.py
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
claim_scope: "For explicit native CAR occupation encodings of four Z4 labels, one bridge after quadratic evolution cannot deterministically read the high flux bit on the nine-mode code. A supplied finite controller and selective native hopping on twelve modes form both flux bits in five physical bridge Records. No autonomous control or exact finite-battery compiler is derived."
---

# Native Z4 flux Records: one-event boundary and controlled five-event construction

**Type:** bounded_theorem

The carry-sensitive high flux bit cannot be read by one Gaussian-preprocessed native bridge on the specified nine-mode code. A larger twelve-mode code and a supplied sixteen-history controller do admit five actual native bridge events whose physical output sites store both flux bits. These are different, explicitly declared instrument domains, so the construction does not contradict the boundary.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [native instrument and energy-ledger parent](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md) supplies the physical edge projector and its bridge/nonbridge interpretation. Native code preparation, ready-input occurrence, control and scheduling remain premises. The result does not derive Wilson weights, a role-label phase compiler, or arbitrary universal gates.

Exact support: [single-bridge checker](../scripts/native_edge_record_z4_flux_single_bridge_check_2026_09_07.py) enumerates256 inputs,36 two-particle states and8 diagonal-sign controls. [Five-event checker](../scripts/native_edge_record_z4_flux_five_event_check_2026_09_07.py) enumerates256 inputs and8 actual physical three-site Pauli actions. These are finite support counts, not counts of all possible Gaussian controls or physical energy tests. The exterior-square argument below supplies the all-unitary quantifier.

## Single-event boundary on the nine-mode encoding

This is a bounded encoding-specific result, not a general compiler no-go. The generic Toffoli/modular-addition route was abandoned before implementation because it would import the gate family being sought. The construction and obstruction below use the actual native CAR/Record instrument.

## Existing native capabilities and the readout contract

`docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md`, definitions(1) and the Nonbridge/Bridge theorem around214–258, gives a physical edge-qubit projector Q_e,z=(I+zZ_e)/2. On a legal nonbridge code P_R Q_e,z P_R=P_R/2. On a bridge it is a signed component occupation-parity projection. Real hopping dwells are number-conserving quadratic CAR evolution; ordinary composition, code preparation, Born/Lueders occurrence and schedule remain supplied conditions.

Therefore an input-independent schedule of legal nonbridge events, with arbitrary intervening code-preserving unitary dwells, has a fair conditional sign at every event. A sign string from such a prefix cannot carry a nonconstant flux value. This does NOT say the post-event matter, apparatus, selected edge or joint correlations are input-independent. Reading them changes the readout contract. The energy-lift statement below is restricted to native signs and an initially independent ready battery.

The old frozen eight-vertex four-fermion cube has only70 matter states; its full fixed-parity CAR code has128. It cannot isometrically encode256 independent four-Z4 boundary labels while all other ready factors are fixed. That is only a dimensional check for that carrier. Extra sites, a different code, or encoding only gauge-equivalence classes are legitimate different tasks. No global capacity bound is claimed.

## Orthogonal native carrier extension and exact low-bit Record

Use a nine-vertex path with eight physical edge qubits. Its cycle-free BKSF even-parity code has dimension2^8=256. Let fermion modes0..3 store a0,b0,c0,d0; modes4..7 store a1,b1,c1,d1; mode8 stores r=(sum first8 bits) mod2. Every boundary label tuple(a,b,c,d) corresponds to a different even occupation basis vector, so this is an actual orthogonal code, not the corrected source's set injection diag(k/A_N,1). Preparing that code state and assigning these port roles are still explicit inputs.

Take Phi=a+b-c-d mod4. Its low bit is a0 xor b0 xor c0 xor d0. Cut the path bridge between modes3 and4. The native bridge-Z observable is exactly the occupation parity of component{0,1,2,3}, with the known old-record sign fixed. Its native Record outcome therefore reads the low flux bit deterministically on every encoded input, and its parity projection is nondemolition on those occupation basis inputs. This is a physical single-edge Record readout after the supplied code preparation. It need not read or alter every individual label Record first. The original labels are encoded in unrecorded native code degrees of freedom; it is not a protocol for moving already permanent site Records.

## Why a single Gaussian-preprocessed bridge cannot read the high bit

Permit any number-conserving quadratic CAR unitary before ONE native bridge readout, a larger class than the actual real nearest-neighbor path controls. The measured component parity has second-quantized one-particle form Gamma(D), D=I-2P_component. After such a dwell it is Gamma(R), R=V* D V, a Hermitian unitary reflection on the nine-dimensional one-particle space. Allow an overall known sign eta from old Records and outcome naming.

Suppose this one-shot measurement deterministically outputs the high bit of Phi on every one of the256 orthogonal even-parity inputs. Determinism for a Hermitian involution implies each such basis state is an eigenvector with the required sign. The vacuum has high bit0, so eta=+1, since Gamma(R) fixes the vacuum. In particular the entire two-particle sector is diagonal under Lambda²R: every one of its36 coordinate basis vectors is one of the encoded inputs.

If Lambda²R is diagonal in the coordinate wedge basis and R is invertible, R preserves every coordinate two-plane. Indeed a nonzero decomposable wedge determines its spanning two-plane. Intersect the planes span(e_i,e_j) over j!=i to conclude that R preserves each coordinate line. Thus R itself is diagonal. Because R is a Hermitian unitary, its diagonal entries r_i are±1. The eigenvalues on pairs must therefore be r_i r_j, and the product around any three-index triangle is+1.

The actual high-flux-bit table violates this. For occupied pairs(0,1),(0,2),(1,2), with all high modes and reference empty, the labels are respectively(a,b,c,d)=(1,1,0,0),(1,0,1,0),(0,1,1,0). Their fluxes are2,0,0, so high-bit signs are(-1,+1,+1), with product-1. Contradiction.

This proves a narrowly stated impossibility: on this explicit orthogonal native encoding, no single native bridge Record preceded by arbitrary number-conserving quadratic CAR evolution can deterministically read the high flux bit for every input. It is not an assumption that all parity processes are affine; it follows from the exterior-square matrix action and Hermitian reflection constraint. The complete finite truth table in result.json checks256 labels, all36 two-particle states, the low-bit identity and this exact three-sign witness.

## Energy-lift qualification

For the full-line energy lift of an ideal native branch, Fourier battery coordinate tau gives the branch column e^-iAout tau K_z e^iAin tau. Its squared effect is e^-iAin tau K_z* K_z e^iAin tau (orientation of tau is immaterial to the conclusion). On a nonbridge K_z*K_z=I/2, so native sign fairness is preserved exactly, including a retained correlated battery. This does not make other battery/matter observables uninformative.

For a bridge and an initially product ready battery, native sign probabilities are the positive tau-density average of the corresponding ideal parity effects conjugated by the incoming quadratic Hamiltonian. Any deterministic0/1 outcome on a given input forces the ideal effects to have that same value for almost every tau. Since there are only256 tested inputs, their full-measure sets can be intersected. At such a tau the one-shot Gaussian-parity contradiction above applies. Therefore an independent ready battery used only in this standard full-line lift does not evade this deterministic sign-readout obstruction. Scalar fuel energies cancel in the effect. A cap-safe restriction reproducing the full-line instrument on these inputs inherits the statement.

This paragraph does NOT cover input-correlated apparatus preloaded with information, reading battery energy as the answer, cap-refusal-dependent readout, approximation guarantees or arbitrary additional apparatus control. The native theorem itself retains supplied apparatus/control and possible nonlocal spectral-lift implementation. No new local energy-conserving gate family is derived.


## Positive five-event construction on an extended twelve-mode encoding

## Frozen scope and carrier

This follows the separately frozen positive-escape preregistration and original exact checker, executed before its explanatory proof. It is a positive escape from the earlier one-event and direct-two-event obstructions, on a larger prepared carrier with a supplied finite controller. It is not an axiomatic gate compiler, a minimal flux Lüders instrument, or a finite-battery realization.

The CAR path has twelve vertices in the fixed order
(a0,b0,c0,d0,a1,b1,c1,d1,q,qbar,r,anchor).
There are eleven native BKSF physical edge qubits e0,...,e10. Use the even fermion-parity code, dimension 2048. This tree has no cycle stabilizers. In its occupation dictionary the physical bit xj is the prefix parity n0 xor ... xor nj; consequently B0=Z0, Bj=Z(j-1)Zj internally, and B11=Z10. The 256 inputs have arbitrary eight data occupations, q=0, qbar=1, r=parity(data), anchor=1. Thus every input has even total parity, and the physical computational codewords are orthogonal. Preparing the correlated reference r is an input preparation assumption, not supplied by an arbitrary set injection.

Define the four oriented Z4 labels ai=a0+2a1, etc., and flux F=(a+b-c-d) mod4. The boundary labels are prepared occupation data, not already permanent Record signs. All eleven edges start live; their native coefficients and controlled pulse sign are taken in the displayed positive path convention.

## Actual event and pulse instrument

Record e0,e1,e2,e3 in that order with no intervening matter dwell. Their outcomes are the actual physical bits x0,x1,x2,x3 (Z sign (-1)^x). Every selected edge is a bridge. After each deletion its left endpoint has become isolated; after four deletions the low four vertices are isolated and modes4,...,11 still form a path. The native ready-input projectors are Qj,x=(I+(-1)^x Zj)/2. No generic Boolean quantum gate is used.

Let z=(x0,x1,x2,x3). A supplied classical controller with sixteen possible history states reconstructs li=xi xor x(i-1), with x(-1)=0, and computes
  L=(l0+l1-l2-l3) mod4,
  c=x3 xor floor(L/2).
The event schedule/pulse clock is additional supplied control; sixteen counts the stored history, not a complete autonomous controller implementation.

If c=1 apply U=exp[-i(pi/2)T8]; if c=0 apply identity. Then Record e8. Here T8 is the actual native whole hopping term joining adjacent CAR vertices q and qbar. With the path edge ordering,
  A8=X8 Z7, B8=Z7 Z8, B9=Z8 Z9,
  T8=(i/2) A8(B8-B9)=Y8(I-Z7Z9)/2.
This identity was checked on all eight physical three-bit basis states, including its complex phase. On the prepared subspace q xor qbar=1, so Z7Z9=-1 and T8=Y8. Therefore the pulse flips x8 and leaves every other physical bit fixed. Its phase is (-1)^(old x8). It swaps the q,qbar occupations, leaves all eight data occupations fixed, and does not act on any old Record site e0,...,e3. e8 is still a live bridge when recorded. Its removal disconnects the remaining path, so the final Record is permanent under the surviving native hopping terms.

For history z and final bit b the ideal branch map on the prepared carrier is
  M(z,b)=Q8,b U^c Q3,x3 Q2,x2 Q1,x1 Q0,x0.
Sum M(z,b)^*M(z,b)=I on the whole even-code space, since U^c is unitary and each event is a complete projective instrument. An outcome-register isometry is Vpsi=sum_(z,b) M(z,b)psi tensor |z,b>. This is an explicit finite isometry, not a relabeling of observed outcomes as a new physical measurement. The final Q8 is essential.

## Exact truth table and coherence scope

Let H=(a1+b1+c1+d1) mod2. Before the controlled pulse x8=x3 xor H, since q=0. Afterwards
  x8=x3 xor H xor c=H xor floor(L/2).
But F=(L+2(a1+b1-c1-d1)) mod4, whose high bit is exactly H xor floor(L/2). Hence e3 stores F mod2 and e8 stores floor(F/2), both as physical native Z Records. The checker exhausts all 256 labels, verifies every recovered data occupation, every old Record, the pulse guard and phase, and uniqueness of all 256 output physical codewords.

For fixed low history the conditional pulse phase depends only on H and therefore only on the final high Record bit. It does not resolve individual high occupations. Nevertheless the first four Records reveal the low occupations separately: superpositions with equal flux but distinct low data generally decohere when histories are discarded. The claim is nondemolition preservation of the orthogonal input basis and an isometry retaining complete history, not coherent Lüders measurement of flux alone. The output retains data as well as the two flux Record sites; it does not compress 256 states into four states.

## Load-bearing control, locality and energy imports

This is a controlled native instrument sequence. It does not evolve under an unmodified fixed H_R. Generic surviving hopping terms would move the high data and references. Setting the dwell to zero during the first four events, activating only T8 for the conditional pulse, and suspending the pulse interaction for the final sharp event are supplied bond selection and switching assumptions. No prior result is imported as proving that this selective control is available. With selected Hamiltonian g T8, g>0, the active duration is pi/(2g). Its physical Pauli support is the three consecutive edge sites e7,e8,e9, not a two-site physical nearest-neighbor gate. CAR adjacency and bounded whole-hop support are explicit; a two-site bounded-strength hardware synthesis is not proved.

The controller reads four already formed permanent signs and chooses one of two pulse actions. It contains a nonlinear sixteen-entry rule and a timed schedule. This is an explicit finite classical control resource, not a native Toffoli or an autonomous computation derived from the axioms. Initial preparation, ready Record apparatus, prescribed event occurrence and controller coupling are likewise premises.

The ideal selective unitary/projector calculation is not an energy ledger. Switching a Hamiltonian is generally work; the energy change of forming/deleting a Record edge requires its modeled battery apparatus. If a nonzero incoming hopping remains active at the final event, the usual independent-ready normalizable battery lift averages rotated effects and does not inherit this exact sharp truth table. The earlier battery obstruction cannot simply be bypassed by naming the pulse a control. This construction therefore isolates a positive information-processing bridge and identifies selective native hopping plus compatible work/Record apparatus as the remaining physical import. No exact finite-battery success probability or energy-conservation claim is made.


## Proof provenance and remaining import

The single-event proof was frozen at SHA612bf0a75361f0889fe437286bbf36ec587e43a1d7262a4da06933b1029b1d87 and independently reviewed by the native worker. The positive construction was preregistered separately, checked on all256 basis inputs, frozen at SHAe7852a0c4b168df912725a097e64213c72860de8e966f394c7e3769121a0f96b and independently reviewed by root. The original code, raw outputs and unsuccessful direct-two-event route remain preserved in scratch. This cohesive note is a retrospective port, not a new preregistration. The canonical scripts add output/resource metadata without changing those truth tables.

The bridge gained here is a physical output Record on a native orthogonal carrier. The unresolved premise is bond-selective, timed native control with a compatible preparation/work/Record apparatus. The already formed low-sign history feeds a supplied finite controller; its nonlinear rule is not hidden as an axiom-derived quantum gate. No theorem about an autonomous finite closed apparatus or arbitrary coherent flux instrument is claimed.

The [durable packet](../.claude/science/physics-loops/native-flux-record-20260907/PROOF_REVIEW.md) preserves the N1–N8 scope review, original preregistrations, full truth tables, failed routes and independent reviews.

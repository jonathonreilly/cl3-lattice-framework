# Native flux-readout attempt: exact low bit, one-shot high-bit obstruction

Scratch bounded result, not a repository theorem or general compiler no-go. The generic Toffoli/modular-addition route was abandoned before implementation because it would import the gate family being sought. The construction and obstruction below use the actual native CAR/Record instrument.

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

## Remaining constructive target

The hard next positive attempt is a finite sequence of native bridge parity instruments with retained outcomes and a physically specified conditional quadratic evolution, or another explicitly native nonquadratic operation. Intermediate parity projections can create richer states; the one-shot proof does not exclude that. The two-output readout after a low-bit measurement is a separate conditional-sector question and has NOT been reduced to the above all-input argument. Additional prepared native sites may also change the accessible instrument class.

Any successful flux compiler must preserve original logical label information on the declared domain, form two permanent output Records, and list its actual local controls, energy lift, ancillas and schedule. It must not insert a Toffoli gate or a globally evaluated classical flux into the control condition. The present result retires the set-encoding ambiguity for one orthogonal code and gives an exact low-bit bridge readout, while locating a genuine carry-sensitive boundary for the first native one-shot proposal. No new PR is proposed from generic circuit compilation.

## Fresh-main check at e043c95b37

The newly landed `U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md` supplies an actual finite-hop integrated current Jbar=(V*n_head V-n_head)/h and its layerwise local continuity/work interface. It explicitly leaves the phase, hopping coefficient, Hamiltonian supplier and finite field/Record compiler open. Thus it sharpens the current target but does not supply a Record gate for modular flux.

The newer `U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md` genuinely adds a nonquadratic joint matter/link model on a162-dimensional block. Its spin-one U is a hard-cutoff shift with U³=0, not a cyclic Z4 phase-label operator. The source explicitly distinguishes its supplied scalar exp(iA) comparison from that finite operator and leaves the operator-to-phase bridge and Record formation/readout untouched (Result and section1; boundary around303–305 and530–534). Its H_B=-(kappa/2)(U0 U1 U2* U3*+adjoint) is an explicit supplied face Hamiltonian, not a derived native edge-Z compiler. It lies outside the narrow Gaussian-parity obstruction and is a possible different future carrier, but cannot be silently imported as a gate on the current CAR encoding.

Accordingly the priority remains the native conditional bridge-instrument/carry-readout problem, or an explicitly new operator-to-phase/Record bridge for the hard-cutoff quantum-link carrier. Neither fresh source licenses the generic controlled-addition circuit rejected above. The all-input orthogonal encoder here is supplied; it is not yet a local preparation compiler from already-formed corrected-role Records.

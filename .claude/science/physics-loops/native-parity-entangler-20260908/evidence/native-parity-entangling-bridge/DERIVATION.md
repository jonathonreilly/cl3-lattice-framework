# Readable heralded dual-rail entanglement from one native internal Record

## Supplied carrier and exact resource

Use native path0–1–2–3, with three physical edge qubits at the supplied midpoint roles. The full tree carrier is the even four-mode CAR representation. Native B_v=product incidentZ, n_v=(1−B_v)/2, T_ij=iA_ij(B_i−B_j)/2. No cycles, extra reservoir, controlled hopping or onsite phase primitive is introduced. Initial occupation1100 is a single physical computational basis vector and hence a product preparation of the three edge qubits; it is supplied, not selected by the axioms.

Input logical qubitA has rails(0,2),B rails(1,3), with one fermion each. Their four-dimensional encoding is V_in|ab>=the actual native occupation vector with occupied rail a ofA and b ofB, fixing phases in the physical computational basis. Output logical qubits will instead have rails(0,1) and(2,3). This regrouping is essential and explicit: the construction is not a deterministic same-wire two-qubit gate.

## Preparation using only native whole hops

Write U_j(c,s)=I+(c−1)T_j²−isT_j on path edgej. Let S=U_12(0,1), c=1/sqrt2, and define

 G02=S U01(c,c) S†,
 G13=S† U23(c,c) S.

Each is a finite chronological sequence of supplied adjacent whole-hop pulses; inverse full hops are permitted by the supplied signed pulse control. They are rotations on disjoint mode pairs, commute, and preserve each input rail-pair total number. Their product applied to1100 is V_in(1,1,1,1)^T/2 in the actual physical convention. Thus the initial two logical qubits are |+>|+>, prepared through number-conserving native transport before any cut. No independent nonlocal Hamiltonian generator is silently assumed; the displayed conjugations implement it.

## Complete internal parity instrument and output regrouping

The physical middle edge obeys Z12=B0B1=(−1)^(n0+n1). Supply the usual binary Z Record measurement Q_-=(I−Z12)/2 and Q_+=(I+Z12)/2. Both signs are permanent Records and both branches remain in the complete instrument.

In the total-two-particle input domain, the odd branch has exactly one particle in each connected component after cutting12. These two components carry readable output rails(0,1) and(2,3). Let V_out encode those one-particle rails with the same physical occupation-vector convention. Full physical columns satisfy

 Q_- V_in = V_out K,  K=diag(0,1,1,0).

Also V_in†(Q_-+Q_+)V_in=I. The even branch, carrying input00/11, has two particles on one side and zero on the other; it is retained as failure rather than misidentified as two output qubits. The success map works for arbitrary input density matrices and passive references; it is not merely a |++> probability calculation.

For |++>, success probability is1/2 and the normalized output is(|01>+|10>)/sqrt2. Thus an internal native parity measurement supplies a nontrivial heralded entangling map on declared input/output dual-rail encodings. It does not choose when the Record occurs or make either branch unrecorded.

## Coherence remains operationally readable after the cut

T01 andT23 commute with the recorded Z12. Each output component has odd parity and its native two-mode algebra acts on its single-particle dual rail. The Bell state has a surviving product-hop correlation<T01 T23>=−1, whereas its occupation-dephased counterpart has0.

More concretely, no additional phase/readout primitive is needed for a coherence test. Apply the two surviving local rotations R=U23(c,c)U01(c,c), then measure the two outer-edge Z values. The product outcome has expectation

 <R† Z01 Z23 R>=1

for the successful Bell state, versus0 for its dephased mixture. R commutes with the middle Record, and the two final outer-edge measurements are ordinary native Z Records. The test consumes the output qubits at readout as usual, without recrossing the cut. Bare Z01Z23 and this rotated correlation on repeated identically prepared attempts can distinguish Bell coherence from a diagonal mixture; full Bell certification would state its witness assumptions separately.

## What obstacle was overcome and what was not

If the original crossed rail labels were held fixed after cutting12, their individual logical hops would cross the deleted edge and cease to be available. The odd branch instead permits a precise regrouping into one rail pair per surviving component. The heralded quantum channel preserves a four-column input/output specification while this regrouping restores local output readability. The even branch does not have that property and is not recycled without further resources.

The result is a three-physical-qubit native instrument with bounded pulses, explicit product starting state, one permanent internal Record and two optional destructive readouts. It is not a compiler for general interacting dynamics, an autonomous occurrence mechanism, a gauge/matter identification or a selected coupling law. It uses the same supplied Born/Record schedule and whole-hop controls as the native instrument theorem. No unlimited fresh capacity is invoked for one attempt.

check.py independently constructs full8-by8 native Pauli matrices. Fourteen predicates verify full success columns/completeness, independent preparation rotations, success probability, output concurrence, surviving and operational coherence, both permanent outcomes and forbidden middle-edge reuse. No author module or generic Gaussian-circuit oracle is imported. Numerical radicals are evaluated in floating arithmetic at1e-11; displayed algebra gives the finite exact construction. Raw output and source hashes are preserved.

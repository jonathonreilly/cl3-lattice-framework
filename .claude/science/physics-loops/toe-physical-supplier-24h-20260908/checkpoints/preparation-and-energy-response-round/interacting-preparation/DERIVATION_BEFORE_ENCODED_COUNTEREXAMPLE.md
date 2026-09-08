# Interacting preparation: a restricted obstruction and a native escape resource

2026-09-08. Bounded exploratory result, not a canonical theorem or audit. No successful general interacting preparation is claimed.

## Sources and control domain

The phase-preparation DERIVATION.md and path_probe.py in the sibling phase-preparation directory supply a programmed quadratic diagonalization, occupation-difference phases, vacant/filled leaf attenuation, and actual leaf Z Records. Their general target is dGamma(h). Their finite certificate does not include density-density filters. The current main source is docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md, especially its Eq.(6): an actual bridge Z Record measures signed component parity, deletes the selected hopping, and retains its sign in the surviving dictionary. That is a substantially larger measurement menu than single-mode occupation detection.

The source docs/NATIVE_EDGE_RECORD_REDUCED_CELL_CONTROL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-09-07.md additionally analyzes supplied two-/three-site controls on an expanded head/fuel/battery workspace. Its explicitly scoped state-transfer pulses are neither a general admitted gate set nor an established density-density compiler on this matter path. Ordinary M2 algebra contains Pauli operators; that fact alone does not authorize their arbitrary coherent Hamiltonian use while preserving code, Records and energy. The axioms do not select the Hamiltonian, phases, product initialization, Born probabilities or schedule. DEFERRED_DECISIONS keeps Record Statistics parked; this probe does not reopen that selection question.

The restricted class below consists of quadratic number-conserving fermionic unitaries, occupation-product ready ancillas, single-mode occupation measurements with fully resolved classical histories, discards, and finite classical feedforward. It includes the reviewed leaf preparation construction after suitable dictionary changes. It excludes multi-mode component-parity measurements, non-Gaussian ready states, coherent erasure of classical histories, and imported many-body Hamiltonians. Mixed product-ready states can be resolved into occupation inputs.

Gaussian preservation for the restricted class is standard fermionic linear optics, not a new result: Sergey Bravyi, Lagrangian representation for fermionic linear optics, https://arxiv.org/abs/quant-ph/0404180 (Gaussian maps and single-mode projectors). Our decisive algebraic witness below avoids needing an unproved claim that every native Record is Gaussian.

## Exact interacting filter discriminator

On the entire two-mode Fock input domain let K_g=exp(-g n0 n1), g>0. Its occupation diagonal is (1,1,1,e^-g). An invertible diagonal number-conserving Gaussian operator has diagonal amplitudes proportional to (1,x,y,xy); hence d00*d11=d10*d01. K_g fails this identity. At g=log2 the discrepancy is -1/2.

An input-state proof also handles ancillas and postselection. On four modes take the normalized Slater two-form

  psi=(|01>+|03>-|12>+|23>)/2,

where |ij>=c_i^dagger c_j^dagger|vac>, i<j. Its Pluecker expression a01*a23-a02*a13+a03*a12 vanishes. Acting with K_g on modes0,1 leaves that expression (e^-g-1)/4, which is nonzero. The output is a pure non-Gaussian state. Every resolved branch in the restricted class preserves Gaussian input states; discarding ancillary modes cannot produce this pure non-Gaussian state either. Therefore no nonzero exact branch supplies K_g on all inputs, including these spectator modes/reference compatibility. Classical grouping cannot repair this: the desired CP map has Choi rank one, so every accepted Kraus operator must be proportional to K_g on the stated input domain. Refining mixed ancilla preparation gives the same conclusion.

This is about the full-input filter, not merely fitting a thermal trace or preparing one classical distribution by an imported classical sampler. For uniform two-mode input the desired interacting Gibbs state at 2g=log4 has weights (4,4,4,1)/13. Its Wick defect <n0n1>-<n0><n1>=-12/169 also shows that it is not a gauge-invariant Gaussian density. Mixtures of Gaussian states can reproduce some non-Gaussian diagonal distributions; that does not invalidate the rank-one instrument obstruction.

Adding nonzero dimer hopping tT01 does not remove the obstruction: [T01,n0n1]=0 and its exponential is an invertible Gaussian factor. If their product were Gaussian, multiplying by the inverse hopping exponential would make K_g Gaussian. This density interaction is genuinely nonquadratic on full Fock space, but it is trivial in the isolated fixed-N=1 dimer. We do not disguise that fixed-sector limitation. A three-mode connected hopping-plus-density target introduces further noncommutation; no claim about its exact compiler is made here.

## Actual native bridge escape, with the topology cost retained

Use the four-vertex path 0--1--2--3, embedded along a lattice axis. Its three physical edge qubits represent the even four-mode sector with no cycle constraint. If n has even total occupation, physical edge bits are (n0,n0+n1,n0+n1+n2) modulo2. Thus middle-edge Z12 equals (-1)^(n0+n1). The B identities are exactly the products of incident Z values.

The Slater state above is attainable with quadratic number-conserving mode rotations from an occupation Slater state; adjacent Givens on the connected path suffice, with the already supplied phase controls. This is a supplied preparation, not an axiomatic formation law. Record edge12. The two unnormalized branches are

  psi_even=(|01>+|23>)/2,
  psi_odd=(|03>-|12>)/2.

Each has probability1/2. Their Pluecker expressions are +1/4 and -1/4, respectively: both are non-Gaussian in the original full four-mode CAR description. The full instrument is P_even and P_odd, with sum of effects I. Physical Z12 is fixed in each output; hopping12 is deleted permanently. Remaining hopping edges01 and23 preserve the Record. Replacing this actual operation by single-mode occupation measurement gives zero Pluecker expression, an adverse control against overgeneralizing the restricted closure.

There is an important operational qualification: after deletion, the source grants even CAR separately within each component. Coherence between different component-number sectors in the displayed global vectors is not automatically accessible by surviving operations. Non-Gaussianity in the pre-event global CAR representation is therefore a resource candidate, not proof of useful surviving non-Gaussian gate power. Reconnecting the recorded bond would violate the stated Record-preserving protocol.

A direct parity Record on the two target modes cannot itself implement K_g: each branch has rank2 while K_g has rank4. Keeping both classical outcomes dephases cross-parity coherences, whereas K_g preserves and attenuates them. Feedforward after that bare rank loss cannot restore a full-input injective map. This rank argument does not apply when information has first been encoded into extra modes; that is precisely the unclosed escape.

## Strongest next obligation, rather than a supplied universal gate

A genuinely useful extension must give a finite extra-mode path/tree encoding made from the already supplied quadratic controls, use an actual component-parity Record on an auxiliary cut, and return the target information to a still-live component with an accepted full-rank Kraus map proportional to K_g. It must exhibit every failure Kraus operator, old-sign code maps, and no reactivation of the recorded cut. An arbitrary weak-parity measurement exp(kappa B0B1), density-density Hamiltonian, controlled-Pauli writer or coherent history recombination would simply import the missing resource. No such exact construction was obtained in this bounded probe.

The outcome is consequently useful but limited: the reviewed Gaussian preparation does not extend by its existing diagonalize-and-leaf-filter method; the actual native Record menu contains a concrete non-Gaussian boundary operation, so a generic Gaussian no-go would be false; its irreversible cut and surviving-algebra restriction are the precise obstacles a positive interacting compiler must overcome. Born/readout, initialization, pulse scheduling, phase controls and energy/work supply remain explicit.

## Executed support

check.py uses exact rational arithmetic on at most eight basis states. RESULT.json reports its actual assertion count, source hash and elapsed time. It checks the full physical prefix-parity dictionary, both Record outcomes and probabilities, Pluecker witnesses, product-filter controls, target Wick defect and the direct rank obstruction. It is not a numerical proof of all adaptive protocols, nor a full interacting-instrument construction. The source mutation log deliberately replaces the actual parity branch selection with a single-mode selection and must fail the resource predicate, separately from the passing adverse assertion in the baseline.

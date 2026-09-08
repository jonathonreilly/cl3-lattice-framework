# Independent phase-preparation review

Mathematical disposition: PASS on the stipulated initially unrecorded ready-subspace domain. No blocking matrix or sign defect found. Explicitly retain the ready-state, phase/control, event and success-conditioning assumptions below before downstream use.

## Exact coverage and source binding

Complete author reads: PREREGISTRATION.md, check.py SHA c767cfad5beaa9af5acc5b55a16a5e069b37f47104ce93d7fb30838001f82dfc, RESULT.json, execution.stdout and empty execution.stderr. Parsed stdout equals raw RESULT.json with49 passing checks. The author program was not rerun because it writes its raw result into its own directory; instead the independent CAR program writes exclusively in this review folder.

Main source pin2b42ebe4b6b4ee76b0fa1b8e668ad7775e946307. Native edge-instrument source: physical midpoint placement, definitions of A/B/T, full Theorem1 proof/dictionary, and Theorem2's branch/deletion meaning were inspected. The tree has no cycle constraints; its16 physical dimensions agree with the even five-mode dimension. The source proof constructs one-dimensional occupation fibers, full parity-sector matrix units and the faithful common quotient algebra. Thus the CAR computation below transfers through its simultaneous A/B dictionary, not a fitted phase change chosen to match this result. The local-cycle source explicitly supplies phase pulses exp(-i theta(n0-n1)); it does not derive their physical selection. That source was read only at its phase/control/import sections here, not re-reviewed in full.

## Independent algebraic derivation

Use CAR modes0,1 as matter,2 vacant leaf,3 occupied leaf,4 inert parity reservoir. Let T=c0†c1+c1†c0, D=n0-n1. Both vanish on the matter zero/two-particle sectors. On the ordered one-particle basis(|10>,|01>), T=X and D=Z. With U=exp(-i pi T/4), R=exp(-i pi D/4), W=RU, Pauli rotation gives UZU†=-Y and R(-Y)R†=X. Hence WDW†=T on the entire Fock space, and W is unitary. Reversing the phase sign gives the wrong conjugation, as the author adverse case tests.

For a vacant leaf2, a number-conserving hopping pulse with cosine r and sine sqrt(1-r²), followed by recording n2=0, has survival operator r^n0 on the ready subspace: matter vacancy is unchanged, matter occupancy has amplitude r. For the filled leaf3, survival at n3=1 gives r^(1-n1). Both results follow directly from the two-level single-particle hopping block; fermionic ordering signs affect exchanged amplitudes but not this no-exchange branch. The two even hopping operators on disjoint mode pairs commute, and the second pulse commutes with the first leaf occupation.

Their successful product is r^(1+D). Rotating before by W† and after by W gives

    K_success = W r^(1+D) W† P = r exp[(log r)T] P
              = r exp(-aT) P,  a=-log r.

The full operator equality holds, not just a trace. At r=3/5, its multipliers on T eigenvalues(-1,0,+1) are(1,r,r²). The ready subspace has multiplicities(1,2,1), because each matter occupation has exactly one even-compatible reservoir occupation. For ready density P/4, success probability is(1+2r²+r⁴)/4=289/625, and conditional energy is(r⁴-1)/(1+2r²+r⁴)=-8/17.

The resulting matter density is proportional to exp(-2aT), so the state inverse-temperature parameter is2a, whereas the Kraus filter parameter is a. For an arbitrary ready input rho, the result is K rho K†/Tr(K rho K†), generally NOT a Gibbs state. Since the whole Kraus identity holds on P, tensoring any reference identity establishes the unnormalized CP-map identity for every entangled input supported on P tensor H_ref. Success normalization is input dependent; the quoted289/625 is specific to P/4.

## Initial state and physical Record scope

P/4 is diagonal in the physical edge-Z basis: edge02 is0, edge13 is1, and the two remaining physical qubits are maximally mixed. This is a supplied flat ready distribution, not the desired thermal preparation. Its hopping expectation is0, whereas the successful state's is-8/17; the author also detects nonreal physical coherence in the output. The rank-four ready mixture effectively fixes unbiased weighting over compatible matter/parity-reservoir labels. Nothing here derives that weighting, reservoir role or a physical trace law from the axioms.

The initially sharp leaf occupations MUST mean unrecorded ready states, not pre-existing permanent Records. The attenuation pulses change those occupations on failure. Reading them as old Records would violate permanence before the new event. The intended protocol treats their Z measurements as first formation, which is consistent with the preregistered leaf-event description; make this distinction explicit in later prose.

After the first leaf Record, its hopping is no longer applied. The other leaf pulse and final matter rotation commute with that physical leaf Z. Final W also commutes with both leaf Z operators, so all four branches preserve both newly recorded values, including failures. This is a finite supplied switching protocol. It does not prove perpetual preservation under arbitrary future leaf hopping, automatic deletion, or autonomous occurrence. Rejecting failures selects the desired conditional preparation; it is not an unconditional primitive formation law.

The four physical edge centers are(1,0,0),(0,1,0),(2,1,0),(0,0,1). They are distinct sites on the source placement. The BKSF hopping/phase support is on bounded endpoint stars, not asserted to be a strictly nearest-neighbor gate circuit. Shared vertices in the virtual tree do not make physical edge centers nearest neighbors. No extra local M4 algebra is used, but roles, ordinary tensor composition, code and readiness are supplied.

## Independent finite evidence

`independent_car.py` builds annihilation matrices directly by occupation-bit parity signs on the full32-dimensional five-mode Fock space. It does not import author matrices or its source. It restricts to total even parity with n2=0,n3=1 (four occupation states), derives the pulse action there, and checks20 exact assertions:

- phase conjugation and both separate attenuation maps;
- every branch's two leaf eigenvalues and complete ready-input normalization;
- whole successful Kraus operator against the spectral target;
- number preservation, second-pulse/first-Record commutation and final Record preservation;
- a maximally entangled four-dimensional reference input;
- all four probabilities:136/625,289/625,64/625,136/625 in00,01,10,11 order;
- initial zero energy versus successful -8/17, excluding preinserted target thermal preparation.

All20 passed. Reference universality rests on the whole-operator identity, not the one entangled numerical witness. No empirical frequency, physical beta, q selection, controller selection, or primitive Admissibility identification is inferred. The result is a genuine positive filter within the declared phase-enabled apparatus class, with its initialization, success cost and physical-law bridge explicit.

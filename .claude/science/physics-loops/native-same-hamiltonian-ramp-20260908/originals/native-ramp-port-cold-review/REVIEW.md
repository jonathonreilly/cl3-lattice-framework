# Independent standard-library ramp jet port review

PASS for complete check.py22a929f54debf8fcc2f3b386836522cbcc80bc3785ded0db0805340763bf777c and REPORT4c7af1a628aff7f906fc2fda3040b0e4db5aebe5b73f909c63349b4e92181509. Full implementation, raw result, mutation source diffs/stderr and hash closure reviewed. All frozen hashes verify. The already independently reviewed ramp and initial-ice proofs are reused, not replaced by finite controls.

The sparse monomial dictionary correctly represents ordinary profile jets f,f',... rather than Taylor coefficients. deriv applies the product rule with multiplicity m_k and shifts one derivative index. Six jet slots suffice for this order-four recursion; no discarded sixth derivative is reached. Fraction arithmetic, vector cross products and -2 ad convention reproduce the Hermitian Pauli transform. The moving-frame derivative has the required negative vector prefactor corresponding to positive i epsilon dotY Y†. Transverse cancellation is checked against the correct transform separately from the altered solves.

The arbitrary-profile fourth scalar (f^4+ff'')/8 agrees with my prior independent hand derivation: rotated Hamiltonian gives f^4/8+f'^2/8 and derivative frame gives -f'^2/8+ff''/8. The second generator f' iX/4 is nonzero. Static odd/even generator grading cannot be imposed during the ramp. The standard-library port retains this information instead of merely evaluating one schedule.

Independently evaluated three rational jet assignments and a nontrivial product derivative: nine controls pass without running the full graph helper or any dynamics. Exact beta(15,15) integral coefficients and fourteen zero endpoint derivatives are correctly formed. The four time powers agree with the analytical two-cone and slow-ramp proofs. Full L4 support checks count every distinct pair separately here, yielding18626 total predicates; this differs honestly from the earlier215-count aggregate-pair implementation.

All three actual mutations change the solve while keeping the physical transform fixed, so wrong derivative sign, omission and deleting the second generator fail at order-two transverse cancellation. These are mathematical failures rather than hash failures or two jointly altered circular comparisons. The claim that these controls prove a volume-uniform dynamics is explicitly excluded. Standalone-only alarm and explicit exceptions remain active under-OO.

No blocker found. No canonical edits, sampling, whole dynamical proof rerun or new theorem authority claim was made.

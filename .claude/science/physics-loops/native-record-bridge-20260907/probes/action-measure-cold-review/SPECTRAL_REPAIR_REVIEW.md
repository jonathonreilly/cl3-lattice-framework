# Same-session spectral repair review

PASS. Complete final sources read: check.py SHA d559e8ec8933083b1e83e3c58939a350e6144876716ebc5ff2b6ef1d364d9b87 and check_reservoir.py SHA00d88c8b48e447ffe336044c9a3f08e88b1ee2faba771c09260468cc1eaeb60f. Current memo SHA77bee8691ef9e01b2e88b5128789cce49a4b6c28390f85459550cc0118c15c2a preserves the historical results and accurately describes the coverage repair. No scientific coefficient or geometry retuning occurred.

Both final sources were freshly executed, producing27 and17 passing assertions. Parsed results exactly match current raw files; every prior scientific field and old check value matches this review folder's preserved earlier execution. Only source identity, added checks and counts change.

The ten added assertions per source bind each used hopping matrix to the intended exponential: Hermiticity and T^3=T imply spectrum contained in {-1,0,1}; the displayed polynomial projectors are the complete orthogonal spectral resolution; the six identities F(T)P_lambda=2^(-lambda)P_lambda imply F(T)=exp(-log(2)T). I additionally checked projector Hermiticity, idempotence, mutual orthogonality and sum I, and disjoint-hop commutation directly in both final matrix namespaces. Thus the product is the intended exp(-log(2)(T01+T23)), not merely a trace-compatible polynomial.

Independently recreated odd-coefficient -3/4 to -2/4 mutants in this review folder both exit1 with failed spectral_exponential assertions. The previous trace-only mutation survivor was a real evidence gap; earlier PASS did not establish mutation completeness. The current repair closes this specific operator-exponential coverage gap. It does not claim every possible mutation is detected or that tests select a physical measure.

Exact trace values, the normalized q counterexample, zero-mode degeneracies and physical scope remain as in the original review. See SPECTRAL_REPAIR_RECEIPT.json and the preserved new execution/mutant outputs. This review supersedes the prior unchanged-runners statement only for this newly declared repair; prior review files are left unchanged as history.

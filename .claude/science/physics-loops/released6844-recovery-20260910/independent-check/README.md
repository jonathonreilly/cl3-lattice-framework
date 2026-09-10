# Independent finite-matrix reconstruction

The supervisor independently reconstructed the specified Hodge, exterior differential, cover action and antiperiodic quotient with standard-library exact rational arithmetic. It imports no repository module or SymPy. This checks the chart nilpotency, matrix difference, time bands, shift commutators, raw block ranks and complete grouped-map counterexample. Expected comparison values were already known; this is not a blind check or an audit.

The final check passed and rejects two semantic mutations: dropping the grouped cross blocks and flipping an exterior insertion sign. The first attempt did not detect the exterior-sign mutation using its selected summary predicates. It is preserved under `failed-attempt/`; the revised checker adds the actual chart-differential nilpotency invariant already asserted by the primary. The successful canonical producer was not repeated.

Execution receipts retain their actual historical command paths. Run `python3 check.py` from this directory to reproduce this standalone finite check. Its scope does not include transition equivalence, Schur elimination, physical evolution, OS positivity, or TOE closure.

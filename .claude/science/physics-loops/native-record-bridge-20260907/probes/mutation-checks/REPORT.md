# Seven targeted raw-probe mutations

Six of seven mutations were detected by actual mathematical assertions. One survived. No frozen original was changed; every original hash was rechecked after execution. All subprocesses ran directly on isolated mutant.py copies. No integrity/hash assertion served as a detector (the scripts merely emit their own hash).

| Mutation | Return code | Mathematical assertion result |
|---|---|---|
| native_cycle_sign | 1 | DETECTED: AssertionError: actual cycle stabilizer equals minus X Y X Y |
| native_post_normalization | 1 | DETECTED: AssertionError: fixed vacuum edge1 sign-1 forces edge0 |
| probability_coefficient | 1 | DETECTED: AssertionError: one identity neighbor 1/3 |
| improper_cubic_group | 1 | DETECTED: AssertionError: rotation group closed |
| action_transfer_polynomial | 0 | SURVIVED; all existing checks passed |
| reservoir_occupation_sign | 1 | DETECTED: AssertionError: {'rank16': True, 'source_code': True, 'ancilla_conserved': True, 'native_full_trace': True, 'generic_reservoir_weight': False, 'biased_reservoir_rejects_det': True, 'normalized_full': True} |
| relay_wrong_copy | 1 | DETECTED: AssertionError: path-distance-1 |

## Survivor diagnosis

The square transfer mutant replaces F(t)=1-3t/4+t²/4 by Ftilde(t)=1-t/4+t²/4. On the hopping spectrum {0,+1,-1}, the original values are1,1/2,2; the mutant values are1,1,3/2. These are genuinely different operators. Yet their odd-one-particle dimer traces are both5/2, and their even dimer subspace traces are both2. Thus the two-dimer even trace is2·2+(5/2)²=41/4 for both, and the full trace is(2+5/2)²=81/4 for both. The scalar aggregate tests therefore cannot detect this change. The hardcoded comparison eigenvalues2,1/2 are not independently bound to the implemented polynomial by a spectral-value or inverse identity check.

A prospective repair could check F(+1)=1/2 and F(-1)=2 directly, or the operator identity F(T)F(-T)=I for an actual nonzero dimer. The original polynomial satisfies the identity because T³=T; the mutant product is I+T²/2. This is a suggested extra mathematical control, not a change made here, and is not counted among the seven tests. The survivor is a runner coverage gap, not by itself a refutation of the analytically correct frozen polynomial or source theorem.

The relay wrong-copy mutation is instructive: on this bipartite center-and-four-target star, copying the opposite sign can still make the target marginal a common fair bit, so the star-target tests alone do not detect it. The existing distance1 path assertion does detect it. This shows the adverse controls exercise distinct scopes rather than merely repeat the same target marginal.

Exact deltas, stdout, stderr, return codes, source/mutant hashes and execution times are stored in each case directory. RESULT.json is the machine-readable summary. This is a bounded robustness pass, not a formal N-gate evaluation or science audit verdict.

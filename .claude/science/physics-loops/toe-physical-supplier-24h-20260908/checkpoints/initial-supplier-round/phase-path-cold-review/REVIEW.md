# Independent finite implementation review: native path phase preparation

**PASS for the final finite implementation and its declared conditional scope.** Full Kraus maps, rather than only traces, were independently checked. This review does not prove the all-m analytical theorem, select a physical action/beta/Born law, or certify a canonical audit artifact. Native_ladder separately reviews the general proof.

## Source-bound coverage

Read COMPLETE DERIVATION.md and COMPLETE original path_probe.py184e13a4263605d5974919e1cfcb49b5637da75e10f3ed8f8685daebb7c58733, parsed all current original142-control PATH_RESULT fields, and read/reran the complete49-control exact dimercheck. Then reviewed the full same-session repair diff and reran independent comparisons against the final source:

- Final DERIVATION.md `1f18fbf41b5d81bd82fff2e0467ea32454e4588fedfb205e02e24c7c7e37a0c8`.
- Final path_probe.py `eba4eb0a87566a28a72080bdab991d913d4cd821a3e6faaa4743f5f4d4d36aed`.
- Final PATH_RESULT.json `05bf7d6052f11c2f8ba2201a914cd7b99060ca6b9a37f78b4ed5707f320429ba`,148 controls.
- Exact dimer check.py `c767cfad5beaa9af5acc5b55a16a5e069b37f47104ce93d7fb30838001f82dfc`; original RESULT.json `38b159f17bae0e821d92655e37e56ec83279bbe3dae8fd75ed35e59f6e6d4b86`,49 controls.
- Preserved first138-control source `45ee3e0c9117f629b830e912109f7765c6f44516c4169e861f2e6e4a6a282502`, result `8fec79c7ac3c44097a2795cb2862dd7006ea8cf0aee38bbc507ca55f4ba336d6`. Those are resource-history evidence, not extra independently executed physics checks.

All executions occurred on scratch copies because the author programs write their adjacent result files. No author/WT files were edited. The scratch instrumentation adds only a bound_cases capture immediately before each existing row emission, storing actual Qready,V and all branch columns. It does not replace gates, states, comparisons or constants.

## Independent representation and actual operator comparison

I did NOT reproduce the author's QR algorithm as the independent calculation. I constructed the256 even-occupation masks of9 fermion modes, canonical CAR hopping matrices from occupation-bit signs, and separately constructed native physical hopping matrices by their bit-flip/Z-sign action. A transition-graph phase dictionary in each total-number sector intertwines those representations. All8 native hopping matrices and the entire dictionary unitarity were checked.

For each supplied one-particle O (the actual control specification), I formed its fermionic lift using exterior minors det O[I,J], with ancilla bits fixed. This avoids Givens compilation. The resulting whole256-dimensional operator matches the compiled native V. I then applied independent CAR leaf unitaries and every occupation projection, retaining all16 outcomes, rotated back by the exterior lift, and compared each resulting256×16 ready-domain Kraus column matrix with the actual physical output. This checks every ready input and hence its reference extension, not just the uniform mixture.

All96 branches across two families and three beta settings match; the largest independent residual is approximately1.3991e−14. Own INDEPENDENT_RESULT.json contains137 explicit comparisons, including dictionary, full rotations,96 branches, independent success/completeness and energy. They are verification assertions, not137 distinct physical experiments or independent theorem discoveries. The full finite target/formulas were exposed before review; the independent method and operators were derived without copying numeric expected probabilities/energies.

## Geometry, ready domain, and phase orientation

m4 has9 virtual vertices and8 actual edge M2 sites at distinct midpoint coordinates, not4 enlarged local sites. The graph is a tree, so its unaugmented even9-mode representation has dimension256 and no cycle stabilizer. The4 fixed sacrificial leaf Z values and4 maximally mixed other physical edges give a literal product ready density of rank16. Every4-mode matter occupation pattern has one compatible inert-reservoir parity, so this is the full matter occupation functional, not a restriction to even matter parity. It supplies no odd CAR observable outside the represented algebra.

For a canonical adjacent pair T=X and D=Z on its one-particle subspace, J=(TD−DT)/(2i)=−Y. R=exp(−i pi D/4) gives RTR†=Y=−J. Therefore R exp(−i theta T)R†=exp(+i theta J), whose real2×2 matrix is the inverse of the elimination G. This fixes the sign without relying on a descriptive gate name. Reversing the phase in a scratch source fails the actual phase_compilation predicate.

The full exterior comparison validates the implemented multiplication order, diagonalization H=V diag(epsilon·n)V†, and all fermionic signs on the ready and full code domains. In particular a correct one-particle reconstruction alone would not have supplied this many-body check.

A pair sign exp(i pi(n_a−n_b)) equals BaBb and factors into adjacent difference phases. No individual B_j generator is required. I independently verified all6 prescribed pairs in occupation representation; the final author's shared helper additionally verifies them on the physical256-dimensional matrices.

## Original uncovered branch, repaired honestly

The first142-control revision has EMPTY residual negative-sign sets for both tested SO QR inputs. Positive-hypot elimination of an SO matrix gives positive diagonal entries and thus Q=I. Changing the unused pair-phase constant−1 to+1 therefore survived; it was not evidence for a correct executed residual branch. I preserved that mutated source/output and reported it before repair.

Final repair factors the actual implementation into paired_sign(a,b), used both by the QR residual path and six explicitly prescribed pair tests. The same−1→+1 mutation of the shared helper now fails at direct_pair_sign_0_1 with an actual AssertionError. All original142 predicates and ALL physical probability/energy rows remain unchanged; exactly6 controls were added. Source prose now accurately distinguishes empty QR residuals from separate pair tests. The old survivor and138/142 histories remain available rather than being overwritten as successful mutation evidence.

## Completeness, probabilities and thermal meaning

Vacant-leaf retention gives r^n; filled-leaf retention gives r^(1−n). Both come from actual number-conserving leaf pulses and physical leaf-Z Records. All outcomes remain in the complete instrument. Their sums give the identity effect on the entire16-dimensional ready domain. The final matter rotation commutes with every leaf occupation, so each branch's recorded signs persist through that rotation. No reset/reuse of recorded leaves is licensed by a failed branch.

The successful eigenmode factors yield the scalar prefactor exp(−beta sum_negative|epsilon|/2) times exp(−beta H/2). Uniform ready matter occupations then give product[(1+exp(−beta|epsilon|))/2] and energy sum epsilon/(1+exp(beta epsilon)). Independent branch calculation agrees for families(1,2,3),(2,1,2) and beta0,.7,2. These families are connected and genuinely noncommuting bond sums, with characteristic polynomials x^4−14x²+9 and x^4−9x²+16 respectively; both have distinct nonzero one-particle spectra. beta0 tests no attenuation, not an actual zero-energy mode. General zero modes and arbitrarym belong to the analytic theorem, not this finite scan.

The dimer's exact success contraction has spectral values1,r,r² at T eigenvalues−1,0,1, multiplicities1,2,1. This directly gives p=(1+r²)²/4=289/625 and energy(r^4−1)/(1+r²)^2=−8/17 at r3/5. Its complete copied executable passes49 and checks full physical K, not just this arithmetic. The path numerical support does not turn the Gibbs filter into a universal reset: arbitrary ready/reference inputs receive K rho K†, while the Gibbs conclusion uses the stated product mixed preparation.

## Limits and small editorial point

Numerical Frobenius tolerances are2e−10 for operators,2e−12 for success and2e−11 for energy; observed errors are far below these thresholds. This is numerical support, not a directed-rounding interval proof. No all-m accuracy/precision/resource scaling is inferred. The routines' source hashes and finite outputs are evidence bindings, not scientific authority.

The apparatus supplies phase pulses, real hopping isolation, beta/h/eigenbasis, product preparation, schedule, Born/Lueders events, spatial roles, work and success selection. Whole endpoint-star hopping support is not a strict nearest-neighbor physical two-qubit compilation. Quantum leaf-Z outcomes become primitive Records only under the already declared native instrument calibration. The construction does remove the thermal-state oracle within that conditional apparatus class, not these other imports.

Minor editorial underclaim: the opening paragraph still says the general proposal awaits “a noncommuting finite test”, while the last section documents that test. It can say the general proof awaits independent review, with the finite test completed. This is not a mathematical blocker and requires no parameter or operator change.

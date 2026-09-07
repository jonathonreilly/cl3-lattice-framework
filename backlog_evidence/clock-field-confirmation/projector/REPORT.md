# Deferred #7941 projector source review

**Disposition: corrections required; no source PASS or production rerun.** I read all 1,433 lines of the original note (502), runner (888) and cache (43), before execution. The exact three files from original #7941 head `8ac1ccdfa1735fd6facdf910defb964469fba35a`, original base `2814c6768e4d7b38048f70ad7883b4951cb12da3`, remain byte-identical on #7966 head `369f785003f19c1ec5e8c4a6f1155c2827a7986b`. `ORIGINAL_SCOPE.json` binds every mode/blob/hash. Current-main authority is `94e90cbf928cb35fa1b50e894cd897c94b73077f`.

The actual computational closure is just the projector and two corrected ice modules: RK has no repository helper imports; stiffness imports RK. I verified both current helper hashes against my previous complete ice review. The two parent notes and the role-compiler note also match the earlier complete reviewed corrections; the axiom memo remains unchanged. The parent notes are supplied scientific context, not a grant of phase or law-selection authority. The raw projector does not import the deferred magnetic, charge or spectral producer tower, nor any reserved science. `CLOSURE.json` gives actual imports and raw/current context hashes. This is a closed three-source review with explicitly reused current-parent coverage, not approval of the entire field chain.

## F1 — P1: sample loop writes past every array when burn is positive

Runner lines 266–271 allocate `sample_sweeps` values. Lines 309–329 sample when `step+1 >= first_sample_step`, including the burn endpoint itself, then continue through `(burn_sweeps+sample_sweeps)*M`. With positive burn, this stores **sample_sweeps+1** entries. Every original production call has positive burn.

The exact function AST with ordinary NumPy bounds checking raises `IndexError` at actual line 314 for two-walker L2 calls with `(burn,samples)=(1,2)` and `(2,3)`; `(0,2)` is a returning control. I independently reproduced the same failure through the **actual unmodified Numba dispatcher** with `NUMBA_BOUNDSCHECK=1`, using exact corrected current-main helpers copied into external scratch. Compilation plus the three tiny calls took about two seconds. See `BOUNDS_PROBE.json` and `COMPILED_BOUNDS_PROBE.json`.

Default unchecked compiled array access can write beyond the allocation. I have not executed the unsafe unchecked variant, and I do not claim which original allocator/object was corrupted. The old 12/0 receipt does not establish safe execution or validate the resulting data. Fix the burn/sampling convention explicitly, require exactly the allocated sample count, and test compiled bounds plus a reference/sentinel sequence for zero and positive burn. The narrow `>` boundary is one natural interpretation of the documented burn followed by requested samples; whichever convention is selected must be stated and tested. Do not merely enlarge the array and silently alter the protocol. Historical output must be preserved separately, and any repaired production result needs its own fresh identity-bound receipt.

## F2 — P2: common zero-flux subtraction is omitted from uncertainty propagation

`fit_flux_curve`, lines 490–527, sets each difference to `E_i-E_0`, includes the reference error in each marginal variance, then treats the differences as independent for `slope_error`. Even if the underlying energy estimates were independent, the differences share covariance

`Sigma_ij = delta_ij sigma_i^2 + sigma_0^2`.

For the exact current weighted point estimator `a^T y`, its variance is `a^T Sigma a`, not the diagonal-only expression at line 511. A deterministic call to the actual fit function with three flux points, true U=1 and independent energy errors 0.1 gives reported U error `0.1714285714`; the variance of that same estimator including the shared reference gives `0.2099562637`, a factor `1.2247448714` larger. `CACHE_AND_FIT_PROBE.json` records the full control and formula. This counterexample does not assert that the original numerical positivity reverses; it demonstrates a wrong reported uncertainty prescription.

Preserve or explicitly revise the point-estimator protocol, propagate shared-reference covariance correctly, and distinguish nominal block-error arithmetic from independently calibrated statistical coverage. Ten time blocks of one branching population do not establish independence, mixing, absence of population bias or convergence. The existing note acknowledges these limits, but the six-error acceptance threshold must use the estimator's own correct nominal covariance. The cache contains summaries only, so the original per-flux energy covariance cannot be reconstructed from that receipt alone.

## F3 — P1 for a microscopic operator claim: sum of bare E squared is constant

Note lines 245–255 write `H_E=(U/2) sum_links E^2` and derive the observed topological flux cost. For the supplied microscopic spin-half observable `E=epsilon(n-1/2)`, however, every link has `E^2=1/4`. That literal operator is `3 U L^3/8` times identity and cannot distinguish these flux sectors.

The fitted finite-component energy differences can be retained as a **protocol-dependent flux-cost coefficient**. Explain that `U Phi^2/(2L)` is comparison with a supplied coarse-field energy functional, not a derivation from the bare microscopic `sum E_link^2`. Define the coarse observable/normalization if making that bridge. Do not infer a physical electromagnetic coefficient or a uniform thermodynamic stiffness from the finite fit. The corrected ice parent already distinguishes its finite fitted quantity and the phase/composite assumptions; carry that boundary into this descendant.

## F4 — P1 for receipt reuse: current inputs differ, and the old record is not fresh

The raw runner hash matches its historical cache header, but both actually imported helper files differ from the old branch. Running the actual current `runner_cache.cache_status` against an external overlay of this producer/cache and exact current-main inputs returns **`input_mismatch`**. The old fingerprint is `3c58cd9e3a66fa268a03c885c7305ba4d1c4a505800468e4342a58d8e4625766`; current declared-input fingerprint is `bb0a58f1b1281afad25fa19f5b2be9f1b68b9699df901ec519cfa963e862aa95`.

The imported utility function corrections previously reviewed did not authorize replaying old evidence as fresh. Further runner fixes also change its own hash. Preserve the old cache as historical only, bind the final note, actual helpers and load-bearing benchmark/proof context, and create new evidence only after the implementation and bounded controls pass. The first-order comparison at line 795 hardcodes a parent coefficient; its parent is a finite-protocol component fit with nominal errors, not an independently established universal constant. Its exact provenance and qualification must remain visible.

## F5 — P2: a compound protocol change is not an isolated population or component test

The L8 control simultaneously doubles population, changes start family, changes warmup, increases projection burn and sampling length, and changes seeds (lines 723–738). Agreement is a useful sensitivity check under that combined change. It does not separately establish population convergence, projection-time convergence, component equality, or that the chosen start lies in a different local-move component. The note mostly acknowledges the finite and component limits, but the table/program claims should consistently describe this combined finite protocol and selected-component energies. A nonlocal preparation move alone does not prove that the resulting configuration is outside the original local-move component.

This need not trigger expensive new convergence ladders merely to preserve a narrow diagnostic result. Narrow the statements now; any later claim of converged component ground energies requires separately varied controls or a proved bound. The supplied projectors and finite mixed-estimator identity remain useful even while those obligations are open.

## F6 — P2: align inherited claims and the evidence trace with corrected parents

Note lines 276–289 include “RK Coulomb correlations and positive magnetic response” in an asserted progression. The corrected ice parent separates finite RK algebra, variational twist controls and a supplied phase comparison. This projector contributes no matched uniform-source response and cannot promote that earlier trial-state control into relaxed magnetic stiffness. Correct the inherited interpretation without rejecting unrelated electric measurements by association.

The note's `per_element: every accepted square flip is checked` (line 420) and runner output (line 879) also overstate executed instrumentation. The code checks geometry, recomputes one walker's flippability at each sample and all walkers' final flippability/Gauss/flux; it does not check every accepted flip's full invariants at runtime. An exact local proof and a complete finite transition control may justify all flips mathematically, but must be distinguished from actual per-step execution checks. The sampling memory error shows why this distinction matters.

## F7 — P2: current claim/governance conventions and no-go table need honest scope

Add current proposed-author status and a complete claim/proof/runner/input trace while retaining the exact Green-function and mixed-estimator identities separately from stochastic finite-protocol claims. The N1 table counts open future work and an imported phase route among “eight route families”; it should identify the actual executed controls and label open/imported context separately. The N2 assertions that none of W1–W4 closes another lack a complete pairwise argument; record unresolved relations rather than a new independence theorem. These are narrow packaging corrections, not grounds to erase useful conditional mathematics or start a formal audit.

## Mathematics that survives, and the next bounded check

For the two tested detunings, `b(C)=1-deltaV*N_f(C)/M >= 1`. Weighting by b and proposing each square with probability 1/M followed by acceptance 1/b gives exactly the normalized off-diagonal Green-function column; the remaining probability is its nonnegative diagonal. On a finite connected component at V<1, G is irreducible with positive diagonal, and its Perron vector is the lowest H eigenvector. For that exact positive eigenvector, the constant-trial row sum yields the stated mixed-estimator identity. None of these statements equates a finite resampled population to the exact eigenvector.

After F1 is corrected, the smallest decisive implementation controls are complete finite/local transition-column comparison with the stated G, exact incremental flippability updates over representative/full tiny states, normalized resampling/reference checks, exact sample-count and bounds controls, corrected covariance propagation, and actual input-drift rejection. Branch-factor or transition-sign mutants must fail the implementation controls rather than only a hardcoded certificate. A short tiny-state check is appropriate before any planned production budget. I did not run the 266-second original sampler, and no repaired production/source verdict is implied here.

All writes and tiny executions were external. There were no repository edits, commits, pushes, GitHub actions, full pipelines, audits or shared-planning changes. This lower-priority constituent review pauses for the separate final eleven-path field source/receipt review as soon as the author freezes it.

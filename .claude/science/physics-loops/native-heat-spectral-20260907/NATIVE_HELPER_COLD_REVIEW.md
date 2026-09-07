# Cold review of independent native killed-heat helper

Mathematical/implementation review PASS, with one required reporting clarification: the analytic Chernoff inequality is rigorous, but this runner evaluates its transcendental expression with floating math.asinh/cosh/exp. The displayed tail numbers are not certified interval upper enclosures. They must be described as numerical evaluations of an analytic upper-bound formula, alongside the already explicit uncertified expm error. This can be fixed in metadata/documentation without changing any36 rows or119 assertions.

No rerun was needed. I inspected the frozen source, raw receipt, preregistration and both preserved failed-allocation sources. The review does not claim that unavailable raw outputs from failed runs were compared numerically.

## Actual generator and adjoint

The action is beta(J-I), with four axial and two anti-diagonal shifts, each coefficient beta/6. The paired slice updates are transposes of each other; the diagonal is real, so the same action is the correct rmatvec/rmatmat. The reshape(N,N,-1) handles multiple columns consistently with the flattened p*N+q indexing. Slices omit exits at all four box walls while retaining diagonal-beta, giving killing rather than degree normalization or wrapping. Source p=(floor√beta,floor(3√beta/4)) and N=max(p)+ceil(6√beta)+1 match the preregistration. All six endpoints remain inside the box for each frozen beta.

The source is unshifted in lattice indexing, but continuum coordinates use h(p+1) for BOTH endpoints. expm_multiply receives tG and its exact trace-beta*t*N². No continuum approximation enters the generator action. The implementation is genuinely independent of the Gaussian comparison.

## Reflection and polynomial normalization

The matrices s1=[[-1,0],[1,1]],s2=[[1,1],[0,-1]] are the parent's simple reflections. The six listed words and determinant signs are exactly the Weyl image set, preserving Q. The leading kernel has prefactor sqrt3/(2pi t) and exponent-Q(y-wx)/t. Since LG=partial_t G and L²G=G(r²-4r+2)/t², the t/(4beta) correction is exactly G(r²-4r+2)/(4beta t). Multiplying the native entry by beta is the correct h^-2 scaling. Boundary cancellation and arbitrary shifted-source signs are retained.

## Counts, truncation and memory history

There are3 beta cases,2 times and6 endpoints, all36 unique keys. Direct source accounting gives119 actual assertions:34 each for beta128/512,46 for beta2048, then5 case/resource assertions. Only beta2048 receives the theorem-domain numerical margin check. The final receipt reports119,10.1961seconds and120.390625MiB.

Each upper-wall distance is N-p_i. The coordinate cumulant rate2beta*t/3 and theta=asinh(distance/rate) minimize the exponential-martingale bound for that coordinate. Union over the two upper walls bounds additional path loss; lower-wall killing is already native and is not a truncation error. The formula is a maximal/first-exit bound, not an endpoint substitution. However its floating evaluation is not a rigorous numerical enclosure, and the final residual-plus-tail assertion is a diagnostic, not a proof of the theorem constant.

Both allocation failures preserve the SAME beta/time/source/endpoints/N, weights, reflected formula and correction. The replacements are Kronecker sparse allocation, direct sparse diagonals, then six-shift LinearOperator. Resource assertions were not relaxed, and no scientific subset was dropped. The receipt correctly refuses to invent unprinted failed-run RSS values.

## Output repair scope

Add an explicit field or scope sentence that the Chernoff numerical values are uncertified evaluations of the analytic bound; retaining existing row keys is acceptable if that limitation is unambiguous. Do not describe these floating values as an exact-rational truncation certificate like the separate earlier recurrence runner.

The default output has five literal N5 lines rather than per_element/per_site/per_mode/per_block/lattice_wide prefixes. Converting those labels to the canonical prefixes is a harmless packaging repair if the scope classifier requires them; it changes no assertion or numerical field. No need to rerun the expensive numerical body merely to establish the mathematics, though a fresh receipt after any source edit is appropriate for hash binding.

Reviewed source SHA 8f09240d60541b73352dc8741c9a34a85d1a2f620defc8abd356443137568346. Raw result SHA 4b8ae1c840a338791c3bbd7e8aa473167a2dbbbe0347cdc811767586ceafe44b.

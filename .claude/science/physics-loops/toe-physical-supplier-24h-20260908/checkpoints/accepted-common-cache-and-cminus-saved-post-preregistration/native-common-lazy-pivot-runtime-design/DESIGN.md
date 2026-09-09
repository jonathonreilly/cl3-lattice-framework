# Prospective direct physical paired-pivot runtime — execution disabled

This is a design, not an execution proposal or a measured resource claim. Reviewed lazy source8b5c and coldff646 remain unchanged. No cache output yet exists in this design's premises; no native pivot/mock/cache replay is performed. Any runnable implementation needs independent review, measured cost and root preregistration.

## Exact input and physical error contract

Require completed common-cache worker/root acceptance AND independent saved postcheck, all source/runtime hashes,52536 stream entries/132 coefficients/five orbits, actual A/B endpoints, original geometry/pi and all underlying accepted scalar bindings. Build an indexed cache reader from byte offsets for660 rows; validate whole file hash and exact row membership once before use. Do not load52536 Python interval records blindly under384MiB. A bounded LRU reader (e.g32 rows) is a candidate, not a measured memory promise; retain input bytes immutability before/after use.

Use the exact rational midpoints fixed by the cache for poles, weights and pi. Compute each alpha=35*w/(2*pi) as Fraction. Its maximum must be<=12. These define exact physical columns; they are not approximate pole geometry masquerading as exact quadrature. Physical quadrature displacement stays in the separate parent operator ledger.

Compute etaA=max(actual A/Aprime half-widths), etaB=max(actual B/Bprime half-widths). Require etaA<=1e-30 and etaB<=1e-19; do not substitute announced small widths for a parsed maximum. For every original reconstructed G/J entry, first perform the exact selector (including k2 interval doubling), then inflate by alpha_max*2^24*etaA and alpha_max*10136*etaB. The general l1<=2 source bound already includes the k2 geometry, so do not multiply this physical radius again. Arithmetic width is already contained in cache intervals. Half-combination coefficients have sum of absolute values1 and retain these entry-radius guarantees. Do not add the separate .005 factor/dilation budget to each entry or treat the numerical cache as the exact PSD Gram.

Canonical label map: for each66 pole and source0..2, two eta=±1 labels with exact plus/minus cache indices; source chi=(+1,-1,-1). Validate all396 labels, uniqueness, eta membership, chirality agreement and source indices before imposing structural zeros. Native symmetry is a mathematical premise; malformed labels must not be accepted by merely zeroing the mismatched entries.

## Augmented Ward compatibility

The original pole half columns remain396. Append x0=e0/2,xA=wA/2,xC=wC/2 as three separate positive-chirality labels (not fake pole pairs), yielding399 candidates and798 covariance-closed coordinates. A new fetch adapter must handle pole/pole, appended/pole and appended/appended entries separately, transpose G and negate J correctly. It requires the reviewed Ward API interval implementation, accepted normalized a0/c_minus, scaled exact dependencies, and all physical error inflations. These do not yet exist in a runnable binder.

Pole/append arithmetic must include sqrt(alpha) enclosures; appended weight1/2 is exact. Use actual scalar interval evaluation, not midpoint API values without inflation. For the prospective global budget retain Ward ledger trace<531 and epsilon_Bc<5e-12, A error<2^40*1e-30, arithmetic<=2^-60. Structural J=0 on the appended block is exact, but its signed G cross entries and center1/12 terms are retained.

For an actual raw residual r, the unaugmented operator bound is sqrt(1058r), augmented sqrt(1062r). In half coordinates, original pole residual is twice the sum of pole-half residuals, whereas each appended column is present only once. Thus AUGMENTED r=2*sum(pole-half diagonals)+sum(three appended diagonals). It is NOT twice every399 diagonal. A conservative all-half factor2 remains safe but loses accuracy. For epsilon_comp=.001 the precise augmented weighted sum must be<=1/1062000000. Current compress() assumes equal factor2 for all columns and threshold2116; it must not silently be advertised as the precise augmented certificate. A separately reviewed weighted residual adapter is necessary. If deliberately using the conservative factor2, threshold must still change to epsilon²/2124, not retain2116.

## Pivot caps and unresolved conditioning

Retain198 pairs only as a fixed resource cap for the original candidate. It is not a dimension-exhaustion theorem:396 raw columns plus their Gamma partners have up to792 real dimensions/396 pairs. Augmentation permits up to399 pairs, not automatically199. Increasing198 to199 is a new prospective parameter requiring review; it closes no missing rank argument. Every fixed cap may honestly finish PAIR_CAP or PRECISION_STALL.

No exact rank, positive pivots, residual target or runtime is forecast from entry counts alone. Direct192-bit intervals can expand under small positive pivot denominators. A certified positive lower bound is necessary but can be too small for useful coordinates. Do not retry at higher precision or skip a pivot after seeing data under the same contract.

## Coordinates and error separation

Store every interval g,j,r BEFORE its diagonal update, selected indices, exact label map, trace checkpoint and input hashes. These are certified unnormalized row enclosures only. Future coordinates are g/sqrt(r),-j/sqrt(r), using outward isqrt-based positive root enclosures and interval division. A zero-crossing root denominator stalls; midpoint replacement is forbidden. For each coordinate interval choose a dyadic midpoint and retain its radius. The Frobenius radius (exact sum of squared radii, outward root) bounds coordinate operator error. Transform pole-half coordinates back to original columns by y+=v++v−, y−=chi(v−−v+); appended columns are unchanged. Only then may the original coefficient norm<=1 be used.

For exact coordinate matrix U and approximation Uhat with Frobenius error d and ||U||F<=sqrt(T_raw), finite impurity coefficient error obeys ||U C U^T−Uhat C Uhat^T||1<=2sqrt(T_raw)d+d². Add coefficient C uncertainty using ||Uhat||F² times its operator bound. This is additional to compression and input/displacement errors, not a repeated charge of the same entry inflation. No available measured pivot condition number establishes a useful d. An implementation must price and certify these coordinate intervals before claiming a finite Gaussian operator.

## Staged resource design, not authority

First implement exact tiny deterministic tests of reader selectors, weighted residuals, root coordinates and failure paths. Then a separately frozen cost-only attempt could allow at most4 paired steps,30 seconds inclusive/384MiB, fixed orbit and labels selected before data. This would need explicit root authorization; it is NOT authorized here. It must retain actual intervals even when the residual gate fails, and include input hashing/index construction/LRU I/O, inflation, all row reconstruction, checkpoint serialization and coordinate norm scans. No physical cost run is proposed until all input dependencies and source are ready.

A later production proposal may cap180 seconds/384MiB and198 pairs, but no forecast currently justifies that cap. Price O(k²n) rational operations from the fixed pilot without asserting constant denominator bit length. Include a conservative late-pivot denominator/size mechanism or admit the forecast cannot certify completion. Watchdog failure, PAIR_CAP and PRECISION_STALL remain valid terminal outcomes; no retry/refinement. The current folder supplies no executable native driver or authorization.

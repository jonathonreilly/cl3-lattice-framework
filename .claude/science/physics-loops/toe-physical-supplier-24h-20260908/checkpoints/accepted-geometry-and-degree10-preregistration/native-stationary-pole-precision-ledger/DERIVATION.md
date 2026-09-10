# Sufficient B-input width for the actual weighted 528-dimensional Gram

No physical calculation. This is a conservative sufficient certificate, not a lower bound on intrinsically necessary precision. Keep stationary oracle source9845 unchanged. The B error below holds with exact A-dependent balancing; its rounding/coefficient error needs a separate remaining budget.

## Native weight bounds

For h=1, A<=17/60, sA<=Cminus/2<7/30, and Bgeo<=A. The latter follows for opposite pairs from Jensen: (s²+6)A>=1. Since0<=D<=1/6, |a|=|1-4D|<=1. Both row and column norms of the actual Woodbury T are bounded by18(1+4*7/30)<35. Thus ||T||<=35.

For each pair of poles the unbalanced two-seed Gram has trace2(A+2Bgeo)<=6A<=17/10. The balanced covariance-closed Gram M therefore satisfies

    Tr M <= (35/pi)*(17/10)*sum w <318,

because the exact positive Gauss weights sum to16-1/128<16. This uses actual quadrature weights; it does not infer a factor trace from the physical trace-norm87.

Let W be the block-diagonal balancing map on the264 raw columns. Its norm squared is at most Cmax=(35/6)max(w_upper), using pi>3. This is less10.918 for the frozen pole intervals.

## Entry and operator errors from B and B'

Use the seven-source formula L_sigma(s)=-B(s)(N+s² O/6)+sigma*s B(s)T/6. Each raw seed is e0 or a signed sum of two neighbors; its l1 norm is at most2. A conservative endpoint multiplier is

    k(s)=4(1+s²/6+s/6), d(s)=4(s/3+1/6).

If the error radius of both B and B' is at most eta, a nonconfluent J entry has error at most [k(s)+k(t)]eta/|sigma*s+tau*t|. The confluent entry has error at most[k(s)+d(s)]eta. Exact root intervals bound these denominators; same-pole opposite-sign pairs use the confluent formula. The maximum over all frozen66 poles and sign choices is less10136. This is an enclosure calculation on source geometry only.

The raw J matrix has264 rows. Consequently ||Delta J_raw||<=264*10136*eta. The covariance-closed Gram error is the same off-diagonal-block norm, and balancing gives

    ||Delta M|| <= a eta,
    a=Cmax*264*entry_multiplier <29215444.

This is much sharper than using the largest s numerator together with the smallest denominator from unrelated poles, but still conservative.

## Conditioning-free physical operator comparison

Symmetry-twirl the Gram midpoint, then add its certified operator error epsilon to make it PSD. Its difference from the true Gram is at most2epsilon. Positive-square-root Holder continuity implies an HS factor error <=sqrt(1056epsilon), with dimension528. Since Tr M<318 and the balanced signed coefficient has norm1, the resulting trace-norm operator difference is at most

    2 sqrt(318*1056*epsilon)+1056*epsilon.

This compares the exact coefficient-space representatives with fixed reference covariance; it is not permission to identify artificial numerical ghost modes with a native pure state. Contour or polynomial certificates from the parent derivation still define the exact rounded native projector.

The exact geometry ledger gives a sufficient eta limit greater2.293e-19 by requiring the square-root term<=.003 and the final term<=1e-6. Thus eta=1e-19 (full B and B' widths<=2e-19) suffices for a B-induced error less.003001. Reserve the remainder of the1/200 arithmetic budget for A-dependent coefficients, square-root arithmetic and implementation errors. Those remaining errors have not been certified by this scalar ledger.

## Consequences for choosing a shared catalog

The accepted p12/low2^-28 catalog cannot establish this particular sufficient bound: its analytic radius alone is much larger. This does not prove that a sharper structured certificate cannot use those data. It does mean a24,552-pair batch must not be launched under the claim that this conservative matrix gate will pass.

A prospective p26 shared catalog, low cutoff2^-64, high cutoff8, and26 high-tail moments has67 panels and3484 endpoint A calls. The uniform analytic width upper bound (using2/pi<2/3) is

    (2/3)[2*(400/27)*(4/25)^26 +2^-64/3
          +12^26/(53*8^53)].

This is below the required2e-19 but is only the analytic contribution: oracle/root interval amplification must fit the remaining margin. High-order root brackets should be160 bits. No source or physical job for this new catalog is prepared here. The simple existing maximum-call forecast3*3484*.012281042+10 is about138.4 seconds, so a60-second contract would not cover this conservative forecast. The existing A66 attempt remains useful and unchanged.

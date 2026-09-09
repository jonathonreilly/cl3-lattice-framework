# Independent B/B' transform pilot review

PASS final worker76350a2216507351cfbcbced2751b706de62025e723a006abfafd4b096b3d6ed. No physical A oracle, B transform, native quadrature or matrix call was executed. This is a source/proof/readiness verdict, not a measured precision or cost result.

## Full mathematical/source review

Read DESIGN, PROTOCOL, PLANNING, all six implementation/helper files, toy/readiness receipts, and the newly pinned identity/transform derivations and review chain. I independently reviewed the preceding elliptic oracle; reuse of that source proof is disclosed. The new192-bit/160-term oracle differs in precision and truncation only, and uses the same outward dual arithmetic and positive value/derivative tails. Its internal legacy1e-12 status label is not the pilot's input criterion: get() explicitly requires BOTH stored widths<=1e-30 before use.

The positive transform follows by Tonelli from integral dt/(X+t²)=pi/(2sqrt X). The derivative magnitude H is positive, and differentiating the rational G expression yields the exact sign and numerator in core.integrands. Applying2/pi and then negating H gives B', not B. Node t intervals are propagated through the full numerator and denominator; dependency overestimation can widen a bound but cannot invalidate it. Denominators containing zero fail honestly. The fixed even Gauss nodes lie inside panels, while s1,2 are endpoints.

Low tails are one-sided with the stated s-dependent bounds. On the disk |z-c|<=c/2, Re(z²)>=0 and |X+z²|>=max(X,c²/4), giving the claimed G/H envelopes. Their common dyadic sum is bounded by50/9. The rho5/2 ellipse fits the disk. A degree2p-1 Chebyshev truncation has sup error at most(10/3)M rho^(-2p); positivity and total mass of the Gauss rule add at most twice the interval length times that error. Hence (20/3)a M and total1000/27 before multiplication by2/pi are correct. The implementation adds this radius on BOTH sides, then applies the interval2/pi factor; it does not count an already normalized radius twice.

The high-tail expansion has positive remainder after16 terms. Cn and En recurrences follow polynomial division and differentiation, with simultaneous assignment correctly using the OLD c in the En update. The native multinomial moments of4sum sin² are exact. The G remainder12^16/(33*8^33) uses X/(X+s²)<=1; H gains1/(2s) from2sX/(X+s²)²<=1/(2s). Interval coefficients are never clamped positive. The final width includes all input, node, weight, pi, moment and low/middle/high errors.

The Legendre code finds12 disjoint sign-change brackets and verifies root completeness against the degree; exact rational bisection and derivative intervals enclose nodes and positive weights. There is no floating eigensolver or unproved root-location rounding. Degree12 and even-node endpoint avoidance are fixed before data.

## Independent bounded checks

24 exact controls used a synthetic three-atom measure on0,3,12: direct G/H values, the same high-tail routine with an injected synthetic moment functional, generic two-node Gauss polynomial exactness and analytic budget constants. No physical moment/integral/oracle was evaluated by these tests. The finite high-tail comparison is supporting evidence; validity of the entire remainder follows the proof above. The author's16 synthetic controls remain honestly scoped. All1893 final source/runtime pins match; strict actual -I-B-S readiness was exercised without calling the body.

## Coverage, retention and runtime

The fixed schedule is31 panels times12 nodes, two endpoint A calls per node, shared between the two s values, plus two fixed A/A' calls:746 oracle rows. Each computed oracle result and timing is saved before its width gate; a gate failure preserves that actual row. Every completed panel retains its cumulative interval, and final rows distinguish CERTIFIED_TARGET from INDETERMINATE using full widths. Output is fresh, no retries or pole/precision retuning occur. The arithmetic body carries an actual59-second alarm, subordinate to the60-second external root contract and384MiB whole-tree measurement. The forecast is explicitly an extrapolation from the previous smaller-precision oracle, not a measurement of this new workload.

Source modules execute only from verified bytes; strict -I-B-S, exact local executable membership and broad runtime pins prevent local shadow/cache substitution. Module origins are checked before and after the body. The inherited unused integration functions are loaded definitions, not invoked by this pilot. Operating-system behavior remains outside file hashes. Failure records preserve stage, completed oracle files and panel history; a failure during a still-running oracle cannot contain a nonexistent returned interval.

## Closure repair and final monitor delta

Original859d lacked the actual load-bearing mathematical proof paths despite copying the arithmetic. Root preserved that version and added PROOF_PROVENANCE plus five exact proof/review input pins. I read the newly bound transform proof and verified all hashes. Every previous source/protocol/receipt file is byte-unchanged. This closes the documentary source-closure finding without arithmetic changes.

The root monitor was previously independently reviewed by Primary0984b64c. I checked only the final affected delta: sourceaf7f56e395459aac0c3f79397383aa6897e05221872a2ad82773b354b9dec61c differs solely in worker freeze and fresh output suffix. ROOT_FREEZE matches. I do not claim a second independent full monitor review. No remaining material blocker was found for root's separately preregistered one-attempt launch.

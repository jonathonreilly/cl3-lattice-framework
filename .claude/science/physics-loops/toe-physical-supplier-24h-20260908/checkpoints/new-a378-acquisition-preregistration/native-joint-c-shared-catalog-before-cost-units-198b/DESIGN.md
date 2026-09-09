# Shared acquisition for the joint C certificate

This separate source version preserves FIXED_CERTIFICATE77e91db0 unchanged. No native geometry, scalar catalog or oracle is read. The earlier 1,016,064 figure counts contractions, not necessary independent oracle evaluations.

The outer integration panels and their32 Gauss nodes are independent of the target s. Acquire one shared2688-point A(t) catalog and one378-point A(s) catalog:3066 evaluations. The fixed contractions remain378*2688=1,016,064 exact interval operations, performed serially with per-pole/panel partials. A streamed scalar catalog is small compared with a dense Gram matrix. Deduplication is optional and cannot increase the census.

## Precision choices

A uniform acquisition radius10^-80 for all3066 points eliminates repeated refinement in the middle separation branch. This is a new precision requirement, not a claim the old160-bit oracle achieves it. Alternatively acquire radius10^-49 first only when a pre-acquisition exact geometry ledger proves every use of that point has |t²-s²|>=2^-80. Every other point uses10^-80 from its first acquisition. The entire tier assignment is frozen before any oracle call; no completed oracle is repeated for refinement.

Near coincidence |t²-s²|<2^-144 requires L((s+t)/2), also to radius10^-80. A prospective exact geometry gate must establish that each target has at most one near node, permitting at most378 additional calls, total<=3444. A sufficient condition is that distinct relevant outer squared nodes are separated by at least2^-143. This is an exact gate to be checked on certified brackets, not a claimed property already verified. If the gate fails or is ambiguous, stop before acquisition and retain the ledger; do not silently exceed the fixed call budget. Exact coincidence uses the same derivative branch. The derivative oracle can return A and A' jointly; no second call at the same argument is needed.

The actual target-node brackets and quadrature t brackets must be refined enough to prove these inequalities and to fit the10^-23 combined node/weight/log/pi/moment allowance from77e91. No oracle call is allowed merely because approximate floating geometry suggests separation.

## Cost proposal, explicitly incomplete

The prior actual catalog took43.21 external seconds for3484 scalar endpoint records (1742 node pairs). The new worst-case3444 evaluation count is comparable, but its10^-80 radius is stricter. A count-scaled inference would be43.21*(3444/3484) seconds only IF cost per new evaluation were no larger; that condition is unproved. A proposed conservative multiplier must be validated by an independently reviewed fixed small precision-cost pilot before any full acquisition forecast is accepted. No numeric runtime cap is claimed sufficient here. Acquisition and million interval contractions should be separate prospective stages, with immutable acquisition output reusable by all targets. Neither stage is a rerun of the previous B protocol.

A minimal readiness stage performs exact geometry and tier/census verification only, without native scalar evaluation. A subsequent fixed pilot samples predeclared smallest, largest and intermediate arguments at the required precision and preserves every result/failure. Only its measured inclusive time and source operation bounds can justify a full serial acquisition contract. Memory384MiB is a prospective cap, not a measured assertion. All calls, tiers and stop rules must be frozen and parent-preregistered separately.

## Correlated B and derivative interface

Store C jointly with the shared cminus certificate and s, defining B=cminus-s² C. Never reintroduce an independently acquired B box into a formula that algebraically cancels cminus. A consumer requiring cminus-B should use the primitive s²C with its common dependency. For B itself, radius is bounded by eta_c+s² eta_C plus node/rounding terms; this can be a poor independent enclosure at large s, where another existing B certificate may be intersected if its provenance is valid.

For derivatives define T(s)=E[1/(sqrt(X)(X+s²)²)]>=0. Then C'=-2sT and
 B'=-2sC+2s³T.

This is an exact correlated representation, but C values alone do not certify T. Its positive integral kernel is E[1/((X+t²)(X+s²)²)]. Away from coincidence it equals [K(s,t)+A'(s)/(2s)]/(s²-t²); at coincidence it is E[(X+s²)^-3]=A''(s)/(8s²)-A'(s)/(8s³). These expressions have cancellation and require their own derivative/jet precision and quadrature proof. Differentiating the already bounded C quadrature error is invalid. Thus the present candidate acquires C and can recover B; a high-precision B' supplier remains a separate extension, explicitly not included in its target.

## Retention and interface

Freeze source, target geometry provenance, complete tier ledger, node/weight bracket certificates, moment proof, and prospective cap before launch. Save current point before parse/evaluation; persist each raw oracle interval before width checks. Save each completed panel and pole before advancing. Final complete status requires exact call census, source rehash, all widths and cumulative budget, and external resource receipt. Failure retains all previous records and records unstarted calls; no automatic retry. Synthetic controls below test algebra and counts only, not geometry, oracle containment or cost.

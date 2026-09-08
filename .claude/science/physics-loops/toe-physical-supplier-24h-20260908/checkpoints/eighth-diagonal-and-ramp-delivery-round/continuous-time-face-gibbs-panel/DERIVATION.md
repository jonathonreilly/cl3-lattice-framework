# Continuous-time single-face conditional: exact target and implementation obligations

Independent theory/design only. No sampling, timing claim or production code. The supplied model is H=V N_F-A on one finite seed-reachable legal plaquette component, V>=0 fixed. Each geometric face label contributes unit offdiagonal amplitude when legal. This is the continuous-time exp(-tau H) free-uniform-endpoint path ensemble, not the previous finite G^n target. It requires its own exact L2 calibration and projector-time convention.

## Labeled continuous-time path measure

A path has initial physical configuration x0, finitely many ordered event times0<t1<...<tk<tau, and geometric labels q1,...,qk. Every event is a LEGAL nontrivial flip; illegal-face proposals and artificial self events are not physical events in this expansion. The configuration is constant between events. Its unnormalized density relative to counting measure on x0 and labels and Lebesgue measure on ordered times is

 exp[-V integral_0^tau N_F(x(t))dt].

This follows directly from the diagonal/offdiagonal Dyson expansion. Summing labels gives the actual adjacency multiplicity. Free uniform bra/ket produce no additional endpoint weight. It is equivalent to the tilted RK jump measure after its holding-rate factor is accounted for, but it is not a normalized RK process without that tilt.

## A valid conditional class

Choose one GEOMETRIC label p with a state-independent law. Let Fp flip that face when legal and fix other configurations. It is an involution. From a labeled path retain ALL non-p event times and labels, even those whose physical flip equals p's flip at L2. Also retain the distinct-state p orbit on every open interval between these retained events. Remove only events with label exactly p. This retained skeleton, including interval orbits, defines the conditional class. The event times alone are insufficient: they do not specify the outside orbit sector.

Each interval orbit has one or two states. A p event can only switch the two members of a double orbit. It cannot create an event in a singleton. At a retained q event, a candidate pre-event state x and post-event state y have compatibility1 exactly when q is legal on x and y=Fq x lies in the next recorded orbit; otherwise0. Thus every allowed candidate has the SAME retained q skeleton and SAME p orbit list, and removes to the same class. This is an actual partition, rather than a state-dependent proposal requiring a missing acceptance ratio.

The old path gives positive conditional support. Zero compatibility alternatives remain excluded. All candidates remain in the same physical component, since they are concatenations of actual legal flips. A seed witness for an initial representative and legal orbit flips establishes this without identifying components merely by flux.

## Transfer representation and coordinate gauges

Fix a distinct-state ordering independently on each interval orbit. If it is a double orbit, the local Metzler matrix is

 B_i = [[-V N_F(x_i0), 1], [1, -V N_F(x_i1)]].

For a singleton it is the1x1 matrix[-V N_F(x)]. Let C_i be the pre-to-post compatibility matrix for the retained label q_i, with entries0 or1. Its row/column dimensions may differ. Because a legal q flip is invertible, C is a partial permutation, not an arbitrary many-to-one multiplicity matrix. The class normalization is the product of exp(Delta_i B_i) and C_i, contracted with ALL-ONES vectors at both free endpoints. The sign/transpose placement depends only on the chosen row propagation convention; one must use it consistently in backward messages and sampling.

Orbital coordinate labels have no physical meaning. If sorted representatives swap across an event, C can be the swap matrix rather than identity. Relabeling an interval conjugates/transforms both adjacent matrices and endpoint vectors and leaves the law unchanged. Never assume compatibility is identity just because both intervals have two members. This is especially important when labels overlap or are L2 aliases.

At L2, the selected label p contributes rate1, not the total multiplicity of all labels with that mask. Other alias labels remain explicit retained events, each with its own0/1 map. An alternative update selecting a whole mask class must instead remove every alias event and put its multiplicity in the offdiagonal rate. Mixing those two conventions changes the target. Equal singleton aliases are avoided by distinct-state coordinates; if artificially duplicated, their event/endpoint measures must be handled consistently rather than assumed harmless in every representation.

Subtracting any common scalar a_i I from B_i multiplies that interval transfer by exp(-a_i Delta_i), independent of the conditional path, so it cancels in normalized draws. This permits using only the N_F difference within the orbit. It does not remove a nontrivial retained-event compatibility factor or allow endpoint pinning.

## Constructive bridge sampling, not just transfer weights

First compute positive backward messages through the finite matrix products and sample interval boundary states and retained-event transitions by their conditional weights. For each interval with fixed endpoint states, draw the continuous p-event bridge for exp(Delta B). There is an explicit positive-series uniformization construction.

Choose lambda>=V max_s N_F(s) for that interval (and lambda>0 for convenience). Put K=B+lambda I, a nonnegative matrix with offdiagonal1. Then

 exp(Delta B)=exp(-lambda Delta) sum_{k>=0} Delta^k K^k/k!.

Conditional on interval endpoints a,b, draw the integer k with probability proportional to Delta^k (K^k)ab/k!. Given k, sample the finite nonnegative matrix-product bridge with K, then draw sorted k independent uniform times in the interval. Diagonal K steps are auxiliary self events and are discarded; offdiagonal steps are actual p events. This gives the exact labeled continuous-time conditional in ideal arithmetic, including intervals with no p event and multiple separated flips. For V0, lambda can be1; the construction still works.

This is implementable in principle but is not yet a finite certified floating algorithm. To invert the unbounded k distribution without bias, use a convergent cumulative sum with rigorous positive tail bounds and sufficient precision until a uniform is separated from the interval. Alternatively prove an exact rejection sampler with a dominating Poisson law. A fixed cutoff, clipping k, or renormalizing a truncated series changes the law. Matrix exponentials alone are not a bridge sampler. Tail cost, rare endpoint conditioning and finite-precision comparisons need explicit review.

One dominating bound is ||K||_infinity<=lambda+1 for V>=0, so the unnormalized k-tail is bounded by the corresponding exponential-series tail. A certified positive lower bound on the actual endpoint transfer converts it to a conditional tail bound. That lower bound may be small; no uniform efficient runtime is inferred. Common diagonal subtraction and an optimized two-state spectral representation can reduce constants, but must preserve the same measure.

## When distant events can be ignored computationally

A sufficient condition is that the retained q flip has disjoint support from p and from every edge on which Delta_p N_F depends. Then p legality is unchanged, q legality is identical on the two p-related states, Fq commutes with Fp, and the q compatibility map is a full bijection between interval orbits. In a transported coordinate gauge it is identity. Moreover N_F differences between orbit members are unchanged, so successive B matrices differ only by a scalar identity. Those scalar factors are class constants and can be dropped. Such consecutive intervals can be merged for conditional-message purposes.

This condition is stronger than merely observing unchanged p legality or a numerical N_F difference in one chosen state. If q validity differs on orbit alternatives, or compatibility is partial, it cannot be ignored. A swap must be transported into the coordinate convention even if no energetic difference changes. The dependency neighborhood is finite: Delta_p N_F depends on faces touching p and the edges of those faces. A selected q whose edge mask intersects that neighborhood is potentially relevant.

Ignoring an event in the two-state transfer computation does NOT delete it from the physical trajectory. The full non-p skeleton must remain available for reconstruction, output legality and observables. One must implement lazy outside-state updates or a local event index and prove that every needed orbit representative/cache is recovered. Building that index initially still costs the total event count. Global NF need not be recounted per event if local differences are maintained and common constants canceled, but this needs actual cache verification.

Hence the proposed per-update cost is proportional to the number of relevant retained events plus the number of newly drawn p events, AFTER a valid local event index and representative transport are built. This is a conditional algorithmic opportunity, not an established throughput or mixing improvement. Whole spatial coverage still requires all geometric faces to be eligible; one face block is not a full sweep.

## Required next gates

Before any stochastic performance fixture: construct a short labeled L2 oracle including alias labels, free endpoints and singleton/double transitions; verify full restricted path masses and coordinate swaps against a direct Dyson expansion or analytic exp(-tau H) reference. Include actual biased controls: omitting compatibility, pinning an endpoint, removing only p events while using alias multiplicity in B, and truncating uniformization without accounting for its tail. Check a distant-event merge against the unmerged product, and a nearby partial-compatibility example that must not merge.

A separate finite continuous-time target/reference and exact time units must be frozen. Actual bridge-tail precision and raw event/endpoint storage contracts precede a cost profile. Only then compare independent-chain physical autocorrelation, initialization and projection-time dependence. Neither partition correctness, acceptance-one Gibbs updates nor removal of old reptation tags establishes equilibration, a ground state, a phase or efficient thermodynamic sampling.

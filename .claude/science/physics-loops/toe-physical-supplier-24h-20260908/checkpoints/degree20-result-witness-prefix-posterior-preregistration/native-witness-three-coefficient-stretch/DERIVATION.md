# Three-coefficient native overlaps and a prospective retained-prefix continuation

Source only; unreviewed. No running or failed package is modified. No actual T, selected IDs, nodes, scalar values, or partial matrix entries were loaded. The failed once-only witness remains failed. This note defines a new arithmetic implementation proposal, not authorization to resume it.

## Exact scalar decomposition

Let I,O,T be the same fixed real seven-star matrices. Write a matrix as its coefficient triple (cI,cO,cT). For a fixed rational pole s and sign sigma, set d_s=(1-s² A_s)/6. Then

 C_sigma(s)=(sigma s A_s, sigma s(A_s-d_s), d_s),
 L_sigma(s)=(-B_s, -(1+s²/6)B_s, sigma s B_s/6).                 (1)

L is the reduced Gamma matrix. The FULL local Gamma overlap is

 -L_sigma(s) - (mu/6) O.                                      (2)

The last term must stay in the local-to-old-frame block. It cancels only in differences of two reduced L matrices. The real stored projector convention remains -i times the physical positive-projector difference.

For any two fixed real source vectors x,y, precompute the three integers

 d(x,y)=(x^T I y, x^T O y, x^T T y).

Then x^T M y is the dot product of this integer triple with the coefficient triple. This is an identity, including T's skew sign. It does not assume that the three matrices commute. Sources are the same e0,dA,dC (at most two nonzero entries for each d). All source triples can be prepared from the fixed five-orbit integer geometry, without native scalar acquisition.

For a new pole s/sign sigma and old pole t/sign tau, with the original nonzero denominator Delta=sigma s+tau t,

 G=(C_tau(t)-C_-sigma(s))/Delta,
 J=-(L_tau(t)-L_-sigma(s))/Delta.                               (3)

Compute these three-component interval triples once for each distinct pole/sign/Gamma combination. Contract with d(x,y), then multiply by the SAME old sqrt(alpha) enclosure. No49-entry divided-difference matrix is needed. The original half/Gamma seed map and its rational coefficients remain unchanged. Equal/overlapping denominators still refuse; no unregistered confluent branch or node shift is introduced.

An even cheaper implementation may contract the numerator first, then divide once. Both are valid outward interval evaluations of the same exact expression. Their interval endpoints need not equal the old endpoints. This is an enclosure implementation change, not a midpoint identity claim. All exact pole values, alpha, scalar uncertainties and final Frobenius/error gates remain the same.

## Cache structure and cost counts

For a fixed orbit, the3x3 source-pair table needs9 integer triples; local seven-site extraction needs21 triples. These are reusable across nodes and both impurity choices. Old scalar triples require2*66 sign entries; new triples require2*378 sign entries. A bounded per-node cache stores the G/J triples only for selected distinct old poles/signs; discard it after the node to keep memory bounded. It contains at most24 distinct old poles,2old signs,2new signs,2Gamma choices,3intervals:576 intervals per case/node. Even allowing all66old poles gives1584 intervals.

The prior raw cross call constructs49 divided-difference entries before taking a sparse source contraction. A direct three-coefficient implementation constructs3 entries instead: a factor49/3 reduction for this particular stage. Caching additionally shares the result across source rows, half-seed components and the two new-source choices. This is NOT a factor49/3 claim for whole runtime: the factored48x7 interval matrix products, input hashing, retention and schema costs remain.

The maximum original half-seed expansion is48 selected columns times2 raw components=96 raw labels per source row. With4new source/sign rows, at most384 raw cross requests per node. Their old full-matrix path builds at most18816 scalar divided entries; the selected-pole cache builds at most576, before sparse triple dot products. Appended local/Ward labels need their existing specialized formulas, not G/J. A new implementation should separately count cross requests, unique triple keys, triple contractions, matrix summands and durable records; it must not infer speed from the reduced stage alone.

The parent reports the failed run retained cases00..02 and case3's completed210-node panel prefix at299.83 seconds. This is a cost warning, not a price for the new kernel. No new measured runtime or unconditional300-second completion claim is made here. A bounded synthetic comparison or conservative reviewed inference is required before the successor's execution forecast is frozen.

## Prospective continuation boundary

A successor may authenticate the old failure receipt, frozen source and every retained output hash, then import completed cases00..02 without recomputation. For case3, a separately verified stage prefix ending at completed=210 means nodes0..209 are already accumulated; resume at index210, not209. Import the retained direct/mixed interval accumulators and the same local/factorization records. The new outward expressions may safely extend those old interval accumulators because both enclose the same exact summands. Do not subtract old contributions, recenter old intervals, or recompute completed nodes.

Complete cases4..9 afterward under a new fixed cap and preregistration. A schema must prove the exact saved stage prefix and reject missing/future/duplicate panels, source identity changes, or a mismatch of case/orbit/impurity. The first three case arithmetic truths are explicitly inherited from the old reviewed adapter and any new saved-prefix reconciliation, not newly computed by this kernel. The old failed root is not promoted to COMPLETE. A new final acceptance would concern the composite authenticated prefix plus new continuation only.

The frozen next protocol still needs an independently reviewed concrete cache implementation, cost gate, exact failed-prefix binding, source closure, output schema and once-only execution authorization. This note supplies none of the missing physical values and does not assume that any coarse exclusion gate passes.

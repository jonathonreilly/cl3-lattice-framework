# Fresh paired endpoint/order design, pending cost profile and authorization

No stochastic profile or production is authorized here. The measurement implementation is deterministic and independent of the sampler. It adds no physical interaction. The supplied operator is the elementary-plaquette H(V), with V=.95 or0, on L8. At V0 it matches the leading native fourth-order ice kinetic operator after the explicit Zpi basis change; finite-g/higher-order errors remain separate. The soft full-carrier supplier removes the necessity of a hard low projection at that order, not the supplied comparison model or ice trial domain.

## Fixed proposed arms

Four fresh arms: V=.95 and0, each at tau12 and36. Proposed16 independent chains per arm, RK2048 propagated initialization, burn32n and32n measured attempted updates, n=2M tau, M=1536. All seeds must be newly fixed before the authorized profile/production freeze; reuse of old outcomes or chain streams is forbidden. This gives a projection contrast within each endpoint and an endpoint contrast at each projection time. It does not supply a second burn/initialization comparison: memory/split diagnostics can fail it, but passing them cannot establish equilibration. If the cost permits an initialization control, that must be chosen before any physics run rather than added after favorable or adverse endpoint data. A second seed family must have a demonstrated legal path into the same component before being called a same-component initialization control.

Pairing means the same preregistered seed index is used across V/τ arms; it does not mean trajectories remain equal after their transition laws diverge. Preserve the entire per-index four-arm vector and use its actual joint covariance for differences. If an arm is absent or invalid, do not silently replace its index or use a reduced paired sample. Whole chains are the independent units; segments and batches are not replicas.

## Measurement cadence and cost gate

Full order measurement is O(N) per snapshot. Do not blindly recompute it on every one of the millions of elementary reptation updates. Proposed fixed cadence is M attempted updates after burn, with an offset cid mod M, retaining equal snapshot count per chain because32n is divisible byM. Take the nine spectral/residual moments and145 order entries at the SAME snapshots so their joint influence covariance is directly available. This differs from the old every-update estimator and requires a fresh profile; it targets the same stationary path law, not the same finite-chain trajectory average. Large stride does not certify independence or remove lifted-chain trapping. Sixteen fixed within-chain batches remain diagnostics.

One future authorized end-to-end profile must include initialization, actual update work, snapshot measurements, batching/serialization and checkpoint overhead; timing only a numerator kernel is insufficient. First try exact existing core plus literal full snapshot measurement, with no speculative incremental cache. The previous update-only .95 cost is a lower bound, not a forecast for this design. Proposed overall ceiling is four hours with180s/384MiB segment caps and20% forecast headroom. If the largest segment does not fit, revise segment length prospectively with the reviewed resumable machinery; do not count segments as independent chains or trim coverage after outcomes. No profile has run.

## Exact normalization and schema

N=L³. The eight fixed momenta are k=πb, b∈{0,1}³ in lexicographic order. For each k and a=0,1,2,

  m_a(k)=N^-1 sum_r epsilon(r)(x_(r,a)−1/2)exp(ik.r).

For each plane ab in(01,02,12),

  f_ab(k)=N^-1 sum_r F_ab(r)exp(ik.r).

Corner amplitudes are real on integer anchors. Store the signed24 electric amplitudes, signed24 face amplitudes, their24+24 squares and24+24 fourth powers, then plane anisotropy=sum_ab[f_ab(0)−mean_plane f(0)]²:145 entries. Do not replace mean(m²) by mean(m)². The normalized intensities are bounded electric≤1/4 and face≤1; unnormalized structure factors would multiply them byN and must be labeled separately. In an ice state m_a(0)=Phi_a/L² exactly. In a fixed zero-flux component this entry is identically zero, not evidence against all order. The positive f_ab(0) background is not translation-breaking order; use nonzero momenta for that question and orientation anisotropy for cubic-rotation breaking.

At finite volume a symmetry-invariant ensemble can have zero signed order amplitude even when its distribution is broad; therefore retain squares/fourths. A Binder-style ratio is descriptive only and must be invalid when its denominator is unresolved or zero. A single L8 point supplies no Binder crossing, thermodynamic order parameter or exhaustive ordering search. The corner menu misses incommensurate and more elaborate unit cells. Rotation/translation covariance of the implemented menu is tested, but no symmetry pooling of raw channels is automatic.

## Statistical gates and interpretation

Retain all raw chain/batch vectors, same-time nine moments, accepted-run/tag history, and negative variance estimates. Publish full chain covariance and covariance-of-mean (divide by16), paired endpoint/projection contrasts and ratio influences. Nominal4SE consistency/contrast rules and ten-percent4SE/D precision may be carried forward only if frozen before data. Order contrasts should be reported with simultaneous multiplicity explicitly acknowledged; no post hoc 'largest significant channel' selection is a phase verdict. Record all channels, not only flagged ones.

The strongest possible result of this small design is a resolved finite-projector endpoint change accompanied by explicit candidate order distributions, or a failure/indeterminate diagnosis due to memory, projection dependence, precision, component trapping or residual uncertainty. D/R remain finite-ψ quantities; raw nonequilibrated samples cannot be assigned an inferred exact ψ. No photon pole, phase continuity, ground-state convergence or bulk confinement conclusion is licensed. Additional sizes, flux-sector control and a broader order search would be separate obligations.

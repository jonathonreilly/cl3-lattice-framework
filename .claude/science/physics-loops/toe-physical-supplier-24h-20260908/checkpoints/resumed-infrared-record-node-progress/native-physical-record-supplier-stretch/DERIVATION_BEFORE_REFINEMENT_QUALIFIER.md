# Constructive local correction for a full-carrier native edge Record

Prospective theorem, before the finite controls. Supplied premises: finite simple ordered native edge graph, ordinary tensor composition, the phase-correct8038 dictionary, and the stipulated physical Z/Born Record instrument. No formation probability, rate, covariant role placement or axiomatic Born rule is supplied by this construction. It applies to arbitrary full-carrier states, including coherent Wilson-sector superpositions.

Use8038 conventions: W_G|x>=d_G(x)|∂x>_f|x>_g, d_G(x)=(-i)^|x|(-1)^q_G(x), M=w⊕ell, q=Σe<f Mef xe xf. For e=(i,j), i<j, w_e is its ordered-star mask and ell_e is the sum of incidence rows from i through j−1. Native A_e=X_e Z_{w_e}; enlarged A_e=(-iγ_iγ_j)X_e^g. Relative orders on surviving edges and neighbor lists are inherited after deletion.

Write x_e=a∈{0,1}, z=(-1)^a, G'=G−e, and y for the remaining electric bits. The raw contraction L_e^a=<a|_e maps the all-positive Gauss space of G into the charged Gauss space on G' with charges z at i,j. This is the most direct gauge-correct map: retain these two signs as record content. Every old Record is unchanged. The maps have complete effects (L_e^a)†L_e^a=Π_e^a on the constrained input.

If an all-positive Gauss frame on G' is desired, let C_e=-iγ_iγ_j. It is an even Hermitian involution and flips precisely the two endpoint Gauss signs. Thus (C_e)^a L_e^a maps into the all-positive sector. It is an algebraic frame correction; it is not asserted to be a permitted standalone gauge-invariant operation on the original G physical space. Its conjugation also changes the endpoint occupation convention, so the original number observable must be transported rather than renamed as the new bare number.

## The local cancellation identity

Define D_e^a=(Z_{w_e restricted to E−e})^a on surviving native edge qubits. Then, column by column,

    C_e^a L_e^a W_G = W_{G'} D_e^a <a|_e.                 (1)

For a=0 the restricted phases agree. For a=1, M_G restricted to surviving rows/columns equals M_G' because removal preserves neighbor orders and incidence restrictions. Hence

    d_G(y,1)/d_G'(y)=(-i)(-1)^(Σf≠e Mef yf).

The fermion occupation before correction is n=∂y⊕e_i⊕e_j. Direct CAR gives C_e|n>=-i(-1)^(Σi≤v<j nv)|n⊕e_i⊕e_j>. The interval contains i and not j, so its extra endpoint contribution is1. Multiplying the two phases yields

    (-i) i (-1)^((M_e⊕ell_e)·y)=(-1)^(w_e·y),

which is exactly D_e. No uncancelled long Jordan–Wigner string survives in this native correction. Its support is within the two endpoint stars, at most deg(i)+deg(j)−2 edges. It is a product of commuting native Z phase operators; using it as physical feedforward would still require a supplied control law. Equation(1) itself is a dictionary/state-action theorem without that control assumption.

## Complete instrument and adjacent-history phase

The corrected native Kraus map is K_e^a=D_e^a<a|_e. It is a coisometry from its outcome subspace to the surviving full native carrier and Σa K_e^{a†}K_e^a=I. Arbitrary initial states have arbitrary legal Born outcome probabilities; the fixed-cycle nonbridge fair-isometry result cannot be extended to them. For example an electric basis state fixes every outcome, even if e lies on a cycle.

For two different edges e,f and outcomes a,b, compare the corrected maps in the two orders, inheriting all surviving orders. Their final diagonal factors on the remaining edges agree. The only discrepancy is the phase from the first correction on the edge that is subsequently recorded:

    K_f^b K_e^a = (-1)^[ab(w_ef+w_fe)] K_e^a K_f^b,

where both sides identify the same final output ordering. Native A commutation gives w_ef+w_fe=1 exactly when e,f meet, and0 otherwise. Consequently the branch CP maps commute exactly even when the Kraus amplitudes acquire a minus sign. The sign cannot be dropped in a coherent history dilation; it is an outcome/history-dependent scalar cocycle. Adjacent transpositions generate the full permutation relation, so the sign for any order is the parity of inversions among recorded-one edges that share a vertex. This gives a complete computable history correction rather than an assumed phase-free composition rule.

The raw charged-sector deletion maps commute as actual contractions. Choosing positive-Gauss frames trades that simple composition for the explicitly tracked projective sign. This distinction explains why a correction is needed and does not introduce a physical gauge anomaly.

## Indexed refinement supplied and unsupplied

For any finite recorded set R, the ordinary commuting native projectors produce a consistent family of CP instruments indexed by outcome words, with exact marginalization over finer outcome lists. The local corrected version is unitarily equivalent branchwise and remains refinement-consistent after transporting observables into the same final frame; its branch CP maps are order-independent. This provides an explicit finite physical-carrier instrument refinement, not merely a scalar menu. It does not derive which set R forms, a nearest-neighbor admissibility law for the quantum state, a scheduler, or a permanent-record dynamical realization. Those remain the precise external supplier obligations.

Novelty scope is limited:8038 already maps the effect and8037/main already give selected fixed-code instruments. The proposed increment is the local cancellation(1), full-carrier charged-frame update and all-history projective composition. If a prior source contains these formulas, the result should be treated as a reconstruction rather than a new milestone.

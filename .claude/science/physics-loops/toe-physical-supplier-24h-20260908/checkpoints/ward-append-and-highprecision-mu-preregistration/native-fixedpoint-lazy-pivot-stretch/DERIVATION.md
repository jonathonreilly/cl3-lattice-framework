# Fixed-point interval alternative for the common lazy pivot design

Independent source review of native-common-lazy-pivot-runtime-design/DESIGN.md and contracts.py, plus the unchanged exact lazy reference in native-common-symmetric-pivot-compression. No native or full mock matrix/pivot run. The design correctly separates raw half-column residual weights, physical input intervals, finite coordinate errors, and a fixed resource cap from rank exhaustion.

## Review conclusions and normalization

The design uses HALF combinations, not the normalized1/sqrt2 chiral combinations of some earlier prose. With v_eta=(y_plus-eta*chi*y_minus)/2, y_plus=v_plus+v_minus and y_minus=chi(v_minus-v_plus). Therefore sum of original pole squared residuals is twice the sum of half-column squared residuals. A raw appended x=e0/2 or w/2 is already one column and gets weight1. The actual augmented residual is2 sum pole-half diagonals+sum append diagonals. Its operator certificate sqrt(1062r) agrees with the reviewed trace531/2. No factor2 is applied twice to append rows. The contracts.py helper implements this precisely.

The198-pair cap is correctly described as a resource cap, not dimension exhaustion.399 candidates can support399 orthonormal Gamma pairs. Positive lower pivots and upper residual trace are needed; midpoint PSD or a small numerical rank does not certify them. The source-only proposed design makes no contrary claim.

## Fixed dyadic endpoints eliminate denominator growth

Use intervals [l,u]/2^b with signed integer endpoints, b fixed prospectively (192 is a candidate, not a successful conditioning claim). Addition/subtraction are exact endpoint operations. Multiplication computes four integer products, floor/ceils after division by2^b. Division with a positive denominator interval uses all endpoint ratios with outward integer floor/ceil; reject lower endpoint<=0. Square root uses integer isqrt of endpoint*2^b, raising the upper endpoint if needed. None of these operations stores an accumulating rational denominator.

Let the original G,J entry oracle enclose the exact PHYSICAL Gram of the half/append columns, with source symmetry labels validated first. It includes scalar uncertainty and cache arithmetic, not merely the midpoint cache. For previously selected exact residual rows g_l,j_l and exact positive pivots r_l, reconstruct an interval row using

 G_ij=G0_ij-sum_l(g_li*g_lj+j_li*j_lj)/r_l,
 J_ij=J0_ij-sum_l(g_li*j_lj-j_li*g_lj)/r_l.

All products and ratios are interval operations. By induction these enclose the exact orthogonal-projection residual for the concrete sequence of selected indices. The selected sequence need not match exact maximum-diagonal pivoting: selecting any index whose interval lower diagonal is positive is valid. Choose maximum certified lower diagonal with fixed label tie-breaking for reproducibility.

Compute each candidate diagonal lazily from the ORIGINAL entry and all saved rows, rather than recursively subtracting already widened diagonal intervals. Intersect the two independently valid pivot-diagonal enclosures if both are available. Their intersection must be nonempty; it may certify a positive pivot more tightly. Record the interval actually used as r along with row intervals BEFORE later gates. Coordinate output is g/sqrt(r),-j/sqrt(r); the minus sign is essential.

Exact mathematical structural zeros (J diagonal, forbidden chiral blocks, or entries annihilated by a previously selected exact projection) may be imposed only after the original labels/symmetry premises were checked. A negative upper diagonal is a failure, not zero. A lower bound below zero is merely uncertainty and cannot create a positive pivot. No midpoint replacement, unreviewed higher-precision retry, or pivot skipping after a failed division is allowed.

## Bounded storage arithmetic is not a width theorem

For exact residual columns, Cauchy-Schwarz gives |Gij|,|Jij|<=T with T=531, since the half/append total trace is even smaller. Thus interval enclosures may be intersected with the proven box[-T,T], and diagonal enclosures with[0,T]. This is a justified interval intersection, NOT clipping a negative upper bound or inventing positivity. An empty intersection is FAILURE. Record whether intersections occurred so the use of the analytical bound is auditable.

After this intersection every saved row endpoint has at most b+ceil(log2(T+1))+1 bits. A positive dyadic pivot lower bound is at least2^-b. A product numerator before rescaling has O(2b+log T) bits; a divided term has at most O(2b+2log T) bits. Summing k terms adds O(log k) bits before the final interval intersection. Consequently integer bit length is bounded by a fixed expression in b,T,k; Fraction denominator explosion is removed. O(kn) saved endpoints and O(k²n) arithmetic remain. This does NOT prevent cancellation-driven interval width growth or PRECISION_STALL. A minimum pivot floor may be added only prospectively; it is a resource/conditioning refusal, not a theorem about native pivots.

## Rigorous finite coordinates

Choose dyadic coordinate midpoints and outward radii after dividing by the outward positive root. Let d_half² be the exact sum of squared radii over the two rows per selected pair. Reconstruct original pole coordinates by the half-column transform. A safe Frobenius error bound is

 d_raw² <= 2 sum_(pole-half coordinate entries) radius²
          +sum_(append coordinate entries) radius².

The factor2 follows from the orthogonal sum/difference identity; interval addition can be used directly if tighter. It is not2 on every entry. With exact raw coordinate matrix U, ||U||F<=sqrt(531/2)<17, and any actual raw coefficient ||C||<=1,

 ||U C U^T-Uhat C Uhat^T||1 <=34 d_raw+d_raw².

Thus a prospective d_raw<=1/40000 gives less than.001 coordinate error per impurity. Coefficient uncertainty adds ||Uhat||F²||Delta C|| and is separate. The residual compression certificate and coordinate-error certificate can each fail independently. Accurate residual diagonals alone do not certify usable coordinates.

When physical entry intervals drive direct pivots, the resulting compression certificate concerns the actual native input columns already. Do not charge the same scalar uncertainty again as though the selected exact physical rows were only midpoint rows. Any separate rounded/dilated physical operator approximation must be explicitly distinguished in the final triangle inequality. The source design correctly calls for that distinction; implementation should name which exact object each coordinate interval encloses.

## Prospective implementation and cost boundary

A fixed-point reference module can expose original_entry(i,j), residual_row(i,history), diagonal(i,history), weighted_trace, and coordinate_intervals. A bounded LRU cache reader retains immutable original192-bit entry enclosures; every saved pivot row/radius remains exact integer data. A later four-step once pilot must include actual source hashing, index creation, all399 diagonal reconstructions, row I/O, scalar inflation, clipping audit, persistence and coordinate norm scan. No such pilot is authorized here and no runtime is inferred from bit bounds alone.

This closes the arithmetic-representation objection to a bounded fixed-precision attempt. It leaves genuine pivot conditioning, attainable residual rank, input precision and actual generator representation unresolved. No native values are evaluated in this note.

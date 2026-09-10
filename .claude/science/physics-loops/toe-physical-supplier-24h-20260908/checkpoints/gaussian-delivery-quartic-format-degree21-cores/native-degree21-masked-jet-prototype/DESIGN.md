# Disabled p2/q1 masked-jet implementation proposal

This new folder implements the reviewed source closure43638641 and generalizes multivariate core440bac1c. It contains no native loader, accepted arrays, actual q fit, scientific dispatcher, authorization, or execution proposal. No completed protocol is replayed. Parent proof review38b760 confirms the reflection and scalar budget. Arithmetic.py and radial.py are unchanged copies of the earlier bounded primitives/formulas.

## Literal masks and matrices

core supports only nominal21=(2,2,1,1), width4, and inner21=(2,2,4), width3. assembly.defects fixes the matrices; callers do not infer signs from adjacency. Nominal source order is(a,d_A,d_C,ha), with left exponential V_C, center-reflected V_a, marker/right V_A. Its relative product is exp((t+s+z)h) exp(-t(h+V_C)) exp(-z(h+V_a)) exp(2wV_A) exp(-s(h+V_A)). The center defect has(0,1)=-2i,(1,0)=2i,(0,3)=(3,0)=-2. Inner source order is(a,d,hd), with relative product exp((t+s+z)h) exp(-t(h+V)) exp(-z(h+V_d)) exp(-s(h+V)); V_d has(0,1)=-2i,(1,0)=2i,(1,2)=(2,1)=-1. Same E0 and the outer factor8 in source moments are retained.

Exact word collection removes free-only coefficients. The analytically zero one-defect trace is excluded before projected-table lookup. Linear sectors remain in higher log products. Generalized indexing uses the literal source width, without Gram inversion or an independence assumption. Endpoint support/query caps remain checked.

The shifted tables use the exact signed radial formulas. Nominal maps four sources to(a,d_A,d_C) with shifts(0,0,0,1), freepower<=4, so maximal odd radial order5 and even6. Inner maps to(a,d) with shifts(0,0,1), freepower<=6, so odd9/even10. table_check exercises only formal lookup indices with a fabricated sequence, not physical moments.

## Fixed candidate strategy, frozen before native fitting

The only new q proposal is the midpoint normal-equation solution of Hq=(s1,s2), H=(s2,s3;s3,s4). It is attempted only when midpoint s2 and determinant are positive. Each coefficient is clipped to[-16,16] and rounded downward to the2^-64 grid. Nonpositive midpoint/cap refusal falls back to the old exact constant q. Candidate0 is ALWAYS(old_q,0); a distinct proposal is candidate1. No continuous optimum is claimed.

Both candidates are reevaluated on the FULL certified s0..4 boxes. The selected candidate has the smaller certified eta² upper endpoint; ties choose the old constant. A negative upper is a discrepancy, not a zero. Choosing q on this criterion does not guarantee a better Ward sign. The unchanged first error still propagates as sqrt8*u/delta. The polynomial and its exact descriptor must be retained before evaluating the new nominal.

The strategy is identical for both P/O classes and both already-fixed p modes. No saved q values, native moment arrays or actual midpoint solve were used to choose the strategy.

## Complete new arithmetic paths

assembly.new_inner reconstructs ONLY s3,s4 from the45-coefficient inner jet and fixed p, using8*(-1)^(i+j+k)*i!j!k!. Accepted s0..2 are supplied unchanged; no old source-moment replay occurs. assembly.choose computes the signed residual and new q-trial norm from all five s boxes. assembly.nominal forms the36-coefficient ordered nominal with correct z sign and no extra marker factor. The source signatures, in literal(left C,right A,opposite,count) order, are(P,P,1,48),(P,P,2,12),(P,O,0,12),(O,P,0,12),(O,O,0,6).

certificate.finish aggregates the NEW nominal, NEW q-trial norm, channelwise coupled F and posterior error. Its first-squared bounds and old a² must belong to the same p. An old physical-target alpha interval may be intersected only after this entirely new-q certificate is formed; an old numerical nominal is never substituted. All raw forms and final intersection are emitted before nonnegative/intersection gates. There is no sign promise.

The two inner jets and five nominal jets are independent of the trial coefficients and may serve both modes. Both modes require72 new inner contraction terms and270 nominal contraction terms, plus bounded q/posterior arithmetic. No additional scalar supplier is needed beyond the reviewed omega9/evenR10 closure.

## Retention and finite counts

The final core emits, in deterministic total-degree/lexicographic order:

1. operator_matrices(A,Q) BEFORE trace, then operator_coefficient(trace/counts);
2. for each log power, log_power_matrix BEFORE trace, then log_power_trace;
3. all final log_coefficient values, then jet_coefficient values.

Sparse matrices are canonical sorted rows[i,j,complex_box] with literal integer indices and256-grid endpoints. Each nominal jet emits286 core events; each inner emits448. Five plus two yields2,326 core events before trial/summary callbacks. Maximum retained sparse matrix rows are10,128 per nominal and14,580 per inner. A future worker MUST stream callbacks; collecting all native events in memory is not an accepted implementation. At the4096-bit endpoint cap, a conservative5000-byte row bound gives approximately399MB total matrix JSON across seven jets, plus event/scalar overhead. Actual endpoints may be much shorter, but that is not assumed. A future protocol must price and bound output retention explicitly before launch; no silent matrix omission is permitted.

Proof-level dense bounds remain27,498,378 complex products across seven jets, at most439,974,048 endpoint multiplications, with under15,000 live complex boxes if jets/matrix families are released sequentially. Four4096-bit endpoints per box have under31MB packed payload, before Python and stream overhead. Stored dyadic endpoints4096bits and multiplication temporaries8193bits are unchanged. Proposal rational operations have a16,384-bit stored cap, staged binary operations, and less than65,536-bit transient storage; converting a coefficient to the dyadic primitive may refuse at its stricter input cap. There is no unsupported low-precision approximation.

No native resource ceiling is selected. Full source bindings, durable caller lifecycle, runtime serialization cap and independent root review remain necessary. These modules do not open scientific files.

## Exact synthetic profile and limits

check.py ran two fabricated reflected Hamiltonians and five fabricated nominal Hamiltonians on four exact rational Majoranas. These are NOT the five native geometric signatures. Direct4x4 Fock power products independently enclose all270 requested coefficients; the assembly comparisons also verify new s3/s4, selected trial residual/norm and nominal. There were282 checks. The complete synthetic mathematical profile took6.445 seconds with process ru_maxrss21,463,040 bytes on this host; measured complex products were1,865,080 across the seven jets. Native conditioning, hashing and native tables were absent.

That profile preceded the final output-only matrix-retention delta. PRE_RETENTION_CORE.py.txt preserves its exact code. Arithmetic is unchanged by the delta; retention_check exercises both complete final event schedules on zero synthetic Grams, matrix-before-trace ordering, and posterior intersection failure. Consequently the6.445s/21.5MB measurement must NOT be represented as a full final-output runtime profile. TABLE_CONTROLS confirms the literal source-index budgets without acquiring moments. No actual q fit or native/saved scientific replay occurred.

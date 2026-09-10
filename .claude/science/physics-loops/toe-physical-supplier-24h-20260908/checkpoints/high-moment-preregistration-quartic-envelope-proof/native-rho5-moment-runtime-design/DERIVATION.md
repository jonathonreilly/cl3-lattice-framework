# New rho5 saved-component moment certificates

Status: source-only conditional design; actual adapter NOT_READY. No refined numerical interval is supplied. The reviewed rho5 ellipse proof is imported explicitly, with the same native dispersion measure, A0<=17/60 and derivative bound. Original rho4 executions remain immutable.

For cminus, mu, nu the integrated functions are respectively A(t), 1-t²A(t), and 6-t²+t⁴A(t). All carry the factor 2/pi. The new analytic quadrature radii are (85/6,50,300)*5^-52. No final width is rescaled.

## Retained numerical family

These completed moment computations used interval Gauss sums, not single midpoint node centers. Reuse means retaining those exact saved panel interval endpoints (equivalently their exact centers AND input/rounding radii). There are 67 panels of 26 nodes; the future adapter must authenticate the completed execution AND full-node post acceptance for each source. The post certificates justify the saved panel input/rounding bounds. This program reconstructs every panel cumulative with the original directed192 addition. It does not recompute the 1742 node functions or assert independence of those inherited bounds.

Low intervals are reconstructed exactly: eps=2^-64, cminus [eps*A_first_lower, eps*(A_first_upper+3*t_first_upper)], mu [eps-(17/60)*eps³/3,eps], nu [6eps-eps³/3,6eps-eps³/3+(17/60)*eps^5/5]. The first node's authenticated interval must lie strictly inside [eps,2eps]. Thus cminus needs a minimal authenticated first-node record; no new oracle.

High partials are independently recomputed from the exact multinomial return moments M_j. For observable index k=0,1,2, the 40 terms are sum_{n=0}^{39} (-1)^n M_{n+k}/((2n+1)8^(2n+1)), with positive remainder 12^(40+k)/(81*8^81). Moments through41 suffice. These sums are NOT executed during preparation. The same positive-tail interval is retained, with no new remainder centering convention.

The old analytic radii are exactly (544/45,128/3,256)*4^-52. Reconstruction of the original output from saved middle, original low/high, original radius and independently reconstructed Machin pi must match exactly. This is a source-family check, not a claim to rerun the old physical integral. Then only the radius is changed. The same two outward192 additions and outward192 multiplication are applied, preserving the original rounding rule and per-operation error budget (each endpoint at most 2^-192). Numerical rounding residuals may differ with the changed radius; no claim that those residual numbers are identical. All inherited middle rounding stays unchanged. Interval monotonicity proves the new interval is contained in the old one. Fixed new target is full width <=2e-28 for each of three observables, with an explicit false target outcome allowed.

## Authentication and boundedness

A future normalized adapter must map the dual source PANELS values/cumulatives columns 0/1 and nu PANELS value/cumulative to this API. It must bind every source/result/TAIL/PI/PARTIAL/root receipt/root acceptance/full-node post and transitive source closure, then compare saved old intervals, low/high/radius and middle exactly. It must authenticate first-node t/A against the same original catalog. This adapter is deliberately absent: load_actual always refuses. No caller-created snapshot is itself an accepted physical certificate.

Source operands and stored endpoints are capped at32768 numerator/denominator bits. At most65536-bit products plus192-bit directed shifts are transient. The fixed finite moments are small relative to this ceiling; the future adapter must enforce exact canonical scalar syntax before Fraction parsing. Prospective work is 201 panel additions, three40-term tails (at most4100 small multinomial summands per tail moment), three final interval reconstructions, plus streaming input hashes. There is no measured fit or active resource contract. A future source-reviewed once-only 30s/384MiB proposal must price authentication/I/O and retain current component before a failed check. Existing emit callbacks must durably serialize before return; repeated stages require append sequencing. Native execution remains disabled pending that runtime and preregistration.

## B extension excluded

The B66 new-center computation is not yet accepted. Later reuse would require its exact coefficient midpoint centers and centered-tail family plus accepted node radii. Its distinct G/H analytic radii cannot be substituted using this moment adapter. No B certificate or width gain is claimed here.

## Controls

23 source-only synthetic predicates cover multinomial moments0..3, retained interval nesting, wrong old radius/middle/high/output rejection and disabled loading. Synthetic tests explicitly replace tail() with a toy partial/remainder, so they do not execute native moments40 or actual high tails. They are arithmetic controls, not independent physical validation. Author previously implemented related rho4 runtimes; independent source review remains required.

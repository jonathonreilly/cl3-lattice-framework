# Prospective rho4 B66 precision ledger

SOURCE ONLY, NOT_READY. This is a new certificate method and prospective saved-data diagnostic. No actual catalog/geometry/pole scan, oracle, integral, moment40 computation or old worker rerun has occurred. The intended inputs are the unchanged66 exact midpoint poles and1742 accepted A-at-Gauss-node intervals, with their original mapped weights and accepted pole A/A' enclosures. The future binder must authenticate all actual source/ROOT/POST chains. Targets are full widths2e-28 for B and2e-27 for Bprime, not radii and not already achieved.

The reviewed rho4 bound reduces the analytic radius for both integrands to R=128*4^-52 before2/pi. It does not tighten individual A or A' certificates. B is a dominant input in the old selected Gram error ledger at the previous1e-19 radius scale. Whether these new widths suffice for a24-pair certificate still depends on selected-frame conditioning; no such success follows from scalar widths alone.

## Fixed family, separation and node error

For exact s>0 and interval t, put a=s²,b=t²,d=b−a. The future ledger must check all114972 (66×1742) interval denominators exclude zero. A failed separation is a completed diagnostic failure/indeterminate branch, never permission to insert the coincident formula. No adaptive refinement or changed node family is allowed.

At d!=0 the exact integrands are
 G=(b/d)At−(a/d)As,
 H=2s b(As−At)/d²+(a/d)A's,
with B=(2/pi)int G and Bprime=−(2/pi)int H. H is positive. Compute outward interval coefficients at the whole t interval. For coefficient interval c with midpoint c0/radius zc and scalar interval x with midpoint x0/radius zx, the product center c0*x0 has radius at most max|c| zx+zc |x0|. Sum this for the two G and three H terms. This includes node coefficient displacement, actual A-node uncertainty and pole A/A' uncertainty. A-node enclosures must already contain A at the same true quadrature root. No nominal1e-30 substitution is made.

With mapped weight midpoint w0/radius zw, use weight-upper times the node radius plus zw*M, where true G<=A0<=17/60 and true H<=−A'(s)<=3. This corresponds to an explicitly defined approximate quadrature center w0 times the node center, with safe error decomposition w0(center−true)+ (w0−true_weight) true; using weight-upper is conservative. Add all node radii and the declared fixed arithmetic allowance. This is a conservative sum, not a lower precision floor. Shared-input coefficient collection may later reduce it under a separately proved protocol.

## Low tail subtraction

Let epsilon=2^-64. Since G_s(0)=As and H_s(0)=−A's,
 0<=epsilon As−int_0^epsilon G<=epsilon³ A0/(3s²),
 0<=epsilon(−A's)−int_0^epsilon H<=2epsilon³ A0/(3s³).
These follow by subtracting denominators: G_s(0)−G_s(t)<=t²A0/s² and H_s(0)−H_s(t)<=2t²A0/s³. Center each tail at epsilon times the pole scalar midpoint minus half the displayed remainder bound. Its radius is epsilon times the scalar radius plus half the remainder. Use the exact s midpoint; if the family were whole pole intervals instead, take the positive lower s and account scalar/coefficient displacement separately. That is not a silent family change.

## Forty high terms and the potentially decisive amplification

For high t>=8 define J_j=E[X^j/(X+s²)]. The exact recurrence J_0=As, J_j=M_(j−1)−s²J_(j−1) yields40 terms J1..J40 for G. The positive integrated remainder is <=M40/(81*8^81)<=12^40/(81*8^81). For H coefficients −partial_s J_j, the analogous positive remainder is <=12^40/(81*8^81): use2s/(X+s²)<=1/sqrtX, then X40.5/(X+s²)<=X39.5<=12^40. This is deliberately conservative.

Crucially, forty terms can amplify pole-input uncertainty even though their analytic remainder is smaller. Collect the exact coefficient of As in the integrated partial:
 K_N(s)=sum_(n=0)^(N−1) s^(2n+2)/[(2n+1)8^(2n+1)], N=40.
The G partial contains −K_N As. Its input radius is K_N etaAs, since moment values are exact. The H partial contains K_N' As+K_N A's, and has input radius <=K_N' etaAs+K_N etaAprime. All signs in K are positive; blindly treating each recurrence step as a fresh interval is no improvement. At a hypothetical s=16, successive high-order factors grow roughly4 per term. This warns of a genuine information-amplification risk for this representation, not an actual statement about a saved pole or a universal lower bound on achievable B precision.

The prospective ledger must calculate these coefficient sums at all66 fixed poles before any high-moment evaluation. A failed budget cannot be rescued by more fixed-point bits alone. Possible NEW alternatives include a differently centered moment expansion for large s, a stable high-tail representation, or coefficient collection across middle/low/high regions retaining the same shared As. None is implemented, executed or claimed successful here. Actual complete-integral cancellations may reduce sensitivity beyond this conservative separated ledger.

## Total target and fixed diagnostic scope

For each pole compute node error sum, low input/remainder, K/K' high input amplification, high analytic remainder, rho4 radius and a fixed arithmetic allowance. Multiply total radius by4/pi_lower to get full width, then add a separately proved pi allowance. Under declared1/128<=s<=16, A0<=17/60 and |A'|<=3, a1e-35 full-width pi allowance is safe for the reviewed Machin32/10 enclosure and crude integral bounds below2^25. Final contraction arithmetic is not yet implemented; reserve1e-35 unscaled radius provisionally and require a future operation count and an actual bound no larger than this reserve.

A prospective ledger result is FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE only if ALL66 B widths<=2e-28 and Bprime widths<=2e-27, every denominator separates, and all fixed input/domain/shape gates pass. Otherwise report the exact deficient component per pole, retaining all processed node and pole records. Completion of the ledger is not a B/Bprime certificate: it bounds errors for a future explicitly prescribed center calculation, but does not calculate that center or new integral values.

Fixed counts:114972 coefficient-width node checks,2640 high amplification terms and67 panels per pole. No local moments or integrand sums are needed for this diagnostic. The old B66 contraction's32.92-second external time is a reference for a different algorithm, not a measured cost for this Fraction width ledger. A proposed once-only120-second/384MiB budget is a conservative design ceiling requiring actual runtime closure and independent review; no <=120 performance assertion is made. Root may reject or revise the prospective contract before any run. No binder, runtime, authorization or native entry point is supplied now.

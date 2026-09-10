# One fixed A-node catalogue for uniformly bounded B/B' quadrature

This is a prospective uniform analytic/error result, not a batch evaluation. Native h1, every real s>0. Use the reviewed A0<=17/60, the direct infrared derivative bound -A'(s)<=3 for0<s<=1, and the trivial -A'(s)<=2/s³ for s>=1. The infrared bound is an explicit additional mathematical dependency of this improvement; it is not inferred from numerical oracle output.

Define C0(s)=E[X/(X+s²)]=1-s²A(s) and E0(s)=2s E[X/(X+s²)²]=2sA(s)+s²A'(s). Both are nonnegative. C0<=1. For s<=1, E0<=2sA0<=17/30; for s>=1, maximizing X/(X+s²)² gives E0<=1/(2s)<=1/2. Consequently E0<=17/30 uniformly.

On |z-c|<=c/2, |X+z²|>=X and >=c²/4. The transform integrands therefore satisfy

 |G_s(z)|<=min(A(s),4C0(s)/c²)<=min(17/60,4/c²),
 |H_s(z)|<=min(-A'(s),4E0(s)/c²)<=min(3,(34/15)/c²).

The common bound min(3,4/c²) holds for ALL s>0. This avoids the earlier small-s divergence of2/s³ and1/(2s) estimates.

## Reuse of the existing fixed schedule

Keep epsilon2^-28,T8,31panels j=-28,...,2,12-node Gauss on each panel. The analytic continuation argument is uniform in s; apparent divided-difference poles cancel before any bound is taken. Summing a M(3a/2) over all dyadic panels is bounded by3+32/9=59/9. Thus the middle error after2/pi is at most

 (2360/81)(4/25)^12.

This is a radius and contributes twice to final width. The low tail of either integrand is at most3epsilon, so after2/pi its width is at most2epsilon. With16 high-tail terms, the G remainder is at most C0(s)12^16/[33*8^33], and the H remainder at most E0(s)12^16/[33*8^33]. Both are bounded by the same expression without a small-s singular factor. After2/pi multiply by2/3. Therefore the uniform analytic WIDTH budget is

 2*2^-28 +2*(2360/81)(4/25)^12 +(2/3)*12^16/(33*8^33),

strictly below1e-6. Numerical interval errors, moment recurrence and pi rounding still consume the remaining width. This schedule proves no relative-error guarantee for tiny B' or large-s B.

## Batch source plan and exact collision obligation

The744 A(t) endpoint calls for the fixed Gauss catalogue are independent of s and can be reused for any fixed finite pole family. Each additional pole requires its own A(s),A'(s) enclosure,16 moment recurrence terms and372 interval integrand evaluations. This reduces expensive special-function calls from roughly746 per pole pair to744 plus one per pole, assuming the existing catalogue precision proves adequate. The actual catalogue is not regenerated or silently tightened from observed outcomes.

For t²-s² separated from0, the saved divided-difference formulas apply with outward arithmetic. Validate the final width at every pole; no uniform separation follows from the analytic bound. For exact coincidence, G_s(s)=A(s)+(s/2)A'(s), but H_s(s)=-(3A'(s)+sA''(s))/4. Thus the existing first-dual oracle alone is insufficient for exact collisions. A second-dual or independently bounded A'' extension is required, or a prospectively chosen pole family with certified separation from catalogue nodes. Near collisions likewise need joint divided-difference/derivative enclosures or more precision. Reusing a pole's own A(s) interval in both numerator appearances reduces dependency loss but does not abolish it.

A stationary-pole family sharing the Gauss grid can contain exact collisions; it cannot be assumed safe merely because each grid has even-order nodes. That earlier avoidance only applied to the two dyadic poles1,2, which were panel endpoints. Complex stationary poles additionally require a genuine complex oracle and are outside this real-positive statement.

## Scaling and computational boundary

Restore B_h(s)=h^-1 B_1(s/h), B_h'(s)=h^-2 B_1'(s/h). The common dimensionless target thus yields absolute widths1e-6/h and1e-6/h² respectively. A proposed384-pole real batch would need744 catalogue calls plus384 pole calls, not384 fresh catalogues. It still needs a fixed source-bound pole list, separation/collision policy, actual input-width ledger, memory/cost forecast and independent review. No batch, oracle, Gram or physical integral has been run here.

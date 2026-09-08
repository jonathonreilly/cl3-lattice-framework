# Exact interval trigonometric inputs for the n32 grid

The intended product grid has k_j=2π(j+1/2)/32, so the Clifford parameters are q_j=2sin[π(2j+1)/64]. These inputs are geometry, not an eigenvalue calculation or physical density scan.

Machin's identity π=16atan(1/5)−4atan(1/239) follows from tangent addition and the branch0<4atan(1/5)−atan(1/239)<π/2; its tangent is1. Each arctangent is enclosed by its48-term alternating Taylor sum and the next term. Subtracting intervals gives exact rational bounds on π.

At the rational midpoint x of each argument interval, sine's polynomial through degree79 is evaluated using exact Fractions. Taylor's degree80 remainder is at most |x|^81/81!, since every derivative of sine is bounded by1. The unknown argument adds at most its interval radius because sine is1-Lipschitz. Multiplying by2 gives rational q bounds, then100-bit dyadic floor/ceiling expands them outward. No accuracy premise for libm, Decimal, or a numerical eigensolver is used.

The chosen binary64 center is merely a candidate. Exact Fraction.from_float comparison verifies that its symmetric radius2^-48 contains the entire rational interval; no correctly-rounded float-conversion assumption is necessary. The consumer must retain this input error in its matrix certificate. Since each q coefficient is a unit-norm signed Pauli matrix, three such errors contribute at most3*2^-48 in operator norm before matrix-assembly roundoff.

All32 entries are strictly between0 and2; interval intersections check the exact reflection identity q_j=q_(31-j). The source performs exact construction and simple integrity controls. Independent source/input review remains required before a physical grid launch. This packet supplies no energy-density sign or spectral integral.

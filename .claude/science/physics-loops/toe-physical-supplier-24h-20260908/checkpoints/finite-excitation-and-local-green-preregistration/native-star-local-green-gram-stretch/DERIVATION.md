# Local resolvent and negative-band Gram reduction for the actual star

Prospective analytic and certification design. No physical integral or Gram matrix has been evaluated. Use the infinite canonical staggered cubic gauge, h=2|t_hop|>0, center0 and neighbors(+x,-x,+y,-y,+z,-z). A hopping-sign gauge fixes t_hop>0 for the displayed oriented entries.

## 1. Two scalar functions suffice for all Gram entries

Put X(k)=4h² sum_a sin²(k_a), and define
A(s)=E[(X+s²)^-1], B(s)=E[sqrt(X)/(X+s²)], Re(s)>0.
These are analytic on the open right half-plane. Let O be the 7x7 matrix with ones only between opposite neighbors. Let T be real skew with T_(0,+a)=-1, T_(0,-a)=+1, and all other independent entries zero. Set N=I+O and
D(s)=(1-s² A(s))/(6h²).

The local resolvent R_sigma(s)=U^dagger(h0-i sigma s)^-1 U, for real s>0 and sigma=+/-1, is exactly

 R_sigma(s)=i sigma s[A(s)N-D(s)O]+i h D(s)T.           (1)

The even Green function connects the center only to itself and a neighbor only to itself or its opposite. Different axis cell parities have zero cross entries. The same-axis opposite entry is A-D. Applying h0 to this even Green function produces the oriented center-neighbor entries in (1).

For the negative-band projected resolvent F_sigma(s)=U^dagger P0(h0-i sigma s)^-1 U, write mu=E sqrt(X). The sign(h0) factor gives a weighted even Green function with diagonal B and opposite entry B-(mu-s²B)/(6h²). Its odd center-neighbor entry is controlled by B/(6h²). Consequently

 F_sigma(s)=Ftilde_sigma(s)+mu O/(12h²),
 Ftilde_sigma(s)=(1/2){R_sigma(s)-B(s)[N+s²O/(6h²)]+sigma s B(s)T/(6h)}.  (2)

All signs follow from h0=iK and <0|h0|+a>=-ih. In particular the reference-energy moment mu is a constant term and CANCELS from every Gram divided difference.

Let v_(sigma,s,a)=(h0-i sigma s)^-1 e_a. Then

 <v_(sigma,s,a),v_(tau,t,b)>
 =[(R_tau(t)-R_(-sigma)(s))/(i(sigma s+tau t))]_(a,b),
 <v_(sigma,s,a),P0 v_(tau,t,b)>
 =[(Ftilde_tau(t)-Ftilde_(-sigma)(s))/(i(sigma s+tau t))]_(a,b).          (3)

When the denominator vanishes, use the analytic resolvent derivative, not subtraction or division by zero. This requires A'(s),B'(s), but no new scalar moment. For genuinely complex nodes replace the first pole by its conjugate before taking the divided difference. The proposed pilot below handles real positive s only; it does not claim a complex interval engine.

The perturbed resolvent columns in the rank-two Woodbury formula are linear combinations of these bare local columns, so their Grams add only small coefficient matrices. The enlarged subspace span(range Q,P0 range Q) is P0-invariant; its reference state is pure once represented exactly. This does not make that subspace invariant under the perturbed dynamics, and does not by itself solve finite-time transport.

## 2. One coordinate is integrated exactly for A

In units h=1, fold each momentum to [0,pi/2] and rescale to u in[0,1]. Write b=4[sin²(pi u/2)+sin²(pi v/2)] and a=s²+b. The elementary integral over the third coordinate yields

 A(s)=integral_[0,1]^2 [a(a+4)]^-1/2 du dv,
 A'(s)=-2s integral_[0,1]^2 (a+2)[a(a+4)]^-3/2 du dv.                 (4)

Both positive magnitudes decrease with a. On a dyadic square, certified endpoint sine bounds therefore give rigorous lower/upper integral bounds by multiplying corner function bounds by the exact square area. Adaptive subdivision refines a guaranteed enclosure; it is not a heuristic quadrature error estimate.

B has the direct positive three-dimensional representation

 B(s)=integral_[0,1]^3 w/(w²+s²) du,
 B'(s)=-2s integral_[0,1]^3 w/(w²+s²)² du,
 w=2 sqrt(sum sin²(pi u_a/2)).                         (5)

The corresponding one-coordinate analytic reduction involves complete elliptic integrals and can suffer cancellation at the conical corner. The first pilot instead retains (5), with exact range bounds on each dyadic cube. The first scalar integrand has its only maximum at w=s, and the derivative magnitude has its only maximum at w=s/sqrt(3). Endpoint and critical-point bounds suffice. No derivative regularity at the conical corner is assumed.

Restore dimensions by A_h(s)=h^-2 A_1(s/h), B_h(s)=h^-1 B_1(s/h); their derivatives have one additional h^-1.

## 3. Concrete certification arithmetic

Pi is enclosed by the alternating Machin arctangent series, not a floating library constant. Sines use a rational Taylor polynomial plus an explicit remainder and argument-interval Lipschitz error, then outward dyadic rounding. Square roots use integer isqrt on scaled fractions, with outward endpoints. Every cell value is rounded outward to 40 fractional bits before accumulation; cell volumes are exact dyadics. Thus denominator growth does not explode across adaptive leaves. The total enclosure is the exact sum of cell enclosures, including all rounding.

The fixed first pilot proposes s=1 and s=2, with both functions and their derivatives. A/A' use at most1024 leaves; B/B' use at most4096 leaves. The largest normalized enclosure width selects the next cell deterministically, with lexicographic ties. A width target1/32 is a declared useful-cost gate; reaching the leaf cap instead is INDETERMINATE and is preserved. It is not a license to relax the target, change s, or treat an interval midpoint as certified.

These enclosures may be much too wide for a final thousands-column Gram matrix. The purpose is to measure exact arithmetic cost and the achieved widths of the actual local bath scalars, before choosing a full precision contract. No physical integral is authorized by this design document.

# New omega5 positive-integral certificate from the existing A catalog

SOURCE ONLY / NOT EXECUTED. Dimensionless h=1, X=6-2 sum cos(theta),0<=X<=12, M1=6,M2=42. This is a NEW quantity omega5=E X^(5/2), not a rerun of nu. Target full width1e-24. The existing catalog contains1742 Gauss26 nodes and3484 separately computed endpoint A/Aprime oracle calls; no new oracle is proposed.

## Identity and quadrature

Tonelli gives omega5=(2/pi) integral_0^infinity Q5(t)dt, with

 Q5(t)=E[X³/(X+t²)]=42-6t²+t⁴-t⁶A(t).

On every dyadic panel[a,2a], a=2^j,j=-64..2, the rho4 ellipse has z/a=3/2+(17/16)cos(theta)+i(15/16)sin(theta). Its real part exceeds the absolute imaginary part because9/4-((17/16)²+(15/16)²)=31/128>0. Thus Re z²>0 and |X/(X+z²)|<=1. In particular |Q5(z)|<=EX²=42 (and the looser42*17/16 also holds). Holomorphy follows by dominated integration locally inside the ellipse. Positive Gauss26 and integration agree through degree51; the Chebyshev tail argument gives radius(16/3)aM4^-52. Summing a<8 gives1792*4^-52; this protocol deliberately uses the looser R=1904*4^-52, consistent with M=42*17/16. The factor17/16 is unnecessary slack, not a claim that Re z² fails.

## Low/high pieces

For epsilon=2^-64, integrate the polynomial exactly:

 L=42epsilon-2epsilon³+epsilon^5/5,
 integral_0^epsilon Q5 in[L-(17/60)epsilon^7/7,L].

The correction is NEGATIVE, unlike the positive nu low correction. This sign is essential. For t>=8, even truncation40 gives

 high partial=sum_(n=0)^39 (-1)^n M_(n+3)/[(2n+1)8^(2n+1)],
 0<=high remainder<=M43/(81*8^81)<=12^43/(81*8^81).

The runtime computes exact M3..M43 via the finite multinomial formula from independent torus phases, and saves all41 values and40 coefficient contributions before the target gate. No such moments were evaluated during preparation, except tiny synthetic M0..M3. The unknown scalar omega5 is not imported via this combinatorics.

## Input width sufficiency, not an assumed new precision

Use authenticated endpoint A widths1e-30, node widths2^-140, mapped weight widths1e-38 (plus outward192 rounding), positive weights with sum upper<=9. As in the reviewed nu source, the combined monotonic A-at-node width is<3e-30; the new runtime checks it. It also checks A upper<1/3 and the weighted sixth-power sum<=300000. This sharper sum matters: the coarse9*8^6 factor would waste the available input precision.

Indeed the exact Gauss rule integrates t^6 exactly, so its ideal sum is(8^7-epsilon^7)/7<299594. Moving roots by2^-140 and weights by1e-38+2*2^-192 changes the upper sum by at most9*6*8^5*2^-140+1742*8^6*(1e-38+2*2^-192), which is<1. Hence300000 is a safe predata gate. The source oracle uncertainty contributes at most300000*3e-30=9e-25 to the unscaled integral width.

At fixed A in[0,1/3], the sum of absolute derivatives of the separated polynomial terms is<=12*8+4*8³+6*8^5/3<2^17. Its node-box contribution is<=9*2^17*2^-140. True Q5 lies[0,42]; its computed interval magnitude is<43 once the displayed width bounds hold. The weight-box contribution is<=1742*43*(1e-38+2*2^-192). All fixed192 rounded primitives have a conservative aggregate width allowance1e-43. Thus the middle width is<1e-24; actual middle width<=1e-24 remains a mandatory runtime gate, not a conclusion from bit settings alone.

Using exact Machin32/10 bounds, pi>3, the final full width is bounded by

 (2/3)*(1e-24+2R+(17/60)epsilon^7/7+12^43/(81*8^81))+1e-35 <1e-24.

The reciprocal-pi term1e-35 is conservative: Q5 integral<42*8+M3/8<400 and the exact alternating Machin remainder is much smaller. The tiny predata control checks this rational budget without evaluating catalog values or M43. It does not claim the actual interval attains a particular width.

## Rounding and remaining boundary

Each of1742 nodes uses at most12 rounded primitives (t²,t⁴,t⁶,t⁶A, two scaled polynomial terms, additions, weight product, panel sum), plus67 cumulative sums and a bounded final combination. A conservative25000 operations, amplification2^24 and two endpoint ulps2^-192 give total width<1e-43. Mapped weights are rounded once by the inherited loader; node/A boxes retain their authenticated exact endpoints. Exact moment and high-tail rational sums are not rounded. Node/weight/A interval errors are charged separately above. Intermediate physical intervals are bounded by polynomial magnitudes<2^20; source operand guards constrain arbitrary malformed inputs.

This supplies only omega5 for a prospective low-degree moment Ward certificate. The degree11 derivation, the actual gate outcome and full alpha remain separate obligations. Execution requires source/runtime review and new preregistration. No accepted numerical input was parsed in preparation.

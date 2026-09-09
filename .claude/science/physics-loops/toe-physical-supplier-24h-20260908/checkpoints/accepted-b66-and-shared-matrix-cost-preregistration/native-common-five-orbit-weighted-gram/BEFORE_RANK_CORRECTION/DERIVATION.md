# A legitimate common stationary frame for all five pair orbits

Source-only extension of the reviewed individual P/O weighted-Gram construction. Units h=1 and the same real staggered reference frame are used throughout. No native matrix, propagator or scalar oracle is evaluated. This derivation imports the full7-source resolvent/projected-resolvent formulas, the corrected five-orbit gauge classification, and the scalar-balanced complete error ledger.

## Signed star projections and exact cross coefficients

Order the star sources (0,+x,-x,+y,-y,+z,-z), with epsilon_(+a)=+1 and epsilon_(-a)=-1. For a support pair A define d_A=sum_(v in A)epsilon_v e_v. This sign is required by the native oriented hopping; d_A is not an unsigned sum when a negative neighbor occurs. For disjoint A,C form the7x3 real projection W=[e0,d_A,d_C]. The two neighbor columns are orthogonal, each of norm sqrt2. They are source columns, not already normalized CAR modes.

Let o_A,o_C indicate an opposite pair and k count opposite-neighbor links crossing from A to C. Direct contraction of the literal7x7 matrices gives

    W^T I W=diag(1,2,2),
    W^T O W=[[0,0,0],[0,-2o_A,-k],[0,-k,-2o_C]],
    W^T T W=[[0,-2,-2],[2,0,0],[2,0,0]], N=I+O.

Thus the only orbit-dependent parameters are

    (o_A,o_C,k): (1,1,0), (1,0,0), (0,1,0), (0,0,2), (0,0,1),
    multiplicities: 6,12,12,12,48.

Representatives are respectively (+x,-x ; +y,-y), (+x,-x ; +y,+z), (+x,+y ; +z,-z), (+x,+y ; -x,-y), (+x,+y ; -x,+z). These are ordered A,C pairs. No exchange equality is assumed. The corrected signed coordinate-permutation gauge has center sign+1 and on-star sign epsilon_f(v)/epsilon_v; it intertwines these signed source projections. The full spatial gauge theorem is imported, not inferred from these seven sites alone.

## Same scalar catalog supplies every cross Gram

Write D=(1-s²A)/6, geo_A=A for P and D for O. The real rephased full resolvent C_sigma=R_sigma/i restricted to W is

    [[sigma*s*A, -2D, -2D],
     [2D, 2sigma*s*geo_A, k*sigma*s*(D-A)],
     [2D, k*sigma*s*(D-A), 2sigma*s*geo_C]].

For L_sigma=2Ftilde_sigma-i C_sigma the corresponding matrix is

    [[-B, -sigma*s*B/3, -sigma*s*B/3],
     [sigma*s*B/3, ell_A, k*B*(1+s²/6)],
     [sigma*s*B/3, k*B*(1+s²/6), ell_C]],

where ell_P=-2B and ell_O=s²B/3. B here is the scalar E sqrt(X)/(X+s²), not geo_A. Derivatives are obtained directly using A',B'.

For labels (s,sigma,a),(t,tau,b), the raw real Gram and covariance Gram are

    G=[C_tau(t)-C_-sigma(s)]_ab/(sigma*s+tau*t),
    J=-[L_tau(t)-L_-sigma(s)]_ab/(sigma*s+tau*t).

At the only zero denominator (same positive pole, tau=-sigma), use G=C'_tau/tau and J=-L'_tau/tau. G is symmetric and J skew; its diagonal vanishes exactly. The omitted constant mu O/(12) in F cancels also in CROSS divided differences because the same fixed W is used at both poles. Consequently the same accepted A,A',B,B' values at66 midpoints suffice for every stationary common cross Gram. There is no new bath scalar for this construction. This claim does not extend automatically to time propagation or arbitrary appended bare-source observables, which have their own data requirements.

## Pair-specific operators in one actual common space

Let U_A=[e0,d_A], U_C=[e0,d_C]. Define the3x2 coefficient selectors E_A=[e_0,e_1], E_C=[e_0,e_2], so U_A=W E_A and U_C=W E_C. The already reviewed2x2 Woodbury matrix T_A depends only on whether A is P or O, and similarly for C. At each pole the common six columns [R(is)W,R(-is)W] carry scalar balance sqrt(alpha), alpha=35w/(2pi). Embed each native signed coefficient using E_A T_A E_A^T or E_C T_C E_C^T in its plus/minus off-diagonal block, divided by35. Both embedded coefficients have norm<=1; their relative phases are fixed by these same real signed source maps.

There are6*66=396 raw columns Y and at most792 columns F=[Y,Gamma0Y]. Their Gram is [[G,J],[-J,G]], with Gamma0 F=F Jcol. The exact range of F is a real Gamma0-invariant physical subspace. After quotienting exact null vectors, one common orthonormal CAR frame exists, and the reference restriction is pure. Both finite-rank operators Q_A,Q_C are represented there with the same reference covariance and the displayed coefficients. Separate arbitrary frames or separate square-root signs are unnecessary.

This does not identify a PSD-shifted numerical Gram with that physical subspace. Numerical ghost modes and any unknown nullspace remain subject to the conditioning-free coefficient/contour/polynomial enclosures. Exact spectral rounding of P0+Q_A and P0+Q_C, when its gap criterion holds, yields two finite-rank modifications supported in this SAME physical subspace. Finite purification iterates are not themselves pure projectors. A common frame does not by itself certify a chart radius, evolution approximation or inserted kernel sign.

## Existing scalar width target remains sufficient conservatively

The common pole trace is2(A+2geo_A+2geo_C)<=10A<=17/6. Hence the covariance-closed scalar-balanced Gram obeys

    Tr M <=(35/pi)*(17/6)*sum w <529.

This derives the factor trace from native columns and positive quadrature weights. It is not inferred from a trace-norm bound on Q.

The previous per-entry B/B' error multiplier<10136 still holds, since every signed source column has l1 norm<=2. With396 raw rows and max alpha<12,

    epsilon_B <=12*396*10136*eta =48166272 eta.

The conditioning-free factor comparison in dimension792 gives a trace operator error <=2sqrt(529*1584*epsilon_B)+1584epsilon_B. At eta=1e-19 this is below.0041. Thus the existing B/B' full-width target2e-19 remains sufficient for this conservative common-frame B allocation. It is not necessary to launch a tighter scalar catalog merely because the frame has grown.

The analogous A Gram error may be bounded by2^38 eta_A, giving factor discrepancy<1e-6 at eta_A=1e-30. Additional matrix arithmetic epsilon_num<=2^-60 gives discrepancy<2e-6. The common trace529 times the signed coefficient error2^-40 is<1e-9. The parent physical geometry displacements and coefficient input bounds remain separately charged per impurity; their previously tiny allocations have ample slack. These sufficient targets fit1/200, but actual midpoint arithmetic and input acceptance must still pass. No matrix error has been measured here.

## Size/cost design, not a measured forecast

Each orbit's raw upper triangle has396*397/2=78606 entries, represented as streamed G/J pairs; five such tables contain393030 entries. The existing individual P/O tables supply reusable diagonal kernels. Only k times one extra d_A/d_C kernel is new, and k=0 cross blocks vanish. A full universal7-source table would have924 raw/1848 closed dimensions and427350 upper-triangle entries. It provides one shared source representation for all five orbits but is not automatically cheaper than five streamed3-source tables.

Across all five representatives the neighbor source columns span all six neighbor directions, so the universal seven-source rank cannot be reduced merely by dropping an unused axis. Structured blocks, exact source selectors and streamed integer intervals can avoid materializing all dense matrices. There is no native runtime/memory claim. The next implementation should retain the current disabled individual source unchanged, add source-only3x3 cross formulas and actual symbolic selector tests, then obtain a separately frozen cost/acceptance contract before any physical matrix assembly.

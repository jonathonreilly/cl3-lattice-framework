# Direct positive low-pole scalar supplier

Source-only proposal, no actual catalog, node, oracle or integral evaluation. Let expectation be the normalized supplied native measure of X=6-2 sum cos(theta), h=1. Define A(s)=E[(X+s²)^-1], B(s)=E[sqrt(X)/(X+s²)], cminus=E[X^-1/2]. For s>0,

 C(s)=(cminus-B(s))/s²=E[1/(sqrt(X)(X+s²))]>0.

All expectations are finite at fixed positive s. The pointwise identity is exact; the separate divergent limit C(0) is not used. The one-folded-torus normalization has no extra node multiplicity.

## Positive Stieltjes identity and confluence

Since X^-1/2=(2/pi) integral_0^infty (X+t²)^-1 dt, Tonelli gives

 C(s)=(2/pi) integral_0^infty K(s,t) dt,
 K(s,t)=E[1/((X+s²)(X+t²))]
       =(A(t)-A(s))/(s²-t²).

At t=s the exact continuation is K(s,s)=-A'(s)/(2s). The numerator and denominator have the same sign. Neither independent subtraction near t=s nor subtraction of independent cminus/B boxes is a stable certification method.

Put L(r)=-A'(r)>=0. The fundamental theorem gives the cancellation-free identity

 K(s,t)=1/(s+t) integral_0^1 L(t+u(s-t)) du.                 (1)

This includes t=s literally. An interval enclosing L on the segment between s and t gives an enclosure for K divided only by s+t. It does not require correlated samples of A. Conversely, a quadrature in u needs its own derivative/error certificate; simply replacing the average by L at a midpoint is invalid.

## Explicit low and high splits

Import the independently proved infrared estimate
 |L(r)-ell|<=k r, ell=1/(4pi), k=2+7/(6pi²), 0<r<=1.

If 0<s<=1 and 0<d<=1, equation (1) gives for every 0<=t<=d

 |K(s,t)-ell/(s+t)|<=k/2.

Consequently the complete low interval has the analytic certificate

 integral_0^d K(s,t)dt =ell log(1+d/s) + error,
 |error|<=k d/2.                                         (2)

The identity remains valid at t=0 as a limiting integral; A'(0+) exists. After the 2/pi prefactor the low error is <=k d/pi. Choosing d<=epsilon_low*pi/k suffices uniformly in the lowest pole s. This is a new endpoint subtraction, not use of an independently boxed cminus.

For T>s, a simple positive high bound is K(s,t)<=A(s)/t²<=A0/t², hence the omitted high error <=2A0/(pi T). A more useful finite expansion is

 K(s,t)=sum_(j=0)^(N-1) (-1)^j E[X^j/(X+s²)]/t^(2j+2) + remainder.

The integrated remainder has magnitude <= E[X^N/(X+s²)]/((2N+1)T^(2N+1)), with sign (-1)^N. This follows from finite geometric division, not an infinite series; multiply by 2/pi. Its coefficients are recursively Q0=A(s), Q_(j+1)=M_j-s²Q_j, M_j=E[X^j]. They must be enclosed jointly with outward rounding; positive defining expectations provide Qj>=0. The crude bound Q_N<=12^(N-1) for N>=1 supplies a data-free remainder. At T=16 a modest new N gives geometric decrease (12/256)^N; no coefficient or moment was computed here.

## Precision ledger for the middle integral

Suppose a future certified derivative representation has uniform absolute error delta_L for all arguments used between d and T and the fixed s. Formula (1) implies a middle input-error bound

 epsilon_input <=(2/pi) delta_L log((s+T)/(s+d)).          (3)

Thus dependence on the lowest s is logarithmic, not s^-2. For s>=2^-32 and T=16, log((s+T)/(s+d))<37 log2<26, so delta_L<=pi epsilon_input/52 suffices. This is an absolute precision requirement on L, not on A. No existing derivative catalog is asserted to meet it at the new nodes.

If using A endpoint intervals instead on a region separated by |t²-s²|>=g, their numerator radius is (eta_t+eta_s)/g. This branch must carry its actual separation and integrated weights. Near coincidence use (1) or direct confluent data; no fixed minimum separation may be assumed for a future Gauss bank. A widths of order1e-30 can still yield order1e-10 after division by s² around s~2^-32, before integration weights; neither that pointwise estimate nor its apparent failure alone establishes the final weighted operator error.

The elementary infrared bound alone does not close (3): near r~s it permits L error O(s), which can exceed a 1e-13 scalar allocation. A higher precision derivative oracle, directly certified positive average, or higher-order infrared subtraction is a genuine additional supplier. Small d makes (2) cheap but does not improve L accuracy on the segment from d to s.

## Prospective algorithm and cost boundary

A new algorithm can combine (2), positive panel integration of (1) on [d,T], and the finite high expansion. For d=2^-48,T=16 there are26 ratio-four panels. With p outer Gauss nodes and q certified inner nodes this costs26pq derivative samples per pole before sharing. For378 poles, the unshared census is9828pq. These are symbolic counts only; no claim p or q achieves a target is made without a Banach ellipse or derivative remainder bound for this new integrand. Interval range bounds for L give a simpler adaptive certificate but may require many subdivisions. This is not execution-ready and is not a proposal to rerun the old B integrals.

C(s) is the relevant cancellation-free scalar, but a projector Gram uses weighted combinations and perhaps divided differences of C. Equation (3) is only its scalar input budget. The operator nuclear error still requires coefficient norms, Gram stability, and correlated differences where requested. The new global378-node analytic bound leaves an explicit 8e-13 operator-input budget, not 8e-13 independently for every scalar.

Under X_h=h²X, C_h(s)=h^-3 C(s/h). All constants above apply after rescaling. No kernel/alpha value or successful compression follows from these source-only identities.

# Quartic inverse-square bound with unchanged quadratic trials

Source-only independent derivation of the proposed Hermite majorant. Dimensionless supplied D>=delta I, delta=1/4; no native moments, coefficients or outputs are evaluated. This changes a residual norm estimator, not the old degree2 p, constant q or nominal.

Let a,b>0 (coincident and equal-to-delta values allowed), and define
 P(x)=(x-delta)(x-a)^2(x-b)^2,
 B=1/(delta a² b²), A=B(1/delta+2/a+2/b).
Then A,B>0. At zero, P(0)=-1/B and P'(0)=(1/delta+2/a+2/b)/B. Thus the constant and linear coefficients of1+P(x)(Ax+B) vanish exactly. The quotient Q(x)=[1+P(x)(Ax+B)]/x² is a polynomial of degree4. For every real x>=delta,
 Q(x)-x^-2=(x-delta)(x-a)^2(x-b)^2(Ax+B)/x²>=0.
There is no requirement that a,b lie above delta, no singularity when they coincide, and no optimization premise. The touches at a,b are relevant only where those nodes lie in the spectral domain.

## Exact coefficients

Write the elementary symmetric functions of(delta,a,a,b,b) as e1..e5. Then
 e1=delta+2a+2b,
 e2=a²+b²+4ab+2delta(a+b),
 e3=2ab(a+b)+delta(a²+b²+4ab),
 e4=a²b²+2delta ab(a+b), e5=delta a²b².
In ascending order Q(x)=c0+c1x+c2x²+c3x³+c4x4,
 c0=Ae4-Be3,
 c1=Be2-Ae3,
 c2=Ae2-Be1,
 c3=B-Ae1,
 c4=A.
These coefficients can have either sign. Choosing interval endpoints solely by the degree or treating all moment coefficients as positive is incorrect.

For r=(I-Dp(D))Omega with p degree2, define rho_j=<r,D^j r>,j0..4. The spectral theorem yields
 ||D^-1 r||² <= sum_(j=0..4)c_j rho_j.
The required moments are only m0..10: write v=(1,-p0,-p1,-p2), then rho_j=sum_(i,k=0..3) v_i v_k m_(i+k+j). Convolve once to seven exact coefficients d_l=sum_(i+k=l)v_i v_k, then rho_j=sum_(l=0..6)d_l m_(l+j). This preserves shared trial coefficients; no new inverse, trial solve or mixed-source kernel is required.

Given rigorous boxes rho_j in[l_j,u_j] and exact rational c_j, the upper endpoint is sum c_j*(u_j if c_j>=0 else l_j), with outward arithmetic. The lower endpoint reverses the choice. Correlations may make this enclosure loose but cannot invalidate it. The same signed endpoint rule applies when constructing rho boxes from exact d_l and original m boxes. A negative certified upper endpoint contradicts the norm premise and must refuse, not be clipped into a successful zero. A lower endpoint may intersect zero using true norm nonnegativity. Use an outward square root of the nonnegative upper to certify E_A. Taking the minimum over any finite family of valid upper bounds is legitimate. Retain old gap/quadratic-majorant bounds as explicit alternatives; a new candidate need not improve them.

## Fixed cheap proposal family

A sufficient initial schedule is the15 unordered pairs, with repetition, from a,b in{1/2,1,2,4,8}, in lexicographic order. This includes coincident pairs and requires no moment-dependent optimization or numerical search. It is a prospective fixed family, not a continuous optimum. Both retained degree20 modes and both P/O classes give60 evaluations. Exact dyadic proposal nodes make coefficients rational. If a later source chooses moment-dependent nodes, it must fix a bounded positive proposal/fallback and reevaluate the FULL original moment intervals at those exact nodes; no optimizer-enclosure claim is necessary.

Per class/mode, one residual convolution has16 products, five rho sums have35 moment terms, and15 quartic candidates have75 signed moment terms. Across four class/modes:64 convolution products,140 rho terms and300 quartic terms, plus60 outward roots if all are retained. Coefficients of the15 Q polynomials are shared across every class/mode. These counts exclude rational bit growth, serialization and authenticated input loading; no runtime is inferred without the existing scalar-guard cost contract. They are much smaller than new mixed determinant jets.

## Full coupled F and posterior update

For unchanged b_A=J_A p_A(D_A)Omega, unchanged q_A, and accepted s0,s1,s2, define eta_A²=s0-2q_A s1+q_A²s2. This source residual is unchanged and should be reused from its accepted enclosure where available. The exact target v=D^-1 J D^-1 Omega and trial v0=qJp imply
 F <= (sqrt8/delta) E + delta^-1 sqrt(sum_A eta_A²),
 E²=sum_A E_A² (12 P,3 O channels).
At delta1/4 the propagated coefficient is4sqrt8. A sharper E from the quartic majorant therefore tightens the propagated part of F without acquiring new s3,s4 or changing q. The inner residual term may still dominate, so improvement of the final Ward sign is not promised.

Feed these smaller certified E,F into the already reviewed posterior norm estimator using its same p/q/norm inputs and same nominal. Its norm upper formulas are monotone in E,F when based on nonnegative errors, and the general error guarantee applies regardless of improvement. Recompute the new error interval as NEW certificate arithmetic and intersect with the accepted old interval; preserve the old result if a new arithmetic candidate refuses. This is outside an exclusion proved for the previous numerical error estimator, but not outside the underlying supplied Ward assumptions. No old physical trial or nominal is recomputed as a comparison value.

Required future inputs: accepted exact quadratic p and q, original class moments0..6, newly accepted class moments7..10, original s0..2 or their source-residual certificate, nominal and old interval, plus their full source/receipt identities. Required retained outputs: original coefficients, residual convolution, rho boxes, all15 Q coefficient vectors and ungated expectations, per-class chosen E, combined E/F and posterior bound, and old/new intersection. New moments being available does not itself certify their useful width or any alpha sign.

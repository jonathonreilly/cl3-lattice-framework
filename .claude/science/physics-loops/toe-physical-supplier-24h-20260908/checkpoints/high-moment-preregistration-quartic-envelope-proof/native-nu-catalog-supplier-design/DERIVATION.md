# Nu from the existing accepted A catalog, with a sharper ellipse

SOURCE-ONLY proposal. No catalog values are loaded or contracted, and no oracle/integral has run. In dimensionless native units X=6−2 sum cos(theta), 0<=X<=12, M1=6,M2=42. The target is a certified interval of full width<=2e-19, hence radius<=1e-19, for nu=E X^(3/2). This supplies only the new second-action covariance moment; no action accuracy follows automatically.

## Integral and same-node stronger quadrature bound

Tonelli yields nu=(2/pi) integral_0^infinity Q(t)dt, Q(t)=E[X²/(X+t²)]=6−t²+t⁴A(t). Use the already accepted26-point Gauss rule on each of67 panels [a,2a], a=2^j,j=-64..2. No new root or weight is required.

Unlike the older rho=5/2 proof, choose the Bernstein ellipse rho=4: z/a=3/2+(17/16)cos(theta)+i(15/16)sin(theta). The ellipse lies strictly in u>|v|: the minimum of u−|v| is at least3/2−sqrt((17/16)²+(15/16)²)>0, since9/4−514/256=31/128. Thus Re(z²)>0 throughout its interior. Consequently |X+z²|>=X for X>=0, so |Q(z)|<=E X=6. Holomorphy follows locally by dominated integration; there is no Dirac-node singularity inside this ellipse.

For completeness, an analytic function bounded by M on ellipse rho has Chebyshev coefficients |c_k|<=2M rho^-k for k>=1. Truncating at degree51 gives uniform error<=2M rho^-52/(1−rho^-1). Both integration over a panel and its positive Gauss rule have norm a and agree through degree51. Their difference is therefore bounded by4a M rho^-52/(1−rho^-1). At rho4 this is(16/3)aM4^-52. Summing all panels with sum a<8 and M6 gives total quadrature radius R<=256*4^-52. This proof uses exact Gauss nodes; accepted interval nodes/weights introduce a separate arithmetic enclosure below. The old nodes do not constrain the new analytic ellipse.

## Low and high tails

Let eps=2^-64. On[0,eps], integrate the exact polynomial6−t², retaining the positive residual:
 low ∈ [6eps−eps³/3,6eps−eps³/3+(17/60)eps^5/5].
A coarse[0,6eps] would be too wide; this polynomial subtraction is essential.

For t>=8 fix40 terms, not the predecessor26:
 Q(t)=sum_(n=0)^39 (-1)^n M_(n+2)t^(-2n-2) + E[X^42/(t^80(X+t²))].
Hence the integrated partial uses M2..M41 divided by(2n+1)8^(2n+1); its positive remainder is at most12^42/(81*8^81). This only changes exact local-moment arithmetic, not the catalog or oracle. Moments have the exact multinomial formula M_k=sum_(a+b+c=k) k!/(a!b!c!) C(2a,a)C(2b,b)C(2c,c), obtained by independent torus phases (X is the sum of three4sin² variables). No physical spectrum evaluation is required. The use of an even40-term truncation fixes the remainder sign.

## Accepted finite precision suffices

Import only the successful mu weight-repair premises:1742 mapped positive weight intervals of width<=1e-38, sum upper weights<=9; node widths<=2^-140; accepted endpoint A widths<=1e-30. The failed f9e4 weight-width2^-140 premise is excluded. Monotonicity and the reviewed derivative bound give combined A-at-node width<3e-30. Evaluate the full interval6−t²+t⁴A in outward192-bit arithmetic. Independent t/A correlation loss is safe.

For0<t<=8, sensitivity to A is<=4096; holding A fixed, |−2t+4t³A|<600 using A<=17/60 plus its tiny enclosure. Thus node full-width<=4096*3e-30+600*2^-140<2e-26. The interval contains the true Q∈[0,6], so its magnitude is<7. Weight uncertainty and outward operation errors give middle full-width<=9*node_width+1742*7e-38+1e-45<2e-25. The roundoff allowance is conservative for fewer than100000 elementary fixed192 operations with intermediate magnitudes bounded by2^20; a final implementation must count/guard these and enforce actual middle width<=2e-25 before success.

Use the same Machin32/10 pi enclosure. Its width is bounded by16/(65*5^65)+4/(21*239^21). The unscaled integral is<=48+42/8<64, so reciprocal multiplication uncertainty is far below1e-35 using pi>3. For pi>157/50 the final full width is bounded by
 (100/157)*(2R+(17/60)eps^5/5+12^42/(81*8^81)+2e-25)+1e-35 <2e-19.
The tighter predata expression in plan.py uses the derived middle uncertainty, not its rounded gate. Exact rational controls verify the inequality without reading any catalog. The existing accepted A/node/weight precision therefore suffices under these premises; no tighter oracle is needed.

## Fixed implementation plan and remaining gates

A new worker should port only the successful9d21 loader, with its1e-38 mapped-weight gate, pin its full accepted catalog/root/post closure, and preserve the existing source/failure histories. It must retain every node contribution or complete panel cumulative before any gate, use all1742 nodes once, compute the40 exact tail moments, and report separate low/high/quadrature/middle/pi widths. Check actual endpoint/root/weight premises and middle width, never infer them from nominal bit precision. Keep oracle_calls=0 but label the contraction a NEW physical integral. No runtime or cost contract is selected here; root review, complete source/runtime closure and remote preregistration are prerequisites. Nu remains unavailable until that separate once-only execution and independent saved certificate pass.

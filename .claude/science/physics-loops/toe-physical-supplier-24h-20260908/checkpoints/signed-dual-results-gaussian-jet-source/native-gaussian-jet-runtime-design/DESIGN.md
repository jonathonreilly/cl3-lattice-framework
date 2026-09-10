# Degree-filtered Gaussian moment-jet implementation proposal

NOT_READY. This source implements inert bounded arithmetic and synthetic tests only. No native loader, output directory, authorization, scalar supplier, execution contract or runtime forecast exists. The Gaussian bridge eea8f713 is a separate independently authored proof under bounded real lattice/no-zero-atom assumptions, still subject to parent review. This proposal imports that conditional scope; finite controls alone do not establish a native identity.

## Exact20-column representation

For N<=10 use physical F_j=h0^j(a,d),0<=j<N, at most2N columns, without independence assumptions. Write U_n=sum F_i A_n[i,j] F_j*. Coefficient indices in code are2i+source_index. Ordinary D_l=(a,d)*h0^l(a,d), projected B_l=(a,d)*P h0^l(a,d) implement products and traces. Neither ordinary nor projected Gram is inverted.

Separate A_n=L_n+Q_n, where L_n is exactly the one-V sector:

 L_n[i,j]=-(-1)^j binom(n-1,i) J/n!, i+j=n-1,
 J=2i[[0,1],[-1,0]].

Q1=0. The recurrence is

 (n+1)Q_(n+1)=shift_left Q_n-shift_right Q_n
              -(L_n+Q_n) D J into right power0.

Here the last summand is sum_l A_n[i,l] D_l J. Thus Q_n contains only at least two perturbations and has support i+j<=n-2. Every D query is <=N-2. L coefficients are converted independently to outward256-grid intervals; their analytic zero trace is never evaluated by summing those intervals.

Let C_(n,1)=A_n and C_(n,m)=sum_(k=1..n-m+1) A_k B C_(n-k,m-1). A product contracts intermediate indices through B_(j+l). For m>=2 both each B query and final trace query have power<=n-2; the surviving coefficient support has i+j<=n-m. Then

 ell1=Tr(L1 B)/2,
 ell_n=Tr(Q_n B)/2+sum_(m=2..n) (-1)^(m+1)Tr(C_(n,m) B)/(2m).

This explicitly enforces the reviewed single-V cancellation before interval trace evaluation. The code checks the source-degree and support bounds. It cannot silently ask for a B9,B10 or raw h^18 Gram. The nonlinear coefficients may contain lower ordinary scalar moments; those internal powers count toward the total degree proof and do not invalidate its bound.

## Lower moments are reused

The generic core can emit all log coefficients for synthetic comparison. The intended future native path MUST call first_order=7. That still builds prerequisite operator coefficients/powers, but performs no trace or emits no ell1..ell6. It imports accepted m0..m6, forms Z_n=(-1)^n m_n/n!, and derives their scalar lower log coefficients recursively. Combine those with new ell7..ell10 and the scalar exponential recurrence to produce only m7..m10. This is reuse of accepted native moments, not re-evaluation as comparison targets. Accepted lower moment source identity and class labels must be authenticated by the future binder. Optional inconsistent lower data cannot be treated as a new physical state.

## Scalar input boundary

Use the explicit D_j/B_j table in degree review9e8555db, j<=8, negative-band P convention. The required symbolic absolute moments are M1=3c,M3=nu,M5=omega5,M7=omega7,M9=omega9 plus exact even M0..M10. Native B0[a,d]=+ic/2 is not the ordered Majorana contraction-ic. No table, coefficient, local identity or scalar value was evaluated in this preparation. Omega7/omega9 and any new exact even-moment implementation remain prospective and separately reviewed; their widths must propagate all the way through the eventual cumulants and reconstructed moments.

## Directed arithmetic and bit bounds

Each real interval is integer endpoints divided by2^256; complex intervals have two real intervals. Addition is exact at this grid; every product and division by a known positive integer rounds endpoints outward. No division by a matrix pivot or approximate moment occurs. Coefficient rational conversion also rounds outward. Stored integer endpoints are limited to4096bits; input rational numerator/denominator limits reserve256bits before shifting. A multiplication uses at most8192bits and signed ceiling adds at most one bit; real sums of already rounded endpoints need at most4097 transient bits. Refusal prevents silently exceeding the stored cap. Grid rounding creates no asserted numerical precision target by itself.

Every finite step encloses the corresponding exact expression. The dynamic interval radius, including repeated scalar dependencies and cancellation, is the actual error certificate. It is invalid to claim total error equals operation_count*2^-256 without multiplicative amplification. This proposal makes no width-success claim. A future worker needs input containment/type guards, periodic liveness, durable order/trace/high-moment outputs before gates, failure cleanup, complete source pins and a once-only contract; none is supplied here.

## Source operation and storage bound

A_n has at most2n² complex entries (4 nonlinear blocks plus2n linear entries). C_(n,m) for m>=2 has at most2(n-m+1)(n-m+2) entries. The explicit sparse product loop therefore admits a conservative141240 complex multiplication count across all log products through10,2642 trace multiplications, and2280 operator-recursion multiplications, total146162. Each complex multiplication has at most16 integer endpoint products, giving at most2338592 such products before scalar reconstruction. These are combinatorial upper bounds, not measurements of native input arithmetic. Scalar reconstruction contributes only bounded O(N²) work.

A_n are retained; the one-V/nonlinear split is discarded after initial traces, and only adjacent m layers are retained. Peak persistent coefficient dictionaries have at most1910 complex entries, with a bounded additional product/result dictionary and eighteen2x2 input blocks. Packed maximum-size endpoint payload is several MiB, not a dense infinite operator. Python object, transient multiplication, interpreter, logging and input closure memory are extra and must be measured/capped by a future runtime. No source count is asserted to prove a30s or384MiB successful native run.

## Independent synthetic controls

The test uses abstract2x2 h=diag(-1,2), a fixed imaginary offdiagonal V and P=diag(1,0). It constructs exact rational U coefficients independently and uses det(I-P+PU)=U00, then solves Z²=U00 directly. This bypasses log powers and the sparse factor-bank recurrence. All coefficients through10 lie in directed core output intervals; the accepted-lower/high-only path agrees too. Degree queries are limited to8, with countercontrols for order, stored-bit and first-output bounds. This is an abstract finite determinant test, not a physical native covariance, Fock bridge or actual high moment. The first test script had a syntax-only whitespace error, retained separately. No native or saved scientific inputs were read.

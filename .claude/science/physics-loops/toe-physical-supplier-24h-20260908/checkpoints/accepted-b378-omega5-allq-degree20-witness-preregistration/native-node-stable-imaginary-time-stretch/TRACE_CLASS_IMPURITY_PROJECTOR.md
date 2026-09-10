# Infinite pair impurities change the Fermi projector by a trace-class operator

A first-principles structural lemma for independent review. It uses the already reviewed infinite two-link determinant and Green bounds, not a finite-volume gap or an assumed active gap. It concerns the stationary one-particle spectral projector; a uniform low-rank description of the finite-time normalized quench is a separate obligation.

Let h0=iK and h_lambda=h0+lambda Delta h, 0<=lambda<=1, for either actual pair geometry. Let U have columns the center and the normalized signed neighbor sum. In hopping units h=2|t_hop|, ||Delta h||=beta=2sqrt(2)h and rank Delta h=2. The reviewed scalar Green bound is A(0)<=a/h², a=17/60. The opposite-pair entry B=D<=1/(6h²), and the perpendicular entry B=A. The center and neighbor sum have opposite bipartite parity, so their off-diagonal entry in U^dagger(h0²+s²)^-1 U vanishes. Hence

 ||(h0-is)^-1 U||_HS²=A(s)+B(s)<=2a/h²,
 ||U^dagger(h0-is)^-1 U||<=sqrt(a)/h.

The rank-two Birman-Schwinger determinant at coupling lambda is

 d_lambda(s)=(1-4lambda h²D(s))²+8lambda²h²s²A(s)B(s).

Since 0<=D(s)<=1/(6h²), d_lambda(s)>=(1-2lambda/3)²>=1/9. This is uniform in s>0 and along the entire coupling interpolation. For a two-by-two matrix M, ||M^-1||=||M||/|det M|. Thus the exact Woodbury matrix has norm at most

 9(1+beta sqrt(a)/h).

The resolvent difference is a product of two bare local resolvent columns, this bounded two-by-two matrix, and the rank-two coupling. Its trace norm is consequently bounded near s=0 by

 C0=2a beta*9(1+beta sqrt(a)/h)/h².

At s>=2beta, a Neumann estimate instead gives

 ||(h_lambda-is)^-1-(h0-is)^-1||_1<=4beta/s².

Both bounds are integrable in s. The sign-function resolvent integral therefore converges in trace norm for the difference, proving

 P_-(h_lambda)-P_-(h0) is trace class,
 ||P_-(h_lambda)-P_-(h0)||_1
 <=(1/pi) integral_0^infinity ||Delta R(is)||_1 ds.

There are no zero eigenvectors: at lambda=0 the Fourier symbol has no square-integrable zero mode; a zero eigenvector at nonzero lambda would satisfy the finite-rank zero-energy equation, whose limiting two-by-two matrix remains invertible by d_lambda(0)>=1/9. The local inverse columns exist in l² because A(0)<infinity. This also rules out that particular finite-rank zero-energy solution, without postulating a spectral gap.

For a completely explicit conservative bound use sqrt(a)<3/5, beta<3h, and split at s=6h. Then C0<1071/(25h), the high integral is <2, and pi>3 gives

 ||P_-(h_lambda)-P_-(h0)||_1<87.

This bound is intentionally coarse. It proves a finite excitation-sector change in a Schatten sense and makes the rank-tail inequality

 ||D-D_rank-r||_HS <= ||D||_1/sqrt(r+1)

available. At a small requested error that particular bound is not computationally useful. It does not prove a rapidly decaying numerical singular spectrum, a uniform rank for every finite-time quench, a nonzero reference overlap, or an affordable 384-MiB evaluation. Those must not be inferred merely from trace-class implementability folklore.

The argument also gives trace-norm continuity in lambda by dominated convergence. Any further use of a Fock implementability theorem or parity/index conclusion needs its assumptions stated separately; it is not an imported conclusion here. The result is a concrete reason to investigate excitation compression rather than retain the entire bath, while preserving the remaining quantitative rank bottleneck.

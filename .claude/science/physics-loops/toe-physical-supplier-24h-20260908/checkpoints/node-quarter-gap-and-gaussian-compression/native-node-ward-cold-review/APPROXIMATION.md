# Two-filter approximation of the complete bounded Ward target

New analytic extension; no physical action. Let w=max_A||W_A||<=sqrt(102/5)<5 and choose q=13>=3+2w. All fields are real CAR vectors, with possible common scalar phases carried explicitly. For each ordered word, the sum of the coefficients times inserted-operator norms is at most q:

 3+(||W_A-W_C||+||W_C||+||W_A||)/2 <=3+||W_A||+||W_C||.

Each term contains exactly two inverses. Replacing them by F_T=(1-exp(-T D²))/D gives the complete error

 Einverse <=(90/4) q delta^-2 exp(-T delta²).       (1)

No soft commutator or internal J-time integration is needed. Likewise the two-dimensional positive Laplace representation has absolute integrand <=q exp[-delta(s+t)], so its union time tail beyond[0,R]^2 is <=(90/4)q delta^-2 exp(-delta R). This bounds a signed target without assuming the integrand is positive.

For the Gaussian real-time representation, M0=2sqrt(T)/sqrt(pi), M1=T. Symmetric truncation to|t|<=R has omitted zeroth moment r0<=2sqrt(T)/sqrt(pi)exp[-R²/(4T)]. The full Ward functional time error is <=(90/4)q M0 r0. Again only two filter variables occur.

## Cyclic space with the Ward tails included exactly

For each of six individual bonds let z_j=(B^T)^-1 b_{j}, so w_A=sum_(j in A)z_j. Add these at most six l2 vectors to V_m. Since K z_j is an original neighbor vector up to sign, all further powers K^n z_j reduce to powers of the original seven seeds. Thus the enlarged cyclic dimension is at most7m+6, not13m. Polynomial agreement up to degree<m still holds on every field needed, including W_A, and the Chebyshev seed-error E_m applies relative to its norm. There is no spatial truncation of W_A.

As before, evaluate compressed interaction-picture operators in the restricted mixed Gaussian state; do not substitute sign(K_m), assume stationarity of that state, or invent a compressed generalized zero mode. The added covariance moments now include the l2 inverse seeds and need their own certified evaluation.

A contour of total length L=|s|+|t| gives unitary error <=beta L E_m. A two-Majorana insertion gives an additional2E_m times its field-norm product. Summing the overlap and three Ward corrections yields at most

 [q beta L+2(q-3)]E_m.

Hence, using E_m uniformly for L<=2R,

 Ecompression <=(90/8)E_m[2q beta M0M1+2(q-3)M0²].         (2)

The reviewed covariance response for an overlap and two real Majorana insertions gives, for restricted covariance operator error epsilon,

 Ecovariance <=(90/8)epsilon[3(q-3)M0²+3q beta M0M1].     (3)

External left/right Ward fields can be collected with the central gamma into two real Majorana insertions by orthogonal transport; their norms are unchanged. Equation(3) includes all three corrections. Finite-rank displacement of the covariance still has rank<=14, since the extra z_j map back into the existing seed span under K.

## Concrete conservative parameters

In units h=1 use delta=1/4, beta<3, q=13, T=384, R=224, m=2048. Equation(1) is4680 exp(-24)<1.8e-7. The real-time tail is at most449280 exp(-98/3)<3e-9. With W<4, tau<=1792 and rho=3/2, the Chebyshev bound is12exp(2240/3)(2/3)^2048. Using log(3/2)>=152/375 makes this negligible after multiplication by(2). Use M0<=40,M1=384 for conservative rational coefficients in(2)-(3). An epsilon covariance error of10^-6/(4Ccovariance) budgets2.5e-7 to covariance. These are error budgets, not achieved arithmetic or conditioning certificates.

Dimension<=14342 real modes still makes a dense covariance larger than384MiB. The improvement is the simpler two-variable kernel, elimination of internal insertion time, and a significantly smaller covariance error coefficient. Structured representation and certified inverse-seed moments are still necessary for practical evaluation. No alpha sign or value follows.

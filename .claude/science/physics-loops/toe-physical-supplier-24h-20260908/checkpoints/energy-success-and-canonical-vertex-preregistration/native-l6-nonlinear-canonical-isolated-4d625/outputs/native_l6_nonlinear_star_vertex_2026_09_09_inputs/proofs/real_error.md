# Real star residual certificate with two vector-norm scans

Conditional arithmetic design only; no native action, solve, scan or transport has been executed. Reuse the exact21-mode adapted frame, real-star sign proof2260e100 and9e489 arithmetic assumptions. Let d=2^20, s=sqrt(d)=1024, u=2^-53, zeta=2^-1075 and gamma_k=ku/(1-ku), all treated as exact rationals. Every bound below can be evaluated with outward rational arithmetic. This is not a certificate for the existing candidate code until its operation ordering and floating environment satisfy the stated assumptions.

Assume binary64 round-to-nearest/ties-even, gradual underflow, no flush-to-zero or fast-math reassociation, and elementary real multiplication/addition/subtraction obeying |fl(op)-op|<=u|op|+zeta with every intermediate finite. Exact indexing, copies and sign changes introduce no error. Intermediate finiteness must be guarded or proved from these magnitude bounds; final finiteness alone is insufficient. Coefficient conversion is enclosed from the exact frame by rational radical intervals and actual dyadic stored values. No correctly-rounded math.sqrt assumption is needed.

## One real Majorana scatter

For an A or real-B endpoint with m nonzero coefficients, every signed scatter is a permutation. The exact endpoint operator has norm1, including real-B whose square is-I. Let eta bound the Euclidean coefficient error, and L bound sum|stored coefficients|. CAR yields operator coefficient error<=eta. For m products accumulated from zero, use the deliberately conservative gamma_(m+1) bound and2m absolute rounding injections per coordinate. Define

epsilon_m=eta+gamma_(m+1)L,
a_m=s*2m*zeta/(1-u)^(m+1).

Then ||computed_G(x)-Gx||<=epsilon_m X+a_m for any certified X>=||x||. This follows by scalar rounding bounds, Minkowski and permutation invariance; no dimension factor multiplies the relative term. m=4 at the center and m=11 or15 at a neighbor, with exact-zero skipping only. Hence the computed intermediate norm is at most(1+epsilon_m)X+a_m. No intermediate scan is needed.

## Two independent neighbor-center chains

For neighbor j and center0 define

e_j=epsilon_j X+a_j,
Y_j=X+e_j,
e_0j=e_j+epsilon_0 Y_j+a_0,
Z_j=X+e_0j.

The second action's inherited error is not amplified because its exact norm is1. Equivalently e_0j=[epsilon_j+epsilon_0(1+epsilon_j)]X+(1+epsilon_0)a_j+a_0. The two chains are independent, not four serial operations. Scaling by native K0j=±2 is exact when finite and cannot underflow; each scaled candidate norm is bounded by V_j=2 Z_j and its action error by2e_0j. For general non-power-two |t|, separately price coefficient/scaling errors; these formulas use the frozen t=1 units, with dimensional rescaling performed analytically afterward.

## Diagonal and two final additions

Let stored positive frequencies be nuhat_j, exact radii d_j, T=sum|nuhat_j|, Delta=sum d_j, and Lambda0=sum exact sqrt(lambda_j) enclosed above rationally. The computed occupation-energy coefficient is bounded by

Dmax=T+gamma_21*T+21*zeta/(1-u)^21.

Its error from the exact coefficient is at most d0=Delta+gamma_21*T+21*zeta/(1-u)^21. Multiplying by real x has vector error

E_D=(d0+u*Dmax)X+s*zeta,
Q0=Lambda0 X+E_D.

For the two scaled chain additions use

A1=u(Q0+V1)+s*zeta, Q1=Q0+V1+A1,
A2=u(Q1+V2)+s*zeta.

The complete positive pair action obeys

E_H=E_D+2e_01+2e_02+A1+A2,
||yhat||<=Y_H=(Lambda0+4)X+E_H.

The exact +K B_real A sign and neighbor-first ordering are required. These bounds deliberately overcount cancellations and use no observed intermediate norms. An implementation with a fused common-center action needs its own changed proof; it cannot inherit this two-chain count silently.

## Residual: only X and rhat require full scans

Let Bhat be a certified upper bound on the actual stored right-hand-side norm. Form rhat=fl(bhat-yhat) and scan its exact dyadic squared norm to obtain Rhat>=||rhat||. Then

rho=Rhat+E_H+u(Bhat+Y_H)+s*zeta

bounds ||bhat-A xhat||. One exact dyadic scan for X=||xhat|| and one for Rhat suffice at each checkpoint. Bhat comes from an exact known vacuum norm or the propagated construction bounds below; neither yhat nor individual Gamma/partial-sum vectors require a scan. If the source itself approximates a true source with error Berr, the solution error is(rho+Berr)/delta, delta=1/3 in these units. Do not count source uncertainty twice by placing it in both rho and Berr. Exact norms use streaming integer sums of dyadic squares and outward integer-square-root brackets; ordinary numpy norms are not replacements.

## Four Eg blocks and exact signed permutations

A normalized Eg block R is orthogonal. Obtain Frobenius radius eta_E for its four stored entry errors and a rational L_E>=||abs(Rhat)||2, for example ||Rhat||F<=sqrt2+eta_E. A real two-term dot product is covered conservatively by gamma_3 and three underflow injections per output. Thus for the whole parity-vector Eg action,

epsilon_E=eta_E+gamma_3 L_E,
a_E=3s*zeta/(1-u)^3,
E_E(X)=epsilon_E X+a_E.

The00 action is a copy and11 uses the exact determinant±1; only01/10 mixing rounds. The displayed dimension factor conservatively includes all coordinates. The top-parity-bit block is the same orthogonal action in a different storage order. Three local signed T permutations are exact. Four sequential Eg blocks therefore have error tau_T(X)=[product_(j=1..4)(1+epsilon_Ej)-1]X + sum_(j=1..4) a_Ej product_(l=j+1..4)(1+epsilon_El). For equal envelopes this is[(1+epsilon_E)^4-1]X+a_E sum_(j=0..3)(1+epsilon_E)^j. Their output norm is at most X+tau_T(X). This explicitly includes irrational-entry rounding and fixes the vacuum phase.

## Six-source and fifteen-output sums

For n stored real vectors with certified norms X_i, summing sequentially from a copy of the first yields error

S_n=gamma_(n-1) sum_i X_i + (n-1)s*zeta/(1-u)^(n-1).

Use n=6 for each odd source and n=15 for the final vertex. Their candidate sum norms are bounded by sum_i X_i+S_n, without scans. For the odd source apply the center real-B action to the six-vector candidate sum; its additional error is epsilon_0(sum X_i+S_6)+a_0. Add S_6 and all inherited first-solution/transport errors to obtain Berr. Bhat is bounded by sum X_i+S_6 plus this computed center-action error, since the exact center norm is1. The omitted overall i does not change norms.

For the final vertex, add inherited second-solution/transport errors and S_15, then divide by8. Binary division by8 is exact for normal results but may underflow, so include an additional s*zeta in the final norm error. Thus E_chi=[sum inherited second errors+S_15]/8+s*zeta. Its total norm bound is obtained by the same formula from the15 candidate norms. The previous four-solve propagation weights remain unchanged.

## Fixed practical certificate schedule

Keep the prospective four systems,256-iteration cap and checkpoints16,32,...,256 from540c8154. At each checkpoint perform one fresh real pair action, the X scan and residual scan, and rational evaluation of this envelope. CG's recursive residual is candidate-generation state only. At most64 checkpoint certificates require128 full exact norm scans, plus final particle-count/total norms; no scans are required for each scatter intermediate. Candidate dot products/axpy work still needs full cost accounting even though their rounding need not be trusted for the final a posteriori certificate.

The target remains E_chi<=10^-6 in t=1 units, with the earlier first/second residual thresholds and all transport/source contributions included. Whether it can be reached within256 iterations is a numerical outcome, not proved here. Real arrays halve candidate storage relative to complex arrays, but finite-environment evidence, interval coefficients, norm-scanner implementation, whole memory and worst-case timing remain prelaunch obligations. This design licenses no physical run and makes no exact-zero multiparticle claim.

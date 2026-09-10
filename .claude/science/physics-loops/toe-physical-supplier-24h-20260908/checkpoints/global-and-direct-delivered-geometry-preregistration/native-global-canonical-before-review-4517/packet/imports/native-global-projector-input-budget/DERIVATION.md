# A-only operator acquisition and separate joint-kernel consumer precision

Source-only sufficient budget for the NEW378-node ratio4 candidate. No actual poles, A/C values, selected T, Gram matrices or histories evaluated. Units h=1; SCALING_BRIDGE governs restoration and positive/negative polarization signs. The exact candidate uses physical resolvent columns, not a numerically fabricated Gram square root.

## 1. What defines the operator

At each exact positive quadrature node s and weight w, use unnormalized U=[e0,d], ||U||²=2, and physical columns X_±=R0(±is)U. The finite coefficient T=(I+V G)^-1V, V=2iJ2, depends only on

 G=i[[s A,-2D],[2D,2s Bgeo]], D=(1-s²A)/6,
 Bgeo=A (P) or D (O).

It does NOT depend on Bgreen,cminus,C or reference-Gamma cross-Grams. Their accuracy matters to the downstream finite numerical consumer, not to the mathematical definition of this finite-rank operator.

Define the numerical candidate using exact physical columns at exact dyadic midpoint nodes, exact rational midpoint weights, and certified2x2 approximate coefficients. This is a legitimate specified finite-rank operator even before computing its complete Gram. Column descriptors are not approximate sampled wavefunctions. If an implementation later replaces those physical columns by a common approximate factor, its factor error is an additional consumer/representation budget; it cannot be silently set to zero.

## 2. Explicit uniform acquisition constants

For s∈[2^-32,16], unnormalized local column HS norm² is at most L²=3a=17/20. The normalized-source Woodbury bound from the trace-class proof is9(1+beta sqrt(a)) with beta<3 and sqrt(a)<3/5, implying ||T||<76 also in the unnormalized convention. This is deliberately loose and uniform.

A scalar radius epsilon_A perturbs G by operator norm at most1451 epsilon_A: each offdiagonal error is s² epsilon_A/3, and the largest row sum is bounded by s²/3+2s max(1,s²/6)<1451. If epsilon_A<=2^-20 then ||T deltaG||<1/2 and the exact inverse identity gives ||deltaT||<=2*76²*1451 epsilon_A. With midpoint weights summing to at most17, the resulting projector S1 error is at most2^27 epsilon_A.

A pole displacement rho_s is bounded using X'_s=iR_s X_s, ||X'_s||HS<=L/s, G'_s=iU*R_s²U with norm<=L², and T'=-T G' T. Consequently

 ||F'(s)||1 <=130/s+4174,

for F=R_A-R0. Exact weights total<16 and pi>3 imply a total pole error<=2^42 rho_s, provided each complete root bracket lies in the declared interval.

A per-weight absolute radius rho_w gives at most2^13 rho_w over378 nodes, since ||F(s)||1<=L²*76 and378 L²*76/3<8192. Midpoint weight sum<=17 is verified independently. An additional direct2x2 coefficient operator rounding radius epsilon_T contributes at most5 epsilon_T. A reciprocal-pi radius rho_pi contributes at most2^12 rho_pi, including quadrature and low/high correction coefficients; the conservative bound allows approximateT norm<=153,17totalweight and the finite high-series geometric sum.

Therefore the sufficient input bound is

 E_input <=2^27 epsilon_A+2^42 rho_s+2^13 rho_w+5 epsilon_T+2^12 rho_pi. (1)

The low endpoint correction has exact rational frequency2^-32 and exact coefficient3V; the high correction has exact integer powers and rational coefficients before reciprocalpi. Their basis descriptors are exact physical inverse/power columns. No A0,mu,nu,C or B value is needed to define those operators. Computing their Grams later is separate. Exact rational coefficient generation is allowed to have zero mathematical rounding error; a future fixed-point implementation must include its actual coefficient bound in(1), not assume it.

A concrete sufficient acquisition target is A full width1e-30 (hence radius<=5e-31), root andweight radii2^-160, directT rounding operator radius2^-80, reciprocalpi radius2^-180. Equation(1) is then far below8e-13. These are verification targets, not claims about a nominal bit setting. A' is not required by (1); the same width may be requested for later kernels but has no automatic consumer verdict.

No square root of a global Gram error appears in (1), because it compares actual physical-column operators. Applying the old common-factor comparison to reconstruct an entire approximate frame at1e-12 would impose much more stringent Gram accuracy. That is a different task and is not hidden here.

## 3. Joint-kernel Gram variables with no low-pole cancellation

Let B(s)=E[sqrt(X)/(X+s²)], c=B(0), C(s)=E[1/(sqrt(X)(X+s²))]. Use B(s)=c-s²C(s), never an independent c-B subtraction divided by s². Define the joint kernels

 K_A(s,t)=E[1/((X+s²)(X+t²))],
 K_B(s,t)=E[sqrt(X)/((X+s²)(X+t²))].

At s=t use K_A=-A'(s)/(2s), K_B=-B'(s)/(2s)=C(s)+(s/2)C'(s). A C-value certificate alone does NOT supply the confluent or two-point K_B certificate. A normalized derivative sC'(s), or a direct positive K_B calculation, is a needed interface. James's proposed C width1e-20 is therefore only one ingredient.

For signed q=sigma*s,r=tau*t, put E_B=B(s)+r(q-r)K_B, F_B=(r-q)[B(s)-r²K_B]. Then exactly

 (B(t)-B(s))/(q+r)=(q-r)K_B,
 (rB(t)+qB(s))/(q+r)=E_B,
 (t²B(t)-s²B(s))/(q+r)=F_B.

These identities extend to q+r=0 by continuity. They remove the artificial small denominator before interval evaluation. Insert them into the actual common-source L matrix decomposition E0 B+E2 s²B+O1 qB, whose entry magnitudes are at most2,1/3,1/3. This gives the explicit unbalanced J-entry radius

 rho_J <=11 epsilon_c+2816 epsilon_C+2966 epsilon_KB.           (2)

For G define K_D=(A(s)-t²K_A)/6 and E_A=A(s)+r(q-r)K_A, E_D=D(s)+r(q-r)K_D. The actual C_sigma matrix decomposition into qA,qD,D with entry coefficients<=2 gives

 rho_G <=269 epsilon_A+47446 epsilon_KA.                       (3)

All coefficients are bounded on s,t<=16; neither (2) nor(3) divides by s² or by an almost coincident signed denominator. Pole uncertainty must still be evaluated over the joint boxes or charged by kernel derivatives. Gauge/half-chirality selectors have exact signs; any selector l1 amplification is applied before calling these bounds a particular entry radius. The stated constants apply to the canonical three-source signed W, not an arbitrary6-source projection.

## 4. Exact saved preconditioning, not an entrywise C gate

Let W=S T with the exact saved rational T for the unchanged selected24-pair span. Let H=W*W have certified aI<=H<=bI, a>0; use a rational inverse candidate X with r0=||I-HX||. The projection is W H^-1 W*, and cross block D_j=T*(S*F_j). The exact T is retained; no newly fitted frame or C-width test is required.

Set tau=||T||F, m48,r4. Scalar balance is alpha_j=35w_j/(2pi), with alpha_j<=70 and sum alpha_j<280/3. Old selected balances also lie below70. If unbalanced cross entry radius is rho=max(rho_G,rho_J), then

 ||delta D_j||F <=sqrt(alpha_j)*tau*sqrt(70*m*r)*rho.             (4)

This explicitly exposes coefficient magnification. It must be computed from the actual rational T or bounded by a source-verified norm; tau=1 is NOT assumed. If the half-chirality source transform has l1 norm1 it adds no factor; otherwise include its exact l1 norm in (4).

Let mu_j bound self-block operator error, d_j the right side of(4), and dnorm_j a certified norm of the computed cross block. With K_j=M_j-D_j*H^-1D_j and computed Khat_j=Mhat_j-Dhat_j*X Dhat_j,

 ||K_j-Khat_j|| <=mu_j+(2 dnorm_j d_j+d_j²)/a+dnorm_j² r0/a+arithmetic. (5)

This is direct matrix perturbation, independent of any smallest eigenvalue of M_j. The metric uncertainty enters a and r0; it is not charged twice as a separate fictitious frame perturbation.

## 5. Precision dictated by the consumer, not guessed from C width

A simple node bound uses fixed certified kappa>=||C_j|| (kappa3 is safe from76/35) rather than a delicate absolute-value matrix. Then the streaming projection objective is bounded bysum_j kappa sqrt(Tr M_j Tr K_j). The trace radii are at most r times the operator radii. Square-root Holder near a zero residual is unavoidable for this conservative objective. For positive m,k and their uncertain changes, use

 |sqrt(mk)-sqrt(mhat khat)| <=sqrt(mhat delta_k)+sqrt(khat delta_m)+sqrt(delta_m delta_k),

with nonnegative certified upper quantities. This is an upper-error bound, not permission to clip a contradictory negative upper interval into zero.

Equations(2)-(5), the actual a,b,tau,r0 and node traces determine the required C/K_B radii for a specified objective tolerance. For orientation only, if a>=1/2,b<=2,tau<=1, self-error/inverse/arithmetic already allocated, and epsilon_c,epsilon_C,epsilon_KB<=epsilon, then rho_J<=8192epsilon and the C-induced traceK error can conservatively be bounded by alpha_j*2^25 epsilon for epsilon<=2^-40. Since Tr M_j<=alpha_j*(17/10), summing yields an objective uncertainty no larger than3*(280/3)*sqrt((17/10)*2^25 epsilon). At epsilon1e-20 this conservative contribution is of order2e-4, not1e-12. It scales with actual tau through(4)-(5). This illustrative bound is not an assertion that the actual T meets tau<=1.

Thus a proposed C width1e-20 cannot be declared sufficient for the consumer without its actual metric/coefficient and target ledger. Conversely it is not required for the A-only operator certificate (1). The exact choice follows from the downstream objective tolerance; no generic unexplained eta reserve is being assigned.

## 6. Remaining scientific and executable gates

The NEW378 A/root/weight acquisition can target(1) independently of C. A complete runtime must bind the new Gauss roots/weights, verify their radii/positive sums and every2x2 coefficient radius, retain failures, and carry the exact low/high descriptors. Its numerical S1 certificate compares the operator defined by those physical descriptors, not a stored dense matrix.

The streaming Gaussian/Ward consumer remains open until joint K_A/K_B and C inputs, old-family/new-cross consistency, actual preconditioned metric, inverse, and scalarDelta/observable budgets are certified. No physical source evaluation or acquisition launch occurs in this proof. All old protocols and cached centers remain immutable.

Precision decision: an earlier draft suggested1e-49 as merely sufficient. This was unnecessarily strong:2^27*1e-30<1.35e-22. The established192-bit/160-term supplier may be used at the NEW points, subject to its actual fullwidth1e-30 gate. No standalone high-precision pilot is motivated by this operator budget. JointC/near-confluent derivative precision is a distinct later protocol.

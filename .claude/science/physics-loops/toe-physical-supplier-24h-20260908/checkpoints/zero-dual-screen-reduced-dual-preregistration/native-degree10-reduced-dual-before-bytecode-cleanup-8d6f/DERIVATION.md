# Reduced native degree10 dual residuals, h=1

Source-only, unreviewed. No actual scalar, coefficient, moment or saved result is evaluated. This retains the SAME degree1 first polynomial and constant q, with the accepted spectral error bounds as future inputs. It changes the signed error certificate, not the physical trial. The general dual identity and sharp L are imported from298c/eaf0 and independent reviewc622.

Write g=gamma(a), B_A=i g gamma(d), J_A=2i gamma(d), d=d_A, k=Ka, ||d||²=2. Let p_C=u_C+w_C D_C and q_C be the fixed existing real coefficients. The actual sign convention is x0_C=-(u_C+w_C B_C)Omega, v0_C=q_C(2iu_C gamma(d_C)+4w_C g)Omega, with coupling Ccouple=-J and Ccouple*=J. Here the indexless vector u below is an adjoint gradient, not the scalar polynomial coefficient u_C.

For one fixed channel A, sum over its six disjoint neighbors C and define
 U=sum u_C, Z=sum q_C w_C,
 W=sum w_C d_C, R=sum q_C u_C d_C,
 alpha=-2U-4Z, beta=-2(W+R).

Then the two gradient vectors have exact local representatives
 u=(Tg)*x0 = [-U g-i gamma(W)]Omega,
 w=2Tx0-Tg v0 = [alpha I+i g gamma(beta)]Omega.                (1)

The first is linear and the second scalar-plus-quadratic. This follows by multiplying the common g through each trial, not by a norm estimate or assuming H commutes with T.

## Exact reduced H actions

Use [H0,gamma(f)]=i gamma(Kf), H0Omega=0 and H_A=H0+B_A. With v=Kd and representatives understood on Omega:

 J_A u = 2iU g gamma(d)+2 gamma(d)gamma(W),                    (2)
 H_A u = gamma(KW)+iU gamma(d-k)+g gamma(d)gamma(W),           (3)
 H_A w = -gamma(k)gamma(beta)-g gamma(Kbeta)
           +i alpha g gamma(d)+gamma(d)gamma(beta),          (4)
 H_A J_A u = -2U gamma(k)gamma(d)-2U g gamma(v)
           +2i gamma(v)gamma(W)+2i gamma(d)gamma(KW)
           +4U I+4i g gamma(W).                             (5)

Every sign in(2) uses gamma(d)g=-g gamma(d). The apparent quartic impurity terms in(4),(5) collapse because g²=1 and gamma(d)²=2. Thus(2),(4),(5) are quadratic (possibly with a scalar), and only(3) can be cubic. These are identities for H acting on the specified polynomial vacuum vectors. They are NOT identities replacing H by commutation alone on arbitrary states.

The first residual and inner residual also reduce:
 r_A=[(-1+2w_A)I+i u_A g gamma(d)
          -w_A gamma(k)gamma(d)-w_A g gamma(v)]Omega,         (6)
 s_A=[2iu_A gamma(d)+(4w_A+4q_Au_A)g+2q_Au_A gamma(v)
          -4i q_Aw_A gamma(k-d)]Omega.                      (7)

Indeed r=-Omega-Hx0; s=Ccouple x0-Hv0=JpOmega-qH JpOmega, and H JpOmega=-2u_A gamma(v)-4u_A g+4i w_A gamma(k-d). In particular s is linear, not a generic cubic vector. No inverse is evaluated in(1)–(7).

## Finite native vector bank and scalar closure

Set b_j=epsilon_j e_j for the six neighbors, so k=sum b_j and d is the signed pair sum. If A is an opposite pair, its complement contains two opposite pairs, and
 W=(2w_P+w_O)(k-d), U=4u_P+2u_O.

If A is perpendicular, let e be the opposite pair on the third, untouched axis. Then
 W=3w_P(k-d)+(w_O-w_P)e, U=5u_P+u_O.

The same formulas with coefficient w_C replaced by q_Cu_C give R, and with u_C replaced by q_Cw_C give Z's class counts. Hence W,beta are in span(d,k,e), and KW,Kbeta in span(Kd,Kk,Ke). One can use the seven-vector bank(a,d,k,e,Kd,Kk,Ke) for P and omit e,Ke for O (five vectors). Alternatively compute all15 channels without asserting class equivalence. These are fixed literal geometric identities from the six disjoint pairs, not a fitted reduction.

For any neighbor combinations f=sum f_j b_j and h=sum h_j b_j, define n=sum f_jh_j and m=sum f_jh_(j xor1). The complete required two-point data are
 <f,h>_real=n;
 <Kf,Kh>_real=6n+m;
 <a,Kf>_real=-sum f_j;
 kappa(a,f)=-(c/2)sum f_j;
 kappa(Kf,h)=3c*n+(nu/6-3c)*m.

Other same-color kappa and opposite-color dots vanish; reverse kappa changes sign. These formulas are the polarized native seven-star identities already used for the closed degree10 kernels. They supply every entry of this reduced bank using only c=mu/3 and nu. In particular Kk=K²a introduces no omega5: it is a linear combination of Kb_j, and all required covariances have at most one K on each neighbor combination. The norm/residual bounds E,F retain whatever omega5 provenance their separate spectral certificate requires.

## Complete new data and conservative count

Per channel acquire the real4-by4 Gram matrix of(w,Hw,Ju,HJu), the real2-by2 Gram matrix of(u,Hu), and the three signed real contractions
 c0=Re<r,w>, c1=Re<r,Ju>, c2=Re<s,u>.

These are13 real Gram entries plus3 signed entries. They are not present as a complete set in the saved spectral or posterior outputs. For duals z_A=-t_Au_A and y_A=s0_A(w_A-t_AJ_Au_A), the exact correction is
 sum_A[s0_A c0_A-s0_A t_A c1_A-t_A c2_A].                     (8)

The dual residual norms are the Gram quadratic forms of coefficient vectors
 a_A: (1,-s0_A,-t_A,s0_A t_A),
 b_A: (-1,t_A).

Sum their squared upper norms across channels and use
 W_lower = W0_lower + correction_lower
             - E*sqrt(sum||a_A||²_upper)
             - F*sqrt(sum||b_A||²_upper)+L(E,F).             (9)

No primal/dual residual independence or H/T commutation is assumed. Taking a maximum with all older valid lower certificates is permitted; their errors/nominals must be the same supplied problem. The signed correction can change the center, so the zero-dual necessary screen does not exclude(9).

Literal monomial bounds from(1)–(7) are2,4,2,6 for the four a-vectors;2,3 for the b-vectors;4 for r and4 for s. Their upper-triangular Gram expansions need at most128 and19 Wick words, respectively; three cross contractions add24. Total171 words per channel,2565 per choice,5130 for both existing choices. Word length is at most6. A simple uniform bound is76950 perfect-pairing terms for both choices (15 per six-field word); the quadratic groups in fact require at most3 each. This is a SOURCE operation bound, not an executed profile. It excludes covariance assembly, rational bookkeeping, candidate evaluation and logging overhead, which a future runtime must budget separately. It is orders smaller than the generic degree20 length12 estimate, without raising the primal degree or acquiring new scalar values.

## Deterministic no-search dual proposal

For exact nonzero u and H>=delta, t*=Re<u,Hu>/||Hu||² uniquely minimizes||u-tHu||² over real t, and 0<t*<=1/delta=4. For v=w-tJu fixed, s*=Re<v,Hv>/||Hv||² has the same properties when v is nonzero. Zero vectors give flat objectives and may use0. Positivity follows from spectral calculus, and H²>=delta H proves the upper bound. This is sequential residual minimization, not a theorem of optimality for the final Ward certificate.

A prospective deterministic implementation may use midpoint Gram entries ONLY to propose t, then propose s at that exact t. If a denominator midpoint is nonpositive, fall back to0. Otherwise divide, clamp to[0,4], and round downward to a fixed2^-64 grid. Reevaluate the COMPLETE original interval Gram quadratic forms and signed correction at these exact dyadics. No optimizer enclosure is required for validity. Midpoint Gram need not be PSD; it is not used as a certificate.

Writing G for the4-Gram and B for the2-Gram, the proposals use
 t_mid=B01_mid/B11_mid;
 numerator_s=G01_mid-t(G03_mid+G12_mid)+t²G23_mid;
 denominator_s=G11_mid-2tG13_mid+t²G33_mid.

These expressions require no new contraction beyond the16 entries. Use independent t_A,s_A per each of15 channels, avoiding an unproved symmetry collapse, and retain the all-zero dual as a fixed alternative. There are30 rational divisions per choice at most, no grid search. Every eventual norm upper must be nonnegative; contradictory interval certificates are refused. Actual precision, runtime cost and whether any signed correction is sufficient remain untested. No new physical protocol or runtime is authorized by this proof alone.

# Literal overlaps and a bounded coarse witness supplier

New source-only protocol candidate; no nodes, T or selected IDs are read. Fix X=Z to the seven star site unit vectors and allfive previously fixed selected spans. No post-output choice of sites or impurity is permitted. The witness theorem and actual-real-P proof are those in the paired predecessor files.

## Complete overlap dictionary needed by the contraction

Use the actual real signed three-source W=[e0,dA,dC] and matrices I=W*W,O,T,N=I+O from the common-Gram source. For any real star source z the same bilinear formulas use z*I/W, z*O/W, z*T/W, so selecting each of the seven site rows gives the full7x3 blocks, without extending the scalar dictionary. Let D_s=(1-s²A_s)/6 and sigma=±1.

The raw local-to-pole block is C_sigma=sigma*s*(A I+(A-D_s) O)+D_s T, with the sign convention calibrated by C00=sigma*s*A and C0,dA=-2D_s. The corresponding covariance block is

 L_sigma=-B I-(1+s²/6)B O+(sigma*s*B/6)T.

These reproduce the full3x3 matrices in the source; in particular O_dA,dA=-2 for opposite geometry gives diagonal s²B/3. Resolvent-to-old-resolvent overlaps are exactly G=(C_tau(t)-C_-sigma(s))/(sigma*s+tau*t), J=-(L_tau(t)-L_-sigma(s))/(sigma*s+tau*t), with the stated confluent derivatives. They supply every old raw and Gamma-raw selected seed column by the actual rational half maps. No new spatial scalar is missing for the fixed seven-star block.

For the appended x0=e0/2, xk=wk/2,k=A,C, the literal overlap with a balanced pole column sqrt(alpha)R_sigma e_v is sqrt(alpha)/2 times:

 g0v=sigma*s*A I0v+D_s T0v,
 j0v=B I0v-sigma*s*B T0v/6,
 gkv= -A Nkv+D_s Okv+sigma*s*A Tkv/6,
 jkv=B Tkv/6+sigma[(c-B)Nkv/s-s B Okv/6].

These are exactly the reviewed append_core.cross formula, transposed with G symmetric/J skew when the argument order is reversed. Gamma partner signs follow J, and Gamma-Gamma uses G. Thus Ward poles introduce only (c-B)/s, not (c-B)/s². Store that shared numerator once. The native diagonal rephasing must be used consistently; multiplying a whole source by i changes its displayed real-coordinate signs.

With these blocks form the finite raw real operator node coefficient from the accepted A-only Woodbury blocks, and evaluate

 Wloc=sum_nodes Z*F_node K_node F_node*X
      -[sum_nodes Z*F_node K_node F_node*V] H^-1[V*X].

This is an explicit finite matrix expression for all49 entries. V=S T uses the actual fixed real half/Gamma seed embedding, not a reselected or approximately orthogonal basis. The accepted node coefficients and source signs are reused. No full new-new Gram is required by this expression.

## Why the Ward low pole need not demand extreme precision

For the displayed Ward j formula, |I|,|O|,|N|,|T|<=2 and s<=16 give coefficient-error bound (6+2/s)eta_B+2eta_c/s before balancing. For ratio-four positive weights, sum w<16 and sum w/s<=54. Hence weighted sums are bounded by204eta_B+108eta_c. The node factor1/pi, a conservative local resolvent factor4 and Woodbury norm76 give less than2^17(eta_B+eta_c) before selected-coordinate multiplication. This bound must be applied before any independently inflated C(s) box is introduced.

The selected embedding uses at most96 raw/Gamma labels and48 columns, with half coefficients of absolute sum<=1 per column. The accepted T norm gate||T||<=10^4 then gives a safe whole7x48 cross-error bound below2^39(eta_B+eta_c), including the real half maps and transpose signs. Multiplication by||H^-1V*X||<=sqrt(b)/a<2 gives below2^40(eta_B+eta_c) in the final block. Thus eta_B,eta_c<=1e-22 each suffice for a Ward-error allocation below3e-10. This is deliberately loose; it is still much less demanding than1e-37. It concerns Ward error only, not the remaining old-pole divided differences.

For old-pole differences impose the NEW geometry gate

 |sigma*s+tau*t| >= 1e-6*max(s,t)

unless the exact confluent branch is supplied. Existing old t>=1/128 then gives denominator>=1e-6/128 whenever cancellation is possible. The L polynomial has coefficients bounded by100 on s,t<=16. A crude raw J radius is therefore<=3e10 eta_B. With the same selected-coordinate, node-factor and48/96-dimensional bounds, a conservative final-block allocation may require eta_B as small as1e-28. The weighted Ward cancellation alone therefore does NOT prove that a universal B1e-22 acquisition suffices for all49 entries. To keep the coarse protocol honest, either freeze per-pole weighted divided-difference gains and charge their actual upper bounds before acquisition, or use the stronger uniform B radius1e-30 as a sufficient preliminary design. The exact kernel gain ledger is finite and uses geometry only, not physical values.

## Existing-catalog coarse B candidate and decisive gate

For G_s(t)=E[X/((X+s²)(X+t²))], B(s)=(2/pi) integral G_s(t)dt and
 G_s(t)=(t²A(t)-s²A(s))/(t²-s²).

Reuse the accepted1742 outer nodes, not old B outputs. The old geometry and new378 nodes must pass a pre-acquisition relative-square separation gate |t²-s²|>=g0(t²+s²). For g0=1e-6 and A radius1e-30, input radius can be about1e-24 before weights. This is adequate for a proposed B1e-22 target but cannot certify a1e-30 target. The analytic rho4/p26 remainder and40-term high tail can be far smaller; they do not remove this fixed A(s) uncertainty amplification. Low subtraction epsilon*A(s) has error<=epsilon³ A0/(3s²) and suppresses the old low cutoff error at epsilon2^-64. All of these are new contraction bounds, not a rerun of old B66.

This yields a precise obstruction to promising the full coarse witness from existing scalar caps alone: even after Ward cancellation, near old-pole L divided differences and the exactselected T can make the source-only worst-case block radius exceed1e-7. It is a limitation of these independent interval bounds, not a proof the actual intervals or witness fail.

Minimal next gate is a saved-geometry-only gain ledger (378x66 plus378x1742 separation checks), no scalar reevaluation. It computes the coefficient-weighted radius requirement for each B(s) and each oldB(t). If B1e-22 suffices, new378 B contractions use existing A catalog, with an inferred cost roughly(378/66)*32.92 seconds before method differences and verification; a300s cap would be a prospective bound, not a completion prediction. If a tighterB radius is required, the newA(s) oracle needs radius at most target_B*g0/(32), plus separately charged analytic/rounding terms; e.g target_B1e-28 suggests A radius<=3e-36 at g0=1e-6. This is378 additional point acquisitions in a NEW precision method, not a million unshared calls, and must be preregistered after a fixed cost check if its source precision differs materially.

No execution-ready claim is made for the earlier B1e-22 shortcut. The literal contraction and the stopping gate above decide which precision contract is justified before any physical contraction. A failure to obtain a lower witness remains INDETERMINATE, never evidence of small tau. All completed studies remain immutable.

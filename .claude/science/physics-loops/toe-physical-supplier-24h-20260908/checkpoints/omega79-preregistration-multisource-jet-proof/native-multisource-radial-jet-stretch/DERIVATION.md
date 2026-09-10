# Three-source radial table for the degree3 nominal

Source-only theorem under the supplied canonical infinite pi-gauge lattice and pure negative-band covariance P. All energies are dimensionless h=1. No native scalar, saved trial, or covariance value is evaluated. This extends the reviewed one-pair table; a new multivariate implementation and interval/cost review remain required.

## Signed local sources, not unsigned adjacency

Use K=-sum eta_a(T_a-T_a*) in one fixed sign choice; reversing the overall sign reverses both K and the defined signed sources consistently. Let a=delta0 and b_(+j)=delta_(+e_j), b_(-j)=-delta_(-e_j), so Ka=sum_i b_i. For a pair A put d_A=sum_(i in A)b_i. The canonical staggered signs at the origin give these literal coefficients. K²=sum_j(T_j²+T_j*²-2I), so X=-K² is a translation-invariant two-step scalar operator.

For a radial function f(|h|), write R_j=<a,|h|^j a> when f=|h|^j. Its kernel preserves each coordinate parity. Hence a-to-neighbor and perpendicular-neighbor radial kernels vanish. Same-neighbor kernel is R_j. For opposite neighbors the unsigned displacement kernel is E[cos(theta_1) X^(j/2)]=R_j-R_(j+2)/6: cubic symmetry and X=6-2 sum cos(theta) prove this identity. But the SIGNED b vectors have opposite coefficients, so their kernel is
 L_j=R_(j+2)/6-R_j.
This sign is essential: the opposite-pair diagonal becomes2R_j+2L_j=R_(j+2)/3, agreeing with the reviewed table.

For arbitrary pairs A,C define n=|A intersect C| and o=#{i in A: opposite(i) in C}. Then
 T_AC(j)=<d_A,|h|^j d_C>=n R_j+o L_j.
The formula includes diagonal pairs, disjoint pairs and overlapping pairs. For A=C, n=2 and o is0 for perpendicular or2 for opposite. For disjoint pairs n=0; the remaining signed cross entry is exactly o L_j. No anisotropic scalar integral is introduced.

The odd center-edge entry has its own signed proof. The six quantities a^T K f(|h|) b_i are equal by signed cubic symmetry (or by the explicit two-step convolution and the origin row of K). Summing gives a^T K f K a=-R_(j+2). Thus each is -R_(j+2)/6 and each pair gives -R_(j+2)/3. Odd neighbor-neighbor and center-center entries vanish by bipartite parity. This is not an inference from unsigned adjacency.

## Complete ordinary/projected three-source blocks

In source order F=(a,d_A,d_C), define Q_j=[[R_j,0,0],[0,T_AA(j),T_AC(j)],[0,T_CA(j),T_CC(j)]], and
 O_j=[[0,-i R_(j+1)/3,-i R_(j+1)/3],[+i R_(j+1)/3,0,0],[+i R_(j+1)/3,0,0]] for odd j.
Then D_j=F* h^j F equals Q_j for even j and O_j for odd j. For even j, define Oplus_j by replacing R_(j+1) in the displayed O matrix by the same R_(j+1); it is the matrix of h^j sign(h). Therefore
 B_j=F* P h^j F=(Q_j-Oplus_j)/2 for even j,
 B_j=(O_j-Q_j)/2 for odd j.
In the second formula Q_j uses the odd absolute radial moment, not D_j. Explicitly B_even[a,d]=+i R_(j+1)/6; B_odd[a,a]=-R_j/2; B_odd[d_A,d_C]=-T_AC(j)/2. Lower entries are conjugates. Negative-band signs and the physical ordered Majorana contraction are different conventions. At j0, B0[a,d]=+ic/2 since R1=3c; Tr(P V_A)=2c remains the independent normalization check.

For even j=0 the sign expression uses K/|h|, which is bounded as a whole; no globally bounded inverse |h| is assumed. The displayed local scalar integrals exist. For j>=0 the table follows directly from P=(I-sign h)/2 and [P,h]=0.

## Mixed nominal determinant and degree filtering

For p degree3 and constant q, exact nominal kernels are derivatives of
 Z(t,z,s)=<Omega,exp(-t D_A) exp(2z B_C) exp(-s D_C)Omega>.
The relative one-particle product is U=exp((t+s)h0) exp(-t h_A) exp(2z V_C) exp(-s h_C). Its squared vacuum expectation is det(I+P(U-I)), with branch1 at zero and original vacuum subtraction retained. Zeroth z coefficient supplies <D_A^i Omega,D_C^j Omega>; first z derivative supplies <D_A^i Omega,2B_C D_C^j Omega>. Derivative signs are (-1)^(i+j); gJ_C=2B_C and the original x0=-p gives the plus nominal insertion. Do not change order A/C in the exponential product without conjugating the intended kernel.

For z-degree0, the total t/s degree is at most6. For z-degree1 it is at most7, counting the marker as one quadratic perturbation. In the logarithm, every nonconstant relative word has a perturbation. Any term with only ONE perturbation has projected trace independent of its position along free propagation, because P commutes with h0. Accordingly it contributes only a linear t,s or z coefficient; all higher-degree one-perturbation traces vanish analytically. In particular the marker-only term is conjugate to V_C and has no positive t/s degree. Every surviving cumulant of totaldegree>=2 has at least two perturbations, leaving at most totaldegree-2 free h letters.

Splitting traces at V_A/V_C=F J_A/C F* yields precisely the three-source D_j/B_j above, with total segment degree bounded by5 for the marker degree7 sector, and4 for the plain degree6 sector. Scalar exponential reconstruction does not increase the largest cumulant order. This cancellation must be enforced BEFORE table acquisition; numerically cancelling high-degree boxes does not justify the reduced count.

Through j5 the largest odd radial moment in T is R7, and the largest even moment is R6. Even j4 center-edge uses R5; odd j5 center-edge uses R6. Therefore c,nu,omega5 and prospective omega7, plus accepted exact even R0,R2,R4,R6, suffice for this degree3/constant-q pair nominal. Omega9 is unnecessary for this particular nominal, though useful for the separate m0..10 first-residual construction. No new anisotropic oracle is required. This conclusion does NOT yet establish closure of the J-reflected inner residual kernel table, whose extra h d sources require a separate total-degree accounting.

## Finite counts and remaining work

The complete unshared j0..5 table has6 ordinary plus6 projected3x3 matrices:108 complex slots per ordered pair before Hermiticity/parity reuse. There are90 ordered disjoint pairs,16 powers per kernel type and two kernel types:2880 requested derivatives. The truncated rectangular jet indices i,j<=3,k<=1 have32 coefficients, each totaldegree<=7. These are exact census bounds, not runtime product counts. Cache may use the literal labels and their (n,o,typeA,typeC) data only after proving all coefficient matrices agree; the table itself is already fixed by that data.

No Gram inverse or assumption that three sources are independent occurs. A word-tagged multivariate logarithm/exponential recurrence can implement the total-degree rule using the above3x3 contractions. Its rational growth, product count, width and runtime remain to be designed. No native trial or nominal was evaluated; this is a new supplier-closure proof, not a successful Ward certificate.

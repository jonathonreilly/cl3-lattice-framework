# Reflected-J inner kernel with its scalar convention retained

Source-only new proof proposal, h=1. No native scalar, moment, table or jet was evaluated. This extends the conditional relative Gaussian determinant bridge, not a ready scientific runtime. The original degree3 nominal closure is a separate source.

## Exact CAR reflection

Let a,d be real, a·d=0, ||a||=1, ||d||²=2. Put g=gamma(a), J=2i gamma(d), U=gamma(d)/sqrt2. Then U*=U, U²=I, J*=−J, and

 J* exp(-zD) J=8 U exp(-zD) U=8 exp(-zD'), D'=UDU.

For any real f, U gamma(f)U=gamma(O f), O=dd^T-I. On quadratic operators the global minus is immaterial, so use R=I-dd^T=-O. It is an orthogonal reflection with Ra=a and Rd=−d. With h0=iK, B=i gamma(a)gamma(d), V=2i(ad^T-da^T),

 D=gamma^T(h0+V)gamma/4-E0,
 D'=gamma^T R(h0+V)R gamma/4-E0.

The scalar subtraction is the SAME E0; quadratic orthogonal conjugation introduces no scalar. RVR=−V. Since d* h0 d=0,

 R h0 R-h0=-d(h0d)*-(h0d)d*.

Thus D'=H0+B', where

 B'=−i gamma(a)gamma(d)+(i/2)gamma(d)gamma(Kd).

An independent commutator derivation is U H0 U-H0=U[H0,U]=(i/2)gamma(d)gamma(Kd), and UBU=−B. This fixes both signs. There is no extra arbitrary energy constant, and no substitution of the impurity ground energy.

As a check of the original-vacuum mean only,

 <D'>=e_d/2-c, e_d=<d,|h0|d>,

which is2c for P and nu/6-c for O. This is an identity in supplied symbols, not a numerical evaluation. Normal ordering D' against a different vacuum would require a new scalar convention and must not be silently substituted. Unitary conjugation retains D'>=delta.

## Finite defect and source table

Use F=(a,d,v), v=h0d, which is generally imaginary. The Hermitian finite coefficient matrix for V'=R(h0+V)R-h0 is

 J'=[[0,-2i,0],[2i,0,-1],[0,-1,0]], V'=F J' F*.

Equivalently use real sources(a,d,Kd), with coefficient matrix
 [[0,-2i,0],[2i,0,i],[0,-i,0]].

Both matrices have rank2; no independence of the three physical columns is assumed. The reflected free operator is absorbed as another bounded finite-rank defect relative to the SAME free h0. It is not necessary to acquire a new global reflected covariance.

For either ordinary h^j or projected P h^j moments, the3x3 matrix in(a,d,h0d) is obtained from the fundamental2x2 table D_j or B_j by shifting powers:

 [[M_j(a,a),M_j(a,d),M_(j+1)(a,d)],
  [M_j(d,a),M_j(d,d),M_(j+1)(d,d)],
  [M_(j+1)(d,a),M_(j+1)(d,d),M_(j+2)(d,d)]].

Here M denotes D or B, not an absolute radial scalar. Hermitian lower entries and the complex nature of h0d must be retained. Replacing h0d by Kd without changing its coefficient/phases would be wrong.

## Required degree for a cubic first polynomial and constant q

For b=Jp(D)Omega, degree p<=3, the needed s_j=<b,D^j b>, j=0,1,2, are derivatives of

 <Omega,exp(-tD) J* exp(-zD) J exp(-sD)Omega>
 =8<Omega,exp(-tD) exp(-zD') exp(-sD)Omega>.

The normalized expectation on the right equals1 at zero and has relative one-particle product

 exp((t+z+s)h0) exp(-t(h0+V)) exp(-z(h0+V')) exp(-s(h0+V)).

Use the analytic determinant square-root germ of this product and then multiply by8. This relative factor includes the original E0 subtraction for all three times. There is no additional exp(-z times an inferred mean) factor.

The derivative rectangle i,k<=3 and j<=2 has48 coefficients and totaldegree<=8. Treat V,V' as fixed finite perturbations when cancelling all higher one-perturbation projected traces. Each surviving term has at least two defect factors, leaving at most totaldegree-2 BETWEEN-factor free h letters. However V' has h0d in its source bank: at most one extra free power can appear at each end of a contracted segment. A segment can therefore require fundamental power up to totaldegree, NOT merely totaldegree-2. This two-power endpoint charge is mandatory.

For totaldegree8, the fundamental(a,d) table is thus needed through power8. By the independent native table9e8555db this is supplied by c,nu,omega5, prospective omega7/omega9, and exact even radial moments throughR10. No omega11 or anisotropic spatial moment is forced at this degree. This is sufficient, not a claim that further algebra cannot reduce the inputs.

If the inner spectral residual asks instead for s0..s4 at the same cubic p, totaldegree reaches10, the fundamental power bound becomes10, and omega11 plus exact evenR12 can be required. One must not reuse the constant-q s0..2 supplier claim for that stronger problem.

## Cost representation and open implementation

The shifted3x3 table for between-source powers0..6 has126 unshared complex slots (7 ordinary and7 projected blocks) per class; all are reductions of the fundamental2x2 table through8. The two P/O classes require at most96 multivariate coefficients before class/coefficient reuse; subsequent p-weighted combinations are finite. Those are source-table/jet census bounds, not arithmetic or runtime forecasts.

A filtered multivariate log implementation must tag both total order and endpoint free powers. A naive dense Krylov Gram can request unnecessarily high powers and does not inherit this reduced count. The same finite-rank coefficient calculus avoids Gram inverses. All source uncertainty, cancellation, marker derivative factors8 and(-1)^(i+j+k), and original p coefficients must be retained through directed interval evaluation. New omega7/omega9, exact-even inputs, native binding, proof review and bounded implementation remain unsupplied. No scientific execution is authorized by this proof.

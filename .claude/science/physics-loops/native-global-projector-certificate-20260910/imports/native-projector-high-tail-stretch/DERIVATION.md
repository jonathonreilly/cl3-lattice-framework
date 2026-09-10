# Analytically integrated high-frequency projector correction

Source-only provisional derivation, based on the complete LOW_RANK_PROJECTOR_CERTIFICATE.md and TRACE_CLASS_IMPURITY_PROJECTOR.md and the local2x2 resolvent identities in UNIFORM_PAIR_GAP.md. No native matrix, moment catalog, quadrature node or integral was evaluated. Let A=h_A,B=h0 and V=A−B in the supplied infinite model, h=2|t_hop|. Link flips preserve the six absolute hopping magnitudes, so ||A||,||B||<=W=6h by the Schur row/column bound. V has rank2 and ||V||1=4sqrt2 h<6h.

## Convention and exact correction

For a self-adjoint operator with no zero atom, P_+=(I+sign h)/2. Thus the positive-projector difference uses PLUS(2π)^−1 times the integral of the Hermitian resolvent difference. The cited old low-rank proof uses MINUS and concerns P_−. Bounds below apply to either; use σ=+1 for P_+ andσ=−1 for P_−, never silently exchange them.

The high-s contribution from S to infinity is approximated by the explicitly finite-rank Hermitian operator

 T_N=σ/π Σ_(n=0)^(N−1) [(-1)^n (A^(2n+1)−B^(2n+1))/((2n+1)S^(2n+1))].

Indeed (h−is)^−1+(h+is)^−1=2h(h²+s²)^−1. Finite geometric division gives the displayed odd powers and remainder2(-1)^N h^(2N+1)(h²+s²)^−1/s^(2N). Although A and B are not trace class, every difference of their positive integer powers is finite rank by telescoping.

## Direct nuclear remainder bound

Write m=2N+1 and V1=||V||1. For s>0,

 ||A^m(A²+s²)^−1−B^m(B²+s²)^−1||1
 <=mW^(m−1)V1/s² +2W^(m+1)V1/s⁴.

The first term uses ||A^m−B^m||1<=mW^(m−1)V1 and the resolvent bound1/s². For the second use the second resolvent identity, ||A²−B²||1<=2WV1, and ||B^m||<=W^m. No commutation between A and B is assumed. Multiplying by1/(πs^(2N)) and integrating gives

 ε_high <= V1/(πS) (W/S)^(2N) [1+2(W/S)²/(2N+3)].       (1)

This direct bound is valid even without W<S; usefulness requires decay, and the present S=16h satisfies W/S=3/8. Consequently

 ε_high <(1/8)(9/64)^N [1+18/(64(2N+3))].               (2)

N=6 makes(2)<10^-6. This replaces only the old omitted high tail2*2^-4=1/8. The old low tail and quadrature error remain unchanged and can dominate; it does not make the entire projector error10^-6. There is no new oracle in the analytic correction, but constructing its finite coefficients/Gram and certifying cross terms is a new computational task.

## Finite native support and required moments

Let U contain center v and normalized signed two-neighbor vector u, with V=U C U*. Telescoping A^m−B^m=Σ_(j=0)^(m−1)A^j V B^(m−1−j). Induction on j shows A^jU lies in span{B^kU:0<=k<=j}. Therefore range(T_N) is contained in the bare Krylov space

 K_N=span{B^jU:0<=j<=2N−2}, dim<=4N−2.

T_N is Hermitian, so both its domain support and range are contained there. At N6 the degree is10 and rank bound22. This does not place those22 directions inside the current selected24 trial span; their overlaps and projection residual remain required.

Set M_k=E X^k, X=4h²Σsin²k. The exact local Green identities imply

 U*B^(2k)U=diag(M_k,M_k) for perpendicular pairs,
 U*B^(2k)U=diag(M_k,M_(k+1)/(6h²)) for opposite pairs,
 U*B^(2k+1)U has zero diagonal and offdiagonals
 −i sqrt2 M_(k+1)/(6h), +i sqrt2 M_(k+1)/(6h).

These follow by matching the convergent large-s Laurent expansion of the exact projected resolvent: its diagonals are isA(s),isB(s) and offdiagonal−i sqrt2 h D(s), with6h²D=1−s²A. The common notation B(s) here is a scalar Green entry, distinct from the operator B=h0. Comparing finite coefficients is justified for s>||h0||.

Gram entries of K_N require powers through4N−4, hence integer moments M_0,...,M_(2N−1). At N6 only M_0..M_11 are required. Finite coefficient recursion for A^jU uses no higher moments. These moments have exact finite lattice-walk/binomial formulas; accepted scalar high-moment schemes already use such formulas, but no actual stored moment array has been read or declared sufficient by hash in this proof. An implementation must bind its own exact moment certificate. No nonzero-s Green oracle is intrinsically needed for these Krylov self-Grams. Cross-Grams with existing resolvent columns reduce by polynomial division to their existing local Green entries plus moments, with nearcoincident and rounding rules still to be specified before execution.

## Avoiding a needless new half-moment requirement

Exact left P0^−-projected Krylov Grams introduce sign(B), hence generally higher half moments E X^(j+1/2). Existing μ andν alone do not provide all of them. Do not claim all projected data free from integer moments.

For the polar occupation upper-bound interface, however, use Dhat approximating D=P_A^+−P0^+ and Chat=P0^-Dhat. Since P0^- is contractive,

 ||ChatY||1<=||DhatY||1,
 ||Chat(I−P)||1<=||Dhat(I−P)||1,
 ||Chat||1<=||Dhat||1.

Thus the conservative majorant/tail bounds may use unprojected Dhat factors and integer-moment Grams. This costs sharpness but avoids the extra projected half-moment supplier. The actual Fock chart and approximation error remain imported; dropping the projection in an upper bound does not identify the unprojected operator with the physical C.

## Cost and scope

At fixed N6, coefficient arithmetic is finite on at most22 directions per geometry, with exact integer moments through11 and no spectral solve. Combining this correction with the existing66-node rational bank requires new cross-Grams and matrix contraction, not a rerun of its original quadrature. This is a distinct source-only certificate method with no measured cost or execution authority. Parent/independent review and a prospective protocol must precede any actual moments/Gram/correction computation. The high-tail bound alone does not determine an alpha value, a useful weighted majorant, or success of the current trial space.

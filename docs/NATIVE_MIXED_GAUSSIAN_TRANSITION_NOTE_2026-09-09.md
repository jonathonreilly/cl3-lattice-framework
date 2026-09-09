---
claim_id: native_mixed_gaussian_transition
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
runner: scripts/native_mixed_gaussian_transition_2026_09_09.py
---
# Positive mixed Gaussian overlaps and certified transition arithmetic

For the supplied real infinite native model, normalized finite-imaginary-time impurity vacua in a single common reference CAR frame have strictly positive mixed overlap. For unit real Majorana combinations, their overlap-normalized two- and four-insertion transition ratios are uniformly bounded by199 and118803. This note also supplies efficient finite-matrix inverse/logarithm certificates, with explicit input and Hilbert–Schmidt tail obligations. It performs no native evolution, overlap, or alpha calculation.

The load-bearing physical import is the [uniform imaginary-time reference-chart theorem](NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md): real skew pairings at every finite time have norm<=99/100 and are trace class. The [finite-excitation Ward theorem](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md) supplies the common Fock realization and finite relative-energy interpretation. These are supplied-model premises, not selection of a new microscopic theory. The finite-matrix arithmetic below requires a separately certified approximation to those pairings; no shifted Gram ghost representation is presumed physical.

Conditional on the supplied real native reference frame and the linked uniform reference-chart theorem: each finite-time pairing Z_A(t) is real skew, trace class (HS suffices below), and ||Z_A(t)||<=r=99/100. Its normalized vector has the reference-positive convention

    |Z>=a(Z) exp(½ f† Z f†)|0>,
    a(Z)=det(I+Z*Z)^(-1/4)>0.

The same single reference CAR frame is mandatory for both impurities. Independent gauge changes of one state must be transported, not discarded. No actual native time evolution or numerical matrix is computed here.

## Nonzero overlap with fixed positive phase

Put W=Z_A Z_C and q=r²=9801/10000. W is trace class with norm<=q<1. The Fredholm logarithm log(I-W)=-sum_(n>=1)W^n/n converges in trace norm; each trace is real. Finite exterior-algebra Gaussian overlap gives

    O_AC=<Z_A|Z_C>
      =a(Z_A)a(Z_C) exp[½ Tr log(I-Z_A Z_C)] >0.       (1)

This is the positive square root of the Fredholm determinant, not an arbitrary numerical determinant branch. For finite matrices, scaling both pairings from zero never crosses a zero because ||W||<1; the real overlap starts at1. Finite-rank real compressions converge in HS, their products in trace norm, Gaussian vectors in Fock norm, and determinants continuously. Their positive logarithms converge to the finite real value in(1), proving strict positivity in infinite volume as well. Thus the uninserted mixed-vacuum phase obstruction is removed on this common disk. Majorana-inserted kernels can still vanish or have either sign/complex phase.

Let T_A=||Z_A||HS²,T_C=||Z_C||HS². A conservative explicit lower bound is

    log O_AC >= -(T_A+T_C)/4 -sqrt(T_A T_C)/(2(1-q)).

The anchor bound uses log(I+Z*Z)<=Z*Z; the mixed logarithm uses ||W||1<=sqrt(T_A T_C). No positive amplitude floor independent of these trace quantities follows from the disk alone. For example many copies of opposite2-mode pairings have an exponentially small positive overlap. Work in logarithms to avoid underflow. Positive unnormalized evolution scalars multiply(1) and must be tracked separately.

## Ordered CAR contractions: index convention is load bearing

Define every transition expectation as <Z_A|operator|Z_C>/O_AC, in the displayed operator order. Write

    A=(I-Z_C Z_A)^-1,
    <f_i f_j†>=A_ij,
    <f_i f_j>=F_ij,             F=-A Z_C,
    <f_i† f_j†>=B_ij,           B=Z_A A,
    <f_i† f_j>=C_ij,            C=-Z_A A Z_C.            (2)

The ket relation f_i|Z_C>=sum_j (Z_C)_ij f_j†|Z_C> and its bra adjoint, together with CAR, derive(2). In particular F and B are skew and A+C^T=I. The transpose/order in C must not be replaced by a guessed occupation matrix. A2-mode check gives <f1 f2>=-z_C/(1+z_A z_C), fixing the minus sign. Uniformly

    ||A||<=10000/199, ||F||,||B||<=r/(1-q), ||C||<=q/(1-q).

For L=u^T f+v^T f†, use bilinear coefficients (no implicit complex conjugation):

    D(L1,L2)=u1^T F u2+u1^T A v2+v1^T C u2+v1^T B v2.

The physical Majoranas are a_j=f_j+f_j† and b_j=i(f_j†-f_j). Thus b has(u,v)=(-i e_j,i e_j). Odd insertions have zero transition expectation. For four ordered insertions Wick's rule gives

    <L1 L2 L3 L4>=D12 D34-D13 D24+D14 D23.             (3)

This also holds with repeated insertions; CAR contact terms are already in A. It is a quasifree transition functional, not a positive state when A and C differ. Multiply(2)-(3) by the positive overlap and any supplied positive evolution norms for unnormalized Ward kernels. All explicit i factors and any extra native operator coefficient remain necessary.

## Stable finite series and computable tails

For V=Z_C Z_A, A_N=sum_(n=0)^N V^n satisfies

    ||A-A_N|| <= q^(N+1)/(1-q).

No eigenvalue decomposition or square-root branch tracking is needed. The log-determinant truncation afterN terms obeys

    |Tr log(I-W)+sum_(n=1)^N Tr W^n/n|
      <=||W||1 q^N/((N+1)(1-q)).

For the full normalized log overlap use

    log O =¼ sum Tr(Z_A²)^n/n +¼ sum Tr(Z_C²)^n/n
            -½ sum Tr(Z_A Z_C)^n/n.

A common truncation bound is [¼(T_A+T_C)+½sqrt(T_A T_C)]q^N/((N+1)(1-q)). These formulas are finite-rank implementable once a common pairing approximation and its HS error are certified; the disk alone supplies neither that approximation nor a cost guarantee. The inverse tail atN=2048 is less10^-15 by exact rational comparison, although performing2048 dense products is not claimed practical. Faster certified solves may replace this deliberately simple series.

## Input error rather than assumed floating-point stability

Let hat pairings be real skew with norms<1. The number q_* must bound BOTH the actual and approximate product norms; for example choose q_*=max(r²,||hat Z_A||||hat Z_C||)<1. Set e_A=||Z_A-hat Z_A||, e_C analogously. Then

    delta_V <= e_C||Z_A||+||hat Z_C||e_A,
    ||A-hat A|| <=delta_V/[(1-||Z_C||||Z_A||)(1-||hat Z_C||||hat Z_A||)].

Add the computed inverse residual or finite-series tail separately. For F, for example, error<=||A-hat A||||Z_C||+||hat A||e_C; B and C follow by the displayed two-/three-factor telescoping products. This is an actual absolute transition-kernel error bound, independent of how small O is.

For HS input errors E_A,E_C, let delta_W1<=E_A||Z_C||HS+||hat Z_A||HS E_C. Then

    |Delta log O| <=¼(||Z_A||HS+||hat Z_A||HS)E_A
                    +¼(||Z_C||HS+||hat Z_C||HS)E_C
                    +delta_W1/[2(1-q_*)].

The anchor terms use the positive-matrix log Lipschitz bound with inverse norm<=1; the mixed term uses the trace-log series/line integral on the operator-norm ball. This yields multiplicative overlap error exp(±bound). A sufficient implementation must bound HS tails as well as operator norms, and preserve/reconstruct the real-skew common frame.

For four insertions propagate the three products in(3): each product error is bounded by delta_Dij*|Dkl|+|hat Dij|*delta_Dkl, summed with absolute values. Combining O and an inserted scalar K uses |Delta(OK)|<=|Delta O||K|+|hat O||Delta K|. These estimates do not prove the sign of any inserted Ward sum or determine the unresolved alpha.

## Fixed-degree Majorana consequences

For a normalized real Majorana combination L=sum_j(x_j a_j+y_j b_j), ||x||²+||y||²=1, the annihilation/creation coefficient vectors u=x-iy and v=x+iy both have norm1. Therefore the four contraction-block bounds in the main derivation give

    |D(L1,L2)| <=(1+2r+r²)/(1-r²)=(1+r)/(1-r)=199.

The four-insertion Wick ratio is consequently at most3*199²=118803 in absolute value. Odd ratios vanish. These are uniform in volume and in the finite imaginary times for which the reviewed common-disk theorem holds. They bound only fixed-degree insertions normalized by the positive mixed overlap. They neither imply the inserted ratio is positive nor control arbitrary high-degree operators. They show that a small uninserted overlap does not by itself introduce an unbounded fixed-degree transition ratio; coefficient/operator approximation errors remain those in the main derivation.

These inequalities are immediate consequences of the proved norm estimates, not results of a new physical calculation.

## Efficient finite-matrix certificate

Let E=Z_C Z_A, ||E||<=q<1, M=I−E, and g=1−q. For the exact native disk q=9801/10000 and g=199/10000. For approximate finite inputs use a certified common qbar bounding their actual products; do not assume the exact disk automatically applies to approximate matrices. Then sigma_min(M)>=g and ||M||<=1+q. The positive mixed determinant branch is supplied by the independently proved real Gaussian overlap theorem.

## Eleven doubling steps

Set P_1=E and S_1=I. Given P_n=E^n and S_n=sum[k=0..n−1]E^k, compute

 S_2n=S_n+P_n S_n, P_2n=P_n P_n.

Eleven steps give2048 terms with22 matrix products, not2048 products. The last power product can be omitted if only the sum is wanted. In exact arithmetic ||P_n||<=q^n and ||S_n||<1/g, so no exact intermediate magnitude grows exponentially. The inverse tail is q^2048/g<10^-15. No normality or spectral-eigenvector assumption is used.

Floating or approximate products are candidates only. A fresh certified residual rho>=||I−M Shat|| gives

 ||M^-1−Shat||<=rho/g.

If the residual is computed for a matrix Mhat with certified ||M−Mhat||<=eta, use rho<=rhohat+eta||Shat||. Directed interval residual loops or an independently proved roundoff bound are required; a vendor multiplication result alone is not a certificate. This residual can replace lengthy forward propagation through all doubling products. Finite intermediate checks and a failed residual gate must stop the fixed attempt, not silently increase precision or iterations.

For optional forward enclosures, if power/sum errors at n are ep,es and new product/addition roundoff envelopes are dp,ds, then

 ep_next <=2 q^n ep+ep²+dp,
 es_next <=(1+q^n)es+ep(1/g+es)+ds.

These are sufficient, not claims that binary64 automatically meets a target. The fresh residual remains preferable. Transition F,B,C errors follow the previously reviewed two-/three-factor telescoping bounds.

## LU candidate and certified log determinant

Suppose a real LU candidate, including its row permutation Pi, defines the exact dyadic matrix B=Pi^-1 L U. Require finite stored entries and nonzero pivots. Unit diagonal L must actually be represented as unit, or its diagonal product must also be included. Build a certified residual bound eta>=||B−M|| with eta<g. Matrix-input error is included in eta, not omitted from the reconstruction residual.

Every M+t(B−M) is invertible because its least singular value is >=g−t eta. Its real determinant cannot change sign. Since det M>0, det B>0. The exact sign from permutation and diagonal factors must agree; a disagreement means the candidate/residual certificate failed. No numerical determinant square-root branch is selected.

The exact determinant differential gives

 |log det B−log det M| <=−N log(1−eta/g).             (1)

Indeed integrate |Tr[(M+tDelta)^−1 Delta]|<=N eta/(g−t eta). This works for nonsymmetric, nonnormal M. If a trace-norm residual tau>=||Delta||1 is available, the alternative bound tau/(g−eta) is valid. For eta/g<=1/2, the simple rational sufficient bound2N eta/g avoids evaluating the logarithm in(1). Thus a target delta_log may use eta<=g delta_log/(2N), with eta<=g/2. This is a dimension-dependent finite determinant bound, not a determinant continuity assertion based only on operator error in infinite dimension.

The computed scalar log det B also needs enclosure; summing unproved libm logarithms is insufficient. Each |Lii| or |Uii| is an exact positive dyadic. Write x=2^k y with1<=y<2 by integer comparisons. For z=(y−1)/(y+1),0<=z<1/3,

 log y=2 sum[j=0..m−1]z^(2j+1)/(2j+1)+R,
 0<=R<=2 z^(2m+1)/((2m+1)(1−z²)).

Use z=1/3 for log2. Combine all k into one signed integer before multiplying its log2 enclosure; then sum the remaining log y intervals outward. This certifies log|det B| directly without multiplying enormous/small pivots. The determinant sign is accounted for separately as above. Scalar interval widths and residual bound(1) are added.

## Normalized overlap and separate infinite-input error

The finite normalized log overlap is

 ell=½log det(I−Z_A Z_C)−¼log det(I+Z_A^T Z_A)−¼log det(I+Z_C^T Z_C).

Using I−Z_CZ_A instead gives the same determinant. Each anchor has least singular value>=1 and norm<=1+||Z||² (use the certified approximate pairing norm for approximate inputs), so the same backward-certificate method works with g=1 (or certified Cholesky plus its residual). Add half the mixed log error and one quarter of each anchor log error. Positive overlap follows from the theorem, not an amplitude floor. An ell interval yields multiplicative error exp(±delta); a separate outward scalar exponential is needed only when an amplitude is requested.

For true infinite pairings approximated by these finite matrices, first add the reviewed HS input bound with q_* controlling BOTH actual and approximate products. This is essential: finiteN LU error does not control omitted HS tails. Zero-padding a valid common finite CAR frame adds determinant1 and changes no state, while inventing numerical ghost modes is not justified. Relative gauges/frames and unnormalized evolution scalars remain separately bound.

## Prospective cost and outputs

Candidate inverse: at most22 doubling matrix products plus one fresh residual. Candidate log determinant: one real LU and one certified product residual per determinant, plus O(N) scalar log enclosures. These operation counts replace a2048-product narrative; no measured runtime or memory target is claimed. A later contract should save pairings/source hashes, qbar, inverse residual, exact pivot/permutation signs, LU residual, scalar log intervals and all HS/input allocations. No alpha or inserted-kernel sign conclusion follows.

## Supporting evidence and scope

The portable runner executes only the preserved synthetic2/4-mode literal Fock/CAR controls and exact2x2 doubling/log-tail controls. The716 Fock supporting predicates include one resource predicate; the16 fast predicates are exact rational controls. Wrong-sign comparisons are finite algebra discriminations, not mutated native physical solvers. No physical replay, determinant evaluation on native data, or timing forecast is included.

Original mathematical proofs, control receipts and source-bound independent reviews are preserved and pinned in the paired provenance directory. The assembled canonical proof includes only one clarification beyond those sources: approximate anchor upper norms use the actual certified approximate norm rather than silently inheriting r. Research protocol status is provenance, not a claim that a new computation ran. Formal audit status is not assigned by these supporting controls.

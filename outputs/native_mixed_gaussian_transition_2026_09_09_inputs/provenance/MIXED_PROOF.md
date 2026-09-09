# Positive mixed vacuum overlaps and CAR transition kernels

Conditional on the supplied real native reference frame and the reviewed Riccati disk theorem74531a24: each finite-time pairing Z_A(t) is real skew, trace class (HS suffices below), and ||Z_A(t)||<=r=99/100. Its normalized vector has the reference-positive convention

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

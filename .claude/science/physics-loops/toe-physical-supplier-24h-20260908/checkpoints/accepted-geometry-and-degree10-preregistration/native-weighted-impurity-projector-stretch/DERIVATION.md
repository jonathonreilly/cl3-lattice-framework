# Actual weighted impurity projector: constructive reduction

Research derivation, not an executed physical matrix certificate. The supplied infinite cubic pi-flux carrier, source conventions, and trace-class quadrature theorem are imported from `native-node-stable-imaginary-time-stretch/TRACE_CLASS_IMPURITY_PROJECTOR.md` and `LOW_RANK_PROJECTOR_CERTIFICATE.md`. All statements about numerical enclosures below require their stated residual bounds to be computed. No physical integral, projector, or state has been evaluated here.

## Native coefficient rather than an arbitrary coefficient ball

Let h0=iK and R(z)=(h0-z)^-1. For a selected pair of links set U=[e0,d], where d is the signed sum of their two neighbor vectors, of norm sqrt(2). The actual perturbation is UVU*, V=2ih J2, J2=[[0,1],[-1,0]]. Write A=E(X+s²)^-1, D=(1-s²A)/(6h²), and Bgeo=A for a perpendicular pair and D for an opposite pair. Then

    U*R(is)U = i [[sA,-2hD],[2hD,2sBgeo]].
    a=1-4h²D; ddet=a²+8h²s² A Bgeo >=1/9.
    T+=(I+V U*R(is)U)^-1 V
       = (2ih/ddet) [[-4hsBgeo,a],[-a,-2hsA]].

With X±=R(±is)U, the resolvent difference is -X+ T+ X-* and its adjoint. Consequently a positive ds quadrature weight w contributes to P_A,- minus P0 the actual coefficient

    [X+,X-] C [X+,X-]*,
    C=(w/(2pi)) [[0,T+],[T+*,0]].

The minus sign in the negative-band projector integral cancels the Woodbury minus sign. Bgeo is not the projected-Green scalar E sqrt(X)/(X+s²).

Balance each node: C=|C|^(1/2) J |C|^(1/2), ||J||<=1. The columns Y=[X+,X-]|C|^(1/2) now carry all physical weights. The two 2x2 blocks of |C| require only two successive positive square roots. For positive definite H, sqrt(H)=(H+sqrt(det H)I)/sqrt(tr H+2sqrt(det H)). Intervals must certify denominators and coefficient errors. For two impurities concatenate their columns before Gram construction; retaining separate coefficients preserves cross-impurity signs. A bound on ||Q||1 does not upper-bound Tr(Y*Y), since cancellations are possible.

## Symmetries and exact native representation

For chiral grading Sigma and a seed of chirality chi, Sigma R(z)e=-chi R(-z)e. Pole sums/differences are exact chiral vectors. Balancing preserves this decomposition because |C| commutes with the induced grading. Work in the real rephased convention Y=-iX with the corresponding coefficients. Append reference covariance partners:

    F=[Y,Gamma0 Y], M=F*F=[[G,J],[-J,G]],
    Jcol=[[0,-I],[I,0]], Gamma0 F=F Jcol,
    P0 F=F J0, J0=(I+iJcol)/2.

M commutes with Jcol and the induced chiral grading. For the embedded Hermitian coefficient Cbar, Q=F Cbar F*. Products require M, never its inverse. Exact null vectors cause no difficulty. A square-root coefficient-space model sqrt(M) Cbar sqrt(M) is isometric to the physical model on range(M). A numerical positive shift of M can create ghost couplings on ker(M); it must not silently be interpreted as a physical pure state.

## Conditioning-free actual rounding by contour

Suppose the exact candidate P=P0+F Cbar F* has ||P-P_A,-||<1/4. On |zeta-1|=1/2 the physical resolvent norm is at most4. Let r=(zeta-J0)^-1. Then the exact rounded projector satisfies

    Psharp-P0 = F K F*,
    K=(1/(2pi i)) integral r Cbar (I-M r Cbar)^-1 r dzeta.

Indeed this is the finite-rank resolvent identity, using (zeta-P0)^-1F=Fr. Moreover

    (I-M r Cbar)^-1 = I+F*(zeta-P)^-1 F Cbar,

so its norm is <=1+4 Tr(M)||Cbar||. This is independent of the smallest nonzero Gram eigenvalue. A finite contour rule with a certified inverse residual and integration remainder therefore encloses actual native coefficients. For any further columns W, the rounded projected Gram is W*P0W+(W*F)K(F*W). This still needs the additional mixed Green data for W. Symmetries are preserved by exact functional calculus; numerical symmetry projection must retain its error.

## Polynomial alternative, supplied by root and checked here

Set f(x)=3x²-2x³. If the spectrum of P lies within e<=1/4 of {0,1}, each iteration has error at most (7/2)e² relative to its exact spectral rounding. This includes negative eigenvalues and eigenvalues above1: |f(x)|<=3e²+2e³ near0, and f(1-x)=1-f(x). Hence

    e_n <= (2/7) (7/8)^(2^n).

All iterates have the same exact rounded projector and remain actual finite-rank corrections. If P=P0+F C F*, define

    D2=J0 C+C J0+C M C,
    D3=J0 D2+C J0+C M D2,
    Cnext=3 D2-2 D3.

These are exact multiplication identities, needing no inverse, pivot threshold, or ghost basis. The finite iterate is not itself a pure projector. Its operator-norm error to the pure limit is <=e_n; trace-norm error <=rank(F)e_n because the complement is unchanged. Input/coefficient arithmetic error must be propagated through each product, rather than assuming purification removes roundoff. PH/chiral complement symmetries survive f(1-x)=1-f(x). This provides a simpler prospective enclosure route than contour inversion, subject to actual coefficient growth.

## First full-strength schedule and honest next gate

The imported trace error is <=(357/25)2^-Jlo+2*2^-Jhi+429(4/25)^p. Choose p=6, Jlo=7,Jhi=4: 11 panels and66 nodes. Adding1/200 arithmetic budget still gives <1/4. Four balanced columns/node yield264 columns and528 after covariance closure, before exact symmetry reduction. This is a fixed actual lambda=1 candidate, not a weak-coupling surrogate. It needs A,A',Bgreen,Bgreen' at all66 pole brackets and coefficient intervals. The accepted s=1,2 data alone do not supply these.

The existing shared744 elliptic-A catalog can support multi-s B transforms, but current analytic quadrature widths may be too large for a528-dimensional weighted Gram. Certify that precision gate before constructing matrices. New pole brackets must be proved disjoint from catalog brackets to avoid unimplemented confluent A'' evaluations. No runtime claim follows from this dimension count. A meaningful first once pilot would assemble the actual weighted symmetric Gram and propagate one or more purification steps, reporting a rigorous error or a precision stall. Its physical execution remains unlaunched and requires a separately frozen input/source/resource contract.

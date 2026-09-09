# Polar-factor occupation bounds from an offdiagonal projector approximation

Independent check of the parent's new lemma; source-only, no native arrays. This improves the earlier supplier diagnosis: explicit approximation of sqrt(N) is sufficient but **not necessary**. The new nuclear-norm interface avoids any invalid absolute-value Lipschitz argument.

Let C be trace class, with polar decomposition C=UQ, Q=|C|>=0; U is a partial isometry and U*C=Q. For any bounded positive Y,

 0<=Tr(QY)=Tr(U*CY)<=||CY||1.

The trace equality is legitimate because C is trace class and Y,U are bounded. The inequality follows |Tr U*Z|<=||Z||1 and ||U||<=1. For any finite Chat with ||C−Chat||1<=ε,

 Tr(QY)<=||Chat Y||1+ε||Y||.                         (1)

For an orthogonal P, τ=Tr((I−P)Q) therefore satisfies

 τ<=||C(I−P)||1<=ε+||Chat(I−P)||1.                  (2)

If Chat(I−P)=0, this reduces toτ<=ε exactly. No commutation between P and Q is assumed. No continuity estimate for C→|C| in trace norm is used. TrQ<=||Chat||1+ε independently bounds the Fock mode-weight sum.

## Majorant objective

In the preconditioned frame S' with H=S'*S', let W'=W'* dominate the residual form L' and satisfy exact B'*W'+W'B'=0. The physical positive operator

 Y_W=S'H^-1W'H^-1S'*

has norm ||H^-1/2W'H^-1/2||<=||W'||/(1−e) when ||H−I||<=e<1. The weighted residual coefficient is exactlyρ²=Tr(QY_W). Hence

 ρ²<=||Chat Y_W||1+ε||W'||/(1−e).                  (3)

Together with (2) and M<=||Chat||1+ε, this supplies the prior state-weighted/Poisson/Fock error bound using certified finite matrices and one nuclear errorε. Using x²<=M is conservative and avoids recovering Tr(PQ) separately. Smaller x bounds may be substituted only with independent certification.

## Entirely finite factor formulas

Suppose Chat=F_L K F_R*, where F_L,F_R are actual finite physical column families (not shifted numerical Gram ghost modes). Define G_L=F_L*F_L, G_R=F_R*F_R, D=F_R*S' and H=S'*S'. Then

 Chat Y_W=F_L [K D H^-1 W'H^-1] S'*,
 Chat(I−P)=F_L K [(I−P)F_R]*,
 G_tail=G_R−D H^-1 D* >=0.

These are exact identities. Every nuclear norm on the right is a finite-factor norm. For A=F_L B F_Z*, its nonzero singular values are those of G_L^(1/2) B G_Z^(1/2). A conservative root-free sufficient bound is

 ||A||1 <= sqrt(rank_bound * Tr(B*G_L B G_Z)).       (4)

The trace is ||A||HS²; rank_bound may be min(number of left columns, number of right columns), and must be fixed explicitly. Another bound follows from any factor split B=B1 B2*: ||A||1<=||F_L B1||HS ||F_Z B2||HS. Finite certified PSD square roots/singular values can sharpen these estimates; (4) needs only Gram products and an outward scalar square root. Negative upper enclosures for positive traces are failures, not permission to clip silently. Thus (1)-(3) need no natural-mode computation and no infinite occupation-square-root approximation.

Right-support containment is not automatic. If the selected24 span does not contain the right factor, use G_tail and (4); do not discard it. Existing ordinary G/J cross-Grams may suffice for these factor formulas if they describe the exact F_L,F_R and S'. The full factor coefficients K and the certified nuclear approximation error remain mandatory numerical inputs.

## Native projector identification and physical chart

In the intended excitation convention C=P0^- P_A^+, Q=sqrt(P_A^+P0^-P_A^+) is the mode-weight operator for the reference vacuum in the impurity positive excitation space. This identification must retain the canonical convention and multiplicities used by the Fock consumer. If an actual finite operator Dhat approximates P_A^+−P0^+ in nuclear normε, then

 Chat=P0^- Dhat,
 ||C−Chat||1<=ε,

because P0^-P0^+=0. Left multiplication by the exact reference projection is contractive; its column Gram must be supplied in the same physical reference frame. This is a useful bridge to the previously proved low-rank projector quadrature, but its existence theorem alone is not computed factor data.

A full-space Galerkin approximation to exp(-t|h_A|) can be projected on the left/right by the exact P_A^+ to form a contraction on the impurity excitation Hilbert space. For positive-band initial columns, the added left projection cannot increase the full-space vector error. Actual projected columns and cross-impurity transport remain separate obligations. One must not feed an unprojected full-space map into impurity Fock second quantization without this identification.

## Disposition

The parent polar lemma is valid under its stated trace-class/positive-Y hypotheses. It materially reduces the missing supplier from an occupation-square-root matrix to a certified finite offdiagonal-projector approximation with actual Gram factors. It does not prove that current24 rows give a useful τ orρ, nor evaluate a kernel/alpha. The earlier explicit-Q route remains valid as a sufficient alternative; its necessity claim is superseded by this interface. Independent review of this extension and exact native factor availability are required before any new numerical protocol.

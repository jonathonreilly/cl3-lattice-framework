# Constructive finite majorants and weighted Gaussian input pullback

Provisional source-only continuation. Canonical8070 imaginary-time and8071 mixed-Gaussian notes were read completely; no physical arrays or saved stage data were read. Primary separately develops the Fock derivative consumer. This note supplies the finite certificate and an explicit trace-class input interface, conditional on that consumer's hypotheses.

## Exact commutation without certified eigenvectors

Let S be the selected frame, G=S*S>0, J=S*KS with K*=-K, D=(KS)*(KS), L=D+JG^-1J and B=G^-1J. For real coefficients a_j set

 q(B)=Σ_(j=0)^d a_j(-B²)^j,   W=G q(B).

Because B*G=-GB, every even power is G-self-adjoint and commutes with B. Thus W*=W and B*W+WB=0 identically for the actual G,J, including when they are known only by intervals. If W-L>=0 is certified, the weighted residual bound follows for all real times. Polynomial positivity is not separately required: W>=L>=0 supplies it. The constant polynomial always gives a feasible sufficiently large majorant, but not necessarily a useful objective. Optimizing coefficients against a specified input covariance is a new finite problem, not an achieved computation.

Use the already proposed exact triangular preconditioner T as a coordinate change, not an approximately orthonormal physical frame: S'=ST, H=T*GT, A=T*JT, Z=T*DT and L'=Z+A H^-1A. Set B'=H^-1A and W'=H q(B'). The same algebra is exact. All matrices are at most48 square. No requirement on narrow entries of a corrected isometry is imposed. An enclosure H± with ||H-I||<=e<1 supplies ||H^-1||<=1/(1-e). An exact candidate X0 with ||I-HX0||<=r yields ||H^-1-X0||<=r/(1-e). This permits outward matrix evaluation of W' and L' without an uncontrolled inverse. Polynomial expressions must be evaluated for the true interval matrices; a point polynomial in the midpoint alone need not commute with the actual generator.

To certify positivity, enclose W'-L' by a symmetric center Y plus spectral-radius errorδ. A sufficient exact Gershgorin test is

 min_i [Y_ii−Σ_(j≠i)|Y_ij|] >= δ.

Verified rational LDL/Cholesky residual bounds can replace this conservative test. If the certificate has no positive margin, interval failure is indeterminate, not a proof that no majorant exists. The same interval computation encloses Tr(W' C_weight). A candidate coefficient optimization may use ordinary arithmetic; only the final domination and weighted objective certificates carry meaning.

An alternative exactly spectrally resolved construction illustrates potential sharpness. For A=Σλ λPλ, set bλμ=||Pλ L Pμ|| and any positive tλ. Then W=Σλ wλPλ dominates L for

 wλ=bλλ+Σ_(μ≠λ)bλμ tμ/tλ.

Indeed each offdiagonal quadratic term is bounded by bλμ[(tμ/tλ)||vλ||²+(tλ/tμ)||vμ||²]. For input masses aλ=||PλX||HS², choosing tλ=√aλ when all are positive gives Tr(X*WX)=Σλ bλλaλ+2Σλ<μ bλμ√(aλaμ). Zero masses require a positive limiting regularization; no finite W with infinite coefficients is claimed. This construction is an exact theorem, not a recommendation to use uncertified nearly degenerate eigenvectors.

## Pullback of original raw input family

For specified physical Y=F_raw D_input, let C_y=S'*Y and G_y=Y*Y. The exact projection P=S'H^-1S'* gives projected coefficients c=H^-1 C_y. Then

 ||(I-P)Y||HS²=Tr(G_y−C_y*H^-1 C_y),
 ||P Y||HS²=Tr(C_y*H^-1 C_y),
 ρ_Y²=Tr(C_y*H^-1 W'H^-1 C_y).

The first is an initial projection error; it cannot be omitted just because the propagation estimate is state-weighted. It must be enclosed with cancellation-aware exact matrix arithmetic. A negative computed upper bound is contradictory data, not permission to clip to zero. Existing rawF source/Gram data may supply G_y,C_y for specified finite combinations, but the current selected Gram alone does not give all these cross terms. No new data are presumed available.

## Basis-free trace-class Gaussian input

Let Φ be the relevant normalized excitation state and N its one-particle occupation density. In a natural mode basis, ||a_iΦ||=sqrt(n_i). Suppose Q=N^(1/2) is trace class, M=TrQ<∞; the imported stationary Gaussian comparison supplies a bound of this type in the intended chart, subject to its exact mode convention. Primary's contraction interpolation inequality yields

 ||(Γ(T1)−Γ(T2))Φ|| <= Σ_i sqrt(n_i)||(T1−T2)e_i||
 <= sqrt(M) ||(T1−T2) Q^(1/2)||HS.

The second step is weighted Cauchy–Schwarz, and is independent of the chosen presentation of the natural modes. Q^(1/2)=N^(1/4) is HS. Infinite sums converge under the displayed trace assumption and contraction hypotheses. This does not assert that every Gaussian with finite particle number has trace-class sqrt(N); finite TrN alone is weaker.

Thus one need not individually compute every natural mode: a sufficient finite input is the matrix

 M_Q=S'* Q S', together with a certified scalar M=TrQ.

Projected coefficient covariance is C_weight=H^-1 M_Q H^-1. Its norm mass is x²=Tr(H^-1 M_Q), and omitted weighted input mass is

 τ=M−Tr(H^-1 M_Q)=||(I-P)Q^(1/2)||HS².

The all-time residual objective is ρ²=Tr(W'H^-1 M_Q H^-1). These quantities use only finite matrices plus one trace-tail certificate, once Q and its common physical chart are authenticated. No explicit natural-mode basis or entrywise corrected-frame coefficient certificate is needed.

For the positive contraction target exp(-t|H_full|), or an actually identified positive-band generator, define its Galerkin approximation on P and zero on P-perp. Decompose its one-body error acting on Q^(1/2) into the initial omitted component and projected-input propagation. Contractivity bounds the first by√τ. The second is bounded by the Poisson state-weighted expression E(t;x,ρ) from DERIVATION.md. Consequently the Fock consumer obeys the conditional bound

 sqrt(M) [sqrt(τ)+E(t;x,ρ)].

This formula requires the same one-body/Fock chart, the contractions and the actual positive-band identification assumed by the consumer. It cannot turn a reference-frame real-time model into the impurity positive-band semigroup by notation alone. Insertions add their own finite-column errors; unnormalized energy scalars, phase, stationary-vacuum approximation, pairing HS tails and mixed log-determinant conversion remain separate under8070/8071. The bound is useful only if certified M_Q and τ are small enough; a scalar bound M<43.5 alone cannot establish that.

## Precisely new missing supplier

The ordinary accepted Gram M=F*F is not the weighted Gram F*sqrt(N)F. These matrices are generally different even with identical frame geometry and uniform leakage summaries. A sufficient new supplier must certify M_Q and TrQ (or a finite low-rank approximation with a trace-norm error), in the correct impurity excitation chart. If ||Q−Qhat||1<=η, then |TrQ−TrQhat|<=η and ||S'*(Q−Qhat)S'||1<=||H||η. These explicit errors can be added to the finite pullback. A native stationary-projector/pairing construction may eventually supply Q; the current scalarA/B/cminus/mu catalog does not by itself constitute that certificate.

This isolates a genuine next consumer obligation: certified occupation-weighted cross-Gram and trace-tail data, rather than blindly enlarging the uniform leakage trial space. No assertion that the present24-mode frame succeeds, no new physical evaluation, and no alpha accuracy is claimed.

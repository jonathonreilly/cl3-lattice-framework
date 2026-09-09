# Common symmetry-preserving compression of weighted impurity columns

Source-only mathematical continuation. Import the reviewed common3-source396/792-column construction and the reviewed equivariant Gram dilation3c1bb/57ade. No native Gram, pivot, compression rank or physical insertion is evaluated. All residual tests below concern the actual weighted common carrier, not an arbitrary coefficient ball substituted for a physical impurity.

## Chiral splitting makes PAIRS sufficient

Let Gamma be the real reference complex structure, Gamma²=-I, and Sigma the real chiral involution, Sigma²=I, Sigma Gamma=-Gamma Sigma. The centered sources have chiralities chi=(+1,-1,-1). For real rephased balanced pole columns y_sigma=-i sqrt(alpha)R(i sigma s)w,

    Sigma y_+=-chi y_-, Sigma y_-=-chi y_+.

Thus v_eta=(y_+-eta*chi*y_-)/sqrt2 has chirality eta. This is an orthogonal change among the two pole signs. Apply its corresponding exact transformation to both physical coefficient matrices. Their norms remain<=1 and the weighted trace is unchanged. Particle-hole structure is the real representation with exactly imaginary skew coefficients; it needs no additional independent partner.

If a residual pivot x has Sigma x=eta x, then a=x/||x|| and b=Gamma a are orthonormal, have opposite chiralities, and span a space invariant under BOTH Gamma and Sigma. Every such pair projection therefore commutes with both. The finite basis convention is always b=Gamma a, fixing the covariance block[[0,-1],[1,0]] and chiral block diag(eta,-eta). The same sequence serves both impurities.

An arbitrary unsplit pivot generally does NOT have this property. Its invariant orbit is span{x,Gamma x,Sigma x,Gamma Sigma x}, of dimension at most4; these four vectors are not generally orthogonal. A safe implementation splits x into x_+=(I+Sigma)x/2 and x_-=(I-Sigma)x/2, performs one positive scalar paired pivot, then projects the other component and pivots its residual if nonzero. Each intermediate pair already preserves both symmetries. Therefore no4x4 inverse is needed. Blindly normalizing all four orbit vectors by one norm is wrong. Starting with the chiral pole combinations avoids this complication entirely.

The factor1/sqrt2 can be enclosed by a scalar exact-root interval. Alternatively use the unnormalized half-combinations as pivot candidates while tracking residuals on the original weighted columns. Then only rational half-combinations enter the pivot row; the residual certificate still uses the ORIGINAL factor trace and not a silently rescaled trace.

## Paired residual arithmetic and a streaming algorithm

For residual columns Y after earlier invariant projection, let G=Y^T Y,J=Y^T Gamma Y. At pivot i, r=Gii>0,g=G_i,: and j=J_i,:. The exact update is

    Gnew=G-(g^T g+j^T j)/r,
    Jnew=J-(g^T j-j^T g)/r.

The new finite-coordinate rows against the ORIGINAL columns are g/sqrt(r), -j/sqrt(r). The minus sign in the second row follows from (Gamma a)^T=-a^T Gamma. Store these rows or their unnormalized g,j,r form. The finite impurity matrices are U C_A U^T and U C_C U^T in the ONE common basis U, with the same reference and chiral blocks. There is no inverse of the full Gram.

A source-only efficient design need not rewrite the full396x396 residual matrix after every pivot. Store the immutable indexed upper-triangle input and the earlier g_l,j_l,r_l. Reconstruct only a requested pivot row by

    Gij=G0ij-sum_l(g_li g_lj+j_li j_lj)/r_l,
    Jij=J0ij-sum_l(g_li j_lj-j_li g_lj)/r_l.

Maintain all diagonal residual intervals in O(n) work per pair and store O(kn) interval numbers after k pairs. Pivot-row reconstruction costs O(kn), so a full k-pair selection costs O(k²n), apart from input indexing. A final residual triangle, if requested, is a separate O(kn²) output pass; it is unnecessary for the trace stop certificate. This is an operation count, not a measured runtime/memory promise.

With interval inputs, choose the maximal certified positive lower diagonal, deterministic label tie-break. Require r_lower>0 before division. If no such pivot exists before the targets pass, report PRECISION_STALL; do not clip an uncertain pivot positive. Exact chiral zeros (G between opposite chiralities and J between equal chiralities), selected-row zeros and skew diagonals may be imposed only because the invariant projection proves them. A negative upper residual diagonal contradicts the imported PSD enclosure and must fail. Complete pivot/stage/trace/error history must survive failures. No adaptive precision increase is included in this source-only design.

## One residual certifies BOTH actual weighted impurity operators

Write Q_s=Y C_s Y^T, s=A,C, with the actual embedded coefficients ||C_s||<=1. For an invariant projection Pi put T=Tr(Y^T Y) and r=||(I-Pi)Y||HS². Expanding the difference and applying HS-times-HS Schatten bounds gives simultaneously

    ||Q_s-Pi Q_s Pi||1 <=2 sqrt(T r).

For the reviewed common carrier T<529/2. Thus a separate compression target epsilon_comp is guaranteed by r<=epsilon_comp²/1058. As an illustrative prospective allocation epsilon_comp=1/1000 requires r<=1/1058000000. This is a new compression allocation, not already covered by the input arithmetic budget. A tiny rank is not guaranteed: interval conditioning or slowly decreasing residuals may force a stall/full rank.

The residual uses the raw weighted columns. Because Pi commutes with Gamma, the covariance-closed residual is exactly2r; do not mix raw and closed trace constants and lose a factor. Different coefficient signs or the five orbit multiplicities do not change this simultaneous bound. Actual quadrature, input arithmetic, coefficient approximation and later spectral-rounding errors are still added separately. Pure-state/parity conclusions require the appropriate rounded gap-preserving path; a real PH/chiral frame alone does not force even parity.

## Joint Gamma/Sigma extension of the reviewed dilation

The imported dilation extends the polar partial isometry of a singular Gram equivariantly under Gamma. Here it can preserve Sigma too. On the coefficient space use J0²=-I and S0²=I with S0 J0=-J0 S0, and assume F intertwines both. Its Gram commutes with both, so ker M and its complement reduce both. In each kernel representation, choose an orthonormal S0=+1 basis and its J0 partners. In the actual native complement choose the same number of Sigma=+1 vectors and their Gamma partners. Both chiral sectors of that complement are infinite after removing a finite-dimensional invariant range. This extends the polar map to ONE isometry V intertwining BOTH structures.

Before shifting an approximate Gram, twirl it over the four conjugations by I,J0,S0,J0 S0. Since the exact Gram is fixed by these conjugations, the certified operator error cannot increase. The twirled matrix commutes exactly with both. Adding epsilon I then yields the reviewed positive dilation Ftilde=V sqrt(Mplus), with ||Ftilde-F||HS<=sqrt(2n epsilon). This is a legitimate common native approximation, uniform over the allowed extension choice. It is not an assertion that the shifted Gram equals the physical Gram.

Run the symmetric compression on this common dilated carrier only with its own certified residual and trace. Both embedded operators then incur the dilation error plus2sqrt(Ttilde rtilde), and any coefficient error. The same V must also carry any bound inserted vectors. Chiral spectral rounding preserves Sigma P Sigma=I-P when the exact coefficient structure and gap criterion hold. Generator leakage and time errors remain separate: the selected span is not asserted to be h_A- or h_C-invariant.

## Insertions must be included or quantitatively represented

For a required real vector w, either prove w=F a for a known coefficient a, or append sqrt(omega)w and its Gamma partner to the common data with all cross Grams certified. If w is not chiral, first split it and include both components. A bare local source is not automatically in a finite resolvent span just because the resolvents were seeded there.

For exact columns, the appended residual diagonal gives ||(I-Pi)w||<=sqrt(r_w/omega). For a dilated representation, add sqrt(2epsilon)||a||; when w is an appended column this is sqrt(2epsilon/omega). The two errors cannot be discarded by identifying a coordinate with an unbound physical insertion. Multiple insertions can have separate residual targets; the operator residual may still track only the original weighted Y block.

A useful concrete exception needs no new scalar: append the central e0 to the per-orbit3-source carrier. Its cross full/projected resolvent entries use the center row of the existing7-source formulas; O has zero center row, so the otherwise constant mu term vanishes. Its self norm is1 and e0^T Gamma e0=0. Therefore A/B66 suffices also for this central insertion pair, enlarging raw/closed dimensions to397/794. Its additional error ledger must nevertheless be checked. For general bare neighbor insertions, mu terms need not cancel in single-resolvent cross data; do not claim their support from the stationary divided-difference catalog alone.

In the fixed-six-source universal representative carrier there is also an exact center relation at any pole: e0=sigma*s*(-iR_sigma e0)-sum_a(-iR_sigma d_oa) in h=1 units. After scalar balancing this supplies a known coefficient vector for e0. The per-orbit3-source carrier generally lacks all three d_oa and may not use this relation. No analogous unproved finite relation for every bare neighbor is assumed.

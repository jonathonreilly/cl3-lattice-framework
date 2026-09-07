# Independent adapted-tree reproduction of the first actual ground correction

This calculation was preregistered and executed before reading native's correction coefficients. It uses a different adapted spanning tree and independently expands the22 ordered face words. The exact agreement is a nontrivial gauge-coordinate control, not a repeated evaluation of the same source.

## Distinct adapted gauge and local fields

The tree is [0,20,1,4,23,5,31,30,29,27,26,19,18,11,9] in the frozen lex-vertex/axis edge enumeration. It contains three edges of each source square, omitting the x edge at y1 rather than native's y edge at x0. Reverse-edge greedy extension completes the tree. Both source loops are literal chord variables up to inverse signs; the two ground functions and source Haar terms are invariant under inversion and conjugation. Changing the adapted tree can align color frames differently, but it does not change these actual central source integrals.

Let H=B^TWB and use Tr(TaTb)=delta_ab. Expanding the actual Wilson action gives E2=z^THz/6 per color, E3 and E4 from ordered matrix products, not commuting holonomies. The partition covariance is G0=3H^-1. The normalized limiting ground function is proportional to exp[-omega TrX²/2], omega=sqrt55/90. Its two source factors add omega times the source-coordinate projector to the precision, giving Gg=(H/3+omega Psource)^-1. Exact inversion and the unchanged2-source covariance are checked independently.

## Independent color and word calculation

Using explicit trace-orthonormal Gell-Mann matrices, define F_abc=ImTr(TaTbTc). The matrix calculation gives sumF²=12. It also gives the three fourth trace contractions64/3,-8/3,64/3. Consequently

    E Tr(Xe Xf Xg Xh)
      =(64/3)(Gef Ggh+Geh Gfg)−(8/3)Geg Gfh.

For each face, enumerate every degree-four composition among its ordered exponential factors. Its coefficient is minus the face weight divided by3, multiplied by orientation signs and inverse exponential factorials. These are kept per face and per ordered word. The middle Wick contraction is negative and cannot be dropped as an Abelian simplification.

Every ordered three-distinct-factor choice contributes -weight/3 times its sign to F(Xe,Xf,Xg). Sorting the edge triple contributes the corresponding alternating parity. Repeated-factor cubic real traces vanish. If q_I are these coefficients, then

    E E3² =12 sum_(I,J) q_I q_J det G[I,J].

Within-triple Wick contractions vanish against F. The six cross-pairings give the determinant with their alternating signs. All cross-face terms are retained; the raw22-by22 face-pair matrix is part of result.json. This convention is independently related to native's f' by F=f'/2, so12 corresponds to48/4 rather than a conflicting color normalization.

## Haar and kernel normalization

The local Haar Jacobian satisfies

    log(j(X)/j0)=−sum_(positive roots) alpha(X)²/12+O(|X|4)
               =−TrX²/4+O(|X|4).

For a traceless diagonal X, sum_(i<j)(lambda_i−lambda_j)²=3sum_i lambda_i², establishing the coefficient. Since ETrXe²=8Gee, the product Haar insertion is−2TrG. The source-kernel local unitary contributes reciprocal square roots of its two source Haar densities; their second-order insertion is +(TrXu²+TrXv²)/8, whose expectation is Guu+Gvv. Omitting it would compute a different, non-unitarily normalized matrix element.

Thus, with R=E3²/2−E4,

    Z1=E_G0 R−2TrG0,
    Ng1=E_Gg R−2TrGg+Gg_uu+Gg_vv,
    k0=Ng1−Z1.

The ground Gaussian integral is normalized when taking these expectations: its leading factor cancels against the actual Gaussian ground eigenvalue. In the one-group control, G=3 gives E E4=−5 and Haar=−6, hence Z1=−1. This control independently fixes both action and Haar conventions.

## Analytic interface, including the missing-resolvent issue

The separately reviewed two-source cancellation theorem makes the WHOLE first epsilon kernel coefficient vanish, not just its ground expectation. This matters: otherwise a second-order eigenvalue correction could contain a first-order-kernel resolvent contribution even when the first ground expectation vanishes.

With epsilon=beta^-1/2, the Hessian-integral Taylor representation of E(epsilon z)/epsilon² can be differentiated three times on a small star-shaped chart. Bounded fifth action derivatives and third cutoff/Haar derivatives give a fixed polynomial times Gaussian bound for the third epsilon derivative. Taylor expansion through epsilon² is therefore valid in weighted marginal L2 with remainder O(epsilon³); compact complements are exponentially negligible. Dividing by the partition and source square-root densities preserves this expansion. It yields K_beta=K0+beta^-1 K2+o(beta^-1) in operator norm as well as Hilbert-Schmidt norm.

The ground is simple and isolated, so its eigenvalue correction is the Rayleigh insertion <phi,K2phi>, with no first-order-kernel term. The same exponentially small off-chart estimate transfers this coefficient to the actual finite supplied group operator. Therefore

    beta^-4 ell0(A_beta)=lambda0[1+k0/beta+o(beta^-1)].

This is a coordinate-dilated statement; no fixed-group operator expansion or finite-beta onset is implied.

## Frozen result and distinct-tree agreement

The independent results are

    Z1=1444313/38720,
    Ng1=1012365/23276+(27961081/27931200)sqrt55,
    k0=126839623/20482880+(27961081/27931200)sqrt55 >0.

Both rational coefficients of k0 are positive. The result is not inferred from a numerical eigenvalue fit.

Our partition components are

    E E3²=4401207/3520,
    E E4=24786923/77440,
    Haar=−29457/110.

Native's different tree instead gives1439937/880,19686973/38720,−1362/5 respectively. These DIFFER individually, while their normalized sum agrees exactly. Ground bulk and source-half correction likewise combine to the identical coefficient. This is expected: coordinate-dependent Taylor pieces need not be gauge invariant separately, but the actual normalized central integral is.

The independent source and raw receipt were frozen before reading native's result. All matrices, per-face quartics, cross-face cubic covariance, mutations and full exact field values remain in result.json. Dropping cross-face covariance, the middle noncommuting quartic pairing, Haar or the active source half-density has a recorded nonzero effect. The partition source-half term is correctly inactive, not counted as a failed mutation. No physical coupling, thermodynamic result, ratio correction or numerical accuracy atbeta6 is claimed.

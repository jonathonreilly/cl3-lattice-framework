# Gaussian differential derivation, before coefficient computation

Let G(a,b)=(H/3+2aP_u+2bP_v)^(-1) be the per-color covariance and let Gamma(a,b) denote the unnormalized136-dimensional Gaussian integral. Eight independent colors give Gamma proportional to det(G)^4. Differentiating precision inverse yields G_a=-2G P_u G, G_b=-2G P_v G, and G_ab=4(G P_u G P_v G+G P_v G P_u G). Thus L_a=partial_a logGamma=-8G_uu, L_b=-8G_vv and L_ab=16G_uv². The factors8 and16 reflect all eight colors, not rank-two Cartan dimension.

The first nonconstant invariant oscillator polynomial is 4-omega Q in eight dimensions. For phi0 proportional to exp(-omega Q/2), its squared norm relative to phi0 is Var(omega Q)=4, while its mean is zero. Multiplication by that polynomial in the source integral is exactly 4+omega partial_a. Hence d=(D Gamma)/Gamma is

  d=16+4omega(L_a+L_b)+omega²(L_a L_b+L_ab).

For the Mehler kernel exp[-A(QX+QY)+B<X,Y>], A=8/135,B=23/270, omega=sqrt(4A²-B²)=sqrt55/90 and theta=B/(2A+omega)=23/(32+3sqrt55). Its degree-two eigenvalue ratio is theta², so the independent check is d=4theta², not4theta or theta².

The scalar Wick numerator correction at arbitrary(a,b) is

  K=E_G[E3²]/2-E_G[E4]-2 sum_e G_ee+G_uu+G_vv.

Each full normalized Haar density has quadratic coefficient -Tr(X²)/4 in Tr(TaTb)=delta convention, whose Gaussian expectation is -2G_ee. The dilated operator integrates sqrt(j) at each source instead of j, giving back G_uu+G_vv. This source half-density term is essential and is included before differentiation. Partition normalization Z1 is independent of a,b.

Leibniz differentiation gives

  k1-k0 = ((4omega+omega² L_b)K_a
           +(4omega+omega² L_a)K_b+omega² K_ab)/d.

Thus neither Gamma's absolute normalization nor j0 nor Z1 needs evaluation to compute the first/top relative correction. k0=K-Z1 and k1=k0+(k1-k0) remain conditional coefficient candidates until a common operator expansion and isolated invariant branches are justified. A potential trace-free degree2 oscillator state is not invariant under SU3 conjugation; the radial mode is the sole invariant degree2 polynomial. No noninvariant first-excited degeneracy is silently imported.

Shared input declaration: native check.py supplies the validated ordered-word construction and color contractions tr4=(64/3)(G_abG_cd+G_adG_bc)-(8/3)G_acG_bd and f-pair contraction48det(G_IJ). The computation below reconstructs the graph independently with integer bit vertices and a frozen supplied adapted tree; it verifies the derivative algebra and small covariance controls independently. The shared tensors are not called an independent SU3 tensor derivation. No native result JSON or ground coefficient was read before this calculation.

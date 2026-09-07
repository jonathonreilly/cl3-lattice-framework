# Cold review of uniform reflected heat correction

PASS for the frozen orbital DERIVATION.md and certificate.py. This is an independent recalculation, not a rerun of that certificate. The exact parent six-image identity, shifts and L convention were read in the parent source earlier in this lane and match the formulas here.

The scaled full-walk Fourier integral has measure h^-2 canceled by dk=h²dz. Its quartic correction is t a²/(36beta), and L² has symbol a²/9, so the coefficient is exactly(t h²/4)L². The sixth-order cosine and low-cutoff estimates are the same independently reviewed identities as the refined Wilson proof, now with the factors t retained. Low damping23t/72 and both powers of t in the remainder are correct. The radial Fourier prefactor1/(2pi sqrt3)<1/10 is safe. Its integrated bound scales t^-3 and is maximal at t=1/2.

Independently computed low=449888256/160908575<14/5. The exact high tail uses exp(-a/48), not exp(-a/24), to cover the full time interval. Its beta² coefficient is decreasing beyond beta192, hence certainly beyond2048. A45-term positive exponential lower sum suffices for exp(64/3)>10^9. The endpoint rational bound is196608/9765625<21/1000.

The Gaussian tail expression is correct: integrating a²exp(-a/6) from beta/2 yields the bracket7/6+beta/144+2/beta after including the leading term. Polynomial powers are at most beta³, so monotonicity holds beyond36. Replacing exp(beta/12) by the smaller exp32 is conservative at the endpoint; a60-term positive sum proves exp32>10^12. The rational bound141833/3662109375<1/1000 follows. These calculations use different Taylor truncation lengths from the author's80. Gaussian integration outside the torus is included. Low plus both tails is strictly below3.

The exact killed kernel and continuum Dirichlet heat use the same six Weyl images with shifted endpoints h(p+rho). Weyl invariance preserves the diffusion differential operator, including its square, so each correction transforms consistently. Triangle inequality gives18 without a boundary-relative estimate. This is uniform for all labels and t in[1/2,1]. No missing rho shift or alternant factor belongs in this ordinary heat calculation.

The weighted HS scaling is correct: a scaled-kernel error18h4 means an actual matrix-entry error18h6. Squaring/summing two weighted indices gives18h4 times the two quadrature L² norms. This requires BOTH weights and does not imply an unweighted operator bound.

For W, xy(x+y)<=x³+y³ and Q>=x²+y² yield the stated separable envelope. The monotone Gaussian right sum is below sqrt(pi)/2<1. The x³Gaussian total variation is2maxf<2, so its right sum is at most1/2+2h<=1 for h<=1/4. Their product bounds h²sumW strictly below1. Hence the actual two-sided sqrtW remainder is<18h4. No hidden continuum integral is substituted for a lattice sum.

The explicit warning about O(h) cell projection is necessary and correct. The lemma alone supplies neither a second-order embedded operator expansion nor a spectral coefficient; combined with the separately proved sampled-eigenvector quadrature lemma it supplies the missing heat input.

Reviewed DERIVATION.md SHA 80d5a3f5c01256b002b00c1947d81aa857b449e11ef4d8a8b3e7e0b7b86dceec.

Reviewed certificate.py SHA 7f695357c9ccdd939c85fe289e18ab5e76d399294d90c25062fc25acce0c5719.

Reviewed certificate.json SHA 4a2611414ff87a2cfd156b75448910c840e3f6dfa35aa51bfdacec1b7c979430.

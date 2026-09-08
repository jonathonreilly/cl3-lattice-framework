# Endpoint residual identities and the finite-projection source quotient

Root supplied the candidate identities before this independent derivation. Fix a finite real symmetric Hamiltonian H, a positive integer m, n=2m, and G=I-H/M with entrywise nonnegative entries. Assume Z=1^T G^(2m)1>0, and use the normalized path law proportional to product G(x_i,x_(i+1)), with uniform trial amplitudes at both ends. Here “positive” need not mean that every eigenvalue of G is positive. Let psi=G^m1, h=H1, and brackets denote psi-normalized Hilbert expectations. No stochastic stationarity is presumed for an unburned finite chain.

## Endpoint and midpoint identities

Symmetry and HG=GH give

E_path[h(x0)]=h^T G^(2m)1/Z=<H>,
E_path[h(x0)h(xn)]=h^T G^(2m)h/Z=<H²>.

Thus the cross-endpoint product, not the square of an endpoint value or square of their average, measures <H²>. For any real diagonal X, summing each half path around its midpoint gives

E_path[X(xm)h(x0)]=(G^m h)^T X(G^m1)/Z=<H X>=<X H>.

The last equality is for the expectation in this real psi and real symmetric H,X; it is not an operator commutation assertion. The same result holds with the right endpoint. Accordingly, with e=(h(x0)+h(xn))/2 and E=<H>,

Cov_path(X(xm),e)=<(X-<X>)(H-E)>.

For H=V Nf-A on the actual symmetric geometric-face graph, A1=Nf including move multiplicity, so h=(V-1)Nf. This is the existing endpoint readout, but the new product/cross statistics were not stored by the running production and cannot be reconstructed from separate batch means without extra assumptions.

## Complex diagonal source family

Let O_alpha be any finite collection of complex diagonal source operators and X=sum_alpha |O_alpha|². Put S=<X>>0. The nonnegative kinetic Dirichlet quadratic form is

D_num=(1/(2Z)) sum_xy A_xy psi_x psi_y sum_alpha |O_alpha(y)-O_alpha(x)|².

For H=V Nf-A, direct expansion, symmetry A_xy=A_yx, and real psi yield exactly

sum_alpha <O_alpha psi,(H-E)O_alpha psi>/Z
 = D_num + <XH>-E S.

For a complex source the off-diagonal imaginary terms cancel between x,y; equivalently one may sum its real and imaginary Hermitian components. This is why no imaginary coherence term has been omitted. The identity does not assume O commutes with H, nor that psi is an eigenstate.

For the actual six pooled transverse sources at one harmonic, the literal flip identity is sum_alpha |Delta O_alpha|²=2 qhat²/L³ on every allowed geometric face. It must be checked with the actual Fourier normalization; it is not true for an arbitrary single orientation. Then D_num=qhat²<A>/L³ and <A>=V<Nf>-E. Hence

R_E := sum_alpha <O_alpha psi,(H-E)O_alpha psi>/(Z S)
 = D + Cov_path(X(xm),e)/S,
D=qhat²(V<Nf>-E)/(L³ S).

The correction has a plus sign. Omitting it generally replaces the actual source Rayleigh quotient by the Dirichlet quotient. At exact ground projection it vanishes, but it need not vanish at finite m. R_E is a spectral Rayleigh average relative to E, not necessarily nonnegative: H-E can have negative spectrum. Relative to the unknown ground energy E0, the corresponding quotient is R_E+(E-E0). This additive offset cannot be removed by terminology. A supported-gap inference additionally needs the correct ground state/source orthogonality and spectral conditions; no pole claim follows.

## Residual bound

Because <(H-E)>=0, the sharper Cauchy–Schwarz estimate is

|Cov_path(X,e)|=|<(X-S)(H-E)>|
 <= sqrt(Var_psi(X)) sqrt(Var_psi(H)).

Therefore |R_E-D|<=sqrt(Var_psi(X) Var_psi(H))/S. The weaker root candidate follows by Var(X)<=<X²>. Endpoint cross product supplies Var(H)=E_path[h_left h_right]-E²; midpoint samples supply Var(X)=<X²>-S². The variance of the classical endpoint-average random variable is generally different from Var_psi(H), and must not be substituted silently. Numerical subtraction can lose precision near zero residual; direct oracle residual norms are useful for checking that cancellation, but stochastic estimates remain noisy.

A small energy variance alone is not a general certified ground-state error bound. It establishes proximity to some spectral energy only with additional quantitative information; finite-G convergence, spectral separation and ground overlap must not be inferred from the new readouts alone. All identities are conditional on the symmetric real finite H, uniform endpoint trials, correctly sampled finite path measure and the specified source family. No new physical Hamiltonian, formation law, or current-production observable is supplied by this calculation.

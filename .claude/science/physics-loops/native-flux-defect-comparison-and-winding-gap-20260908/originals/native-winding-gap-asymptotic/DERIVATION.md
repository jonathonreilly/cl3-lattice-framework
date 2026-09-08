# Winding twists preclude a volume-uniform full wrong-flux gap

Consider uniform cubic L×L×L tori, even L≥4, fixed nonzero t. Use the exact canonical-seam dispersion already derived in native-zero-penalty-pi-dispersion/DERIVATION.md. For winding twist alpha in{0,1/2}³ its physical fixed-flux ground energy is

E_L(alpha) = -|t| sum_(n in{0,...,L-1}³) f(2pi(n+alpha)/L),

f(k)=sqrt(sin²k0+sin²k1+sin²k2).

The canonical minimizing orbit has alpha*=(1/2,1/2,1/2). Set alpha'=(0,1/2,1/2): this changes one winding and no elementary plaquette flux, hence is a different orbit. No zero active mode is introduced because two directions remain antiperiodic. The independently reviewed strictness theorem gives E_L(alpha')−E_L(alpha*)>0 for every finite L. We now bound this difference above without computing it.

## Uniform Fourier decay

With period2pi define fhat(q)=(2pi)^−3 integral f(k)e^(−iq·k)dk. There is a constant C independent of integer q such that |fhat(q)|≤C(1+|q|)^−4.

Proof: f is smooth except at the eight points with all coordinates0 orpi. Near each such point, its positive quadratic leading form is Euclidean norm squared. Consequently on a dyadic annulus of radius r, derivatives of order j of f are bounded by C_j r^(1−j). Choose a smooth annular partition with the usual derivative scaling; the localized function has derivative L1 bounds C_j r^(4−j). Its Fourier coefficient is therefore bounded by C r^4 min(1,(|q|r)^−5), integrating five times along a largest coordinate of q for the second bound. Sum annuli r≤|q|^−1 directly: their r^4 sum is O(|q|^−4). For larger r the bound is C|q|^−5 r^−1, whose dyadic sum is O(|q|^−4), dominated by the smallest such radius. The smooth remainder decays faster. A finite sum over the eight singularities proves the bound. This avoids the logarithmic loss that a naive global fourth-derivative L1 estimate would produce.

Since power4 exceeds dimension3, the Fourier series is absolutely convergent. Thus termwise finite grid summation is valid and gives exactly

sum_n f(2pi(n+alpha)/L) = L³ sum_(m in Z³) fhat(Lm) exp(2pi i m·alpha).

The m=0 bulk term cancels between twists. Therefore

|E_L(alpha')−E_L(alpha*)| ≤ 2C |t| L^−1 sum_(m≠0)|m|^−4 = C' |t|/L.

C' is finite and independent of L; no explicit numerical value is asserted. This is an upper bound, not an asymptotic equality or a computed Casimir coefficient.

## Precise consequence

Let Delta_flux(L) be the minimum ground-energy difference from the canonical orbit to ANY wrong native flux orbit. The exhibited winding sector proves

0 < Delta_flux(L) ≤ E_L(alpha')−E_L(alpha*) ≤ C'|t|/L.

Thus the strictly positive finite-volume wrong-flux separation cannot have a positive volume-independent lower bound along cubic even tori. This does not contradict finite all-even flux uniqueness or the enumerated L6 prefix bounds. Those prefixes are local electric toggles, whereas a winding twist changes a noncontractible flux class. The argument proves neither a positive local plaquette-defect cost nor its absence. It also supplies no nonzero-U phase, finite-penalty radius, full excitation dispersion, or mixing statement.

The only spectral input is the exact finite dispersion in the specified eight pi-plaquette winding sectors; the strict positive lower side imports the separately reviewed finite strictness theorem. No numerical production or new spectrum computation was performed. Extension to uniformly bounded aspect-ratio rectangular sequences follows by the same anisotropic grid estimate, but the stated conclusion is deliberately restricted to cubic L.

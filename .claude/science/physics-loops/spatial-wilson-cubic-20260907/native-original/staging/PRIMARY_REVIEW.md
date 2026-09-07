# Cold review: cubic cancellation and actual kernel rate

Verdict: PASS for DERIVATION.md SHA5df246ae7f02fd119567f0f63eb3ce142975b29a72f49eb7893de2a3bbe4fbee. I checked the color algebra, conditional Gaussian contractions, differentiated cutoff bounds, normalization and operator transfer independently. The original structural Hilbert-Schmidt theorem is unchanged. No numerical engine or pipeline was run.

## Cubic action and conditional mean

For Hermitian A,B,C, Tr(A^3) and Tr(A^2 B) are real, including cyclic reorderings. Their cubic exponential coefficients are imaginary, so they make no real-action cubic term. For three distinct factors, Re(-i Tr ABC)=Im Tr ABC=Tr(A[B,C])/(2i). This is the fully alternating invariant tensor, with no symmetric d tensor. Inverse edge factors only introduce real signs. The adapted spanning-tree coordinates are essential: the sources are literal chords, so no nonlinear source-coordinate substitution contributes an extra cubic term.

The leading covariance is H^-1 tensor the color identity. Conditioning on two complete source vectors therefore leaves means A_e X+B_e Y and nuisance covariance C_ef delta_ab. In the conditional third moment, the three-mean contraction with f is zero because its three vectors lie in a two-dimensional span. Each mean-times-covariance term contracts two indices of f with delta and is zero separately. This proves the conditional cancellation pointwise in X,Y, not merely after source integration or angular averaging. It would not justify the same claim for three independent source vectors. The unconditional linear term also vanishes by centered Gaussian oddness.

## Differentiation on expanding coordinates

The potentially dangerous issue is that z can be of order1/epsilon on the cutoff support. The claimed estimate nevertheless holds: write

    E(epsilon z)/epsilon²
      = integral_0^1 (1-t) D²E(t epsilon z)[z,z] dt.

One and two epsilon derivatives bring bounded third/fourth derivatives of E and respectively three/four factors of z. This gives the stated C|z|³ and C|z|4 bounds without inverse epsilon divergences. Choose the nested coordinate neighborhoods as sufficiently small star-shaped product balls, so every intermediate t epsilon z remains in the chart where the quadratic lower bound holds. This is always available in the structural proof's exponential chart and should stay explicit in a canonical port.

Differentiating the exponential twice gives the square of the first derivative and the second derivative, hence at most polynomial factors of degrees6 and4 multiplying exp(-c|z|²). Derivatives of the smooth compactly supported cutoff and of Haar density contribute only further fixed polynomial factors. The cutoff derivatives are supported strictly inside the outer chart; extending the product byzero is smooth. Thus the uniform second-derivative Gaussian dominator is valid even on its annulus. At epsilon0, the first derivative is precisely -j0^17 E3 exp(-Q2), since both cutoff and Haar first derivatives vanish there.

Taylor remainder integration over120 nuisance coordinates preserves a polynomial Gaussian envelope in the16 source coordinates. The pointwise conditional cancellation removes the whole linear coefficient. The partition's nonzero constant term and zero linear term imply an O(epsilon²) normalization correction. This is enough for the weighted L1/L2 error, not an inference from weak convergence.

## Cutoff tails and kernel denominator

The excluded group-coordinate region is separated from the unique minimum. Its normalized fiber contribution has at most a fixed polynomial in beta multiplying exp(-gap beta). On the expanding source chart, |X|²+|Y|²<=2delta²beta allows this term to be bounded by a weaker source Gaussian. An additional beta^-1 prefactor can also be extracted by absorbing another polynomial into the remaining exponential. Outside the source chart the actual kernel is exponentially small in Hilbert-Schmidt norm; the limiting Gaussian's tail is likewise exponentially small. This justifies an O(beta^-1) common-space kernel estimate rather than merely an O(1) dominating envelope.

Haar inversion makes j even, so on a fixed small chart

    sqrt(j(epsilon X)j(epsilon Y))=j0+O(epsilon²(|X|²+|Y|²)).

It is uniformly bounded away from zero there. The reciprocal difference has the same weighted order. Multiplying by the marginal density and its Gaussian envelope therefore introduces no hidden O(epsilon) term. Independent conjugation averaging is an L2 contraction preserving the radial envelope. The claimed actual central-operator Hilbert-Schmidt O(beta^-1) rate follows.

## Spectral scope

The fixed isolated nonzero eigenvalues of the rescaled compact positive operators differ by O(beta^-1) in absolute value. The Gaussian ground eigenvalue is strictly positive, so dividing the first two fixed branches yields theta²+O(beta^-1). This is an implicit-constant asymptotic statement. It supplies neither a first correction coefficient nor its sign, and no finite-beta onset or beta6 accuracy. The next coefficient would indeed require E3²/2-E4, quadratic Haar density, normalization and the relevant spectral perturbation calculation. No correction to the proof is requested.

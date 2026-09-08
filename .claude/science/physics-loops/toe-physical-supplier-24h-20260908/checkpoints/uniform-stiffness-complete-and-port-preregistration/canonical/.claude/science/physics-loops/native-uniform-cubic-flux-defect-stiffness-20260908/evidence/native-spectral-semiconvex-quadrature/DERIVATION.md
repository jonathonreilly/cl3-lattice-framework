# Uniform quadrature bounds without spectral smoothness

Status: conditional-support candidate, independent analytical review pending. This is a proof candidate for the supplied period-four Bloch matrices, not a completed density certificate. No new physical spectral evaluation is executed by this packet.

## Minimal premises

The six frozen unit-hopping64-site Hermitian Laurent matrices have16 disjoint wrapped edges in each coordinate. Their second coordinate derivative is supported on those edges and is a direct sum of16 two-by-two matrices with eigenvalues±1. Consequently its nuclear norm is exactly32. The auxiliary energy density is minus the normalized zone integral of f=Tr|h| divided by128. The native physical hopping normalization is restored separately. No nonzero band gap, differentiable eigenvectors, or absence of band crossings is assumed.

## Semiconvexity of the trace norm

Fix two momentum coordinates and write H(t) for the remaining Hermitian matrix. The nuclear norm is convex and1-Lipschitz in its own norm. Taylor's integral remainder gives

||[H(t+s)+H(t−s)]/2−H(t)||_* ≤ 16s².

Indeed the second derivative has nuclear norm32 uniformly and each one-sided remainder has norm at most16s². Convexity then gives

[f(t+s)+f(t−s)]/2 ≥ ||[H(t+s)+H(t−s)]/2||_* ≥ f(t)−16s².

Therefore f(t)+16t² is midpoint convex and continuous, hence convex on the real line. Thus f is semiconvex with constant C=32. This argument permits zero eigenvalues and cusps. For g=f/128 the constant is1/4.

## One-dimensional periodic quadrature

Let g be a continuous2π-periodic function with g(t)+(C/2)t² convex, and use n uniformly spaced samples with arbitrary shift. Put Δ=2π/n and Q_n the sample mean, I the normalized integral.

On a cell centered at c, a subgradient of g(t)+(C/2)t² at c supplies

g(t)≥g(c)+p(t−c)−(C/2)(t−c)².

Integrating over that cell cancels the linear term. Summing centered cells yields

I g−Q_n g≥−CΔ²/24.

On a cell[a,b] whose endpoints are consecutive sample points, convexity of the corrected function gives

g(t)≤[(b−t)g(a)+(t−a)g(b)]/Δ+(C/2)(t−a)(b−t).

Integrating and summing over a period makes the composite trapezoidal sample mean exactly Q_n. Hence

I g−Q_n g≤CΔ²/12.

Both bounds hold for every shift, with no differentiability requirement. The two decompositions use the same periodic sample mean.

## Three-dimensional product grid and energy differences

Each coordinate integration or finite averaging preserves the same semiconvex constant in each remaining coordinate. A telescoping difference between the three-dimensional integral and product-grid mean therefore adds the three one-dimensional errors. For g=f/128 and grid counts(n1,n2,n3),

−(π²/24)Σ_a n_a^−2 ≤ I g−Q g ≤ (π²/12)Σ_a n_a^−2.

For auxiliary energy e=−g the signs reverse. Comparing two such energy densities, possibly with different grid shifts but the same counts, gives

|[I e_q−I e_pi]−[Q e_q−Q e_pi]| ≤ (π²/8)Σ_a n_a^−2.

On a cubic n³ grid this is3π²/(8n²), about0.003615 at n32. A looser boundπ²/(2n²) is also safe. Arithmetic error in the sampled trace norms must be added separately; no floating eigensolver stability theorem is silently assumed.

## Consequence if the five density certificates succeed

Suppose a later verified calculation proves each of the five noncanonical infinite-volume auxiliary density differences at least d0>0. The same shift-uniform bound controls finite cubic M³ momentum grids, including all eight winding twists and the canonical twist. For all M with3π²/(8M²)≤d0/2, every finite comparison density is at least d0/2. The finite collection of smaller cubic M has strictly positive comparisons by the separately proved finite flux-isolation theorem. Their minimum is positive, so a volume-uniform positive local-defect coefficient exists for all cubic L=4M. This does not supply its explicit value unless the finite collection is quantified, and does not extend to all aspect ratios with unbounded other sides while one side stays small.

This potential conclusion is conditional on the five as-yet unproved density bounds. It is compatible with the closing pure-winding gap because winding sectors have zero elementary defect count. It concerns the supplied zero-electric-penalty Hamiltonian and is not a nonzero-penalty phase theorem or Hamiltonian-selection result.

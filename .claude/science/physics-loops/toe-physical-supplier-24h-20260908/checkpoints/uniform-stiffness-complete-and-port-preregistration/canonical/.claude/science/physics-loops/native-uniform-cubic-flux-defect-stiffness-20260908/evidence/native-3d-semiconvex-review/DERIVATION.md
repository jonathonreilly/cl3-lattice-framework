# Independent semiconvex quadrature derivation

The candidate route and constants were exposed by root before this derivation. This independently checks the argument, including nonsmoothness and the product rule. No numerical run, eigenvalue evaluation or quadrature was performed. The actual64-cell Laurent matrices and density normalization are those previously reviewed.

## Uniform semiconvexity of the trace norm

Hold two momentum coordinates fixed and write H(t)=H_rest+exp(it)B+exp(-it)B†, where B is the positive wrapped-edge matrix in one direction. The boundary bonds form16 disjoint two-vertex pairs. Hence H''(t)=-(exp(it)B+exp(-it)B†) has32 singular values equal to1 and all other singular values zero: its nuclear norm is32, uniformly in t and the fixed other coordinates.

For any base point t choose a nuclear-norm supporting functional U there: ||U||_op<=1 and Re Tr U†H(t)=||H(t)||_*. Such a functional exists in finite dimensions even when H(t) has zero eigenvalues. Taylor's integral remainder and the uniform nuclear-norm bound give

||H(t+s)||_* >= ||H(t)||_* + s Re Tr U†H'(t) - 16s².

Equivalently f(t)=||H(t)||_* is32-semiconvex: f(t)+16t² is convex on every real interval. One may alternatively prove its midpoint inequality directly from convexity of the norm and the exact boundary second difference. Continuity then promotes midpoint convexity to convexity. No differentiability of f, no isolated bands and no nonzero spectral gap are required. Positive cusps from eigenvalue zero crossings are compatible with this lower-curvature bound.

For g=f/128, which is minus the unit auxiliary energy integrand, the semiconvex constant is C=1/4. The bound is uniform in the other coordinates and the cube label.

## Periodic one-dimensional quadrature

Let F be continuous, period P, and C-semiconvex, with grid t_j=t0+j Delta, Delta=P/n. Write Q=n^{-1}sum_j F(t_j), I=P^{-1}integral over one period.

On the centered cell around t_j, convexity of F(t)+Ct²/2 supplies a supporting line. Removing the quadratic gives F(t_j+s)>=F(t_j)+a_j s-(C/2)s². Integrating s from-Delta/2 toDelta/2 cancels the possibly nonsmooth supporting slope. Summing the cells yields

I-Q >= -C Delta²/24.

For the interval[t_j,t_{j+1}], the chord inequality for that same convex function gives

F(t_j+s) <= (1-s/Delta)F(t_j)+(s/Delta)F(t_{j+1}) +(C/2)s(Delta-s).

Integrating and using periodicity to equate the sum of endpoint trapezoids to Q yields

I-Q <= C Delta²/12.

The centered cells and endpoint cells are different partitions of the same periodic integral; they need not coincide. This is the key reason both one-sided bounds apply to the SAME grid Q. The argument holds for any grid offset, including midpoint sampling, and for functions with cusps. It does not insert a two-sided bound on F''.

For g, P=2pi, C=1/4, therefore

-pi²/(24 n²) <= I-Q <= pi²/(12 n²).

## Product rule and density differences

Expand the difference between the normalized three-dimensional integral and the product grid as a telescoping sum replacing one coordinate integration by its grid average at a time. Positive normalized averages preserve the coordinatewise inequalities and their uniform constants. For equal grid size n in each axis,

-pi²/(8n²) <= integral(g)-grid(g) <= pi²/(4n²).

For e_aux=-integral(g), this reverses to

-pi²/(4n²) <= e_aux-e_aux,grid <= pi²/(8n²).

Consequently the root's symmetric per-density bound pi²/(4n²) and two-density bound pi²/(2n²) are valid. Keeping the asymmetric interval gives the slightly sharper symmetric two-density difference bound3pi²/(8n²). No reliance on cancellation or correlated errors is needed. For unequal grids replace3/n² by sum_a1/n_a² in the derivation.

The trace-norm variation is priced at the actual unit hopping. Restoring hopping magnitude rescales every constant linearly. Applying the native objective half-factor also halves the error. The cube defect denominator8/m rescales a certified density-cost interval as stated in the dissemination theorem; it must not be silently omitted.

## Disposition and remaining arithmetic

The proposed O(n^-2) analytic quadrature certificate is sound under the declared64-cell Laurent construction. It remains valid at the canonical zero corner and any other band crossings. It can replace the much looser Lipschitz O(n^-1) estimate without a high-order smoothness assumption.

This proves only the integration error from exact grid values. A separate outward certificate for each computed trace absolute value or for their summed error is still necessary. Binary64 eigvalsh values and internal residual checks alone are not supplied by this theorem. It also does not itself establish positive density costs, a finite-size bound uniform over seam twists, a defect theorem beyond the supplied premises, or a phase claim. The proof was completed without reading the pilot spectra.

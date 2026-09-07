---
claim_id: gauge_wilson_cube_slab_simultaneous_anisotropic_source_semigroup_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/gauge_wilson_cube_slab_anisotropic_uniform_limit_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_cube_slab_anisotropic_central_oscillator_bounded_theorem_note_2026-09-07
  - gauge_wilson_cube_slab_two_source_cubic_cancellation_rate_bounded_theorem_note_2026-09-07
  - gauge_wilson_cube_slab_nonlinear_saddle_dilated_kernel_bounded_theorem_note_2026-09-07
claim_scope: "Uniform polynomial anisotropy estimate and explicit simultaneous sequence for repeated compressed source operators; no uncompressed multilayer composition or selected physical time."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

For the exact supplied compressed central source operator, kappa_n=4n²/(5t²) and beta_n=n^108 give a simultaneous norm limit exp(-tN) after n normalized steps and the specified oscillator dilation. The proof bounds one-step error by C kappa^52/beta. Constants and onset are finite but unspecified; this is not numerical accuracy at a chosen coupling.

This source imports [the anisotropic geometry/oscillator interface](GAUGE_WILSON_CUBE_SLAB_ANISOTROPIC_CENTRAL_OSCILLATOR_BOUNDED_THEOREM_NOTE_2026-09-07.md), [the nonlinear dilated kernel theorem](GAUGE_WILSON_CUBE_SLAB_NONLINEAR_SADDLE_DILATED_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-07.md), and [the whole two-source cubic cancellation theorem](GAUGE_WILSON_CUBE_SLAB_TWO_SOURCE_CUBIC_CANCELLATION_RATE_BOUNDED_THEOREM_NOTE_2026-09-07.md). It does not import the first spectral-correction coefficient theorem. Repeated compression remains an additional supplied composition contract.

Root independently froze a coarser kappa^98/beta, beta_n=n^200 proof before reading the sharper proof. Both originals and their timing records are preserved. The exact normalized-Gaussian identity in section3 below gives the sharper exponent52 without changing the model. Primary independently reviewed both bounds. These are corroborating derivations, not separately counted physical experiments.

# Polynomial simultaneous limit for repeated compressed cube source operators

This is a separate extension under the prospective contract in PREREGISTRATION.md. It preserves the frozen iterated-limit proof. The composition object is A_beta,kappa=D_beta,kappa/D00, the exact compressed bare central source operator. Taking its powers is an ADDITIONAL composition contract: in general(I* T I)^n is not I* T^n I. No longer microscopic slab, autonomous time evolution or environment-free physical composition is inferred.

All constants below are finite and depend only on the fixed cube, chosen fixed charts and SU(3) coordinate conventions, unless a subscript t is displayed. They are independent of beta and kappa>=1. No explicit numerical value of these constants or finite-beta accuracy is asserted.

## 1. Uniform geometry and Gaussian partition

Write E_k=E_spatial+k E_temporal. Both deficits are nonnegative, so E_k>=E_1 for k>=1. Use once and for all the nested star-shaped product-ball charts from the k=1 proof. They have

    E_k(w)>=c|w|² on the chart,
    E_k>=g>0 on its compact excluded complement.

Derivatives of E_k of each fixed order through four are bounded by C k on these fixed charts. The unique minimum and literal two-source coordinates are unchanged. The same product Haar density J is independent of k.

Let Q_k(z)=sum_color z_color^T H_k z_color/6. Its full136-dimensional unnormalized Gaussian integral is

    Z0(k)=j0^17(2pi)^68 det(H_k/3)^-4.

The exact determinant obeys

    k^12 <= det H_k <= (55/2) k^12,  k>=1,

by bounding separately(k+1)^2,(2k+3),(4k²+6k+1) in the exact formula. Hence

    c0 k^-48 <= Z0(k) <= C0 k^-48.

This polynomial loss is retained explicitly.

## 2. Uniform unnormalized Taylor estimates

Put epsilon=beta^-1/2 and use a fixed smooth cutoff chi supported inside the larger chart, equal to one on the smaller one. Define

    F_k,epsilon(z)=chi(epsilon z) exp[-E_k(epsilon z)/epsilon²] J(epsilon z).

The Hessian-integral representation makes the divided action smooth at epsilon0. Its first and second epsilon derivatives are bounded by Ck|z|³ and Ck|z|4. The uniform quadratic lower bound controls every intermediate epsilon value on the star-shaped support. Product differentiation therefore gives

    |partial_epsilon² F_k,epsilon(z)|
       <= C k² P(|z|) exp(-c|z|²)

for a fixed polynomial P and all k>=1. Cutoff and Haar derivatives add only lower polynomial terms. Haar has no linear term. The first derivative is -j0^17 E3,k exp(-Q_k). Conditional Gaussian integration over the120 nuisance coordinates annihilates this term identically for each pair of retained source vectors, by the reviewed alternating-tensor/two-source argument. The unconditioned first derivative also integrates to zero.

Let n_beta,k(x,y) denote the full unnormalized scaled marginal, and n0,k its Gaussian counterpart. Thus integral n0,k=Z0(k) and n0,k=Z0(k) g_k, with g_k the normalized16-dimensional source Gaussian. Let Ztilde_beta,k=beta^68 Zphysical_beta,k. Taylor's theorem, integrating the polynomial Gaussian, yields for the cutoff pieces

    ||n_beta,k-n0,k||_L2 <= C k²/beta,
    |Ztilde_beta,k-Z0(k)| <= C k²/beta.

The estimates are uniform even though the true Gaussian narrows in some directions, because the fixed E1 lower bound was used only to dominate the remainder.

For completeness, the omitted compact pieces contribute at most C beta^60 exp(-g beta) pointwise to n on the scaled source chart. Its volume is O(beta^8), hence its L2 contribution is at most C beta^64 exp(-g beta). The full scaled partition tail is at most C beta^68 exp(-g beta). These are bounded by C/beta for beta>=1, with a finite constant independent of k, and can be included above. No probability-tail bound is substituted for an L2 bound.

The Gaussian mass outside the expanding source chart is exponentially small uniformly in its covariance's largest eigenvalue. Its amplitude can grow polynomially in k, as tracked next; adding this tail does not alter the final exponent.

## 3. Normalize without losing the Gaussian factor twice

For beta>=C k^50 the preceding partition estimate and Z0>=c k^-48 imply

    Ztilde_beta,k>=Z0(k)/2.

The source covariance has eigenvalues sigma_plus=30 and sigma_minus=6(4k+5)/(4k²+6k+1), each repeated8times. For k>=1, c/k<=sigma_minus<=C/k. Exact Gaussian integration gives

    ||g_k||_L2 <= C k².

The same bound holds with any fixed polynomial weight in |x|+|y|: under the normalized squared Gaussian, covariance eigenvalues are bounded above uniformly, so all fixed moments are uniformly bounded. This identity avoids replacing the leading unnormalized marginal by a crude k-independent upper bound and then paying a second entire k^48 denominator loss.

Writing p_beta,k=n_beta,k/Ztilde_beta,k, the exact normalization identity is

    p_beta,k-g_k=(n_beta,k-n0,k)/Ztilde_beta,k
                    +g_k (Z0(k)-Ztilde_beta,k)/Ztilde_beta,k.

The first L2 term is bounded by C k^50/beta. The second is bounded by C k² k^50/beta. Hence

    ||p_beta,k-g_k||_L2 <= C k^52/beta,
    beta>=C k^50.

The same calculation permits the fixed polynomial weights needed for the source Jacobian. Gaussian truncation tails have bound C k^4 polynomial(beta) exp(-c beta), using its explicit density and uniform smallest precision; this is also absorbed by C k^52/beta. All such bounds are on the same fixed source charts, independent of k.

## 4. Source half densities, off-chart operator and normalization

The beta^-4 Haar-unitarily dilated kernel is the central average of p_beta,k divided by sqrt(j(x/sqrt(beta))j(y/sqrt(beta))). On the fixed chart these densities are bounded above and below by positive constants. Haar evenness gives

    |1/sqrt(j_x j_y)-1/j0| <= C (|x|²+|y|²)/beta.

Multiplying the normalized Gaussian costs at most C k²/beta in L2. Angular averaging contracts L2. Thus the chart kernel differs from K_k by at most C k^52/beta in Hilbert-Schmidt norm.

If either source lies outside the fixed chart, the compact gap gives the original source density bound

    k_beta,k(U,V)<= C beta^68 k^48 exp(-g beta)

after the partition lower bound. Consequently the beta^-4-scaled off-chart operator has Hilbert-Schmidt norm at most C beta^64 k^48 exp(-g beta), absorbed by C k^52/beta. This controls the full source operator rather than only its chart compression.

The limiting Gaussian leading eigenvalue is

    lambda0(k)=16sqrt(3)pi/(sqrt(sigma_plus)+sqrt(sigma_minus))^8.

It has a uniform strictly positive lower bound for k>=1 because sigma_plus=30 and sigma_minus is positive and bounded above. Hence, after increasing the fixed constant and requiring beta>=C k^52, the scaled actual operator norm is bounded below by half this constant. Normalizing by the ACTUAL norm therefore preserves the estimate:

    ||D_omega U_beta P [A_beta,k/||A_beta,k||] P U_beta* D_omega*
                  - exp(-t_k N)|| <= C k^52/beta.

Here N=(-Delta+|w|²-8)/2 on Ad-invariants, t_k=2 artanh(sqrt(sigma_minus/sigma_plus)), and D_omega is the k-dependent oscillator unitary. Its norm is one, so it introduces no hidden anisotropy loss. The normalized full-operator off-chart error obeys the same bound. Both the actual normalized operator and its compression are contractions.

## 5. Explicit simultaneous sequence

Fix t>0. For all sufficiently large n set

    k_n=4n²/(5t²),     beta_n=n^108.

The threshold beta_n>=C k_n^52 is eventually satisfied, since its right side is C_t n^104. Contractive telescoping controls n repeated steps by

    n C k_n^52/beta_n <= C_t n^-3.

It also bounds the difference between the true normalized source-operator power and the repeated chart compression, using the off-chart operator estimate. Thus no projection error is silently reset to zero.

Moreover t_k=2/sqrt(5k)+O(k^-3/2), so n t_k_n=t+O_t(n^-2). The spectral estimate

    ||exp(-aN)-exp(-tN)|| <= |a-t|/[e min(a,t)]

then bounds the limiting Gaussian-power difference by O_t(n^-2). Combining gives actual simultaneous convergence in operator norm, with error O_t(n^-2), on the common Ad-invariant oscillator space. More explicitly the compared operator is

    D_omega_n U_beta_n P
      [A_beta_n,k_n/||A_beta_n,k_n||]^n
      P U_beta_n* D_omega_n*.

It tends to exp(-tN). The displayed exponent108 is a deliberately crude sufficient choice, not an optimal scale or finite-resource proposal. Constants and the eventual onset depend on the fixed model and t; no numerical onset or beta6 accuracy is asserted.

## Limits of the conclusion

This closes a quantitative simultaneous sequence for powers of the supplied compressed source operator. It does not identify those powers with a longer uncompressed Wilson slab, select physical time or anisotropy, establish locality of the limiting oscillator clock, or provide a practical simulation cost. The underlying operator, gauge/source embedding and composition contract remain explicit imports.

## Claim-local finite interface and scope

The [exact helper](../scripts/gauge_wilson_cube_slab_anisotropic_uniform_limit_2026_09_07.py) performs23actual checks: the original14geometry/OU assertions, eight separately prospective scalar-bound checks and one positive resource guard. Its five reporting groups are per_element0, per_site2, per_mode6, per_block6, lattice_wide9; zero means no element-level check is claimed. Raw fixed geometry, covariance and source data agree exactly with the frozen14check result. No runtime input files are read; mathematical imports are source dependencies, not fabricated file dependencies.

N5 per_element: no individual-element dynamical simulation or finite-beta accuracy is certified.
N5 per_site: the fixed16vertex32edge22face geometry is supplied, not a thermodynamic limit.
N5 per_mode: covariance and invariant oscillator modes concern the central source space.
N5 per_block: repeated compressed-source powers are an additional composition contract, not a longer microscopic slab.
N5 lattice_wide: polynomial sequence108 has unspecified constants/onset and selects no physical time or coupling.

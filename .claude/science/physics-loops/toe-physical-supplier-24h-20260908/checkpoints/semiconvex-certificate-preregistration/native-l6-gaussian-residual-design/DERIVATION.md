# L6 Gaussian residual-DP route: exact formulas and a bounded feasibility gate

Outcome: a concrete alternative to five-dimensional word-by-word quadrature is available, with an exact residual certificate and Pfaffians of order at most80. Its low-rank sufficiency and runtime are NOT established. No physical coefficient, Gaussian profile, or integration was run. The next permitted work is source review of this design; any physical cost test needs a separate frozen authorization.

## 1. Exact source scope and what is still missing

Read the complete native-l6-active-krylov/DERIVATION.md, native-l6-sixth-factorization/DERIVATION.md, native-l6-gaussian-sixth-route/DERIVATION.md, and native-l6-allprefix-post-review/REVIEW.md. The exact spaces have dimensions68,76,80 for the six pair representatives001,003,012,023,122,223, hence34,38,40 active complex modes. Dense parity vectors are impossible within the intended resources. Every prefix quadratic preserves its support's W and has an unchanged bath in its vacuum. The bath energy cancels against the same part of E0; it must not be dropped inconsistently.

The completed1534-mask certificate provides positive gaps for the ADJACENT five bridge families, with minimum greater than0.3449 in the source units. It does not provide certified gaps for the other five pair representatives. Those require a new exact proper-prefix census and gap ledger. Singleton-star prefixes must use the fixed-initial-parity excitation gap, not the unrestricted vacuum energy. The mixed middle sectors in the factorization source must remain: retaining only star-cut middle sectors is invalid.

The earlier Gaussian route proves an ordered, sign-safe Laplace/Pfaffian kernel, but its naive M*n^5 evaluation count is not practical. The present route removes the quadrature from the CERTIFICATE by certifying residuals of arbitrary trial vectors. It does not assume that a resolvent maps a Gaussian to another Gaussian.

## 2. A small exact coefficient field, without normalized eigenvectors

Use the frozen integer paired basis (r_j,K0 r_j), with K0²r_j=-lambda_j r_j and d_j=r_j dot r_j. Here lambda_j is12,24,36,48. Define

    b_j = [gamma(r_j)-i gamma(K0 r_j)/sqrt(lambda_j)]/2.

Then {b_i,b_j†}=d_i delta_ij, and the canonical vacuum is annihilated by every b_j. In this convention

    H0,W = sum_j sqrt(lambda_j) [b_j† b_j/d_j -1/2].

This sign follows from the stored real-skew block [[0,-sqrt(lambda)],[sqrt(lambda),0]], not from a chosen vacuum label. Each endpoint Majorana is exactly

    gamma(e_v)=sum_j { r_j[v](b_j+b_j†)/d_j
              + i (K0r_j)[v](b_j-b_j†)/(sqrt(lambda_j)d_j) }.

Thus every changed-edge quadratic and H0,W has coefficients in Q(i,sqrt(2),sqrt(3)); no square roots of the large integer norms d_j are needed. The number field has fixed degree eight over Q. It is not an exponentially growing algebraic extension. The basis and its exact endpoint-containment certificate are required inputs.

Set c_j†=b_j†/d_j. These are convenient non-normalized creation coordinates: {b_i,c_j†}=delta_ij, while their Hilbert Gram metric is g_j=1/d_j. All trial states below have even parity and share the exact canonical vacuum, so the fixed initial parity and the unchanged bath are explicit.

## 3. Branch-free Gaussian dictionary and overlaps

For any skew matrix Z of complex rational entries define the UNNORMALIZED trial state

    |Z> = exp[ (1/2)sum_ij Z_ij c_i† c_j† ] |0>.

There is no requirement that Z be the exact output of a physical imaginary-time evolution. A floating Gaussian proposal can be rounded to rational Z and then treated as a new exact trial vector. Its approximation quality is measured by the final residual; no unverified matrix-exponential accuracy enters that certificate.

Let G=diag(g_j) and s_m=(-1)^(m(m+1)/2), where m<=40. Direct expansion in occupied subsets gives

    <Z|W> = sum_even I conjugate(Pf Z_I) Pf W_I product_(i in I) g_i
           = s_m Pf [ -conjugate(Z)   -I
                        I             G W G ].          (1)

The minus on conjugate(Z), the overall s_m, and the fixed creation order are essential. This formula follows by selecting whole matching pairs in the block Pfaffian, or by comparing the displayed subset expansion. It uses a2m-by-2m matrix, at most80, not the1082-by-1082 ordered-product matrix of the earlier route. It has no determinant square root or branch continuation. The states need not be normalized or mutually orthogonal.

Matrix elements of a quadratic B and B² between dictionary states are obtained from the same overlap polynomial and its first and mixed second derivatives. For example, differentiation in W_ij inserts c_i†c_j† on the right. An annihilator b_i satisfies

    b_i|W> = sum_j W_ij c_j†|W>,
    b_j b_i|W> = W_ij|W> - sum_kl W_ik W_jl c_k†c_l†|W>.

Use these identities to normal order each quadratic action. Left derivatives are the Hermitian adjoints with the metric factors retained. This supplies <Z|B|W> and <Z|B²|W> as finite Pfaffian minors, including zero-overlap cases. An inverse-transition-covariance shortcut is allowed only when its denominator is bounded away from zero; the polynomial/minor definition remains the reference at singular overlap. Arbitrary phases of Gaussian vectors are not discarded: their vacuum coefficient is fixed to1 in this chart.

All entries are in the fixed field Q(i,sqrt(2),sqrt(3)) if Z is Gaussian-rational. Exact field arithmetic or outward interval evaluation of this algebraic expression can certify the result. Ordinary floating Pfaffians, unbounded cancellation, or an overlap square root alone are not certificates. A different chart is possible for nearly orthogonal vacua, but must carry an explicit reference state and phase; it is not silently substituted here.

## 4. Sum ordered words by prefix DP before any inverse

Use the exact input word family, not a fitted subset. For adjacent pairs retain all five bridge families from the source census, their proper-key multiplicities and closing signs. For nonadjacent representatives the twelve boundary edges are distinct. Pair insertions at each center give15 perfect matchings per star and720 interleavings, hence162000 ordered words per representative. A subset recurrence can sum them without enumerating each ordered integral: each star's used subset has even cardinality, giving32²=1024 prefix states including endpoints. The precise physical mask-to-state mapping and possible proper gauge cuts must still be checked against the actual graph before use.

In the fixed gauge coordinates of the earlier Gaussian chain, each insertion contributes1/2 and each proper inverse is negative. Let x_0=|0>, and for a proper key F put

    s_F = (1/2)sum_(G -> F) x_G,
    x_F = - B_F^(-1) s_F,       B_F=H_F,W-E0,W.         (2)

The transitions include their actual multiplicities. There are five inverse stages. The final transition contributes another1/2 but NO sixth inverse. Apply the original ordered gamma_v gamma_w closing functional and its established conversion to the real coefficient of i beta_v beta_w. The norm of that normalized physical closing pair is1. If a numerical coordinate convention instead introduces a non-unit closing matrix, its norm factor must be priced explicitly, as in the earlier L4 implementation.

Equation (2) retains all mixed middle masks and automatically retains the five negative signs. Neither positivity of a Gram factor nor an absolute value can replace the closing amplitude. Folded/scalar cancellation and identification of these irreducible chains with each sixth nonscalar coefficient remain the same source-bound perturbation premise; this algorithm does not independently prove new folded cancellations.

## 5. Residual-certified Galerkin inverse

Choose a finite dictionary |Z_1>,...,|Z_R> for one support. Define the Hilbert Gram S, quadratic A_F, and squared-quadratic Q_F by

    S_ij=<Z_i|Z_j>, A_F,ij=<Z_i|B_F|Z_j>,
    Q_F,ij=<Z_i|B_F²|Z_j>.

These are obtained from Section3; no Fock vector is stored. If the approximate source has dictionary coefficients b, a Galerkin candidate c solves A_F c=-S b. Any computed c is acceptable as a candidate; round it to rational complex values for certification. Its EXACT residual is r_F=B_F sum_i c_i|Z_i> + sum_i b_i|Z_i>, with

    ||r_F||² = c†Q_F c + 2 Re(c†A_F b) + b†S b.        (3)

A certified upper bound on (3), together with the certified parity gap delta_F, yields

    error_F <= [residual_norm_F +(1/2)sum_(G -> F) error_G]/delta_F. (4)

This follows directly from ||B_F^(-1)||<=1/delta_F and the triangle inequality. It covers Galerkin truncation, rounded coefficients, overlap arithmetic and preceding errors. A certified nonnegative upper enclosure is required; clipping a negative floating residual to zero is invalid. Interval expressions can be cancellation dominated and require higher precision or an exact evaluation. Ill-conditioned Gram matrices must be treated with certified rank/conditioning checks; discarded dictionary directions require their own norm-loss bound.

The final error is half the sum of incoming errors, multiplied by the closing functional norm. This produces an interval for each coefficient. No integration tail enters if the certificate is computed by (3). If Gaussian time filters are used merely to propose Z, their approximation errors do not enter separately: Z defines the actual trial vector and (3) judges it directly.

## 6. Laplace route remains a fallback, with proper gap scope

For any chain with positive fixed-parity gaps, the previous exact kernel obeys |K(t_1,...,t_5)|<=exp(-sum_j delta_j t_j). Using separate cutoffs T_j gives a union-bound tail

    sum_j exp(-delta_j T_j) / product_i delta_i

per normalized ordered kernel. Multiply by actual word weights1/64 and sum every word. This permits mask-specific gaps, but it does not remove the five-dimensional quadrature or word count. The1/64 and five-resolvent minus are unchanged. A proper return to the initial vacuum would require an explicit reduced-projector subtraction; it cannot be fed into this bound as an ordinary positive inverse. The current adjacent census excludes such proper zero toggles; other support censuses need their own proof.

## 7. Concrete feasibility gate, not a launch plan

The practical unknown is the dictionary rank and the cost of certified overlap arithmetic, not the existence of formula(1). An uncompressed sum of Gaussian states grows exponentially under successive inverses. There is no theorem here bounding the useful rank by32 or any constant.

A bounded next implementation should first build exact field/Pfaffian B and B² matrix-element primitives and compare them with tiny CAR fixtures. Then, under a separately reviewed cost contract, measure one fixed80-by-80 overlap-plus-quadratic-residual pair, including a deliberately near-singular overlap. No physical coefficient is needed for that cost. This would price the real certificate kernel before thousands of prefix states are attempted.

Only after that passes, a separate rank-limited physical pilot could use R<=32: vacuum plus all thirty first-stage two-edge Gaussian filter proposals at a fixed time1 in units|t|=1 for a nonadjacent support, rounded to a preregistered dyadic precision. Select one predetermined mixed second-stage key, with one pair used at each star; retain BOTH predecessor orders. Solve and certify its two first-stage inverses and its mixed inverse. The same three-key test on an adjacent support is a separate control if its census is frozen. No favorable-prefix replacement or rank increase is implicit. The pilot succeeds only if its residual-derived error meets a prospectively specified coefficient-budget share AND its measured cost forecasts the whole fixed census with headroom. Otherwise it records a low-rank/cost failure, not a physical coefficient result.

At R=32,m=40, a double-complex transition covariance cache for all R² pairs is about R²(2m)²*16 bytes, roughly100MiB before interval widening and overhead. Storing exact algebraic entries can be far larger. Streaming pair kernels and retaining only small coefficient matrices is therefore necessary under384MiB. Naively every prefix requires R² Pfaffians of cost O(m³); even though there are only1022 or2038 states, this can be expensive in exact arithmetic. A common dictionary permits reuse of overlaps and linear quadratic forms; prefix-dependent B_F² terms still need certified contraction or streaming. No measured speed or rank forecast is asserted.

This is a falsifiable route that replaces huge Fock vectors and tensor quadrature with a finite dictionary and exact residual accounting. It is not yet a demonstrated practical all-six computation. The missing nonadjacent gap certificates and rank/certificate-cost test are explicit blockers to claiming such completion.

## Exact toy control

A four-mode even Gaussian source with amplitudes(1,1,1,1) on occupations00,10,01,11 is divided by positive denominators(1,3,5,7). The resulting coefficients violate the Gaussian Plucker relation a00*a11=a10*a01. Thus an inverse is demonstrably non-Gaussian. Four specified product-pair Gaussian dictionary states span this example, and exact Fraction Galerkin solution gives zero residual. A one-state dictionary gives a positive residual and its gap-one error enclosure is checked. The block-Pfaffian overlap sign is checked against all16 direct overlaps. These are finite mathematical controls, not evidence of low rank in the physical L6 problem.

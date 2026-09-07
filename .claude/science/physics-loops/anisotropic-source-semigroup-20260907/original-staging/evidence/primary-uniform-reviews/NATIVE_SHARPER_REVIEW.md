# Independent cold review of the sharper k^52 normalization

Reviewed native DERIVATION.md SHA230e7f325100b27e2f1f1642383f526fc52be7e23792e42f5981b9f8e6720b31 after freezing my independent review of root's k^98 proof. I did not read root's sharper-review memo. Verdict: PASS. The k^52 improvement follows from a valid exact normalization identity and the true Gaussian L2 size; it does not assume a uniform Gaussian peak or discard a partition factor without accounting for it.

Let the full sixteen-dimensional source covariance have sigma_plus and sigma_minus each repeated eight times. Its determinant is (sigma_plus sigma_minus)^8. For its normalized Gaussian g, direct squaring and integration give

    ||g||2=(4pi)^-4 (sigma_plus sigma_minus)^-2.

Since sigma_plus=30 and sigma_minus is bounded above and below by constants times k^-1 for k>=1, this is O(k²). The density peak itself is O(k4), so treating the peak as uniformly bounded would be false; the proof does not do that. For any fixed polynomial weight, the ratio of the weighted squared integral to ||g||2² is a Gaussian moment with covariance Sigma/2. Its largest eigenvalue is at most15, independent of k, so the weighted norm is also O(k²).

The uniform unnormalized Taylor estimate O(k²/beta) is justified by the same fixed E1 chart lower bound, affine-in-k action derivative bounds and exact two-source cubic cancellation reviewed in ROOT_REVIEW.md. It remains valid in every fixed polynomial-weighted L2 norm. For the actual nuisance-complement piece, the pointwise scaled bound is beta60 exp(-g beta); the sixteen-dimensional source chart has volume O(beta8), giving L2 bound beta64 exp(-g beta). Adding a fixed polynomial weight only introduces a further fixed beta power, absorbed by the exponential. This supplies an L2 tail estimate, not merely a small total mass assertion. The full partition tail is beta68 exp(-g beta).

The Gaussian nuisance-cutoff remainder is dominated by the fixed Q1 Gaussian. Extending from the expanding source chart produces at worst Ck4 times a fixed polynomial in beta times exp(-c beta) in weighted L2, using the actual O(k4) peak and uniform smallest precision. This is harmless compared with k52/beta for k>=1. Thus chart extension and nuisance tails do not introduce an unpriced dependence on k.

The exact identity is

    p-g=(n-n0)/Z + g(Z0-Z)/Z,   n0=Z0 g.

Under beta>=Ck50, Z>=Z0/2>=c k^-48. The first term costs k^(2+48)/beta=k50/beta. The second costs ||g||2 k^(2+48)/beta=k52/beta. This is equivalent to the two-denominator form but retains the exact leading Gaussian factor instead of bounding n0 by a k-independent envelope. No cancellation of unrelated remainders is assumed.

The reciprocal source half-Haar factor is uniformly bounded on the fixed chart. Its difference from its value at zero is at most C R²/beta, so its action on g costs O(k²/beta); multiplying the p-g error by the bounded factor preserves k52/beta. Independent angular averaging contracts L2. Outside the source chart the actual density is bounded by C beta68 k48 exp(-c beta), using the partition lower bound; after beta^-4 scaling and finite Haar-volume integration this gives beta64 k48 exp(-c beta), again bounded by Ck52/beta. The full operator, not only its compression, is therefore controlled.

The limiting top eigenvalue has a uniform positive lower bound. The norm comparison then permits actual-norm normalization once beta>=Ck52, with the same error rate. Both the full normalized source operator and its compression are contractions. Unitary oscillator rescaling adds no k loss to norm or Hilbert-Schmidt error. For k_n=4n²/(5t²), beta_n=n108, the n-step telescope costs n*k_n52/beta_n=O_t(n^-3), while n*t_k_n-t=O_t(n^-2). Spectral calculus on the full nonnegative number-operator spectrum gives the total O_t(n^-2) rate. The same telescope controls true powers versus repeated chart cutoff; source compression itself remains an explicitly supplied composition rule.

No correction is required to the frozen sharper theorem. The n108 schedule is a sufficient asymptotic construction with unknown constants and onset, not a practical finite-resource accuracy certificate. It does not equate powers of the compressed source with a longer full Wilson slab, derive physical elapsed time, or remove the fixed-model imports. This review approves these stated mathematical quantifiers only.

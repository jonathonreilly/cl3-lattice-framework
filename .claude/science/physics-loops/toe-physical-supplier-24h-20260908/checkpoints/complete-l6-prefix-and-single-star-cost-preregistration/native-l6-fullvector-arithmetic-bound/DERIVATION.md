# Certified arithmetic envelope for a21-mode Majorana action

Status: conditional arithmetic theorem and candidate-certificate design. No physical action, solve, spectrum or residual has been executed or certified in this task. Root exposed the21-mode/four-action target before the independent derivation. Subsequently read the complete candidate kernel.py and run.py in native-l6-single-star-action-pilot at freeze8c4e8537. That code explicitly labels its output a floating candidate. This proof does not retroactively turn it into an interval implementation.

## Exact operator and indexing domain

There are21 complex modes and d=2^20 coordinates in each parity. Source coordinates encode the first20 occupation bits; bit20 is the XOR of their parity and the prescribed source parity. Toggling j<20 changes compressed index by XOR2^j; toggling j=20 leaves it fixed. The target belongs to the opposite parity, including j=20. The Jordan–Wigner sign is (-1) to the number of occupied lower bits. For fixed j this is a signed permutation between parity spaces. Hence a scatter update with a fixed j and chunk has no repeated targets. Across all chunks each target receives exactly one term from each j. The per-coordinate summation order may differ from j-order because the chunks are outermost, but it is deterministic and contains21 terms. The bounds below do not require the same order for different coordinates.

Write the physical endpoint Majorana as Γ=sum_j(a_j A_j+b_j B_j), with real coefficients, Hermitian CAR generators and sum(a_j²+b_j²)=1. In the candidate's empty-mode convention its coefficient on an occupied bit is a_j+i b_j(2n_j-1). Changing the paired-B convention changes both this formula and H0; they must not be changed independently. Exact endpoint containment in the42-dimensional invariant space is load-bearing for norm Γ=1. A projected non-endpoint vector only has norm at most1; it cannot silently be called a full Majorana.

Let the actual stored binary64 coefficients be a_hat,b_hat, interpreted as exact dyadic numbers. Obtain rational bounds e_aj>=|a_hat-a| and e_bj>=|b_hat-b| from the original exact frame, not from a repeat floating conversion. Put eta²=sum(e_aj²+e_bj²), and take any rational upper bound eta_up>=sqrt(eta²). CAR gives

 ||Γ_hat_exact-Γ|| <= eta_up.

This sharper l2 bound requires that both parity directions use the same stored real coefficients and exact sign/conjugation operations. Without that structural guarantee use the conservative sum_j sqrt(e_aj²+e_bj²). Also define rational L>=sum_j sqrt(a_hat_j²+b_hat_j²); L<=sqrt21(1+eta_up) is available with an outward rational sqrt21 bound.

## IEEE assumptions and a rational local roundoff bound

Assume binary64 round-to-nearest/ties-even, gradual underflow, no flush-to-zero, no fast-math reassociation, and the declared deterministic complex product implemented by four real multiplications and two real additions (an FMA realization is allowed only with a separately no-worse bound). All operands and EVERY intermediate real arithmetic result must be finite. Index arithmetic is exact in its stated uint32 range. Complex construction, conjugation, multiplication by ±1 and multiplication by ±i must be exact swaps/sign operations; if a compiler inserts other arithmetic, account for it separately. No BLAS contraction is used.

These are sufficient checkable implementation assumptions, not facts established by a final np.isfinite(output) alone. Final finiteness cannot detect every intermediate exceptional operation or flush-to-zero mode. The present candidate lacks the intermediate/FP-environment evidence required for a certificate.

Set u=2^-53, zeta=2^-1075 and gamma_n=n*u/(1-n*u). The basic bound, allowing subnormal results, is

 |fl(a op b)-(a op b)| <= u|a op b|+zeta

for finite real addition/subtraction/multiplication without overflow. Define, for m=21,

 beta_m=gamma_m+2*gamma_2*(1+gamma_m),
 tau_m=8*m*zeta/(1-u)^(m+2).

Both are exact rational constants. For one complex coordinate summing m products,

 |y_hat-sum_j c_hat_j x_perm(j)|
 <= beta_m sum_j |c_hat_j| |x_perm(j)| + tau_m.                 (1)

Proof: a complex product's two real two-term dot products have relative contribution bounded by sqrt2*gamma_2 |c||x|, which is at most2gamma_2|c||x|. Each real component has at most three absolute zeta injections in that multiplication. The subsequent at most m complex additions have relative gamma_m and at most m further injections per real component. Propagation along a dependency path is bounded by (1-u)^-(m+2). Thus at most4m injections per component, with Euclidean factor at most2, gives tau_m. Using m rather than m-1 also covers adding the first product to zero. This deliberately overestimates exact sign and zero operations.

Minkowski and permutation invariance turn (1) into the full-vector bound

 ||computed_Γ(x)-Γx|| <= epsilon_Γ ||x|| + a_Γ,
 epsilon_Γ=eta_up+beta_21 L,       a_Γ=1024*tau_21.             (2)

No factor2^20 multiplies the relative error: the only dimension factor is sqrt(d)=1024 on the absolute underflow term. With exact coefficients, beta_21 is about25u and L<=sqrt21, so the relative envelope is of order1.3e-14 per action. This decimal is orientation only; a certificate uses the rational expression. Dropping a_Γ requires a certified no-underflow condition for every intermediate, including detection of nonzero products rounded to zero. Merely checking that nonzero outputs are normal is insufficient.

## Two independent two-Γ chains, not four serial Γ factors

The current pair kernel computes

 A_pair x = D0 x + sum_(ij in pair) (-i Kij) Γ_i Γ_j x,
 D0(b)=sum_j sqrt(lambda_j) n_j(b).

There are two independent two-action chains, four Γ calls total. The changed-edge factor is correct: the original sorted-edge term is (i/2)Kij Γ_iΓ_j; reversing it changes H by -iKij Γ_iΓ_j. In the cost fixture |Kij|=2. Its ±2i scaling is an exact swap/sign/power-two operation provided no overflow; power-two underflow would need its own additive term (scaling by2 does not create it).

For a computed first vector y_j and second z_ij, let X>=||x|| and Y_j>=||y_j|| be certified dyadic-norm upper bounds. Then

 e_j=epsilon_j X+a_j,
 e_ij=e_j+epsilon_i Y_j+a_i                                (3)

bounds ||z_ij-Γ_iΓ_j x||. The first error is not amplified because ||Γ_i||=1. This a posteriori recurrence is usually sharper than expanding a worst-case product. For genuinely k serial actions, the analogous recursion is e_k=e_(k-1)+epsilon_k ||y_(k-1)||+a_k. Ignoring underflow, a uniform a priori bound is [(1+epsilon)^k-1]X. Do not apply the four-serial formula as though the actual two chains were composed together.

For the diagonal, independently enclose each exact nu_j=sqrt(lambda_j) around its actual stored float nu_hat_j with radius d_j. Put T=sum|nu_hat_j| and Delta=sum d_j. The21-term nonnegative diagonal accumulation has absolute coordinate error at most

 d_diag=Delta+gamma_21*T+21*zeta/(1-u)^21.

Its real-times-complex multiplication therefore has vector error

 E_D <= [d_diag+u*(T+gamma_21*T+21*zeta/(1-u)^21)]X
          +2048*zeta.                                      (4)

The final two vector additions can be priced a posteriori. If q is the stored running sum and v the stored scaled chain, then the addition error is at most u(||q||+||v||)+2048*zeta. Add these two errors to E_D+sum|Kij|e_ij. Norms must be certified, not ordinary np.linalg.norm values. This gives an explicit E_H with ||H_pair x-y_hat||<=E_H, including all four Γ calls and diagonal arithmetic. For other K coefficients, separately enclose their errors and multiplication roundoff.

## Coefficients and exact norms without a large algebraic field computation

A rational q=n/d>0 has an exact sqrt enclosure at binary precision p: let k=isqrt(floor(n*2^(2p)/d)); then k/2^p<=sqrt(q)<(k+1)/2^p. Verify the two squared inequalities over integers. Apply signed interval division to each exact frame component divided by sqrt(norm_squared), and to each sqrt(lambda). This covers the actual algebraic coefficients without assuming that math.sqrt is correctly rounded or that a large integer-to-float conversion was exact. The stored float is converted with as_integer_ratio and compared to the interval. If the frame uses explicit Q(sqrt2,sqrt3) combinations, enclose each generator and propagate rational intervals, retaining exact denominator positivity. No measured coefficient is selected to fit a residual.

For an arbitrary stored complex vector, sum the exact dyadic squares of real and imaginary parts in a streaming integer accumulator. A common binary exponent and Python integers avoid a million Fraction reductions; the required exponent range is bounded by the binary64 format. An exact squared-norm rational plus an integer-sqrt enclosure supplies X,Y and all error-norm radii. Memory is O(1) beyond the input buffer. This is a proposed certifier, not an already timed implementation.

## Residual certificate and limitations

If r_hat=fl(b-y_hat), with y_hat the candidate Hx application, then

 ||b-Hx|| <= ||r_hat|| + E_H + u(||b||+||y_hat||)+2048*zeta.

Each displayed norm has an exact dyadic upper enclosure. A separate positive lower spectral bound delta for the SAME parity/prefix operator then gives solution error at most this residual bound/delta. An approximate right-hand side needs its own error added. All-prefix positivity is not supplied by this arithmetic lemma.

Selected coordinates can be recomputed in exact algebraic interval arithmetic as a sensitive implementation check, but cannot certify the remaining coordinates. A full certificate can combine a full deterministic-error envelope (2)-(4) with an exact full-vector norm, or replay every coordinate in intervals. A sampled-coordinate test alone, an IEEE-model statement without implementation guards, or a finite output check alone is not a residual certificate. The current cost candidate may be profiled under its declared noncertificate scope; it must not be used as certified arithmetic without these additional obligations.

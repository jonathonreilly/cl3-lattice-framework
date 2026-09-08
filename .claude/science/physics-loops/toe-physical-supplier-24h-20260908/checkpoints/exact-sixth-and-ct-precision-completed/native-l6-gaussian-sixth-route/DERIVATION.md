# Branch-free Gaussian kernel for the L6 sixth-order route

Outcome: an exact polynomial-size pointwise kernel and rigorous integral error bounds are available. They do NOT yet give a tractable certified full coefficient calculation. The explicit tensor-quadrature cost below is the remaining obstruction. No physical integral was executed.

Use the supplied uniform L6 endpoint, unique active vacuum |0>, and actual ordered closure gamma_v gamma_w. Assume each proper prefix F in the specified adjacent sixth-word family has a certified positive fixed-INITIAL-parity denominator delta_F for G_F=H_F−E0. This assumption can follow from strict flux isolation plus the separate singleton-cut parity argument, but an existential gap is not a numerical integration parameter. The initial parity is invariant under all quadratic evolutions. A singleton cut's unrestricted zero-energy state must not be used to set delta=0 or silently removed by changing parity.

For an irreducible word with five proper inverses,

<0|gamma_v gamma_w R5 R4 R3 R2 R1|0>
 = − integral_(R_+^5) <0|gamma_v gamma_w exp(-t5 G5)...exp(-t1 G1)|0> dt.

The minus is FIVE negative resolvents. Electric factors1/2 per insertion and the parent Gauss closing orientation remain outside, giving1/64 per six-insertion word. The closing expectation is generally imaginary; its conversion to the real coefficient of i beta_v beta_w must retain the established ordered sign. This expression cannot be replaced by its absolute value. The specified boundary-once/bridge-twice family has no zero-toggle proper prefix; a general family with a vacuum return would require reduced-projector subtraction, not this unmodified integral.

## Exact Pfaffian evaluation without a square-root branch

Diagonalize each real skew216x216 K_F into108 orthogonal two-planes, keeping the identity K_F=sum_l omega_l(a_l b_l^T−b_l a_l^T), omega_l>=0. Then H_F=sum_l (i omega_l/2) gamma(a_l)gamma(b_l). Its exponential is a product of108 commuting factors

cosh(t omega_l/2) [1−i tanh(t omega_l/2) gamma(a_l)gamma(b_l)].

Keep the FIVE exponentials in their physical order. There are q=540 elementary pairs, plus the closing pair placed FIRST. Let eta_1,...,eta_(2q+2) be those ordered Majorana linear forms. For i<j define C_ij=<0|eta_i eta_j|0>, extend skewly and set diagonal zero. In terms of the initial complex structure J0, this contraction is a_i·a_j+i a_i^T J0 a_j in the stated vacuum convention. The dot product must remain for forms from different factors; they are not generally orthogonal.

Let Jpair have2x2 antisymmetric blocks with upper entry1 for each exponential pair, and upper entryZERO for the closing pair. Let D be diagonal: the first member of each exponential pair receives its coefficient -i tanh(t omega/2), the second receives1; both closing entries receive1. The kernel is exactly

exp(E0 sum t_j) product_(j,l)cosh(t_j omega_jl/2) Pf(Jpair+D C D).

This formula has no determinant square root and no sign choice. Expand the Pfaffian in its Jpair entries: omitted factors must be whole adjacent pairs; all remaining contractions form their ordered Wick Pfaffian. Moving whole pairs has even sign. The zero closing Jpair block forces both closing operators to participate. This proves the formula directly from CAR/Wick expansion. Six small exact integer-complex CAR controls compare it with direct two-mode multiplication, including repeated generators and mandatory insertion. They supplement the derivation, not a216-mode benchmark.

A numerical implementation must certify eigenplanes/exponentials and the Pfaffian or use an equivalent interval matrix-function construction. Arbitrary real eigenvectors without reconstruction/error bounds are not certificates. The cosh prefactor can be enormous while the final answer is small; direct floating assembly can overflow or lose cancellation. A stable scaled Pfaffian implementation is therefore an additional engineering/certification obligation. Pointwise arithmetic size is1082x1082 rather than2^108 Fock dimension, but that is not by itself an efficient five-dimensional integration method.

For literature context only, Klich arXiv1403.7824 and Robledo arXiv0901.3213 study Gaussian determinant/Pfaffian sign issues. Only their abstracts were inspected in this pass; neither is a load-bearing unverified formula import here. The ordered-pair Pfaffian above was derived by finite expansion.

## Certified tail and a concrete, expensive quadrature

Let delta=min delta_F>0. Restricted semigroup norms imply |kernel(t)|<=exp(-sum delta_j t_j), since the closing pair has norm1. Truncating every coordinate at T gives absolute error at most5 exp(-delta T)/delta^5. For a family of M ordered words with coefficient1/64, a safe summed tail is (5M/64) exp(-delta T)/delta^5. Choose T from this inequality BEFORE numerical integration. This bound is valid despite unrestricted odd-parity zero modes because the entire integrand remains in the fixed initial parity space.

For an entirely explicit tensor Gauss-Legendre rule with n points per coordinate, let B bound every ||G_F||. The 2n-th derivative in one coordinate has magnitude at most B^(2n) on the truncated box. Positivity of the quadrature weights and telescoping tensor integration give error at most

5 T^(2n+5) B^(2n) (n!)^4 / [(2n+1)((2n)!)^3]

per word, plus certified point-evaluation error times T^5. This is crude but rigorous and avoids claiming an observed convergence rate. It requires M n^5 Pfaffian evaluations. For illustration only, even n=20 and M=194400 would mean622,080,000,000 evaluations. The L4 word count is NOT automatically the L6 count; exact L6 graph matching must supply its own M. The example demonstrates the scaling problem, not a proposed run budget.

For L6, a simple uniform bound is B<=648+|E0| in units|t|=1, since648 bond terms each have norm1. Thus the crude derivative bound can demand far more than20 nodes when delta is small. Geometric paneling and analytic semigroup derivative estimates can reduce one-dimensional cost, but do not remove the fifth power or word sum. No claimed optimization has been silently applied.

## Numerical gap route and remaining work

The physical vacuum energy difference of a prefix is half the difference of sums of positive active frequencies, with the full vacuum offset. Rational upper approximants to sqrt(x), including iterated Newton rational functions, can bound the prefix trace from above, while the known canonical radicals are bounded below. Exact LDL traces at rational shifts avoid treating floating singular values as certificates. At L6 the canonical spectrum is not constant; the L4 one-iteration bound may be negative despite a positive true gap. Increase approximation order only under a new fixed bounded contract and retain failures. A singleton cut still uses the initial-parity excitation threshold separately.

A useful next design must reduce the integrated WORD SUM before quadrature (for example, a verified Gaussian mixture compression with explicit error, or a recurrence integrating one variable without exponential growth), and supply numerical lower bounds for every relevant prefix. Neither step is solved here. This pass gives an exact sign-safe kernel and finite rigorous error contract, but does not meet the target of a tractable certified adjacent coefficient beyond the flat-W20 case. It does not license a costly full calculation or assert that the coefficient vanishes/nonvanishes on L6.

# Independent review: infinite two-link impurity gap

Verdict: **PASS, source-bound**, for the stated canonical infinite Gaussian GNS reference and h=2|t_hop|>0. No finite-size h/6 threshold, active bulk gap, node value, or new physical numerical result is inferred.

Reviewed complete UNIFORM_PAIR_GAP.md (8797f6b4bc361eb270b4ee3b70d31ff2b5b04b122c495b7bcfedc24d41a38c0d), standalone impurity_gap_controls.py (7caf394eb720c778fec6aad485435c0d93e74c7b85f2c89873ee774a0d2a14c0), its contract and exact output, and the improved-tail receipt. Re-read the complete canonical thermodynamic parent, reusing my prior independent review of its local-core passage and the earlier canonical dispersion/shifted-grid premises. This review is independent of the new impurity derivation; I previously reviewed related parent theorems.

## Determinant and normalization

Writing the projected resolvent as [[a,c],[-c,b]] and DeltaK=[[0,beta],[-beta,0]], the determinant is det(I-R DeltaK)=(1+beta c)^2+beta^2 ab. Here c=-sqrt(2)h D and beta=2sqrt(2)h, giving exactly (1-4h^2D)^2+8h^2 s^2 A B. In particular the sign of the linear term is negative; reversing it would destroy the claimed reduction.

The canonical square hopping operator has same-cell-parity two-step translations and no mixed-axis terms. In the signed neighbor sum, perpendicular neighbors occupy different cell parities and give B=A; opposite neighbors subtract the same-axis Green entry and give B=A-G2=D. The center row resolvent identity gives s^2 A+6h^2D=1. Substitution yields both stated determinants. These are full-bath determinants, not a reduced-state energy formula.

For a real skew K, det(s-K)=product over positive frequencies (s^2+omega^2). The native full-active vacuum energy is -sum omega/2=-Tr|iK|/4. Thus the energy difference is exactly -(2pi)^(-1) integral log d. No spectator or parity factor should be applied again. This is the correct normalization.

## Green-function estimate and log bound

At zero frequency X=4h^2 sum sin^2(k) equals 6h^2(1-phi) after folding. Symmetry phi to -phi converts the expectation to 1/(1-phi^2), legitimizing the nonnegative return expansion. On phi>=0, 1-phi>=2|x|^2/(3pi^2), and doubling the Gaussian bound for the negative region gives 3sqrt(3)pi^(3/2)/(32 n^(3/2)). The constant is <1 using pi<22/7. The exact partial sum through100 plus integral tail1/5 gives A(0)<=17/(60h^2).

I independently recomputed the partial sum with a one-index binomial convolution, rather than the author's factorial triple sum. It agrees exactly. The moment inequality is Cauchy-Schwarz with EX=6h^2 and EX^2=42h^4; it gives 1-z>=6h^2/(s^2+7h^2).

For opposite pairs -log d>=1-d gives 4h/(7sqrt7)>h/5. For perpendicular pairs the upper bound at u>=1/3 is algebraically correct. Below that threshold the A(0) polynomial bound applies; its endpoint P(1)<1 also licenses integrating the polynomial lower bound throughout y in[0,1]. The separate global d<=1 proof is essential to dropping the rest of the frequency integral and is supplied. I independently integrated the twelve log terms by a direct trinomial formula, without the author's polynomial multiplication routine. It reproduces the exact rational lower bound, which exceeds1/6.

## Infinite-volume passage

For fixed s>0 the finite AP Riemann sums converge. The previously proved uniform shifted-grid A_L(0) bound and d_L>=1/9 control log d near zero on the required AP sequence. At infinity the canonical bounded dispersion and unchanged Tr K^2 cancel the s^-2 term; the remainder is uniformly O(s^-4). Hence dominated convergence applies to the finite full-active ground-energy differences even though those finite differences were not individually shown >=h/6.

The finite inequality with its actual finite ground-energy difference passes on each fixed local polynomial vector. Only a centered local box is identified between the torus and infinite CAR algebra. The commutator energy form is local, and the Gaussian state converges there. The supplied analytic local-polynomial core plus bounded quadratic impurity extends the limiting form inequality to H+B_A>=h/6. This does not require existence of an impurity ground vector in the reference representation or any gap of H itself.

## Controls and downstream scope

Independent check.py was frozen at fbb338490c2c61ff195c669ae237244c18d5b1dd8b8ddabe332e1c12b01cb8f3 before its single execution. The exact return and polynomial calculations, rational algebra spot checks, and independent degree160 exponential lower sum all passed. The last confirms the stated90-word time-tail bound at delta=h/6, beta<3h, T=160/h, conditional on the previously supplied tail formula. These small algebra controls support the proof; they are not lattice spectra or momentum quadrature. External receipt:0.02s,16,171,008-byte maximum RSS, exit0, within the allowed60s/384MiB. No physical action or solver was run.

The improved gap can be used in the infinite two-link denominator and its tail bound. It does not certify Gaussian numerical conditioning, the node sign, a finite-L threshold, or fixed-U stability.

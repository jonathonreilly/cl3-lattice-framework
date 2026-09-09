# Cyclic CAR compression: independent review

PASS for the mathematical approximation statement in the root DERIVATION.md, with the implementation boundary below. No physical run or covariance construction was performed.

For V_m=span{K^j s:0<=j<m}, induction gives K_m^n s=K^n s for n<m. This holds for every vector in the entire seven-seed span, so the Taylor error bound is an operator-norm bound on that span, with no sqrt(7) loss. Compression cannot increase ||K||, and the factorial-tail inequality gives2exp(W|t|)(W|t|)^m/m!. At m>=4eW|t|, the exponent is <=m/(4e)-m log4<-m. Dimension<=7m and CAR norm comparisons of propagated real fields are correct.

The free Gaussian state must indeed be restricted: Gamma_m=P_m Gamma P_m. Generally Gamma_m² is not the pure-state value, and sign(K_m) is a different state. If the real cyclic dimension is odd, a finite Fock implementation can append an uncoupled auxiliary Majorana with zero covariance; this changes no even expectation being calculated. It must not manufacture a pure vacuum instead.

Important additional boundary: the restricted generalized zero-mode coefficient q need not satisfy K_m q_m=0. Projection can create a boundary source at the top Krylov degree. Therefore the approximation must be applied to the previously derived explicit local-J insertion formula for the node, rather than deriving a new compressed soft-annihilator identity. The former needs only real-time propagated local fields and cocycles and is valid; the latter is not licensed by the Taylor argument.

The accompanying extension derives a complete two-filter node error under the explicit-insertion convention. It is a new derivation requiring separate independent review. It shows a finite sufficient dimension, but does not yet establish affordable computational cost or certify Gram/covariance numerical conditioning.

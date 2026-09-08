# Independent bounded plane-law derivation

This is scratch mathematics for review, not a new canonical claim. The handoff checkout is stale: current main's block05 P7 already proves opposite-corner equality and executes exactly two classes. Reproducing that result is not new work.

Let K be the positive symmetric stochastic six-state orbit kernel, H=K². Current block05 proves the rectangle density

mu_R(x)=(1/6) product_{nearest-neighbor edges in R} K(x_u,x_v) / product_{unit squares in R} H(x_SW,x_NE).

## Projective consistency

The underlying top-left directed construction is normalized. Summing the bottom row right to left removes leaf conditional factors, each summing to one. Summing the right column bottom to top does the same. The already-proved 180-degree identity yields top-row and left-column removal. Successive removal of outside rows and columns therefore gives the same formula on every contained subrectangle, independently of position. This argument applies to every finite size, rather than extrapolating from executed cases.

Consistent rectangle laws determine consistent arbitrary finite-set laws by embedding each set in a rectangle and marginalizing. The countable finite-alphabet extension theorem then gives one probability measure on the plane for this chosen diagonal class. Translation invariance follows from the position-independent marginal formula. This does not construct an infinite physical formation schedule, which has no first site.

## Two classes and constant boundary

Opposite-corner equality is inherited from main. The two diagonal classes differ for every nonconstant orbit triple: in a square their positive common numerator has denominators H(a,b) and H(c,d). Equality for all four labels would require H constant. For the orbit kernel, H_parallel-H_antiparallel=(p-q)^2/Z². If p=q, H_parallel-H_orthogonal=2(p-r)^2/Z². Thus H constant iff p=q=r. For positive nonconstant triples the plane laws differ already on a square; constant weights give the independent uniform measure. This all-parameter extension is analytic and requires independent review; the current parent only asserts its executed distinctness fixtures.

## Conditional density and affirmative interaction identification

For the center of a 3x3 square, conditional on its eight other sites,

mu(z | boundary) is proportional to product_{four axial neighbors v} K(z,x_v) / [H(z,x_NE) H(z,x_SW)].

Exactly two square denominators depend on the center. With all eight labels equal to c this is K(z,c)^4/H(z,c)^2, whereas the original nearest-neighbor specification is proportional to K(z,c)^4. Their equality requires the positive column H(.,c) constant. Orbit transitivity and the preceding formulas imply this occurs only for constant weights. Since the conditioning event has positive probability, the discrepancy is genuine. If the full-rest conditional were the original four-neighbor rule, conditioning it onto these eight sites would retain that rule by the tower property; hence this finite discrepancy rules it out.

There is a positive finite-range identification: the plane law is a Gibbs measure for the pair potential -log K on axial edges and +log H on the chosen SW-NE diagonals. To verify this without assuming a Markov property, condition a finite set A inside an enclosing rectangle whose boundary lies beyond every axial/diagonal neighbor of A. Cancellation in the rectangle density gives precisely the finite-volume conditional with these pair factors. It depends only on the finitely many outside neighbors of A and therefore is unchanged as the enclosing rectangle grows. Conditional-expectation martingale convergence to the sigma algebra of all sites outside A proves the full conditional formula. Positivity prevents undefined local conditionals. No uniqueness of this expanded-interaction Gibbs specification is claimed.

This supplies an exact interaction description of the selected formation-class law, including the extra diagonal interaction induced by local normalizers. It does not identify this law with the original admissibility specification, choose a physical corner/order, identify a Gaussian or quantum instrument, or select an action from the axioms. Those remain the action-identification obligations.

## Executed scope

Independent checker: all 46656 configurations of 2x3 at three frozen triples; all its subrectangle marginals; all reflected dictionaries; exact 3x3 six-value center conditionals. It also checks 96 trimming schedules on 3x3/3x4. The latter is a combinatorial trimming check, NOT a complete 3x3/3x4 marginal enumeration or independent validation of every algebraic cancellation. Total163 checks, 2.504 seconds,50.110MiB. Constant control has zero defects. Nonconstant mirror TV values reproduce current parent exactly.

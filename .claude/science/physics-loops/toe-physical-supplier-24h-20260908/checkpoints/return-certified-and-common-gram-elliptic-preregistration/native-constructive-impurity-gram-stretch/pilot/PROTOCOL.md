# Fixed common-Gram pilot: prospective, UNLAUNCHED

No new physical integral or resolvent solve is authorized by this file. Root review, independent source review, remote preregistration and a separate external watchdog must precede the single actual matrix call.

## Fixed inputs and geometry

Use only the already accepted `native-star-local-green-gram-run-41ebe/RESULT.json`: A,A',B,B' at s=1,2, in h=1 units. The acceptance and worker completion bind that exact result. All eight intervals have width at most1/32. Never replace them by midpoints, refine them in this pilot, or recompute the scalar integrals.

The28 real columns are y_(s,sigma,a)=-i(h0-i sigma s)^-1 e_a, in labels (1,+),(1,-),(2,+),(2,-), each center,+x,-x,+y,-y,+z,-z. The rephasing is common; h0=iK is pure imaginary, so these y are real. Assemble G=Y^T Y and J=Y^T Gamma0 Y, each28x28; P0=(I+iGamma0)/2 gives the projected Gram (G+iJ)/2. Covariance closure is implicit in span(Y,Gamma0Y), at most56 real dimensions. It is not a28-dimensional invariant dynamics approximation.

Write R_sigma=i C_sigma and Ftilde_sigma=(i C_sigma+L_sigma)/2 using the frozen local Green identities. Then G=(C_tau-C_-sigma)/(sigma*s+tau*t), J=-(L_tau-L_-sigma)/(sigma*s+tau*t). At tau=-sigma,t=s the exact confluent replacements are C'_tau/tau and -L'_tau/tau. The derivatives use only the supplied scalar derivatives. Hermitian/skew symmetry and zero skew diagonals are imposed as exact identities, not inferred from interval midpoints.

There are three independent exact column relations. Since (K-sigma*s)y=-e and K e0=sum_a(e_+a-e_-a), each label obeys sum_a(y_+a-y_-a)-sigma*s*y0=-e0. Subtract the first label from each of the other three. This shows raw rank at most25, without asserting that rank is attained. Record all three vectors and verify that interval G,J times each contain zero. Do not force interval cancellations or use these checks as a proof of the Green identities.

Particle-hole and purity follow analytically: Y is real, J real skew, complementary projected Gram is (G-iJ)/2, and Gamma0^2=-I. The enlarged Gram is [[G,J],[-J,G]]. No interval eigenvalue or PSD test is substituted for those source assumptions.

## Fixed pivots, error and stopping

All arithmetic uses exact Fraction endpoints with outward48-bit dyadic rounding after operations. A divisor must exclude zero. Greedy next index maximizes the certified diagonal LOWER bound, smallest index breaks ties. A pivot requires its lower bound strictly positive. Updates are the reviewed paired formulas, including both y and Gamma0 y. Selected rows and columns are set to exact zero by their algebraic annihilation identity. No other negative diagonal is clipped or made positive.

After each pair, record residual trace interval and initial trace interval. With actual residual r>=0, the error bound for Q=Y C Y^dagger with ANY ||C||<=1 is 2 sqrt(Tr G_initial) sqrt(r). The pilot reports its squared upper bound 4*TrG_upper*r_upper. Target is squared error<=1/4 (error<=1/2). This is a conditional raw-column certificate: no actual physical C, stationary quadrature, balanced impurity projector, alpha, or time evolution is assembled.

Stop at the target, or when the maximal pivot lower bound is nonpositive, or after28 pairs. All non-target endings are explicitly INDETERMINATE, not failed precision tests silently replaced by a different threshold. If the residual upper endpoint is negative, raise FAILURE. Interval residual lower bounds may be negative from overestimation; they are reported intact. No rerun, precision escalation or new pole follows this contract.

## Execution and retention

Require exactly `python -I -B -S run.py gram FRESH_EXTERNAL_OUTPUT`. Actual readiness uses `readiness` instead and validates pins, parser and accepted input schema; it does not call assemble/compress. The worker imports source only from verified bytes. Freeze pins interpreter, broad standard-library and dylib runtime inherited from the already reviewed scalar dispatcher, all actual source/proof/input files, and exact local executable/directory membership. Loaded modules are checked before and after execution. Operating-system implementation remains outside these file pins.

One external root monitor and one worker, at most30 seconds total inclusive startup/hash/I/O/teardown and384MiB whole-tree sampled RSS. Worker alarm29 seconds; proposed external kill29.5 seconds, external30-second limit. The root must supply that monitor separately before execution. No root monitor exists in this package yet.

The matrix workload is at most28 paired updates of406 upper-triangle entries, with exact dyadic rounding limiting denominator growth. Two28x28 matrices and compact histories are small relative to384MiB. Expected seconds are only an algorithmic estimate, not a measured physical cost. This bounded pilot establishes actual cost; a timeout is retained and ends the attempt. The earlier scalar pilot's0.63-second timing does not price these updates.

Write PARTIAL before every stage and pivot, full initial GRAM_INTERVALS, ALGEBRA null receipts, then RESULT. Any exception retains stage and rows in FAILURE; dispatcher failures retain DISPATCH_FAILURE. Worker COMPLETE means execution and guards completed, independent of scientific target/INDETERMINATE status. No accepted result is overwritten.

## Prelaunch synthetic controls

The same core is tested using dyadic vectors in an exact six-dimensional pure covariance and independently dual-differentiated non-native scalar moment functions. These cover interval paired updates, confluent signs and an actual positive-pivot stall. Two actual altered source files remove the covariance partner or reverse the confluent J sign; the synthetic tests must reject each. These tests neither read physical scalar inputs nor assemble a physical Gram.

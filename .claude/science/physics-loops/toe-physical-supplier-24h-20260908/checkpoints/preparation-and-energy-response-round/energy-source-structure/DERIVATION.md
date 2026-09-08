# Pure structure factor through a new diagonal-source energy response

Conditional finite-component construction, 2026-09-08. Root exposed the candidate shift and branch formula before this independent implementation; PREREGISTRATION records that exposure and all parameter choices. This is a new source-tilted kernel, not an unchanged-producer instrumentation. It removes forward walking from the formal response identity, not from every possible practical estimator obligation. No stochastic production has run.

## Source and complete positive kernel

On the actual periodic ice binary-link carrier define the six transverse observables

 O_ab(q,x)=Vol^(-1/2) sum_r (-1)^(r1+r2+r3) exp(i q r_a) [n_b(r)-1/2], a!=b,
 X(x)=sum_(a!=b)|O_ab(q,x)|².

The staggered coefficient, link indexing, geometric plaquette multiplicity and initial component are those of the current-main spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 and transverse-correlator producer, bound by the check source and raw dictionary. Since each of Vol terms has magnitude1/2, |O_ab|<=sqrt(Vol)/2 and0<=X<=3Vol/2=:Xmax on the entire binary carrier. This bound does not rely on an enumerated component or phase cancellation. The observed L2 component maximum6 is not substituted for the frozen global bound12.

Take H(V,lambda)=V Nf-A+lambda X, V<=1, with A the actual geometric flip adjacency and M=3Vol. Set Lambda=|lambda|Xmax and

 G'=I-[H(V,lambda)-Lambda I]/M,
 b(x)=sum_y G'(y,x)=1+[(1-V)Nf(x)+Lambda-lambda X(x)]/M >=1.

At x, uniformly propose one of the M geometric faces; if flippable, accept its flip with probability1/b(x), otherwise stay. Thus P(y,x) equals the number of proposed faces reaching y divided by M b(x), and P(x,x)=1-Nf(x)/(M b(x)). It is nonnegative and sums to1. Retaining the branch b(x) gives b(x)P(y,x)=G'(y,x), including the diagonal. Duplicate destination faces, if present, must be counted separately. Applying only P and discarding b generally gives a different evolution. Systematic population resampling is a finite-population approximation to this positive weighted kernel, not an exact finite-population ground sampler.

At RK V=1, positive lambda without the safeguard would give b=1-lambda X/M<1 on states with X>0 and acceptance1/b>1. The shift is sufficient for either source sign without changing eigenvectors. It is a scalar numerical device; X itself is a nonlocal diagonal source probe and is not derived as a physical interaction or local apparatus.

## Restoring physical energy before response

On the finite connected component the off-diagonal graph is connected. The matrix cI-H for sufficiently large c is nonnegative and irreducible with the same lowest-energy eigenvector as its Perron eigenvector; its Perron eigenvector psi is strictly positive and simple. Finite-dimensional differentiation of H psi=E psi, with psi^T psi=1, yields

 E_lambda=<X>pure,  E_V=<Nf>pure.

The all-ones bra instead gives the distinct mixed identity

 E(V,lambda)=(V-1)<Nf>mixed_lambda + lambda<X>mixed_lambda,
 mixed average = sum_x psi(x) f(x)/sum_x psi(x).

The shifted kernel eigenvalue is g=1-[E-Lambda]/M. Its reported shifted energy M(1-g) is E-Lambda, so Lambda must be added at each source value before differentiating. Alternatively the displayed physical mixed local energy restores it algebraically and needs no unknown discarded growth normalizer. Lambda's absolute-value cusp is not a physical cusp of E. A centered symmetric difference can accidentally cancel an omitted even shift, so that particular cancellation is not a valid restoration check; the per-source energies and one-sided responses are the required distinction.

At lambda=0 the prior exact local moment sum rule gives

 mu_pool = qhat² [V E_V(V,0)-E(V,0)] / [Vol E_lambda(V,0)].

This replaces both pure kinetic and pure structure-factor factors by ground-energy responses. At nonzero lambda the kinetic identity is instead <A>=V E_V+lambda E_lambda-E; omitting the lambda term there would be wrong. Our moment target is strictly lambda=0.

X is uncentered. Its spectral measure includes any elastic mass sum|<O_ab>|² at energy0. The L2 source means vanish to numerical precision, but this is not assumed on arbitrary components. Calling the quotient an upper bound on a positive excitation requires removing elastic mass or proving a suitable symmetry. It never proves a pole or a gap equality.

## Fixed exact finite test and adverse evidence

The independent coordinate reconstruction has864 states and6912 directed geometric moves. All six source values agree with the actual producer on every state. All864 diagonal and6912 off-diagonal entries are covered at14 frozen(V,lambda) pairs: V=.95,1 and lambda0,±.005,±.01,±.02. Column sums, positivity, branch bounds and bP=G' hold within declared floating tolerance. Eigen-residual and physical/restored mixed-energy checks pass. These are floating matrix computations, not certified interval enclosures.

Final check.py executes59 named groups in1.206seconds,132.47MiB. Full raw state/face/move/nf/O/X dictionaries and all source rows are retained. The first run failed because the RK all-ones ARPACK starting vector was already an exact eigenvector; original source/stderr are preserved. A deterministic nonconstant starting vector replaced it without changing any physical or numerical target. Three actual temporary source mutants fail mathematical assertions: omitted shift restoration, old unsourced branch, omitted staggering. Mixed-versus-pure and unsafeguarded-acceptance discrepancies are separate direct adverse controls, not additional mutant runs.

At V=.95,lambda0:

 E=-.4027365059097320,
 <X>pure=2.435242126009581,
 <X>mixed=2.467333608642005.

Therefore simply substituting the old mixed X is materially wrong. The centered source derivatives are:

|h|energy derivative|error versus pure X|
|---|---|---|
|.02|2.435318758461581|7.6632452e-5|
|.01|2.435261283057360|1.9157048e-5|
|.005|2.435246915205052|4.7891955e-6|

At RK the exact pure value is2.5 and the corresponding errors are8.52393e-5,2.13088e-5,5.32714e-6. Concavity of the lowest eigenvalue, as an infimum of affine Rayleigh quotients, gives forward/backward secant brackets for E_lambda. The h=.02,V=.95 bracket is[2.4251045208,2.4455329961]. Floating endpoints are not certified bounds.

Combining the already frozen V-centered step.02 with source steps.02,.01,.005 gives moments1.6642623381,1.6643016169,1.6643114362 versus pure1.6643330523. Every step is retained; none is selected after observing stochastic precision. The deterministic normalized G' evolution from20 RK sweeps and the last40-of80 projector window differs from its stationary physical energy by at most5.0e-15 over the14 cases. This removes a finite-fixture infinite-population window bookkeeping discrepancy, not population-control bias.

## Practical uncertainty and remaining obligation

For a source step h, T_h=[E(V,h)-E(V,-h)]/(2h). Energy errors are amplified by1/(2h). The known shift is subtracted/restored exactly algebraically, but this does not reduce stochastic covariance by itself. Both source signs and neighboring V energies should be paired by independent replica index; all same-replica covariances must be retained. If B_h is the kinetic response and T_h the structure response, the ratio influence is (qhat²/Vol)/meanT times [B_r-meanB-(meanB/meanT)(T_r-meanT)]. A zero or negative denominator must remain a failure. No forward ancestry is required by this identity, but source finite-difference bias, finite-population bias, finite burn, covariance and ratio error remain.

This is a viable exact finite-source mechanism and a new positive transition law. Practical precision has not yet been tested. The most consequential next obligation is independent review of an implemented tilted branch/weight kernel and a fixed paired stochastic protocol; the old producer review cannot cover that new kernel. No larger-volume job or stochastic pilot is authorized by this note.

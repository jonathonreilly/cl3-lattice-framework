# Exact finite-projector residual oracle and first calibration gate

The literal L2 binary graph was reconstructed independently, preserving all24 geometric face labels and6912 directed moves on864 states. No prior oracle arrays or analyzer were imported. The six real transverse Fourier sums use O=s/sqrt32; X1=sum s²/32. Integer B=480G at V=19/20 and B=24G atRK allows exact powers without eigensolvers or floating errors. Decimal summaries are rounded displays of retained exact fractions.

For k=n/2 propagate v_a=B^k NF^a, a=0,1,2. For endpoint powers a,b and midpoint monomial NF^r X1^s, the exact moment is

 (V-1)^(a+b) sum_i v_a(i)v_b(i) NF(i)^r x32(i)^s / [32^s sum_i v_0(i)^2].

Expanding Eavg=(hL+hR)/2 supplies every mean and all36 raw crossmoments of (NF,X1,Eavg,hLhR,X1Eavg,X1²). This is the full single-path joint covariance, not six independent error bars. A separate direct quadratic form with each integer Fourier vector verifies R=D+correction; the endpoint covariance is not used to define that direct R.

| n | Var(H) | R-D | D | R relative to Epsi |
|---|---:|---:|---:|---:|
|2|0.0076614871|0.0395121511|1.6108011929|1.6503133440|
|48|0.0000216007|0.0017483620|1.6609933300|1.6627416920|
|192|3.27829e-11|2.01816e-6|1.6643290887|1.6643311068|

At V=1 every endpoint h is identically zero: E, VarH, XE and correction vanish exactly for all three lengths, while D=R=8/5. This is an exact zero control, not a small numerical tolerance.

## Prospective first stochastic calibration recommendation

Use n=2,V=.95 plusRK zero control first, with unchanged observable definitions. Before production, freeze two distinct gates: (i) truth consistency |estimate-oracle|<=4 reported independent-chain SE; (ii) nonzero residual and VarH precision, reported SE<=25% of the corresponding oracle magnitude. Require finite positive X; do not clip negative VarH estimates. Report both gates separately and retain failed estimates. For RK require exact zero endpoint observables and derived zero residual in the implementation, rather than a relative-SE test around zero. A passing finite gate is not a mixing theorem.

The exact single-path delta-method influence variances imply IID reference sample requirements of about46 and87 for25% relative SE of correction andVarH atn2. Atn48 those are about9699 and6.09million; atn192 about7.23billion and2.64e18. These are asymptotic independent-draw benchmarks, not proposed MCMC lengths or assurances of precision. Reptation autocorrelation and chain initialization can greatly increase cost. This quantitatively exposes subtraction noise: a mathematically exact endpoint energy-variance identity can become statistically useless at long projection even while its correction tends to zero.

The initial checker had a syntax-only missing-space failure before execution; BEFORE_SYNTAX_FIX.py preserves it. Corrected run24 guards passed in0.374s17.92MiB. No stochastic production or old production rerun occurred. Independent review remains required before these oracles become production acceptance authority.

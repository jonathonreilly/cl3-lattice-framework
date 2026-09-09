# Four-solve implementation readiness, unlaunched

The actual CG recurrence passes the fixed 64-dimensional diagonal test with independent exact-dyadic residual certificates at 16, 32, 48 and 64. Exact solution error is bounded separately. Nonpositive curvature, recursive-zero breakdown and the fixed 256-iteration cap fail closed. This is a small solver control, not a native spectral or convergence result.

The actual worker dataflow is separately exercised with a 16-entry synthetic operator and injected solver. The two controls have distinct scopes. No physical L6 CG was executed.

Four representatives, two assembled sources and final chi retain NPY and lossless little-endian complex raw files. First representatives have real phase; sources, second representatives and chi have global phase i. The RESULT includes the full partial manifest, representative certificates and source Bhat/Berr. Intermediate checkpoints remain NPY with certificate sidecars. Final Echi failure writes RESULT and then fails the job; exceptions preserve completed PARTIAL records.

The fixed candidate schedule is zero start, no preconditioner, at most 256 iterations per solve, certificates every 16 iterations. Recursive-zero before a certificate is a retained breakdown, not a guarantee of convergence. No replacement or automatic retry is implemented.

Full execution remains disabled without a separate reviewed CONTRACT. The prospective 1800-second budget must include 1088 maximum operator actions, 128 checkpoint norm scans, source/final operations, 27 transports, conversion and output, FP checks, startup and independent replay. A 400-second independent replay reserve is proposed, not yet demonstrated sufficient. The dedicated vector-cost micro is immutable and root-run; its result is pending. No complete resource or launch readiness claim is made here.

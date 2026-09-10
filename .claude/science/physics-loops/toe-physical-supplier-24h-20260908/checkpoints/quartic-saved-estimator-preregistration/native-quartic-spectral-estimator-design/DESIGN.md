# Quartic estimator for the unchanged degree-two Ward trial

This source-only proposal changes a residual error certificate. It does not evaluate a native moment or import any pending high-moment output. The exact saved degree-two p, constant q, signed nominal, source residual and trial norms remain unchanged. The majorant claim imports parent proof877664 and independently derived proof1500245, both pinned. interval.py is an unchanged copy of the existing reviewed spectral interval arithmetic.

## Majorant and fixed schedule

For positive delta,t,u, form P(x)=(x-delta)(x-t)^2(x-u)^2, B=1/(delta*t^2*u^2), A=B*(1/delta+2/t+2/u). The code convolves exact rational polynomial coefficients and checks that the constant and linear terms of1+P(x)(Ax+B) are exactly zero before returning the degree-four quotient. For x>=delta, its difference from1/x^2 is P(x)(Ax+B)/x^2>=0. Coincident contact points are allowed. No optimizer or spectral upper cutoff is assumed.

The only contact set is the parent-selected {1,2,4,8,16}. Its15 lexicographically ordered unordered pairs with repetition give30 candidates per P/O choice,60 across the two original modes. Coefficient vectors are cached immutably and shared. They are exact certificate parameters, not approximate solutions of an optimization problem.

## New arithmetic and inherited quantities

For each unchanged quadratic p define v=(1,-p0,-p1,-p2). Compute the seven exact coefficients of v*v once (16 rational products). The accepted old r2 is rho0 and is NOT recomputed. The only new residual contractions are rho_j=sum_l(v*v)_l m_(l+j), j=1..4. They need m0..10: original m0..6 plus future accepted m7..10. The bound input boxes must describe the same D, class, units and physical scalar family. Higher precision or a different parameter midpoint does not silently redefine that family.

Every majorant expectation scales the FULL original rho boxes by its signed coefficients. Negative coefficients use the lower moment endpoint for the upper sum. A negative certified upper is a discrepancy and refuses; it is not turned into zero. Nonnegative norm premises justify intersecting a lower bound with zero. Take the minimum of these upper bounds and a prior bound for the exact SAME degree-two p, including its own rho0/delta^2. A previously computed degree-one spectral estimate is ineligible, even if its numerical value is smaller.

For h=1, delta=1/4 and ||J||=sqrt8, use each class's unchanged accepted t2=||b-qDb||^2. The new first bound u gives v=(sqrt8*u+sqrt(t2))/delta. Then E^2=12u_P^2+3u_O^2 and F^2=12v_P^2+3v_O^2, using outward roots throughout. The coupling term is essential. No s3/s4 or new mixed kernel is acquired; accepted s0..2/q remain provenance dependencies of t2 rather than being recomputed.

The posterior uses the SAME accepted aggregate trial norms a^2,b^2 and nominal, with X=4sqrt15,V=32sqrt30. It evaluates6[E(a+chi)+min(Eb+chi F,E psi+aF)], chi=min(X,a+E), psi=min(V,b+F). It divides the resulting nominal enclosure by8, intersects with the old interval for the same trial/state/unit/nominal, and refuses if the intersection is empty. A runtime refusal must retain the old certificate as historical evidence, not report a new successful result. No sign improvement is promised.

## Interface, persistence and missing bindings

core.evaluate accepts only already-decoded inert descriptors, not paths. Per P/O row it requires eleven moment boxes, three exact p coefficients, inherited r2,t2 and same-p first-squared upper. Separate arguments are nominal, old alpha interval and the two aggregate trial norm boxes. q and source moments are not numerically re-evaluated; their exact saved identity must be authenticated by a future binder.

The callbacks emit convolution, four raw rho boxes BEFORE nonnegative gates, inherited first bounds, all15 raw coefficient/expectation candidates BEFORE upper checks, per-class first/F bounds, and posterior values BEFORE intersection checks. There are45 core events per choice,90 for both modes. The successor worker retains the supplied packet first, then persists these callbacks synchronously with a current-stage record and preserves failures. PROTOCOL.md documents its separate filesystem and once-dispatch contract.

BINDING.json now pins accepted original degree20, its posterior, and the new high-moment result/receipts. Execution remains false. No scientific input was parsed during preparation: only metadata and file hashes were read. The exact actual source-family and same-trial predicates are implemented in loader.py. The new strict dispatcher and full synthetic worker controls are described in PROTOCOL.md; no authorization exists.

## Bounded source cost

Across both modes and both classes:64 exact convolution products;112 NEW signed moment terms (rho0 inherited);300 signed envelope terms. The15 shared quotient polynomials use600 polynomial convolution products plus a small fixed number of A/B operations. The implemented code uses22 directed square-root calls for both choices, independent of the15 contacts. Source callbacks retain90 compact events; the separate worker emits97 events and8 success files as specified in PROTOCOL.md.

Stored rational endpoints have the copied32,768-bit cap. Binary rational operations are checked after each step; transient numerator/denominator products and additions, including the128-bit square-root grid checks, are bounded by131,072 bits. This permits a bounded refusal if unrelated denominators produce excessive growth; it is not a promise that prospective interval widths or costs pass. At these input lengths the future textual parser also needs an explicitly reviewed combined numerator/denominator token limit, not a guessed decimal limit.

A prospective30/29.5/29 second,384MiB wrapper is recorded only as an unaccepted candidate in RUNTIME_PLAN.json. These hundreds of arithmetic terms are much less work than mixed-kernel acquisition, but full transitive hashing, parsing, persistence, and exact input widths are unmeasured here. No observed timing or resource guarantee is inferred. The implemented dispatcher remains disabled pending independent root review and remote preregistration.

## Independent synthetic scope

check.py uses a fabricated three-atom positive spectral measure and a fixed rational quadratic p. It compares convolution moments with independent direct evaluation of r(x)^2*x^j, checks all15 coefficient vectors against elementary symmetric formulas, checks pointwise factorization/positivity, signed endpoint containment, positivity refusals and an inert full posterior. All96 checks pass with zero native values. A provisional half-shifted contact grid and aggregate-F source are preserved as PRE_PARENT_GRID files; the final parent grid and channelwise formula were rechecked. This is a source/control result, not a native Ward certificate.

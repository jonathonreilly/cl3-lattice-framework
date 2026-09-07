# Independent six-mode exterior-spectral quench witness

The implementation and 32 raw rows were frozen before opening the root full-Fock source or its JSON. Independent source SHA: 515cb0a38a4b98d2ce7d46a961ddf3403bb30db4b33dec3adc5090f7113b9a63. Raw SHA: 98b0688a6b3737a39c91d4401bd4962908734c8714797e571944ede87a491af6. Files check.py and results.json are beside this memo.

## Independent route and result

Only 6x6 one-particle matrices are allocated. For W=E†ER, functoriality of exterior powers gives Gamma(E)†Gamma(ER)=Gamma(W). Its eigenvalues are every subset product of the six eigenvalues of W, including the empty product. Therefore the full-Fock norm difference is max_S |1-product_S lambda|. For Hermitian G=ER†h_ext ER-h_ext, the spectrum of dGamma(G) is all subset sums; its norm is max(sum positive eigenvalues, minus sum negative eigenvalues). Neither calculation constructs a 64x64 Fock matrix or imports the root checker.

All 32 keyed cut/time rows agree with the independently authored root full-Fock witness. Maximum residuals: echo norm 2.220446049250313e-15; global energy drift/defect norm 8.881784197001252e-16. Both factorial bounds agree exactly numerically. Geometry gives m=1,2,2,infinity for cuts [], [1,3], [0,1,3], [0,1,3,4]. This is one plus the distance from a seed endpoint to an omitted hopping endpoint in the remaining graph. The graph has d=2 and maximum hopping t=1. All rows obey min(2,4 Tail_(m+1)(2|tau|)) and min(4 Tail_m(2|tau|),8|tau|), respectively. The complete-cut errors vanish up to floating point roundoff.

## Cold review of root source

No mathematical defect found. The CAR construction, echo order, whole-hop truncation, and derivative sign are consistent. The differentiated expression -i ER'=ER(HR+he)-HR ER reduces the full energy defect to [Hext,ER]; multiplication by ER† produces the Hermitian drift. Its norm equals the defect norm by unitarity. The feedback diagnostic correctly evolves J in the interaction picture instead of treating it as a constant postfactor. My independent numerical comparison covers complete echo and energy norms, not the feedback norm, whose formula was checked algebraically.

The `checks` counter counts actual calls of close(): 36 CAR relations, one full number check, four truncated number checks, and four close checks per time/cut, totaling169. The additional 96 echo/feedback/energy bound assertions are not counted, so there is no inflation. The CAR relation count is not itself advertised as exhaustive testing of every CAR axiom. close() explicitly rejects nonfinite residuals; a NaN error in a bound assertion also fails its <= comparison. Defaults permit NaN in JSON serialization in principle, so allow_nan=False is sensible portable hardening, but no nonfinite value occurs in this receipt. Runtime starts after imports, as in the other witnesses. Full64 Fock is accurately scoped as CAR, not an ambient native edge-code simulation.

## Rational conditional resource certificate

Exact arithmetic independently gives coefficient 3+2(10/7)*3*(10/3)=221/7; at delta=1/320 its trace upper bound is221/2240<1/10 and mean-energy upper bound 3delta+2delta^2=481/51200<1/100. The upper surrogates satisfy (10/7)^2>2 and (10/3)^2>(22/7)^2+1. Cap97 divided by spacing1/320 gives31040 bins/levels under the stated discretization convention, requiring15 storage qubits. The supplied finite-device register inventory12+12+8+15+1 totals48.

This verifies the arithmetic of the declared conditional safe-cap finite-ladder recipe. It does not independently prove the safe-cap comparison theorem from this script, does not simulate a48-qubit device, and does not include reservoir storage, preparation, controls, locality implementation, or a positive-half-line extension. The certificate's source/scope text makes that distinction. If a later implementation uses endpoint-inclusive point samples rather than bins, its count is31041; the15-qubit and48-total storage bounds are unchanged, but M must retain the declared convention.

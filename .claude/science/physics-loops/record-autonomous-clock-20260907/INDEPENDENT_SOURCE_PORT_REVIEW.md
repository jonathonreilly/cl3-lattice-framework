# Independent clock/boundary source and port review

Read-only2026-09-07 review of both notes and three scripts in /private/tmp/toe-clock-campaign-20260907, compared with immutable staged originals in primary/native scratch. This reviewer did not author the clock construction or boundary theorem. All three script diffs against their staged originals are empty. No source edits or duplicate canonical cache run performed.

## Verdict

PASS at the explicitly conditional scope; no blocking mathematical or port defect found. The ready-input/reference extension, joint versus discarded clock bounds, full-register norm distinction and fixed-chain global-commutant quantifiers are correctly stated.

## Clock proof

The D gauge is unitary on the18-position one-hot sector, and actual all-input native pulse unitaries give D(Hpath tensorI)D†. Full [Uj,K]=0 justifies both [D,K]=0 and the retained exp(-itK) factor. This is stronger than the earlier state-specific pulse path and is not silently inferred from that weaker example.

The virtual17-spin symmetric-subspace calculation gives the exact binomial amplitudes and the17-step perfect-transfer phase. Virtual spins are a derivation, not a missing extra apparatus allocation. Identity padding makes every j>=9 prefix the same completed isometry on the entire ready input subspace.

For any purified ready input, the reference completed-clock vector is supported only on those finished positions. Its overlap with the actual output is exactly sqrt(1-eta), including arbitrary external reference entanglement. The joint pure trace-norm distance is consequently2sqrt(eta), and convexity/purification bounds the restricted input-map diamond norm. This does not grant arbitrary initial-clock inputs. Tracing the clock produces a genuine mixture of prefixes: its unfinished total weight eta gives the sharper2eta channel bound. No outcome postselection or physical renormalization occurs.

Markov's bound on missing clock steps gives eta<=17pi²/360000 at the stated window, strictly below1/2000. Thus2sqrt(eta)<1/20 and2eta<1/1000. The recurrence at2 undoes the circuit up to original free evolution. The source explicitly declines permanent Record formation and renewal.

## Resources and interactions

27 means9 reduced native plus18 physical one-hot clock qubits; the one-hot computational sector has dimension18 but no logarithmic clock compression is assumed. One-hot ||Hc||=17pi/2 and ||K+Hc||<33 do not bound the entire27-qubit Hilbert space. The source separately supplies the natural Hermitian clock-exchange extension, preserving excitation number and K, with sum-of-edge-norm bound<255 and total<261. Each clock-edge/native-unitary Hermitian term has support at most5 sites. The global one-hot projector is not required for this extension. These are supplied engineered multi-site couplings, not nearest-neighbor gates or axiomatic control primitives.

The bound on K by11/2 is consistent with active energy up to2 plus four-level battery maximum7/2. Clock observation within the completion window remains a timing condition even though the nine external switching pulses have been removed.

## Connected-chain proof

On the full Fock space, an even operator in the initial-segment CAR algebra maps to a spin operator supported on that segment. Exterior I,X,Y coefficient independence forces commutation with both endpoint Pauli generators when the boundary hopping is nonzero. Matrix-algebra commutation then factors identity on that site, and induction strips the whole prefix. Battery factors remain arbitrary until the final [B,HB]=0 condition. Hermitian and anti-Hermitian decomposition correctly handles non-Hermitian O.

The strict support, proper prefix, connected fixed hopping and full-operator commutation hypotheses are explicit. The theorem does not prohibit a fixed-input energy-preserving orbit, fuel-switched sector maps, approximate energy locality or full-support operators. Zero hoppings break the stripping premise as the severed contrasts demonstrate. Arbitrary battery degeneracy affects only its final commutant. The spin-tensor/onsite-Z extension is explicitly analytic rather than silently counted as the frozen even-CAR numerical ansatz. No graph-general zero-forcing theorem is inferred from the chain.

## Numerical/source coverage

The primary clock revalidates163 native exact assertions; its37 clock assertions and18x18 matrix computation are separately reported. The helper revalidates62 native isometry checks, builds the4608-dimensional sparse clock/native matrix with the fixed old sentinel folded, and performs56 distinct clock checks including all8 ready columns and their144-column gauge embedding. This supports the all-input identities but is not a measured diamond norm or2^27 simulation. The boundary runner's356 assertions concern full rational finite bases and fixed contrasts. The notes do not inflate these into continuum or all-graph numerical coverage.

Minor nonblocking robustness observation: primary clock close() rejects a NaN residual through the e<tol test, although it does not call isfinite explicitly; comparison is safe. Native parent import/revalidation is disclosed, so no independent rebuild of all upstream carrier algebra is claimed. Root owns ongoing canonical cache and pipeline validation.

# Propagated L4 fixed-study result

All 32 fixed shards completed successfully: four arms, 16 independent chains per arm, 32n measured updates per chain. Production wall time 721.756460 s; charged total including the original micro 722.088382 s. Maximum shard 39.177913 s; maximum reported RSS 34.437500 MiB. No replacements, additional arms, or source changes during production.

Frozen analyzer status: `passes_limited_diagnostics_not_convergence`. All 8 nominal D precision gates pass; 0 of 18 predeclared comparison flags. These are finite-chain diagnostics, not evidence establishing stationarity, ground-state convergence, or an excitation pole.

| Arm (tau,RK sweeps,burn/n) | h | D ± chain SE | R ± chain SE | correction ± SE | signed VarH ± SE |
|---|---:|---|---|---|---|
| [12, 128, 32] | 1 | 0.756878503 ± 0.005627 | 0.758164213 ± 0.005596 | 0.00128571 ± 0.0004654 | 3.81781e-05 ± 0.0002319 |
| [12, 128, 32] | 2 | 1.44435311 ± 0.01062 | 1.4435192 ± 0.01069 | -0.000833906 ± 0.00057 | 3.81781e-05 ± 0.0002319 |
| [12, 512, 32] | 1 | 0.740580248 ± 0.006069 | 0.740254404 ± 0.006262 | -0.000325844 ± 0.0004179 | 0.000269347 ± 0.000215 |
| [12, 512, 32] | 2 | 1.42360878 ± 0.01063 | 1.42316455 ± 0.01083 | -0.000444229 ± 0.000573 | 0.000269347 ± 0.000215 |
| [36, 512, 8] | 1 | 0.735140386 ± 0.006397 | 0.735123989 ± 0.006441 | -1.63972e-05 ± 0.0002867 | 2.30384e-05 ± 0.0001329 |
| [36, 512, 8] | 2 | 1.42362608 ± 0.0147 | 1.42380418 ± 0.01465 | 0.000178092 ± 0.0002784 | 2.30384e-05 ± 0.0001329 |
| [36, 512, 32] | 1 | 0.752563927 ± 0.006543 | 0.753079159 ± 0.006673 | 0.000515231 ± 0.0002879 | -0.000243683 ± 0.0001396 |
| [36, 512, 32] | 2 | 1.43035092 ± 0.008914 | 1.43052569 ± 0.008826 | 0.000174764 ± 0.0003716 | -0.000243683 ± 0.0001396 |

All 8 residual-resolution and variance-resolution classifications are indeterminate. Arm D has negative signed VarH, retained without clipping; its bound plugin is null. Positive plug-in variance values in other arms are also unresolved and do not provide certified bounds.

Original-tag fractions are zero in arms A, B and D. Arm C ranges from zero to 0.004319932725694444; every chain remains below the predeclared 1% flag. This checks survival of the original path labels, not forgetting of all initialization effects.

R and Epsi identities refer to the stationary product-G path measure. The propagated initializer samples a finite RK start followed by product Q, not that equilibrium path law. Until stationarity is established, the measured ratios and cross moments are diagnostics rather than exact Rayleigh quotients of an inferred state. Lack of flagged differences is not convergence; no L4 exact oracle exists here.

The original failed constant-path L4 study remains untouched. This prospectively specified propagated-start study reduces the observed original-tag retention and avoids the previous large disagreements, but does not prove a causal decomposition of all earlier bias.

Full chain vectors, 16 within-chain batches, acceptance counters, accepted-run histories, initial-tag replay data, signed moments, chain influences and estimator covariance are retained in raw shard JSON and ANALYSIS.json. Batches were not treated as independent replicas.

Provenance: freeze d666579d4f33c95a8a1835852c54e7bf28b7f8eadd285c9629034bba8bba4c66; independent review fe1f7bb43066e430fe88804734cb2ec4693f83d4035e111ebd21157cb6580689. Earlier freezes, the integrity-repair evidence and exact cost-micro producer are preserved.

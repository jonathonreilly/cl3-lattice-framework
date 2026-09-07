# #8007 independent source review — changes required

**Verdict: FAIL pending three narrow corrections.** The conditional multiplier, insertion and Perron-sign arguments survive this review; the executable numerical evidence and packaging do not yet meet the current source contract. No audit was run or status applied.

Frozen live PR #8007 is OPEN and non-draft at `9450957fc039bf362bd2ca3d71d301d35d55cf40`, branch `codex/native-wilson-second-order-block10-20260907`. The reviewed selected candidate is tree `680b425872ec1b0353d744e5b349ba90842b88ba` on landed main `b9653d0ead5bbd2058beaa4d7ceb3785f1cfac92`; source patch SHA-256 is `f2de867431ec52976e31ccde6c6f744ebf6e378dcc54c6ce895052a427a50995`.

## F1 — P2: register the complete sibling set in both real consumers

`docs/audit/scripts/build_citation_graph.py:154–157` adds the multiplier claim's quadrature and killed-recurrence siblings. The corresponding registry in `scripts/audit_packet_script_deps.py:47` has no entry. Calling the actual `helper_runner_paths_for_claim` APIs on the complete candidate returns those two paths from the graph consumer and an empty set from the diagnostic consumer. The primary is self-contained, so import traversal cannot recover these siblings. Restricted source packaging can therefore omit the very evidence being asserted, despite the graph apparently carrying it.

Add precisely the same complete two-path registration to the diagnostic consumer; preserve every existing key, value and function. Confirm both actual APIs and missing-source controls on the exact final candidate. The source-omission issue is discovery only; none of the five runners secretly imports these siblings. INPUT_CLOSURE.json records the exact paths and both observed results.

## F2 — P2: make the named numerical falsifiers discriminate their scientific targets

The quadrature runner's lines 13–35 calculate W2, v and residuals, but its assertions check only finiteness, a positive denominator, endpoint window and agreement of two quadrature orders. The recurrence runner's lines 44–49 compute the endpoint, coefficient and residual without asserting their agreement. Its other checks protect the walk/rate/tail/resources, not the coefficient. The source note lines 140–148 and historical QUADRATURE_PREREG.md describe a coefficient falsifier, including W2−W as a deliberate discriminator.

Actual one-edit copies of the canonical source, executed with the same cases, produce these results:

| Mutation | Result |
|---|---|
| Quadrature denominator multiplied by six | exit 0 |
| Quadrature numerator sign reversed | exit 0 |
| Quadrature W2 replaced by W2−W | exit 0 |
| Recurrence W2 replaced by W2−W | exit 0 |
| Recurrence x omits its rho shift | exit 0 |

These are genuine false negatives for the advertised witnesses. At β=1024 the sign-reversed quadrature still passes with a scaled residual around −34030.8; the denominator error passes around −14179.5. At β=512 the omitted endpoint shift passes around −837.0. Conversely actual wrong native-rate, primary differential-normalization and sign-trace-constant mutations are rejected, demonstrating that the harness can detect relevant failures. All eight edits, source hashes, exit codes and outputs are preserved in MUTANTS.json and mutants/.

Add actual finite scientific comparison assertions with justified, explicitly scoped tolerances or independent reference construction; verify normalization, the actual shifted endpoints, and the frozen coefficient/declared alternative. The existing subthreshold β values remain numerical diagnostics, never certified applications of the β≥2048 theorem. Do not fit the theorem or its constants to these data, and do not invent interval certification. Run the actual wrong-normalization/coefficient/shift controls against the corrected source and report rejection.

The quadrature default/cache output also contains only scope labels, although the note says every numerator, denominator, v and residual is reported. `--json` has those values, but the canonical fresh-looking cache does not. Retain the substantive numerical result in the normal executed/cache receipt, and update affected scope/count language honestly. Preserve the original historical JSON/spec/cache receipts as dated provenance where required; refresh affected canonical caches after the final source and any actual input declarations are frozen. This is part of repairing the evidence witness, not a new theorem.

## F3 — P2: remove canonical draft framing

`docs/NATIVE_GAUGE_TRANSFER_WILSON_SECOND_ORDER_MULTIPLIER_BOUNDED_THEOREM_NOTE_2026-09-07.md:33` still begins “Draft bounded theorem”. Current review-loop SKILL.md:1028–1034 expressly blocks long-lived draft/branch framing from repo-facing source. Replace that phrase with neutral canonical theorem/proof wording while retaining conditional-support, the exact native premise, and unset audit status. No grade promotion or rewriting of historical drafts is warranted. A narrow dated correction receipt can distinguish current reviewed source from the packet's preserved earlier snapshots and statuses.

## Full scope, provenance and preservation

All 79 raw authored paths are mapped individually. The original head `2558f2efa0c05021cfc91eb6eb5cb389e9910517` has actual base `a8f84aaad75fdcb790ba6ba094e4275e237d9a5a`. The latest raw head's actual base against its recorded base is `e043c95b37bd46d80e97c39f36c8b3cb7643c62f`. All objects were available after an ordinary branch fetch. The intermediate `93b701e8...` changed four historical publication bookkeeping paths. Subsequent actual commits merged current-main inheritance and adjusted the generated manifest; their complete per-path movements are recorded, not inferred from PR titles or shallow ancestry.

The selected unit contains 78 paths: three notes (408 lines), five canonical runners (283 lines), five canonical caches, 64 historical packet paths (1,901 lines), and one additive graph registry change. It excludes the raw generated manifest. All 77 other selected paths are exact raw-head bytes/modes. Only the new registry literal was ported onto current main; raw inherited tool/parent/planning files were not copied. All 28,292 current-main paths are preserved, except that one additive literal registration; there are no deletions. The 28,369-path candidate tree and full raw/main union have explicit content/mode dispositions.

The five runtime modules are self-contained, importing only the standard library and numpy/scipy/sympy. Their only mutable file reads are their own source hashes. There are no omitted runtime helpers or data files and no transitive #8006 input. The two actual proof parents are the September 2 reflection/heat-sandwich note and the representation-ring recurrence note; both were fully read, byte-bound to current main, and unchanged from the prior base. The former's old finite support executable is not invoked or used as proof authority here. No ledger grade, old pipeline PASS, historical review label or Nyström number supplies a premise.

Exact frozen reserved scopes #6379/#6858/#6859 have no intersection with selected source or actual proof premises. Full selected prose and runtime/proof closure also introduce none of that reserved content. No unavailable ancestry is interpreted as negative reachability. Root's new arrivals and other moving PRs remain outside this unit.

## Executed checks and complete lenses

All five canonical `--json` runs succeed on b965, taking approximately 0.056, 0.040, 0.934, 0.434 and 1.424 seconds. The four counted runners execute 96 checks total (26, 9, 14, 47); quadrature separately completes all twelve declared meshes. Historical caches are identity-fresh under the actual current cache API. Five actual source changes in isolated cache fixtures become `sha_mismatch`. All selected structured JSON parses without duplicate keys/nonfinite constants.

The independently written mathematical control performs 24 exact symbolic/rational/combinatorial checks, including 1,053 exact killed/reflected walk comparisons. It derives normalization and denominator correction, W2, the heat solution, chamber integrals, the legitimate Rayleigh quotient and sign margins without importing candidate modules. PROOF_REVIEW.md records the analytic remainder, topology, dense-range and perturbation arguments and their limits.

- **CodeRunnerReviewer:** changes required for F1/F2; complete runtime closure otherwise found, all actual runs/results and surviving controls disclosed.
- **PhysicsClaimReviewer:** conditional native mathematical claims supported; no physical bridge or TOE closure supplied.
- **ProofObligationReviewer:** displayed multiplier/insertion/sign obligations closed within the declared setting; overall physical scope CONDITIONAL, no equivalent-gap result disguised as closure.
- **ImportSupportReviewer:** exact current-main proof parents explicit and read; no runtime input omission, numerical support never proof authority.
- **NatureRetentionReviewer:** BOUNDED conditional mathematical source, not a retained-status decision or publication/physical sufficiency grant.
- **NoGoDisciplineReviewer:** N1 honestly one family, N2 related supplied inputs without independence claim, heavy packet explicitly NOT PASS; constructive results and remaining walls separated. No additional actionable N1/N2 defect.
- **LabelingConventionReviewer:** F3 requires neutral canonical language; conditional and unset audit labels stay intact.
- **RepoGovernanceReviewer:** current-main source preservation passes, complete graph/diagnostic parity fails F1; no raw tower or generated verdict import.

The five passing originals cannot override the observed false-negative controls. Corrections should be returned to this same reviewer session with the complete final source/input/cache map, the exact correction diff and full path dispositions. Re-review can focus on those affected assertions, caches, labels and registration functions while reusing these unchanged proof/source reads under verified hashes. No whole-unit restart, full pipeline, formal audit, push or PR action was performed here.

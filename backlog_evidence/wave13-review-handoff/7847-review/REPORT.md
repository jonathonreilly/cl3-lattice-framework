# Independent original-source review of #7847 carrying #7846

**FINAL VERDICT: FIXES REQUIRED.** One P1 and five P2 findings below apply to the exact original source at #7847 `3c375f8cfa2b3423cd80974a2fa075f3b8b9824d`, carrying #7846 `26209dd0d09a58dc5a4fb21358968d4acefb5885`. This is a scoped mathematical/source review, not an applied audit or retained-status decision. No scientific source was edited.

The general binary-qubit CP repeatability proof, orientation distinctions, finite grading/capacity obstruction and positive even-code/typed-algebra constructions survive the review at their stated conditional scope. The proposed conditional-probability theorem has a missing domain hypothesis. The source packet also omits an actual runtime dependency and fails on current main's archived comparator path. Several broader claims need narrowing to the proved local objects.

## Exact source and coverage

The review worktree is `/Users/jonreilly/Projects/Physics-worktrees/review-backlog-7847-20260907`, based on `7887b4481feae2800c04c7c42ddac9554f2c2b9f`. Its 36 additions are exact original blobs. The remaining four inputs are exact existing main sources, including the Cycle20 comparator at its **archived** path. The external `original-source/` snapshot preserves all 40 original paths, including that comparator's old path, solely to replay the original layout. These are different execution layouts, explicitly distinguished below.

Preparation's complete original/base/inherited maps are reused and hash-bound in `PREPARATION_MAP_BINDING.json`; no raw-ancestor search was repeated. #7846 contributes 14 additions and #7847 contributes 16, with no original moves or deletions. All 30 remain represented: two notes, the proposed decision memo, two runners, two historical caches and 23 historical packet bodies. The closure adds B38 and B37 helper modules plus eight premise/proof/comparator documents. `FINAL_40_PATH_DISPOSITIONS.json` records every path, mode, blob, SHA-256, actual review location, origin and disposition.

All 30 original bodies, all eight proof/comparator documents and all 2,157 lines of B38 were read. For B37, the complete used rotation/Gaussian/PIT/Haar functions, their prerequisites, and all module/class initialization statements were inspected. An actual call profile confirms the bounded runtime closure. B37's other function bodies and the independent B37/B38 `main()` campaigns are **not** accepted by this review. Their unused CTMC, archive-induction and broad parent obligations remain unselected. Reading their complete note bodies as context does not silently close #7824–#7827 or import their entire towers.

All 23 original historical packet bodies were read and remain immutable. Their pre-execution predictions, initial sign-twin failure, post-execution novelty corrections, old shipping labels and old N1–N8 claims are historical evidence, not present acceptance. In particular, Block42's original full typed sign-twin expectation stays falsified; it must never be restored by a correction.

Fresh read-only GitHub metadata confirms #7847 remains open, non-draft and at the frozen head. Main later advanced to `66b1b4f8a964f4011a3f4e7876369b7daf8e1834`; its 23 changed paths have zero overlap with these 40 actual inputs. `MAIN_PRESERVATION.json` binds this disjoint advancement and verifies no tracked review-base changes. The reviewed source base remains `7887…`.

## Findings

### F1 — P1: calibration may be vacuous at the states used to prove the Born conclusion

**Locations:** B42 note lines 180–185, 242–255, 264–268 and 342–351; decision memo lines 17–25, 32–37, 56–67 and 85–87; B42 runner lines 867–919. The long B42 filename is recorded in the scope inventory and `FINDINGS.json`.

The clause calibrates an eigenpreparation only **if** `Pr(F|C,rho)>0`, and conditional affinity applies only where the laws are defined. The proof then assumes both eigenpreparations are eligible and treats the response as a bounded affine probability on the complete density-matrix domain. Neither step follows from those clauses.

For a fixed context let `x=Tr(P rho)`, and set `f=Pr(F)=4x(1-x)` and `h_P=h_Q=f/2`. Both endpoint preparations have zero formation probability. On the entire eligible domain `0<x<1`, the conditional law is the constant affine function `q_P=q_Q=1/2`; the calibration implications are vacuous. The construction is invariant under exchanging P and Q, normalized and nonnegative, but differs from Born at `x=1/4`. A second witness `f=1-x, h_P=0, h_Q=1-x` has even affine **joint** probabilities, valid Q calibration and an ineligible P endpoint, yet `q_P(I/2)=0`. These are exact counterexamples to the written implication, not objections to the usual full-domain affine-effect theorem.

`INDEPENDENT_CONTROLS.json` recomputes both witnesses without importing the candidate. The original runner passes because it inserts the calibrated diagonal `(1,0)` into an effect matrix, without checking whether endpoint calibration can be invoked.

**Narrow repair:** state an adequate eligible-domain hypothesis wherever this implication is used. The simplest sufficient version explicitly assumes a conditional response on every qubit density matrix, with positive formation for that registered ideal context at every such preparation, including P and Q. Alternatively provide and prove an equally adequate domain/extension theorem. Keep arbitrary state-dependent heralded processes outside that ideal-context hypothesis. Preserve the original selection-bias counterexample and add actual rejection of both zero-formation-endpoint witnesses. Carry the condition into the note, decision memo, runner, current claim summary and dated correction receipt; preserve the original historical bodies.

### F2 — P2: the actual primary/helper/proof packet is incomplete

**Locations:** B42 note frontmatter and reproduction surface (no primary runner metadata/link); B42 runner `AUDIT_INPUT_PATHS`, lines 88–108; B42 dynamic import, lines 143–154; B38 `SourceMeasure.normalized`, lines 691–709. Both existing consumer registries have no B42 entry.

Starting from the actual note path, `build_citation_graph.claim_id_from_path` returns `admissibility_sharp_qubit_record_writer_orientation_axiom_decision_bounded_theorem_note_2026-09-01`; `extract_runner` returns `None`. Supplying the actual B42 primary explicitly still returns no helpers through either `build_citation_graph.helper_runner_paths_for_claim` or `audit_packet_script_deps.helper_runner_paths_for_claim`. B42 really imports B38, which imports B37 and calls its Gaussian normalization, PIT and Haar certificates. B37 is absent from B42's current input declaration.

In an external copy, doubling the actual B37 Gaussian coordinate density changes the derived eight-coordinate normalization to **256**, and B38's actual source measure correctly reports `normalized=False`. Yet B42's actual source/preregistration gate still returns PASS, its declared fingerprint is unchanged, and the current actual cache API still reports **fresh**. This is a demonstrated evidence-completeness failure, not merely a desired registry convention. See `ACTUAL_SOURCE_CONTROLS.json`.

The actual citation extraction also yields no source dependencies for either new canonical note or the decision memo. Their use of the current minimal memo and of the typed B38 premise is invisible to the graph. Algebra rederived in the new source need not acquire unrelated parent authority; actual consumed premises must be linked and scoped.

**Narrow repair:** add B42's real primary runner/cache metadata; include B37 in the primary's declared current-input closure; add the exact B38/B37 helper set under the filename-derived claim ID in both actual consumers, preserving all old entries/functions/policy. Bind actual premise links, especially the current minimal memo and the used typed B38 context, with an explicit consumed scope. Keep self-contained comparisons and unselected parent claims separate. Test from each real note path, not an invented ID. Actual missing-helper/alias/source-omission controls must fail, and actual B37 source drift must invalidate the cache. No whole-parent execution campaign is required.

### F3 — P2: B42 fails on the current archived comparator location

**Locations:** B42 runner lines 63–66, 95 and 113–117; `worktree_blob` lines 229–237 and the source loop lines 257–259.

The original active Cycle20 path is absent on current main. Its identical blob `d6d2bda3d5cd8063479270c7ce462e1faee5b660` is preserved under `archive/notes/docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md`. A fresh unmodified B42 invocation on the main-based worktree exits 1 before any check, at `git hash-object` of the old path. The exact original-layout external replay passes 16/0; that does not cure current-layout failure.

**Narrow repair:** read and declare the archived path, while keeping the original preregistration path/blob separately for historical Git verification. Use an explicit historical-to-current path mapping in the worktree-pin comparison. Replacing the historical key indiscriminately would break the original commit proof. Do not restore the old active path or edit the archived comparator. Preserve its stale scalar-Record-additivity claims solely as dated history; they are not current axioms. Refresh only affected final caches after the final source/input freeze.

### F4 — P2: finite local product twins are promoted to complete four-axiom lattice models

**Locations:** B43 note claim_scope, lines 301–339, especially 329–335; runner lines 690–809 and its `current_axiom_product_twins` result label. Related B42 note lines 139–174 and runner lines 738–772 need the same explicit candidate/local boundary.

The executed B43 witnesses are four **supplied typed** carriers, a 729-profile scalar local rule, and 1,458 formation/re-read pairs. They establish shared local number/Record expectations and different odd cross-relations under the supplied products. They do not construct a covariant assignment of matter/Record roles and products over the full lattice. The note itself acknowledges that missing assignment and transition law at lines 381–387 and disclaims a full lattice role law at lines 441–445. Attaching the local table to finite matrices is not the missing proof that both are complete models of all four axioms.

The problem is not that every result needs a global stochastic schedule: Admissibility itself is not a dynamics axiom. It is that this source expressly advertises a complete semantic countermodel pair beyond the constructed carrier/type/law scope. Keyword checks of the axiom sentences and all finite local profiles do not supply the missing extension. B42's two response parameters likewise remain supplied candidate-law comparisons, not an unqualified foundation-level model theorem.

**Narrow repair:** retain the finite algebraic/nonselection result: under the supplied roles and candidate products, the displayed local Record/number data do not distinguish ordinary from graded composition. State that no full four-axiom/covariant lattice countermodel theorem is established here. Update canonical claims, affected gate names/details and the authoritative dated correction overlay. Preserve the positive conditional architecture and all live G/M/D, pointer-only, context-dependent and real-Clifford routes. Do not fabricate a new lattice process to get a preferred verdict.

### F5 — P2: the blanket independent-wall count is unsupported

**Locations:** B43 note lines 430–432; its historical N2 summaries, including `POSTEXECUTION_NO_GO_AUDIT.md` lines 32–47. B42's historical N2 list likewise names distinctions without proving a complete pairwise independence result.

The canonical sentence calls nine items independent and says countermodels change only the named wall. The more careful historical sidecar instead separates four particular witnesses and explicitly says that role assignment, placement and physical identification were **not independently countermodeled**. A list of different nouns is not a proof that closing either wall leaves every other wall open. Capacity and even readability are conditional on each other’s carrier/readout choices; the finite ordinary/graded pair holds supplied roles fixed. Its witness cannot certify role-selection independence or arbitrary state/dynamics/identification separations.

**Narrow repair:** replace the blanket count with scoped proved separations and an honest list of unresolved obligations. Use a pair/implication table only where actual witnesses justify the stated direction; leave the others unresolved. No new independent-wall number is required. Preserve the 23 historical bodies, including their initial and corrected N2 positions, and point from the corrected canonical surface to a dated authoritative scope overlay. Unselected parent N2 tables remain context/provenance, not independently certified results of this unit.

### F6 — P2: the displayed N-trial statistics omit their joint-law premise

**Locations:** B42 note lines 288–300 and 314–318; B42 runner lines 991–1015 and 1044–1055.

The single-use law determines `E[3s·n]=lambda` and `Var(3s·n)=3-lambda^2`. It does not determine the variance of an N-trial mean, the factorized likelihood, or the power formula for N matches. The note supplies a “causally certified” corpus and one-use Haar axes, but defers reset/freshness assumptions only when discussing almost-sure recovery and concentration. Those assumptions already matter for the finite formulas.

For example, draw one lawful Haar-axis/label pair and repeat it. Every coordinate has the stated one-use law, but at `lambda=0` the two-trial estimator variance is **3**, rather than **3/2**. Likewise a frozen match indicator with marginal 3/4 gives two matches with probability 3/4, not 9/16. `JOINT_TRIAL_CONTROL.json` computes the exact distinction. These are joint-law counterexamples, not qualifying fresh-reset experimental corpora.

**Narrow repair:** make the trial-by-trial conditional-kernel/factorization assumption explicit at the likelihood and all-match displays; add independent Haar draws and the corresponding fresh outcomes for the variance formula, or state an equally sufficient covariance condition. Keep the one-use moment calculation separate and retain the frozen-memory control. The SPAM gauges, finite all-match non-proof and absence of empirical evidence remain valid.

## Fresh evidence and meaningful controls

| Execution | Result | Interpretation |
|---|---|---|
| Original B43 on the main-based worktree | 10/0, 28.13 s | Fresh finite algebra/local-law baseline; original stdout body reproduced exactly |
| Original B42 on the main-based worktree | Exit 1, 0.54 s | Actual archived-path failure, preserved unaltered |
| Exact original B42 in external original layout | 16/0, 42.96 s | Fresh original-layout mathematical baseline; original stdout body reproduced exactly |
| Independent symbolic construction | 45/45 | Matrix units, code isometry, occupation-basis CAR, local scalar law, two conditioning counterexamples; no candidate import |
| Six actual source mutations | Six rejected by relevant gates | Branch normalization/orientation, logical Y, complement completion, CAR string, Record-factor separation |
| Actual helper mutation | Cache/source-binding falsely accept; actual measure rejects | F2 demonstrated through actual consumers |
| Actual helper call profile | B42→B38→B37 | Module initialization plus used local source/transcript closure; no B37/B38 main campaign |
| Independent joint-trial control | Exact differences reproduced | F6; no empirical inference |

The first exploratory orientation mutation was initially sent to the sign-forgotten channel gate, which correctly did not distinguish it. The existing general-repeatability gate **does** reject that same source mutation by comparing each branch with its oriented effect. This initial gate-selection miss is preserved in the control receipt and is not reported as a whole-run false PASS. The six final controls use their relevant gates. No failed experiment was relabeled green.

## Proof/import/no-go/governance disposition

`PROOF_REVIEW.md` maps the original claim families to surviving conditional results and required narrowing. The general support proof uses positive output and zero failure mass to force rank-one range, then branch trace to determine the reduced CP map; it does not establish dilation uniqueness. The global sign convention survives only at the abstract instrument/label quotient; the literal typed carrier separates the endpoints. The reduced collision wrapper does not establish a global codec conjugacy.

The fixed complex one-qubit grading/readability theorem and scalar commutant obstruction are finite algebra. The code is minimal only within the stated fixed-parity complex-qubit setting. Its fair complement is one supplied normalized CP completion. Its logical projective cubic action does not place physical apparatus on the lattice. Neither pointer readout, CAR representation, finite local laws, nor owner proposal language is promoted to a derived physical law.

All relevant code, physics-boundary, proof-obligation, import, retained-scope, labeling, governance and audit-compatibility lenses were applied. N1–N8 was applied to the actual negative statements, preserving positive alternatives; F4/F5 prevent a broad negative or inflated independence inventory from shipping. Existing four-axiom and approved-primitive scopes were checked; the parked decisions remain parked. The scalar additivity removed from Record is not restored. The current minimal memo remains byte-identical and must not be edited as part of these repairs.

The reserved #6379/#6858/#6859 original authored paths have zero intersection with the 40-path boundary. Actual runtime/proof review found no dependency on their science. Their sources, owner reservations and obligations remain excluded. The 2,937 other differing inherited sources and 4,001 generated paths in preparation's map are not accepted; its 6,908 main-only paths remain protected. No original generated audit publication is selected. Historical packet files whose names include “audit” remain immutable dated provenance, not applied verdicts.

The pair can be repaired narrowly without a broad parent campaign. A later author should preserve all originals, correct the affected live surfaces and current bindings, freeze source before fresh affected caches, and return one exact candidate for original-session confirmation together with the coordinator's intended manifest. **This review gives no permission to close #7846 by landing only B43.** Root owns integration, any final combined gates and PR actions. No formal audit was run or applied.

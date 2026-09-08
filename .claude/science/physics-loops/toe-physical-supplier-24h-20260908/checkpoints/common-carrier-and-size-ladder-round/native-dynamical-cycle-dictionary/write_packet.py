from pathlib import Path
import json,hashlib,subprocess,shutil
w=Path('/private/tmp/toe-native-dynamical-cycle-dictionary-20260908');p=w/'.claude/science/physics-loops/native-dynamical-cycle-dictionary-20260908'
base=subprocess.check_output(['git','-C',str(w),'rev-parse','HEAD'],text=True).strip()
texts={
'GOAL.md':'''# Target
Prove the full supplied native edge algebra, including physical Z, is exactly a constrained CAR–Z2-link algebra. The affirmative corollaries identify gated rings and low-charge signed hopping with its exchange algebra. This is frontier discovery, not retirement of a physical-action or Record-occurrence import.

The source revision is BASE. The exact finite graph, ordering, state-domain and Hamiltonian assumptions are in the canonical note. Success is a phase-correct onto unitary and all-generator proof; finite matrices are supporting evidence. No negative overlap claim is submitted.
''',
'ASSUMPTIONS_AND_IMPORTS.md':'''# Imports
- Native graph, ordered A/B/Z definitions, cycle convention and supplied instrument: the declared native instrument parent, equations 1–4 and Theorem 1.
- Literal degree-three ice and alternating geometric ring: only the exact definitions in the declared ice parent. No stochastic estimates, Coulomb phase, field calibration or transitive physical identification is reused.
- Mathematical tools: finite CAR/Jordan–Wigner matrices, incidence parity, exact phase cocycles, finite tensor products. Hypotheses are proved in the note.
- Additional conditions for the corollaries: full ambient state space in place of fixed positive cycle constraints, diagonal ice/low-charge gates, real V,J,t and use of the displayed Hamiltonian. These are supplied, not axiom-derived.
- Mathematical redundant fermion/link variables add no physical sites. Q signs are electric-configuration data, not two independent CAR species. Z2 is not U1.
- Prior U1 extra-link note is read as a contextual comparison, not a load-bearing physical premise. Its source hash is bound by the primary because the canonical source cites that comparison.

The live runner imports only its three declared local helper paths through runpy. Helpers import Python standard libraries; the independent matrix helper additionally uses installed NumPy. No scratch or moving external source is imported by a live helper. SOURCE_CLOSURE.json binds canonical source and every runtime local input. Preserved historical scripts are evidence, not secretly executed dependencies.
''',
'TRACE_GATE.md':'''# Trace gate
```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Test which native physical assumptions supply the newly explicit gates, Hamiltonian and state domain."
```
This identifies an exact common-carrier structure. It does not close a pre-existing physical supplier, promote a lane, derive a phase of matter, or constitute TOE completion.
''',
'CLAIM_STATUS_CERTIFICATE.md':'''# Status certificate
```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite dictionary under supplied algebra; gated dynamics conditional on additional stated model choices."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
proposal_allowed: false
proposal_allowed_reason: "No physical supplier or direct blocker closure is established."
hypothetical_axiom_status: null
admitted_observation_status: null
bare_retained_allowed: false
audit_required_before_effective_retained: true
```
The independently reviewed scratch mathematics passed. Canonical port review is pending root inspection. No audit verdict is applied and no formal negative/N1 claim is part of this block.
''',
'REVIEW_HISTORY.md':'''# Review history
The original dictionary proof f7598a669f9a263f21288dc7fbdf8bc76069fd72008865c010089f2fdf41945a and charged/exchange/gated-cycle proofs were independently read in full by the primary reviewer. Its final REVIEW.md is preserved under evidence/native-common-carrier-cold-review and has hash 442e3b3e6d1d90246a467bbf7a361e3585b1eae0736c76b436bcc8b76faf862e. A different pentagon/chord dense JW implementation tests all generator columns, including heterogeneous orders; a separate local Pauli implementation tests the exchange sign. No source correction was requested.

Canonical changes: coherent readable LaTeX presentation, explicit dependency/status links, portable helper wrappers and explicit guards replacing two Python asserts in the exchange helper. Scientific output equality is recorded in PORT_RECEIPT.json. The independent review did not pre-approve these canonical bytes; root's final port review remains pending.
''',
'HANDOFF.md':'''# Handoff
Base: BASE. Branch: codex/native-dynamical-cycle-dictionary-20260908. Worktree: /private/tmp/toe-native-dynamical-cycle-dictionary-20260908.

The canonical note is docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md. The primary is scripts/native_dynamical_cycle_dictionary_2026_09_08.py and executes three portable local helpers. Its live result has7919 scientific assertions:6712 author checks,15 independent dense matrix groups plus2 guards, and1188 exchange representatives plus2 guards. See PORT_RECEIPT, MUTATIONS and INTERFACE_CHECKS for exact preservation and adverse results. Actual raw files, original contracts, independent proofs and reviews are under evidence.

No formal negative overlap theorem, N1 packet, audit status or authority surface is changed. No full pipeline, strict lint or changed-evidence validation was run, as instructed. The primary cache is live-executed and source/input-bound; this does not confer an audit verdict.

Next action: root reads the full canonical source and wrapper delta, confirms source/hash closure and author/independent provenance, then decides publication. No PR or push has been performed at this checkpoint.
''',
'ARTIFACT_PLAN.md':'''# Artifact plan
One affirmative bounded-theorem note; one primary runner with three transparent live helpers; one primary cache and raw output; preserved mathematical proofs, independent controls/review, source-bound receipt and actual mutation failures. No duplicate theorem claim for the earlier negative overlap lane.
''',
'ROUTE_PORTFOLIO.md':'''# Route record
The fixed-code CAR dictionary did not by itself cover physical electric Z on the full ambient carrier. The selected constructive route enlarges mathematically and imposes all Gauss constraints, then integrates the exact edge-toggle phase. A direct quadratic phase removes the global sign ambiguity. The gated ice and low-charge routes become conditional corollaries. No generic numerical fit or phase inference is used.
''',
'OPPORTUNITY_QUEUE.md':'''# Next questions, not new claims
1. Identify which physical native premise supplies relaxed cycle states and the gated Hamiltonian.
2. Determine the phase and charge mobility of a specifically supplied Hamiltonian; the dictionary alone does not answer it.
3. Identify operational preparation/Record readout within permanent-record restrictions for that domain.
These are frontier questions, not audited closures or authorization for unbounded jobs.
''',
'NO_GO_LEDGER.md':'''# Scope memory
This affirmative packet does not submit the prior same-edge fixed-code overlap theorem. The present state domain is explicitly ambient/relaxed, so it must not be combined silently with the original fixed positive cycle code. Unitary coordinate equivalence alone does not select a Hamiltonian, create an extra physical link role, or derive a U1 field. No route family is claimed exhaustively excluded here.
''',
'LITERATURE_BRIDGES.md':'''# Mathematical context
Fermion encodings, Jordan–Wigner signs and constrained gauge representations are standard ideas. This proof derives its exact finite native convention directly from the repository operator definitions and finite algebra. No external quantitative theorem or empirical value is a load-bearing input. No historical-priority claim is made.
''',
'CHECKS.md':'''# Executed checks
- Canonical primary live run:7919 scientific assertions, positive elapsed/RSS guard,180s/384MiB contract.
- Pure --json output parses without trailing prose; unknown argument exits2.
- All scientific helper payload fields equal the frozen originals after removing only seconds and source_sha256.
- Actual temporary omitted-basis-phase and omitted-native-cycle-factor source mutations fail under python -O; complete stderr/stdout and bytes retained.
- Existing independent missing-phase control fails all6 edge comparisons; local unsigned exchange identity fails both nonzero representative domains.

Finite checks are supporting evidence for the general mathematical proof. No full repository pipeline, strict lint, changed-evidence audit or stochastic simulation was run.
''',
'PR_BACKLOG.md':'''# Publication checkpoint
Canonical staging awaits the root's requested full port review. No PR/push/commit at this checkpoint. Proposed title after review: [physics-loop] native dynamical-cycle dictionary conditional-support. Proposed base: main. The next authorized action is review, not a permission request or a claim of completed publication.
''',
'STATE.yaml':'''slug: native-dynamical-cycle-dictionary-20260908
base_revision: BASE
branch: codex/native-dynamical-cycle-dictionary-20260908
actual_current_surface_status: conditional-support
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
bare_retained_allowed: false
audit_required_before_effective_retained: true
current_step: canonical_staging_for_root_review
reviewed_original_math: pass
canonical_port_review: pending
next_action: root_full_canonical_source_and_helper_delta_review
open_imports: [native_operator_carrier, relaxed_cycle_state_domain, ice_low_charge_gates, hamiltonian_couplings, physical_occurrence_and_control]
'''
}
for name,text in texts.items():(p/name).write_text(text.replace('BASE',base).replace('has7919','has 7919').replace(':6712',': 6712').replace('plus2','plus 2').replace('and1188','and 1188').replace('all6','all 6').replace('exit2','exit 2').replace('run:7919','run: 7919').replace(',180s',', 180s').replace('exits2','exits 2').replace('proof f759','proof f759'))
# Source closure binds the exact runtime dependency paths without arbitrary parent-helper execution.
namespace={};script=w/'scripts/native_dynamical_cycle_dictionary_2026_09_08.py';import ast
module=ast.parse(script.read_text());paths=[]
for node in module.body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in node.targets):paths=list(ast.literal_eval(node.value))
allpaths=[str(script.relative_to(w))]+paths
(p/'SOURCE_CLOSURE.json').write_text(json.dumps({'base':base,'runtime_local_inputs':{f:hashlib.sha256((w/f).read_bytes()).hexdigest() for f in allpaths},'runtime_nonlocal_packages':['Python standard library','NumPy in independent dense helper'],'scratch_runtime_imports':[]},indent=2)+'\n')
shutil.copy2('/private/tmp/toe-native-dictionary-first-run.txt',p/'evidence/first-canonical-run.txt')

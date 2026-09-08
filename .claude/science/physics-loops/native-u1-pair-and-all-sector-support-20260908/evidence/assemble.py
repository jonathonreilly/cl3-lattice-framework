import pathlib,json,hashlib
S=pathlib.Path('/private/tmp/toe-24h-probes-20260908');W=pathlib.Path('/private/tmp/toe-native-u1-pair-and-all-sector-support-20260908');pack=W/'.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908'
name='NATIVE_U1_PAIR_OPERATOR_AND_ALL_LOW_SUPPORT_NOTE_2026-09-08.md';runner='native_u1_pair_and_all_low_support_2026_09_08.py'
head='''---
claim_id: native_u1_pair_operator_and_all_low_support_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Exact off-defect-number pair operator in the supplied redundant U1 carrier and constructive connectivity of all low native A support. No sign-free, mixing, energy, physical occurrence or coupling-selection conclusion."
upstream_dependencies:
  - native_low_charge_u1_dictionary_note_2026-09-08
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/'''+runner+'''
---

# Native pair channels and connected low-charge support

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

The low-projected native edge operator has both hopping and opposite-charge pair channels, with a phase fixed by the corrected unitary dictionary. Allowing every such edge move connects the full low-charge support on any connected finite simple six-regular bipartite graph. Connectivity does not remove the closed fermionic phase obstruction.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite operator/support statements under the supplied native algebra and low-domain restriction."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Dependencies and model dictionary

Use the [corrected signed-defect U1 dictionary](NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md) and [full native fermion/Z2 dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), with the [native instrument Pauli conventions](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). The physical carrier remains the original edge-bit Hilbert space; two species and electric links are constrained redundant coordinates, not added physical registers. Magnetic-cycle constraints are relaxed and the low-charge projection is supplied. Signed Gauss charge is distinct from the prior conserved defect-number quantity. An A coupling need not preserve that quantity.

The two complete reviewed proofs below retain their original statements and provenance. Part I uses the even cubic torus scope of its dictionary parent. Part II's support-only theorem applies more generally to the stated six-regular bipartite graphs. Its phase witness is established on the actual cubic carrier and independently on K6,6; no universal sign-frustration claim for every graph is needed.

## Part I: exact pair operator

'''
a=(S/'native-u1-pair-creation/DERIVATION.md').read_text();b=(S/'native-u1-all-sector-connectivity-root/DERIVATION.md').read_text()
text=head+a+'\n## Part II: constructive support theorem\n\n'+b+'''
## Executable boundary and provenance

The primary runner reads and hashes this note, its three mathematical source parents, four live exact helpers, and the preserved D4 seed fixture. It executes both author and independent implementations. The author pair helper tests actual L4 native columns and composed paths; the independent helper uses a different vertex labeling and neighbor ordering and forms the adjoint automatically. The support helpers construct explicit paths on L4 and independently on K6,6. The closed minus word and omitted-pair-sign adverse controls are mathematical failures of the altered formulas, not intended failures of the theorem. Predicate totals count actual condition evaluations, including repeated columns; they are neither Hilbert dimensions nor exhaustive state counts.

The original scripts, prospective contracts, raw results, failed variants, corrected absolute-phase parent, nonzero-coupling qualifier history, and hash-specific cold reviews are preserved in the associated research packet. Canonical changes are reporting, portable paths, and explicit predicates that remain active under Python optimization. No source-side audit verdict is assigned.

The premises do not provide a probability rule, preparation instrument, physical A coupling, or its magnitude. Neither connected support nor the conditional U1 coordinates establish sign-free dynamics, ground-state uniqueness, a spectral gap, mixing, deconfinement, electromagnetic identification, or relativistic pair production. Fixed-D results from a T-only Hamiltonian do not transfer to the pair Hamiltonian.
'''
(W/'docs'/name).write_text(text.rstrip()+'\n')
inputs=['docs/'+name,'docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md','docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md','docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md']+[f'scripts/native_u1_pair_support_{k}_2026_09_08.py' for k in ['pair_author','pair_independent','support_author','support_independent']]+[str((pack/'inputs/GLOBAL_D4_SEED.json').relative_to(W))]
code='''"""Exact finite pair-phase and constructive support controls."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS='''+repr(tuple(inputs))+'''
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
parts={}
for kind in ('pair_author','pair_independent','support_author','support_independent'):
 captured=io.StringIO()
 with contextlib.redirect_stdout(captured):runpy.run_path(str(root/'scripts'/f'native_u1_pair_support_{kind}_2026_09_08.py'))
 parts[kind]=json.loads(captured.getvalue())
 if parts[kind]['executed_predicates']<=0:raise RuntimeError('empty helper predicates')
if parts['pair_author']['nonbacktracking_two_edge_paths']!=24596:raise RuntimeError('pair composition coverage')
if parts['pair_independent']['pair_columns']!=3292 or parts['pair_independent']['forbidden_columns']!=532:raise RuntimeError('independent pair coverage')
if parts['support_author']['A_exchange_phase']!=-1 or parts['support_independent']['phase']!=-1:raise RuntimeError('closed phase')
if len(parts['support_independent']['all_ordered_pair_routes'])!=100:raise RuntimeError('independent route coverage')
def finite(x):
 if isinstance(x,float) and not math.isfinite(x):raise RuntimeError('nonfinite output')
 if isinstance(x,dict):
  for v in x.values():finite(v)
 if isinstance(x,(list,tuple)):
  for v in x:finite(v)
finite(parts)
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
count=sum(x['executed_predicates'] for x in parts.values())
out=dict(executed_predicates=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Selected exact operator columns and constructive routes; general proofs conditional, no physics selection or audit verdict.')
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_u1_pair_and_all_low_support_2026_09_08.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\\n')
print(json.dumps(out,indent=2,allow_nan=False))
if not args.json:
 print('per_element: oriented native A and signed pair/hopping CAR columns, including forbidden toggles.')
 print('per_site: no-double and integer Gauss support on both sublattices.')
 print('per_mode: explicit two-species adjoint and off-D block-phase comparisons.')
 print('per_block: actual L4 composed paths and independent relabeled native columns.')
 print('lattice_wide: constructive low-domain paths on L4 and K6,6, with closed minus witnesses.')
 print(f'TOTAL: PASS={count} FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s RSS384MiB.')
'''
(W/'scripts'/runner).write_text(code)
(pack/'ASSEMBLY_SCOPE.md').write_text('One coherent conditional claim combines the two already reviewed proofs. Both complete original bodies are retained verbatim in the canonical note. The source and helper inputs are actually read; no graph/registry/commit/publication changes are made by this port. Independent review remains pending.\n')

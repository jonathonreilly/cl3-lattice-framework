from pathlib import Path
import shutil,json,hashlib,subprocess
p=Path(__file__).resolve().parent; own=p.parent; root=Path('/private/tmp/toe-campaign-20260907/local-observable-cutoff')
for n in ['docs','scripts','evidence/primary','evidence/root']:(p/n).mkdir(parents=True,exist_ok=True)
for src,dest in [(own,p/'evidence/primary'),(root,p/'evidence/root')]:
 for f in src.iterdir():
  if f.is_file():shutil.copy2(f,dest/f.name)
shutil.copy2('/private/tmp/toe-autonomous-native-ladder-20260907/local-observable-review/REVIEW.md',p/'NATIVE_PRIMARY_REVIEW.md')
name='GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md'
runner='gauge_wilson_local_observable_finite_region_pw_2026_09_07.py'; helper='gauge_wilson_local_observable_boundary_schmidt_check_2026_09_07.py'
body=(root/'ROOT_DERIVATION.md').read_text().rstrip()
header='''---
claim_id: gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/'''+runner+'''
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
  - gauge_wilson_compact_cube_finite_qubit_cutoff_bounded_theorem_note_2026-09-07
claim_scope: "Local expectation approximation by finite spatial region and complete Peter-Weyl registers, with finite local energy and explicit preparation probability."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [compact Hamiltonian parent](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the model; the [finite-carrier parent](GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies its form-energy cutoff construction. The small-coupling gap theorem is not a premise. The proof below preserves the reviewed sharper root derivation verbatim. Independent strong-topology derivation and historical clarifications are preserved in the accompanying evidence packet.

The [primary exact geometry runner](../scripts/'''+runner+''') has29 named checks, including one resource check. The [independent Wilson-loop and coefficient helper](../scripts/'''+helper+''') has28 named checks, including one resource check. Haar orthogonality, the all-orders propagation bound and form-domain argument remain analytical premises; neither runner computes large-lattice dynamics. Four-link support means four finite registers, not four qubits or a native compiler. The optional infinite-volume statement uses restrictions of one fixed interaction, not volume-varying local couplings.

'''
(p/'docs'/name).write_text(header+body+'\n')
receipts={}
for tag,src,out in [('PRIMARY',own/'check.py',runner),('INDEPENDENT',root/'check.py',helper)]:
 s=src.read_text();s=s.replace('checks=[]','AUDIT_TIMEOUT_SEC=180\nAUDIT_MEMORY_LIMIT_MB=180\nif sys.argv[1:] not in ([],[\'--json\']): raise SystemExit(\'usage: '+out+' [--json]\')\nchecks=[]',1)
 # The source guards are before Sympy in the independent helper.
 if tag=='INDEPENDENT':
  guard="AUDIT_TIMEOUT_SEC=180\nAUDIT_MEMORY_LIMIT_MB=180\nif sys.argv[1:] not in ([],['--json']): raise SystemExit('usage: "+out+" [--json]')\n"
  s=s.replace(guard,'').replace('import sympy as s',guard+'import sympy as s')
 idx=s.index('print(json.dumps(');s=s[:idx]+s[idx:].replace('print(json.dumps(','result=',1)
 s=s.rstrip();suffix=',indent=2,allow_nan=False))' if tag=='PRIMARY' else ',indent=2))';assert s.endswith(suffix);s=s[:-len(suffix)]+'\n'
 scopes=(['per_element: PASS 4 actual cubic incidence and adjacent-tail controls','per_site: PASS 16 radius0..3 ball, crossing-distance and face-count controls','per_mode: PASS 5 balanced omitted Peter-Weyl threshold controls','per_block: PASS 3 projection normalization and zero-coupling/time controls','lattice_wide: PASS 1 resource control; all-volume propagation remains analytical'] if tag=='PRIMARY' else ['per_element: PASS 3 exact nine-mode Schmidt density and purity checks','per_site: PASS 10 endpoint-generator and boundary-singlet adverse checks','per_mode: PASS 2 whole-boundary-state retention and kinetic-energy checks','per_block: PASS 12 tail coefficient, integration, normalization and zero-coupling checks','lattice_wide: PASS 1 resource control; all-orders Haar/domain proofs remain analytical'])
 s+="if sys.argv[1:]==['--json']:\n print(json.dumps(result,indent=2,allow_nan=False))\nelse:\n print('PASS TOTAL='+str(result['TOTAL'])+' unique named checks')\n"
 for line in scopes:s+=' print('+repr(line)+')\n'
 s+=" print('DATA: '+json.dumps({k:v for k,v in result.items() if k not in ('checks','seconds','rss_MiB','source_sha256')},sort_keys=True,allow_nan=False))\n print('RESOURCE: seconds='+str(result['seconds'])+' rss_MiB='+str(result['rss_MiB'])+' limits=180sec/180MiB')\n print('SOURCE_SHA256: '+result['source_sha256'])\nsignal.alarm(0)\n"
 f=p/'scripts'/out;f.write_text(s)
 run=subprocess.run(['python3',str(f),'--json'],capture_output=True,text=True,timeout=180);assert run.returncode==0,run.stderr
 a=json.loads(run.stdout);b=json.loads((src.parent/'result.json').read_text());ignored={'seconds','rss_MiB','source_sha256'}
 assert {k:v for k,v in a.items() if k not in ignored}=={k:v for k,v in b.items() if k not in ignored}
 (p/(tag+'_RAW.json')).write_text(run.stdout)
 default=subprocess.run(['python3',str(f)],capture_output=True,text=True,timeout=180);assert default.returncode==0,default.stderr;(p/(tag+'_STDOUT.txt')).write_text(default.stdout)
 receipts[tag]={'original_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'scientific_payload_exactly_unchanged':True,'TOTAL':a['TOTAL'],'seconds':a['seconds'],'rss_MiB':a['rss_MiB']}
receipts['source']={'original_proof_sha256':hashlib.sha256((root/'ROOT_DERIVATION.md').read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256((p/'docs'/name).read_bytes()).hexdigest(),'body_verbatim':True}
(p/'PORT_EXECUTION_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n');print(json.dumps(receipts,indent=2))

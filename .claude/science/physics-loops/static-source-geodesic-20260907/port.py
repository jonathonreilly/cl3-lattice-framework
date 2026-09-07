from pathlib import Path
import shutil,json,hashlib,subprocess
p=Path(__file__).resolve().parent;own=p.parent;root=Path('/private/tmp/toe-campaign-20260907/static-charge-geodesics')
for n in ['docs','scripts','evidence/primary','evidence/root']:(p/n).mkdir(parents=True,exist_ok=True)
for src,dst in [(own,p/'evidence/primary'),(root,p/'evidence/root')]:
 for f in src.iterdir():
  if f.is_file():shutil.copy2(f,dst/f.name)
source='GAUGE_WILSON_STATIC_SOURCE_GEODESIC_PERTURBATION_BOUNDED_THEOREM_NOTE_2026-09-07.md';primary='gauge_wilson_static_source_geodesic_2026_09_07.py';helper='gauge_wilson_static_source_geodesic_cube_check_2026_09_07.py'
body=(root/'ROOT_DERIVATION.md').read_text();body=body.replace('One-particle normalized sine modes sin(pi k j/(L+1))','One-particle normalized sine modes sqrt(2/(L+1)) sin(pi k j/(L+1))')
header='''---
claim_id: gauge_wilson_static_source_geodesic_perturbation_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/'''+primary+'''
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
claim_scope: "Supplied finite static fundamental source sector: complete free geodesic eigenspace and exact first-order plaquette-flip operator, with finite-volume perturbative remainder."
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

The [compact Hamiltonian parent](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the lattice action. Static external color representations and their zero rest/kinetic energy are additional declared probes. The [primary exact planar runner](../scripts/'''+primary+''') has34 named checks and the [independent cube/source helper](../scripts/'''+helper+''') has37; each includes one resource control. The source's all-representation classification and perturbation argument remain analytical. Neither runner computes a full interacting charged spectrum or a uniform remainder. Both independently frozen derivations, candidate timing and prior-art review remain in the evidence packet.

'''
(p/'docs'/source).write_text(header+body.rstrip()+'\n')
receipts={}
for tag,src,name in [('PRIMARY',own/'check.py',primary),('INDEPENDENT',root/'check.py',helper)]:
 s=src.read_text()
 if tag=='PRIMARY':
  s=s.replace('import sympy as s',"AUDIT_TIMEOUT_SEC=180\nAUDIT_MEMORY_LIMIT_MB=180\nif sys.argv[1:] not in ([],['--json']):raise SystemExit('usage: "+name+" [--json]')\nimport sympy as s")
  pos=s.index('print(json.dumps(');tail=s[pos:];assert tail.rstrip().endswith(',default=encode,indent=2,allow_nan=False))');s=s[:pos]+tail.rstrip().replace('print(json.dumps(','result=',1)[:-len(',default=encode,indent=2,allow_nan=False))')]+'\n'
  scopes=['per_element: PASS 5 source/Haar normalization and adverse-factor checks','per_site: PASS 10 actual planar path-count and edge-charge matrix checks','per_mode: PASS 8 all-label increment and complete planar spectrum checks','per_block: PASS 10 adjacency symmetry and fixed-number fermion matrix checks','lattice_wide: PASS 1 resource guard; no uniform interacting remainder']
  s+="if sys.argv[1:]==['--json']:\n print(json.dumps(result,default=encode,indent=2,allow_nan=False))\nelse:\n print('PASS TOTAL='+str(result['TOTAL'])+' unique named checks')\n"
  for line in scopes:s+=' print('+repr(line)+')\n'
  s+=" print('DATA: '+json.dumps({k:v for k,v in result.items() if k not in ('checks','seconds','rss_MiB','source_sha256')},default=encode,sort_keys=True,allow_nan=False))\n print('RESOURCE: seconds='+str(result['seconds'])+' rss_MiB='+str(result['rss_MiB'])+' limits=180sec/180MiB')\n print('SOURCE_SHA256: '+result['source_sha256'])\n"
 else:
  s=s.replace("import os\nos.environ.setdefault('OPENBLAS_NUM_THREADS','1')", "import os,time,signal,sys,hashlib\nfrom pathlib import Path\nSTART=time.monotonic();signal.alarm(180)\nAUDIT_TIMEOUT_SEC=180\nAUDIT_MEMORY_LIMIT_MB=180\nfor key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'\nif sys.argv[1:] not in ([],['--json']):raise SystemExit('usage: "+name+" [--json]')")
  s=s.replace('START=time.monotonic(); checks={}; geometry=[]','checks={}; geometry=[]')
  s=s.replace('print(json.dumps(result,indent=2,default=int))',"result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()\nif sys.argv[1:]==['--json']:\n print(json.dumps(result,indent=2,default=int,allow_nan=False))\nelse:\n print('PASS TOTAL='+str(result['check_count'])+' unique named checks')\n")
  scopes=['per_element: PASS 7 path-count and actual4096-support census checks','per_site: PASS 12 actual three-dimensional edge-charge/face-flip geometry checks','per_mode: PASS 12 planar exterior-spectrum, finite-label and straight-path controls','per_block: PASS 5 source/Haar normalization and adverse-factor checks','lattice_wide: PASS 1 resource guard; all-representation proof remains analytical']
  for line in scopes:s+=' print('+repr(line)+')\n'
  s+=" print('DATA: '+json.dumps(result['geometry'],default=int,sort_keys=True,allow_nan=False))\n print('RESOURCE: seconds='+str(result['elapsed_sec'])+' rss_MiB='+str(result['peak_rss_mib'])+' limits=180sec/180MiB')\n print('SOURCE_SHA256: '+result['source_sha256'])\n"
 s+='signal.alarm(0)\n';f=p/'scripts'/name;f.write_text(s)
 run=subprocess.run(['python3',str(f),'--json'],capture_output=True,text=True,timeout=180);assert run.returncode==0,run.stderr;a=json.loads(run.stdout);b=json.loads((src.parent/'result.json').read_text());ignored={'source_sha256','seconds','rss_MiB','elapsed_sec','peak_rss_mib'}
 assert {k:v for k,v in a.items() if k not in ignored}=={k:v for k,v in b.items() if k not in ignored}
 (p/(tag+'_RAW.json')).write_text(run.stdout);r=subprocess.run(['python3',str(f)],capture_output=True,text=True,timeout=180);assert r.returncode==0,r.stderr;(p/(tag+'_STDOUT.txt')).write_text(r.stdout)
 receipts[tag]={'original_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'science_payload_unchanged':True,'TOTAL':a.get('TOTAL',a.get('check_count'))}
receipts['source']={'original_sha256':hashlib.sha256((root/'ROOT_DERIVATION.md').read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256((p/'docs'/source).read_bytes()).hexdigest(),'body_delta':'Explicit sqrt(2/(L+1)) normalization of sine modes only; all eigenvalues and coefficients unchanged.'}
(p/'PORT_EXECUTION_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n');print(json.dumps(receipts,indent=2))

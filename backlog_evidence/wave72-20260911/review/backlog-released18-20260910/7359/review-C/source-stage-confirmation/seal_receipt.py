import pathlib,json,hashlib,ast,subprocess
E=pathlib.Path('/Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/backlog-released18-20260910/7359'); W=pathlib.Path('/Users/jonreilly/Projects/Physics-worktrees/fix-released7359-c-20260911'); D=E/'fixes-C/source-draft-003'; R=W/'.claude/science/physics-loops/released7359-c-recovery-20260911'; O=E/'review-C/source-stage-confirmation'; O.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x): (O/n).write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
files=json.loads((D/'SOURCE_SHA256.json').read_text())['files']; inputs={}; count=0
for p,h in files.items():
 assert sha(D/'source'/p)==sha(W/p)==h
 if p.endswith('.py'):
  vals={}
  for node in ast.parse((W/p).read_text()).body:
   if isinstance(node,ast.Assign):
    for t in node.targets:
     if isinstance(t,ast.Name) and t.id in ('INPUT_SHA256','AUDIT_INPUT_PATHS'): vals[t.id]=ast.literal_eval(node.value)
  if 'INPUT_SHA256' in vals:
   for q,v in vals['INPUT_SHA256'].items():
    assert sha(W/q)==v; inputs[q]=v;count+=1
assert count==50
recovery={}
for f in ('RECOVERY_FREEZE.json',):
 data=json.loads((R/f).read_text()); recovery[str((R/f).relative_to(W))]=sha(R/f)
 for x in data['records']:
  assert sha(R/x['path'])==x['sha256']; recovery[str((R/x['path']).relative_to(W))]=x['sha256']
A=E/'fixes-C/recovery-author'; ef=json.loads((A/'EVIDENCE_FREEZE.json').read_text())
for x in ef['records']: assert sha(A/x['path'])==x['sha256']
assert sha(R/'RECOVERY_FREEZE.json')==ef['recovery_freeze_sha256']
main=subprocess.check_output(['git','rev-parse','main'],cwd='/Users/jonreilly/Projects/Physics',text=True).strip()
for p,h in inputs.items():
 result=subprocess.run(['git','show',main+':'+p],cwd='/Users/jonreilly/Projects/Physics',capture_output=True)
 if result.returncode==0: assert hashlib.sha256(result.stdout).hexdigest()==h
put('BINDINGS.json',{'source':files,'recovery':recovery,'inputs':dict(inputs,**{p:h for p,h in files.items() if p.endswith('.py')}),'current_main':main,'input_occurrences':count,'source_manifest_sha256':sha(D/'SOURCE_SHA256.json'),'recovery_evidence_freeze_sha256':sha(A/'EVIDENCE_FREEZE.json'),'recovery_handoff_sha256':sha(A/'RECOVERY_HANDOFF.json')})
report='''Source-stage PASS for frozen source-draft-003 and the final recovery refreeze. This confirms the corrected finite conditional claims and their source/input closure; fresh producer outputs and final composition remain pending. No science execution or formal audit was performed.

Coverage reuses the complete original review of 26 occurrences/22 paths and C01–C10, the complete helper, five primaries, five notes and five ledgers, then the full draft001 correction diff and draft002/draft003 affected deltas. All 16 frozen source files match the author tree. All 50 literal input occurrences match actual bytes; existing current-main input bodies are unchanged. Exact source, recovery and input hashes are in BINDINGS.json. Original Git body/delta verification remains bound by correction-source-read001/recovery-identity.json.

The decisive algebra remains sound within the corrected hypotheses: reflection covariance gives Gram Hermiticity but not positivity; the spectral anti-commutant is supported on the zero eigenspace under the stated gcd condition; Jacobi complement signs and interpolation degree bounds support the finite determinant checks; seam minors have determinant −|b|²; true congruence preserves inertia while left multiplication alone does not. General SPD congruence exists, leaving only the proposed physical/gauge identification open. The local continuity statement now excludes the helper’s separate zero-shear branch, and the section-frame construction explicitly defines its seams and shear-flipped image.

C01–C10 are resolved by corrected construction, narrowed statements or explicit historical disposition. The recovery retains all 26 actual original occurrences, all five complete Git deltas and the 354-line B188 sidecar. Its portable decoder was inspected and archived bodies independently compared with actual Git. Historical B9 open-half success is preserved; unavailable campaign/b186 sidecar bodies are not invented; the inconsistent nine-nonreal census is not treated as verified. Omitted detailed finite legs remain recoverable historical evidence. B187 volume controls are live candidates awaiting fresh output.

No new primitive, parent theorem, physical model selection, universal positivity boundary or reconstruction claim is accepted. Remaining obligations are the five fresh bounded producer outputs, unchanged before/after source/input identities, and original-reviewer confirmation of the final composed source/cache/recovery tree. Root retains execution authorization and integration gates.
'''
(O/'REPORT.md').write_text(report)
put('RECEIPT.json',{'status':'SOURCE_PASS','stage':'pre-producer source correction confirmation','reviewer':'/root/released6858_6859_review','model_requested':'Astra low','source_snapshot':str(D),'current_main':main,'bindings_sha256':sha(O/'BINDINGS.json'),'report_sha256':sha(O/'REPORT.md'),'composition_sha256':None,'science_execution':False,'formal_audit':False,'original_occurrences':26,'original_unique_paths':22,'finding_groups':10,'remaining':['fresh five producer outputs','final composed tree confirmation'],'prior_identity_verification_sha256':sha(E/'review-C/correction-source-read001/recovery-identity.json')})
print(str(O)); print(sha(O/'RECEIPT.json'))

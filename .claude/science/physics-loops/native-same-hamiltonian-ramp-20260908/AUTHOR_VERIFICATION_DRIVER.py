from pathlib import Path
import json,hashlib,subprocess,tempfile,shutil,runpy,signal
w=Path('/private/tmp/toe-native-same-hamiltonian-ramp-20260908');p=w/'.claude/science/physics-loops/native-same-hamiltonian-ramp-20260908';primary=w/'scripts/native_same_hamiltonian_ramp_2026_09_08.py';helper=w/'scripts/native_same_hamiltonian_ramp_jets_2026_09_08.py'
r=subprocess.run(['python3','-OO',str(primary)],capture_output=True,text=True,timeout=180);(p/'LIVE.stdout').write_text(r.stdout);(p/'LIVE.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError(r.stderr)
a=json.loads((w/'outputs/native_same_hamiltonian_ramp_2026_09_08.json').read_text());paths=list(a['input_sha256'])+[str(primary.relative_to(w))]
with tempfile.TemporaryDirectory(prefix='ramp-isolated-') as d:
 t=Path(d)
 for n in paths:(t/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,t/n)
 r=subprocess.run(['python3','-OO',str(t/primary.relative_to(w)),'--json'],capture_output=True,text=True,timeout=180)
 (p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
 if r.returncode:raise RuntimeError(r.stderr)
 b=json.loads(r.stdout)
 for key in ['K','generators','beta14_normalizer','distinct_pairs','checks']:
  if a['parts']['jets'][key]!=b['parts']['jets'][key]:raise RuntimeError('isolated payload '+key)
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps(dict(paths=paths,files=len(paths),scientific_payload_equal=True),indent=2)+'\n')
mut=[];s=helper.read_text();md=p/'mutations';md.mkdir(exist_ok=True)
for name,repl in [('wrong_moving_sign','a,k=solve(-1)'),('omit_derivatives','a,k=solve(derivatives=False)'),('static_generator_grading','a,k=solve();a.pop(2)')]:
 q=md/(name+'.py');q.write_text(s.replace('a,k=solve() # MUTATION_SOLVE',repl+' # MUTATION_SOLVE'))
 r=subprocess.run(['python3','-OO',str(q),'--json'],capture_output=True,text=True,timeout=180);(md/(name+'.stderr')).write_text(r.stderr);(md/(name+'.stdout')).write_text(r.stdout)
 if r.returncode==0:raise RuntimeError('mutant survived')
 mut.append(dict(name=name,exit_code=r.returncode,sha256=hashlib.sha256(q.read_bytes()).hexdigest()))
(p/'MUTATIONS.json').write_text(json.dumps(mut,indent=2)+'\n')
calls=[];old=signal.alarm;signal.alarm=lambda n:calls.append(n)
try:runpy.run_path(str(helper))
finally:signal.alarm=old
if calls:raise RuntimeError('helper reset alarm')
bad=subprocess.run(['python3','-OO',str(primary),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode==0:raise RuntimeError('unknown argument accepted')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps(dict(import_alarm_calls=calls,unknown_argument_exit=bad.returncode,optimized_run=True),indent=2)+'\n')
texts={
'GOAL.md':'Prove a conditional same-Hamiltonian ramp and original-ice local ring comparison. No selected physical law or ground-state preparation.',
'ASSUMPTIONS_AND_IMPORTS.md':'Supplied full native Hamiltonian, geometry, real bounded edge coefficients, beta14 common-coupling schedule, ice-supported initial density matrix and dressed final readout. Parent local-norm, homological inverse, strong-support and Lieb–Robinson results are load-bearing; Floquet literature is contextual only.',
'TRACE_GATE.md':'frontier_discovery; no exact axiom blocker retired. This removes a separately programmed initial dressing operation inside the supplied model, not the model or readout premise.',
'CONTROL_CONTRACT.md':'Prospective original contract preserved in originals/native-ramp-port-controls/PREREGISTRATION.md. Canonical coverage unchanged: 18,626 explicit predicates. Three discriminating semantic mutants fail. No generic odd-ramp deletion claim.',
'REVIEW_HISTORY.md':'Original complete proofs and source-bound independent reviews preserved under originals. Standard-library port reviewed at original SHA22a929f54debf8fcc2f3b386836522cbcc80bc3785ded0db0805340763bf777c (review01f2997382df0da072a8d443556f9a38aa43ca9f6516426ae501003f3852e562). Canonical note and wrapper await complete independent review; no preapproval inherited for new prose.',
'LITERATURE_BRIDGES.md':'Ho–Abanin1611.05024 is contextual prior art only. Original root reading scope preserved. No third-party PDF/text copied and no theorem imported from that work.',
'NO_GO_LEDGER.md':'No no-go result. Odd epsilon grading does not hold generically during the ramp; retain K5 and higher. Do not propagate an end-of-ramp local error without the later cone. No bare-observable epsilon² claim.',
'ARTIFACT_PLAN.md':'One note, one primary, one stdlib jet helper and paired JSON. No parent helper execution, graph, audit or publication.',
'CLAIM_STATUS_CERTIFICATE.md':'conditional-support, bounded_theorem, frontier_discovery. Formal audit status unchanged.',
'HANDOFF.md':'Author package ready for complete independent canonical review. Parent owns graph, staging, commit and PR. Full live/isolated outputs and actual mutant failures preserved.',
'PR_BACKLOG.md':'No PR created by author; parent integration pending.',
'ROUTE_PORTFOLIO.md':'Completed finite local moving frame, full-protocol fast cone, slow original-rho replacement. No new route launched.',
'OPPORTUNITY_QUEUE.md':'Current bounded author assignment complete; further physics targets belong to parent campaign.'}
for n,t in texts.items():(p/n).write_text('# '+n[:-3].replace('_',' ').title()+'\n\n'+t+'\n')
(p/'STATE.yaml').write_text('status: author_frozen_pending_canonical_review\nclaim_status: conditional-support\ntrace_class: frontier_discovery\n')
freeze={str(f.relative_to(w)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [w/'docs/NATIVE_SAME_HAMILTONIAN_RAMP_NOTE_2026-09-08.md',primary,helper,w/'outputs/native_same_hamiltonian_ramp_2026_09_08.json']}
(p/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n');print(json.dumps(freeze,indent=2))

from pathlib import Path
import hashlib,json,shutil,subprocess
B=Path('/private/tmp/toe-24h-probes-20260908');W=Path('/private/tmp/toe-native-finite-moment-ward-20260910');P=W/'.claude/science/physics-loops/native-finite-moment-ward-20260910';C=Path('/private/tmp/toe-physical-supplier-24h-20260908');CP=C/'.claude/science/physics-loops/toe-physical-supplier-24h-20260908';head='6871442099da4c984dd5f9707ffb2082e3696242'
old=B/'native-finite-moment-canonical-before-delivery-846578';old.mkdir();shutil.copytree(P,old/'packet');shutil.copy2(W/'docs/NATIVE_FINITE_MOMENT_WARD_NOTE_2026-09-10.md',old/'note.md');shutil.copy2(W/'scripts/native_finite_moment_ward_2026_09_10.py',old/'runner.py')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
index={}
files=sorted(CP.glob('*_SHA256.json'),key=lambda p:(p.name!='EIGHTY_THIRD_SHA256.json',p.name!='EIGHTY_SECOND_SHA256.json',p.name))
for m in files:
 d=json.loads(m.read_text());snap=d.get('snapshot');fs=d.get('files')
 if not isinstance(snap,str)or not isinstance(fs,dict):continue
 for name,h in fs.items():
  if isinstance(h,str):index.setdefault(h,[]).append((m,CP/snap/name))
rows=[]
for x in json.loads((P/'IMPORT_PROVENANCE.json').read_text()):
 choices=index.get(x['sha256'],[]);found=None
 for manifest,path in choices:
  rel=str(path.relative_to(C));run=subprocess.run(['git','show',head+':'+rel],cwd=C,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
  if run.returncode==0 and hashlib.sha256(run.stdout).hexdigest()==x['sha256']:found=(manifest,rel);break
 if found is None:raise ValueError('unmapped '+x['original'])
 m,rel=found;rows.append({**x,'recovery_commit':head,'recovery_repo_path':rel,'manifest':str(m.relative_to(C)),'url':'https://github.com/JonBridger/cl3-lattice-framework/blob/'+head+'/'+rel,'verified_git_blob_sha256':True})
(P/'RECOVERY_MAP.json').write_text(json.dumps(rows,indent=2)+'\n')
shutil.copy2(B/'CHECKPOINT83_REMOTE_VERIFICATION.json',P/'verification/CHECKPOINT83_REMOTE_VERIFICATION.json');shutil.copy2(B/'native-finite-moment-canonical-cold-review/RUNNER_REVIEW.md',P/'reviews/AFFECTED_RUNNER_REVIEW.md')
(P/'RECOVERY.md').write_text('''# Exact recovery

Stack base8078:4600d22d47052040aabe090148ec82cb9a1828f5. Preregistration82:b2a67aea7d4122961aac12c443ba0c320350a8e2 precedes the accepted ALLQ and omega5 outputs. Those outputs are now durably included in checkpoint83, exact remote commit6871442099da4c984dd5f9707ffb2082e3696242, snapshot accepted-b378-omega5-allq-degree20-witness-preregistration. Degree10 and earlier proof imports are recovered from earlier snapshots present at that same commit.

RECOVERY_MAP.json maps every copied import to an exact repository path at that commit and its SHA256. Each mapped blob was read with git show and verified against the copied import hash. The copied parent remote receipt authenticates checkpoint83's remote tree and all9698files. Earlier snapshot manifests establish the earlier paths; no subsequently produced degree20/witness outcome is claimed by this packet.

This is direct copied-import recovery. Transitive runtime input dictionaries retain their original absolute paths and hashes; it does not claim every platform interpreter/library byte is remotely archived, nor duplicate large catalogs or supply a new scientific replay. Recover with git show COMMIT:PATH and verify SHA256; platform runtime recreation is a separate requirement.
''')
(P/'STATE.yaml').write_text('status: source_reviewed_delivery_candidate\nsource_review: PASS_WITH_BOUNDED_CLAIMS\nphysical_replay: forbidden\nfull_integration: UNRUN\nchanged_audit_readiness: UNRUN\nformal_audit: UNRUN\nnext_action: parent final delivery review before commit push PR\n')
for name in ['CLAIM_STATUS_CERTIFICATE.md','REVIEW_HISTORY.md','HANDOFF.md']:
 p=P/name;s=p.read_text().replace('affected runner review pending','affected runner review PASS c353220e').replace('Affected parent runner review pending.','Affected independent runner review PASS c353220e.');p.write_text(s)
p=W/'docs/NATIVE_FINITE_MOMENT_WARD_NOTE_2026-09-10.md';s=p.read_text().replace('affected runner review pending','affected runner review PASS').replace('Affected runner review, full integration pipeline, changed-audit readiness, citation graph and formal audit remain unrun or pending.','Affected runner review is PASS. Full integration pipeline, changed-audit readiness and formal audit remain UNRUN; citation graph delivery receipt is recorded in the packet.');p.write_text(s)
print('recovery imports',len(rows))

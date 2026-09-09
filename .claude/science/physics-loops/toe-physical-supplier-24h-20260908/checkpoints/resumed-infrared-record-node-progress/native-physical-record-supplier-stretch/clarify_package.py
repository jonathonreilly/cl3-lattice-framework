from pathlib import Path
import shutil,json,hashlib,subprocess,sys
W=Path('/private/tmp/toe-native-charged-record-histories-20260909');P=W/'.claude/science/physics-loops/native-charged-record-histories-20260909';R=P/'PORT_RECORDS';H=P/'history/BEFORE_CLARIFICATION_6b7ddd';H.mkdir(parents=True,exist_ok=False)
note=W/'docs/NATIVE_CHARGED_RECORD_HISTORIES_NOTE_2026-09-09.md';out=W/'outputs/native_charged_record_histories_2026_09_09.json'
shutil.copytree(R,H/'PORT_RECORDS');shutil.copyfile(note,H/note.name);shutil.copyfile(out,H/out.name)
for f in P.glob('*.md'):shutil.copyfile(f,H/f.name)
s=note.read_text().replace('trace_class: frontier_discovery','trace_class: upstream_support')
s=s.replace('equation(1) determines D_e up to an outcome-only scalar. The surviving full native algebra is a full matrix algebra, so any other unitary intertwining the complete same observable map differs by a scalar.','equation(1) determines D_e exactly. If instead only the complete observable intertwining map is fixed, its implementing unitary is determined up to an outcome-only scalar. Here the full surviving native algebra includes both Z_e and A_e, which generate all matrix units by the full-carrier dictionary parent; equality on a smaller observable subalgebra would not suffice.')
note.write_text(s)
f=P/'TRACE_GATE.md';f.write_text(f.read_text().replace('trace_class: frontier_discovery','trace_class: upstream_support')+'\nNamed supported target: native instrument state-action interface with charged output carriers and coherent deletion histories. Physical occurrence closure and nearest-neighbor formation locality remain unsupplied.\n')
for n in ['CLAIM_STATUS_CERTIFICATE.md','HANDOFF.md']:
 f=P/n;f.write_text(f.read_text()+'\nTrace class: upstream_support for the native instrument state-action interface; this is not physical occurrence closure.\n')
f=P/'REVIEW_HISTORY.md';f.write_text(f.read_text()+'\nRoot source review requested two prose/metadata clarifications: fixed isometries determine equation (1) exactly, while observable intertwining admits scalar freedom; trace class is upstream_support. Predecessor source/output/isolated evidence preserved in history/BEFORE_CLARIFICATION_6b7ddd. Helpers and primary unchanged.\n')
old=json.loads((H/'PORT_RECORDS/SOURCE_FREEZE.json').read_text());m={n:hashlib.sha256((W/n).read_bytes()).hexdigest() for n in old};(R/'SOURCE_FREEZE.json').write_text(json.dumps(m,indent=2)+'\n')
for n in m:shutil.copyfile(W/n,R/'isolated'/n)
primary='scripts/native_charged_record_histories_2026_09_09.py'
a=subprocess.run([sys.executable,'-I','-B','-S','-OO',str(W/primary),'--json'],capture_output=True,text=True,timeout=30);(R/'CLARIFIED.stderr').write_text(a.stderr)
if a.returncode:raise RuntimeError(a.stderr)
out.write_text(a.stdout)
b=subprocess.run([sys.executable,'-I','-B','-S','-OO',str(R/'isolated'/primary),'--json'],capture_output=True,text=True,timeout=30);(R/'ISOLATED.stdout').write_text(b.stdout);(R/'ISOLATED.stderr').write_text(b.stderr)
if b.returncode:raise RuntimeError(b.stderr)
def payload(s):
 z=json.loads(s);z.pop('seconds');z.pop('peak_rss_bytes')
 for c in z['controls']:c.pop('seconds',None)
 return z
x,y=payload(a.stdout),payload(b.stdout)
if x!=y:raise ValueError('isolated mismatch')
z=payload((H/out.name).read_text());z['input_sha256'][str(note.relative_to(W))]=m[str(note.relative_to(W))]
if x!=z:raise ValueError('unexpected payload change')
(R/'CLARIFICATION_RECEIPT.json').write_text(json.dumps({'status':'PASS','isolated_payload_equal':True,'predecessor_payload_equal_except_note_hash':True,'helper_primary_unchanged':True,'source_freeze_sha256':hashlib.sha256((R/'SOURCE_FREEZE.json').read_bytes()).hexdigest(),'note_sha256':m[str(note.relative_to(W))]},indent=2)+'\n')
print((R/'CLARIFICATION_RECEIPT.json').read_text())

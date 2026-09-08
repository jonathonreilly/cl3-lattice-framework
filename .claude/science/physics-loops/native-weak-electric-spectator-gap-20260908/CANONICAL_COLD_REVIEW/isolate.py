import ast,json,hashlib,shutil,subprocess,os,time,signal
from pathlib import Path
B=Path('/private/tmp/toe-native-weak-electric-spectator-gap-20260908');O=Path(__file__).parent;D=O/'isolated';D.mkdir(exist_ok=False)
p='scripts/native_weak_electric_spectator_gap_2026_09_08.py';tree=ast.parse((B/p).read_text());inputs=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets))
pins={}
for n in (p,*inputs):
 dst=D/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(B/n,dst);pins[n]=hashlib.sha256(dst.read_bytes()).hexdigest()
(O/'ISOLATED_INPUT_HASHES.json').write_text(json.dumps(pins,indent=2)+'\n')
start=time.monotonic();cmd=['/usr/bin/time','-lp','/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12','-I','-OO',str(D/p)]
# -I removes script directory, so use a standard-library runpy wrapper explicitly
# exposing only this isolated scripts directory, as required by local sibling imports.
cmd=cmd[:-1]+['-c','import sys,runpy;sys.path.insert(0,sys.argv[1]);sys.argv=[sys.argv[2],"--json"];runpy.run_path(sys.argv[0],run_name="__main__")',str(D/'scripts'),str(D/p)]
with (O/'ISOLATED.stdout').open('w') as out,(O/'ISOLATED.stderr').open('w') as err:
 proc=subprocess.Popen(cmd,cwd=D,stdout=out,stderr=err,start_new_session=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
 try:code=proc.wait(timeout=180)
 except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait();raise
elapsed=time.monotonic()-start;stderr=(O/'ISOLATED.stderr').read_text();rss=int(next(x.split()[0] for x in stderr.splitlines() if 'maximum resident set size' in x))
if code or elapsed>=180 or rss>=384*1048576:raise ValueError((code,elapsed,rss))
name='outputs/native_weak_electric_spectator_gap_2026_09_08.json';actual=json.loads((D/name).read_text());canonical=json.loads((B/name).read_text())
for key in ('parts','exact_interval','residual_count','bridge_count','executed_predicates','predicate_breakdown','input_sha256','source_sha256'):
 if actual[key]!=canonical[key]:raise ValueError('payload '+key)
for key in ('generators','orbits','invariant_dimension','checks'):
 if actual['symmetry'][key]!=canonical['symmetry'][key]:raise ValueError('symmetry '+key)
receipt=dict(returncode=code,seconds=elapsed,rss_bytes=rss,files_copied=len(pins),exact_payload_equal=True,output_sha256=hashlib.sha256((D/name).read_bytes()).hexdigest(),command=cmd)
(O/'ISOLATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))

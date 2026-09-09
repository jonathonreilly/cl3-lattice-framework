import sys,json,hashlib,struct,time,signal,resource,argparse,types
from pathlib import Path
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('binding');ap.add_argument('output');args=ap.parse_args()
if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('-I -B -S required')
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h:raise ValueError('pin '+p)
data=(P/'core.py').read_bytes();m=types.ModuleType('core');m.__file__=str(P/'core.py');exec(compile(data,m.__file__,'exec'),m.__dict__)
for mod in list(sys.modules.values()):
 path=getattr(mod,'__file__',None)
 if path and not path.startswith('<'):
  path=str(Path(path).resolve())
  if path not in f['inputs']:raise ValueError('loaded origin '+path)
out=Path(args.output)
if out.exists():raise ValueError('fresh output')
out.mkdir();start=time.monotonic();signal.alarm(29);stage='binding';index=0
try:
 bp=Path(args.binding);bh=hashlib.sha256(bp.read_bytes()).hexdigest();b=json.loads(bp.read_text());error=m.F(b['Echi'])
 if b['physical_global_phase']!='i' or b['replay_status']!='PASS':raise ValueError('binding state')
 # Root binds these exact receipts; no free choice of Echi or input after results.
 for k in ['production_result_sha256','independent_replay_sha256','raw_sha256']:
  if len(b[k])!=64 or any(c not in '0123456789abcdef' for c in b[k]):raise ValueError('receipt digest')
 path=Path(args.input)
 if path.stat().st_size!=16*(1<<20):raise ValueError('length')
 bins={};digest=hashlib.sha256();stage='single raw scan'
 with path.open('rb') as file:
  while True:
   raw=file.read(4096*16)
   if not raw:break
   digest.update(raw)
   if len(raw)%16:raise ValueError('partial pair')
   for zero,value in struct.iter_unpack('<Qd',raw):
    if zero!=0 or index>=1<<20:raise ValueError('phase/extra record')
    c=m.counts(index);bins[c]=bins.get(c,0)+m.square(value);index+=1
 if index!=1<<20 or digest.hexdigest()!=b['raw_sha256']:raise ValueError('coverage/hash')
 stage='rational energy bins';summary=m.summarize(bins,error)
 if hashlib.sha256(bp.read_bytes()).hexdigest()!=bh:raise ValueError('binding changed')
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
 result={'status':'PASS','entries':index,'input_sha256':digest.hexdigest(),'binding_sha256':bh,'bins':[{'counts':c,'numerator':str(v)} for c,v in sorted(bins.items())],'denominator_exponent':2148,'summary':summary,'seconds':time.monotonic()-start,'source_freeze':hashlib.sha256((P/'FREEZE.json').read_bytes()).hexdigest()}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps({'stage':stage,'entries':index,'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise

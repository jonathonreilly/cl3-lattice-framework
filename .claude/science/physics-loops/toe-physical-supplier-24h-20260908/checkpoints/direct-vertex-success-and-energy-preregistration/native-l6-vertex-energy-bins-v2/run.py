import sys,json,hashlib,struct,time,signal,resource,argparse,types
from pathlib import Path
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('binding');ap.add_argument('output');ap.add_argument('--readiness',action='store_true');args=ap.parse_args()
if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('-I -B -S required')
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as file:
  for chunk in iter(lambda:file.read(1<<20),b''):h.update(chunk)
 return h.hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
mods={}
for name in ['core','binding']:
 data=(P/(name+'.py')).read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(P/(name+'.py'))]:raise ValueError('verified source')
 module=types.ModuleType(name);module.__file__=str(P/(name+'.py'));exec(compile(data,module.__file__,'exec'),module.__dict__);mods[name]=module
m=mods['core']
def loaded_guard():
 for mod in list(sys.modules.values()):
  path=getattr(mod,'__file__',None)
  if path and not path.startswith('<'):
   path=str(Path(path).resolve())
   if path not in f['inputs'] or sha(path)!=f['inputs'][path]:raise ValueError('loaded origin '+path)
loaded_guard()
if args.readiness:
 print(json.dumps({'status':'PASS','parser_and_imports':True,'full_scans':0}));raise SystemExit
out=Path(args.output)
if out.exists():raise ValueError('fresh output')
out.mkdir();start=time.monotonic();signal.alarm(29);stage='binding';index=0
try:
 b=mods['binding'].validate(args.binding);bh=b['binding_sha256'];error=m.F(b['Echi'])
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
 (out/'BINS.json').write_text(json.dumps({'entries':index,'input_sha256':digest.hexdigest(),'bins':[{'counts':c,'numerator':str(v)} for c,v in sorted(bins.items())],'denominator_exponent':2148},indent=2)+'\n')
 stage='rational energy bins';summary=m.summarize(bins,error);loaded_guard()
 if any(sha(path)!=h for path,h in b['hashes'].items()):raise ValueError('receipt changed')
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
 result={'status':'PASS','entries':index,'input_sha256':digest.hexdigest(),'binding_sha256':bh,'bins':[{'counts':c,'numerator':str(v)} for c,v in sorted(bins.items())],'denominator_exponent':2148,'summary':summary,'seconds':time.monotonic()-start,'source_freeze':hashlib.sha256((P/'FREEZE.json').read_bytes()).hexdigest()}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps({'stage':stage,'entries':index,'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise

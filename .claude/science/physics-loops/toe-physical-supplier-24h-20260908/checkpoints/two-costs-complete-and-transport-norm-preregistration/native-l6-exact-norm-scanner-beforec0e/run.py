import sys,os,json,time,hashlib,signal,resource,struct,runpy
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(29)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=2:raise ValueError('-I -B fresh output')
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for path,h in f['inputs'].items():
 if sha(path)!=h:raise ValueError('pin')
out=Path(sys.argv[1]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external')
out.mkdir(parents=True)
try:
 t=time.monotonic();path=out/'FIXED.bin'
 # Predeclared mixture includes signed zero, subnormal, largest finite and ordinary dyadics.
 special=[0,1,(1<<52)-1,1<<52,(2046<<52)|((1<<52)-1),1<<63]
 with path.open('wb') as file:
  for i in range(1<<20):
   if i%1024<6:bits=special[i%1024];file.write(struct.pack('<QQ',bits,bits^(1<<63)))
   else:file.write(struct.pack('<dd',((i%17)-8)/16,((i%13)-6)/32))
 generation=time.monotonic()-t;ns=runpy.run_path(str(P/'scanner.py'));t=time.monotonic();result=ns['scan'](path,21,1);elapsed=time.monotonic()-t
 result.update(generation_seconds=generation,scan_seconds=elapsed,fixture_sha256=sha(path),seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,freeze=sha(P/'FREEZE.json'),status='COMPLETE')
 (out/'PARTIAL.json').write_text(json.dumps(result)+'\n')
 if result['rss_bytes']>384*1048576:raise MemoryError('RSS')
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise

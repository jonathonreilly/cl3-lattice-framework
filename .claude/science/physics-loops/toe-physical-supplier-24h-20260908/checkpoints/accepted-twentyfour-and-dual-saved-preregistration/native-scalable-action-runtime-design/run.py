"""Source-only readiness. Native execution unconditionally disabled."""
import sys,json,hashlib,types,argparse
from pathlib import Path
P=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['source-readiness','native']);a=ap.parse_args()
 if a.mode=='native':raise ValueError('NOTREADY: actual24POST/source-runtime/root contract absent')
 if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S')
 f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
 if str(Path(sys.executable).resolve())!=f['interpreter'] or sorted(x.name for x in P.iterdir())!=f['membership']:raise ValueError('runtime/member')
 for p,h in f['inputs'].items():
  if sha(p)!=h:raise ValueError('source/runtime pin')
 for name in('interval','coefficients','core','binder','old_reader','adapter','worker'):
  p=P/(name+'.py');raw=p.read_bytes()
  if hashlib.sha256(raw).hexdigest()!=f['inputs'][str(p)]:raise ValueError('verified bytes')
  m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(raw,str(p),'exec'),m.__dict__)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('loaded origin')
 print(json.dumps({'status':'PASS_SOURCE_ONLY_NATIVE_DISABLED','history_loads':0,'index_calls':0,'entry_calls':0,'C_calls':0,'bound_calls':0}))
if __name__=='__main__':main()

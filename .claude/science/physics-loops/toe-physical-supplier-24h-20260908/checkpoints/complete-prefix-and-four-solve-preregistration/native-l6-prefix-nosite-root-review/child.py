from pathlib import Path
import sys,os,json,hashlib,runpy,argparse,signal,time,resource
from fractions import Fraction
from math import isqrt
P=Path(__file__).resolve().parent;c=json.loads((P/'CONFIG.json').read_text());W=Path(c['canonical']);I=Path(c['isolated']);f=json.loads((W/c['packet']/'SOURCE_FREEZE.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if not sys.flags.isolated or not sys.dont_write_bytecode or not sys.flags.no_site or sys.flags.optimize!=2:raise ValueError('-I -B -S -OO required')
if sha(W/c['packet']/'SOURCE_FREEZE.json')!=c['source_freeze']:raise ValueError('sourcefreeze')
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('threads')
if sorted(str(p.relative_to(I)) for p in I.rglob('*') if p.is_file())!=sorted(f['files']):raise ValueError('whole isolated membership')
for n,h in f['files'].items():
 if sha(I/n)!=h:raise ValueError('isolated hash '+n)
for n,h in f['runtime'].items():
 if sha(n)!=h:raise ValueError('runtime '+n)
# Definition/import-only loading before the arithmetic entry point.
for n in f['isolated_executable_membership']:
 ns=runpy.run_path(str(I/n))
 if n==c['primary']:primary=ns
rootfreeze=json.loads((P/'FREEZE.json').read_text())
def guard():
 for m in tuple(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if not path:continue
  path=str(Path(path).resolve())
  if path==str(Path(__file__).resolve()):
   if sha(path)!=rootfreeze['files']['child.py']:raise ValueError('child hash')
  elif path.startswith(str(I)+'/'):
   n=str(Path(path).relative_to(I))
   if n not in f['files'] or sha(path)!=f['files'][n]:raise ValueError('loaded local '+path)
  elif path not in f['runtime'] or sha(path)!=f['runtime'][path]:raise ValueError('loaded runtime '+path)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args(['--json'])
guard()
if sys.argv[1:]==['--preflight']:
 print(json.dumps({'status':'PASS import/closure only','gap_calls':0,'baseline_calls':0}))
else:
 sys.argv=[str(I/c['primary']),'--json'];primary['main']();guard()

"""Same-process portable replay adapter; no candidate generation."""
import argparse,hashlib,json,os,sys,time,types,signal,math,resource
from pathlib import Path
START=time.monotonic();R=Path(__file__).resolve().parent

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','verify']);a=ap.parse_args()
 require(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I -B -S')
 freeze_sha=sha(R/'ROOT_FREEZE.json');frozen=json.loads((R/'ROOT_FREEZE.json').read_text())
 for n,h in frozen['files'].items():require(sha(R/n)==h,'adapter source '+n)
 f=json.loads((R/'INPUTS.json').read_text());C=Path(f['isolated_root']);require(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 def pins():
  require(sha(R/'ROOT_FREEZE.json')==freeze_sha,'immutable root freeze')
  for p,h in f['runtime'].items():require(sha(p)==h,'runtime '+p)
  for p,h in f['science'].items():require(sha(C/p)==h,'science '+p)
  for n,h in frozen['files'].items():require(sha(R/n)==h,'wrapper '+n)
  actual={str(p.relative_to(C)) for p in C.rglob('*') if p.is_file() and not str(p.relative_to(C)).startswith('outputs/native_l6_nonlinear_star_vertex_2026_09_09.')}
  require(actual==set(f['science']),'exact isolated membership')
 def origins():
  for mod in list(sys.modules.values()):
   q=getattr(mod,'__file__',None)
   if q:
    q=str(Path(q).resolve())
    if q.startswith(str(C)+'/'):require(q[len(str(C))+1:] in f['science'] and sha(q)==f['science'][q[len(str(C))+1:]],'science origin '+q)
    elif q.startswith(str(R)+'/'):require(Path(q).name in frozen['files'] and sha(q)==frozen['files'][Path(q).name],'wrapper origin')
    else:require(q in f['runtime'] and sha(q)==f['runtime'][q],'runtime origin '+q)
 pins();origins()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):require(os.environ.get(k)=='1','threads')
 sys.path.insert(0,str(Path(f['numpy_origin']).parents[1]))
 import numpy as np
 import numpy.lib.format,numpy.lib.npyio,pickle,ast,tokenize,shutil,zlib,bz2,lzma,io,tempfile
 require(str(Path(np.__file__).resolve())==f['numpy_origin'] and np.__version__==f['numpy_version'],'numpy origin/version')
 stream=io.BytesIO();np.save(stream,np.array([0.,-0.,1.],dtype=np.float64),allow_pickle=False);stream.seek(0);require(np.load(stream,allow_pickle=False).view(np.uint64).tolist()==[0,1<<63,4607182418800017408],'tiny late NPY')
 origins();p=C/'scripts/native_l6_nonlinear_star_vertex_2026_09_09.py';data=p.read_bytes();require(hashlib.sha256(data).hexdigest()==f['science'][str(p.relative_to(C))],'main bytes')
 sys.argv=[str(p),'--json']+(['--verify'] if a.mode=='verify' else [])
 m=types.ModuleType('__main__');m.__file__=str(p);sys.modules['__main__']=m
 try:
  exec(compile(data,str(p),'exec'),m.__dict__)
  pins();origins();require(time.monotonic()-START<180,'adapter180 postcheck')
  if a.mode=='verify':
   output=C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json';r=json.loads(output.read_text());require(r['status']=='PASS' and r['replay']['scientific_pass'] is True,'replay pass')
   (R/'WORKER_COMPLETE.json').write_text(json.dumps(dict(status='PASS',result_sha256=sha(output),seconds=time.monotonic()-START,canonical_freeze=f['canonical_freeze']),indent=2)+'\n')
  else:print(json.dumps(dict(status='READINESS_PASS',native_replay=False,pins=len(f['runtime']),actual_parser=True,late_npy=True)))
 finally:signal.alarm(0)
if __name__=='__main__':
 try:main()
 except BaseException as e:
  (R/'WORKER_FAILURE.json').write_text(json.dumps(dict(error=repr(e),seconds=time.monotonic()-START),indent=2)+'\n');raise

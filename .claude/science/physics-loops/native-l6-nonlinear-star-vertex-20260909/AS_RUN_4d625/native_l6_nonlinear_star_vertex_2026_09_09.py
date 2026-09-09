"""Portable saved-candidate certificate. --verify performs the full replay; never a solve."""
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,tempfile,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs'
PREFIX='native_l6_nonlinear_vertex_'
AUDIT_TIMEOUT_SEC=180

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pins():
 m=json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())
 for p,h in m.items():require(sha(ROOT/p)==h,'source '+p)
 return m

def load(alias,name):
 p=ROOT/'scripts'/(PREFIX+name+'_2026_09_09.py');data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location(alias,p);m=importlib.util.module_from_spec(spec);sys.modules[alias]=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def claims(result, factor=F(1)):
 require(result.get('status')=='PASS' and result.get('scientific_pass') is True,'certificate passed')
 w=list(map(F,result['particle_intervals']['all_ge3']));w=[x*factor for x in w]
 require(F('0.001921920169')<w[0]<=w[1]<F('0.001921920178'),'rounded higher-sector enclosure')
 require(F('0.04383')**2<w[0] and w[1]<F('0.04384')**2,'distance enclosure')
 require(F(result['Echi'])<=F('0.00000000004825'),'rounded error')
 for n in ('3','5','7'):require(F(result['particle_intervals'][n][0])>0,'positive '+n)
 require([result[k] for k in ('full_vectors','fresh_residuals','transports','exact_norm_scans')]==[7,4,27,9],'full coverage')
 return {'squared_distance_strict_decimal':['0.001921920169','0.001921920178'],'distance_strict_decimal':['0.04383','0.04384'],'full_linear_modes':108,'positive_particle_sectors':[3,5,7]}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.add_argument('--verify',action='store_true');args=ap.parse_args()
 require(sys.flags.isolated and sys.flags.dont_write_bytecode,'use -I -B')
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):require(os.environ.get(k)=='1','single thread '+k)
 start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('audit timeout')));signal.alarm(AUDIT_TIMEOUT_SEC)
 output=ROOT/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json';stage='pins'
 try:
  manifest=pins();geometry=load('canonical_geometry','geometry').check(INPUT)
  imported={}
  for alias,name in [('envelope','envelope'),('transport','transport'),('fp_guard','fp_guard'),('validate_coefficients','validate_coefficients'),('canonical_replay','review')]:imported[alias]=load(alias,name)
  accepted=json.loads((INPUT/'accepted/INDEPENDENT_REVIEW.json').read_text())
  report=accepted
  receipt=json.loads((INPUT/'accepted/ROOT_ACCEPTANCE.json').read_text())
  require(receipt['accepted'] is True and receipt['status']=='PASS','root acceptance')
  for key,name in [('production_result_sha256','RESULT.json'),('independent_replay_sha256','INDEPENDENT_REVIEW.json'),('worker_complete_sha256','WORKER_COMPLETE.json')]:require(receipt[key]==sha(INPUT/'accepted'/name),'accepted binding '+key)
  require(receipt['Echi']==report['Echi'] and receipt['particle_intervals']==report['particle_intervals'],'accepted certificate binding')
  rounded=claims(report)
  if not args.verify:
   print(json.dumps({'status':'READINESS_ONLY','geometry':geometry,'rounded_accepted_evidence':rounded,'physical_replay_executed':False}));return
  require(not output.exists(),'fresh canonical output')
  with tempfile.TemporaryDirectory(prefix='l6-certificate-') as temp:
   folder=Path(temp)
   for p in (INPUT/'accepted').glob('*'):
    if p.name=='RESULT.json' or p.name.endswith('_candidate.json'):(folder/p.name).write_bytes(p.read_bytes())
   vm=json.loads((INPUT/'VECTOR_MANIFEST.json').read_text())
   rows=vm if isinstance(vm,list) else vm['files']
   for row in rows:
    source=INPUT/row['compressed'];require(sha(source)==row['gzip_sha256'],'compressed hash')
    target=folder/row['name']
    with gzip.open(source,'rb') as src,target.open('wb') as dst:
     for b in iter(lambda:src.read(1048576),b''):dst.write(b)
    require(target.stat().st_size==row['bytes'] and sha(target)==row['sha256'],'decompressed hash')
   def progress(s,**detail):
    nonlocal stage
    stage=s;(output.with_suffix('.PARTIAL.json')).write_text(json.dumps(dict(stage=s,detail=detail,seconds=time.monotonic()-start),indent=2)+'\n')
   actual=imported['canonical_replay'].replay(folder,progress)
  require(actual['Echi']==report['Echi'] and actual['particle_intervals']==report['particle_intervals'],'accepted exact payload')
  rounded=claims(actual);require(pins()==manifest,'post source closure');peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if sys.platform!='darwin':peak*=1024
  require(peak<384*1048576 and time.monotonic()-start<180,'resource cap')
  output.write_text(json.dumps(dict(status='PASS',scope='finite L6 supplied-model vacuum image',geometry=geometry,replay=actual,claims=rounded,input_hashes=manifest,seconds=time.monotonic()-start,peak_bytes=peak),indent=2)+'\n');print(output.read_text())
 except BaseException as e:
  failure=output.with_suffix('.FAILED.json');failure.write_text(json.dumps(dict(status='FAIL',stage=stage,error=repr(e),seconds=time.monotonic()-start),indent=2)+'\n');raise
 finally:signal.alarm(0)
if __name__=='__main__':main()

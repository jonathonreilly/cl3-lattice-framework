import pathlib,json,hashlib,subprocess,time,os,signal,sys
from fractions import Fraction
P=pathlib.Path(__file__).resolve().parent
OUT=P/'REPLAY_OUTPUT'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();pins=json.loads((P/'REPLAY_INPUTS.json').read_text())
 for f,h in pins['files'].items():
  if sha(f)!=h:raise ValueError('input changed '+f)
 source=pathlib.Path(pins['candidate_directory'])
 if sorted(x.name for x in source.glob('bridge_*.json'))!=pins['json_membership'] or sorted(x.name for x in source.glob('bridge_*.npz'))!=pins['npz_membership']:raise ValueError('membership')
 if OUT.exists():raise ValueError('no overwrite')
 OUT.mkdir();receipts=[]
 try:
  for b in (0,3,9,12,36,96):
   if 10+time.monotonic()-start+180>1200:raise RuntimeError('full reserve')
   out=OUT/f'bridge_{b}.json';log=OUT/f'bridge_{b}.stdout';err=OUT/f'bridge_{b}.stderr';t=time.monotonic();peak=0;reason=None
   with log.open('wb') as so,err.open('wb') as se:
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
    proc=subprocess.Popen(['/usr/bin/time','-lp',sys.executable,str(P/'postcheck.py'),str(source/f'bridge_{b}.json'),str(out)],stdout=so,stderr=se,env=env,start_new_session=True)
    while proc.poll() is None:
     elapsed=time.monotonic()-t
     try:
      listing=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True,timeout=2)
      rss=sum(int(a[1])*1024 for line in listing.splitlines() if len(a:=line.split())==2 and int(a[0])==proc.pid);peak=max(peak,rss)
     except subprocess.TimeoutExpired:reason='RSS monitor timeout'
     if elapsed>=180:reason='wall cap'
     if peak>384*1024**2:reason='RSS cap'
     if reason:
      os.killpg(proc.pid,signal.SIGKILL);break
     time.sleep(.05)
    code=proc.wait()
   receipt={'bridge':b,'returncode':code,'failure':reason,'elapsed':time.monotonic()-t,'peak_group_rss':peak,'stdout_sha':sha(log),'stderr_sha':sha(err),'input_manifest_sha':sha(P/'REPLAY_INPUTS.json'),'dispatcher_sha':sha(__file__)}
   if out.exists():receipt['output_sha']=sha(out)
   receipts.append(receipt);(OUT/f'bridge_{b}.receipt.json').write_text(json.dumps(receipt,indent=2))
   if reason or code or not out.exists():raise RuntimeError('bridge failed '+str(b))
  low=Fraction(0);high=Fraction(0)
  for b in (0,3,9,12,36,96):
   z=json.loads((OUT/f'bridge_{b}.json').read_text());a,c=map(Fraction,z['interval'])
   if a>c or z['bridge']!=b:raise ValueError('interval')
   low+=a;high+=c
  total=10+time.monotonic()-start
  if total>1200:raise RuntimeError('aggregate cap')
  summary={'status':'complete','interval_exact':[str(low),str(high)],'excludes_zero':low>0 or high<0,'charged_seconds':total,'prior_charge_seconds':10,'receipts':receipts,'scope':'independent exact rational residual certificate; adjacent bilinear only'}
  (OUT/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
  if 10+time.monotonic()-start>1200:raise RuntimeError('final aggregate cap')
 except BaseException as e:
  (OUT/'FAILURE.json').write_text(json.dumps({'error':repr(e),'charged_seconds':10+time.monotonic()-start,'receipts':receipts},indent=2));raise
if __name__=='__main__':main()

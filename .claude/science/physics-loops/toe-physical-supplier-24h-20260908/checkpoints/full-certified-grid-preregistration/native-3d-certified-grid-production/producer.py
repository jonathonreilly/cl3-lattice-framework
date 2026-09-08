import sys
if not sys.flags.isolated:raise RuntimeError('Python -I required')
from pathlib import Path
import argparse,runpy,json,signal,time,resource,itertools,hashlib
B=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--job',type=int,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 if not 0<=a.job<24:raise ValueError('job range')
 out=Path(a.output);out.mkdir(exist_ok=False);start=time.monotonic();signal.alarm(170)
 guard=runpy.run_path(str(B/'verify.py'));freeze=guard['verify']()
 try:
  import numpy as np
  guard['verify_numpy'](np)
  build=runpy.run_path(str(B/'matrix.py'))['build'];certify=runpy.run_path(str(B/'exact_certificate.py'))['certificate']
  cubes=json.loads((B/'CUBE_INPUTS.json').read_text());trig=json.loads((B/'TRIG_INPUTS.json').read_text())
  if trig['grid_n']!=32 or [x['j'] for x in trig['rows']]!=list(range(32)):raise ValueError('grid input')
  rep=(0,1,3,5,10,15)[a.job//4];block=a.job%4;count=0;times=[0.,0.,0.,0.]
  with (out/'NODES.jsonl').open('x') as file:
   for index in itertools.product(range(4*block,4*block+4),range(16),range(16)):
    t=time.monotonic();D,r=build(cubes['rows'][rep],[trig['rows'][j] for j in index]);A=np.array(D,dtype=complex);times[0]+=time.monotonic()-t
    t=time.monotonic();ev,Q=np.linalg.eigh(A);times[1]+=time.monotonic()-t
    t=time.monotonic();cert=certify(D,Q.tolist(),ev.tolist(),r);times[2]+=time.monotonic()-t
    t=time.monotonic();row=dict(job=a.job,rep=rep,index=index,eigenvalues_hex=[float(x).hex() for x in ev],vectors_hex=[[[float(z.real).hex(),float(z.imag).hex()] for z in line] for line in Q],certificate=cert);file.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n');file.flush();times[3]+=time.monotonic()-t;count+=1
  rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if count!=1024 or time.monotonic()-start>170 or rss>384*1048576:raise ValueError('job coverage/resources')
  result=dict(job=a.job,rep=rep,block=block,nodes=count,freeze=freeze,node_sha=hashlib.sha256((out/'NODES.jsonl').read_bytes()).hexdigest(),seconds=time.monotonic()-start,peak_bytes=rss,component_seconds=times)
  (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 except BaseException as e:
  (out/'FAILURE.json').write_text(json.dumps(dict(job=a.job,error=type(e).__name__,message=str(e),seconds=time.monotonic()-start))+'\n');raise
if __name__=='__main__':main()

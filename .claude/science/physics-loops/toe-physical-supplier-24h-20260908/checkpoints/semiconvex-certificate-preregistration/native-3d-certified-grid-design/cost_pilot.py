"""UNLAUNCHED: exact fixed96 candidate matrices, external30s384MiB required."""
import sys
if not sys.flags.isolated:raise RuntimeError('Python -I required')
from pathlib import Path
import argparse,json,runpy,time,signal,resource,hashlib,itertools
B=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-cost-pilot',action='store_true',required=True);ap.parse_args()
 if (B/'COST_STARTED.json').exists():raise ValueError('single attempt already started')
 signal.alarm(28);start=time.monotonic()
 guard=runpy.run_path(str(B/'verify.py'));freeze=guard['verify']()
 with (B/'COST_STARTED.json').open('x') as receipt:receipt.write(json.dumps(dict(freeze=freeze,utc=time.time()))+'\n')
 import numpy as np
 guard['verify_numpy'](np)
 build=runpy.run_path(str(B/'matrix.py'))['build'];certify=runpy.run_path(str(B/'exact_certificate.py'))['certificate']
 cubes=json.loads((B/'CUBE_INPUTS.json').read_text());trig=json.loads((B/'TRIG_INPUTS.json').read_text())
 if trig['grid_n']!=32 or [x['j'] for x in trig['rows']]!=list(range(32)):raise ValueError('trig membership')
 summaries=[]
 with (B/'CANDIDATES.jsonl').open('x') as file:
  for rep in (0,1,3,5,10,15):
   for index in itertools.product((0,4,8,12),(0,8),(0,8)):
    t=time.monotonic();D,radius=build(cubes['rows'][rep],[trig['rows'][j] for j in index]);array=np.array(D,dtype=complex);buildtime=time.monotonic()-t
    t=time.monotonic();ev,Q=np.linalg.eigh(array);eigtime=time.monotonic()-t
    t=time.monotonic();cert=certify(D,Q.tolist(),ev.tolist(),radius);certtime=time.monotonic()-t
    t=time.monotonic();row=dict(rep=rep,index=index,eigenvalues_hex=[float(x).hex() for x in ev],vectors_hex=[[[float(z.real).hex(),float(z.imag).hex()] for z in line] for line in Q],certificate=cert)
    file.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n');file.flush();iotime=time.monotonic()-t
    summaries.append(dict(rep=rep,index=index,build_seconds=buildtime,eigh_seconds=eigtime,certificate_seconds=certtime,serialization_seconds=iotime))
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if len(summaries)!=96 or time.monotonic()-start>28 or rss>384*1048576:raise ValueError('fixed coverage/resource')
 result=dict(freeze=freeze,rows=summaries,candidate_sha=hashlib.sha256((B/'CANDIDATES.jsonl').read_bytes()).hexdigest(),internal_seconds=time.monotonic()-start,peak_bytes=rss,scope='cost only; no grid integral or density sign')
 (B/'COST_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()

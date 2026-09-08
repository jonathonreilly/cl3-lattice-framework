"""UNLAUNCHED. Requires separate root authorization and external30s/384MiB guard."""
import sys
if not sys.flags.isolated:raise RuntimeError("isolated Python -I required")
import argparse,hashlib,json,os,resource,signal,time
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--run-cost-pilot',action='store_true',required=True);p.parse_args()
 root=Path(__file__).resolve().parent;out=root/'COST_RESULT.json'
 if out.exists():raise RuntimeError('existing result; no rerun')
 signal.alarm(30);start=time.monotonic()
 import runpy
 guard=runpy.run_path(str(root/'verify.py'));guard['verify']()
 import numpy as np
 guard['verify_numpy'](np)
 data=json.loads((root/'INPUTS.json').read_text());reps=[0,1,3,5,10,15];rows=[]
 import itertools
 for rep in reps:
  terms=data['rows'][rep]['terms']
  for ijk in itertools.product(range(4),range(2),range(2)):
   k=[2*np.pi*(n+.5)/d for n,d in zip(ijk,[4,2,2])];h=np.zeros((64,64),complex)
   for i,j,e,s in terms:h[i,j]+=s*np.exp(1j*sum(a*b for a,b in zip(k,e)))
   if np.max(np.abs(h-h.conj().T))>1e-12:raise RuntimeError('Hermitian control')
   t=time.monotonic();ev=np.linalg.eigvalsh(h);dt=time.monotonic()-t
   if not np.all(np.isfinite(ev)) or abs(sum(ev))>1e-9 or abs(sum(ev*ev)-384)>1e-8:raise RuntimeError('spectral arithmetic control')
   rows.append({'rep':rep,'index':ijk,'k':k,'eigenvalues':ev.tolist(),'eigvalsh_seconds':dt})
 seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if len(rows)!=96 or seconds>=30 or not 0<rss<384:raise RuntimeError('coverage/resource')
 out.write_text(json.dumps({'status':'cost pilot complete, not an integral certificate','seconds':seconds,'rss_mib':rss,'numpy_version':np.__version__,'input_sha256':hashlib.sha256((root/'INPUTS.json').read_bytes()).hexdigest(),'rows':rows},indent=2)+'\n')
if __name__=='__main__':main()

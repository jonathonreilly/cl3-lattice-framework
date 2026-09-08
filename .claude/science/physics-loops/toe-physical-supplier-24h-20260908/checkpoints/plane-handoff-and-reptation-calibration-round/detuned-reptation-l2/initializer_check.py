import time,json,pathlib
import numpy as np
import graph as g
from initializer import powers
p=pathlib.Path(__file__).resolve().parent;t=time.monotonic();checks=0;times=[]
for n in [48,192,768]:
 st=time.monotonic();psi,scale=powers(n)
 for k in range(1,n+1):
  actual=g.G@psi[k-1]
  if np.max(abs(actual-scale[k-1]*psi[k]))>1e-13:raise RuntimeError('power recurrence')
  # Summing all24 legal labels plus aggregate self reproduces conditional normalizer at every state.
  target=np.maximum(g.T,0);w=(np.where(g.T>=0,1/24,0)*psi[k-1,target]).sum(1)+(1-.95*g.nf/24)*psi[k-1]
  if np.max(abs(w-actual))>1e-13:raise RuntimeError('labeled sum')
  checks+=2
 # Deterministic all-self path telescoping, no RNG or production sample.
 x=0;logprob=np.log(psi[n,x]/psi[n].sum())
 for k in range(n,0,-1):logprob+=np.log((1-.95*g.nf[x]/24)*psi[k-1,x]/(scale[k-1]*psi[k,x]))
 logtarget=n*np.log(1-.95*g.nf[x]/24)-sum(np.log(scale))-np.log(psi[n].sum())
 if abs(logprob-logtarget)>1e-10:raise RuntimeError('telescoping')
 checks+=1;times.append(dict(n=n,seconds=time.monotonic()-st))
out=dict(checks=checks,times=times,total=time.monotonic()-t,scope='deterministic finite probabilities, no stochastic pilot');(p/'INITIALIZER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

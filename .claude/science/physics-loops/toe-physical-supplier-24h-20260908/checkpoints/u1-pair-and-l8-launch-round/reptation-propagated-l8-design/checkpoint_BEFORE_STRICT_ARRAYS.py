"""Lossless local-path checkpoint. Not a production driver."""
from pathlib import Path as File
import json
import numpy as np
from core import Path,count

def save(file,a,rng,L,accumulator):
 # All cumulative measurement/counter/tag state must be supplied by the caller.
 meta=dict(L=L,n=a.n,head=a.head,direction=a.direction,rng=rng.bit_generator.state,accumulator=accumulator)
 np.savez_compressed(file,metadata=np.array(json.dumps(meta,allow_nan=False)),labels=a.labels,states=np.array(a.states),nf=np.array(a.nf),O=np.array(a.O))

def load(file):
 with np.load(file,allow_pickle=False) as z:
  m=json.loads(str(z['metadata']));a=Path(m['L'],m['n']);a.head=m['head'];a.direction=m['direction'];a.labels=z['labels'].copy();a.states=[x.copy() for x in z['states']];a.nf=z['nf'].tolist();a.O=[x.copy() for x in z['O']]
 if a.direction not in [-1,1] or not 0<=a.head<a.n or a.labels.shape!=(a.n,) or np.any(a.labels < -1) or np.any(a.labels>=len(a.faces)):raise ValueError('path metadata')
 for j,x in enumerate(a.states):
  if x.shape!=(3*m['L']**3,) or np.any(x>1) or a.nf[j]!=count(x,a.faces) or np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))>1e-9:raise ValueError('cache')
 rng=np.random.default_rng();rng.bit_generator.state=m['rng']
 return a,rng,m['accumulator']

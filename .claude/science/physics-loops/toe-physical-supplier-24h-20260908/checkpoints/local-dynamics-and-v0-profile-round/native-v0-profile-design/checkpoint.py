"""Lossless local-path checkpoint. Not a production driver."""
from pathlib import Path as File
import json
import numpy as np
from core import Path,count

def save(file,a,rng,L,accumulator):
 # All cumulative measurement/counter/tag state must be supplied by the caller.
 meta=dict(V=a.V,L=L,n=a.n,head=a.head,direction=a.direction,rng=rng.bit_generator.state,accumulator=accumulator)
 np.savez_compressed(file,metadata=np.array(json.dumps(meta,allow_nan=False)),labels=a.labels,states=np.array(a.states),nf=np.array(a.nf),O=np.array(a.O))

def load(file,expected=None):
 with np.load(file,allow_pickle=False) as z:
  m=json.loads(str(z['metadata']))
  if type(m.get('V')) not in (int,float) or not np.isfinite(m['V']) or not 0<=m['V']<=1:raise ValueError('checkpoint V')
  if expected is not None and m['V']!=expected['V']:raise ValueError('checkpoint V mismatch')
  if any(type(m[k]) is not int for k in ['L','n','head','direction']) or m['L']<2 or m['L']%2 or m['n']<=0 or m['n']%2 or m['direction'] not in [-1,1] or not 0<=m['head']<m['n']:raise ValueError('integer path metadata')
  if expected is not None and (m['L']!=expected['L'] or m['n']!=expected['n']):raise ValueError('checkpoint configuration dimensions')
  labels=z['labels'].copy();states=z['states'].copy();nf=z['nf'].copy();obs=z['O'].copy();L=m['L'];n=m['n'];modes=6 if L==2 else 12
  if labels.shape!=(n,) or states.shape!=(3,3*L**3) or nf.shape!=(3,) or obs.shape!=(3,modes):raise ValueError('array shapes')
  if any(not np.issubdtype(x.dtype,np.integer) for x in [labels,states,nf]):raise ValueError('integer array dtypes')
  if np.any(labels < -1) or np.any(labels>=3*L**3) or np.any(states<0) or np.any(states>1) or not np.isfinite(obs).all():raise ValueError('array domains/finiteness')
  a=Path(L,n,m['V']);a.head=m['head'];a.direction=m['direction'];a.labels=labels;a.states=[x.copy() for x in states];a.nf=nf.tolist();a.O=[x.copy() for x in obs]
 for j,x in enumerate(a.states):
  if a.nf[j]!=count(x,a.faces) or np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))>1e-9:raise ValueError('cache')
 rng=np.random.default_rng();rng.bit_generator.state=m['rng']
 return a,rng,m['accumulator']

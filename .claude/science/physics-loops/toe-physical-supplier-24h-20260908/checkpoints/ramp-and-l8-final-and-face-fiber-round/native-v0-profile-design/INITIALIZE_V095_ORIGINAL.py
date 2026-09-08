import numpy as np
from core import Path,legal,count,next_count

def initialize(L,n,rng,rk_sweeps=128):
 if type(rk_sweeps) is not int or rk_sweeps<0:raise ValueError('RK sweeps')
 a=Path(L,n);x=a.states[0].copy();M=len(a.faces)
 for step in range(rk_sweeps*M):
  f=int(rng.integers(M))
  if legal(x,a.faces[f]):x[a.faces[f]]^=1
 nf=count(x,a.faces);O=a.coeff@(x.astype(float)-.5)
 a.states[0]=x.copy();a.nf[0]=nf;a.O[0]=O.copy();nonself=0
 for j in range(n):
  u=rng.random()*(M+.05*nf);f=int(u) if u<M else -1
  label=f if f>=0 and legal(x,a.faces[f]) else -1;a.labels[j]=label
  if label>=0:
   face=a.faces[label];nf=next_count(x,label,a.faces,a.affected,nf);O+=a.coeff[:,face]@(1.-2*x[face]);x[face]^=1;nonself+=1
  if j+1==n//2:a.states[1]=x.copy();a.nf[1]=nf;a.O[1]=O.copy()
 a.states[2]=x.copy();a.nf[2]=nf;a.O[2]=O.copy()
 return a,dict(rk_sweeps=rk_sweeps,rk_proposals=rk_sweeps*M,Q_steps=n,nonself_Q_steps=nonself,law='finite RK start followed by productQ; not equilibrium productG path law')

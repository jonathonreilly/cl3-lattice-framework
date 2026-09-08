import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np,itertools,json,hashlib
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/detuned-reptation-local');src=(p/'core.py').read_text();ns={};exec(compile(src,str(p/'core.py'),'exec'),ns)
r=np.load(p/'MICRO_RAW.npz');L=4;M=192
# Independent integer-coordinate geometry and direct Fourier coefficients.
coords=[(v//16,(v//4)%4,v%4) for v in range(64)]
def edge(c,a):return 3*(16*c[0]+4*c[1]+c[2])+a
faces=[]
for a,b in [(0,1),(0,2),(1,2)]:
 for c in coords:
  ca=list(c);cb=list(c);ca[a]=(ca[a]+1)%4;cb[b]=(cb[b]+1)%4
  faces.append([edge(c,a),edge(ca,b),edge(cb,a),edge(c,b)])
faces=np.array(faces);coeff=np.zeros((6,192),complex)
for row,(a,b) in enumerate([(a,b) for a in range(3) for b in range(3) if a!=b]):
 for c in coords:coeff[row,edge(c,b)]=(-1)**sum(c)*(1j)**c[a]/8
assert np.max(abs(coeff-ns['geometry'](4)[1]))<1e-15
assert np.array_equal(faces,ns['geometry'](4)[0])
def nf(x):
 return sum(tuple(x[f]) in ((0,1,0,1),(1,0,1,0)) for f in faces)
def toggle(x,f):
 y=x.copy()
 if f>=0:y[faces[f]]=1-y[faces[f]]
 return y
def degree(x):
 return [sum(x[edge(c,a)]+x[edge(tuple((c[j]-1)%4 if j==a else c[j] for j in range(3)),a)] for a in range(3)) for c in coords]
def flux(x):return [sum((-1)**sum(c)*(x[edge(c,a)]-.5) for c in coords if c[a]==0) for a in range(3)]
path=[r['left'].copy()]
for f in r['labels']:
 if f>=0:assert tuple(path[-1][faces[f]]) in ((0,1,0,1),(1,0,1,0))
 path.append(toggle(path[-1],int(f)))
assert np.array_equal(path[192],r['mid']) and np.array_equal(path[-1],r['right'])
for x in path:
 assert degree(x)==[3]*64 and flux(x)==flux(path[0])
for i,k in enumerate([0,192,384]):
 assert nf(path[k])==r['Nf'][i] and np.max(abs(coeff@(path[k].astype(float)-.5)-r['O'][i]))<1e-12
# Actual core on deterministic short windows from preserved path, every face and self.
class Fixed:
 def __init__(self,u,v):self.a=iter([u,v])
 def random(self):return next(self.a)
def controls(source):
 env={};exec(compile(source,'<core>','exec'),env);cases=0;rejects=0
 starts=[j for j in range(380) if np.any(r['labels'][j:j+4]>=0)][:6]
 for n in [2,4]:
  for start in starts:
   full=path[start:start+n+1];labels=r['labels'][start:start+n]
   for d in [-1,1]:
    old=full[-1] if d==1 else full[0];near=full[1] if d==1 else full[-2];width=M+.05*nf(old);ratio=min(1,(M+.05*nf(old))/(M+.05*nf(near)))
    for f in range(M+1):
     u=(f+.5)/width if f<M else (M+.025*nf(old))/width
     lab=f if f<M and tuple(old[faces[f]]) in ((0,1,0,1),(1,0,1,0)) else -1
     for coin in [0.,np.nextafter(1.,0.)]:
      a=env['Path'](4,n);a.direction=d;a.labels=labels.copy();a.states=[full[0].copy(),full[n//2].copy(),full[-1].copy()];a.nf=list(map(nf,a.states));a.O=[coeff@(x.astype(float)-.5) for x in a.states]
      acc=coin<ratio;got=a.step(Fixed(u,coin));expected=full[1:]+[toggle(old,lab)] if d==1 else [toggle(old,lab)]+full[:-1]
      if not acc:expected=full
      if got!=(lab,acc) or a.direction!=(d if acc else -d):raise RuntimeError('event')
      for k,z in enumerate([expected[0],expected[n//2],expected[-1]]):
       if not np.array_equal(a.states[k],z) or a.nf[k]!=nf(z) or np.max(abs(a.O[k]-coeff@(z.astype(float)-.5)))>1e-12:raise RuntimeError('cache')
      recon=a.states[0].copy()
      for lab0 in np.roll(a.labels,-a.head):recon=toggle(recon,int(lab0))
      if not np.array_equal(recon,a.states[2]):raise RuntimeError('label buffer')
      cases+=1;rejects+=not acc
 return cases,rejects
base=controls(src);bad=src.replace('(self.head+self.n//2)%self.n','(self.head+self.n//2-1)%self.n')
try:controls(bad)
except RuntimeError as e:mutant=str(e)
else:raise RuntimeError('midpoint mutant survived')
print(json.dumps({'core_sha':hashlib.sha256(src.encode()).hexdigest(),'all_L4_Fourier_coefficients':1152,'saved_path_degree_and_flux_states':len(path),'deterministic_local_core_cases':base[0],'rejection_cases':base[1],'actual_plus_midpoint_mutant_failure':mutant},indent=2))

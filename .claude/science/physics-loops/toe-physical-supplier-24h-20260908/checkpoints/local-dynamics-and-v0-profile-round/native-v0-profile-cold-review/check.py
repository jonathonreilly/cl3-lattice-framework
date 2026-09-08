from pathlib import Path
import sys,json,hashlib
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/native-v0-profile-design');sys.path.insert(0,str(p))
from checkpoint import load
from profile import vector,advance,accumulator
from observables import OrderMenu
checks=0
def req(x):
 global checks
 checks+=1
 if not x:raise RuntimeError('independent profile invariant')
for V in (.95,0.):
 a,r,s=load(p/f'CONTROL_V{V}_split3.npz',dict(L=2,n=24,V=V));q=vector(a,OrderMenu(2));S=sum(abs(z)**2 for z in a.O[1]);l=(V-1)*a.nf[0];rr=(V-1)*a.nf[2];E=(l+rr)/2
 req(np.allclose(q[:9],[a.nf[1],S,0,E,l*rr,S*E,0,S*S,0],atol=1e-12,rtol=0));req(np.allclose(np.array(s['raw']).sum(0),np.array(s['batch']).sum(0),atol=1e-12));req(len(q)==154)
# No Markov steps: use fixed state stand-in solely to exercise actual cadence/accumulator.
class Fixed:
 direction=1;n=110592;V=0.;nf=[2,3,4];O=[np.ones(12)]*3
 states=[np.zeros(1536,dtype=int)]*3
 def step(self,r):return -1,True
menu=OrderMenu(8);a=Fixed();s=accumulator();advance(a,None,s,menu,4096+8192);req(s['snapshots']==5);req(np.count_nonzero(np.any(np.array(s['batch']),axis=1))==2);saved=json.loads(json.dumps(s));advance(a,None,s,menu,4096+24576);advance(a,None,saved,menu,4096+24576);req(s==saved);req(s['snapshots']==16)
out={'checks':checks,'scope':'Deterministic saved-checkpoint read and fixed-state cadence stub; no stochastic update or cost profile','freeze':hashlib.sha256((p/'FINAL_FREEZE.json').read_bytes()).hexdigest()};Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

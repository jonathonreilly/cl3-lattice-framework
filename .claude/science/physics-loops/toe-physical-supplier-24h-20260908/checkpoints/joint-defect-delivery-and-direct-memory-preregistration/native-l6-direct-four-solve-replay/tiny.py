import sys,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
for name in ('envelope','transport','fp_guard','validate_coefficients','review'):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
import review as r
import numpy as np
checks=0
for p in (0,1):
 x=np.array([F(i-3,8) for i in range(8)],dtype=float)
 for j in range(4):
  for kind in ('A','B'):
   want=np.zeros(8)
   for i,v in enumerate(x):
    bits=i|(((i.bit_count()&1)^p)<<3);sg=(-1)**((bits&((1<<j)-1)).bit_count())
    if kind=='B':sg*=2*((bits>>j)&1)-1
    target=(bits^(1<<j))&7;want[target]+=v*sg
   r.same(r.linear(x,p,[(j,1.)],kind),want);checks+=1
 _,b=r.norm(x,p);expected=[F(0)]*22
 for i,v in enumerate(x):expected[i.bit_count()+((i.bit_count()&1)^p)]+=F(float(v))**2
 if [F(z,1<<2148) for z in b]!=expected:raise ValueError('norm')
 checks+=1
for value in (float.fromhex('0x0.0000000000001p-1022'),-0.,float.fromhex('0x1.fffffffffffffp+1023')):
 _,b=r.norm(np.array([value]),0)
 if F(sum(b),1<<2148)!=F(value)**2:raise ValueError('dyadic extreme')
 checks+=1
try:r.same(np.array([0.]),np.array([-0.]));raise RuntimeError('survived signedzero')
except ValueError:checks+=1
for name,old,rho in [('firstP',{'candidate_attempts':'1'},F(1,10**10)),('secondO',{'candidate_attempts':'1'},F(1,10**9))]:
 r.contract_certificate(name,old,rho);checks+=1
for name,old,rho in [('firstP',{'candidate_attempts':'2'},F(0)),('secondP',{'candidate_attempts':1},F(0)),('firstP',{'candidate_attempts':'1'},F(1,10**9)),('secondO',{'candidate_attempts':'1'},F(1,10**8))]:
 try:r.contract_certificate(name,old,rho);raise RuntimeError('guard survived')
 except ValueError:checks+=1
rows=[(0,.1),(2,-.3),(4,.7),(5,-.2)];x=np.array([(-1.)**i*(1e16 if i%5==0 else (i-30)/7) for i in range(64)])
for p in (0,1):
 for kind in ('A','B'):
  want=np.zeros(64)
  for lo in range(0,64,8):
   for j,c in rows:
    for src in range(lo,lo+8):
     bits=src|(((src.bit_count()&1)^p)<<6);sg=(-1)**((bits&((1<<j)-1)).bit_count())
     if kind=='B':sg*=2*((bits>>j)&1)-1
     dst=src^(1<<j);want[dst]+=(x[src]*c)*sg
  r.same(r.linear(x,p,rows,kind,chunk=8),want);checks+=1
d={'active':[0,1,6,7,12,13,18,19],'spectators':[j for j in range(21) if j not in [0,1,6,7,12,13,18,19]],'signed_sigma':[1.]*8,'svd_orientation':[1,-1],'delta_active':2.,'minimum_denominator':.5,'alignment_planes':[[1,2,-.1,'AA'],[1,2,.1,'BB']],'active_planes':[[0,1,.2,'AA']],'alignment_givens':1,'spin_passes':6}
r.diagnostics(d);checks+=1
import copy
for key,value in [('active',list(range(8))),('minimum_denominator',0.),('spin_passes',8),('signed_sigma',[1.]*7),('svd_orientation',[0,1])]:
 bad=copy.deepcopy(d);bad[key]=value
 try:r.diagnostics(bad);raise RuntimeError('diagnostic mutant survived')
 except ValueError:checks+=1
print(json.dumps({'status':'PASS','predicates':checks,'physical_calls':0}))

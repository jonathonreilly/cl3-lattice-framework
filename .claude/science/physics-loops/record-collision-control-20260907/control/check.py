import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools,json,hashlib,time,resource,signal,sys
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic();N=9
I='I'*N
def word(**kw):
 s=list(I)
 for k,v in kw.items():s[int(k)]=v
 return ''.join(s)
def w(i,a):return I[:i]+a+I[i+1:]
def mul(a,b):
 out=[];phase=1
 for x,y in zip(a,b):
  if x=='I':out.append(y)
  elif y=='I':out.append(x)
  elif x==y:out.append('I')
  else:
   out.append(({'X','Y','Z'}-{x,y}).pop());phase*=1j if (x,y) in [('X','Y'),('Y','Z'),('Z','X')] else -1j
 return ''.join(out),phase
def add(d,k,v):
 d[k]=d.get(k,F(0))+v
 if d[k]==0:del d[k]
def comm(a,b):
 # [a,b]/(2i), real coefficients for Hermitian Pauli inputs
 out={}
 for x,c in a.items():
  for y,d in b.items():
   z,p=mul(x,y)
   if p.imag:add(out,z,c*d*int(p.imag))
 return out
Zf=w(4,'Z');Yx=w(3,'Y');ZfYx=mul(Zf,Yx)[0]
Qa={I:F(1,2),Yx:F(1,2),Zf:F(-1,2),ZfYx:F(-1,2)}
K=dict(Qa)
for a,c in {I:F(2),w(5,'Z'):F(-1,2),w(6,'Z'):F(-1)}.items():add(K,a,c)
Zr={w(0,'Z'):F(1)};Nh={I:F(1),w(1,'Z'):F(-1,2),w(2,'Z'):F(-1,2)}
def solve(graph,strict=False):
 basis=[] if strict else [I]+[w(i,a) for i in range(N) for a in 'XYZ']
 basis += [mul(w(i,a),w(j,b))[0] for i,j in graph for a in 'XYZ' for b in 'XYZ']
 rows={}
 for col,x in enumerate(basis):
  for family,op in enumerate((K,Zr,Nh)):
   for key,v in comm({x:F(1)},op).items():rows.setdefault((family,key),{})[col]=v
 piv={}
 for row in rows.values():
  row=dict(row)
  while row:
   p=min(row)
   if p not in piv:
    v=row[p];piv[p]={k:x/v for k,x in row.items()};break
   v=row[p]
   for k,x in piv[p].items():add(row,k,-v*x)
 gens=[]
 for free in range(len(basis)):
  if free in piv:continue
  vec={free:F(1)}
  for p,row in sorted(piv.items(),reverse=True):
   v=-sum((x*vec.get(k,0) for k,x in row.items() if k!=p),F(0))
   if v:vec[p]=v
  g={basis[k]:v for k,v in vec.items()}
  assert all(not comm(g,op) for op in (K,Zr,Nh))
  gens.append(g)
 return {'columns':len(basis),'rank':len(piv),'nullity':len(gens),'all_commute_active_energy':all(not comm(g,Qa) for g in gens),'fuel_noncommuting_generators':sum(bool(comm(g,{Zf:F(1)})) for g in gens),'basis':[{k:str(v) for k,v in g.items()} for g in gens]}
complete=list(itertools.combinations(range(N),2));path=[(i,i+1) for i in range(N-1)]
results={name:solve(graph,strict) for name,graph,strict in [('complete_at_most_two',complete,False),('path_at_most_two',path,False),('complete_exactly_two',complete,True),('path_exactly_two',path,True)]}
Xf=w(4,'X');cancel={Xf:F(1),mul(Xf,Yx)[0]:F(-1)}
assert not comm(cancel,K) and not comm(cancel,Zr) and not comm(cancel,Nh)
assert comm({Xf:F(1)},K)
assert not comm(K,K) and not comm({I:F(1)},K)
assert comm({w(0,'X'):F(1)},Zr)
# Every path generator is exactly in the complete allowed span because its support is a subset and its constraints vanish.
for gen in results['path_at_most_two']['basis']:
 assert all(sum(c!='I' for c in p)<=2 for p in gen)
 assert all(not comm({k:F(v) for k,v in gen.items()},op) for op in (K,Zr,Nh))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert rss<180 and time.monotonic()-start<180
print(json.dumps({'results':results,'controls':{'sum_cancellation_allowed':True,'fuel_flip_rejected':True,'old_record_flip_rejected':True,'identity_and_energy_allowed':True,'path_subset':True},'source_active_energy':2,'target_active_energy':0,'source_target_total_energy':'5/2','source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss},indent=2))

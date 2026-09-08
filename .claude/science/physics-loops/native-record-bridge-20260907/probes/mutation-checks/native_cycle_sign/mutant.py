import itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex)
def word(terms):
 a=np.array([[1]],complex)
 for j in range(4):a=np.kron(a,terms.get(j,I))
 return a
Is=word({});Xs=[word({j:X}) for j in range(4)];Zs=[word({j:Z}) for j in range(4)]
A=[Xs[0],Zs[0]@Xs[1],Zs[1]@Xs[2]@Zs[3],Zs[0]@Xs[3]]
S=A[0]@A[1]@A[2]@A[3];P=(Is+S)/2
B=[Zs[0]@Zs[3],Zs[0]@Zs[1],Zs[1]@Zs[2],Zs[2]@Zs[3]]
checks=[]
def check(name,truth):
 if not truth:raise AssertionError(name)
 checks.append(name)
def eq(a,b):return np.max(np.abs(a-b))<1e-12
check('actual cycle stabilizer equals minus X Y X Y',eq(S,-word({0:X,1:Y,2:X,3:Y})))
check('cycle code projector rank8',eq(P@P,P) and abs(np.trace(P)-8)<1e-12)
V=P.copy()
for b in B:V=V@(Is+b)/2
om=np.zeros(16,complex);om[0]=om[-1]=1/math.sqrt(2)
rho=np.outer(om,om.conj())
check('literal code vacuum rank1 equals independent GHZ vector',eq(V,rho) and abs(np.trace(V)-1)<1e-12)
check('four vertex occupations zero',all(eq(b@om,om) for b in B))
centers=[(1,0,0),(2,1,0),(1,2,0),(0,1,0)]
def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
check('actual target physical sites form independent set',all(dist(a,b)>1 for a,b in itertools.combinations(centers,2)))
check('central mediator adjacent to all4 targets',all(dist(a,(1,1,0))==1 for a in centers))
check('opposite edge lies outside physical nearest-neighbor shell',dist(centers[0],centers[2])==2)
Q={(e,z):(Is+z*Zs[e])/2 for e in range(4) for z in [-1,1]}
for e,z in Q:check(f'initial edge{e} sign{z} fair',abs(np.trace(Q[e,z]@rho)-.5)<1e-12)
for e,f in itertools.permutations(range(4),2):
 for z in [-1,1]:
  post=Q[f,z]@rho@Q[f,z]*2
  check(f'fixed vacuum edge{f} sign{z} forces edge{e}',abs(np.trace(Q[e,z]@post)-1)<1e-12)
# Full native operator histories versus independent binary cycle-boundary enumeration.
cyclewords=[]
for bits in itertools.product([0,1],repeat=4):
 if all(bits[i]^bits[(i+1)%4]==0 for i in range(4)):cyclewords.append(bits)
check('binary incidence independently has exactly2 vacuum words',cyclewords==[(0,0,0,0),(1,1,1,1)])
maxres=0;nonzero=0
for order in itertools.permutations(range(4)):
 for signs in itertools.product([-1,1],repeat=4):
  state=rho.copy()
  for e,z in zip(order,signs):state=Q[e,z]@state@Q[e,z]
  actual=float(np.trace(state).real)
  independent=F(sum(all((1-2*b[e])==z for e,z in zip(order,signs)) for b in cyclewords),2)
  maxres=max(maxres,abs(actual-float(independent)));nonzero+=actual>1e-12
check('all384 ordered native histories equal independent cycle-word law',maxres<1e-12 and nonzero==48)
# Direct local-history kernel, including an auxiliary mediator and complete sign branches.
def history_law(sites):
 branches=[({},F(1))]
 for s in sites:
  nxt=[]
  for hist,weight in branches:
   nei=[v for t,v in hist.items() if dist(s,t)==1]
   p=F(sum(v==1 for v in nei),len(nei)) if nei else F(1,2)
   for z,w in [(1,p),(-1,1-p)]:nxt.append((dict(hist,**{})|{s:z},weight*w))
  branches=nxt
 out={}
 for hist,weight in branches:
  key=tuple(hist[t] for t in centers)
  out[key]=out.get(key,F(0))+weight
 return out
for order in itertools.permutations(centers):
 law=history_law([order[0],(1,1,0),*order[1:]])
 check('one-mediator exact marginal for target order'+str(order),all(v==(F(1,2) if len(set(k))==1 else 0) for k,v in law.items()) and sum(law.values())==1)
plain=history_law(centers)
check('unrelayed local process has independent16 equiprobable targetwords',len(plain)==16 and all(v==F(1,16) for v in plain.values()))
late=history_law([*centers,(1,1,0)])
check('late-mediator control does not repair earlier target probabilities',late==plain)
# Adverse implementations: actual forgetting of conditioning and wrong geometric chart.
wrong_post=rho
check('reset-before-second-event defect detected',abs(np.trace(Q[0,1]@wrong_post)-1)>.4)
wrong_centers=[(j,0,0) for j in range(4)]
check('consecutive-site reinterpretation detected',any(dist(a,b)==1 for a,b in itertools.combinations(wrong_centers,2)))
def tv(p,q):return 1-min(p*q,F(1,2))-min((1-p)*(1-q),F(1,2))
check('fair first marginal has TV1/2 for all101 rational second odds',all(tv(F(1,2),F(j,100))==F(1,2) for j in range(101)))
vals=[tv(F(i,100),F(j,100)) for i in range(101) for j in range(101)]
check('rational product-law grid respects analytical bound',min(vals)>math.sqrt(2)-1)
ans={'status':'bounded scratch probe; no science grade','checks':len(checks),'failed':0,'native_full_ordered_histories':384,'native_nonzero_histories':nonzero,'maximum_matrix_vs_binary_residual':maxres,'unrelayed_four_target_TV':str(1-sum(min(plain[k],F(1,2)) for k in plain if len(set(k))==1)),'relay_target_orders':24,'two_event_product_grid_min_TV':str(min(vals)),'checks_detail':checks}
Path(__file__).with_name('result.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({k:v for k,v in ans.items() if k!='checks_detail'},indent=2))

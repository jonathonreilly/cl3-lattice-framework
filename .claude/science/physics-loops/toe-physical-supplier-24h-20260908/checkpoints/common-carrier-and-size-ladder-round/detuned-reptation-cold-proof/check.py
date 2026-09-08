from fractions import Fraction as F
from itertools import product
import json,time,hashlib
from pathlib import Path
start=time.monotonic(); groups=[]
def require(ok,name):
 if not ok:raise RuntimeError(name)
 groups.append(name)
def matvec(G,x):return [sum((a*b for a,b in zip(row,x)),F(0)) for row in G]
def powervec(G,n):
 x=[F(1)]*len(G)
 for _ in range(n):x=matvec(G,x)
 return x
def test(G,n,label):
 m=len(G);b=[sum(row) for row in G]
 paths=[x for x in product(range(m),repeat=n+1) if all(G[x[i]][x[i+1]] for i in range(n))]
 weights={x:__import__('functools').reduce(lambda a,k:a*G[x[k]][x[k+1]],range(n),F(1)) for x in paths};Z=sum(weights.values())
 states=[(x,d) for x in paths for d in (1,-1)];idx={s:i for i,s in enumerate(states)}
 pi=[weights[x]/(2*Z) for x,d in states]
 def transitions(mode='correct'):
  rows=[]
  for x,d in states:
   out={};end=x[-1] if d==1 else x[0];new_end=x[1] if d==1 else x[-2]
   ratio=b[end]/b[new_end]
   if mode=='inverted':ratio=1/ratio
   if mode=='unaccepted':ratio=F(1)
   accept=min(F(1),ratio)
   for y in range(m):
    q=G[end][y]/b[end]
    if not q:continue
    xp=x[1:]+(y,) if d==1 else (y,)+x[:-1]
    j=idx[(xp,d)];out[j]=out.get(j,F(0))+q*accept
   j=idx[(x,d if mode=='hold-reject' else -d)]
   out[j]=out.get(j,F(0))+1-accept
   require(sum(out.values())==1,'stochastic-row-'+mode)
   rows.append(out)
  return rows
 def residual(P):
  incoming=[F(0)]*len(states)
  for i,row in enumerate(P):
   for j,p in row.items():incoming[j]+=pi[i]*p
  return max(abs(a-b) for a,b in zip(incoming,pi))
 P=transitions();require(residual(P)==0,'exact-lifted-stationarity')
 # Accepted-flow skew balance, including accepted self transitions.
 for i,(x,d) in enumerate(states):
  end=x[-1] if d==1 else x[0];newend=x[1] if d==1 else x[-2];a=min(F(1),b[end]/b[newend])
  for y in range(m):
   if not G[end][y]:continue
   xp=x[1:]+(y,) if d==1 else (y,)+x[:-1]
   old=x[0] if d==1 else x[-1]
   ep=xp[0] if d==1 else xp[-1];np=xp[-2] if d==1 else xp[1]
   rev_a=min(F(1),b[ep]/b[np])
   lhs=weights[x]*G[end][y]/b[end]*a
   rhs=weights[xp]*G[ep][old]/b[ep]*rev_a
   require(lhs==rhs,'accepted-skew-flow')
 # Directed reachability is sufficient to distinguish one-bond reducibility.
 def reachable(seed):
  seen={seed};front=[seed]
  while front:
   i=front.pop()
   for j,p in P[i].items():
    if p and j not in seen:seen.add(j);front.append(j)
  return seen
 irreducible=all(len(reachable(i))==len(states) for i in range(len(states)))
 expected=n>=2 and len(set(b))>1
 require(irreducible==expected,'lifted-irreducibility-boundary')
 g=powervec(G,n);require(sum(g)==Z,'path-transfer-normalization')
 for k in range(n+1):
  left=powervec(G,k);right=powervec(G,n-k)
  marginal=[sum(w for x,w in weights.items() if x[k]==j)/Z for j in range(m)]
  require(marginal==[a*c/Z for a,c in zip(left,right)],'all-position-marginals')
 if n%2==0:
  psi=powervec(G,n//2);Hpsi=[psi[j]-v for j,v in enumerate(matvec(G,psi))]
  pure=sum(a*c for a,c in zip(psi,Hpsi))/Z
  endpoint=sum(weights[x]*(1-b[x[-1]]) for x in paths)/Z
  require(pure==endpoint,'endpoint-energy-equals-finite-pure-energy')
 mutants={mode:str(residual(transitions(mode))) for mode in ('inverted','unaccepted','hold-reject')}
 if expected:require(all(F(v)>0 for v in mutants.values()),'actual-mutants-killed')
 return {'label':label,'bonds':n,'paths':len(paths),'lifted_states':len(states),'row_sums':list(map(str,b)),'normalizer':str(Z),'irreducible':irreducible,'mutant_stationarity_residuals':mutants}
fixtures=[]
G2=[[F(1),F(1,2)],[F(1,2),F(2)]]
G3=[[F(1),F(1,3),F(0)],[F(1,3),F(2),F(1,4)],[F(0),F(1,4),F(3,2)]]
Gc=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
for n in (1,2,3,4):fixtures.append(test(G2,n,'two-asymmetric'))
for n in (1,2,3,4):fixtures.append(test(G3,n,'three-sparse'))
for n in (1,2,4):fixtures.append(test(Gc,n,'constant-row-adverse'))
print(json.dumps({'checks':len(groups),'groups':{g:groups.count(g) for g in sorted(set(groups))},'fixtures':fixtures,'seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))

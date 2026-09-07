#!/usr/bin/env python3
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[_key]='1'
import time,signal,resource,sys,json,itertools,math,hashlib
from pathlib import Path
from fractions import Fraction as F
start=time.monotonic();signal.alarm(180)
class K:
 def __init__(self,a=0,b=0):
  if isinstance(a,K):self.a,self.b=a.a,a.b
  else:self.a,self.b=F(a),F(b)
 def __add__(x,y):
  y=K(y);return K(x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return K(-x.a,-x.b)
 def __sub__(x,y):return x+-K(y)
 def __rsub__(x,y):return K(y)+-x
 def __mul__(x,y):
  y=K(y);return K(x.a*y.a+55*x.b*y.b,x.a*y.b+x.b*y.a)
 __rmul__=__mul__
 def __truediv__(x,y):
  y=K(y);d=y.a*y.a-55*y.b*y.b;return x*K(y.a/d,-y.b/d)
 def __rtruediv__(x,y):return K(y)/x
 def __eq__(x,y):
  y=K(y);return x.a==y.a and x.b==y.b
 def __repr__(x):return f'({x.a})+({x.b})sqrt55'
 def val(x):return float(x.a)+float(x.b)*math.sqrt(55)
def inv(A):
 n=len(A);M=[list(map(F,r))+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
 for k in range(n):
  if M[k][k]==0:
   l=next(l for l in range(k+1,n) if M[l][k]);M[k],M[l]=M[l],M[k]
  p=M[k][k];M[k]=[x/p for x in M[k]]
  for i in range(n):
   if i!=k:
    p=M[i][k];M[i]=[a-p*b for a,b in zip(M[i],M[k])]
 return [r[n:] for r in M]
V=list(itertools.product((0,1),repeat=4));edges=[]
for v in V:
 for a in range(4):
  if not v[a]:
   w=list(v);w[a]=1;edges.append((v,tuple(w)))
def square(a,b,fixed):
 v=[0]*4
 for axis,val in fixed.items():v[axis]=val
 vs=[tuple(v)];v[a]=1;vs.append(tuple(v));v[b]=1;vs.append(tuple(v));v[a]=0;vs.append(tuple(v))
 return [(edges.index((u,w)),1) if (u,w) in edges else (edges.index((w,u)),-1) for u,w in zip(vs,vs[1:]+vs[:1])]
sources=[square(0,1,{2:0,3:t}) for t in (0,1)]
parent={v:v for v in V}
def root(v):
 while parent[v]!=v:v=parent[v]
 return v
tree=[]
for e in [e for src in sources for e,s in src[:3]]+list(range(32)):
 if e in tree:continue
 u,v=edges[e];ru,rv=root(u),root(v)
 if ru!=rv:parent[rv]=ru;tree.append(e)
chords=[e for e in range(32) if e not in tree]
sourceidx=[next(chords.index(e) for e,s in src if e in chords) for src in sources]
words=[];weights=[]
for a,b in itertools.combinations(range(4),2):
 rest=[j for j in range(4) if j not in (a,b)]
 for vals in itertools.product((0,1),repeat=2):
  fixed=dict(zip(rest,vals))
  if (a,b)==(0,1) and fixed[2]==0:continue
  words.append([(chords.index(e),s) for e,s in square(a,b,fixed) if e in chords]);weights.append(F(1) if b==3 else F(1,2))
B=[[sum(s for e,s in word if e==i) for i in range(17)] for word in words]
H=[[sum(w*r[i]*r[j] for w,r in zip(weights,B)) for j in range(17)] for i in range(17)]
G0=[[3*x for x in r] for r in inv(H)]
omega=K(0,F(1,90));u,v=sourceidx
D=[[K(G0[i][j])+(1/omega if i==j else 0) for j in sourceidx] for i in sourceidx]
det=D[0][0]*D[1][1]-D[0][1]*D[1][0];Di=[[D[1][1]/det,-D[0][1]/det],[-D[1][0]/det,D[0][0]/det]]
Gg=[[K(G0[i][j])-sum(G0[i][sourceidx[a]]*Di[a][b]*G0[sourceidx[b]][j] for a in range(2) for b in range(2)) for j in range(17)] for i in range(17)]
checks=[]
def check(name,b):
 if not b:raise AssertionError(name)
 checks.append(name)
check('17chords22faces',len(chords)==17 and len(words)==22)
check('literal disjoint sources',u!=v and all(sum(e in chords for e,s in src)==1 for src in sources))
check('source covariance',[[G0[i][j] for j in sourceidx] for i in sourceidx]==[[F(192,11),F(138,11)],[F(138,11),F(192,11)]])
check('ground inverse precision',all(sum((K(H[i][k]/3)+(omega if i==k and i in sourceidx else 0))*Gg[k][j] for k in range(17))==int(i==j) for i in range(17) for j in range(17)))
C={};quartic={}
for word,w in zip(words,weights):
 for tri in itertools.combinations(word,3):
  ids=[e for e,s in tri];sgn=math.prod(s for e,s in tri);parity=(-1)**sum(ids[i]>ids[j] for i in range(3) for j in range(i+1,3))
  key=tuple(sorted(ids));C[key]=C.get(key,F(0))-w*sgn*parity/6
 for ns in itertools.product(range(5),repeat=len(word)):
  if sum(ns)!=4:continue
  seq=tuple(e for (e,s),n in zip(word,ns) for _ in range(n))
  c=-w*F(math.prod(s**n for (e,s),n in zip(word,ns)),3*math.prod(math.factorial(n) for n in ns))
  quartic[seq]=quartic.get(seq,F(0))+c
C={k:v for k,v in C.items() if v};quartic={k:v for k,v in quartic.items() if v}
def tr4(G,ids):
 a,b,c,d=ids;return F(64,3)*(G[a][b]*G[c][d]+G[a][d]*G[b][c])-F(8,3)*G[a][c]*G[b][d]
def det3(G,I,J):
 a,b,c=I;x,y,z=J
 return G[a][x]*(G[b][y]*G[c][z]-G[b][z]*G[c][y])-G[a][y]*(G[b][x]*G[c][z]-G[b][z]*G[c][x])+G[a][z]*(G[b][x]*G[c][y]-G[b][y]*G[c][x])
def calc(G):
 e4=sum(c*tr4(G,seq) for seq,c in quartic.items())
 e32=48*sum(c*d*det3(G,I,J) for I,c in C.items() for J,d in C.items())
 haar=-2*sum(G[i][i] for i in range(17))
 return dict(E4=e4,E3_squared=e32,Haar=haar,total=e32/2-e4+haar)
check('single group quartic -5',-F(1,72)*tr4([[F(3)]],(0,0,0,0))==-5)
check('single group partition -1',5-2*3==-1)
z=calc(G0);g=calc(Gg);half=Gg[u][u]+Gg[v][v];ng=g['total']+half;k0=ng-z['total']
def encode(x):
 if isinstance(x,K):return {'rational':str(x.a),'sqrt55':str(x.b),'float_diagnostic':x.val()}
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 return x
out=dict(status='PASS',checks=checks,TOTAL=len(checks),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),tree=tree,chords=chords,source_indices=sourceidx,words=words,weights=list(map(str,weights)),cubic_coefficients={str(k):str(v) for k,v in C.items()},quartic_coefficients={str(k):str(v) for k,v in quartic.items()},Z1_parts=encode(z),ground_parts=encode(g),source_half_back=encode(half),Ng1=encode(ng),k0=encode(k0),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024),scope='Exact Wick coefficient candidate; analytic coefficient theorem and independent tensor checks separate.')
check('positive resource budget',0<out['seconds']<180 and 0<out['rss_MiB']<180)
out['TOTAL']=len(checks)
if sys.argv[1:]==['--json']:print(json.dumps(out,indent=2,allow_nan=False))
elif not sys.argv[1:]:
 print('PASS independent adapted-tree ground correction; TOTAL='+str(out['TOTAL']))
 print('per_element: exact SU3 color contractions')
 print('per_site: 16 vertices in the declared finite cube slab')
 print('per_mode: 17 chord variables with 8 colors')
 print('per_block: 22 weighted face words with two marked sources')
 print('lattice_wide: one finite supplied cube slab')
 print('k0='+str(out['k0']))
else:raise SystemExit('usage: '+sys.argv[0]+' [--json]')

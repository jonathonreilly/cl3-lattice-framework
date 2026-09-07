#!/usr/bin/env python3
"""Exact finite-volume physical SU3 cube gap support; analytical proof separate."""
import os,time,signal
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools as it,json,hashlib,sys,resource
if sys.argv[1:] not in ([], ['--json']):raise SystemExit('usage: '+sys.argv[0]+' [--json]')
import sympy as s
from collections import Counter
checks=[]
def ck(n,b):
 if n in checks or not bool(b):raise AssertionError(n)
 checks.append(n)
verts=list(it.product((0,1),repeat=3));edges=[]
for x in verts:
 for axis in range(3):
  if x[axis]==0:
   y=list(x);y[axis]=1;edges.append((verts.index(x),verts.index(tuple(y)),axis))
ck('cube geometry',len(verts)==8 and len(edges)==12)
raw=[];valid=[]
for mask in range(4096):
 d=[0]*8
 for e,(u,v,axis) in enumerate(edges):
  if mask>>e&1:d[u]+=1;d[v]+=1
 ok=bool(mask) and all(x!=1 for x in d)
 row=dict(mask=mask,edge_count=mask.bit_count(),degrees=d,no_degree_one=ok);raw.append(row)
 if ok:valid.append(row)
hist=Counter(x['edge_count'] for x in valid)
ck('minimum nonempty support four',min(hist)==4)
ck('no five edge support',hist[5]==0)
faces=[]
for a,b in it.combinations(range(3),2):
 other=next(x for x in range(3) if x not in (a,b))
 for bit in (0,1):
  x=[0]*3;x[other]=bit;xa=x.copy();xa[a]=1;xb=x.copy();xb[b]=1
  word=[]
  for start,axis,sign in [(x,a,1),(xa,b,1),(xb,a,-1),(x,b,-1)]:
   u=verts.index(tuple(start));e=next(j for j,(z,w,c) in enumerate(edges) if z==u and c==axis);word.append((e,sign))
  row=[0]*12
  for e,sign in word:row[e]+=sign
  faces.append(dict(axes=[a,b],fixed=bit,word=word,incidence=row,mask=sum(1<<e for e,sign in word)))
ck('all four supports are six faces',set(x['mask'] for x in valid if x['edge_count']==4)==set(x['mask'] for x in faces) and hist[4]==6)
ck('six edge supports are cycles',all(all(d in (0,2) for d in x['degrees']) for x in valid if x['edge_count']==6))
ck('six edge support exists',hist[6]>0)
chars=[dict(face=j,sign=sign,center=[sign*x for x in face['incidence']]) for j,face in enumerate(faces) for sign in (1,-1)]
def center(ids):return [sum(chars[i]['center'][e] for i in ids)%3 for e in range(12)]
pairs=[dict(ids=ids,center=center(ids)) for ids in it.product(range(12),repeat=2)]
ps=[r['ids'] for r in pairs if not any(r['center'])]
ck('character pair center survivors precisely conjugates',set(ps)=={(i,i^1) for i in range(12)})
triples=[dict(ids=ids,center=center(ids)) for ids in it.product(range(12),repeat=3)]
ts=[r['ids'] for r in triples if not any(r['center'])]
ck('triple center survivors precisely same oriented face cubes',set(ts)=={(i,i,i) for i in range(12)})
# Surviving Haar integrals=1 are proved via epsilon invariant in DERIVATION, not assumed from center alone.
M=s.Matrix(12,12,lambda i,j:sum((i^1,j,k) in ts for k in range(12)))
ck('first level insertion pairs conjugate faces',M==s.diag(*([s.Matrix([[0,1],[1,0]])]*6)))
ck('first insertion spectral multiplicities',M.eigenvals()=={s.Integer(-1):6,s.Integer(1):6})
p,q=s.symbols('p q',nonnegative=True,integer=True);A=s.Matrix([[s.Rational(2,3),s.Rational(1,3)],[s.Rational(1,3),s.Rational(2,3)]])
cas=(s.Matrix([[p,q]])*A*s.Matrix([p+2,q+2]))[0]
ck('weight metric Casimir exact',s.expand(cas-s.Rational(2,3)*(p*p+q*q+p*q+3*p+3*q))==0)
ck('fundamental kinetic dimensionless energy four',s.simplify(s.Rational(3,2)*cas.subs({p:1,q:0}))==4)
ck('next nonfundamental irrep minimum nine',min((i*i+j*j+i*j+3*i+3*j) for i,j in [(1,1),(2,0),(0,2)])==9)
x=s.symbols('x',nonnegative=True)
R=s.Matrix([[6*x,-x/s.sqrt(3)],[-x/s.sqrt(3),16+35*x/6]])
ck('Ritz crossing determinant',s.factor((R-16*s.eye(2)).det())==8*x*(13*x-35)/3)
ck('Ritz threshold trace positive',s.simplify(s.trace(R-16*s.eye(2)).subs(x,s.Rational(35,13)))>0)
mu=(s.trace(R)-s.sqrt((R[1,1]-R[0,0])**2+4*R[0,1]**2))/2
ck('ground second order coefficient',s.series(mu,x,0,3).removeO()==6*x-x*x/48)
ck('first gap first perturbation slope',s.Rational(35,6)-6==-s.Rational(1,6))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('resource limits',0<rss<180 and time.monotonic()-START<180)
payload=dict(checks=checks,TOTAL=len(checks),vertices=verts,edges=edges,faces=faces,supports=raw,valid_support_histogram=dict(sorted(hist.items())),signed_characters=chars,pair_patterns=pairs,pair_survivors=ps,triple_patterns=triples,triple_survivors=ts,first_level_S_matrix=[list(map(str,row)) for row in M.tolist()],Ritz_matrix=[list(map(str,row)) for row in R.tolist()],Ritz_ground_upper=str(mu),Ritz_gap_lower=str(16-mu),seconds=time.monotonic()-START,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope='Exact finite graph/center/Ritz controls; full Haar surviving integrals and all-representation spectrum proved separately.')

if sys.argv[1:]==['--json']:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS finite physical cube gap certificate; TOTAL='+str(payload['TOTAL']))
 print('per_element: Exact SU3 weight-metric and Ritz arithmetic; all-label spectrum argument is analytic.')
 print('per_site: All8 cube vertices with full vertex Gauss constraints; no external charges.')
 print('per_mode: All4096 supports of12 links, retaining every degree census.')
 print('per_block: All144 face-character pairs and1728 triples; Haar survivor values proved analytically.')
 print('lattice_wide: One fixed physical cube only; no thermodynamic or continuum gap.')
 print('support_histogram='+json.dumps(payload['valid_support_histogram'],sort_keys=True))
 print('Ritz_gap_lower(x)/a=('+payload['Ritz_gap_lower']+')/a; x=av')
 print('resources: elapsed_sec='+str(payload['seconds'])+' rss_MiB='+str(payload['rss_MiB'])+'; limits=180sec/180MiB')
 print('source_sha256='+payload['source_sha256'])

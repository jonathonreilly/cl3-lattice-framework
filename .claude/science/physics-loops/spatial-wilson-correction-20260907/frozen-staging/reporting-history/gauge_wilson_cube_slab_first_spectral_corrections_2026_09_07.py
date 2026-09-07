#!/usr/bin/env python3
"""Exact alternative-tree Wilson cube first spectral corrections."""
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
import os,time,signal
START=time.monotonic();signal.alarm(180)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sympy as s
from itertools import product,combinations
from math import factorial
import json,resource,sys,hashlib
K=s.QQ.algebraic_field(s.sqrt(55));zero=K.zero
checks=[]
def ck(n,b):
 if n in checks or not bool(b):raise AssertionError(n)
 checks.append(n)
def ex(x):return s.simplify(K.to_sympy(x))
def st(x):return str(ex(x))
def field(M):return [[K.from_sympy(x) for x in row] for row in M.tolist()]
# Explicit color basis, unrelated to native correction implementation.
i=s.I;rt=s.sqrt(2)
T=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]])/rt,s.Matrix([[0,-i,0],[i,0,0],[0,0,0]])/rt,s.diag(1,-1,0)/rt,s.Matrix([[0,0,1],[0,0,0],[1,0,0]])/rt,s.Matrix([[0,0,-i],[0,0,0],[i,0,0]])/rt,s.Matrix([[0,0,0],[0,0,1],[0,1,0]])/rt,s.Matrix([[0,0,0],[0,0,-i],[0,i,0]])/rt,s.diag(1,1,-2)/s.sqrt(6)]
ck('trace orthonormal basis',all(s.trace(a*b)==int(j==k) for j,a in enumerate(T) for k,b in enumerate(T)))
f2=s.simplify(6*sum(s.im(s.trace(T[a]*T[b]*T[c]))**2 for a,b,c in combinations(range(8),3)))
color=[s.simplify(sum(s.trace(a*a*b*b) for a in T for b in T)),s.simplify(sum(s.trace(a*b*a*b) for a in T for b in T)),s.simplify(sum(s.trace(a*b*b*a) for a in T for b in T))]
ck('actual alternating tensor norm',f2==12);ck('actual ordered fourth color contractions',color==[s.Rational(64,3),-s.Rational(8,3),s.Rational(64,3)])
V=list(product((0,1),repeat=4));edges=[]
for v in V:
 for a in range(4):
  if v[a]==0:
   w=list(v);w[a]=1;edges.append((v,tuple(w),a))
idx={(v,a):j for j,(v,w,a) in enumerate(edges)}
faces=[]
for a,b in combinations(range(4),2):
 for fixed in product((0,1),repeat=2):
  v=[0]*4
  for ax,val in zip([j for j in range(4) if j not in (a,b)],fixed):v[ax]=val
  va=v.copy();va[a]=1;vb=v.copy();vb[b]=1
  word=[(idx[(tuple(v),a)],1),(idx[(tuple(va),b)],1),(idx[(tuple(vb),a)],-1),(idx[(tuple(v),b)],-1)]
  faces.append(dict(axes=[a,b],base=v,word=word,weight=s.Integer(1) if b==3 else s.Rational(1,2),omitted=(a,b)==(0,1) and v[2]==0))
parent=list(range(16))
def find(a):
 while parent[a]!=a:a=parent[a]
 return a
def add(e):
 u,v,_=edges[e];a=find(V.index(u));b=find(V.index(v))
 if a==b:return False
 parent[b]=a;return True
tr=[]
for f in faces:
 if f['omitted']:
  for e,sign in f['word']:
   if not(edges[e][2]==0 and edges[e][0][1]==1):
    assert add(e);tr.append(e)
for e in reversed(range(32)):
 if add(e):tr.append(e)
chords=[e for e in range(32) if e not in tr];ci={e:j for j,e in enumerate(chords)}
ck('different complete adapted tree',len(tr)==15 and len(chords)==17 and set(tr)!=set([0,20,12,4,23,15,2,3,6,7,8,10,11,17,19]))
kept=[f for f in faces if not f['omitted']];marked=[f for f in faces if f['omitted']]
def incidence(f):
 row=[0]*17
 for e,sign in f['word']:
  if e in ci:row[ci[e]]+=sign
 return row
B=s.Matrix([incidence(f) for f in kept]);S=s.Matrix([incidence(f) for f in marked]);H=B.T*s.diag(*[f['weight'] for f in kept])*B
ck('literal source chords',all(sum(x!=0 for x in row)==1 for row in S.tolist()))
G0=3*H.inv();omega=s.sqrt(55)/90
ck('independent quadratic source covariance',S*G0*S.T==s.Matrix([[192,138],[138,192]])/11)
M=(s.eye(2)/omega+S*G0*S.T).inv().applyfunc(s.radsimp)
Gg=(G0-G0*S.T*M*S*G0).applyfunc(lambda x:s.radsimp(s.expand(x)))
GF=[field(G0),field(Gg)];Prec=field(H/3+omega*S.T*S)
ck('ground covariance exact inverse',all(sum((Prec[a][c]*GF[1][c][b] for c in range(17)),zero)==K.convert(int(a==b)) for a in range(17) for b in range(17)))
facewords=[[(ci[e],sign) for e,sign in f['word'] if e in ci] for f in kept]
def parity(t):return -1 if sum(t[a]>t[b] for a in range(len(t)) for b in range(a+1,len(t)))%2 else 1
qs=[]
for f,word in zip(kept,facewords):
 q={}
 for terms in combinations(word,3):
  labels=tuple(x[0] for x in terms);assert len(set(labels))==3
  coeff=-f['weight']*s.prod(x[1] for x in terms)*parity(labels)/3;key=tuple(sorted(labels));q[key]=q.get(key,0)+coeff
 qs.append({t:K.from_sympy(c) for t,c in q.items() if c})
def detminor(G,a,b):
 return (G[a[0]][b[0]]*(G[a[1]][b[1]]*G[a[2]][b[2]]-G[a[1]][b[2]]*G[a[2]][b[1]])-G[a[0]][b[1]]*(G[a[1]][b[0]]*G[a[2]][b[2]]-G[a[1]][b[2]]*G[a[2]][b[0]])+G[a[0]][b[2]]*(G[a[1]][b[0]]*G[a[2]][b[1]]-G[a[1]][b[1]]*G[a[2]][b[0]]))
def compositions(n,m):
 if m==1:yield(n,);return
 for k in range(n+1):
  for rest in compositions(n-k,m-1):yield(k,)+rest
quartics=[]
for f,word in zip(kept,facewords):
 terms=[]
 if word:
  for ns in compositions(4,len(word)):
   labels=tuple(e for (e,sign),n in zip(word,ns) for _ in range(n));coeff=-f['weight']/3
   for (e,sign),n in zip(word,ns):coeff*=s.Rational(sign**n,factorial(n))
   terms.append((labels,K.from_sympy(coeff)))
 quartics.append(terms)
def tracefour(G,word,middle=True):
 a,b,c,d=word
 return K.from_sympy(color[0])*G[a][b]*G[c][d]+(K.from_sympy(color[1])*G[a][c]*G[b][d] if middle else zero)+K.from_sympy(color[2])*G[a][d]*G[b][c]
results=[]
for label,G in zip(['partition','ground'],GF):
 pairs=[[K.convert(12)*sum((ca*cb*detminor(G,aa,bb) for aa,ca in qa.items() for bb,cb in qb.items()),zero) for qb in qs] for qa in qs]
 cube=sum((x for row in pairs for x in row),zero);diagonal=sum((pairs[j][j] for j in range(22)),zero)
 fourth=[sum((c*tracefour(G,t) for t,c in terms),zero) for terms in quartics];wrongfour=sum((c*tracefour(G,t,False) for terms in quartics for t,c in terms),zero)
 E4=sum(fourth,zero);haar=-K.convert(2)*sum((G[j][j] for j in range(17)),zero)
 bulk=cube/K.convert(2)-E4+haar
 sourcehalf=sum((G[j][j] for j in range(17) if (S.T*S)[j,j]),zero) if label=='ground' else zero
 ck(label+' cubic variance nonnegative',ex(cube)>=0)
 results.append(dict(label=label,E3_square=st(cube),E4=st(E4),Haar=st(haar),bulk=st(bulk),source_half_density=st(sourcehalf),per_face_E4=[st(x) for x in fourth],per_face_pair_E3_square=[[st(x) for x in row] for row in pairs],mutation_dropped_crossface=st((diagonal-cube)/K.convert(2)),mutation_missing_middle_fourth=st(E4-wrongfour),mutation_missing_Haar=st(-haar),mutation_missing_source_half=st(-sourcehalf)))
# One-group partition control, derived from explicit color traces and covariance3.
one_E4=-sum(color)*9/72;one_Haar=-2*3
ck('one group Wilson partition correction',s.simplify(-one_E4+one_Haar)==-1)
Z1=s.sympify(results[0]['bulk']);ground=s.sympify(results[1]['bulk'])+s.sympify(results[1]['source_half_density']);k0=s.simplify(ground-Z1)
ck('Haar active in partition',results[0]['mutation_missing_Haar']!='0');ck('source half density active',results[1]['source_half_density']!='0')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);ck('resources',0<rss<180 and time.monotonic()-START<180)
def matrix(M):return [[str(x) for x in row] for row in M.tolist()]
ground_payload=dict(checks=checks,tree=tr,chords=chords,vertices=V,edges=edges,faces=[{**f,'weight':str(f['weight'])} for f in faces],face_chord_words=facewords,cubic_threeforms=[{','.join(map(str,t)):st(c) for t,c in q.items()} for q in qs],quartic_terms=[[[list(t),st(c)] for t,c in terms] for terms in quartics],H=matrix(H),G0=matrix(G0),Gg=matrix(Gg),source_incidence=matrix(S),color_F_norm_squared=str(f2),color_fourth=[str(x) for x in color],results=results,Z1=str(Z1),ground_relative_correction=str(k0),one_group_E4=str(one_E4),one_group_Haar=str(one_Haar),seconds=time.monotonic()-START,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest())

from itertools import permutations
from collections import defaultdict
ground_checks=checks.copy()
r=ground_payload
F=s.QQ.algebraic_field(s.sqrt(55));z=F.zero
f=lambda x:F.from_sympy(s.sympify(x))
st=lambda x:str(s.simplify(F.to_sympy(x)))
G=[[f(x) for x in row] for row in r['Gg']];n=len(G)
S=s.Matrix([[s.sympify(x) for x in row] for row in r['source_incidence']]);u,v=[next(i for i,x in enumerate(row) if x) for row in S.tolist()]
w=f(s.sqrt(55)/90);theta=f((32-3*s.sqrt(55))/23)
Ga=[[-2*G[i][u]*G[u][j] for j in range(n)] for i in range(n)]
Gb=[[-2*G[i][v]*G[v][j] for j in range(n)] for i in range(n)]
Gab=[[4*(G[i][u]*G[u][v]*G[v][j]+G[i][v]*G[v][u]*G[u][j]) for j in range(n)] for i in range(n)]
checks=[]
def ck(name,b):
 if name in checks or not b:raise AssertionError(name)
 checks.append(name)
prec=[[f(x) for x in row] for row in (s.Matrix(r['H'])/3+s.sqrt(55)/90*S.T*S).tolist()]
ck('first inverse derivative',all(sum((prec[i][k]*Ga[k][j] for k in range(n)),z)+2*(G[u][j] if i==u else z)==z for i in range(n) for j in range(n)))
ck('mixed inverse derivative',all(sum((prec[i][k]*Gab[k][j] for k in range(n)),z)+2*(Gb[u][j] if i==u else z)+2*(Ga[v][j] if i==v else z)==z for i in range(n) for j in range(n)))
poly=defaultdict(lambda:z)
def add(pairs,c):poly[tuple(sorted(tuple(sorted(p)) for p in pairs))]+=c
q=defaultdict(lambda:z)
for face in r['cubic_threeforms']:
 for key,c in face.items():q[tuple(map(int,key.split(',')))]+=f(c)
for a,ca in q.items():
 for b,cb in q.items():
  for perm in permutations(range(3)):
   sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
   add([(a[i],b[perm[i]]) for i in range(3)],6*sign*ca*cb)
for face in r['quartic_terms']:
 for (a,b,c,d),coef in face:
  cc=f(coef)
  add([(a,b),(c,d)],-cc*f('64/3'));add([(a,c),(b,d)],cc*f('8/3'));add([(a,d),(b,c)],-cc*f('64/3'))
for i in range(n):add([(i,i)],f(-2))
for i in (u,v):add([(i,i)],f(1))
poly={m:c for m,c in poly.items() if c}
def prod(vals):
 out=F.one
 for x in vals:out*=x
 return out
out=[z,z,z,z]
for mon,c in poly.items():
 vals=[G[i][j] for i,j in mon];aa=[Ga[i][j] for i,j in mon];bb=[Gb[i][j] for i,j in mon];ab=[Gab[i][j] for i,j in mon]
 out[0]+=c*prod(vals)
 for i in range(len(mon)):
  rest=prod(vals[k] for k in range(len(mon)) if k!=i)
  out[1]+=c*aa[i]*rest;out[2]+=c*bb[i]*rest;out[3]+=c*ab[i]*rest
  for j in range(len(mon)):
   if i!=j:out[3]+=c*aa[i]*bb[j]*prod(vals[k] for k in range(len(mon)) if k not in (i,j))
K,Ka,Kb,Kab=out;Z1=f(r['Z1']);k0=K-Z1
ck('frozen own ground coefficient reproduced',k0==f(r['ground_relative_correction']))
la=-8*G[u][u];lb=-8*G[v][v];lab=16*G[u][v]**2
den=16+4*w*(la+lb)+w*w*(la*lb+lab)
ck('radial eigenfunction normalization',den==4*theta**2)
num=den*K+(4*w+w*w*lb)*Ka+(4*w+w*w*la)*Kb+w*w*Kab
k1=num/den-Z1
ck('source exchange symmetry',Ka==Kb)
a,b=s.symbols('a b');cov=(s.Matrix([[192,138],[138,192]])/11).inv();C=(cov+s.diag(2*a,2*b)).inv()
for name,mat,da,db in [('a',Ga,1,0),('b',Gb,0,1),('ab',Gab,1,1)]:
 ck('independent two by two symbolic derivative '+name,all(f(s.diff(C[i,j],a,da,b,db).subs({a:s.sqrt(55)/180,b:s.sqrt(55)/180}))==mat[[u,v][i]][[u,v][j]] for i in range(2) for j in range(2)))
ck('nonzero mixed covariance contribution',Kab!=z)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('resource budget',0<rss<180 and time.monotonic()-START<180)
excited_payload=dict(checks=checks,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),tree=r['tree'],source_indices=[u,v],monomials=[dict(pairs=m,coefficient=st(c)) for m,c in sorted(poly.items())],covariance_derivatives={name:[[st(x) for x in row] for row in mat] for name,mat in [('a',Ga),('b',Gb),('ab',Gab)]},K=st(K),Ka=st(Ka),Kb=st(Kb),Kab=st(Kab),log_Gamma_a=st(la),log_Gamma_b=st(lb),log_Gamma_ab=st(lab),D_Gamma_over_Gamma=st(den),k0=st(k0),k1=st(k1),k1_minus_k0=st(k1-k0),seconds=time.monotonic()-START,rss_MiB=rss)

all_checks=['ground: '+x for x in ground_checks]+['excited: '+x for x in checks]
payload=dict(status='PASS',TOTAL=len(all_checks),checks=all_checks,ground=ground_payload,excited=excited_payload,seconds=time.monotonic()-START,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope='Conditional actual two-source cube spectral asymptotics; no finite onset or physical gap identification.')
if sys.argv[1:]==['--json']:print(json.dumps(payload,indent=2,allow_nan=False))
elif not sys.argv[1:]:
 print('PASS exact cube ground and excited correction; TOTAL='+str(payload['TOTAL']))
 print('per_element: 8 trace-orthonormal color matrices; per_site: 16 vertices')
 print('per_mode: 17 chord variables with 8 colors; per_block: 22 weighted face words')
 print('lattice_wide: one finite cube slab; no thermodynamic claim')
 print('k0='+excited_payload['k0']+'; k1='+excited_payload['k1'])
else:raise SystemExit('usage: '+sys.argv[0]+' [--json]')

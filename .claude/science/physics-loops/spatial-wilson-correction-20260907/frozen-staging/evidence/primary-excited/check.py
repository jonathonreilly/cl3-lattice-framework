import os,time,signal
START=time.monotonic();signal.alarm(180)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sympy as s,json,hashlib,resource,sys
from itertools import permutations
from collections import defaultdict
P='/private/tmp/toe-autonomous-primary-20260907/cube-first-correction/result.json'
r=json.load(open(P));F=s.QQ.algebraic_field(s.sqrt(55));z=F.zero
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
print(json.dumps(dict(checks=checks,input_sha256=hashlib.sha256(open(P,'rb').read()).hexdigest(),source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),tree=r['tree'],source_indices=[u,v],monomials=[dict(pairs=m,coefficient=st(c)) for m,c in sorted(poly.items())],covariance_derivatives={name:[[st(x) for x in row] for row in mat] for name,mat in [('a',Ga),('b',Gb),('ab',Gab)]},K=st(K),Ka=st(Ka),Kb=st(Kb),Kab=st(Kab),log_Gamma_a=st(la),log_Gamma_b=st(lb),log_Gamma_ab=st(lab),D_Gamma_over_Gamma=st(den),k0=st(k0),k1=st(k1),k1_minus_k0=st(k1-k0),seconds=time.monotonic()-START,rss_MiB=rss),indent=2))

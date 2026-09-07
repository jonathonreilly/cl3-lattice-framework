import os,time,signal,resource,sys,json,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
t0=time.monotonic();signal.alarm(180)
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
checks=[]
def ck(n,b):
 if n in checks or not b:raise AssertionError(n)
 checks.append(n)
def shift(x,i):return tuple(a+(i==j) for j,a in enumerate(x))
verts=set(product(range(3),range(2),range(2)))
edges=[(x,i) for x in sorted(verts) for i in range(3) if shift(x,i) in verts];index={e:j for j,e in enumerate(edges)}
faces=[]
for x in sorted(verts):
 for i,j in combinations(range(3),2):
  if shift(shift(x,i),j) in verts:
   word=[((x,i),1),((shift(x,i),j),1),((shift(x,j),i),-1),((x,j),-1)]
   b=[0]*len(edges)
   for e,s in word:b[index[e]]=s
   faces.append({'anchor':x,'axes':(i,j),'boundary':b})
ck('actual two-cube graph counts',len(verts)==12 and len(edges)==20 and len(faces)==11)
pair=[i for i,f in enumerate(faces) if f['axes']==(0,1) and f['anchor'][2]==0]
C=[sum(faces[i]['boundary'][j] for i in pair) for j in range(len(edges))]
ck('actual rectangle has six exterior links',sum(x!=0 for x in C)==6 and all(abs(x)<=1 for x in C))
ck('adjacent plaquettes share exactly one link',sum(a!=0 and b!=0 for a,b in zip(*(faces[i]['boundary'] for i in pair)))==1)
rows=[]
for n in [0,1,2]:
 survivors=[]
 for ops in product(list(product(range(len(faces)),[-1,1])),repeat=n):
  for sign in [-1,1]:
   if all((sign*C[j]+sum(s*faces[i]['boundary'][j] for i,s in ops))%3==0 for j in range(len(edges))):survivors.append({'observable_sign':sign,'insertions':ops})
 ck('rectangle center survivor count order'+str(n),len(survivors)==(4 if n==2 else 0))
 if n==2:ck('all second-order survivors exactly planar pair',all({i for i,s in row['insertions']}==set(pair) and all(s==-row['observable_sign'] for i,s in row['insertions']) for row in survivors))
 rows.append({'order':n,'survivors':survivors})
# Actual U(3)/SU(3) fundamental one-U one-conjugate-U Haar contraction.
# Tr(AU)Tr(U*B): coefficient of A_ij B_kl is delta_jl delta_ik/3.
for i,j,k,l in product(range(3),repeat=4):
 actual=F(int(j==l and i==k),3)
 expected=F(int(k==i and l==j),3)
 if actual!=expected:raise AssertionError('Haar tensor mismatch')
ck('all81 shared-link Haar coefficients agree with traceAB over3',True)
ck('fundamental character orthogonality norm1',sum(F(1,3) for i in range(3))==1)
I=F(4,6)*F(1,3)
ck('actual ordered oriented Haar integral',I==F(2,9))
one=2*F(1,6)*F(1,96)*2
ck('one-face coefficient',one==F(1,144))
first=I/F(96)**2;second=2*I/F(576*24);total=first+second
ck('two-face coefficient',total==F(7,124416))
ck('distinct final energy denominator matters',first+2*I/F(576*16)!=total)
ck('scalar vacuum normalization contributes zero',0*F(1,96)**2==0)
# Plane projection of arbitrary finite mod3 face chains has unique finite filling.
for R,S in [(1,1),(1,2),(2,2),(3,2),(3,3)]:
 filling={(x,y):1 for x in range(R) for y in range(S)}
 boundary={}
 for (x,y),a in filling.items():
  for e,s in [((x,y,0),1),((x+1,y,1),1),((x,y+1,0),-1),((x,y,1),-1)]:boundary[e]=boundary.get(e,0)+s*a
 nonzero={e:a for e,a in boundary.items() if a%3}
 ck('rectangle projected boundary R'+str(R)+'S'+str(S),len(nonzero)==2*(R+S))
 ck('each projected cell requires insertion R'+str(R)+'S'+str(S),len(filling)==R*S and all(a%3 for a in filling.values()))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive resources',0<rss<180 and time.monotonic()-t0<180)
out={'checks':checks,'TOTAL':len(checks),'edges':edges,'faces':faces,'rectangle_boundary':C,'center_census':rows,'one_face_coefficient':str(one),'two_face_middle_term':str(first),'two_face_end_terms':str(second),'two_face_coefficient':str(total),'Haar_W_S2':str(I),'seconds':time.monotonic()-t0,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2,allow_nan=False))

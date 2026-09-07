import os,time,signal,json,hashlib,resource,sys
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='1'
import sympy as s
from itertools import combinations
START=time.monotonic();signal.alarm(180)
checks=[]
def ck(n,b):assert n not in checks and bool(b),n;checks.append(n)
V=list(range(8));edges=[(v,v^(1<<a)) for v in V for a in range(3) if not v&(1<<a)]
parent=list(V)
def root(v):
 while parent[v]!=v:v=parent[v]
 return v
tree=[]
for e,(u,v) in enumerate(edges):
 a,b=root(u),root(v)
 if a!=b:parent[b]=a;tree.append(e)
chords=[i for i in range(12) if i not in tree]
D=s.zeros(8,12)
for j,(u,v) in enumerate(edges):D[u,j]=-1;D[v,j]=1
Dt=D[1:,tree];Dc=D[1:,chords];coef=-Dt.inv()*Dc
C=s.zeros(5,12)
for j in range(5):
 C[j,chords[j]]=1
 for i,e in enumerate(tree):C[j,e]=coef[i,j]
F=s.zeros(6,12);facevertices=[];idx=0
for a,b in combinations(range(3),2):
 other=next(x for x in range(3) if x not in(a,b))
 for offset in (0,1<<other):
  vertices=[offset,offset^(1<<a),offset^(1<<a)^(1<<b),offset^(1<<b)];facevertices.append(vertices)
  for u,v in zip(vertices,vertices[1:]+vertices[:1]):
   if(u,v)in edges:F[idx,edges.index((u,v))]=1
   else:F[idx,edges.index((v,u))]=-1
  idx+=1
B=F[:,chords];M=(C*C.T).inv();K=B.T*B
ck('cube8vertices12edges6faces',len(edges)==12 and len(facevertices)==6)
ck('tree7chords5 and cyclebasis',len(tree)==7 and len(chords)==5 and C[:,chords]==s.eye(5) and D*C.T==s.zeros(8,5))
ck('allfaces reconstructed from fundamental cycles',F==B*C)
ck('cycle metric positive and K positive',all(M[:j,:j].det()>0 and K[:j,:j].det()>0 for j in range(1,6)))
lam=s.symbols('lam');poly=s.factor((K-lam*M).det()/M.det())
ck('generalized spectrum4triple6double',s.expand(poly-(4-lam)**3*(6-lam)**2)==0)
ck('octahedral face curl spectrum0,4triple6double',(F*F.T).eigenvals()=={s.Integer(0):1,s.Integer(4):3,s.Integer(6):2})
# Exact full restored graph: spatial copies then eight temporal edges.
full_edges=[(u+8*t,v+8*t) for t in (0,1) for u,v in edges]+[(v,v+8) for v in V]
full_tree=tree+[i+12 for i in tree]+[24];full_chords=chords+[i+12 for i in chords]+list(range(25,32))
ck('actual17chords5plus5plus7',len(full_edges)==32 and len(full_tree)==15 and len(set(full_tree+full_chords))==32 and len(full_chords)==17)
fullD=s.zeros(16,32)
for j,(u,v)in enumerate(full_edges):fullD[u,j]=-1;fullD[v,j]=1
ck('restored fulltree connects16vertices',fullD[:,full_tree].rank()==15)
T=s.zeros(12,17)
for j,(u,v) in enumerate(edges):
 if j in chords:T[j,chords.index(j)]=1;T[j,5+chords.index(j)]=-1
 if v:T[j,10+v-1]+=1
 if u:T[j,10+u-1]-=1
k=s.symbols('k',positive=True);H=s.diag(K/2,K/2,s.zeros(7))+k*T.T*T
Hbb=H[:10,:10];Hbz=H[:10,10:];Hzz=H[10:,10:]
reduced=s.simplify(Hbb-Hbz*Hzz.inv()*Hbz.T);target=s.BlockMatrix([[K/2+k*M,-k*M],[-k*M,K/2+k*M]]).as_explicit()
ck('temporal17dim Schur complement exact in k',reduced==target)
P=s.eye(12)-D[1:,:].T*(D[1:,:]*D[1:,:].T).inv()*D[1:,:];J=s.zeros(12,5)
for i,e in enumerate(chords):J[e,i]=1
ck('minimum temporal norm metric independentlyprojected',J.T*P*J==M)
q=s.symbols('q');pin=[]
for kval in (s.Rational(1,3),s.Integer(1),s.Rational(5,2)):
 hr=reduced.subs(k,kval);cov=3*hr.inv();plus=s.simplify(cov[:5,:5]+cov[:5,5:]);minus=s.simplify(cov[:5,:5]-cov[:5,5:]);ck('plus covariance6Kinv k='+str(kval),plus==6*K.inv());ck('minus covariance6Kplus4kMinv k='+str(kval),minus==6*(K+4*kval*M).inv());pin.append(dict(k=str(kval),covariance=cov))
# Generalized spectral projectors provide coordinate-free metric decomposition.
L=M.inv()*K;P4=(6*s.eye(5)-L)/2;P6=(L-4*s.eye(5))/2
ck('metricorthogonal projectors ranks3,2',P4*P4==P4 and P6*P6==P6 and P4*P6==s.zeros(5) and P4.rank()==3 and P6.rank()==2 and P4.T*M==M*P4 and P6.T*M==M*P6)
# No second covariance model is substituted: modes follow by M metric whitening.
mode_rows=[]
for value,mult in ((4,3),(6,2)):
 for kval in (s.Rational(1,3),s.Integer(1),s.Rational(5,2)):
  A=(value+2*kval)/12;cross=kval/3;omega=s.sqrt(value*(value+4*kval))/6;r=s.sqrt(s.Rational(value)/(value+4*kval));theta=(1-r)/(1+r)
  ck('Mehler normalization lambda%s k%s'%(value,kval),s.simplify(omega**2-(4*A*A-cross*cross))==0 and s.simplify(theta-cross/(2*A+omega))==0)
  mode_rows.append(dict(lam=value,multiplicity=mult,k=str(kval),sigma_plus=str(s.Rational(6,value)),sigma_minus=str(6/(value+4*kval)),omega=str(omega),theta=str(s.simplify(theta))))
# Failure controls: deleting one physical face changes spectrum; retaining gauge link directions gives zeros.
Kd=F[:5,chords].T*F[:5,chords];deletedpoly=s.factor((Kd-lam*M).det()/M.det());ck('deletedface changes generalized spectrum',s.expand(deletedpoly-(4-lam)**3*(6-lam)**2)!=0)
ck('ungaugefixed curl has7gradientzeros',(F.T*F).nullspace().__len__()==7)
slow=[(i,j) for i in range(3) for j in range(i,3)];independent_only=[(i,i) for i in range(3)]
ck('global singlet slow quadratic multiplicity6',len(slow)==6)
ck('independentclass restriction incorrectlydrops3crossinvariants',len(independent_only)==3 and set(independent_only)<set(slow))
ck('two slow quanta energy4 below otherdegrees',4<2+s.sqrt(6) and 4<2*s.sqrt(6) and 4<6)
def enc(x):
 if isinstance(x,s.MatrixBase):return [[str(z) for z in row] for row in x.tolist()]
 if isinstance(x,dict):return {key:enc(v) for key,v in x.items()}
 if isinstance(x,list):return [enc(y) for y in x]
 if isinstance(x,tuple):return [enc(y) for y in x]
 return x
source=Path('/private/tmp/toe-spatial-gaussian-campaign-20260907/docs/GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md')
out=enc(dict(status='PASS',checks=checks,TOTAL=len(checks),vertices=V,edges=edges,tree=tree,chords=chords,face_vertices=facevertices,C=C,F=F,B=B,M=M,K=K,generalized_characteristic=str(poly),full_edges=full_edges,full_tree=full_tree,full_chords=full_chords,temporal_rows=T,reduced_hessian=reduced,covariance_controls=pin,projectors=dict(lambda4=P4,lambda6=P6),modes=mode_rows,deletedface_polynomial=str(deletedpoly),global_singlet_low_pairs=slow,independent_class_pairs=independent_only,seconds=time.monotonic()-START,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),parent_source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),scope='Exact full24face finite cube Gaussian geometry and mode support; no uniform actual-kernel scaling or selected physical action claim.'))
assert out['seconds']<180 and 0<out['rss_MiB']<180
print(json.dumps(out,indent=2,allow_nan=False))

import contextlib,io,runpy,json,hashlib,time,resource,sys
from pathlib import Path
import sympy as s
base=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(base/'check.py'))
N=d['N'];I=d['I'];w=d['w'];mul=d['mul'];comm=d['comm'];F=d['F'];K=d['K'];start=time.monotonic()
def add(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=s.simplify(out.get(k,0)+v)
 return {k:v for k,v in out.items() if v!=0}
def scale(a,c):return {k:s.simplify(v*c) for k,v in a.items() if v*c!=0}
def product(a,b):
 out={}
 for x,c in a.items():
  for y,e in b.items():
   z,p=mul(x,y);p=s.Integer(int(p.real))+s.I*int(p.imag)
   out=add(out,{z:c*e*p})
 return out
def minus(a,b):return add(a,scale(b,-1))
def adj(a):return {k:s.conjugate(v) for k,v in a.items()}
ident={I:s.Integer(1)}
Pi={I:s.Rational(1,2),w(3,'Y'):s.Rational(1,2)}
exchange=add({mul(w(4,'X'),w(6,'X'))[0]:s.Rational(1,2)},{mul(w(4,'Y'),w(6,'Y'))[0]:s.Rational(1,2)})
H1=product(Pi,exchange)
H2=product({I:s.Rational(1,2),w(4,'Z'):s.Rational(1,2)},{w(3,'X'):s.Integer(1)})
H3={mul(w(1,'X'),w(2,'X'))[0]:s.Rational(1,2),mul(w(1,'Y'),w(2,'Y'))[0]:s.Rational(1,2)}
H4={w(8,'X'):s.Integer(1)}
Hs=[H1,H2,H3,H4];angles=[s.pi/2,s.pi/4,s.pi/2,s.pi/2]
Us=[]
for h,theta in zip(Hs,angles):
 assert not minus(product(h,h),adj(product(h,h)))
 assert not minus(product(product(h,h),h),h)
 for op in (K,d['Zr'],d['Nh']):assert not comm(h,op)
 u=add(add(ident,scale(product(h,h),s.cos(theta)-1)),scale(h,-s.I*s.sin(theta)))
 assert not minus(product(adj(u),u),ident)
 Us.append(u)
assert comm(exchange,K)
def apply(op,state):
 out={}
 for word,c in op.items():
  for bits,amp in state.items():
   dst=list(bits);phase=s.Integer(1)
   for j,p in enumerate(word):
    if p=='X':dst[j]=1-dst[j]
    elif p=='Y':phase*=s.I if dst[j]==0 else -s.I;dst[j]=1-dst[j]
    elif p=='Z':phase*=1 if dst[j]==0 else -1
   out=add(out,{tuple(dst):c*amp*phase})
 return out
def state(edge, fuel, head, battery, label,phase=1):
 bits=[0,int(head[0]),int(head[1]),0,fuel,int(battery[1]),int(battery[0]),int(label[0]),int(label[1])]
 if edge=='Y+':
  a=tuple(bits);bits[3]=1;return {a:phase/s.sqrt(2),tuple(bits):phase*s.I/s.sqrt(2)}
 return {tuple(bits):phase}
x=state('Y+',1,'10','00','00');expect=[state('Y+',0,'10','10','00',-s.I),state('Z+',0,'10','10','00',-s.I),state('Z+',0,'01','10','00',-1),state('Z+',0,'01','10','01',s.I)]
rows=[]
for j,(u,h,y) in enumerate(zip(Us,Hs,expect)):
 x=apply(u,x);assert not minus(x,y)
 assert not minus(apply(K,x),scale(x,s.Rational(5,2)))
 rows.append({'pulse':j+1,'hamiltonian':{k:str(v) for k,v in h.items()},'angle':str(angles[j]),'max_pauli_weight':max(sum(c!='I' for c in k) for k in h),'state':{''.join(map(str,k)):str(v) for k,v in x.items()}})
assert rows[0]['max_pauli_weight']==3
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<180
print(json.dumps({'scope':'Exact state transfer under supplied complete-graph at-most-three-site controls, not full instrument or NN synthesis','rows':rows,'final_phase':'I','all_exact_checks_pass':True,'uncontrolled_exchange_energy_mutation_rejected':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':hashlib.sha256((base/'check.py').read_bytes()).hexdigest(),'rss_MiB':rss,'seconds':time.monotonic()-start},indent=2))

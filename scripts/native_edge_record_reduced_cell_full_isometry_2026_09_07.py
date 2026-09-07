import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic()
AUDIT_TIMEOUT_SEC=180
import sympy as s
N=9
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
def accumulate(d,k,v):
 d[k]=d.get(k,F(0))+v
 if d[k]==0:del d[k]
def comm(a,b):
 # [a,b]/(2i), real coefficients for Hermitian Pauli inputs
 out={}
 for x,c in a.items():
  for y,d in b.items():
   z,p=mul(x,y)
   if p.imag:accumulate(out,z,c*d*int(p.imag))
 return out
def sadd(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=s.simplify(out.get(k,0)+v)
 return {k:v for k,v in out.items() if v!=0}
def scale(a,c):return {k:s.simplify(v*c) for k,v in a.items() if v*c!=0}
def product(a,b):
 out={}
 for x,c in a.items():
  for y,e in b.items():
   z,p=mul(x,y);p=s.Integer(int(p.real))+s.I*int(p.imag)
   out=sadd(out,{z:c*e*p})
 return out
def minus(a,b):return sadd(a,scale(b,-1))
def adj(a):return {k:s.conjugate(v) for k,v in a.items()}
def apply(op,state):
 out={}
 for word,c in op.items():
  for bits,amp in state.items():
   dst=list(bits);phase=s.Integer(1)
   for j,p in enumerate(word):
    if p=='X':dst[j]=1-dst[j]
    elif p=='Y':phase*=s.I if dst[j]==0 else -s.I;dst[j]=1-dst[j]
    elif p=='Z':phase*=1 if dst[j]==0 else -1
   out=sadd(out,{tuple(dst):c*amp*phase})
 return out

prod=product
add=sadd
ident={I:s.Integer(1)}
Zr={w(0,'Z'):F(1)}
Nh={I:F(1),w(1,'Z'):F(-1,2),w(2,'Z'):F(-1,2)}
K={I:F(5,2),w(3,'Y'):F(1,2),w(4,'Z'):F(-1,2),mul(w(4,'Z'),w(3,'Y'))[0]:F(-1,2),w(5,'Z'):F(-1,2),w(6,'Z'):F(-1)}
checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
q={I:s.Rational(1,2),w(4,'Z'):s.Rational(-1,2)};a=minus(ident,q)
plus={I:s.Rational(1,2),w(3,'Y'):s.Rational(1,2)};dark=minus(ident,plus)
nb={I:s.Rational(1,2),w(6,'Z'):s.Rational(-1,2)};zm={I:s.Rational(1,2),w(3,'Z'):s.Rational(-1,2)}
def controlled(P,site):
 h=prod(P,minus({w(site,'X'):s.Integer(1)},ident));ck(not minus(prod(h,h),scale(h,-2)))
 return h,add(ident,h),'pi/2'
def cubic(h):
 ck(not minus(prod(prod(h,h),h),h))
 return h,add(minus(ident,prod(h,h)),scale(h,-s.I)),'pi/2'
ex={mul(w(4,'X'),w(6,'X'))[0]:s.Rational(1,2),mul(w(4,'Y'),w(6,'Y'))[0]:s.Rational(1,2)}
head={mul(w(1,'X'),w(2,'X'))[0]:s.Rational(1,2),mul(w(1,'Y'),w(2,'Y'))[0]:s.Rational(1,2)}
pulses=[controlled(prod(plus,nb),7),controlled(prod(plus,nb),8),cubic(prod(plus,ex)),cubic(prod(dark,{w(4,'X'):s.Integer(1)})),controlled(a,8),controlled(prod(a,zm),7),controlled(prod(a,zm),8),cubic(prod(a,head)),(a,minus(ident,scale(a,2)),'pi')]
for h,u,t in pulses:
 ck(not minus(h,adj(h)));ck(not minus(prod(adj(u),u),ident));ck(max(sum(c!='I' for c in x) for x in h)<=3)
 for op in (K,Zr,Nh):ck(not comm(h,op))
def src(edge,b):return {(0,1,0,edge,1,b%2,b//2,0,0):s.Integer(1)}
def target(x):
 out={}
 for sign in (0,1):
  Pz=zm if sign else minus(ident,zm)
  for bright,P in [(True,plus),(False,dark)]:
   v=apply(prod(Pz,P),x)
   for bits,amp in v.items():
    if bright and bits[6]:continue
    dest=list(bits);dest[1:3]=[0,1];dest[4]=0
    if bright:dest[6]=1
    dest[7:9]=[sign,1-sign]
    out=add(out,{tuple(dest):amp})
 for bits,amp in apply(prod(plus,nb),x).items():
  dest=list(bits);dest[7:9]=[1,1];out=add(out,{tuple(dest):amp})
 return out
def evolve(x):
 for h,u,t in pulses:x=apply(u,x)
 return x
def inner(x,y):return s.simplify(sum(s.conjugate(v)*y.get(k,0) for k,v in x.items()))
columns=[];outs=[]
for edge in (0,1):
 for b in range(4):
  x=src(edge,b);got=evolve(x);want=target(x);ck(not minus(got,want));ck(not minus(apply(K,got),target(apply(K,x))))
  ck(not minus(apply(Zr,got),got));ck(not minus(apply(Nh,got),got))
  outs.append(got);columns.append({'edge':edge,'battery':b,'state':{''.join(map(str,k)):str(v) for k,v in got.items()},'refusal_probability':str(s.simplify(sum(s.conjugate(v)*v for k,v in got.items() if k[7:9]==(1,1))))})
for i,x in enumerate(outs):
 for j,y in enumerate(outs):ck(inner(x,y)==int(i==j))
coherent=add(scale(src(0,0),1/s.sqrt(2)),scale(src(1,3),s.I/s.sqrt(2)))
ck(not minus(evolve(coherent),target(coherent)))
y=outs[-1];bad={k:v for k,v in y.items() if k[7:9]!=(1,1)};ck(bool(minus(y,bad)))
y=outs[0];bad={k:(-v if k[7:9]==(1,0) else v) for k,v in y.items()};ck(bool(minus(y,bad)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck(0<rss<180);ck(time.monotonic()-start<180)

def canonical_hash(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rational_complex(v):
 v=s.expand(v);return [str(s.re(v)),str(s.im(v))]
full_columns=[]
for column in outs:
 full_columns.append([{'bits':''.join(map(str,k)),'amplitude':rational_complex(v)} for k,v in sorted(column.items())])
pulse_rows=[{'hamiltonian':{k:str(v) for k,v in h.items()},'angle':t,'max_weight':max(sum(c!='I' for c in x) for x in h)} for h,u,t in pulses]
payload={'schema':'native-reduced-cell-full-isometry-v1','scope':'All8 ready-input native sign/refusal Stinespring columns; supplied globally energy-preserving at-most3-site completegraph controls; not arbitrary-label collisionstar or NN implementation','qubit_order':['r','head_v','head_w','edge','fuel','battery_low','battery_high','label0','label1'],'input_order':'edge computational bit outer, battery integer inner','checks':checks,'columns':columns,'rational_complex_columns':full_columns,'columns_sha256':canonical_hash(full_columns),'pulses':pulse_rows,'pulses_sha256':canonical_hash(pulse_rows),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1},'seconds':time.monotonic()-start,'rss_MiB':rss}
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS exact full native reduced-cell isometry:',checks,'actual exact assertions; all8 columns,9 pulses')
 print('COLUMN_SHA256',payload['columns_sha256'])
 print('per_element: full exact sign amplitudes, one refusal, energy intertwining and phase controls')
 print('per_site: same nine reduced registers, no additional ancillas, old Record unchanged')
 print('per_mode: both matter states and all four positive battery levels, arbitrary reference by linearity')
 print('per_block: nine explicit completegraph generators with support at most3 and exact unitary identities')
 print('lattice_wide: checked and not executed -- no NN synthesis, full cube dynamics or physical control law')
 print('SOURCE_SHA256',payload['source_sha256'])

import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys,runpy,contextlib,io,json,hashlib
from pathlib import Path
signal.alarm(180);start=time.monotonic()
p=Path(__file__).parent;dep=p/'staging/scripts/native_edge_record_reduced_cell_control_2026_09_07.py'
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(dep))
s=d['s'];I=d['I'];w=d['w'];mul=d['mul'];comm=d['comm'];K=d['K'];prod=d['product'];add=d['sadd'];scale=d['scale'];minus=d['minus'];adj=d['adj'];apply=d['apply'];ident=d['ident'];checks=0
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
 for op in (K,d['Zr'],d['Nh']):ck(not comm(h,op))
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
  ck(not minus(apply(d['Zr'],got),got));ck(not minus(apply(d['Nh'],got),got))
  outs.append(got);columns.append({'edge':edge,'battery':b,'state':{''.join(map(str,k)):str(v) for k,v in got.items()},'refusal_probability':str(s.simplify(sum(s.conjugate(v)*v for k,v in got.items() if k[7:9]==(1,1))))})
for i,x in enumerate(outs):
 for j,y in enumerate(outs):ck(inner(x,y)==int(i==j))
coherent=add(scale(src(0,0),1/s.sqrt(2)),scale(src(1,3),s.I/s.sqrt(2)))
ck(not minus(evolve(coherent),target(coherent)))
y=outs[-1];bad={k:v for k,v in y.items() if k[7:9]!=(1,1)};ck(bool(minus(y,bad)))
y=outs[0];bad={k:(-v if k[7:9]==(1,0) else v) for k,v in y.items()};ck(bool(minus(y,bad)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck(0<rss<180);ck(time.monotonic()-start<180)
print(json.dumps({'scope':'All8 source columns exact native sign/refusal isometry; supplied at-most3-site completegraph controls, no extra ancilla, not NN implementation','checks':checks,'columns':columns,'pulses':[{'hamiltonian':{k:str(v) for k,v in h.items()},'angle':t,'max_weight':max(sum(c!='I' for c in x) for x in h)} for h,u,t in pulses],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':hashlib.sha256(dep.read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss},indent=2,allow_nan=False))

from pathlib import Path
import sys,json,hashlib,math
B=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-two-state-bridge');sys.path.insert(0,str(B));import bridge
n=0
def need(x,m):
 global n
 if not x:raise RuntimeError(m)
 n+=1
f=json.loads((B/'FINAL_FREEZE.json').read_text())
for k,h in f['files'].items():need(hashlib.sha256((B/k).read_bytes()).hexdigest()==h,'hash '+k)
def E(d,m,t,i,j):
 r=math.sqrt(d*d+4*m*m);x=r*t/2
 return math.exp(-d*t/2)*((math.cosh(x)+(d/r if i==0 else -d/r)*math.sinh(x)) if i==j else 2*m/r*math.sinh(x))
for d in [-4,-.2,0,.2,4]:
 for m in [.7,1.3]:
  T=.63
  for i in [0,1]:
   for j in [0,1]:
    den=E(d,m,T,i,j);need(abs(math.log(den)-bridge.logE(d,m,T,i,j))<1e-12,'direct E')
    def survival(u):return math.exp((0 if i==0 else -d)*u)*E(d,m,T-u,i,j)/den
    for level in [.03,.37,.81]:
     r=bridge.inverse_first(d,m,T,i,j,level)
     if r['no_event']:need(level>=1-survival(T)-1e-13,'atom')
     else:
      lo,hi=r['bracket'];need(survival(lo)+1e-12>=1-level>=survival(hi)-1e-12,'direct inverse bracket')
need(bridge.inverse_first(1,1,0,0,0,0)['no_event'],'T0 atom')
need(bridge.inverse_first(1,1,1,0,1,0)['bracket']==[0.,0.],'level zero endpoint caveat')
try:bad=2/(math.hypot(-1e16,2)-1e16)
except ZeroDivisionError:need(True,'actual cancellation')
else:raise RuntimeError('cancellation absent')
O=Path(__file__).parent;(O/'RESULT.json').write_text(json.dumps({'checks':n,'scope':'deterministic direct hyperbolic controls; no RNG'},indent=2)+'\n');(O/'READ_HASHES.json').write_text(json.dumps({str(B/k):h for k,h in f['files'].items()},indent=2)+'\n');print(n)

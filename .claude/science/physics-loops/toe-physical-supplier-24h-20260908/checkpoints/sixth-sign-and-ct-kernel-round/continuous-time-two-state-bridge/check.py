import decimal,math,json,time,signal,resource,sys,pathlib
from decimal import Decimal as D
import bridge
N=0
def need(c,msg):
 global N
 N+=1
 if not c:raise ValueError(msg)
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def exp_literal(d,m,t):
 # Independent positive Taylor series after scalar shift, 80-digit arithmetic.
 d=D(str(d));m=D(str(m));t=D(str(t));shift=max(D(0),d)
 K=[[shift,m],[m,shift-d]];term=[[D(1),D(0)],[D(0),D(1)]];S=[r[:] for r in term]
 for k in range(1,1000):
  term=mm(term,K);term=[[z*t/k for z in row] for row in term]
  S=[[S[i][j]+term[i][j] for j in range(2)] for i in range(2)]
  if max(abs(z) for row in term for z in row)<D('1e-70'):break
 else:raise ValueError('Taylor control budget')
 factor=(-shift*t).exp();return [[factor*z for z in row] for row in S]
def close(x,y,tol=3e-12):return abs(x-y)<=tol*max(1,abs(x),abs(y))
def fails(fn):
 try:fn()
 except ValueError:return True
 return False
def main():
 decimal.getcontext().prec=80;comparisons=0
 for d in (-3.,0.,3.):
  for m in (1.,2.):
   a,b,r=bridge.rates(d,m);need(close(a*b,m*m),'rate product');need(close(a+b,r),'rate sum')
   for t in (.1,1.,3.):
    E=exp_literal(d,m,t)
    for i in range(2):
     need(close(sum(math.exp(bridge.logP(d,m,t,i,j)) for j in range(2)),1.),'Markov row')
     for j in range(2):
      need(close(bridge.logE(d,m,t,i,j),float(E[i][j].ln())),'literal transfer');comparisons+=1
      vals=[]
      for k in range(21):
       u=t*k/20
       val=bridge.log_survival(d,m,t,i,j,u);vals.append(val)
       tail=exp_literal(d,m,t-u)[i][j]
       literal=(D(0) if i==0 else -D(str(d)))*D(str(u))+tail.ln()-E[i][j].ln() if tail else -math.inf
       need(close(val,float(literal)) if math.isfinite(val) else literal==-math.inf,'literal survival')
      need(all(x>=y-1e-12 for x,y in zip(vals,vals[1:])),'monotone survival')
      need(abs(vals[0])<1e-12,'initial survival')
      need(vals[-1]==-math.inf if i!=j else math.isfinite(vals[-1]),'atom vs forced switch')
    Ea=exp_literal(d,m,t/3);Eb=exp_literal(d,m,t*2/3);prod=mm(Ea,Eb)
    for i in range(2):
     for j in range(2):need(close(float(prod[i][j]),float(E[i][j])),'semigroup')
 # d0: direct hyperbolic inverse; deterministic levels, no random draws.
 for m in (1.,2.):
  T=.7
  for end in (0,1):
   for level in (0.,.1,.4,.8,.999):
    result=bridge.inverse_first(0.,m,T,0,end,level)
    atom=1/math.cosh(m*T) if end==0 else 0.
    if end==0 and level>=1-atom:need(result['no_event'],'no-event atom')
    else:
     target=T-(math.acosh((1-level)*math.cosh(m*T)) if end==0 else math.asinh((1-level)*math.sinh(m*T)))/m
     lo,hi=result['bracket'];need(lo-2e-15<=target<=hi+2e-15,'hyperbolic inverse bracket')
 # Large signed difference: the naive rationalized denominator cancels for d<0.
 for d in (-1e8,1e8,-1e308,1e308):
  a,b,r=bridge.rates(d,1.);need(a>0 and b>0 and close(a*b,1.,1e-12),'stable signed rates')
  t=1e-308 if abs(d)>1e100 else 1.
  for i in (0,1):
   for j in (0,1):need(math.isfinite(bridge.logP(d,1.,t,i,j)),'rare endpoint log P')
 need(math.hypot(-1e8,2.)+(-1e8)==1.4901161193847656e-08 or math.hypot(-1e8,2.)+(-1e8)>=0,'platform cancellation observation')
 # Exact forced endpoints and singleton behavior.
 need(bridge.inverse_first(3.,1.,0.,0,0,.5)['no_event'],'zero-time same')
 need(fails(lambda:bridge.inverse_first(3.,1.,0.,0,1,.5)),'zero-time incompatible')
 need(bridge.singleton_bridge(True)['no_event'],'singleton')
 need(fails(lambda:bridge.singleton_bridge(False)),'singleton incompatible')
 need(fails(lambda:bridge.rates(1.,1e-300)),'unrepresentable rate rejects')
 # Genuine biased controls: unconditioned Q waiting omits endpoint h; wrong alias rate changes law.
 correct=bridge.log_survival(2.,1.,.8,0,1,.3);a,_,_=bridge.rates(2.,1.)
 need(abs(correct-(-a*.3))>.01,'omitted backward endpoint factor biased')
 need(abs(bridge.log_survival(0.,1.,.8,0,0,.3)-bridge.log_survival(0.,2.,.8,0,0,.3))>.01,'wrong alias rate biased')
 return dict(checks=N,transfer_comparisons=comparisons,scope='deterministic analytic controls only; no trajectory/profile',naive_negative_d_denominator=math.hypot(-1e16,2.)-1e16)
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180);t=time.monotonic();r=main();r['seconds']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<=384,'RSS');r['checks']=N;print(json.dumps(r,indent=2))

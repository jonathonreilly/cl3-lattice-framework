import sys,types,time,signal,resource,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s toy cap')));signal.alarm(29)
for name in ('interval','core'):
 p=P/(name+'.py');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
c=sys.modules['core'];iv=sys.modules['interval'];start=time.monotonic();checks=0;maxcall=0
for i in range(1024):
 s=F(2)**(i%11-7)*F(17+i%7,16);t=F(2)**((7*i)%67-64)/3
 ds=s/F(2**160);dt=t/F(2**160);si=(s-ds,s+ds);ti=(t-dt,t+dt)
 # Derivative interval at a bracket, using exact one-atom Lipschitz enclosure.
 ac=1/(1+s*s);dac=-2*s/(1+s*s)**2
 ai=(ac-2*ds,ac+2*ds);dai=(dac-6*ds,dac+6*ds)
 at=(1/(1+ti[1]**2),1/(1+ti[0]**2))
 tm=time.monotonic();g,h=c.integrands(si,ti,ai,dai,at);maxcall=max(maxcall,time.monotonic()-tm)
 for bounds,truth in [(g,1/((1+s*s)*(1+t*t))),(h,2*s/((1+s*s)**2*(1+t*t)))]:
  if not bounds[0]<=truth<=bounds[1]:raise ValueError('one-atom containment')
  checks+=1
try:c.integrands((F(1),F(1)),(F(1),F(1)),(F(1),F(1)),(F(0),F(0)),(F(1),F(1)));raise RuntimeError('collision accepted')
except ValueError:checks+=1
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if seconds>30 or rss>384*1048576:raise ValueError('toy budget')
print(json.dumps({'status':'PASS','scope':'synthetic X=1 arithmetic only','pairs':1024,'predicates':checks,'seconds':seconds,'max_pair_seconds':maxcall,'rss_bytes':rss,'physical_calls':0},indent=2))

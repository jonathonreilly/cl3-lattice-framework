"""Fabricated receipts. Moment function is explicitly stubbed; no physical integral."""
import tempfile,json,types
from pathlib import Path
from fractions import Fraction as F
p=Path(__file__).resolve().parent;s=types.ModuleType('schema');exec(compile((p/'schema.py').read_bytes(),str(p/'schema.py'),'exec'),s.__dict__);s.moments=lambda:{n:1 for n in range(2,42)}
def write(p,x):p.write_text(json.dumps(x)+'\n')
with tempfile.TemporaryDirectory()as d:
 o=Path(d);(o/'PANELS').mkdir();rf={'authorization':{},'worker_freeze':'w'};write(o/'STARTED.json',{})
 for j in range(67):write(o/f'PANELS/{j:02d}.json',{'panel':j-64,'value':['0','0'],'cumulative':['0','0']})
 high=sum((F((-1)**n,(2*n+1)*8**(2*n+1))for n in range(40)),F(0));rem=F(12**42,81*8**81);rad=F(256,4**52);eps=F(1,2**64);low=6*eps-eps**3/3;hi=low+F(17,60)*eps**5/5;pl,pu=s.pi();ans=s.mul(s.add(s.add((F(0),F(0)),(high,high+rem)),(low-rad,hi+rad)),(2/pu,2/pl))
 t={'moments':{str(n):'1'for n in range(2,42)},'high_partial':str(high),'high_remainder':str(rem),'low_interval':[str(low),str(hi)],'quadrature_radius':str(rad)};write(o/'TAIL.json',t)
 r={**{k:v for k,v in t.items()if k!='moments'},'observable':'nu=E_X_power_3_over_2','status':'CERTIFIED_TARGET','interval':list(map(str,ans)),'width':str(ans[1]-ans[0]),'target':str(F(2,10**19)),'middle':['0','0'],'middle_width_gate':True,'tail_terms':40,'panels':67,'nodes':1742,'oracle_calls':0,'new_catalog_only_integral':True,'seconds':1};write(o/'RESULT.json',r)
 part={'stage':'complete','current':2,'panels':[f'PANELS/{j:02d}.json'for j in range(67)],'sum':['0','0'],'seconds':2};write(o/'PARTIAL.json',part);w={'status':'COMPLETE_CATALOG_INTEGRAL','runtime_sha256':'w','result_sha256':s.sha(o/'RESULT.json'),'seconds':3,'rss_bytes':100};write(o/'WORKER_COMPLETE.json',w);s.check(o,rf,4);checks=1
 for kind in('low','moment','width','time','bool_count'):
  rr=dict(r);tt=json.loads(json.dumps(t));ww=dict(w)
  if kind=='low':rr['low_interval']=['0','0']
  if kind=='moment':tt['moments']['41']='2'
  if kind=='width':rr['target']='1'
  if kind=='time':ww['seconds']=30
  if kind=='bool_count':rr['oracle_calls']=False
  write(o/'RESULT.json',rr);write(o/'TAIL.json',tt);ww['result_sha256']=s.sha(o/'RESULT.json');write(o/'WORKER_COMPLETE.json',ww)
  try:s.check(o,rf,4)
  except ValueError:checks+=1
  else:raise AssertionError(kind)
 print(json.dumps({'status':'PASS_STUBBED_MOMENT_SCHEMA','checks':checks,'integral_calls':0,'oracle_calls':0}))

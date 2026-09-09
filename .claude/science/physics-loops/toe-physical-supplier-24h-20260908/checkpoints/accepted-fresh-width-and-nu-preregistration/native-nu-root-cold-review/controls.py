import pathlib,types,tempfile,json
from fractions import Fraction as F
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-nu-catalog-root-review');s=types.ModuleType('schema');exec((p/'schema.py').read_bytes(),s.__dict__);s.moments=lambda:{k:0 for k in range(2,42)}
with tempfile.TemporaryDirectory() as td:
 o=pathlib.Path(td);(o/'PANELS').mkdir();write=lambda n,x:(o/n).write_text(json.dumps(x));rf={'authorization':{},'worker_freeze':'toy'};write('STARTED.json',{});names=[f'PANELS/{j:02d}.json' for j in range(67)]
 for j,n in enumerate(names):write(n,{'panel':j-64,'value':['0','0'],'cumulative':['0','0']})
 eps=F(1,2**64);low=6*eps-eps**3/3;hi=low+F(17,60)*eps**5/5;rem=F(12**42,81*8**81);rad=F(256,4**52);pl,pu=s.pi();iv=s.mul(s.add((F(0),rem),(low-rad,hi+rad)),(2/pu,2/pl));t={'moments':{str(k):'0' for k in range(2,42)},'high_partial':'0','high_remainder':str(rem),'quadrature_radius':str(rad),'low_interval':[str(low),str(hi)]};r=dict(t);r.pop('moments');r.update(observable='nu=E_X_power_3_over_2',seconds=1,panels=67,nodes=1742,tail_terms=40,oracle_calls=0,new_catalog_only_integral=True,middle_width_gate=True,middle=['0','0'],interval=list(map(str,iv)),width=str(iv[1]-iv[0]),target=str(F(2,10**19)),status='CERTIFIED_TARGET' if iv[1]-iv[0]<=F(2,10**19) else 'INDETERMINATE');write('TAIL.json',t);write('PARTIAL.json',{'stage':'complete','current':2,'panels':names,'sum':['0','0'],'seconds':2})
 def seal():
  write('RESULT.json',r);write('WORKER_COMPLETE.json',{'status':'COMPLETE_CATALOG_INTEGRAL','runtime_sha256':'toy','result_sha256':s.sha(o/'RESULT.json'),'seconds':3,'rss_bytes':100})
 seal();s.check(o,rf,4);n=1
 for k,v in [('oracle_calls',False),('tail_terms',39),('middle_width_gate',False),('width','0')]:
  old=r[k];r[k]=v;seal()
  try:s.check(o,rf,4)
  except ValueError:n+=1
  else:raise AssertionError(k)
  r[k]=old
 seal();write('FAILURE.json',{})
 try:s.check(o,rf,4)
 except ValueError:n+=1
 else:raise AssertionError('failure')
 print(n,'PASS synthetic stub-moment schema checks; zero catalog/integral/moment-production calls')

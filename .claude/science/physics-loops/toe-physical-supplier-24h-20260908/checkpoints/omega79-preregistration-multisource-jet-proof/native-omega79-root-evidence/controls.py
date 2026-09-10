"""Full schema shape on fabricated catalog; no accepted sources or M44/M45 evaluation."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import tempfile,sys,importlib.util,json,copy
B=Path('/private/tmp/toe-24h-probes-20260908');W=B/'native-omega79-catalog-supplier-design';R=B/'native-omega79-root-review'
def load(name,p):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
for n in ['interval','pi','loader','compute','worker']:load(n,W/(n+'.py'))
s=load('schema_test',R/'schema.py');worker=sys.modules['worker'];compute=sys.modules['compute'];loader=sys.modules['loader'];checks=[]
m={k:F(1)for k in range(44)};m[0]=F(1);m[1]=F(6);m[2]=F(42)
catalog=[{'id':i,'panel':i//26-64,'t_interval':(F(1,2),F(1,2)),'A_interval':(F(1,4),F(1,4)),'weight_interval':(F(1,1000),F(1,1000))}for i in range(1742)]
# These substitutions apply only in this temporary synthetic test module.
loader.reused_moments=lambda *args:dict(m);loader.load=lambda *args:catalog;compute.moment=lambda k:F(1);s.inputs=lambda b:(dict(m),catalog);s.new_moments=lambda:{44:F(1),45:F(1)}
def write(p,x):p.write_text(json.dumps(x)+'\n')
with tempfile.TemporaryDirectory(prefix='OMEGA79-SYNTHETIC-')as td:
 T=Path(td);O=T/'out';O.mkdir();p=T/'worker';p.mkdir();write(p/'BINDING.json',{'synthetic':True});rf={'worker_path':str(p),'worker_freeze':'synthetic'};auth={'runtime_sha256':'synthetic','binding_sha256':s.sha(p/'BINDING.json'),'output':str(O.resolve()),'no_retry':True};write(O/'STARTED.json',auth)
 worker.run({},O);r=s.read(O/'RESULT.json');part=s.read(O/'PARTIAL.json');elapsed=max(r['seconds'],part['seconds'])+.25;w={'status':'COMPLETE_NEW_OMEGA79_ONLY','runtime_sha256':'synthetic','binding_sha256':auth['binding_sha256'],'result_sha256':s.sha(O/'RESULT.json'),'seconds':elapsed,'rss_bytes':1000};write(O/'WORKER_COMPLETE.json',w)
 s.check(O,rf,elapsed+.25,lambda x:None);checks.append('full1821files1742dualnodes')
 originals={x.relative_to(O).as_posix():x.read_bytes()for x in O.rglob('*')if x.is_file()}
 def restore():
  for x,data in originals.items():(O/x).write_bytes(data)
 def reject(label,mut):
  restore();mut();z=s.read(O/'WORKER_COMPLETE.json');z['result_sha256']=s.sha(O/'RESULT.json');write(O/'WORKER_COMPLETE.json',z)
  try:s.check(O,rf,elapsed+.25,lambda x:None)
  except ValueError:checks.append(label);return
  raise AssertionError(label+' accepted')
 def badnode():
  z=s.read(O/'NODES/0000.json');z['values']['3']['integrand']=['0','0'];write(O/'NODES/0000.json',z)
 reject('wrong node integrand',badnode)
 def badmoment():write(O/'M44.json',{'index':44,'value':'2'})
 reject('wrong new moment',badmoment)
 def badflags():
  z=copy.deepcopy(r);z['rows'][0]['middle_width_gate']=not z['rows'][0]['middle_width_gate'];write(O/'RESULT.json',z);q=copy.deepcopy(part);q['current']['result']=z;write(O/'PARTIAL.json',q)
 reject('coherently rehashed false gate',badflags)
 def badcount():
  z=copy.deepcopy(r);z['nodes']=1742.0;write(O/'RESULT.json',z)
 reject('float count',badcount)
 reject('hidden failure',lambda:write(O/'FAILURE.json',{}));(O/'FAILURE.json').unlink()
 reject('zero worker time',lambda:write(O/'WORKER_COMPLETE.json',{**w,'seconds':0}))
# Abstract coefficient convolution identity, no native dispersion moments.
c=[1,3,4,7,11]
for n in range(5):
 two=[sum(comb(k,j)*c[j]*c[k-j]for j in range(k+1))for k in range(n+1)];v=sum(comb(n,j)*two[j]*c[n-j]for j in range(n+1));direct=sum(factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))*c[a]*c[b]*c[n-a-b]for a in range(n+1)for b in range(n-a+1));assert v==direct;checks.append('abstract convolution degree'+str(n))
print(json.dumps({'status':'PASS','checks':checks,'native_inputs':False,'new44_45_moments_mocked':True,'catalog_inputs_and_inherited_moments_mocked':True,'actual_worker_integrand_and_independent_root_arithmetic_exercised':True},indent=2))

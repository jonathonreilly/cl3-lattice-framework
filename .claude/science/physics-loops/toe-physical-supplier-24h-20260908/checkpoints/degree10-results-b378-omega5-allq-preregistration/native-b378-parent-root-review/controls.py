from pathlib import Path
from fractions import Fraction as F
import types,json,hashlib,tempfile
P=Path(__file__).resolve().parent;src=P.parent/'native-b378-root-review/schema.py';m=types.ModuleType('schema');exec(compile(src.read_bytes(),str(src),'exec'),m.__dict__)
assert m.moments(3)==[1,6,42,324]
for x in [F(1,3),F(1,7),F(-2,9)]:a,b=m.rnd((x,x));assert a<=x<=b and b-a<=F(1,1<<192)
# Full metadata/census fixture. Native moment function deliberately stubbed below.
m.moments=lambda:[1]+[0]*40
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[enc(y)for y in x]
 if isinstance(x,dict):return{k:enc(y)for k,y in x.items()}
 return x
def save(p,x):p.write_text(json.dumps(enc(x))+'\n')
with tempfile.TemporaryDirectory(dir=P)as tmp:
 t=Path(tmp);out=t/'out';out.mkdir();wp=t/'worker';wp.mkdir();cat=t/'cat';(cat/'ORACLES').mkdir(parents=True);new=t/'new';new.mkdir();geom=[];cr=[];maps=[];nodes=[];hashes={}
 for i in range(1742):
  es=[]
  for side in range(2):
   k=2*i+side;p=cat/('ORACLES/%04d.json'%k);save(p,{'s':'2','A':['1/4','1/4']});h=sha(p);es.append(h);cr.append({'id':k,'path':'ORACLES/%04d.json'%k,'sha256':h,'gate':'PASS'})
  geom.append({'id':i,'endpoint_ids':[2*i,2*i+1],'t_interval':['2','2'],'weight':['1/100','1/100']})
  maps.append({'stage':'mapped_catalog','pole':0,'data':{'id':i,'endpoint_ids':[2*i,2*i+1],'endpoint_hashes':es,'geometry_sha256':'PENDING','mapped':{k:m.rnd(v)for k,v in {'t':(F(2),F(2)),'weight':(F(1,100),F(1,100)),'A':(F(1,4),F(1,4))}.items()}}})
 for i in range(378):
  nodes.append({'id':i,'s':'1/2'});p=new/('RAW_%03d.json'%i);save(p,{'id':i,'raw':{'s':'1/2','A':['1/4','1/4']}});hashes[str(i)]=sha(p);maps.append({'stage':'mapped_new_A','pole':0,'data':{'id':i,'raw_sha256':sha(p),'mapped_A':[F(1,4)]*2}})
 files={}
 for role,value in [('new_nodes',{'rows':nodes}),('catalog_geometry',{'nodes':geom}),('catalog_result',{'rows':cr}),('geometry_result',{'rows':[{'id':i,'required_B_radius':'1/100'}for i in range(378)]})]:
  p=t/role;save(p,value);files[role]={'path':str(p),'sha256':sha(p)}
 for e in maps[:1742]:e['data']['geometry_sha256']=files['catalog_geometry']['sha256']
 save(wp/'BINDING.json',{'files':files,'catalog_directory':str(cat),'new_directory':str(new),'new_raw_hashes':hashes})
 (out/'MAPPED_INPUTS.jsonl').write_text(''.join(json.dumps(enc(x))+'\n'for x in maps))
 panels=[{'stage':'moment','pole':0,'data':{'n':n,'value':F(v)}}for n,v in enumerate(m.moments())];rows=[];ss=(F(1,4),)*2;a=(F(1,4),)*2;eps=F(1,2**64);lo=m.add(m.scale(a,eps),(-eps**3*F(17,60)/(3*ss[0]),F(0)));hi=(F(0),)*2;c=m.sub((F(1),)*2,m.mul(ss,a))
 for n in range(40):hi=m.add(hi,m.scale(c,F((-1)**n,(2*n+1)*8**(2*n+1))));c=m.sub((F(0),)*2,m.mul(ss,c))
 hi=m.add(hi,(F(0),F(12**40,81*8**81)));quad=F(128,4**52);pl,pu=m.pi();factor=m.scale(m.rnd((1/pu,1/pl)),F(2));ans=m.mul(m.add(m.add(m.add((F(1),)*2,lo),hi),(-quad,quad)),factor)
 for i in range(378):
  panels +=[{'stage':'panel','pole':i,'data':{'completed':26*(j+1),'sum':(F(1),)*2}}for j in range(67)];panels.append({'stage':'final_interval','pole':i,'data':{'low':lo,'high':hi,'quadrature_radius':str(quad),'B':ans}});row={'id':i,'s':'1/2','B':ans,'required_radius':F(1,100),'target_met':(ans[1]-ans[0])/2<=F(1,100)};rows.append(row);save(out/('B_%03d.json'%i),row)
 (out/'PANELS.jsonl').write_text(''.join(json.dumps(enc(x))+'\n'for x in panels));result={'status':'COMPLETE_NEW_B378_ONLY','rows':rows,'seconds':1,'all_targets_met':all(x['target_met']for x in rows),'witness_computed':False};save(out/'RESULT.json',result);save(out/'PARTIAL.json',{'current':{'stage':'complete','pole':378,'data':{}},'completed':378})
 def done():save(out/'WORKER_COMPLETE.json',{'status':'COMPLETE','freeze_sha256':'FAKE','result_sha256':sha(out/'RESULT.json'),'rss_bytes':100,'seconds':2})
 done();rf={'worker_path':str(wp),'worker_freeze':'FAKE'};m.check(out,rf,3,lambda x:None)
 # Parent affected guards using the complete nonnative fixture.
 d=json.loads((out/'WORKER_COMPLETE.json').read_text());saved=dict(d)
 for field,bad in [('rss_bytes',True),('seconds',float('nan')),('seconds',4)]:
  d=dict(saved);d[field]=bad;save(out/'WORKER_COMPLETE.json',d)
  try:m.check(out,rf,3,lambda x:None)
  except ValueError:pass
  else:raise AssertionError('invalid resource accepted '+field)
 save(out/'WORKER_COMPLETE.json',saved)
 rows[0]['target_met']=not rows[0]['target_met'];save(out/'B_000.json',rows[0]);save(out/'RESULT.json',result);done()
 try:m.check(out,rf,3,lambda x:None)
 except ValueError:pass
 else:raise AssertionError('false target survived')
 save(P/'CONTROLS.json',{'full_fabricated_maps_panels':'PASS','coherent_false_target':'REJECTED','moments_in_full_fixture':'STUBBED_NONPHYSICAL','only_real_moment_control':'M0..3','native_inputs_read':0,'original_integrands_evaluated':0})
print('PASS')

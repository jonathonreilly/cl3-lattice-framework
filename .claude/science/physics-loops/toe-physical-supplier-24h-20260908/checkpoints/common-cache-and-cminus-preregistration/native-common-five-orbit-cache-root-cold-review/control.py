from pathlib import Path
import json,hashlib,types,tempfile
P=Path('/private/tmp/toe-24h-probes-20260908/native-common-five-orbit-cache-root-review');m=types.ModuleType('schema');exec(compile((P/'schema.py').read_bytes(),str(P/'schema.py'),'exec'),m.__dict__);S=2**192;h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x)+'\n')
f=json.loads((P/'ROOT_FREEZE.json').read_text());checks=[]
with tempfile.TemporaryDirectory(prefix='cache-schema-stub-') as d:
 o=Path(d);count=0
 with(o/'CACHE.ndjson').open('w') as out:
  for t in m.TYPES:
   for i in range(132):
    e=[[j,0,0,0,0] for j in range(0 if t=='cd' else i,132)];count+=len(e);out.write(json.dumps({'type':t,'i':i,'entries':e,'count':count,'max_width':0})+'\n')
 cs=[{'kind':t,'id':i,'det':[S,S],'signed':[[[0,0]]*2]*2,'residual':[[[0,0]]*2]*2} for t in ('P','O') for i in range(66)]
 def coeff(): (o/'COEFFICIENTS.ndjson').write_text(''.join(json.dumps(c)+'\n' for c in cs))
 coeff();r={'status':'COMPLETE_COMMON_CACHE_MIDPOINT_ARITHMETIC','entries':52536,'raw_rows':396,'closed_rows':792,'coefficients':132,'physical_error_ledger_certified':False,'pure_projector_computed':False,'physical_error_ledger':'separate and required','seconds':1,'cache_sha256':h(o/'CACHE.ndjson'),'coefficient_sha256':h(o/'COEFFICIENTS.ndjson'),'arithmetic_radius':'0','orbits':[{'orbit':list(t),'closed_trace':[0,0],'denominator':S,'raw_rows':396,'closed_rows':792,'arithmetic_radius':'0'} for t in m.ORBITS]}
 w={'status':'COMPLETE_MIDPOINT_CACHE_ONLY','freeze_sha256':f['worker_freeze'],'binding_sha256':'stub','seconds':2,'rss_bytes':1024}
 def refresh():
  r['coefficient_sha256']=h(o/'COEFFICIENTS.ndjson');write(o/'RESULT.json',r);w['result_sha256']=h(o/'RESULT.json');write(o/'WORKER_COMPLETE.json',w)
 write(o/'STARTED.json',{'runtime_sha256':f['worker_freeze'],'binding_sha256':'stub'});part={'stage':'five_orbit_gates','coefficients':132,'completed_cache_rows':660,'entries':52536,'maximum_width':0};write(o/'PARTIAL.json',part);refresh();m.check(o,f['worker_freeze'],3);checks.append('accept complete fabricated schema')
 def reject(label):
  try:m.check(o,f['worker_freeze'],3)
  except (ValueError,KeyError):checks.append(label)
  else:raise ValueError('survived '+label)
 cs[0]['residual']=[[[0,3*S//2**42]]*2]*2;coeff();refresh();reject('factor2 residual after rehash');cs[0]['residual']=[[[0,0]]*2]*2;coeff();refresh()
 for key,val in [('seconds',float('nan')),('rss_bytes',384*1048576+1),('freeze_sha256','bad')]:
  old=w[key];w[key]=val;refresh();reject(key);w[key]=old;refresh()
 r['orbits'][0]['closed_trace']=[0,S];refresh();reject('trace after rehash');r['orbits'][0]['closed_trace']=[0,0];refresh()
 part['completed_cache_rows']=659;write(o/'PARTIAL.json',part);reject('partial count');part['completed_cache_rows']=660;write(o/'PARTIAL.json',part)
 old=(o/'CACHE.ndjson').read_bytes();(o/'CACHE.ndjson').write_bytes(old[:-10]);r['cache_sha256']=h(o/'CACHE.ndjson');refresh()
 try:m.check(o,f['worker_freeze'],3)
 except (ValueError,KeyError):checks.append('truncated stream after rehash')
 else:raise ValueError('truncation survived')
 print(json.dumps({'status':'PASS','checks':checks,'count':len(checks),'cache_calls':0,'coefficient_calls':0,'native_calls':0},indent=2))

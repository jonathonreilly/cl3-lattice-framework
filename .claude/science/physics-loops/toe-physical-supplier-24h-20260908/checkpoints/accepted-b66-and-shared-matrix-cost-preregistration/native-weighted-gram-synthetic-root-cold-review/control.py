from pathlib import Path
import json,hashlib,types,tempfile
P=Path('/private/tmp/toe-24h-probes-20260908/native-weighted-gram-synthetic-root-review')
source=(P/'schema.py').read_bytes();m=types.ModuleType('reviewed_schema');exec(compile(source,str(P/'schema.py'),'exec'),m.__dict__)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x)+'\n')
f=json.loads((P/'ROOT_FREEZE.json').read_text());checks=[]
for n,v in f['files'].items():
 if h(P/n)!=v:raise ValueError('pin')
with tempfile.TemporaryDirectory(prefix='schema-only-') as t:
 o=Path(t);classes=[]
 for kind in ('P','O'):
  p=o/kind;p.mkdir();stream=p/'UPPER_TRIANGLE.ndjson'
  with stream.open('w') as out:
   for i in range(264):out.write(json.dumps({'i':i,'entries':[[j,'0','0','0','0'] for j in range(i,264)]})+'\n')
  q={'status':'CERTIFIED_MIDPOINT_ARITHMETIC_ONLY','class':kind,'nodes':66,'raw_dimension':264,'implicit_closed_dimension':528,'triangle_rows':264,'triangle_entries':34980,'denominator':str(2**192),'physical_input_error_charged_separately':True,'purification_performed':False,'Gram_operator_rounding_radius':'0','coefficient_operator_rounding_radius':'0','coefficient_inverse_residual_operator_bound':'0','triangle_sha256':h(stream),'triangle_bytes':stream.stat().st_size,'max_entry_width_scaled':'0','trace_closed':['0','0'],'seconds':1}
  write(p/'RESULT.json',q);write(p/'COEFFICIENTS.json',{'class':kind,'nodes':[{'id':i} for i in range(66)],'physical_input_errors_included':False});write(p/'PARTIAL.json',{'stage':'final_gate','completed_triangle_rows':264,'completed_coefficients':66})
  classes.append({'class':kind,'result_sha256':h(p/'RESULT.json'),'triangle_sha256':h(stream),'seconds':1})
 r={'status':'COMPLETE_FIXED_SYNTHETIC_COST','synthetic_only':True,'physical_scalar_calls':0,'native_gram_computed':False,'physical_error_ledger_certified':False,'pairings_or_states_computed':False,'classes':classes,'seconds':2}
 write(o/'RESULT.json',r);write(o/'PARTIAL.json',{'stage':'O_complete','completed_classes':classes,'synthetic_only':True});w={'status':'COMPLETE_SYNTHETIC_ONLY','runtime_sha256':f['worker_freeze'],'result_sha256':h(o/'RESULT.json'),'seconds':3,'rss_bytes':1024};write(o/'WORKER_COMPLETE.json',w)
 m.check(o,f['worker_freeze'],4);checks.append('accept fabricated zero streams, no matrix assembly')
 for field,value in [('seconds',float('nan')),('seconds',181),('rss_bytes',0),('rss_bytes',384*1048576+1),('runtime_sha256','wrong'),('status','FAILED')]:
  bad=dict(w);bad[field]=value;write(o/'WORKER_COMPLETE.json',bad)
  try:m.check(o,f['worker_freeze'],4)
  except ValueError:checks.append('reject '+field+' '+str(value))
  else:raise ValueError('mutation survived')
 write(o/'WORKER_COMPLETE.json',w)
 for name in ('PARTIAL.json','P/COEFFICIENTS.json','P/UPPER_TRIANGLE.ndjson'):
  p=o/name;old=p.read_bytes();p.write_text('{}\n')
  try:m.check(o,f['worker_freeze'],4)
  except (ValueError,KeyError):checks.append('reject malformed '+name)
  else:raise ValueError('malformed survived')
  p.write_bytes(old)
 print(json.dumps({'status':'PASS','checks':checks,'count':len(checks),'schema_sha256':hashlib.sha256(source).hexdigest(),'matrix_assembly_calls':0,'native_calls':0},indent=2))

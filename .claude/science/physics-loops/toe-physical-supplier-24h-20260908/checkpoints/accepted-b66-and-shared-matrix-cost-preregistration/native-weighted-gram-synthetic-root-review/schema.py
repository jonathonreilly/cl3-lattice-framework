from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(out,freeze,elapsed):
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());part=json.loads((out/'PARTIAL.json').read_text())
 req(w['status']=='COMPLETE_SYNTHETIC_ONLY' and w['runtime_sha256']==freeze and w['result_sha256']==sha(out/'RESULT.json'),'worker identity')
 req(r['status']=='COMPLETE_FIXED_SYNTHETIC_COST' and r['synthetic_only'] is True and r['physical_scalar_calls']==0 and r['native_gram_computed'] is False and r['physical_error_ledger_certified'] is False and r['pairings_or_states_computed'] is False,'scope')
 req([x['class'] for x in r['classes']]==['P','O'],'two classes');req(part=={'stage':'O_complete','completed_classes':r['classes'],'synthetic_only':True},'complete partial')
 req(all(isinstance(t,(int,float)) and math.isfinite(t) and t>0 for t in [r['seconds'],w['seconds'],elapsed]) and r['seconds']<=w['seconds']<=elapsed<=180,'elapsed')
 req(0<w['rss_bytes']<=384*1048576,'worker RSS');counts=[]
 for kind,rr in zip(('P','O'),r['classes']):
  p=out/kind;q=json.loads((p/'RESULT.json').read_text());c=json.loads((p/'COEFFICIENTS.json').read_text());pr=json.loads((p/'PARTIAL.json').read_text());den=1<<192
  req(rr['result_sha256']==sha(p/'RESULT.json') and rr['triangle_sha256']==sha(p/'UPPER_TRIANGLE.ndjson')==q['triangle_sha256'],'retained class hashes')
  req(q['status']=='CERTIFIED_MIDPOINT_ARITHMETIC_ONLY' and q['class']==kind and q['nodes']==66 and q['raw_dimension']==264 and q['implicit_closed_dimension']==528 and q['triangle_rows']==264 and q['triangle_entries']==34980 and q['denominator']==str(den),'full class census')
  req(q['physical_input_error_charged_separately'] is True and q['purification_performed'] is False,'class scope');req(F(q['Gram_operator_rounding_radius'])<=F(1,2**60) and F(q['coefficient_operator_rounding_radius'])<=F(1,2**40) and F(q['coefficient_inverse_residual_operator_bound'])<=F(1,2**40),'arithmetic gates')
  req(c['class']==kind and len(c['nodes'])==66 and [x['id'] for x in c['nodes']]==list(range(66)) and c['physical_input_errors_included'] is False,'coefficients')
  req(pr['stage']=='final_gate' and pr['completed_triangle_rows']==264 and pr['completed_coefficients']==66,'class partial')
  count=0;maxw=0;trace_lo=trace_hi=0
  with(p/'UPPER_TRIANGLE.ndjson').open() as f:
   for i,line in enumerate(f):
    x=json.loads(line);req(i<264 and x['i']==i and [e[0] for e in x['entries']]==list(range(i,264)),'triangle indices')
    for j,gl,gu,jl,ju in x['entries']:
     gl,gu,jl,ju=map(int,(gl,gu,jl,ju));req(gl<=gu and jl<=ju,'interval order');maxw=max(maxw,gu-gl,ju-jl);count+=1
     if j==i:req(jl==ju==0,'skew diagonal');trace_lo+=gl;trace_hi+=gu
  req(count==34980 and i==263,'complete triangle');req(q['triangle_bytes']==(p/'UPPER_TRIANGLE.ndjson').stat().st_size,'stream bytes');req(maxw==int(q['max_entry_width_scaled']),'max width');req(F(q['Gram_operator_rounding_radius'])==F(528*maxw,2*den),'Gram radius')
  req(tuple(map(F,q['trace_closed']))==(F(2*trace_lo,den),F(2*trace_hi,den)) and F(2*trace_hi,den)<318,'closed trace')
  req(0<q['seconds']==rr['seconds']<=r['seconds'],'class times');counts.append(count)
 return {'status':'PASS_FIXED_SYNTHETIC_OUTPUT_SCHEMA','triangle_entries':sum(counts),'classes':['P','O'],'native_gram_computed':False,'physical_scalar_calls':0,'result_sha256':sha(out/'RESULT.json')}

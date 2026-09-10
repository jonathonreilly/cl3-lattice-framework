from pathlib import Path
from fractions import Fraction as F
import hashlib,json,types,tempfile
P=Path(__file__).resolve().parent;src=P.parent/'native-witness-geometry-root-review/schema.py';m=types.ModuleType('schema');exec(compile(src.read_bytes(),str(src),'exec'),m.__dict__)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v)+'\n')
with tempfile.TemporaryDirectory(dir=P) as tmp:
 t=Path(tmp);o=t/'out';o.mkdir();w=t/'worker';w.mkdir();cr=t/'cr';save(cr,{'ledger':{'input_radii':{'A':'1/10000000000000000000000000000000000000000'}}});a=t/'acc';save(a,{'status':'ACCEPTED_NEW_DESCRIPTOR_OPERATOR_COEFFICIENTS','result_sha256':sha(cr)});save(w/'BINDING.json',{'coefficient_result':{'path':str(cr),'sha256':sha(cr)},'coefficient_acceptance':{'path':str(a),'sha256':sha(a)}})
 ev=[{'stage':'before_accepted_radius_metadata'}]+[{'stage':'before_parse','role':x}for x in('new','old','outer')]
 for role,n in [('new',378),('old',66),('outer',1742)]:ev +=[{'stage':'before_normalize','role':role,'row':k}for k in range(n)]
 rows=[];G=1<<64;eb=F(1,10**5)/(7*(1<<40)*378);ea=eb/4;ar=F(json.loads(cr.read_text())['ledger']['input_radii']['A'])
 for k in range(378):
  row={'id':k,'gain_scale':G,'weighted_B_gain_units':G,'As_integral_gain_units':G,'catalog_integral_gain_units':G,'required_B_radius':str(eb),'required_As_radius_quarter_B_budget':str(ea),'accepted_max_A_radius':str(ar),'actual_A_meets_quarter_budget':ar<=ea,'catalog_radius_reserve':str(F(1,10**49))};rows.append(row);ev +=[{'stage':'before_node','id':k,'counts':[k*66,k*1742]},{'stage':'node_complete','data':row}]
 ev +=[{'stage':'complete','counts':[24948,658476]}];r={'status':'COMPLETE_GEOMETRY_GAIN_LEDGER','counts':[24948,658476],'seconds':1,'rows':rows,'old_B_required_radii':['1/100']*66,'c_required_radius':'1/100'}
 def write():
  save(o/'RESULT.json',r);save(o/'WORKER_COMPLETE.json',{'status':'COMPLETE','freeze_sha256':'synthetic','result_sha256':sha(o/'RESULT.json'),'seconds':2,'rss_bytes':100});save(o/'PARTIAL.json',{'current':ev[-1],'completed':378});(o/'EVENTS.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in ev))
 rf={'worker_path':str(w),'worker_freeze':'synthetic'};write();m.check(o,rf,3,lambda x:None)
 # Coherently retain a float counter in both copies: equality-only old schema accepts.
 r['counts'][0]=24948.0;ev[-1]['counts'][0]=24948.0;write()
 try:m.check(o,rf,3,lambda x:None);outcome='ACCEPTED_FLOAT_COUNTER'
 except ValueError:outcome='REJECTED_FLOAT_COUNTER'
 save(P/'CONTROLS.json',{'valid_full_metadata':'PASS','adverse':outcome,'native_reads':0,'events':len(ev)})
 print(outcome)

from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re

def check(O,rf,elapsed,progress):
 def req(v,s):
  if not v:raise ValueError(s)
 def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def rational(x,positive=True):
  req(type(x)is str and len(x)<5000 and re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?',x)is not None,'rational syntax')
  q=F(x);req(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<16000,'canonical rational')
  req(q>0 if positive else q>=0,'rational sign');return q
 O=Path(O);req(set(p.name for p in O.iterdir())=={'RESULT.json','EVENTS.jsonl','PARTIAL.json','WORKER_COMPLETE.json'},'output census')
 r=json.loads((O/'RESULT.json').read_text());done=json.loads((O/'WORKER_COMPLETE.json').read_text());part=json.loads((O/'PARTIAL.json').read_text());ev=[json.loads(l)for l in(O/'EVENTS.jsonl').read_text().splitlines()]
 req(r['status']=='COMPLETE_GEOMETRY_GAIN_LEDGER' and r['counts']==[24948,658476],'result status/counts')
 req(type(r['seconds'])in(int,float)and 0<r['seconds']<119,'worker inner seconds')
 req(done['status']=='COMPLETE' and done['freeze_sha256']==rf['worker_freeze']and done['result_sha256']==sha(O/'RESULT.json'),'worker complete pins')
 req(type(done['seconds'])in(int,float)and r['seconds']<=done['seconds']<119,'worker outer seconds')
 req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'worker RSS')
 req(len(ev)==2947,'event count');i=0
 def event(expected):
  nonlocal i
  req(ev[i]==expected,'event '+str(i));i+=1
 event({'stage':'before_accepted_radius_metadata'})
 for role in('new','old','outer'):event({'stage':'before_parse','role':role})
 for role,n in(('new',378),('old',66),('outer',1742)):
  for k in range(n):event({'stage':'before_normalize','role':role,'row':k})
 P=Path(rf['worker_path']);b=json.loads((P/'BINDING.json').read_text());acc=Path(b['coefficient_acceptance']['path']);cr=Path(b['coefficient_result']['path'])
 req(sha(acc)==b['coefficient_acceptance']['sha256']and sha(cr)==b['coefficient_result']['sha256'],'accepted metadata pins')
 a=json.loads(acc.read_text());req(a['result_sha256']==sha(cr)and a['status']=='ACCEPTED_NEW_DESCRIPTOR_OPERATOR_COEFFICIENTS','accepted metadata linkage')
 ar=rational(json.loads(cr.read_text())['ledger']['input_radii']['A']);req(ar<F(1,10**30),'accepted radius cap')
 req(type(r['rows'])is list and len(r['rows'])==378 and type(r['old_B_required_radii'])is list and len(r['old_B_required_radii'])==66,'rows census')
 flags=[];G=1<<64
 for k,row in enumerate(r['rows']):
  progress({'stage':'schema_row','id':k})
  event({'stage':'before_node','id':k,'counts':[k*66,k*1742]})
  event({'stage':'node_complete','data':row});req(type(row['id'])is int and row['id']==k and row['gain_scale']==G,'row identity')
  for field in('weighted_B_gain_units','As_integral_gain_units','catalog_integral_gain_units'):req(type(row[field])is int and 0<row[field]<1<<4096,'integer gain')
  eb=rational(row['required_B_radius']);ea=rational(row['required_As_radius_quarter_B_budget']);gotar=rational(row['accepted_max_A_radius'])
  req(eb==F(1,10**5)/(7*(1<<40)*378*F(row['weighted_B_gain_units'],G)),'B allocation')
  req(ea==eb/(4*max(F(row['As_integral_gain_units'],G),F(1))),'A quarter allocation')
  req(gotar==ar and type(row['actual_A_meets_quarter_budget'])is bool and row['actual_A_meets_quarter_budget']==(ar<=ea),'actual A comparison')
  req(rational(row['catalog_radius_reserve'])==F(row['catalog_integral_gain_units'],G)*F(1,10**49),'catalog reserve')
  flags.append(row['actual_A_meets_quarter_budget'])
 event({'stage':'complete','counts':[24948,658476]});req(i==len(ev),'event exhaustion')
 req(part=={'current':ev[-1],'completed':378},'partial final')
 for x in r['old_B_required_radii']:rational(x)
 rational(r['c_required_radius']);req(elapsed<119.5,'schema input time')
 return {'status':'ACCEPTED_GEOMETRY_GAIN_SCHEMA','count':378,'events':len(ev),'comparisons':[24948,658476],'result_sha256':sha(O/'RESULT.json'),'events_sha256':sha(O/'EVENTS.jsonl'),'actual_A_quarter_budget_pass_count':sum(flags),'independent_gain_arithmetic_replay':False,'independent_reported_gain_budget_reconciliation':True,'B_or_witness_certified':False}

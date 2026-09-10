"""Saved-T output and normalized-budget checks. No original T reconstruction."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,re

def need(x,m):
 if not x:raise ValueError(m)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rational(x):
 need(type(x)is str and len(x)<=20000 and re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?',x)is not None,'rational string')
 q=F(x);need(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=16384,'canonical bounded rational');return q
def timing(x):need(type(x)in(int,float)and math.isfinite(x)and 0<x<19,'worker timing');return x
def check(out,root,elapsed,progress):
 out=Path(out);binding=json.loads(Path(root['binding_path']).read_text());need(digest(root['binding_path'])==root['binding_sha256'],'binding hash')
 candidates=binding['candidates'];need(type(candidates)is list and len(candidates)==5,'five candidates')
 expected={'RESULT.json','PARTIAL.json','WORKER_COMPLETE.json'}|{f'{kind}_{i}.json' for kind in('NORM','BUDGET')for i in range(5)}
 need({p.name for p in out.iterdir()}==expected,'exact output membership')
 result=json.loads((out/'RESULT.json').read_text());need(result['status']=='COMPLETE_NEW_T_SENSITIVITY' and result['actual_consumer_precision_decided']is False,'result status')
 need(result['scope']=='exact savedT norm and normalized-consumer sufficient thresholds only','result scope');need(type(result['rows'])is list and len(result['rows'])==5,'five rows');timing(result['seconds'])
 hashes={}
 for i,item in enumerate(candidates):
  need(Path(item['path']).parent.name==f'ORBIT_{i}' and Path(item['path']).name=='CANDIDATE.json','original order')
  norm=json.loads((out/f'NORM_{i}.json').read_text());row=json.loads((out/f'BUDGET_{i}.json').read_text())
  need(type(norm['orbit'])is int and norm['orbit']==i and type(norm['dimension'])is int and norm['dimension']==48,'norm identity')
  need(type(norm['row_l1'])is list and type(norm['column_l1'])is list and len(norm['row_l1'])==len(norm['column_l1'])==48,'norm arrays')
  rr=list(map(rational,norm['row_l1']));cc=list(map(rational,norm['column_l1']));f2=rational(norm['frobenius_squared']);b=rational(norm['operator_norm_squared_upper'])
  need(min(rr)>0 and min(cc)>0 and f2>0 and b>0,'positive norms');need(sum(rr)==sum(cc),'entry absolute sum');need(b==min(f2,max(rr)*max(cc)),'norm upper formula')
  need(max(max(rr)**2,max(cc)**2)<=48*f2 and f2<=sum(rr)**2,'norm inequalities')
  gain=48*b;need(type(row['orbit'])is int and row['orbit']==i and row['candidate_sha256']==item['sha256'],'budget binding')
  need(rational(row['metric_gain'])==gain and rational(row['eta_metric_for_unit_trace_tau'])==F(1,10**9)/gain and rational(row['eta_metric_for_unit_trace_r2'])==F(1,10**16)/gain,'normalized budgets')
  need(row['scope']=='unit-trace PSD consumer only; actual consumer multiplier remains required','budget scope');need(result['rows'][i]==row,'result copy')
  hashes[f'NORM_{i}.json']=digest(out/f'NORM_{i}.json');hashes[f'BUDGET_{i}.json']=digest(out/f'BUDGET_{i}.json');progress({'stage':'schema_orbit','completed':i+1})
 partial=json.loads((out/'PARTIAL.json').read_text());need(partial=={'current':{'stage':'complete','orbit':4},'completed':5} and type(partial['completed'])is int and type(partial['current']['orbit'])is int,'complete partial')
 complete=json.loads((out/'WORKER_COMPLETE.json').read_text());need(complete['status']=='COMPLETE' and complete['freeze_sha256']==root['worker_freeze'],'complete binding');timing(complete['seconds']);need(result['seconds']<=complete['seconds'],'time order');need(type(complete['rss_bytes'])is int and 0<complete['rss_bytes']<=384*1048576,'worker RSS');need(complete['result_sha256']==digest(out/'RESULT.json'),'result digest')
 return {'status':'ACCEPTED_SAVED_T_NORMS_SCHEMA','count':5,'result_sha256':digest(out/'RESULT.json'),'record_sha256':hashes,'actual_consumer_precision_decided':False,'independent_original_T_reconstruction':False,'scope':'Norm record relationships and exact normalized budgets checked; original T arithmetic inherits reviewed worker','seconds_before_schema':elapsed}

"""Compact semantic checker; original event and estimator arithmetic are not replayed."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,copy
P=Path(__file__).resolve().parent;checks=0
def need(v,msg):
 global checks
 if not v:raise ValueError(msg)
 checks+=1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads((P/p).read_text())
def integer(v,n):need(type(v)is int and v==n,'canonical integer')
def rat(v):
 need(type(v)is str and len(v)<=20000,'rational string');q=F(v);need(str(q)==v,'canonical fraction');return q
def box(v):
 need(type(v)is list and len(v)==2,'interval shape');a,b=map(rat,v);need(a<=b,'ordered interval');return a,b
def time(v,cap):need(type(v)in(int,float)and math.isfinite(v)and 0<v<cap,'positive time')
def mem(v):need(type(v)is int and 0<v<=384*1048576,'literal RSS')
def validate(r,a,w,receipt,inputs,old,prior):
 need(r['status']=='COMPLETE_NEW_QUARTIC_SPECTRAL_ESTIMATOR'and a['status']=='ACCEPTED_NEW_QUARTIC_SAVED_DATA_BOUND_ONCE','status');need(w['status']=='COMPLETE_NEW_QUARTIC_ONLY','worker status');need(a['once']is True and receipt['pass']is True and receipt['failure']is None,'once acceptance');integer(receipt['returncode'],0)
 for k,v in [('choices',2),('events',97),('majorant_candidates',60),('new_residual_moment_terms',112),('native_oracle_calls',0),('native_moments_recomputed',0),('old_trials_recomputed',0)]:integer(r[k],v)
 need(a['schema']['status']=='PASS_INDEPENDENT_QUARTIC_ARITHMETIC'and a['schema']['native_moment_replay']is False and a['schema']['quartic_arithmetic_reconciled']is True,'independent scope');integer(a['schema']['events'],97);integer(a['schema']['count'],2)
 time(a['external_seconds'],30);time(receipt['seconds'],29.5);time(w['seconds'],29);time(r['seconds'],29);need(r['seconds']<=w['seconds']<=receipt['seconds']<=a['external_seconds'],'chronology')
 for v in [a['external_rss_bytes'],a['sampled_whole_tree_peak'],receipt['sampled_whole_tree_peak'],w['rss_bytes']]:mem(v)
 need(a['sampled_whole_tree_peak']==receipt['sampled_whole_tree_peak'],'tree match');need(len(r['rows'])==2,'row census')
 for j,(mode,row)in enumerate(zip(['residual','variational'],r['rows'])):
  need(row['mode']==old['rows'][j]['mode']==prior['rows'][j]['mode']==mode,'same mode');need(inputs[mode]['nominal']==old['rows'][j]['nominal']==prior['rows'][j]['nominal'],'unchanged nominal')
  need(row['old_alpha']==inputs[mode]['old_alpha']==prior['rows'][j]['alpha_interval'],'same old interval');need(row['status']=='INDETERMINATE_SIGN','honest result')
  for k in ['E_upper','F_upper','error_upper','trial_a_upper','trial_b_upper']:need(rat(row[k])>=0,'nonnegative upper')
  lo,hi=box(row['intersection']);nl,nh=box(row['new_alpha']);ol,oh=box(row['old_alpha']);need(lo==max(nl,ol)and hi==min(nh,oh),'exact intersection');need(lo<=0<=hi,'indeterminate contains zero');box(inputs[mode]['nominal'])

def main():
 imports=rd('IMPORTS.json')
 for name,e in imports.items():need(sha(P/name)==e['sha256'],'import '+name)
 r=rd('packet/RESULT.json');a=rd('packet/ROOT_ACCEPTANCE.json');w=rd('packet/WORKER_COMPLETE.json');receipt=rd('packet/RECEIPT.json');bind=rd('packet/BINDING.json');rf=rd('packet/ROOT_FREEZE.json');wf=rd('packet/RUNTIME_FREEZE.json');inputs=rd('packet/INPUTS.json');old=rd('upstream/degree20/result.json');prior=rd('upstream/posterior20/result.json')
 need(a['result_sha256']==w['result_sha256']==a['schema']['result_sha256']==sha(P/'packet/RESULT.json'),'result hash chain');need(a['worker_freeze']==w['runtime_sha256']==receipt['worker_freeze']==rf['worker_freeze']==sha(P/'packet/RUNTIME_FREEZE.json'),'worker chain');need(a['root_freeze']==sha(P/'packet/ROOT_FREEZE.json'),'root chain')
 need(wf['execution_enabled']is True and rf['execution_enabled']is True,'activated sources')
 names={'WORKER_COMPLETE.json','RESULT.json','EVENTS.ndjson','residual.json','STARTED.json','INPUTS.json','variational.json','PARTIAL.json'};need(set(a['output_hashes'])==names,'eight outputs');need(a['schema']['output_hashes']==a['output_hashes'],'schema output closure')
 for n in names:need(sha(P/'packet'/n)==a['output_hashes'][n],'output hash')
 start=rd('packet/STARTED.json');need(start['runtime_sha256']==a['worker_freeze']and start['binding_sha256']==w['binding_sha256']==sha(P/'packet/BINDING.json')and start['output']==rf['authorization']['output']and start['no_retry']is True,'start binding')
 part=rd('packet/PARTIAL.json');integer(part['completed'],2);time(part['seconds'],29);need(part['seconds']<=r['seconds'],'final partial time')
 # Compact copied family metadata; original event stream is not parsed.
 for name in ['degree20','posterior20','high']:
  spec=bind[name];aa=rd('upstream/'+name+'/acceptance.json');ww=rd('upstream/'+name+'/worker.json');rr=rd('upstream/'+name+'/receipt.json');result=rd('upstream/'+name+'/result.json')
  for k in ['acceptance','root_freeze','result','worker','receipt']:need(sha(P/'upstream'/name/(k+'.json'))==spec['files'][k]['sha256'],'bound upstream')
  need(aa['status']==spec['expected']['acceptance']and ww['status']==spec['expected']['worker']and result['status']==spec['expected']['result'],'upstream status');need(aa['result_sha256']==ww['result_sha256']==spec['files']['result']['sha256'],'upstream result');need(aa['worker_freeze']==ww['runtime_sha256']==rr['worker_freeze']==spec['worker_freeze'],'upstream worker')
  need(aa['once']is True and rr['pass']is True and rr['failure']is None,'upstream acceptance');integer(rr['returncode'],0)
  for value,cap in [(ww['seconds'],spec['expected']['worker_seconds']),(rr['seconds'],spec['expected']['root_seconds']),(aa['external_seconds'],spec['expected']['external_seconds'])]:time(value,cap)
  for value in [ww['rss_bytes'],aa['external_rss_bytes'],aa['sampled_whole_tree_peak']]:mem(value)
 hb=rd('upstream/high/binding.json');pb=rd('upstream/posterior20/binding.json')
 for k in ['events','result']:need(hb['degree20']['files'][k]==pb['files'][k]==bind['degree20']['files'][k],'same original source')
 validate(r,a,w,receipt,inputs,old,prior)
 for j,mode in enumerate(['residual','variational']):need(rd('packet/'+mode+'.json')==r['rows'][j],'mode copy')
 mutants=0
 for tag in ['claim','bool','rss','reverse','intersection','nominal']:
  rr=copy.deepcopy(r);aa=copy.deepcopy(a);ww=copy.deepcopy(w);ii=copy.deepcopy(inputs)
  if tag=='claim':rr['rows'][0]['status']='POSITIVE_CERTIFICATE'
  elif tag=='bool':rr['choices']=True
  elif tag=='rss':ww['rss_bytes']=True
  elif tag=='reverse':rr['rows'][0]['new_alpha'].reverse()
  elif tag=='intersection':rr['rows'][0]['intersection']=['1','2']
  else:ii['residual']['nominal']=['0','0']
  try:validate(rr,aa,ww,receipt,ii,old,prior)
  except ValueError:mutants+=1
  else:raise ValueError('surviving coherent mutant '+tag)
 # Tiny exact synthetic factor/quotient identity, no accepted moments used.
 for t,u in [(F(1),F(1)),(F(2),F(8)),(F(16),F(16))]:
  d=F(1,4);B=1/(d*t*t*u*u);A=B*(1/d+2/t+2/u)
  def mul(p,q):
   z=[F(0)]*(len(p)+len(q)-1)
   for i,x in enumerate(p):
    for j,y in enumerate(q):z[i+j]+=x*y
   return z
  p=[-d,F(1)]
  for z in [t,t,u,u]:p=mul(p,[-z,F(1)])
  p=mul(p,[B,A]);p[0]+=1;need(p[:2]==[0,0],'quotient factor cancellation')
  for x in [d,F(3),F(32)]:need(sum(c*x**i for i,c in enumerate(p[2:]))-1/x**2==(x-d)*(x-t)**2*(x-u)**2*(A*x+B)/x**2>=0,'exact majorant')
 print(json.dumps({'status':'PASS_COMPACT_ONLY','checks':checks,'semantic_mutants':mutants,'native_or_event_arithmetic_replays':0}))
if __name__=='__main__':main()

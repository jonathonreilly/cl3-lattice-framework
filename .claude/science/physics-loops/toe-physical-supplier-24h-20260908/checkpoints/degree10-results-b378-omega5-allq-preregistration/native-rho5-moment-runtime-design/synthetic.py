"""Full worker/schema synthetic adapter control; native high-tail routine replaced explicitly."""
import tempfile,json,sys,types
from pathlib import Path
from fractions import Fraction as F
import core,worker

def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,default=str)+'\n')
def run():
 core.tail=lambda kind:(F(1,100),F(1,10**40));checks=0
 with tempfile.TemporaryDirectory()as t:
  p=Path(t);out=p/'out';out.mkdir();families={};pi=core.machin();first=((F(3,2**65),F(7,2**66)),(F(1,5),F(1,5)));tot=(F(0),F(0));panels=[]
  for j in range(67):v=(F(1,1000),F(1,1000)+F(1,10**40));tot=core.add(tot,v);panels.append({'panel':j-64,'values':[v,v],'cumulatives':[tot,tot],'value':v,'cumulative':tot})
  rows=[]
  for k in ['cminus','mu','nu']:rows.append({'interval':core.finish(tot,core.low(k,first),core.tail(k),pi,core.RAD4[k])})
  for key in ['dual','nu']:
   d=p/key
   for j,x in enumerate(panels):write(d/f'PANELS/{j:02d}.json',x)
   result={'rows':rows[:2]}if key=='dual'else dict(rows[2],middle=tot)
   write(d/'RESULT.json',result)
   if key=='dual':tail={'low_intervals':[core.low(k,first)for k in ['cminus','mu']],'high_partials':['1/100']*2,'high_remainders':[str(F(1,10**40))]*2,'quadrature_radii':[core.RAD4[k]for k in ['cminus','mu']]};write(d/'TAILS.json',tail)
   else:write(d/'TAIL.json',{'low_interval':core.low('nu'),'high_partial':'1/100','high_remainder':str(F(1,10**40)),'quadrature_radius':core.RAD4['nu']})
   f={n:str(d/(n+'.json'))for n in ['worker_freeze','root_freeze','post_worker_freeze','post_root_freeze','post_result']}
   for path in f.values():write(Path(path),{})
   f.update(result=str(d/'RESULT.json'),acceptance=str(d/'acceptance.json'),post_acceptance=str(d/'post_acceptance.json'),acceptance_status='ACCEPTED_TOY',post_status='POST_TOY')
   a={'status':'ACCEPTED_TOY','result_sha256':worker.sha(f['result']),'worker_freeze':worker.sha(f['worker_freeze']),'root_freeze':worker.sha(f['root_freeze'])};write(Path(f['acceptance']),a)
   write(Path(f['post_acceptance']),dict(a,status='POST_TOY',post_result_sha256=worker.sha(f['post_result']),post_worker_freeze=worker.sha(f['post_worker_freeze']),post_root_freeze=worker.sha(f['post_root_freeze'])));families[key]=f
  endpoints=[{'s':str(x)}for x in first[0]];write(p/'geometry.json',{'nodes':[{'id':0,'panel':-64,'endpoint_ids':[0,1],'t_interval':first[0]}],'endpoints':endpoints});cr=[]
  for i,e in enumerate(endpoints):path=p/f'ORACLES/{i:04d}.json';write(path,{'A':first[1],'s':e['s'],'catalog_endpoint':e});cr.append({'id':i,'gate':'PASS','path':f'ORACLES/{i:04d}.json','sha256':worker.sha(path)})
  write(p/'catalog.json',{'rows':cr});binding={'families':families,'geometry':str(p/'geometry.json'),'catalog_result':str(p/'catalog.json'),'inputs':{str(x):worker.sha(x)for x in p.rglob('*')if x.is_file()}}
  write(p/'binding.json',binding);worker.run(binding,out);r=json.loads((out/'RESULT.json').read_text());assert len(r['rows'])==3;checks+=1
  # Receipt schema uses actual worker-produced fixture, not hand-invented events.
  schema_path=Path(__file__).parent.parent/'native-rho5-moment-root-review/schema.py';m=types.ModuleType('toy_schema');exec(compile(schema_path.read_bytes(),str(schema_path),'exec'),m.__dict__)
  auth={};write(out/'STARTED.json',auth);seconds=r['seconds']+1;write(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_RHO5_ONLY','runtime_sha256':'w','binding_sha256':worker.sha(p/'binding.json'),'result_sha256':worker.sha(out/'RESULT.json'),'seconds':seconds,'rss_bytes':10000});rf={'authorization':auth,'worker_freeze':'w','binding_sha256':worker.sha(p/'binding.json'),'binding_path':str(p/'binding.json')};m.check(out,rf,seconds+1);checks+=1
  # Rehashed event corruption must fail despite unchanged census.
  ep=out/'EVENT_0003.json';prior=ep.read_text();write(ep,{'stage':'load_panel','kind':'cminus','panel':True})
  try:m.check(out,rf,seconds+1)
  except ValueError:checks+=1
  else:raise AssertionError('event mutant')
  ep.write_text(prior)
  original_result=(out/'RESULT.json').read_text();r['node_integrands_recomputed']=False;write(out/'RESULT.json',r);w=json.loads((out/'WORKER_COMPLETE.json').read_text());w['result_sha256']=worker.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',w)
  try:m.check(out,rf,seconds+1)
  except ValueError:checks+=1
  else:raise AssertionError('bool scope mutant')
  (out/'RESULT.json').write_text(original_result);w['result_sha256']=worker.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',w)
  write(out/'STARTED.json',{'bad':True})
  try:m.check(out,rf,seconds+1)
  except ValueError:checks+=1
  else:raise AssertionError('authorization mutant')
  bad=dict(binding);bad['inputs']=dict(binding['inputs']);bad['inputs'][families['dual']['result']]='0'*64;other=p/'bad';other.mkdir()
  try:worker.run(bad,other)
  except ValueError:assert(other/'FAILURE.json').exists();checks+=1
  else:raise AssertionError('input mutant')
 print(json.dumps({'status':'PASS','checks':checks,'full_worker_synthetic':True,'tail_replaced_with_toy':True,'actual_inputs_loaded':0}))
if __name__=='__main__':run()
